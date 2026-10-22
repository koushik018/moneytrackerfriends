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

## Received money
- When you record money received, pick the bank or cash account and **how it came**: the UPI apps linked to that bank come first (PhonePe, GPay …), then other UPI apps, bank transfer, cash deposit, cheque or other. History shows it next to the entry.

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

## Upcoming costs and events (Plan → Upcoming)
- Note anything coming up (trip, gift, fee, festival) with a date, an optional cost and a category. Totals for the next 30 days and 3 months, and what is left free after the next 30 days.
- Each item has its own reminders: on the day, or 1, 2, 3, 5, 7 or 14 days before, any mix. They show on Home and as phone notifications (switch all off in Settings → Notifications). Mark Done when it has happened.

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


## IPO (Investments → IPOs)
1. **Plan or apply.** Name, lot size, price band, bidding open / close, allotment, unblock / debit
   and listing dates, the bank the money is blocked from, and where the shares go.
   - **Save as plan** before bidding opens: no money moves; you are reminded when bidding opens.
   - **Apply now** puts the money **on hold** (UPI block). The balance still shows it, as the bank
     SMS does, but it is not free to spend, withdraw or use for another IPO.
2. **Several bids per IPO.** Each bid has a category, lots (− / + stepper), a price or
   **At cut-off price**; shares and amount are worked out (lots × lot size × price).
   - Categories: Regular (retail, up to ₹2,00,000), Employee (up to ₹5,00,000),
     Shareholder (up to ₹2,00,000), HNI (above ₹2,00,000, up to ₹5,00,000).
     Limits can be changed per IPO under **Category limits**.
   - HNI: the lots needed to cross ₹2,00,000 are filled in, cut-off is not allowed, and a warning
     says HNI applications cannot be cancelled or lowered.
   - Warnings for prices outside the band, more than 3 retail bids, or a category over its limit.
3. **Funds check** while filling the form: free in the bank now, free by the closing day (money on
   the way counted on its expected date), and the shortfall.
4. **Find the money**: add one or more sources (**+ Add another source**):
   - another bank, wallet or cash (moved now);
   - unused Groww cash (withdraw first: **Standard** or **Instant**, with charges);
   - sell or redeem an investment (shares, fund, gold, FD; full or part, charges, working days);
   - borrow from a person (recorded in People, not income).
   Other IPOs still on hold in the same bank are listed as not counted yet.
5. **What if** table: 0, 1, 2 … lots allotted → debited, released, free after the unblock day,
   and whether the **next planned IPO** (for example the one opening the day after) is covered.
6. **Result.** Mark how many lots each bid got and the final issue price; the debit and release
   are worked out. Then: **Yes – it is done** (pick the account) or **Not yet** (you are reminded on
   the debit day and the next working day, because it can be a day late).
   The debit becomes a stock holding (with the number of shares) in the platform.
7. **Leftover.** If you brought money in, what is free again is shown with rows already filled
   with where it came from (lenders first). Change, split, add accounts, send all to one account,
   or keep it. Paying a lender is recorded in People.
8. Older IPOs saved before this version keep working (amount-based result).
9. **The money is always blocked in a bank** (UPI mandate). The Groww balance is no longer offered as
   the place an IPO blocks money; Groww cash is withdrawn to the bank first (Find the money).
   The debit on allotment comes from that bank and becomes shares in the platform's holdings;
   the rest is released back to the same bank.
10. **Change bank** on an IPO card fixes an older entry saved against the Groww balance: pick the
    bank, optionally record the Groww → bank withdrawal that paid for it (amount and date), and
    record a missing debit again. Balances after the change are shown before saving.
11. Reverting an IPO's debit in History puts the IPO back to “confirm the debit” and takes its
    shares out of holdings; restoring it puts them back.
12. **Where the IPO money came from** (Change bank): pick one of three:
    - *Already in this bank* – nothing moves;
    - *Withdrawn from Groww or another investment to this bank* – enter the amount and date;
    - *Borrowed from a person* – enter their name and the amount; it is recorded in Lent & owed.
    The chosen source is also listed under the IPO as a source for leftover money.

13. The bank pickers in the IPO form and in Change bank end with **+ Add another bank…**, which opens
    the Add guide on the bank box, so a bank you have not set up yet can be added without leaving the flow.

