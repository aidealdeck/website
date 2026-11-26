#!/usr/bin/env python3
"""Builds the static AiDealDeck site from src/ into public/."""
import json, os, re, shutil
import extras
import faq_data

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, OUT = os.path.join(ROOT, "src"), os.path.join(ROOT, "docs")
import datetime
BUILD_DATE = datetime.date.today().isoformat()
SHOP = "https://shop.aidealdeck.com/l/"
URLS = {
    "DECK": SHOP + "the-ai-agent-deck?wanted=true",
    "KPI": SHOP + "real-estate-kpi-tracker?wanted=true",
    "LISTING": SHOP + "listing-exposure-playbook?wanted=true",
    "LEAD": SHOP + "lead-for-life-system?wanted=true",
    "GCI": SHOP + "agent-commission-gci-ledger?wanted=true",
    "VA": SHOP + "real-estate-va-playbook?wanted=true",
    "FREE": SHOP + "free-ai-agent-deck-bonuses",
}

DECK_SVG = '<svg width="{s}" height="{s}" viewBox="0 0 64 64" aria-hidden="true" data-w="{w}"><g transform="translate(0.0 0.0) scale(1.0)"><defs><mask id="k0" maskUnits="userSpaceOnUse" x="-20" y="-20" width="104" height="104"><rect x="-20" y="-20" width="104" height="104" fill="#fff"/><rect x="24" y="25" width="16" height="25" rx="2.5" transform="rotate(30 32 52)" fill="#000" stroke="#000" stroke-width="2.6"/><rect x="24" y="25" width="16" height="25" rx="2.5" transform="rotate(-15 32 52)" fill="#000" stroke="#000" stroke-width="2.6"/><rect x="24" y="25" width="16" height="25" rx="2.5" transform="rotate(15 32 52)" fill="#000" stroke="#000" stroke-width="2.6"/><rect x="24" y="23" width="16" height="27" rx="2.5" fill="#000" stroke="#000" stroke-width="5.2"/></mask><mask id="k1" maskUnits="userSpaceOnUse" x="-20" y="-20" width="104" height="104"><rect x="-20" y="-20" width="104" height="104" fill="#fff"/><rect x="24" y="25" width="16" height="25" rx="2.5" transform="rotate(-15 32 52)" fill="#000" stroke="#000" stroke-width="2.6"/><rect x="24" y="25" width="16" height="25" rx="2.5" transform="rotate(15 32 52)" fill="#000" stroke="#000" stroke-width="2.6"/><rect x="24" y="23" width="16" height="27" rx="2.5" fill="#000" stroke="#000" stroke-width="5.2"/></mask><mask id="k2" maskUnits="userSpaceOnUse" x="-20" y="-20" width="104" height="104"><rect x="-20" y="-20" width="104" height="104" fill="#fff"/><rect x="24" y="25" width="16" height="25" rx="2.5" transform="rotate(15 32 52)" fill="#000" stroke="#000" stroke-width="2.6"/><rect x="24" y="23" width="16" height="27" rx="2.5" fill="#000" stroke="#000" stroke-width="5.2"/></mask><mask id="k3" maskUnits="userSpaceOnUse" x="-20" y="-20" width="104" height="104"><rect x="-20" y="-20" width="104" height="104" fill="#fff"/><rect x="24" y="23" width="16" height="27" rx="2.5" fill="#000" stroke="#000" stroke-width="5.2"/></mask></defs><g transform="translate(0 0.5)"><g fill="none" stroke="#D4AE5C" stroke-width="2.6" stroke-linejoin="round" stroke-linecap="round"><path d="M5 28 L32 6 L59 28"/><g mask="url(#k0)"><rect x="24" y="25" width="16" height="25" rx="2.5" transform="rotate(-30 32 52)"/></g><g mask="url(#k1)"><rect x="24" y="25" width="16" height="25" rx="2.5" transform="rotate(30 32 52)"/></g><g mask="url(#k2)"><rect x="24" y="25" width="16" height="25" rx="2.5" transform="rotate(-15 32 52)"/></g><g mask="url(#k3)"><rect x="24" y="25" width="16" height="25" rx="2.5" transform="rotate(15 32 52)"/></g><path d="M10 57 H54"/></g><path fill="#D4AE5C" fill-rule="evenodd" d="M26.5 21.7 H37.5 A3.8 3.8 0 0 1 41.3 25.5 V47.5 A3.8 3.8 0 0 1 37.5 51.3 H26.5 A3.8 3.8 0 0 1 22.7 47.5 V25.5 A3.8 3.8 0 0 1 26.5 21.7 Z M26.605 41.141 28.997 32.041H31.987L34.379 41.141H32.611L32.117 39.139H28.867L28.373 41.141ZM29.27 37.553H31.714L30.609 33.12H30.375Z M35.523 41.141V34.693H37.161V41.141Z M36.34 29.299999999999997 Q36.34 31.9 38.940000000000005 31.9 Q36.34 31.9 36.34 34.5 Q36.34 31.9 33.74 31.9 Q36.34 31.9 36.34 29.299999999999997 Z"/></g></g></svg>'
DIAMOND = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="#D4AF5A" aria-hidden="true"><path d="M12 2l7 10-7 10-7-10z"/></svg>'

