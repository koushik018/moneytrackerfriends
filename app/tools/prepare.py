"""Finish the generated Android project: icons, splash, colours, permissions, version.
Run from app/ after `npx cap add android` and `npx cap sync android`:  python3 tools/prepare.py <build-number>"""
import os, re, sys, glob
from PIL import Image

RES = 'android/app/src/main/res'
BG = (10, 15, 11)                       # app background #0a0f0b
build = int(sys.argv[1]) if len(sys.argv) > 1 else 1
icon = Image.open('../icon-512.png').convert('RGBA')
mask = Image.open('../icon-maskable-512.png').convert('RGBA')

# launcher icons (legacy + adaptive foreground)
for d, n in {'mdpi': 48, 'hdpi': 72, 'xhdpi': 96, 'xxhdpi': 144, 'xxxhdpi': 192}.items():
    for name in ('ic_launcher.png', 'ic_launcher_round.png'):
        icon.resize((n, n), Image.LANCZOS).save(f'{RES}/mipmap-{d}/{name}')
    f = n * 108 // 48
    mask.resize((f, f), Image.LANCZOS).save(f'{RES}/mipmap-{d}/ic_launcher_foreground.png')
open(f'{RES}/values/ic_launcher_background.xml', 'w').write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#0A0F0B</color>\n</resources>\n')

