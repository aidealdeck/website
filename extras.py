"""Search/AI-search data, card pages and lead-capture blocks for the Ai Deal Deck site."""
import json

SITE = "https://aidealdeck.com"
PHONE_DISPLAY = "(414) 946-6479"
PHONE_TEL = "+14149466479"
SUBSCRIBE = "https://shop.aidealdeck.com/subscribe"
SALE_ENDS = "2026-11-30"

CARDS = [
    dict(slug="kpi-tracker", key="KPI", n="1", name="Real Estate KPI Tracker",
         short="A real estate KPI tracker that shows your conversion rate at every step, from lead to closing, and the weekly number that gets you to your goal.",
         h1="A real estate KPI tracker that shows <em>where your deals leak.</em>",
         sub="Most agents know how many closings they had. Few know their rate from lead to appointment, appointment to signed, signed to closed. This card tracks every step and tells you the weekly number you need.",
         does=["Tracks lead → appointment set → appointment held → signed → under contract → closed, with the real percentage at each step",
               "Works out the weekly activity you need to reach the goal you type in (no goal is pre-set)",
               "Shows which lead sources produce closings and what each one costs per closing",
               "Starts on clearly labeled starting averages, then switches to your own rates as your year fills in"],
         inside=["START HERE guide (PDF)", "Your KPI Tracker workbook, blank (Excel or Google Sheets)", "Example KPI Tracker filled with sample data",
                 "The copy-and-paste setup prompt for Claude", "Claude Setup Pack (Claude reads this for you)", "Terms and disclaimer"],
         who="Solo agents and team leads who want to manage by numbers instead of by feel."),
    dict(slug="listing-exposure-playbook", key="LISTING", n="2", name="Listing Exposure Playbook",
         short="A repeatable 14-day listing launch plan for real estate agents, with fill-in templates and day-7 and day-14 seller reports.",
         h1="A 14-day listing launch plan you can <em>run the same way every time.</em>",
         sub="Every listing gets the same launch: a day-by-day plan, fill-in templates for the marketing pieces, and seller reports on day 7 and day 14 so your seller always knows what you did.",
         does=["Gives every listing a day-by-day 14-day launch plan", "Includes fill-in templates for the pieces you write for each listing",
               "Builds a day-7 and a day-14 report you can send your seller", "Keeps a launch tracker so nothing on the list gets skipped"],
         inside=["START HERE guide (PDF)", "Your Listing Launch Tracker workbook, blank", "Listing Exposure Playbook (PDF)", "Listing Templates (PDF)",
                 "Example Listing Launch Tracker filled with sample data", "The copy-and-paste setup prompt for Claude", "Claude Setup Pack", "Terms and disclaimer"],
         who="Listing agents who want a consistent launch and an easy way to show sellers the work."),
    dict(slug="lead-for-life-system", key="LEAD", n="3", name="Lead-for-Life System",
         short="A lead follow-up system for real estate agents: fast first contact, a set follow-up plan until they book, a speed scorecard and a TCPA checklist.",
         h1="A lead follow-up plan so <em>no paid lead gets forgotten.</em>",
         sub="New leads get contacted fast, then followed up on a set plan until they book. Claude drafts the messages; you review and send them. Nothing is sent on its own.",
         does=["Lays out a follow-up plan for every new lead until they book an appointment", "Keeps a daily call list so you know who is due today",
               "Scores how fast new leads get their first contact", "Includes a TCPA checklist for texting and calling"],
         inside=["START HERE guide (PDF)", "Your Lead-for-Life Plan & Call List workbook, blank", "Lead-for-Life System Playbook (PDF)",
                 "Example Plan & Call List filled with sample data", "The copy-and-paste setup prompt for Claude", "Claude Setup Pack", "Terms and disclaimer"],
         who="Agents who pay for leads or get more inquiries than they can follow up from memory. Setup takes about 20 minutes, plus an hour or two to build your plan in your CRM and write your own emails."),
    dict(slug="commission-gci-ledger", key="GCI", n="4", name="Commission & GCI Ledger",
         short="A commission and GCI tracker for real estate agents: every closing, fee, referral fee and split in one place, with team totals kept separate from your own income.",
         h1="A commission tracker that shows <em>what you really netted.</em>",
         sub="Every closing, fee, referral fee and split in one ledger. See gross commission income, what came off the top, and what you kept, with team totals separate from your own.",
         does=["Records every closing with its commission, fees, referral fees and splits", "Shows GCI and what you actually kept, by deal and for the year",
               "Keeps team production separate from your personal income", "Gives you one place to check a commission statement against"],
         inside=["START HERE guide (PDF)", "Your Commission Ledger workbook, blank", "Example Commission Ledger filled with sample data",
                 "The copy-and-paste setup prompt for Claude", "Claude Setup Pack", "Terms and disclaimer"],
         who="Agents and team leads who want one clear record of the money. It is a tracking tool, not accounting software or tax advice."),
    dict(slug="va-playbook-scorecard", key="VA", n="5", name="VA Playbook & Scorecard",
         short="A real estate virtual assistant playbook: a narrow role with three jobs, a daily routine, an end-of-day report and a weekly scorecard.",
         h1="A real estate assistant role with <em>three jobs and a scorecard.</em>",
         sub="Most assistant hires fail because the job is vague. This card gives your assistant a narrow role, a daily routine, an end-of-day report and a weekly scorecard you can read in a minute.",
         does=["Defines a narrow assistant role built around three jobs", "Sets a daily routine and an end-of-day report",
               "Scores the week so you can see what got done", "Includes templates for handing work over"],
         inside=["START HERE guide (PDF)", "Your VA Scorecard workbook, blank", "Real Estate VA Playbook (PDF)", "VA Templates (PDF)",
                 "Example VA Scorecard filled with sample data", "The copy-and-paste setup prompt for Claude", "Claude Setup Pack", "Terms and disclaimer"],
         who="Agents with an assistant, or about to hire one. Check your state's rules on what an unlicensed assistant may do."),
]


