# TrackMe – features and money rules

This file describes how the app works. It contains **no personal data**. All balances, entries,
investments and settings live only on the phone (app storage).
Use **Settings → Backup (JSON)** to keep a copy and **Restore** to move it to another phone or app.

## Accounts
- **Types:** bank, credit card, cash, wallet, investment platform, family/others (outside money).
- **Balance** = opening balance + every recorded entry. Reverting an entry restores the balance;
  restoring it applies it again.
- **Balance check:** type what the bank app shows. If there are no entries yet it sets the starting
  balance; otherwise it adds a "Balance correction" entry.
- **Free to spend** = balance − minimum balance − money on hold for IPOs.

## Payment methods
- UPI apps (PhonePe, BHIM, GPay, Paytm, bank UPI), debit cards, credit cards, wallets, cash.
- **Modes:** person (P2P UPI), shop QR, card tap/swipe, online/app.
- **Best way to pay:** suggests the method with the most cashback for the mode and amount, skipping
  inactive accounts and investment platforms.
- **UPI daily limit** per bank, plus per-card limits (ATM, POS, online, tap).

## Cashback
- Rule per method: % of the amount, max per payment, max per month, which modes count.
- Cashback is added to each eligible payment automatically and stops at the monthly cap.
- **Earned so far:** cashback earned this month before tracking started; it counts toward the cap.
- **Add reward:** one-off rewards (scratch cards, offers). **Mark received:** when it reaches the bank.
- Debit-card cashback and the same bank's UPI are separate methods with separate rules.

## Credit cards
- Limit, statement day, due day, minimum due %. Shows used, available, statement amount, minimum due
  and due date, and alerts before the due date.
- Pay bill = transfer from a bank to the card.
- **Late fee / interest / charges:** record the fee as an *expense on the card* (category Bills or
  Fees), then record the payment as a *transfer* from the bank to the card. Recording only the
  payment would make the card look as if it has more credit than its limit.

## Notifications (Android app)
- Own screen (Settings → Notifications): on/off per type, time of day, card-bill lead days, the list of what is coming up,
  and how it works. Each type has its own "days before" buttons (each one switched on is one notification), the monthly check has a day of the month, the weekly check a day and time. Also: unused cashback cap near month end, a monthly balance check, and an optional Sunday weekly nudge. Up to 60 upcoming notifications are scheduled and rebuilt whenever data changes. No amounts are shown.

- Event alerts fire right after you record something: a UPI payment that reaches the bank's daily limit (warn at 80 / 90 / 100 %), or a payment that leaves a bank or wallet below its minimum balance. The app only knows what you record.
- The weekly check is an optional quiet nudge on a day and time you pick; it never shows amounts.

## Cost in every period
- Autopay / fixed costs can repeat weekly, monthly, every 3 months, yearly or once.
- Totals are shown per Day / Week / Month / Quarter / Year, plus "Due this month (exact)" for what really falls due in the calendar month.
- Each item decides which periods it counts in (for example a yearly bill can stay out of the monthly average but remain in the yearly total).
- Rows show the yearly cost of each item and which periods it is left out of.

## Card benefits (Benefits tab in the wallet)
- Note any perk a card or bank gives: OTT, gym, spa, health check-up, cab or gift vouchers, lounge. Each has a worth, how often it comes (one time, monthly, quarterly, yearly), how many times per period, and an optional valid-till date.
- Tap **Claim** when you use it (**Undo** to take it back). The card shows how many are claimed this period and how much value is still unused.
- **Year in benefits:** perks you claimed + cashback recorded – the card's annual fee = what the card gave you, per card and in total, plus perks that went unused. It opens by itself around 20 December and any time from the Benefits tab.
- Notifications: a benefit that is not claimed is flagged before its period or valid-till date ends (days before are editable), and a note on 28 December that the year summary is ready.

## Gift cards (Gifts tab)
- Add any gift card, voucher or store balance you were given. Only the amount is needed; name, where it is held (Amazon Pay, Flipkart…), date received, who gave it, a valid-till date and a note are optional. Never type card codes or PINs.
- **Spent** also writes a History entry ("paid from gift balance") with what for, category and date; reverting it in History gives the balance back.
- Gift balance is kept apart: it is not in bank balances, Money available or net worth.
- **Spent** lowers the gift balance only (nothing changes in the bank). **Move to bank** is a manual record for when the money really reached an account: the gift balance goes down and that account goes up. **Undo last** reverses the latest entry, including the bank credit.
- With a valid-till date you get reminders before it expires (days before are editable), only while balance is left.

## Amazon Pay
- Amazon Pay balance (gift cards, cashback) is tracked in Gifts; spending it appears in History as paid from gift balance. Amazon Pay UPI can be linked to any bank from UPI → Link a bank.

## PayPal (linked only)
- Add PayPal and tick the banks and cards linked to it. No payments or balance are tracked and it is not part of net worth; record the payment on the card or bank that was charged.
- In India PayPal is for international payments only.

## Reminders, autopay, EMI, people
- Monthly reminders (with an amount); "deposit and move it out again" reminders that tick themselves
  when the deposit is recorded.
- Fixed costs and autopay (recorded automatically on the due date), EMIs, repayment schedules
  (equal or custom per month), lent / owed per person, budgets per category.
- Calendar file (.ics) export for phone reminders.