# splash: dark screen with the icon in the middle
for path in glob.glob(f'{RES}/drawable*/splash.png'):
    w, h = Image.open(path).size
    img = Image.new('RGB', (w, h), BG)
    s = max(64, min(w, h) // 4)
    img.paste(icon.resize((s, s), Image.LANCZOS), ((w - s) // 2, (h - s) // 2), icon.resize((s, s), Image.LANCZOS))
    img.save(path)

# dark status / navigation bars
st = open(f'{RES}/values/styles.xml').read()
st = st.replace('<item name="android:background">@null</item>',
    '<item name="android:background">@null</item>\n        <item name="android:statusBarColor">#0A0F0B</item>\n        <item name="android:navigationBarColor">#0A0F0B</item>\n        <item name="android:windowLightStatusBar">false</item>', 1)
open(f'{RES}/values/styles.xml', 'w').write(st)

# permissions: no internet at all; camera and microphone only for the optional intruder log (the app asks only when you switch it on)
mf = 'android/app/src/main/AndroidManifest.xml'
m = open(mf).read()
m = re.sub(r'\s*<uses-permission android:name="android\.permission\.INTERNET"\s*/>', '', m)
m = re.sub(r'\s*<uses-permission android:name="android\.permission\.ACCESS_NETWORK_STATE"\s*/>', '', m)
for perm in ('POST_NOTIFICATIONS', 'VIBRATE', 'RECEIVE_BOOT_COMPLETED', 'WAKE_LOCK', 'CAMERA', 'RECORD_AUDIO', 'MODIFY_AUDIO_SETTINGS'):
    tag = f'<uses-permission android:name="android.permission.{perm}" />'
    if tag not in m:
        m = m.replace('</manifest>', f'    {tag}\n</manifest>')
# also strip them from the MERGED manifest in case a library adds them
if 'xmlns:tools' not in m:
    m = m.replace('<manifest ', '<manifest xmlns:tools="http://schemas.android.com/tools" ', 1)
for perm in ('INTERNET', 'ACCESS_NETWORK_STATE'):
    m = m.replace('</manifest>', f'    <uses-permission android:name="android.permission.{perm}" tools:node="remove" />\n</manifest>')
for feat in ('android.hardware.camera', 'android.hardware.microphone'):
    tag = f'<uses-feature android:name="{feat}" android:required="false" />'
    if tag not in m:
        m = m.replace('</manifest>', f'    {tag}\n</manifest>')
# nothing is copied to Google or to another phone by Android's backup
m = re.sub(r'android:allowBackup="[^"]*"', 'android:allowBackup="false"', m)
if 'android:allowBackup' not in m:
    m = m.replace('<application', '<application android:allowBackup="false"', 1)
m = m.replace('<application', '<application android:usesCleartextTraffic="false"', 1) if 'usesCleartextTraffic' not in m else m
open(mf, 'w').write(m)

# screenshot switch: a tiny native plugin that sets / clears Android's FLAG_SECURE (also hides the app in the recent-apps view)
import json
appid = json.load(open('capacitor.config.json'))['appId']   # e.g. app.trackme.friends
pkg = appid.replace('.', '/')
jdir = 'android/app/src/main/java/' + pkg
os.makedirs(jdir, exist_ok=True)
open(jdir + '/SecureScreenPlugin.java', 'w').write("""package APPID;

import android.view.WindowManager;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;

@CapacitorPlugin(name = "SecureScreen")
public class SecureScreenPlugin extends Plugin {
    @PluginMethod
    public void setSecure(final PluginCall call) {
        final boolean on = Boolean.TRUE.equals(call.getBoolean("on", false));
        getActivity().runOnUiThread(new Runnable() {
            @Override
            public void run() {
                if (on) {
                    getActivity().getWindow().setFlags(WindowManager.LayoutParams.FLAG_SECURE, WindowManager.LayoutParams.FLAG_SECURE);
                } else {
                    getActivity().getWindow().clearFlags(WindowManager.LayoutParams.FLAG_SECURE);
                }
                call.resolve();
            }
        });
    }
}
""".replace('APPID', appid))
open(jdir + '/TextReaderPlugin.java', 'w').write("""package APPID;

import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Rect;
import android.os.Environment;
import android.util.Base64;
import com.getcapacitor.JSArray;
import com.getcapacitor.JSObject;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;
import com.google.mlkit.vision.common.InputImage;
import com.google.mlkit.vision.text.Text;
import com.google.mlkit.vision.text.TextRecognition;
import com.google.mlkit.vision.text.TextRecognizer;
import com.google.mlkit.vision.text.latin.TextRecognizerOptions;
import java.io.File;

/* reads the text in a picture on the phone (bundled ML Kit model, works offline); the picture stays in memory only */
@CapacitorPlugin(name = "TextReader")
public class TextReaderPlugin extends Plugin {
    private TextRecognizer reader;

    @PluginMethod
    public void read(final PluginCall call) {
        String img = call.getString("image", "");
        int comma = img.indexOf(',');
        if (comma >= 0) img = img.substring(comma + 1);
        Bitmap bmp = null;
        try {
            byte[] bytes = Base64.decode(img, Base64.DEFAULT);
            bmp = BitmapFactory.decodeByteArray(bytes, 0, bytes.length);
        } catch (Exception e) { bmp = null; }
        if (bmp == null) { call.reject("The phone could not open that picture."); return; }
        if (reader == null) reader = TextRecognition.getClient(TextRecognizerOptions.DEFAULT_OPTIONS);
        final Bitmap pic = bmp;
        final int w = pic.getWidth(), h = pic.getHeight();
        reader.process(InputImage.fromBitmap(pic, 0))
            .addOnSuccessListener(text -> {
                JSArray lines = new JSArray();
                for (Text.TextBlock b : text.getTextBlocks()) {
                    for (Text.Line l : b.getLines()) {
                        JSObject o = new JSObject();
                        o.put("t", l.getText());
                        Rect r = l.getBoundingBox();
                        if (r != null) { o.put("x", r.left); o.put("y", r.top); o.put("w", r.width()); o.put("h", r.height()); }
                        lines.put(o);
                    }
                }
                pic.recycle();
                JSObject res = new JSObject();
                res.put("lines", lines); res.put("w", w); res.put("h", h);
                call.resolve(res);
            })
            .addOnFailureListener(e -> { pic.recycle(); call.reject("Could not read the text."); });
    }

    /* delete the temporary file the camera wrote for "Take a photo" */
    @PluginMethod
    public void clean(PluginCall call) {
        File[] dirs = { getContext().getCacheDir(), getContext().getExternalCacheDir(), getContext().getExternalFilesDir(Environment.DIRECTORY_PICTURES) };
        for (File d : dirs) {
            if (d == null) continue;
            File[] fs = d.listFiles();
            if (fs == null) continue;
            for (File f : fs) {
                String n = f.getName();
                if (f.isFile() && n.startsWith("JPEG_") && n.endsWith(".jpg")) f.delete();
            }
        }
        call.resolve();
    }
}
""".replace('APPID', appid))
open(jdir + '/MainActivity.java', 'w').write("""package APPID;

import android.os.Bundle;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        registerPlugin(SecureScreenPlugin.class);
        registerPlugin(TextReaderPlugin.class);
        super.onCreate(savedInstanceState);
        try {
            android.webkit.WebSettings ws = getBridge().getWebView().getSettings();
            ws.setSupportZoom(false);
            ws.setBuiltInZoomControls(false);
            ws.setDisplayZoomControls(false);
        } catch (Exception e) { }
    }
}
""".replace('APPID', appid))

# version: every build is an update of the same app (same signing key keeps your data)
g = 'android/app/build.gradle'
b = open(g).read()
b = re.sub(r'versionCode \d+', f'versionCode {build}', b)
ver = open('version.txt').read().strip()
b = re.sub(r'versionName "[^"]*"', f'versionName "{ver}"', b)
# sign every build with the SAME private key, which lives only in GitHub Secrets, so a new APK installs over the old one and keeps its data
ks = os.environ.get('KEYSTORE_PATH', '').replace('\\', '/')
if not ks or not os.path.exists(ks):
    raise SystemExit('KEYSTORE_PATH is not set - add the signing secrets to the repository')
if 'signingConfigs' not in b:
    sign = ("    signingConfigs {\n        debug {\n            storeFile file('" + ks + "')\n            storePassword System.getenv('KEYSTORE_PASSWORD')\n"
            "            keyAlias System.getenv('KEY_ALIAS')\n            keyPassword System.getenv('KEY_PASSWORD')\n        }\n    }\n")
    b = b.replace('android {\n', 'android {\n' + sign, 1)
# offline text reader for screenshots (the model ships inside the APK; no Google Play download, no internet)
if 'com.google.mlkit:text-recognition' not in b:
    b = re.sub(r'\ndependencies \{\n', "\ndependencies {\n    implementation 'com.google.mlkit:text-recognition:16.0.1'\n", b, count=1)
    if 'com.google.mlkit:text-recognition' not in b:
        raise SystemExit('could not add the text reader dependency')
# smaller APK: the text reader's native code only for phones (64-bit and older 32-bit ARM), not for PC emulators (x86), and stored compressed
if 'abiFilters' not in b:
    b = b.replace('defaultConfig {\n', 'defaultConfig {\n        ndk { abiFilters "arm64-v8a", "armeabi-v7a" }\n', 1)
if 'useLegacyPackaging' not in b:
    b = b.replace('android {\n', 'android {\n    packaging { jniLibs { useLegacyPackaging = true } }\n', 1)
if 'abiFilters' not in b or 'useLegacyPackaging' not in b:
    raise SystemExit('could not set the APK size options')
open(g, 'w').write(b)
print('prepared build', build)