SNIP = {
    "CHECK": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#D4AF5A" stroke-width="2.2" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
    "CHECKSM": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#8A6A1F" stroke-width="2.4" aria-hidden="true" style="flex:none;margin-top:1px"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
    "ARROW": '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "FLOWARROW": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#8A6A1F" stroke-width="2" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
    "DECKICON": DECK_SVG.format(s=40, w=1.3),
    "FAN": ('<div class="fan" role="img" aria-label="The AI Agent Deck: 5 cards plus 2 bonus cards, launch price $49">'
            '<div class="c c1"></div><div class="c c2"></div>'
            '<div class="front">' + DECK_SVG.format(s=56, w=1.2) +
            '<div class="t">The AI<br>Agent Deck</div><div class="bar"></div><div class="s">5 cards + 2 bonus cards</div></div>'
            '<div class="badge"><small><s>$199</s></small><b>$49</b></div></div>'),
    "BUYFINE": ('By buying, you agree to the <a href="/terms/">Terms</a>. Needs the Claude desktop app and a paid Claude plan '
                '(Claude Pro is currently $20/month), sold separately by Anthropic; heavier use may need a higher plan. Claude helps you set it up; it is do-it-yourself. All sales are final.'),
}

FAQ = [
    ("Are these physical cards?", "No. They are digital. Nothing is printed and nothing is mailed. You get a download link by email right after checkout."),
    ("Is it done for me?", "No. It's a do-it-yourself toolkit. You paste one prompt into Claude, answer simple questions, and approve what it sets up. The full Deck takes about 20 minutes. The Lead-for-Life System takes another hour or two to build your follow-up plan in your CRM and write your own emails."),
    ("What else do I need?", "The Claude desktop app and a paid Claude plan (Claude Pro is currently $20/month), sold separately by Anthropic. The more cards you run and the more often they update, the more of your Claude plan they use, so you may need a higher plan as you grow. Google Sheets or Excel. A CRM is optional; if Claude has a connector for it, Claude can read it directly."),
    ("Will it contact my leads for me?", "No. It drafts messages for you to review and send. It never texts, calls or emails anyone on its own."),
    ("Will it get me more deals?", "We don't promise more leads, listings, closings or income. It shows you your numbers and what needs you; results depend on your work."),
    ("Can I get a refund?", "All sales are final because the files are delivered instantly and you keep them. Please read this page and the Terms before you buy. If a file is missing or won't open, email us and we'll fix it."),
    ("Do I get a spreadsheet or a dashboard?", "Both are in the box and you choose. Every card comes with a workbook for Google Sheets or Excel. During setup Claude asks whether you want a live dashboard as your main view; if you say yes, Claude builds it for you inside Claude from your own numbers, and the workbook stays as the place your data lives. You can <a href=\"/demo/\">try a sample dashboard</a> before you buy."),
    ("Can I try it before I buy?", "Yes. Two cards are free: the <a href=\"/free/\">Listing Watchdog and Morning Brief</a>. There is also a <a href=\"/demo/\">live demo of the KPI dashboard</a> with sample data."),
    ("Can I talk to someone?", "Yes. Call " + extras.PHONE_DISPLAY + " any time; Sarah answers around the clock and can walk you through the cards. Or email support@aidealdeck.com."),
    ("Is this made by Anthropic?", "No. AiDealDeck is an independent product built to work with Claude. It is not made or endorsed by Anthropic."),
]

SLUGS = {c["n"]: c["slug"] for c in extras.CARDS}

