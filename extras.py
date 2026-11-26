"""Search/AI-search data, card pages and lead-capture blocks for the AiDealDeck site."""
import json, os

SITE = "https://aidealdeck.com"
PHONE_DISPLAY = "(414) 946-6479"
PHONE_TEL = "+14149466479"
SUBSCRIBE = "https://shop.aidealdeck.com/subscribe"
SALE_ENDS = "2026-11-30"

CARDS = [
    dict(slug="kpi-tracker", key="KPI", n="1", name="Real Estate KPI Tracker",
         short="A KPI tracker for real estate pros. It shows how many leads turn into closings at each step, and the one number to hit each week.",
         h1="A real estate KPI tracker that shows <em>where your deals leak.</em>",
         sub="You know how many closings you had. Do you know how many leads it took? This card counts every step and tells you the one number to hit each week.",
         does=["Counts every step: lead, appointment set, appointment held, signed, under contract, closed. Shows the real percent at each one",
               "You type in your goal. It tells you what to do each week to reach it",
               "Shows which lead sources turn into closings, and what each closing costs you",
               "Starts with sample averages, clearly marked. Switches to your own numbers as you add them"],
         inside=["START HERE guide (PDF)", "Your KPI Tracker workbook, blank (Excel or Google Sheets)", "Example KPI Tracker filled with sample data",
                 "The copy-and-paste setup prompt for Claude", "Claude Setup Pack (Claude reads this for you)", "Terms and disclaimer"],
         who="Real estate pros who want to manage by numbers instead of by feel."),
    dict(slug="listing-exposure-playbook", key="LISTING", n="2", name="Listing Exposure Playbook",
         short="A 14-day listing launch plan for real estate pros, with fill-in templates and seller reports on day 7 and day 14.",
         h1="A 14-day listing launch plan you can <em>run the same way every time.</em>",
         sub="Launch every listing the same way. You get a plan for each day, fill-in templates, and a report for your seller on day 7 and day 14.",
         does=["Tells you what to do each day for 14 days", "Gives you fill-in templates, so you are not starting from a blank page",
               "Makes a report for your seller on day 7 and day 14", "Keeps a checklist so nothing gets skipped"],
         inside=["START HERE guide (PDF)", "Your Listing Launch Tracker workbook, blank", "Listing Exposure Playbook (PDF)", "Listing Templates (PDF)",
                 "Example Listing Launch Tracker filled with sample data", "The copy-and-paste setup prompt for Claude", "Claude Setup Pack", "Terms and disclaimer"],
         who="Real estate pros who want a consistent listing launch and an easy way to show sellers the work."),
    dict(slug="lead-for-life-system", key="LEAD", n="3", name="Lead-for-Life System",
         short="A lead follow-up system for real estate pros: call fast, follow a set plan until they book, and track how fast you call.",
         h1="A lead follow-up plan so <em>no paid lead gets forgotten.</em>",
         sub="Call every new lead fast. Then follow a set plan until they book. Claude writes the messages. You read them and send them. Nothing is sent on its own.",
         does=["Gives you a follow-up plan for every new lead, until they book", "Makes a call list each day, so you know who to call",
               "Shows how fast you reach new leads", "Has a checklist of the rules for texting and calling (TCPA)"],
         inside=["START HERE guide (PDF)", "Your Lead-for-Life Plan & Call List workbook, blank", "Lead-for-Life System Playbook (PDF)",
                 "Example Plan & Call List filled with sample data", "The copy-and-paste setup prompt for Claude", "Claude Setup Pack", "Terms and disclaimer"],
         who="Real estate pros who pay for leads or get more inquiries than they can follow up from memory. Claude helps you set it up. Plan an hour or two to build your plan in your CRM and write your own emails."),
    dict(slug="commission-gci-ledger", key="GCI", n="4", name="Commission & GCI Ledger",
         short="A commission and GCI tracker for real estate pros: every closing, fee and split in one place, so you can see what you really kept.",
         h1="A commission tracker that shows <em>what you really netted.</em>",
         sub="Write down every closing and what you were paid. See your total commission, what came off the top, and what you kept. Team numbers stay apart from your own.",
         does=["Keeps every closing with its commission, fees and splits", "Shows what you earned and what you kept, for each deal and for the year",
               "Keeps team numbers apart from your own income", "Gives you one place to check a commission statement"],
         inside=["START HERE guide (PDF)", "Your Commission Ledger workbook, blank", "Example Commission Ledger filled with sample data",
                 "The copy-and-paste setup prompt for Claude", "Claude Setup Pack", "Terms and disclaimer"],
         who="Real estate pros who want one clear record of the money. It is a tracking tool, not accounting software or tax advice."),
    dict(slug="va-playbook-scorecard", key="VA", n="5", name="VA Playbook & Scorecard",
         short="A playbook for your real estate assistant: three clear jobs, a daily routine, a report each night and a score each week.",
         h1="A real estate assistant role with <em>three jobs and a scorecard.</em>",
         sub="An assistant needs a clear job. This card gives yours three tasks, a daily routine, a report each night and a score each week. You can read it in a minute.",
         does=["Gives your assistant three clear jobs", "Sets a daily routine and a report each night",
               "Scores each week, so you can see what got done", "Has templates for handing work over"],
         inside=["START HERE guide (PDF)", "Your VA Scorecard workbook, blank", "Real Estate VA Playbook (PDF)", "VA Templates (PDF)",
                 "Example VA Scorecard filled with sample data", "The copy-and-paste setup prompt for Claude", "Claude Setup Pack", "Terms and disclaimer"],
         who="Real estate pros with an assistant, or about to hire one. Check your state's rules on what an unlicensed assistant may do."),
]


