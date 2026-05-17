#!/usr/bin/env python3
"""Fetch intraday data for S&P 500, Nasdaq, Dow Jones from Yahoo Finance."""

import json
import ssl
import sys
import urllib.request
from datetime import datetime, timezone

SYMBOLS = [
    ("^GSPC",   "S&P 500"),
    ("^IXIC",   "NASDAQ"),
    ("^DJI",    "DOW JONES"),
    ("BTC-USD", "BITCOIN"),
    ("GC=F",    "GOLD"),
]

_CTX = ssl.create_default_context()


def fetch_symbol(symbol):
    url = (
        f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
        "?interval=5m&range=1d&includePrePost=false"
    )
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15, context=_CTX) as r:
        raw = json.loads(r.read())

    result = raw["chart"]["result"][0]
    meta = result["meta"]
    price = float(meta["regularMarketPrice"])
    prev = float(meta.get("chartPreviousClose") or meta["previousClose"])
    change = price - prev
    pct = (change / prev) * 100.0

    timestamps = result.get("timestamp") or []
    closes = (result.get("indicators", {}).get("quote") or [{}])[0].get("close") or []
    series = [(t, c) for t, c in zip(timestamps, closes) if c is not None]

    return {
        "symbol": symbol,
        "price": price,
        "prev_close": prev,
        "change": change,
        "pct": pct,
        "series": series,
        "market_state": meta.get("marketState"),
        "currency": meta.get("currency", "USD"),
        "exchange_tz": meta.get("exchangeTimezoneName"),
    }


def fetch_all():
    out = {"fetched_at_utc": datetime.now(timezone.utc).isoformat(), "indices": []}
    for sym, label in SYMBOLS:
        data = fetch_symbol(sym)
        data["label"] = label
        out["indices"].append(data)
    return out


if __name__ == "__main__":
    data = fetch_all()
    json.dump(data, sys.stdout, indent=2)
    print()