def faq_html():
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    return f'<div class="faq">{items}</div><p class="center" style="margin-top:22px"><a href="/faq/"><b>See all questions and answers</b></a></p>'

def card(m):
    num, tag, name, body, url, tilt = m.group(1).split("|")
    slug = SLUGS.get(num, "")
    more = f'<a class="more" href="/cards/{slug}/">What is inside</a>' if slug else ""
    pip = f'{num}{DIAMOND.format(s=16)}'
    return (f'<div class="pcard" style="transform:rotate({tilt})">'
            f'<div class="top"><div class="pip">{pip}</div><div class="tag">{tag}</div></div>'
            f'<h3>{name}</h3><div class="rule"></div><p>{body}</p>{more}'
            f'<a class="single" href="{url}" data-upsell="single" data-buy="{re.sub("&amp;", "&", name)}" data-value="19">Buy this card: <s>$49</s> $19</a>'
            f'<div class="pip bottom">{num}{DIAMOND.format(s=14)}</div></div>')


CARD_DEFS = [
    ("1", "Your numbers", "Real Estate KPI Tracker", "See how many leads turn into closings, step by step. It also gives you one number to hit each week to reach your goal.", "KPI", "-2deg"),
    ("2", "Your listings", "Listing Exposure Playbook", "A 14-day plan for every new listing. It tells you what to do each day and gives you a report to show the seller.", "LISTING", "1deg"),
    ("3", "Your new leads", "Lead-for-Life System", "Call every new lead fast. Then follow a set plan until they book. It also tracks how fast you call.", "LEAD", "-1deg"),
    ("4", "Your money", "Commission &amp; GCI Ledger", "Write down every closing and what you were paid. See what you really kept this year.", "GCI", "2deg"),
    ("5", "Your assistant", "VA Playbook &amp; Scorecard", "A clear daily job for your assistant: three tasks, a routine, a report each night and a score each week.", "VA", "-1deg"),
]

class _M:
    def __init__(self, s): self.s = s
    def group(self, i): return self.s

VIDEO = '''<section id="how">
<div class="wrap">
<div class="center"><div class="eyebrow">Watch &middot; 36 seconds</div><h2 class="h2">How does AiDealDeck work?</h2></div>
<video controls playsinline preload="none" poster="/assets/video/how-it-works.jpg" style="display:block;width:100%;max-width:960px;aspect-ratio:16/9;margin:28px auto 0;border-radius:16px;border:1px solid rgba(212,175,90,.55);background:#0E1730"><source src="/assets/video/how-it-works.mp4" type="video/mp4"></video>
<p class="center" style="margin:28px 0 0"><a class="btn" href="https://shop.aidealdeck.com/l/the-ai-agent-deck?wanted=true" data-buy="The AI Agent Deck" data-value="49">Get the Deck: <s class="strike sm">$199</s> $49</a></p>
<p class="center" style="margin-top:18px;color:var(--muted)">Rather have it set up for you? Email <a href="mailto:support@aidealdeck.com">support@aidealdeck.com</a> and ask about done-for-you setup.</p>
</div>
</section>'''

VIDEO2 = '''<section class="dark" id="magic">
<div class="wrap">
<div class="center"><div class="eyebrow">Watch &middot; 28 seconds</div><h2 class="h2">Watch the cards go to work</h2></div>
<video controls playsinline preload="none" poster="/assets/video/cards-go-to-work.jpg" style="display:block;width:100%;max-width:960px;aspect-ratio:16/9;margin:28px auto 0;border-radius:16px;border:1px solid rgba(212,175,90,.55);background:#0E1730"><source src="/assets/video/cards-go-to-work.mp4" type="video/mp4"></video>
<p class="center" style="margin:28px 0 0"><a class="btn" href="https://shop.aidealdeck.com/l/the-ai-agent-deck?wanted=true" data-buy="The AI Agent Deck" data-value="49">Get the Deck: <s class="strike sm">$199</s> $49</a></p>
</div>
</section>'''