## Money on the way
1. A withdrawal or sale that lands later: from (Groww, a bank or an investment), to (bank),
   amount, charges, and **Standard**, **Instant** or **My own date**.
   - Standard: processed the next working day, around 10–11 am. A Friday-evening, Saturday or
     Sunday request arrives on Monday; market holidays are skipped.
   - Instant: about 5 minutes (cannot be cancelled, may have a fee).
   - Sale of shares: T+1. Funds, gold and FDs: the working days you set.
2. **Withdraw** on Groww asks when it reaches the bank (Already there / Standard / Instant).
   **Sell / redeem** on a platform with holdings creates one for a holding.
3. Nothing changes in balances until you tap **Arrived** (amount, bank, time). It is recorded as a
   move between your own accounts; charges are a small expense. Groww cash already asked for is
   not counted as free.
4. Notification at the expected time with **Arrived** / **Not yet** buttons, and again the next
   working day. Tapping Arrived opens the confirm screen after you unlock – nothing is recorded
   from the lock screen.

## Market holidays (Investments → IPOs → Holidays)
1. The 2026 exchange holidays come with the app (it has no internet). Add or remove days; restore
   the list any time. The 2027 list is added when the exchanges announce it (usually December).

## IPO notifications
- Bidding opens (9 am) and the last day to bid (10 am) for a planned IPO.
- Allotment (days before you choose, and 10 am on the day), plus a next-day nudge if not marked.
- Debit / unblock day, and the next working day if not confirmed.
- Listing day at 7, 8 and 9 am: "Listing at 10:00. Check Groww to trade or keep."

## Add flow (first-run guide and **+ Add** in the app)
1. One guide with **seven boxed steps**, opened one at a time: 1 UPI apps, 2 Bank accounts,
   3 Cards (Debit / Credit tabs, virtual cards included), 4 Wallets, 5 Cash, 6 Investments, 7 Others.
   - Everything starts **unticked**. Tick an item to open its few fields; **Done – next** opens the
     next box. A badge shows how many you are adding or already have. The **?** on a box explains it.
   - The same guide opens from **+ Add** (Home wallet, Accounts page); items already added show as
     ✓ and are not offered again. Edit an existing one with its own **Edit** button.
2. **Banks**: balance, optional limits, then **Linked UPI apps** (all unticked) and
   **+ Add custom UPI app**, which adds the app to every bank's list and gives it its own card.
   The UPI cards show which banks each app is linked to.
3. **Cards**: debit cards pick the bank they spend from; credit cards take limit, available amount,
   statement day and due day. Virtual cards use the same forms (tick “Virtual card”).
4. **Wallets** show whether they live inside a UPI app or are separate (like Mobikwik).
5. **Cash boxes**: Personal, Office, Family or your own. Each has **Include in my net worth**
   (on for Personal, off for the others). Boxes that are off are left out of the totals and
   shown separately on the net worth page. Change it later: account → Edit.
6. **Investments**: platform balance (private); FD/RD for Stable Money; holdings are added on the
   platform card afterwards.
7. **Others**: anything else, plus PayPal and gift cards (in-app only).
8. What you type in the first-run guide survives switching apps and closing the app.
9. Payment-method form: friendly kind names (UPI app, Debit card, Credit card, Wallet, Cash), the
   “pays from” list no longer offers “Family / others”, and editing a wallet no longer turns it
   into a UPI method.

## Themed dropdowns
- Every dropdown and suggestion list opens a sheet in the app's own colours (readable, large tap
  targets, search when long, ✓ on the current choice) instead of the black Android picker.
- Lists such as UPI apps accept your own entry (**Use “…”**). Back button, Esc and tapping outside close it.

## No zoom
- Pinch-zoom and double-tap zoom are switched off (page, browser and Android WebView), so the app
  keeps its own size.

## Tips and guides
- First-time tip boxes on Accounts and IPOs (**Got it** or **Turn tips off**), a **?** on the
  wallet, Accounts and IPO headers, and a **Tips and guides** switch in Settings to turn all of
  them off or show them again.

## Home stack view
- The last stacked card no longer overlaps the Online money / Cash in hand tiles.