def esc(s):
    return s.replace("&", "&amp;")


def org_ld():
    return {"@type": "Organization", "@id": SITE + "/#org", "name": "AiDealDeck", "url": SITE + "/",
            "logo": SITE + "/assets/og.png", "email": "support@aidealdeck.com", "telephone": PHONE_TEL,
            "legalName": "The Showing Partner LLC",
            "description": "Do-it-yourself AI toolkits (cards) for real estate pros, set up with Claude.",
            "contactPoint": {"@type": "ContactPoint", "telephone": PHONE_TEL, "email": "support@aidealdeck.com",
                             "contactType": "sales and customer support", "areaServed": "US", "availableLanguage": "English"}}


def offer(price, url):
    return {"@type": "Offer", "price": str(price), "priceCurrency": "USD", "availability": "https://schema.org/InStock",
            "priceValidUntil": SALE_ENDS, "url": url, "seller": {"@id": SITE + "/#org"}}


def deck_ld(url):
    return {"@type": "Product", "@id": SITE + "/#deck", "name": "The AI Agent Deck", "brand": {"@type": "Brand", "name": "AiDealDeck"},
            "category": "Real estate agent software toolkit", "image": SITE + "/assets/og.png",
            "description": "Five do-it-yourself AI toolkits for real estate pros (KPI Tracker, Listing Exposure Playbook, Lead-for-Life System, "
                           "Commission & GCI Ledger, VA Playbook & Scorecard) plus two bonus cards (Listing Watchdog and Morning Brief). "
                           "Claude helps you set them up. Requires the Claude desktop app and a paid Claude plan.",
            "offers": offer(49, url)}


def card_ld(c, url):
    return {"@type": "Product", "name": c["name"], "brand": {"@type": "Brand", "name": "AiDealDeck"},
            "category": "Real estate agent software toolkit", "image": SITE + "/assets/og.png", "description": c["short"],
            "isRelatedTo": {"@id": SITE + "/#deck"}, "offers": offer(19, url)}


def faq_ld(faq):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def video_ld(name, desc, slug, secs):
    return {"@type": "VideoObject", "name": name, "description": desc, "thumbnailUrl": f"{SITE}/assets/video/{slug}.jpg",
            "contentUrl": f"{SITE}/assets/video/{slug}.mp4", "uploadDate": "2026-11-25", "duration": f"PT{secs}S"}


def ld_script(items):
    graph = [org_ld(), {"@type": "WebSite", "@id": SITE + "/#site", "url": SITE + "/", "name": "AiDealDeck", "publisher": {"@id": SITE + "/#org"}}] + items
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, separators=(",", ":")).replace("</", "<\\/") + "</script>"


def leadband(free_url):
    return f'''<section class="leadband" id="start-free">
<div class="wrap">
<div class="lb-main">
<div class="eyebrow gold">Not ready?</div>
<h2 class="h2">Take the 2 free cards.</h2>
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


def nudge(free_url, bar=True):
    """Small slide-in offer of the free cards, shown once per visit to people who have not clicked a buy or free button."""
    solo = '' if bar else ' solo'
    mbar = '<div class="mbar" id="mbar"><a href="' + free_url + '" data-buy="Free bonus cards" data-value="0" class="mfree">2 free cards</a><a href="__DECK__" data-buy="The AI Agent Deck" data-value="49" class="mbuy">Get the Deck: $49</a></div>' if bar else ''
    return f'''<aside class="nudge" id="nudge" hidden aria-label="Free cards offer">
