#!/usr/bin/env python3
"""Submit all URLs to IndexNow (Bing, Yandex, DuckDuckGo) for fast indexing."""
import json
import urllib.request
import xml.etree.ElementTree as ET

SITEMAP = "sitemap.xml"
HOST = "svipan.is"
KEY = "df3e0f37c9a14d9d92d42bd6e5f7ef22"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

# Parse sitemap
tree = ET.parse(SITEMAP)
ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
urls = [loc.text for loc in tree.findall(".//s:loc", ns)]
print(f"Found {len(urls)} URLs in sitemap")

# Submit to IndexNow (Bing endpoint — shared with Yandex, DuckDuckGo)
payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": urls
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=data,
    headers={"Content-Type": "application/json; charset=utf-8"},
    method="POST"
)

try:
    resp = urllib.request.urlopen(req)
    print(f"✅ IndexNow submitted {len(urls)} URLs — HTTP {resp.status}")
except urllib.error.HTTPError as e:
    print(f"❌ IndexNow error: HTTP {e.code} — {e.read().decode()}")
except Exception as e:
    print(f"❌ Error: {e}")
