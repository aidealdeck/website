"""The long FAQ. Each entry: (question, answer_html, extra search words).
Only facts already stated on the site, the product pages or the Terms. New entries are added from real questions
(calls, emails and searches on this page that found nothing)."""

P = "(414) 946-6479"

FAQ_LONG = [
    ("The basics", [
        ("What is Ai Deal Deck?", "Ai Deal Deck sells do-it-yourself AI toolkits for real estate pros: agents, team leads, wholesalers and investors. We call each toolkit a card. A card is a workbook, a short guide and one copy-and-paste prompt. You paste the prompt into Claude and Claude helps you set that tool up in about 20 minutes.", "about company product overview"),
        ("What is a card?", "One tool for one part of your business: your numbers, your listings, your new leads, your money or your assistant. Each card comes with a blank workbook, a sample workbook, a START HERE guide, the setup prompt and a Setup Pack that Claude reads.", "toolkit tool"),
        ("What is The AI Agent Deck?", "All five cards in one download, plus two bonus cards (Listing Watchdog and Morning Brief). It costs less than three single cards.", "bundle package all"),
        ("Who is it for?", "Real estate pros who sell for a living: agents, team leads, wholesalers, investors and anyone else running leads, deals and commissions. The examples use agent language (listings, closings, splits), and the trackers work the same way for any real estate sales business that wants its back office organized without hiring a developer or learning new software.", "realtor broker team solo wholesaler wholesaling investor investors flipper pros"),
        ("Is it done for me?", "No. It is a do-it-yourself toolkit. Claude helps you set it up, but you do the setup and you keep it running. If you would rather have it set up for you, email support@aidealdeck.com and ask about done-for-you setup, which is a separate service.", "dfy done for you install service"),
        ("Is this made by Anthropic or Claude?", "No. Ai Deal Deck is an independent product built to work with Claude. It is not made or endorsed by Anthropic. Claude is a trademark of Anthropic, PBC.", "affiliated official endorsed"),
        ("Who is behind Ai Deal Deck?", "Ai Deal Deck is a brand of The Showing Partner LLC, a Wisconsin company. It is not affiliated with or endorsed by any brokerage, MLS or trade association.", "owner company llc who owns"),
    ]),
    ("What you need", [
        ("What do I need to use a card?", "The Claude desktop app and a paid Claude plan, both from Anthropic, plus Google Sheets or Excel. A CRM is optional.", "requirements need software"),
        ("Do I need a paid Claude plan?", "Yes. The cards use Claude features that need a paid plan. Claude Pro is currently $20 a month and is sold separately by Anthropic. It is not included in our price.", "free claude subscription cost pro"),
        ("Will I need a bigger Claude plan later?", "Maybe. The more cards you run and the more often they update, the more of your Claude plan they use. Heavier use may need a higher plan. Anthropic sets those plans and prices and can change them.", "upgrade max limit usage"),
        ("Does it work with ChatGPT or another AI?", "The cards are written and tested for Claude. We do not support other AI tools.", "chatgpt gemini copilot gpt"),
        ("Does it work on a phone or tablet?", "Setup needs the Claude desktop app on a computer. After that you can open your workbook anywhere Google Sheets or Excel runs.", "mobile iphone ipad android mac windows"),
        ("Do I need Google Sheets, or can I use Excel?", "Either one. A free Google account is recommended so your trackers can update on their own, and Excel works too.", "spreadsheet microsoft"),
        ("Will it work with my CRM?", "If Claude has a connector for your CRM, Claude can read it directly. If not, you can export a spreadsheet from your CRM. We cannot promise every CRM works, so check before you buy.", "follow up boss kvcore lofty sierra crm connector integration"),
        ("Do I need to know how to code?", "No. You paste one prompt and answer plain questions.", "technical tech skills programming"),
    ]),
    ("Setup", [
        ("How long does setup take?", "About 20 minutes per card. The Lead-for-Life System takes another hour or two because you build your follow-up plan in your CRM and write your own emails.", "time minutes long"),
        ("How do I set up a card?", "Save the download to your Downloads folder. Open the Claude desktop app, start a new chat and add that folder. Paste in the COPY THIS PROMPT file and press Enter. Claude asks you simple questions and you approve what it sets up. The START HERE guide in every download walks through it.", "install steps start instructions"),
        ("Do I get a spreadsheet or a dashboard?", "Both are in the box and you choose. Every card has a workbook. During setup Claude asks whether you want a live dashboard as your main view. If you say yes, Claude builds it for you inside Claude from your own numbers, and the workbook stays as the place your data lives.", "artifact dashboard view excel"),
        ("Will my dashboard look like the one on the site?", "The site shows examples with sample data. Claude builds your dashboard from your own numbers, so yours may look different.", "screenshot example same demo"),
        ("Can I see a dashboard before I buy?", "Yes. There is a <a href=\"/demo/\">live demo of the KPI dashboard</a> with sample data that you can play with.", "preview try demo sample"),
        ("What if I get stuck during setup?", "Reply to your receipt email, email support@aidealdeck.com or call " + P + ". We can help you with the steps. We cannot log in to your accounts.", "help support stuck error"),
        ("Can I set up one card now and the others later?", "Yes. Each card stands on its own. Play them in any order.", "order later one at a time"),
        ("Do I have to keep it updated?", "Yes. A tracker only helps if your numbers go into it. Where Claude can read your CRM or your sheet, it can update for you on the schedule you set.", "maintain update automatic manual"),
    ]),
    ("The cards", [
        ("What does the Real Estate KPI Tracker do?", "It tracks lead to appointment set, held, signed, under contract and closed, with the real percentage at each step. It works out the weekly number you need for the goal you type in, and shows which lead sources produce closings. <a href=\"/cards/kpi-tracker/\">More about this card</a>.", "kpi numbers conversion funnel"),
        ("What does the Listing Exposure Playbook do?", "It gives every listing the same 14-day launch plan, with fill-in templates and day-7 and day-14 seller reports. <a href=\"/cards/listing-exposure-playbook/\">More about this card</a>.", "listing marketing launch seller report"),
        ("What does the Lead-for-Life System do?", "It lays out a follow-up plan for every new lead until they book, keeps a daily call list, scores how fast leads get a first contact, and includes a TCPA checklist. <a href=\"/cards/lead-for-life-system/\">More about this card</a>.", "lead follow up speed nurture"),
        ("What does the Commission & GCI Ledger do?", "It records every closing with its commission, fees, referral fees and splits, and keeps team totals separate from your own income. It is a tracking tool, not accounting software. <a href=\"/cards/commission-gci-ledger/\">More about this card</a>.", "commission gci income split money"),
        ("What does the VA Playbook & Scorecard do?", "It gives your assistant a narrow role with three jobs, a daily routine, an end-of-day report and a weekly scorecard. <a href=\"/cards/va-playbook-scorecard/\">More about this card</a>.", "assistant va virtual admin"),
        ("What is the Listing Watchdog?", "A bonus card. You tell it which people to watch: past clients, people who went quiet after an appointment, referrals. It tells you when one of them lists with another agent, or when that listing expires or comes back. Public listing sites can be late or wrong, so always confirm on your MLS.", "watchdog lost listing expired fsbo"),
        ("What is the Morning Brief?", "A bonus card. It is one short summary from Claude each morning of what is due, who needs a call and what slipped. It reads every card you have set up.", "brief daily summary morning"),
        ("Are the bonus cards really free?", "Yes. The Listing Watchdog and Morning Brief are a <a href=\"/free/\">free download</a>. They are also included in the Deck. They still need the Claude desktop app and a paid Claude plan.", "free bonus no cost"),
        ("Will there be more cards?", "We plan to release more. New cards are separate products, sold separately, and no release dates are promised.", "future new cards 52 roadmap"),
    ]),
    ("What it does not do", [
        ("Will it text, call or email my leads for me?", "No. It drafts messages for you to review and send. It never texts, calls or emails anyone on its own. If you set up your own automation, you are responsible for consent and for TCPA, CAN-SPAM, do-not-call and your state's rules.", "automatic texting calling dialer autopilot tcpa"),
        ("Will it get me more leads, listings or closings?", "We do not promise more leads, listings, closings or income. It shows you your numbers and what needs your attention. Results depend on your own work.", "guarantee results income more deals roi"),
        ("Is it legal, tax or brokerage advice?", "No. The cards are tools, not professional advice. You are responsible for your license law, brokerage policies, MLS rules and fair housing laws.", "legal tax advice accountant attorney"),
        ("Can AI make mistakes in my numbers?", "Yes. AI can make mistakes. Check what Claude sets up, fills in or drafts, and check important numbers before you rely on them.", "accurate wrong error hallucinate trust"),
    ]),
    ("Price and buying", [
        ("How much does it cost?", "Through November 30: The AI Agent Deck is $49 and each single card is $19. From December 1 the regular prices are $199 for the Deck and $49 for a single card. The price on the page when you buy is the price you pay.", "price cost how much sale discount"),
        ("Is it a subscription?", "No. You pay once and keep the files. The only ongoing cost is your own Claude plan, paid to Anthropic.", "monthly recurring fee one time"),
        ("Should I buy one card or the Deck?", "Five single cards cost more than the Deck, and the Deck adds both bonus cards. If you want more than two cards, the Deck costs less.", "which bundle single compare"),
        ("I bought a single card. Can I upgrade to the Deck?", "The Deck is a separate purchase. At checkout, anyone with a single card in the cart is offered the full Deck in its place. If you already bought and want to move up, email support@aidealdeck.com.", "upgrade credit switch"),
        ("How do I buy?", "Use any buy button on this site. Checkout is handled by Gumroad. We never take payment by phone.", "pay checkout gumroad payment card apple pay"),
        ("How do I get my files?", "The download link is emailed to you right after checkout, and it is on your Gumroad receipt page.", "download delivery email link receive"),
        ("I did not get my download email. What do I do?", "Check your spam folder for an email from Gumroad. If it is not there, email support@aidealdeck.com with the email address you used at checkout and we will send it again.", "missing email not received spam lost"),
        ("Is sales tax added?", "Gumroad adds sales tax at checkout where it applies.", "tax vat"),
        ("Can my whole team use one purchase?", "Your license covers your own business or your own team's business. You may not share, resell or give the files to anyone outside it.", "team license share brokerage office multiple users"),
    ]),
    ("Refunds and support", [
        ("Can I get a refund?", "All sales are final because the files are delivered instantly and you keep them, except where the law where you live gives you a right that cannot be waived. Please read this page and the <a href=\"/terms/\">Terms</a> before you buy. If a file is missing or will not open, we fix it.", "refund money back return cancel guarantee"),
        ("A file will not open or is missing. What do I do?", "Email support@aidealdeck.com with the email you used at checkout and what happened. We will help or send a working copy.", "broken corrupt file open error"),
        ("How do I reach a person?", "Email support@aidealdeck.com, or call " + P + " any time. Sarah answers around the clock, can answer most questions and passes messages to the team.", "contact phone human talk call support"),
        ("Is the phone line a real person?", "The line is answered around the clock by Sarah, an AI assistant. For anything she cannot answer she takes your name and email and the team replies.", "sarah ai bot robot human"),
    ]),
    ("Privacy and your data", [
        ("Can you see my leads, clients or numbers?", "No. The cards run in your own accounts: your Claude account, your Google or Excel files and your CRM. We have no access to them and never see what you put in.", "data privacy access see my clients confidential"),
        ("Where is my data stored?", "In your own accounts. Your workbook lives in your Google Drive or on your computer, and your dashboard lives in your Claude account.", "stored cloud saved location"),
        ("What do you collect about me?", "Your name, email and order details from Gumroad when you buy or download, anything you email or tell us on a call, and visit statistics from this site. The <a href=\"/privacy/\">Privacy page</a> has the details and your choices.", "collect tracking cookies pixel"),
        ("Will you email me?", "You get your receipt and download link. If you bought or subscribed, we may send product help and news about new cards. Every such email has an unsubscribe link.", "spam marketing newsletter unsubscribe"),
    ]),
]


def flat():
    return [(q, a, k, cat) for cat, items in FAQ_LONG for q, a, k in items]
