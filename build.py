#!/usr/bin/env python3
"""Builds the static Ai Deal Deck site from src/ into public/."""
import json, os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, OUT = os.path.join(ROOT, "src"), os.path.join(ROOT, "docs")
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

DECK_SVG = '<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="#D4AF5A" stroke-width="{w}" aria-hidden="true"><rect x="3" y="6" width="10" height="14" rx="1.5" transform="rotate(-12 8 13)"/><rect x="7" y="4" width="10" height="14" rx="1.5"/><rect x="11" y="6" width="10" height="14" rx="1.5" transform="rotate(12 16 13)"/></svg>'
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
                '(Claude Pro is currently $20/month), sold separately by Anthropic. All sales are final.'),
}

FAQ = [
    ("Is it done for me?", "No. It's a do-it-yourself toolkit. Setup takes about 20 minutes per card: paste one prompt into Claude, answer simple questions, and approve what it sets up. The Lead-for-Life System takes another hour or two to build your follow-up plan in your CRM and write your own emails."),
    ("What else do I need?", "The Claude desktop app and a paid Claude plan (Claude Pro is currently $20/month), sold separately by Anthropic. Google Sheets or Excel. A CRM is optional; if Claude has a connector for it, Claude can read it directly."),
    ("Will it contact my leads for me?", "No. It drafts messages for you to review and send. It never texts, calls or emails anyone on its own."),
    ("Will it get me more deals?", "We don't promise more leads, listings, closings or income. It shows you your numbers and what needs you; results depend on your work."),
    ("Can I get a refund?", "All sales are final because the files are delivered instantly and you keep them. Please read this page and the Terms before you buy. If a file is missing or won't open, email us and we'll fix it."),
    ("Is this made by Anthropic?", "No. Ai Deal Deck is an independent product built to work with Claude. It is not made or endorsed by Anthropic."),
]

def faq_html():
    items = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)
    return f'<div class="faq">{items}</div>'

def card(m):
    num, tag, name, body, url, tilt = m.group(1).split("|")
    pip = f'{num}{DIAMOND.format(s=16)}'
    return (f'<div class="pcard" style="transform:rotate({tilt})">'
            f'<div class="top"><div class="pip">{pip}</div><div class="tag">{tag}</div></div>'
            f'<h3>{name}</h3><div class="rule"></div><p>{body}</p>'
            f'<a class="single" href="{url}" data-upsell="single" data-buy="{re.sub("&amp;", "&", name)}" data-value="19">Buy this card: <s>$49</s> $19</a>'
            f'<div class="pip bottom">{num}{DIAMOND.format(s=14)}</div></div>')


CARD_DEFS = [
    ("1", "Your numbers", "Real Estate KPI Tracker", "Lead → appointment → signed → under contract → closed, with the real percentage at each step, and the weekly number you need to hit your goal.", "KPI", "-2deg"),
    ("2", "Your listings", "Listing Exposure Playbook", "A repeatable 14-day launch plan for every listing, with fill-in templates and day-7 and day-14 seller reports.", "LISTING", "1deg"),
    ("3", "Your new leads", "Lead-for-Life System", "Every new lead contacted fast, then followed up on a set plan until they book. Includes a speed scorecard and a TCPA checklist.", "LEAD", "-1deg"),
    ("4", "Your money", "Commission &amp; GCI Ledger", "Every closing, fee, referral fee and split in one place, with team totals kept separate from your own income.", "GCI", "2deg"),
    ("5", "Your assistant", "VA Playbook &amp; Scorecard", "A narrow assistant role with three jobs, a daily routine, an end-of-day report and a weekly scorecard.", "VA", "-1deg"),
]

class _M:
    def __init__(self, s): self.s = s
    def group(self, i): return self.s

def cardgrid_html():
    cards = "".join(card(_M("|".join([n, tag, name, body, URLS[key], tilt]))) for n, tag, name, body, key, tilt in CARD_DEFS)
    deck = ('<div class="pcard deck">' + SNIP["DECKICON"] +
            '<h3>The full deck: all five cards, plus two bonus cards.</h3>'
            f'<a class="btn block" href="{URLS["DECK"]}" data-buy="The AI Agent Deck" data-value="49">Get the Deck: <s class="strike sm">$199</s> $49</a></div>')
    fine = ('<p class="center fine" style="margin-top:20px">Each card alone: <s>$49</s> $19 launch price through Nov 30 ($49 is the regular price, starting Dec 1). '
            'The Deck gets you all five plus both bonus cards for $49 now; $199 is the regular price, starting Dec 1.</p>')
    return f'<div class="cards" id="cards">{cards}{deck}</div>{fine}'

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
<p class="fine" style="margin-top:10px">Launch price through Nov 30. $199 is the regular price, starting Dec 1.</p>
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
<h2 class="h2">Start your deck today. Stack it into a full AI system.</h2>
<p class="lead" style="margin-left:0">The AI Agent Deck is your first seven cards. New cards will cover more of your business, and each one you add plugs into the same deck, so your Morning Brief sees more and Claude knows more of your business with every card you play.</p>
<p class="lead" style="margin-left:0">Lock in the starting hand at the $49 launch price, and every new card has a place waiting for it.</p>
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
    "kpi": "KPI Tracker funnel view (sample data)",
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
    return f'<section class="white"><div class="wrap"><h2 class="h2 center">See it before you buy</h2><div class="shots">{figs}</div></div></section>'

def render(body):
    body = re.sub(r"\{\{CARD:(.+?)\}\}(?=\s*\n)", lambda m: card(m) if "{{" not in m.group(1) else m.group(0), body)
    for k, v in URLS.items():
        body = body.replace("{{" + k + "}}", v)
    body = re.sub(r"\{\{CARD:(.+?)\}\}", card, body)
    body = body.replace("{{CARDGRID}}", cardgrid_html()).replace("{{SHOP}}", shop_section())
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
    foot = open(os.path.join(SRC, "_foot.html")).read()
    for name in sorted(os.listdir(SRC)):
        if name.startswith("_") or not name.endswith(".html"):
            continue
        raw = open(os.path.join(SRC, name)).read()
        meta_m = re.match(r"<!--META (.*?) -->\n", raw, re.S)
        meta = json.loads(meta_m.group(1))
        body = raw[meta_m.end():]
        h = (head.replace("{{TITLE}}", meta["title"]).replace("{{DESC}}", meta["desc"]).replace("{{PATH}}", meta["path"])
                 .replace("{{TOPNOTE}}", meta["topnote"]).replace("{{TOPBTN}}", meta["topbtn"]).replace("{{PIXEL_EXTRA}}", meta["pixel"]))
        modal = UPSELL.replace("__DECK__", URLS["DECK"]).replace("__KPI__", URLS["KPI"]) if meta["out"] in ("index.html","numbers/index.html","free/index.html") else ""
        page = render(h + body + modal + foot)
        leftover = re.findall(r"\{\{[A-Z_:]+.*?\}\}", page)
        assert not leftover, f"{name}: unreplaced {leftover[:3]}"
        dest = os.path.join(OUT, meta["out"])
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "w").write(page)
    shutil.copytree(os.path.join(ROOT, "assets"), os.path.join(OUT, "assets"))
    open(os.path.join(OUT, "CNAME"), "w").write("aidealdeck.com\n")
    open(os.path.join(OUT, ".nojekyll"), "w").write("")
    open(os.path.join(OUT, "robots.txt"), "w").write("User-agent: *\nAllow: /\n")
    print("built:", sorted(os.path.relpath(os.path.join(d, f), OUT) for d, _, fs in os.walk(OUT) for f in fs))

if __name__ == "__main__":
    main()