def esc(s):
    return s.replace("&", "&amp;")


def org_ld():
    return {"@type": "Organization", "@id": SITE + "/#org", "name": "Ai Deal Deck", "url": SITE + "/",
            "logo": SITE + "/assets/og.png", "email": "support@aidealdeck.com", "telephone": PHONE_TEL,
            "legalName": "The Showing Partner LLC",
            "description": "Do-it-yourself AI toolkits (cards) for real estate agents, set up with Claude.",
            "contactPoint": {"@type": "ContactPoint", "telephone": PHONE_TEL, "email": "support@aidealdeck.com",
                             "contactType": "sales and customer support", "areaServed": "US", "availableLanguage": "English"}}


def offer(price, url):
    return {"@type": "Offer", "price": str(price), "priceCurrency": "USD", "availability": "https://schema.org/InStock",
            "priceValidUntil": SALE_ENDS, "url": url, "seller": {"@id": SITE + "/#org"}}


def deck_ld(url):
    return {"@type": "Product", "@id": SITE + "/#deck", "name": "The AI Agent Deck", "brand": {"@type": "Brand", "name": "Ai Deal Deck"},
            "category": "Real estate agent software toolkit", "image": SITE + "/assets/og.png",
            "description": "Five do-it-yourself AI toolkits for real estate agents (KPI Tracker, Listing Exposure Playbook, Lead-for-Life System, "
                           "Commission & GCI Ledger, VA Playbook & Scorecard) plus two bonus cards (Listing Watchdog and Morning Brief). "
                           "Claude helps you set each one up in about 20 minutes. Requires the Claude desktop app and a paid Claude plan.",
            "offers": offer(49, url)}


def card_ld(c, url):
    return {"@type": "Product", "name": c["name"], "brand": {"@type": "Brand", "name": "Ai Deal Deck"},
            "category": "Real estate agent software toolkit", "image": SITE + "/assets/og.png", "description": c["short"],
            "isRelatedTo": {"@id": SITE + "/#deck"}, "offers": offer(19, url)}