def cardgrid_html():
    cards = "".join(card(_M("|".join([n, tag, name, body, URLS[key], tilt]))) for n, tag, name, body, key, tilt in CARD_DEFS)
    deck = ('<div class="pcard deck">' + SNIP["DECKICON"] +
            '<h3>The full deck: all five cards, plus two bonus cards.</h3>'
            f'<a class="btn block" href="{URLS["DECK"]}" data-buy="The AI Agent Deck" data-value="49">Get the Deck: <s class="strike sm">$199</s> $49</a></div>')
    fine = ('<p class="center fine" style="margin-top:20px">Each card alone: <s>$49</s> $19 <span data-sale>Black Friday launch price</span> through Nov 30 ($49 is the regular price, starting Dec 1). '
            'The Deck gets you all five plus both bonus cards for $49 now; $199 is the regular price, starting Dec 1.</p>')
    allin = ('<label class="allin"><input type="checkbox" data-allin> <span><b>Make it the full Deck: all 5 cards + 2 bonus cards for $49</b>'
             '<small>Five single cards would be $95. Tick this and every card below takes you to the $49 Deck instead.</small></span></label>')
    js = ('<script>(function(){document.querySelectorAll("[data-allin]").forEach(function(cb){var box=cb.closest("section")||document;'
          'cb.addEventListener("change",function(){box.querySelectorAll("a.single").forEach(function(a){'
          'if(!a.dataset.h0){a.dataset.h0=a.getAttribute("href");a.dataset.b0=a.dataset.buy;a.dataset.t0=a.innerHTML;}'
          'if(cb.checked){a.setAttribute("href",a.dataset.h0.replace(/\\/l\\/[^?]+/,"/l/the-ai-agent-deck"));a.dataset.buy="The AI Agent Deck";a.dataset.value="49";a.innerHTML="Get all 5 cards + 2 bonuses: $49";a.classList.add("deckd");}'
          'else{a.setAttribute("href",a.dataset.h0);a.dataset.buy=a.dataset.b0;a.dataset.value="19";a.innerHTML=a.dataset.t0;a.classList.remove("deckd");}});});});})();</script>')
    return f'{allin}<div class="cards" id="cards">{cards}{deck}</div>{fine}{js}'

def shop_section():
    return ('<section id="shop"><div class="wrap"><div class="center"><div class="eyebrow">Buy one card or the whole deck</div>'
            '<h2 class="h2">Pick your cards</h2><p class="lead">Start with one card for $19, or get all five plus both bonus cards for $49.</p></div>'
            + cardgrid_html() + '</div></section>')

UPSELL = '''
<dialog id="offer" aria-labelledby="offer-h">
<form method="dialog"><button class="x" aria-label="Close">×</button></form>
<div data-step="deck">
<div class="eyebrow">Before you check out</div>
<h2 id="offer-h" class="h2" style="font-size:28px">Get the whole deck for <s class="strike sm">$199</s> $49?</h2>
<p class="lead" style="font-size:16px">All five cards plus the Listing Watchdog and Morning Brief bonus cards. One card alone is $19, so the Deck is five cards for the price of about two and a half.</p>
<a class="btn block" style="margin-top:20px" href="__DECK__" data-buy="The AI Agent Deck" data-value="49">Yes, get the full Deck: $49</a>
<button type="button" class="no" data-next>No thanks</button>
<p class="fine" style="margin-top:10px"><span data-sale>Black Friday launch price</span> through Nov 30. $199 is the regular price, starting Dec 1.</p>
</div>
<div data-step="card" hidden>
<div class="eyebrow">One more option</div>
<h2 class="h2" style="font-size:28px">Add just the KPI Tracker for <s class="strike sm">$49</s> $19?</h2>
<p class="lead" style="font-size:16px">Card 1: see where your deals leak and the weekly number that gets you to your goal. It is a separate purchase from your free download.</p>
<a class="btn block" style="margin-top:20px" href="__KPI__" data-buy="Real Estate KPI Tracker" data-value="19">Yes, get the KPI Tracker: $19</a>
<button type="button" class="no" data-next>No thanks, just my free cards</button>
</div>
</dialog>
<script>
(function(){var d=document.getElementById('offer');if(!d||!d.showModal)return;var dest=null,steps=[],i=0;
function show(){d.querySelectorAll('[data-step]').forEach(function(s){s.hidden=s.getAttribute('data-step')!==steps[i]});}
document.addEventListener('click',function(e){var a=e.target.closest('a[data-upsell]');if(a){e.preventDefault();dest=a.href;steps=a.getAttribute('data-upsell')==='free'?['deck','card']:['deck'];i=0;show();d.showModal();return;}
if(e.target.closest('[data-next]')){i++;if(i>=steps.length){d.close();window.location.href=dest;}else show();}});
d.addEventListener('close',function(){i=0;});})();
</script>
'''