<button type="button" class="nx" aria-label="Close">×</button>
<b>2 free cards</b>
<span>Listing Watchdog + Morning Brief</span>
<a class="btn sm" href="{free_url}" data-buy="Free bonus cards" data-value="0">Get the free cards</a>
</aside>
<a class="freepill{solo}" id="freepill" href="{free_url}" data-buy="Free bonus cards" data-value="0"><span class="fpic">FREE<i>1</i></span><span><b>Get 2 free cards</b><small>Listing Watchdog + Morning Brief. No payment card.</small></span></a>
{mbar}
<script>
(function(){{var n=document.getElementById('nudge'),pill=document.getElementById('freepill');if(!n)return;var done=false;
try{{done=sessionStorage.getItem('nudge')==='1';}}catch(e){{}}
function show(){{if(done)return;done=true;try{{sessionStorage.setItem('nudge','1');}}catch(e){{}}n.hidden=false;pill.hidden=true;if(window.gtag)gtag('event','free_offer_shown',{{content_type:'nudge',content_id:location.pathname}});}}
function stop(){{done=true;try{{sessionStorage.setItem('nudge','1');}}catch(e){{}}}}
document.addEventListener('click',function(e){{if(e.target.closest('.nx')){{n.hidden=true;pill.hidden=false;return;}}if(e.target.closest('a[data-buy]'))stop();
var l=e.target.closest('a[data-lead]');if(l){{var k=l.getAttribute('data-lead');if(window.gtag)gtag('event','generate_lead',{{method:k,page:location.pathname}});if(window.fbq)fbq('track','Contact',{{method:k}});}}}});
/* The slide-in is off (owner, Nov 25): the deck shuffle is the only pop-up. The round free-cards button stays. */
}})();
</script>'''


def card_page(c, urls, snip, faq_html, shop_html):
    buy = urls[c["key"]]
    does = "".join(f"<li>{snip['CHECKSM']}<span>{esc(x)}</span></li>" for x in c["does"])
    inside = "".join(f"<li>{esc(x)}</li>" for x in c["inside"])
    name = esc(c["name"])
    _t = {"KPI": "KPI<br>Tracker", "LISTING": "Listing Exposure<br>Playbook", "LEAD": "Lead-for-Life<br>System", "GCI": "Commission &amp;<br>GCI Ledger", "VA": "VA Playbook<br>&amp; Scorecard"}[c["key"]]
    fan = (snip["FAN"].replace('aria-label="The AI Agent Deck: 5 cards plus 2 bonus cards, launch price $49"', 'aria-label="' + name + ': launch price $19"')
           .replace('<div class="t">The AI<br>Agent Deck</div>', '<div class="t" style="font-size:24px">' + _t + '</div>')
           .replace('5 cards + 2 bonus cards', 'Card ' + c["n"] + ' of 5')
           .replace('<small><s>$199</s></small><b>$49</b>', '<small><s>$49</s></small><b>$19</b>'))
    assert "$199" not in fan and "Agent Deck</div>" not in fan
    _v = os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'video', c['slug'] + '.mp4'))
    vid = (f'<video controls playsinline preload="none" poster="/assets/video/{c["slug"]}.jpg" style=\"display:block;width:100%;max-width:960px;aspect-ratio:16/9;margin:28px auto 8px;border-radius:16px;border:1px solid rgba(212,175,90,.55);background:#0E1730\"><source src="/assets/video/{c["slug"]}.mp4" type="video/mp4"></video><p class="center fine" style="margin:0 0 28px">Sample data shown.</p>') if _v else ''
    demo = '<a class="btn" href="/demo/" style="background:transparent;color:#fff;border:2px solid var(--gold)">Try the live demo first</a>' if c["key"] == "KPI" else ""
    return f'''<section class="hero">
<div class="wrap">
<div class="copy">
<span class="pill">Card {c["n"]} of The AI Agent Deck</span>
<h1>{c["h1"]}</h1>
<p class="sub">{esc(c["sub"])}</p>
<div class="cta-row">
<a class="btn" href="{buy}" data-buy="{name}" data-value="19">Get this card: <s class="strike sm">$49</s> $19 {snip["ARROW"]}</a>
{demo}
<ol class="howbuy" aria-label="How to buy"><li><b>1.</b> Click.</li><li><b>2.</b> Pay.</li><li><b>3.</b> Card lands in your email.</li></ol>
<div class="meta"><span data-sale>Black Friday launch price</span> through Nov 30.<br>Regular price $49 from Dec 1. Emailed instantly.</div>
</div>
<p class="alt-buy">Want all five cards plus two bonus cards? <a href="{urls["DECK"]}" data-buy="The AI Agent Deck" data-value="49">Get the full Deck for <s>$199</s> $49</a></p>
</div>
<div class="art">{fan}</div>
</div>
</section>

<section>
<div class="wrap">
<div class="center"><div class="eyebrow">What it does</div><h2 class="h2">{name}</h2><p class="lead">{esc(c["short"])}</p></div>
{vid}
<p class="center" style="margin:0 0 28px"><a class="btn" href="{buy}" data-buy="{name}" data-value="19">Get this card: <s class="strike sm">$49</s> $19 {snip["ARROW"]}</a></p>
<div class="cols2">
<div class="tile"><h3>What you get from it</h3><ul class="ticks">{does}</ul></div>
<div class="tile"><h3>What is in the download</h3><ul class="plain">{inside}</ul></div>
</div>
<p class="lead center" style="margin-top:32px"><b>Who it is for.</b> {esc(c["who"])}</p>
</div>
</section>