## Card and bank details on the card back
- Flip a card (double-tap): its back shows one line from your **Details vault**: the last 4 digits,
  expiry and network for debit and credit cards; the account last 4 digits, IFSC and branch for banks.
- Shown only while the details vault is unlocked. Locked, the line shows **Unlock** (asks for the
  details passphrase). It hides again after 5 minutes idle, when you leave the app, or on Lock.
- Nothing is stored in the clear: the data stays inside the encrypted vault. UPI IDs, mobile
  numbers and customer IDs are never put on a card.
- Add or edit the details in Settings → Security & privacy → Open details.

## Lent and owed: several accounts
- When you record **I lent**, **I borrowed**, **They paid me back** or **I paid them back**, the account
  part now has **+ Add another account**. Split an amount across banks, wallets or cash: for example
  borrow ₹10,000 into two banks, or pay a lender back from two accounts. Each part is its own entry, and a
  line shows how much is placed and how much is still to place; it will not save until they match.
- Choose “No – just note it” if nothing moves in your accounts.

## Withdraw charges
- The Withdraw form on an investment platform has **Charges, if any**. It shows what you will get, keeps
  the charges with money on the way, and records them as a small expense when the money arrives (or at once
  when you pick Already there).

## After listing: sold or kept (IPO)
- From listing day an allotted IPO asks **Sold or kept?** (on its card, on Home, and a 4 pm notification).
- Choose **Kept them** (optionally type today's price to see the value), **Sold all**, or **Sold some**
  (shares sold, with quick buttons for whole lots – 1 lot = the IPO's lot size).
- Enter the sell price per share and any charges. It shows what you received and the **gain or loss**
  (₹ and %). The money goes to the platform balance; the shares left stay in holdings at what you paid.
- The card keeps showing the result for 14 days; **Change** lets you correct it.

## Paying back and getting paid back (Lent and owed)
- Each person shows **Borrowed · paid back · left to pay** (or **Lent · got back · still to come**).
- **Pay back** / **They paid back** opens the form already filled with what is left and the account(s)
  the money first came into (or went out of) – change or split it if you like.

## Wallets tab
- Wallets have their own tab (no longer mixed with banks). A wallet that lives inside a UPI app also shows
  on that app's card with its balance.

## Cards: cashback and benefits in the Add guide
- Debit and credit cards in the Add guide have **Cashback %**, max per payment and per month; credit cards
  also take the **annual fee** and **benefits, one per line** (“4 lounge visits a year”, “1 movie ticket every
  month”) – each line becomes a benefit you can tick off.

## Logos, copy, backup reminder, instant warning
- Upload your own logo for any account (Edit → Logo) and for any UPI app (UPI card → **Logo**).
- The card back has **Copy** for the last 4 digits or IFSC (clipboard cleared after 30 seconds).
- **Make a backup** on Home when the last encrypted backup is over 30 days old (or never), and a monthly
  notification when it is over 3 weeks old.
- An **Instant** withdrawal asks you to confirm, because it cannot be cancelled and may cost a fee.

## Search (magnifier at the top)
- One search for **cards and accounts** (banks, cash, wallets, credit and debit cards, UPI apps, gift cards,
  benefits), **history** and **plans** (upcoming, autopay and fixed costs, EMIs, monthly reminders, people).
- Type a name (“Canara”), a word (“rent”) or an amount (“500” or “₹500” – exact amounts first).
- Results come in tabs with counts – All, Cards, History, Plans – showing the top few first with **See all**.
- Tap a result to go straight there: the wallet opens on that card, History opens at that entry, Plan opens
  at that item, People opens that person – each briefly highlighted.
- **Investments, IPOs, anything that moved money to or from an investment platform, and the private vault
  are never searched.** People are left out while that section is locked. Search closes when the app locks.

## Card text and card details
- A card's text never spills out: when there is more than fits (for example an IPO hold and today's UPI use),
  the card scrolls inside itself with a soft fade at the bottom. The same on the back.
- The back of each bank and card shows its details straight from the Details vault: **Set up** (first time),
  **Unlock**, **Add**, then the saved line with **Copy** and **✎** to change it.
- Settings now starts with **Card & bank details** (Open / Set up), so the details page is easy to find.

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