def stack_html():
    cells = "".join('<i class="on"></i>' if i < 7 else "<i></i>" for i in range(52))
    return f'''<section class="darker">
<div class="wrap stack">
<div class="copy">
<div class="eyebrow gold">This is your starting hand</div>
<h2 class="h2">Start with seven cards. Add more later.</h2>
<p class="lead" style="margin-left:0">The Deck gives you seven cards today. When we make new cards, each one works with the cards you already have.</p>
<p class="lead" style="margin-left:0">Get all seven now at the $49 launch price.</p>
<a class="btn" style="margin-top:28px" href="{URLS["DECK"]}" data-buy="The AI Agent Deck" data-value="49">Start my deck: $49</a>
<p class="fine" style="margin-top:14px">Future cards are separate products, sold separately when released. No release dates are promised.</p>
</div>
<div class="board" role="img" aria-label="A 52-card deck with 7 cards filled in and 45 empty slots">
<div style="display:flex;justify-content:space-between;align-items:baseline;gap:12px;flex-wrap:wrap"><b style="color:#fff;font-size:17px">Your deck</b><span style="font-size:14px;color:var(--gold);font-weight:600">7 cards in your starting hand</span></div>
<div class="grid52">{cells}</div>
<div class="legend"><span><i style="width:12px;height:16px;background:var(--gold);border-radius:2px;display:inline-block"></i>In The AI Agent Deck</span><span><i style="width:12px;height:16px;border:1px dashed #4A5A88;border-radius:2px;display:inline-block"></i>Room to grow</span></div>
</div>
</div>
</section>'''

SHOT_DIR = os.path.join(ROOT, "assets", "shots")
SHOT_CAPTIONS = {
    "live": "Example of the live dashboard Claude builds from your KPI Tracker (sample data; yours may look different)",
    "kpi": "KPI Tracker spreadsheet dashboard (sample data)",
    "gci": "Commission & GCI Ledger (sample data)",
    "watch": "Listing Watchdog summary (sample data)",
}

def shot_file(key):
    if not os.path.isdir(SHOT_DIR):
        return None
    for f in sorted(os.listdir(SHOT_DIR)):
        if f.startswith(key + "."):
            return f
    return None

def shot_fig(key):
    f = shot_file(key)
    if not f:
        return ""
    cap = SHOT_CAPTIONS[key].replace("&", "&amp;")
    return f'<figure class="shot" style="margin:0"><img src="/assets/shots/{f}" alt="{cap}"><figcaption>{cap}</figcaption></figure>'

def shots_section():
    figs = "".join(shot_fig(k) for k in SHOT_CAPTIONS)
    if not figs:
        return ""  # no placeholders on the live site
    vid = '<video controls playsinline preload="none" poster="/assets/video/kpi-tracker.jpg" style="display:block;width:100%;max-width:960px;aspect-ratio:16/9;margin:28px auto 8px;border-radius:16px;border:1px solid rgba(212,175,90,.55);background:#0E1730"><source src="/assets/video/kpi-tracker.mp4" type="video/mp4"></video><p class="center" style="color:var(--muted);margin:0 0 28px">The KPI dashboard Claude helps you build, 29 seconds. Sample data. <a href="/demo/"><b>Play with the live demo</b></a></p><p class="center" style="margin:0 0 8px"><a class="btn" href="' + URLS["KPI"] + '" data-buy="Real Estate KPI Tracker" data-value="19">Get the KPI Tracker: <s class="strike sm">$49</s> $19 ' + SNIP.get("ARROW", "") + '</a></p>'
    return f'<section class="white"><div class="wrap"><h2 class="h2 center">See it before you buy</h2>{vid}<div class="carousel"><button type="button" class="cbtn prev" aria-label="Previous picture">&#8249;</button><div class="shots" id="shots">{figs}</div><button type="button" class="cbtn next" aria-label="Next picture">&#8250;</button></div><script>(function(){{var s=document.getElementById("shots");if(!s)return;function go(d){{s.scrollBy({{left:d*s.clientWidth,behavior:"smooth"}});}}s.parentNode.querySelector(".prev").onclick=function(){{go(-1);}};s.parentNode.querySelector(".next").onclick=function(){{go(1);}};}})();</script></div></section>'