## Investments (always private)
- Separate tab, opened only with a PIN – the separate **investments PIN** if set, otherwise the app
  PIN. Fingerprint never opens it.
- **Platform value** = cash balance + holdings. Money on hold for an IPO stays in the balance.
- **Withdraw** to a bank / **Add money** from a bank (transfers; net worth does not change).
- **Holdings:** stocks, mutual funds, gold, bonds (invested + current value, updated by hand),
  FD and RD (calculated every day).
- **FD:** quarterly compounding by default; value grows by days/365.
- **RD:** each deposit at the start of its month; amounts can differ month to month; an RD can be
  saved before it starts ("Start today" when it begins).
- **Other platforms:** add any platform by name (Zerodha, Upstox, Paytm Money …). It gets its own card with an animated first-letter mark; platforms that share a first letter get different colours and ring styles. A logo can be uploaded (kept as it is, or restyled round with a soft glow).
- **Auto-refund (running account settlement):** unused platform cash goes back to the primary bank on
  a monthly/quarterly cycle. Reminder two days before; "Record refund" moves the free balance and
  rolls the date forward. Money on hold is never refunded.


## Deposit rule (any bank, card or wallet)
- In Edit / Add account, or in the Edit screen of any card or payment method (it belongs to the account the card pays from), tick **A deposit is needed to keep an offer** and enter the amount, the day of the month and what it keeps active. You get a monthly reminder (days before are editable under Notifications); Record asks whose money it was and what happened after, so totals stay right. Untick it to remove the reminder.


## IPO
1. Apply: name, amount, money from (platform balance or bank UPI block), schedule dates
   (applied, close, allotment, funds unblock/debit, listing).
2. The amount goes **on hold**: the balance still shows it (as the bank SMS does) but it is not free
   to spend, withdraw or use for another IPO. Net worth does not change.
3. Allotment day: alert with **Allotted** / **Not allotted**.
   - Allotted: the amount actually debited leaves the account and becomes a stock holding in the
     platform; any rest of a partial allotment is released.
   - Not allotted: the hold is released.

## Net worth
- Spendable money + investments + money others owe you − card dues − money you owe.
- A daily snapshot builds the "over time" chart.

## Security and privacy (Settings → Security & privacy)
- **The Security & privacy page opens only with your details passphrase** (set it up first from Settings). The "someone tried your lock" banner still shows on Home, but the intruder log opens only with the passphrase.
- **Changing a lock asks for the current one first** (app PIN, investments PIN, details passphrase). Every PIN and passphrase box has a Show / Hide button and a red / orange / green strength bar. Forgot the app PIN: type the recovery key to set a new one (if no recovery key was made, the only way in is to erase and restore a backup).
- **Intruder photos:** tap to open full screen, pinch or double-tap to zoom, swipe between photos, and save a copy to the phone (a saved copy is not locked).
- **Locks:** app PIN, investments PIN and the details passphrase. Three wrong tries lock that lock for 1 minute, then 5, 30 and 60 minutes. Nothing is ever erased.
- **Details vault:** UPI IDs (any number, per app), account last 4, IFSC, linked mobile, optional customer ID and branch; card last 4, expiry and network. Locked with its own passphrase (AES-256-GCM, key from PBKDF2); opens only after you unlock, locks when you leave the app or after 5 minutes, Copy buttons clear the clipboard after 30 seconds. Full account or card numbers, PINs, CVV, passwords and OTPs are refused.
- **Encrypted backups:** every backup is locked with a password. Optional recovery key: a spare code shown once to write on paper; either the password or the code opens the file. Old plain backups still restore. The intruder log is not part of a backup.
- **Screenshots:** a switch to allow or block screenshots, screen recording and the recent-apps preview (Android app).
- **Intruder log:** after 2 wrong tries in a row on any lock, up to 3 front-camera photos (3 seconds apart) and/or 15 seconds of audio, each switch separate and off by default. Locked with the details passphrase, shown only after entering it, with no notification; a banner appears inside the app. 60 days or 100 MB, delete any time.
- **No internet:** the Android app has no internet permission, fonts are bundled, Android cloud backup is off, and the build fails if a forbidden permission appears.

## Security (earlier)
- App PIN (PBKDF2), fingerprint/face unlock (WebAuthn, device only), auto-lock after a minute in the
  background, hide-all-amounts eye, private accounts, confirmation popups above a chosen amount.
- No account numbers, card numbers or UPI IDs are ever asked for.

## Card carousel (smoothness)
- The finger moves the cards 1:1; there is no fling, so nothing fights the animation. One swipe moves exactly one card (a quick flick or a drag past a fifth of a card); a short drag springs back. The card settles in about a third of a second with one soft tick as it clicks into place. The tilt, size and dimming run as a CSS scroll-driven animation on the graphics side, so they cannot lag.
- Idle logo animations pause while you swipe, and the blur behind each card logo was removed, to keep the swipe light with many cards.

## App behaviour
- Installable (PWA), works offline, setup form survives leaving the app, floating calculator
  (percent maths, "Use as amount"), haptics on Android, themes, Samsung-style wallet: swipe cards,
  drag down for all cards, double-tap to flip for details.

## Repository rules
- Never put balances, amounts, dates of personal deposits, names or bank details in code, commit
  messages or pull-request descriptions. Presets hold only public product rules.
