"""One switch for the launch sale. The build reads it; so do the FAQ and llms.txt.

SALE is True through Nov 30, 2026 (Central time) and False from Dec 1. Set ADD_SALE=1 or ADD_SALE=0 in the
environment to force either state, for example to preview the regular-price site before the date:
    ADD_SALE=0 python3 build.py
The pages also flip a few things on their own after the deadline (Sarah's greeting, the top-bar countdown), but the
printed prices only change when the site is rebuilt, so rebuild on Dec 1 (the GitHub Action does this)."""
import datetime, os

SALE_ENDS = datetime.date(2026, 11, 30)
_env = os.environ.get("ADD_SALE")
if _env in ("0", "1"):
    SALE = _env == "1"
else:
    # Central time without pulling in zoneinfo: the sale ends at 06:00 UTC on Dec 1.
    SALE = datetime.datetime.utcnow() < datetime.datetime(2026, 12, 1, 6, 0, 0)

DECK_PRICE = 49 if SALE else 199
CARD_PRICE = 19 if SALE else 49
DECK_REGULAR = 199
CARD_REGULAR = 49