def render(body):
    body = re.sub(r"\{\{CARD:(.+?)\}\}(?=\s*\n)", lambda m: card(m) if "{{" not in m.group(1) else m.group(0), body)
    for k, v in URLS.items():
        body = body.replace("{{" + k + "}}", v)
    body = re.sub(r"\{\{CARD:(.+?)\}\}", card, body)
    body = body.replace("{{CARDGRID}}", cardgrid_html()).replace("{{SHOP}}", shop_section())
    body = body.replace("{{VIDEO2}}", VIDEO2).replace("{{VIDEO}}", VIDEO)
    body = body.replace("{{STACK}}", stack_html()).replace("{{SHOTS}}", shots_section()).replace("{{FAQ}}", faq_html())
    body = re.sub(r"\{\{SHOT:(\w+)\}\}", lambda m: (f'<div class="shots" style="grid-template-columns:1fr">{shot_fig(m.group(1))}</div>' if shot_fig(m.group(1)) else ""), body)
    for k, v in SNIP.items():
        body = body.replace("{{" + k + "}}", v)
    return body

def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    head = open(os.path.join(SRC, "_head.html")).read()
    import hashlib
    head = head.replace("/assets/site.css\"", "/assets/site.css?v=" + hashlib.md5(open(os.path.join(ROOT, "assets", "site.css"), "rb").read()).hexdigest()[:8] + "\"")
    foot = open(os.path.join(SRC, "_foot.html")).read()
    pages = []
    for name in sorted(os.listdir(SRC)):
        if name.startswith("_") or not name.endswith(".html"):
            continue
        raw = open(os.path.join(SRC, name)).read()
        meta_m = re.match(r"<!--META (.*?) -->\n", raw, re.S)
        pages.append((json.loads(meta_m.group(1)), raw[meta_m.end():]))
    plain_faq = [(q, re.sub(r"<[^>]+>", "", a)) for q, a in FAQ]
    for c in extras.CARDS:
        meta = {"out": f"cards/{c['slug']}/index.html", "path": f"/cards/{c['slug']}/",
                "title": f"{c['name']} for real estate pros | AiDealDeck".replace("&", "&amp;"),
                "desc": (c["short"] + " Launch price $19 through Nov 30.").replace("&", "&amp;"),
                "topnote": "<span data-sale>Black Friday</span>: this card is $19, not $49. <b data-left>Ends Nov 30.</b>",
                "topbtn": "<a class=\"btn sm\" href=\"{{DECK}}\" data-buy=\"The AI Agent Deck\" data-value=\"49\">Get the Deck</a>",
                "pixel": "fbq('track','ViewContent',{content_name:'" + c["name"].replace("&", "and") + "',value:19,currency:'USD'});",
                "ld": [extras.card_ld(c, extras.SITE + f"/cards/{c['slug']}/"), extras.faq_ld(plain_faq)]}
        pages.append((meta, extras.card_page(c, URLS, SNIP, faq_html(), shop_section())))
    long_plain = [(q, re.sub(r"<[^>]+>", "", a)) for q, a, k, c in faq_data.flat()]
    pages.append(({"out": "faq/index.html", "path": "/faq/", "title": "Questions and answers | AiDealDeck",
                   "desc": "Straight answers about AiDealDeck: what the cards do, what you need, setup, price, refunds, privacy and what they do not do.",
                   "topnote": "<span data-sale>Black Friday</span>: all 5 cards + 2 bonus cards for $49, not $199. <b data-left>Ends Nov 30.</b>",
                   "topbtn": "<a class=\"btn sm\" href=\"{{DECK}}\" data-buy=\"The AI Agent Deck\" data-value=\"49\">Get the Deck</a>",
                   "pixel": "", "ld": [extras.faq_ld(long_plain)]}, extras.faq_page(faq_data.FAQ_LONG)))
    LD = {
        "index.html": [extras.deck_ld(extras.SITE + "/"), extras.faq_ld(plain_faq),
                       extras.video_ld("How does AiDealDeck work?", "A 36-second look at how a real estate agent sets up an AiDealDeck card with Claude.", "how-it-works", 36),
                       extras.video_ld("The KPI dashboard Claude helps you build", "A 29-second look at the live real estate KPI dashboard, with sample data.", "kpi-tracker", 29),
                       extras.video_ld("Watch the cards go to work", "A 28-second look at the five AiDealDeck cards.", "cards-go-to-work", 28)],
        "numbers/index.html": [extras.card_ld(extras.CARDS[0], extras.SITE + "/numbers/"), extras.faq_ld(plain_faq)],
        "free/index.html": [{"@type": "Product", "name": "Free cards: Listing Watchdog and Morning Brief", "brand": {"@type": "Brand", "name": "AiDealDeck"},
                             "image": extras.SITE + "/assets/og.png",
                             "description": "Two free AiDealDeck cards for real estate pros. Listing Watchdog tells you when someone you are watching lists with another agent. Morning Brief is one short summary from Claude each morning.",
                             "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD", "availability": "https://schema.org/InStock", "url": extras.SITE + "/free/"}}],
    }
    SALES = lambda out: out not in ("terms/index.html", "privacy/index.html", "feedback/index.html", "start/index.html", "unsubscribe/index.html")
    sitemap = []
    for meta, body in pages:
        name = meta["out"]
        ld = extras.ld_script(meta.get("ld") or LD.get(name, []))
        h = (head.replace("{{TITLE}}", meta["title"]).replace("{{DESC}}", meta["desc"]).replace("{{PATH}}", meta["path"])
                 .replace("{{TOPNOTE}}", meta["topnote"]).replace("{{TOPBTN}}", meta["topbtn"] or '<a class="btn sm" href="' + URLS["DECK"] + '" data-buy="The AI Agent Deck" data-value="49">Get the Deck</a>').replace("{{PIXEL_EXTRA}}", meta["pixel"]).replace("{{LD}}", ld))
        tail = extras.nudge(URLS["FREE"], bar=False) + extras.after_free(URLS) + extras.chat()
        if SALES(name):
            tail = (extras.leadband(URLS["FREE"]) if name != "free/index.html" else "") + extras.nudge(URLS["FREE"]).replace("__DECK__", URLS["DECK"]) + extras.pick().replace("__FREE__", URLS["FREE"]) + extras.after_free(URLS) + extras.chat()
        f = foot.replace("{{PHONE_TEL}}", extras.PHONE_TEL).replace("{{PHONE}}", extras.PHONE_DISPLAY)
        page = render(h + body + tail + f)
        page = page.replace(' data-upsell="single"', '').replace(' data-upsell="free"', '')
        leftover = re.findall(r"\{\{[A-Z_:]+.*?\}\}", page)
        assert not leftover, f"{name}: unreplaced {leftover[:3]}"
        dest = os.path.join(OUT, name)
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        if name in ("feedback/index.html", "start/index.html", "unsubscribe/index.html", "numbers/index.html"): page = page.replace('content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"', 'content="noindex,follow"')
        open(dest, "w").write(page)
        if name not in ("feedback/index.html", "start/index.html", "unsubscribe/index.html", "numbers/index.html"): sitemap.append(meta["path"])
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    open(os.path.join(OUT, "CNAME"), "w").write("aidealdeck.com\n")
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    open(os.path.join(OUT, "robots.txt"), "w").write("User-agent: *\nAllow: /\n\n# AI search and answer engines are welcome. See /llms.txt for a plain-text summary.\n" + "".join("User-agent: %s\nAllow: /\n\n" % b for b in ("GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "PerplexityBot", "Google-Extended", "Applebot-Extended", "CCBot")) + "Sitemap: https://aidealdeck.com/sitemap.xml\n")
    prio = lambda p: "1.0" if p == "/" else ("0.3" if p in ("/terms/", "/privacy/") else "0.8")
    open(os.path.join(OUT, "sitemap.xml"), "w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"<url><loc>https://aidealdeck.com{p}</loc><lastmod>{BUILD_DATE}</lastmod><priority>{prio(p)}</priority></url>\n" for p in sorted(sitemap)) + "</urlset>\n")
    import json as _json
    open(os.path.join(OUT, "faq.json"), "w").write(_json.dumps([{"q": q, "a": a_, "k": k} for q, a_, k, _c in faq_data.flat()]))
    open(os.path.join(OUT, "llms.txt"), "w").write(extras.llms_txt(extras.CARDS, long_plain))
    print("built:", sorted(os.path.relpath(os.path.join(d, f), OUT) for d, _, fs in os.walk(OUT) for f in fs))

if __name__ == "__main__":
    main()