def faq_ld(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def video_ld(name, desc, slug, secs):
    return {"@type": "VideoObject", "name": name, "description": desc, "thumbnailUrl": f"{SITE}/assets/video/{slug}.jpg",
            "contentUrl": f"{SITE}/assets/video/{slug}.mp4", "uploadDate": "2026-11-25", "duration": f"PT{secs}S"}


def ld_script(items):
    graph = [org_ld(), {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": "Ai Deal Deck", "publisher": {"@id": SITE + "/#org"}}] + items
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, separators=(",", ":")).replace("</", "<\\/") + "</script>"


def leadband(free_url):
    return f'''<section class="leadband" id="start-free">
<div class="wrap">
<div class="lb-main">
<div class="eyebrow gold">Not ready to buy today?</div>
<h2 class="h2">Start with two cards, free.</h2>
<p class="lead" style="margin-left:0">Listing Watchdog and Morning Brief. No payment card needed. Enter your email at checkout and the download is sent to you right away.</p>
<a class="btn" style="margin-top:22px" href="{free_url}" data-buy="Free bonus cards" data-value="0">Send me the free cards</a>
</div>
<div class="lb-side">
<b>Have a question first?</b>
<p>Call <a href="tel:{PHONE_TEL}" data-lead="call">{PHONE_DISPLAY}</a>. Sarah answers around the clock.</p>
<p>Or email <a href="mailto:support@aidealdeck.com" data-lead="email">support@aidealdeck.com</a>.</p>
<p>Just want news about new cards and sales? <a href="{SUBSCRIBE}" data-lead="subscribe">Leave your email here</a>.</p>
</div>
</div>
</section>'''


def nudge(free_url):
    """Small slide-in offer of the free cards, shown once per visit to people who have not clicked a buy or free button."""
    return f'''<aside class="nudge" id="nudge" hidden aria-label="Free cards offer">
<button type="button" class="nx" aria-label="Close">×</button>
<b>Before you go: two cards, free</b>
<span>Listing Watchdog + Morning Brief. No payment card needed.</span>
<a class="btn sm" href="{free_url}" data-buy="Free bonus cards" data-value="0">Get the free cards</a>
</aside>
<div class="mbar" id="mbar"><a href="{free_url}" data-buy="Free bonus cards" data-value="0" class="mfree">2 free cards</a><a href="__DECK__" data-buy="The AI Agent Deck" data-value="49" class="mbuy">Get the Deck: $49</a></div>
<script>
(function(){{var n=document.getElementById('nudge');if(!n)return;var done=false;
try{{done=sessionStorage.getItem('nudge')==='1';}}catch(e){{}}
function show(){{if(done)return;done=true;try{{sessionStorage.setItem('nudge','1');}}catch(e){{}}n.hidden=false;if(window.gtag)gtag('event','free_offer_shown',{{page:location.pathname}});}}
function stop(){{done=true;try{{sessionStorage.setItem('nudge','1');}}catch(e){{}}}}
document.addEventListener('click',function(e){{if(e.target.closest('.nx')){{n.hidden=true;return;}}if(e.target.closest('a[data-buy]'))stop();
var l=e.target.closest('a[data-lead]');if(l){{var k=l.getAttribute('data-lead');if(window.gtag)gtag('event','generate_lead',{{method:k,page:location.pathname}});if(window.fbq)fbq('track','Contact',{{method:k}});}}}});
setTimeout(show,40000);
window.addEventListener('scroll',function(){{var h=document.documentElement;if((h.scrollTop+window.innerHeight)/h.scrollHeight>0.6)show();}},{{passive:true}});
document.addEventListener('mouseout',function(e){{if(!e.relatedTarget&&e.clientY<8)show();}});
}})();
</script>'''


def card_page(c, urls, snip, faq_html, shop_html):
    buy = urls[c["key"]]
    does = "".join(f"<li>{snip['CHECKSM']}<span>{esc(x)}</span></li>" for x in c["does"])
    inside = "".join(f"<li>{esc(x)}</li>" for x in c["inside"])
    name = esc(c["name"])
    return f'''<section class="hero">
<div class="wrap">
<div class="copy">
<span class="pill">Card {c["n"]} of The AI Agent Deck</span>
<h1>{c["h1"]}</h1>
<p class="sub">{esc(c["sub"])}</p>
<div class="cta-row">
<a class="btn" href="{buy}" data-buy="{name}" data-value="19">Get this card: <s class="strike sm">$49</s> $19 {snip["ARROW"]}</a>
<div class="meta"><span data-sale>Black Friday launch price</span> through Nov 30.<br>Regular price $49 from Dec 1. Emailed instantly.</div>
</div>
<p class="alt-buy">Want all five cards plus two bonus cards? <a href="{urls["DECK"]}" data-buy="The AI Agent Deck" data-value="49">Get the full Deck for <s>$199</s> $49</a></p>
</div>
<div class="art">{snip["FAN"]}</div>
</div>
</section>

<section>
<div class="wrap">
<div class="center"><div class="eyebrow">What it does</div><h2 class="h2">{name}</h2><p class="lead">{esc(c["short"])}</p></div>
<div class="cols2">
<div class="tile"><h3>What you get from it</h3><ul class="ticks">{does}</ul></div>
<div class="tile"><h3>What is in the download</h3><ul class="plain">{inside}</ul></div>
</div>
<p class="lead center" style="margin-top:32px"><b>Who it is for.</b> {esc(c["who"])}</p>
</div>
</section>

<section class="sand">
<div class="wrap">
<div class="center"><div class="eyebrow" style="color:var(--gold-dark)">How setup works</div><h2 class="h2">Claude helps you set it up in about 20 minutes</h2></div>
<div class="steps">
<div class="step"><div class="n">1</div><div><b>Download the card</b><span>The link is emailed to you right after checkout.</span></div></div>
<div class="step"><div class="n">2</div><div><b>Paste one prompt into Claude</b><span>Claude reads the Setup Pack and asks you simple questions.</span></div></div>
<div class="step"><div class="n">3</div><div><b>Pick your view</b><span>A live dashboard Claude builds for you inside Claude, or the spreadsheet on its own. You choose.</span></div></div>
</div>
<p class="center fine" style="margin-top:24px">Do-it-yourself. Needs the Claude desktop app and a paid Claude plan (Claude Pro is currently $20/month), sold separately by Anthropic; heavier use may need a higher plan. <a href="/demo/">Try a live sample dashboard</a>.</p>
</div>
</section>

{shop_html}

<section>
<div class="narrow">
<h2 class="h2 center">Straight answers</h2>
{faq_html}
</div>
</section>'''


def llms_txt(cards, faq):
    lines = ["# Ai Deal Deck", "",
             "> Ai Deal Deck sells do-it-yourself AI toolkits, called cards, for real estate agents and team leads. Each card is a spreadsheet, a playbook and a copy-and-paste prompt. "
             "The buyer pastes the prompt into Claude (Anthropic's AI assistant) and Claude helps them set the tool up in about 20 minutes, with the option of a live dashboard built inside Claude.", "",
             "Ai Deal Deck is a brand of The Showing Partner LLC (Wisconsin, USA). It is independent and is not made or endorsed by Anthropic.", "",
             "## Products", "",
             f"- [The AI Agent Deck]({SITE}/): all five cards plus two bonus cards. Launch price $49 through November 30, 2026; regular price $199 from December 1, 2026."]
    for c in cards:
        lines.append(f"- [{c['name']}]({SITE}/cards/{c['slug']}/): {c['short']} Launch price $19 through November 30, 2026; regular price $49.")
    lines += [f"- [Free cards: Listing Watchdog and Morning Brief]({SITE}/free/): free download. Listing Watchdog tells an agent when a past client or lead they are watching lists with another agent. Morning Brief is one short summary from Claude each morning.",
              f"- [Live demo]({SITE}/demo/): a playable sample of the KPI dashboard, with sample data.", "",
              "## What buyers need", "",
              "- The Claude desktop app and a paid Claude plan (sold separately by Anthropic; heavier use may need a higher plan)",
              "- Google Sheets or Excel", "- A CRM is optional", "",
              "## Facts", ""]
    lines += [f"- {q} {a}" for q, a in faq]
    lines += ["", "## Contact", "", "- Email: support@aidealdeck.com", f"- Phone: {PHONE_DISPLAY} (answered around the clock)",
              f"- Terms: {SITE}/terms/", f"- Privacy: {SITE}/privacy/", ""]
    return "\n".join(lines)