<section class="sand">
<div class="wrap">
<div class="center"><div class="eyebrow" style="color:var(--gold-dark)">How setup works</div><h2 class="h2">Claude helps you set it up</h2></div>
<div class="steps">
<div class="step"><div class="n">1</div><div><b>Download the card</b><span>The link is emailed to you right after checkout.</span></div></div>
<div class="step"><div class="n">2</div><div><b>Paste one prompt into Claude</b><span>Claude reads the Setup Pack and asks you simple questions.</span></div></div>
<div class="step"><div class="n">3</div><div><b>Pick your view</b><span>A live dashboard inside Claude that Claude helps you build, or the spreadsheet on its own. You choose.</span></div></div>
</div>
<p class="center" style="margin:28px 0 0"><a class="btn" href="{buy}" data-buy="{name}" data-value="19">Get this card: <s class="strike sm">$49</s> $19 {snip["ARROW"]}</a></p>
<p class="center fine" style="margin-top:16px">Do-it-yourself. Needs the Claude desktop app and a paid Claude plan (Claude Pro is currently $20/month), sold separately by Anthropic; heavier use may need a higher plan. <a href="/demo/">Try a live sample dashboard</a>.</p>
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
    lines = ["# AiDealDeck", "",
             "> AiDealDeck sells do-it-yourself AI toolkits, called cards, for real estate pros. Each card is a spreadsheet, a playbook and a copy-and-paste prompt. "
             "The buyer pastes the prompt into Claude (Anthropic's AI assistant) and Claude helps them set the tool up, with the option of a live dashboard built inside Claude.", "",
             "AiDealDeck is a brand of The Showing Partner LLC (Wisconsin, USA). It is independent and is not made or endorsed by Anthropic.", "",
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


def faq_page(groups):
    import re as _re
    blocks = []
    for cat, items in groups:
        rows = "".join(f'<details data-k="{esc(k)}"><summary>{esc(q)}</summary><p>{a}</p></details>' for q, a, k in items)
        blocks.append(f'<div class="faqgroup"><h2 class="h3">{esc(cat)}</h2><div class="faq">{rows}</div></div>')
    return f'''<section class="hero" style="padding-bottom:56px">
<div class="wrap" style="display:block;max-width:820px;text-align:center"><div class="copy" style="max-width:none">
<span class="pill">Answers</span>
<h1>Questions, <em>answered straight.</em></h1>
<p class="sub" style="margin-left:auto;margin-right:auto">Type your question. If we do not have an answer yet, we will see what you asked and add it.</p>
<form class="faqsearch" role="search" onsubmit="return false" style="justify-content:center"><input id="faqq" type="search" placeholder="Try: refund, CRM, dashboard, Claude plan" aria-label="Search the questions" autocomplete="off"><span id="faqcount" aria-live="polite"></span></form>
</div></div>
</section>
<section>
<div class="narrow">
<div id="faqmiss" class="faqmiss" hidden><b>We do not have that one yet.</b> We have noted your question and will add an answer. For an answer now, call <a href="tel:{PHONE_TEL}" data-lead="call">{PHONE_DISPLAY}</a> or email <a href="mailto:support@aidealdeck.com" data-lead="email">support@aidealdeck.com</a>.</div>
{"".join(blocks)}
</div>
</section>
<script>
(function(){{var q=document.getElementById('faqq'),miss=document.getElementById('faqmiss'),cnt=document.getElementById('faqcount');if(!q)return;
var items=[].slice.call(document.querySelectorAll('.faqgroup details'));var stop={{the:1,a:1,an:1,is:1,it:1,do:1,does:1,i:1,to:1,of:1,and:1,or:1,can:1,my:1,you:1,what:1,how:1,for:1,with:1,in:1,on:1,me:1,will:1,be:1,this:1,that:1,are:1,if:1,get:1,have:1}};
items.forEach(function(d){{d._t=(d.textContent+' '+d.getAttribute('data-k')).toLowerCase().replace(/\s/g,' ');}});
var timer=null,last='';
function run(){{var raw=q.value.trim().toLowerCase();var words=raw.split(/[^a-z0-9$]+/).filter(function(w){{return w.length>1&&!stop[w];}});var n=0;
items.forEach(function(d){{var hit=!words.length||words.some(function(w){{return d._t.indexOf(w.replace(/s$/,''))>-1;}});d.hidden=!hit;if(hit)n++;if(words.length&&hit&&n<=1)d.open=true;}});
document.querySelectorAll('.faqgroup').forEach(function(g){{g.hidden=!g.querySelector('details:not([hidden])');}});
miss.hidden=!(raw&&n===0);cnt.textContent=raw?(n+(n===1?' answer':' answers')):'';
clearTimeout(timer);if(raw.length>2){{timer=setTimeout(function(){{if(raw===last)return;last=raw;if(window.gtag)gtag('event','view_search_results',{{search_term:(n?'':'MISS: ')+(window.ADD_SCRUB?ADD_SCRUB(raw):raw).slice(0,90),content_type:n?'faq_hit':'faq_miss',value:n}});}},1500);}}}}
q.addEventListener('input',run);
document.addEventListener('toggle',function(e){{var d=e.target;if(d.tagName==='DETAILS'&&d.open&&d.closest('.faqgroup')&&window.gtag)gtag('event','faq_open',{{content_type:'faq_open',content_id:d.querySelector('summary').textContent.slice(0,90)}});}},true);
}})();
</script>'''


CHAT_URL = "https://script.google.com/macros/s/AKfycbxgjN_RQJlPgyL2hd6ZNf9QPRy020qsZmSF9f0kVub5vX9DwiadjtiLUhGkQRXyIXw/exec"


def after_free(urls):
    """Shown on the site right after someone clicks a free-cards button. The free checkout opens in a new tab;
    the offer shows first (Deck, then one card); the last No thanks goes to the free checkout."""
    cards = "".join('<a class="no" href="%s" data-buy="%s" data-value="19">%s: $19</a>' % (urls[c["key"]], c["name"].replace("&", "&amp;"), c["name"].replace("&", "&amp;")) for c in CARDS)
    html = """<dialog id="offer" aria-labelledby="offer-h">
<form method="dialog"><button class="x" aria-label="Close">×</button></form>
<div data-step="email">
<div class="eyebrow">2 free cards</div>
<h2 id="offer-h" class="h2" style="font-size:28px">Where should we send your free cards?</h2>
<p class="lead" style="font-size:16px">Listing Watchdog + Morning Brief. We email them to you right away. No payment card.</p>
<form id="offer-form" style="margin-top:16px"><input type="email" name="email" required maxlength="120" placeholder="Your email address" autocomplete="email" aria-label="Your email address" style="width:100%;box-sizing:border-box;padding:15px 14px;font:inherit;font-size:17px;border:2px solid var(--navy);border-radius:10px">
<input name="website" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px">
<button class="btn block" type="submit" style="margin-top:12px">Email me my free cards</button></form>
<p class="fine" id="offer-msg" aria-live="polite" style="margin-top:10px"></p>
<p class="fine" style="margin-top:6px">By sending, you agree to our <a href="/terms/">Terms</a> and <a href="/privacy/">Privacy</a>. We email your cards, then a few tips and offers. Unsubscribe in one click.</p>
</div>
<div data-step="deck" hidden>
<div class="eyebrow">Sent. Check your email in a minute.</div>
<h2 class="h2" style="font-size:28px">Want the rest of the cards for <s class="strike sm">$199</s> $49?</h2>
<p class="lead" style="font-size:16px">The Deck has five more cards: your numbers, listings, new leads, money and assistant. Your two free cards are included.</p>
<a class="btn block" style="margin-top:20px" href="__DECK__" data-buy="The AI Agent Deck" data-value="49">Yes, get the Deck: $49</a>
<button type="button" class="no" data-next>No thanks</button>
<p class="fine" style="margin-top:10px">Black Friday launch price through Nov 30. $199 is the regular price, starting Dec 1.</p>
</div>
<div data-step="card" hidden>
<div class="eyebrow">One more idea</div>
<h2 class="h2" style="font-size:28px">Just one card for <s class="strike sm">$49</s> $19?</h2>
<p class="lead" style="font-size:16px">Pick the one that helps you most.</p>
__CARDS__
<button type="button" class="no" data-next style="margin-top:18px;border-style:dashed">No thanks, I am all set</button>
<p class="fine" style="margin-top:10px">$19 is the launch price through Nov 30. $49 is the regular price, starting Dec 1.</p>
</div>
</dialog>
<script>
(function(){var d=document.getElementById('offer');if(!d||!d.showModal)return;var i=0,steps=['email','deck','card'],fallback='',f=document.getElementById('offer-form'),msg=document.getElementById('offer-msg');
function show(){d.querySelectorAll('[data-step]').forEach(function(s){s.hidden=s.getAttribute('data-step')!==steps[i];});}
document.addEventListener('click',function(e){
var a=e.target.closest('a[data-buy="Free bonus cards"]');
if(a&&!d.open){e.preventDefault();fallback=a.href;i=0;show();msg.textContent='';d.showModal();f.email.focus();if(window.gtag)gtag('event','free_offer_shown',{content_type:'after_free',content_id:location.pathname});return;}
if(e.target.closest('#offer [data-next]')){i++;if(i>=steps.length)d.close();else show();}});
f.addEventListener('submit',function(e){e.preventDefault();var b=f.querySelector('button');b.disabled=true;msg.textContent='Sending...';
var ac=window.AbortController?new AbortController():null,slow=setTimeout(function(){msg.textContent='Still sending. One moment.';},5000),kill=setTimeout(function(){if(ac)ac.abort();},15000);function done(){clearTimeout(slow);clearTimeout(kill);}
fetch('__CHAT_URL__',{method:'POST',credentials:'omit',signal:ac?ac.signal:undefined,body:JSON.stringify({action:'free',email:f.email.value,website:f.website.value,page:location.pathname})}).then(function(r){return r.json();}).then(function(j){done();b.disabled=false;
if(j&&j.ok){msg.textContent='';if(window.gtag)gtag('event','generate_lead',{method:'free_cards_email',page:location.pathname});if(window.fbq)fbq('track','Lead',{content_name:'Free bonus cards'});i=1;show();}
else if(j&&j.error==='email'){msg.textContent='That email address does not look right. Please check it.';}
else{msg.innerHTML='We could not send it just now. <a href="'+fallback+'">Get the free cards here instead</a>.';}
}).catch(function(){done();b.disabled=false;msg.innerHTML='We could not send it just now. <a href="'+fallback+'">Get the free cards here instead</a>.';});});
})();
</script>"""
    return html.replace("__DECK__", urls["DECK"]).replace("__CARDS__", cards).replace("__CHAT_URL__", CHAT_URL)


def chat():
    """Sarah, the site's AI assistant. Asks the script for an AI answer; if that is off or fails, answers from the FAQ."""
    html = """<button type="button" class="chatbtn" id="chatbtn" aria-controls="chatbox" aria-expanded="false"><span class="chatav"><img src="https://lh3.googleusercontent.com/ogw/AF2bZyhflXcfsmm4LAEI0ZxqU__QFQx6h8rYqx2lFxW2eyMG=s192-c" alt="" width="52" height="52" referrerpolicy="no-referrer" onerror="this.remove()"><i></i><em>1</em></span><span class="chattx"><b>Chat with Sarah</b><small>Hi! I have a Black Friday tip for you.</small></span></button>
<section class="chatbox" id="chatbox" data-clarity-mask="true" hidden aria-label="Chat with Sarah, the AiDealDeck AI assistant">
<header><img class="chathead" src="https://lh3.googleusercontent.com/ogw/AF2bZyhflXcfsmm4LAEI0ZxqU__QFQx6h8rYqx2lFxW2eyMG=s192-c" alt="" width="40" height="40" referrerpolicy="no-referrer" onerror="this.remove()"><div style="flex:1"><b>Sarah Hill</b><span>AI assistant for AiDealDeck</span></div><button type="button" class="cx" id="chatx" aria-label="Close chat">×</button></header>
<div class="chatlog" id="chatlog" aria-live="polite"></div>
<form id="chatform" autocomplete="off"><input id="chatq" type="text" maxlength="300" placeholder="Type your question" aria-label="Type your question"><button type="submit">Send</button></form>
<p class="chatfine">Sarah is an AI assistant, not a person. Your messages go to our AI provider (xAI) and are stored to answer you and improve our help. Do not share private or payment details. <a href="/privacy/">Privacy</a></p>
</section>
<script>
(function(){var URL_='__CHAT_URL__';var btn=document.getElementById('chatbtn'),box=document.getElementById('chatbox'),log=document.getElementById('chatlog'),form=document.getElementById('chatform'),inp=document.getElementById('chatq');
if(!btn||!box)return;var hist=[],faq=null,busy=false,greeted=false;
function ev(n,p){if(window.gtag)gtag('event',n,p||{});}
function add(who,html,isText){var d=document.createElement('div');d.className='cm '+who;if(isText)d.textContent=html;else d.innerHTML=html;log.appendChild(d);log.scrollTop=log.scrollHeight;return d;}
function open_(){box.hidden=false;btn.setAttribute('aria-expanded','true');btn.hidden=true;if(!greeted){greeted=true;add('s',"Hi, I am Sarah, the AI assistant for AiDealDeck. Black Friday sale: the full Deck is $49, not $199, through Nov 30. Any questions? Ask me.",true);var bd=btn.querySelector('.chatav em');if(bd)bd.remove();btn.classList.add('seen');ev('chat_open',{content_type:'chat',content_id:location.pathname});}inp.focus();}
function close_(){box.hidden=true;btn.hidden=false;btn.setAttribute('aria-expanded','false');}
btn.addEventListener('click',open_);document.getElementById('chatx').addEventListener('click',close_);
var STOP={the:1,a:1,an:1,is:1,are:1,'do':1,does:1,i:1,to:1,it:1,of:1,and:1,or:1,my:1,me:1,you:1,your:1,what:1,how:1,can:1,'for':1,'in':1,on:1,'with':1,'this':1,that:1,be:1,have:1,'if':1,get:1,will:1,there:1,about:1};
function words(t){return (t||'').toLowerCase().replace(/<[^>]+>/g,' ').replace(/[^a-z0-9$ ]/g,' ').split(/ +/).filter(function(w){return w.length>1&&!STOP[w];});}
function fromFaq(q){var qs=words(q),best=null,bs=0;if(!qs.length||!faq)return null;
faq.forEach(function(f){var qw=words(f.q),kw=words(f.k),aw=words(f.a),s=0;qs.forEach(function(w){if(qw.indexOf(w)>-1)s+=3;if(kw.indexOf(w)>-1)s+=3;if(aw.indexOf(w)>-1)s+=1;});s=s/Math.sqrt(qs.length);if(s>bs){bs=s;best=f;}});
return bs>=2.4?best:null;}
function loadFaq(){if(faq)return Promise.resolve();return fetch('/faq.json').then(function(r){return r.json();}).then(function(j){faq=j;}).catch(function(){faq=[];});}
function fallback(q,wait){loadFaq().then(function(){var f=fromFaq(q);log.removeChild(wait);
if(f){add('s',f.a+' <a href="/faq/">More answers</a>');ev('chat_message',{content_type:'chat',content_id:'faq'});}
else{add('s','I am not sure about that one. You can call <a href="tel:+14149466479" data-lead="call">(414) 946-6479</a> or email <a href="mailto:support@aidealdeck.com" data-lead="email">support@aidealdeck.com</a> and we will get you an answer.');ev('view_search_results',{search_term:'MISS: chat: '+(window.ADD_SCRUB?ADD_SCRUB(q):q).slice(0,80)});ev('chat_message',{content_type:'chat',content_id:'miss'});}
busy=false;});}
form.addEventListener('submit',function(e){e.preventDefault();var q=inp.value.trim();if(!q||busy)return;busy=true;inp.value='';add('u',q,true);var wait=add('s','...',true);
var done=false,t=setTimeout(function(){if(!done){done=true;fallback(q,wait);}},9000);
fetch(URL_,{method:'POST',credentials:'omit',body:JSON.stringify({action:'chat',q:q,history:hist.slice(-6),page:location.pathname})}).then(function(r){return r.json();}).then(function(j){if(done)return;done=true;clearTimeout(t);if(j&&j.ok&&j.answer){wait.textContent=j.answer;hist.push({role:'user',content:q});hist.push({role:'assistant',content:j.answer});ev('chat_message',{content_type:'chat',content_id:'ai'});busy=false;}else{fallback(q,wait);}}).catch(function(){if(done)return;done=true;clearTimeout(t);fallback(q,wait);});});
})();
</script>"""
    return html.replace("__CHAT_URL__", CHAT_URL)


def pick():
    """Pick a card: a first-visit pop-up. Type an email, the deck shuffles, tap a card, win a prize (5/10/15% off or the two free cards)."""
    cards = "".join('<button type="button" class="pk-card" aria-label="Card %d"><span class="pk-in"><span class="pk-back"><img src="/assets/brand/mark-gold.svg" alt="" width="54" height="54"></span><span class="pk-front"></span></span></button>' % (i + 1) for i in range(4))
    return PICK_HTML.replace("__CARDS__", cards).replace("__CHAT_URL__", CHAT_URL)


PICK_HTML = r"""<dialog id="pick" aria-label="Pick a card">
<button type="button" class="px" aria-label="Close">&times;</button>
<div data-p="email">
<div class="eyebrow">Welcome</div>
<h3>Pick a card. Win a prize.</h3>
<p class="pk-sub">Type your email. Shuffle. Pick one.</p>
<form id="pick-form"><input type="email" name="email" required placeholder="Your email" autocomplete="email" aria-label="Your email"><button class="btn block" type="submit">Shuffle the deck</button></form>
<p class="fine" id="pick-msg" role="status"></p>
<p class="fine">One prize per email. We email it to you once.</p>
</div>
<div data-p="cards" hidden>
<h3 id="pk-h">Shuffling...</h3>
<div class="pk-row" id="pk-row">__CARDS__</div>
</div>
<div data-p="won" hidden>
<div class="eyebrow" id="pk-eye">You won</div>
<h3 id="pk-won"></h3>
<p class="pk-sub" id="pk-until"></p>
<a class="btn block" id="pk-go" href="#"></a>
<a class="btn block" id="pk-deck" href="#" data-buy="The AI Agent Deck" hidden></a>
<p class="fine" id="pk-fine"></p>
</div>
</dialog>
<script>
(function(){var d=document.getElementById('pick');if(!d||!d.showModal)return;var API='__CHAT_URL__',FREE='__FREE__',LS=null;try{LS=window.localStorage;}catch(e){}
function get(k){try{return LS&&LS.getItem(k);}catch(e){return null;}}function set(k,v){try{LS&&LS.setItem(k,v);}catch(e){}}function del(k){try{LS&&LS.removeItem(k);}catch(e){}}
function step(n){d.querySelectorAll('[data-p]').forEach(function(s){s.hidden=s.getAttribute('data-p')!==n;});}
function post(b){return fetch(API,{method:'POST',credentials:'omit',body:JSON.stringify(b)}).then(function(r){return r.json();});}
function apply(j){if(!j||!j.code)return;document.querySelectorAll('a[href*="shop.aidealdeck.com/l/"]').forEach(function(a){var h=a.getAttribute('href');if(h.indexOf('?wanted=true')>0&&h.indexOf('/'+j.code)<0)a.setAttribute('href',h.replace('?wanted=true','/'+j.code+'?wanted=true'));});
if(!document.getElementById('pk-bar')){var b=document.createElement('div');b.id='pk-bar';b.setAttribute('role','button');b.tabIndex=0;b.textContent='Your prize: '+(j.label||j.pct+'% off')+' with code '+j.code+'. Already added to every buy button. Good until '+j.until+'.';b.onclick=function(){won(j,true);if(!d.open)d.showModal();};document.body.insertBefore(b,document.body.firstChild);}}
function unapply(){var b=document.getElementById('pk-bar');if(b)b.remove();document.querySelectorAll('a[href*="shop.aidealdeck.com/l/"]').forEach(function(a){a.setAttribute('href',a.getAttribute('href').replace(/\/WIN[0-9A-Z]+\?wanted=true/,'?wanted=true'));});}
function keep(j){if(j&&j.code)set('pkPrize',JSON.stringify({pct:j.pct,label:j.label,code:j.code,until:j.until,tok:j.tok,exp:j.exp||0}));}
function deck(){var a=document.querySelector('a[data-buy="The AI Agent Deck"][href*="wanted=true"]');return a?a.getAttribute('href'):'https://shop.aidealdeck.com/l/the-ai-agent-deck?wanted=true';}
function won(j,quiet){var w=document.getElementById('pk-won'),u=document.getElementById('pk-until'),g=document.getElementById('pk-go'),f=document.getElementById('pk-fine'),e=document.getElementById('pk-eye');
e.textContent=quiet?'Your prize':j.again?'You already picked':'You won';
if(j.pct>0&&j.code){apply(j);w.textContent=(j.label||j.pct+'% off')+' anything';u.textContent='Good until '+j.until+'.';g.textContent='Use it on the Deck';g.href=deck();f.textContent='Your code is '+j.code+'. It is already added to every buy button here, so you do not need to type it.';}
else if(j.pct>0){w.textContent='Your prize has ended';u.textContent='It was good until '+j.until+'.';g.textContent='Keep looking';g.href='#';f.textContent='';}
else{w.textContent='2 free cards';u.textContent='Listing Watchdog + Morning Brief.';g.textContent='Keep looking';g.href='#';f.textContent='We just emailed them to you.';}
var k=document.getElementById('pk-deck'),da=document.querySelector('a[data-buy="The AI Agent Deck"][data-value]'),pv=da?da.getAttribute('data-value'):'';if(j.pct>0&&j.code){k.hidden=true;}else{k.hidden=false;k.href=deck();k.textContent='Get the full Deck'+(pv?': $'+pv:'');}
step('won');}
var res=null,picked=null,row=document.getElementById('pk-row'),h=document.getElementById('pk-h'),f=document.getElementById('pick-form'),msg=document.getElementById('pick-msg');
function reveal(){if(!res||!picked)return;picked.querySelector('.pk-front').textContent=(res.label||(res.pct>0?res.pct+'% off':'2 free cards')).toUpperCase();row.classList.add('done');picked.classList.add('flip');if(window.gtag)gtag('event','pick_won',{value:res.pct,content_id:location.pathname});setTimeout(function(){won(res);},1300);}
row.addEventListener('click',function(e){var c=e.target.closest('.pk-card');if(!c||picked||!row.classList.contains('ready'))return;picked=c;h.textContent='Good pick...';reveal();});
f.addEventListener('submit',function(e){e.preventDefault();var b=f.querySelector('button');b.disabled=true;msg.textContent='';
post({action:'pick',email:f.email.value,page:location.pathname}).then(function(j){b.disabled=false;
if(j&&j.ok){res=j;set('pkTok',j.tok);if(!j.again)j.exp=Date.now()+1728e5;keep(j);if(window.gtag)gtag('event','generate_lead',{method:'pick_card',page:location.pathname});if(window.fbq)fbq('track','Lead',{content_name:'Pick a card'});
if(j.again){won(j);return;}step('cards');row.classList.add('shuffle');setTimeout(function(){row.classList.remove('shuffle');row.classList.add('ready');h.textContent='Pick one';},1900);}
else if(j&&j.error==='email'){msg.textContent='That email address does not look right. Please check it.';}
else{msg.innerHTML='We could not shuffle just now. <a href="'+FREE+'">Get the 2 free cards here instead</a>.';}
}).catch(function(){b.disabled=false;msg.innerHTML='We could not shuffle just now. <a href="'+FREE+'">Get the 2 free cards here instead</a>.';});});
d.addEventListener('click',function(e){if(e.target.closest('.px')||(e.target.id==='pk-go'&&e.target.getAttribute('href')==='#')){e.preventDefault();d.close();}});
var m=/[?&]prize=([0-9a-f]{20})/.exec(location.search),tok=m?m[1]:get('pkTok');
var saved=null;try{saved=JSON.parse(get('pkPrize')||'null');}catch(e){}
if(saved&&saved.code&&(!m||saved.tok===m[1])&&(!saved.exp||saved.exp>Date.now()))apply(saved);else if(saved&&saved.exp&&saved.exp<=Date.now()){del('pkPrize');saved=null;}
if(tok){if(m)set('pkTok',tok);post({action:'pick',tok:tok}).then(function(j){if(j&&j.ok&&j.code){if(saved&&saved.exp)j.exp=saved.exp;keep(j);apply(j);}else if(j&&(j.none||j.expired)){del('pkTok');del('pkPrize');unapply();}}).catch(function(){});return;}
if(get('pkSeen')||(saved&&saved.code))return;
setTimeout(function(){if(document.querySelector('dialog[open]'))return;set('pkSeen','1');try{sessionStorage.setItem('nudge','1');}catch(e){}var nn=document.getElementById('nudge');if(nn)nn.style.display='none';step('email');d.showModal();try{f.email.focus();}catch(e){}if(window.gtag)gtag('event','pick_shown',{content_id:location.pathname});},3500);
})();
</script>"""
