#!/usr/bin/env python3
"""Cluster interlinking: inject 'Tengt efni' related-links block into generated pages."""
import re, zlib
from pathlib import Path

ROOT = Path(__file__).parent
URL_BASE = "/slotoro-site/"  # preview; production build replaces via generate --production rerun order
# detect base from any generated page
try:
    probe = (ROOT/"spilaviti"/"index.html").read_text(encoding="utf-8")
    m = re.search(r'href="(/[^"]*?)spilaviti/"', probe)
    if m: URL_BASE = m.group(1)
except Exception:
    pass

SECTIONS = ["spilaviti","spilakassar","live","bonusar","greidslur","leidbeiningar"]

def h1_of(s):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    if not m: return None
    t = re.sub(r"<[^>]+>","",m.group(1)).strip()
    # trim long anchors
    t = re.sub(r"\s*[—–-]\s*(umsögn.*|RTP.*|leiðarvísir.*)$","",t,flags=re.I).strip()
    return t[:60]

# pass 1: registry
reg = {sec:{} for sec in SECTIONS}
provider = {}
for sec in SECTIONS:
    d = ROOT/sec
    if not d.is_dir(): continue
    for sub in sorted(d.iterdir()):
        f = sub/"index.html"
        if not sub.is_dir() or not f.exists(): continue
        s = f.read_text(encoding="utf-8",errors="ignore")
        t = h1_of(s)
        if not t: continue
        reg[sec][sub.name] = t
        if sec=="spilakassar":
            pm = re.search(r'frá ([A-Za-z0-9\'\.\- ]+)" class="slot-hero-img"', s)
            if pm: provider[sub.name] = pm.group(1).strip()

def rot(slug, seq, n):
    seq = [x for x in seq if x[1]!=slug]
    if not seq: return []
    i = zlib.crc32(slug.encode()) % len(seq)
    return [seq[(i+k)%len(seq)] for k in range(min(n,len(seq)))]

def link(sec, slug, title):
    return f'<a href="{URL_BASE}{sec}/{slug}/">{title}</a>'

HUBS = {"spilaviti":"Allar spilavítaumsagnir","spilakassar":"Allir spilakassar","live":"Allir lifandi leikir",
        "bonusar":"Allir bónusar","greidslur":"Allar greiðsluleiðir","leidbeiningar":"Allar leiðbeiningar"}

GUIDE_SLOTS=["hvad-er-rtp","hvad-er-sveifla","hvernig-a-ad-velja-hatt-rtp-spilakassa","lag-sveiflu-spilakassar","spilakassar-med-haesta-vinningsmoguleika"]
GUIDE_PAY=["islenskir-bankar-spilaviti","framhja-bankalokun","kaupa-bitcoin-island","spilaviti-isk-kronur","kostir-dulritunar-spilavita"]
GUIDE_CAS=["hvernig-a-ad-velja-spilaviti","hvernig-a-ad-stadfesta-spilavitaleyfi","einkenni-sanngjarns-spilavitis","spilaviti-samanburdur"]
GUIDE_BON=["hvad-eru-vedskilyrdi","hvernig-a-ad-hamarka-bonusinn","samanburdur-a-bonusum-spilavita","frisnuningar-an-innborgunar"]
GUIDE_LIVE=["hvad-er-evolution-gaming","hvad-er-pragmatic-play"]
# New SEO pages — link these from relevant sections
SEO_HUBS=["spilavitin-a-netinu-a-islandi","bestu-spilavitin-a-netinu","spilaviti-island-2026","ny-spilaviti-2026","netspilaviti-island"]

def related(sec, slug):
    out=[]
    g=reg["leidbeiningar"]
    if sec=="spilakassar":
        same=[("spilakassar",s2,reg[sec][s2]) for s2,p in provider.items() if p==provider.get(slug) and s2 in reg[sec]]
        out+=rot(slug,[(a,b,c) for a,b,c in same],3)
        others=[("spilakassar",s2,t) for s2,t in reg[sec].items() if ("spilakassar",s2,t) not in out]
        out+=rot(slug,others,4-len(out) if len(out)<4 else 1)
        out+=[("leidbeiningar",x,g[x]) for x in rot(slug,[(0,x) for x in GUIDE_SLOTS if x in g],2) for _,x in [x] ][:0]
        picks=rot(slug,[("leidbeiningar",x,g[x]) for x in GUIDE_SLOTS if x in g],2)
        out+=picks
    elif sec=="spilaviti":
        out+=rot(slug,[("spilaviti",s2,t) for s2,t in reg[sec].items()],3)
        if f"bonus-{slug}" in reg["bonusar"]:
            out.append(("bonusar",f"bonus-{slug}",reg["bonusar"][f"bonus-{slug}"]))
        out+=rot(slug,[("leidbeiningar",x,g[x]) for x in GUIDE_CAS if x in g],1)
        # Link to SEO hub pages from casino reviews
        seo_picks=rot(slug,[("leidbeiningar",x,g[x]) for x in SEO_HUBS if x in g],1)
        out+=seo_picks
    elif sec=="bonusar":
        out+=rot(slug,[("bonusar",s2,t) for s2,t in reg[sec].items()],3)
        brand=slug[len("bonus-"):] if slug.startswith("bonus-") else None
        if brand and brand in reg["spilaviti"]:
            out.append(("spilaviti",brand,reg["spilaviti"][brand]))
        out+=rot(slug,[("leidbeiningar",x,g[x]) for x in GUIDE_BON if x in g],2)
    elif sec=="greidslur":
        out+=rot(slug,[("greidslur",s2,t) for s2,t in reg[sec].items()],4)
        out+=rot(slug,[("leidbeiningar",x,g[x]) for x in GUIDE_PAY if x in g],2)
    elif sec=="live":
        out+=rot(slug,[("live",s2,t) for s2,t in reg[sec].items()],4)
        out+=rot(slug,[("leidbeiningar",x,g[x]) for x in GUIDE_LIVE if x in g],1)
        out.append(("spilaviti","live-spilaviti",reg["spilaviti"].get("live-spilaviti","Live spilavíti")))
    elif sec=="leidbeiningar":
        out+=rot(slug,[("leidbeiningar",s2,t) for s2,t in reg[sec].items()],3)
        out+=rot(slug,[("spilaviti",s2,t) for s2,t in list(reg["spilaviti"].items())[:40]],2)
        # Cross-link to SEO hub pages
        if slug not in SEO_HUBS:
            seo_picks=rot(slug,[("leidbeiningar",x,g[x]) for x in SEO_HUBS if x in g and x!=slug],1)
            out+=seo_picks
    # dedupe, drop self, cap 6
    seen=set(); res=[]
    for sec2,s2,t in out:
        if (sec2,s2)==(sec,slug) or (sec2,s2) in seen: continue
        seen.add((sec2,s2)); res.append((sec2,s2,t))
        if len(res)==6: break
    return res

STYLE=('<style>.rel-links{max-width:1140px;margin:44px auto 20px;padding:0 30px;box-sizing:border-box;}.rel-links h2{font-size:20px;margin-bottom:14px;}'
'.rel-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(230px,1fr));gap:10px;}'
'.rel-grid a{display:block;padding:12px 16px;border:1px solid rgba(255,255,255,.1);border-radius:12px;'
'background:rgba(26,29,37,.6);color:#eceef4;font-size:15px;font-weight:500;transition:border-color .2s,transform .2s;}'
'.rel-grid a:hover{border-color:rgba(214,54,65,.55);transform:translateY(-1px);}'
'.rel-hub{margin-top:12px;font-size:15px;}.rel-hub a{color:#ef6672;font-weight:600;}</style>')

MARK='class="rel-links"'
count=0
for sec in SECTIONS:
    d=ROOT/sec
    if not d.is_dir(): continue
    for sub in d.iterdir():
        f=sub/"index.html"
        if not sub.is_dir() or not f.exists(): continue
        slug=sub.name
        s=f.read_text(encoding="utf-8",errors="ignore")
        if MARK in s: continue
        rel=related(sec,slug)
        if not rel: continue
        cards="".join(link(a,b,c) for a,b,c in rel)
        hub=f'<p class="rel-hub"><a href="{URL_BASE}{sec}/">{HUBS[sec]} →</a></p>'
        block=f'{STYLE}<section class="rel-links"><h2>Tengt efni</h2><div class="rel-grid">{cards}</div>{hub}</section>'
        if '<footer class="footer">' in s:
            # inject just before footer, inside page flow
            s=s.replace('<footer class="footer">', block+'\n<footer class="footer">',1)
            f.write_text(s,encoding="utf-8")
            count+=1

# ============================================================
# PASS 2 — hub pages, info/legal pages, English pages, misc
# ============================================================

def abs_link(path, label):
    return f'<a href="{URL_BASE}{path}">{label}</a>'

def pick(sec, n):
    """n entries from a section registry, rotated by section name for variety."""
    items = sorted(reg.get(sec, {}).items())
    if not items: return []
    i = zlib.crc32(sec.encode()) % len(items)
    return [(sec, items[(i+k) % len(items)][0], items[(i+k) % len(items)][1])
            for k in range(min(n, len(items)))]

HUB_LABEL = {"spilaviti":"Spilavíti","spilakassar":"Spilakassar","live":"Lifandi spilavíti",
             "bonusar":"Bónusar","greidslur":"Greiðslur","leidbeiningar":"Leiðbeiningar"}

INFO_PAGES = [("um-okkur/","Um okkur"), ("hvernig-vid-metum/","Hvernig við metum"),
              ("ritstjornarstefna/","Ritstjórnarstefna"), ("samstarf/","Samstarf"),
              ("abyrg-spilun/","Ábyrg spilun"), ("hafa-samband/","Hafa samband"),
              ("personuvernd/","Persónuvernd"), ("skilmalar/","Skilmálar"),
              ("fyrirvari/","Fyrirvari"), ("saga/","Saga Svipan"),
              ("hofundur/valbjorn-gjukason/","Valbjörn Gjúkason"), ("vefkort/","Vefkort")]

def build_block(title, cards_html, hub_html=""):
    return (f'{STYLE}<section class="rel-links"><h2>{title}</h2>'
            f'<div class="rel-grid">{cards_html}</div>{hub_html}</section>')

def inject(path, block):
    """Insert block before the footer, or before </body> on pages without one."""
    f = ROOT / path
    if not f.exists(): return False
    s = f.read_text(encoding="utf-8", errors="ignore")
    if MARK in s: return False
    if '<footer class="footer">' in s:
        s = s.replace('<footer class="footer">', block + '\n<footer class="footer">', 1)
    elif '<footer>' in s:
        s = s.replace('<footer>', block + '\n<footer>', 1)
    elif '</body>' in s:
        s = s.replace('</body>', block + '\n</body>', 1)
    else:
        return False
    f.write_text(s, encoding="utf-8")
    return True

# --- 2a. Section hub pages: other hubs + a few own-section entries ---
for sec in SECTIONS:
    others = [abs_link(f"{s2}/", HUB_LABEL[s2]) for s2 in SECTIONS if s2 != sec]
    own = "".join(link(a, b, c) for a, b, c in pick(sec, 3))
    cards = "".join(others) + own
    if inject(f"{sec}/index.html", build_block("Skoðaðu einnig", cards)):
        count += 1

# --- 2b. Info / legal / about pages: sibling info pages + main sections ---
for path, label in INFO_PAGES:
    siblings = [abs_link(p, l) for p, l in INFO_PAGES if p != path][:4]
    sections = [abs_link(f"{s2}/", HUB_LABEL[s2]) for s2 in ["spilaviti", "spilakassar", "leidbeiningar"]]
    cards = "".join(siblings + sections)
    hub = f'<p class="rel-hub">{abs_link("", "Forsíða Svipan →")}</p>'
    if inject(f"{path}index.html", build_block("Tengt efni", cards, hub)):
        count += 1

# --- 2c. English pages: each other + key Icelandic pages ---
EN_PAGES = [("en/", "Online Casino Iceland"), ("en/casino-in-reykjavik/", "Casino in Reykjavik"),
            ("en/poker-in-iceland/", "Poker in Iceland")]
for path, label in EN_PAGES:
    siblings = [abs_link(p, l) for p, l in EN_PAGES if p != path]
    icelandic = [abs_link("spilaviti/", "Casino reviews (Icelandic)"),
                 abs_link("spilakassar/", "Slot reviews (Icelandic)"),
                 abs_link("leidbeiningar/", "Guides (Icelandic)"),
                 abs_link("greidslur/", "Payment methods (Icelandic)")]
    cards = "".join(siblings + icelandic)
    if inject(f"{path}index.html", build_block("Related pages", cards)):
        count += 1

# --- 2d. Slotoro review page: top casinos + relevant guides ---
afth_cards = "".join([
    abs_link("spilaviti/slotoro/", "Slotoro umsögn"),
    abs_link("spilaviti/", "Allar spilavítaumsagnir"),
    abs_link("spilakassar/", "Spilakassaumsagnir"),
    abs_link("bonusar/bonus-slotoro/", "Slotoro bónus"),
    abs_link("leidbeiningar/hvernig-a-ad-velja-spilaviti-island/", "Hvernig á að velja spilavíti"),
    abs_link("leidbeiningar/islenskir-bankar-spilaviti/", "Íslenskir bankar og spilavíti"),
])
if inject("afthreying/index.html", build_block("Tengt efni", afth_cards)):
    count += 1

# --- 2e. News archive: route old backlink traffic into the live site ---
frettir_cards = "".join([
    abs_link("spilaviti/", "Spilavítaumsagnir"),
    abs_link("spilakassar/", "Spilakassaumsagnir"),
    abs_link("leidbeiningar/", "Leiðbeiningar"),
    abs_link("greidslur/", "Greiðsluleiðir"),
    abs_link("saga/", "Saga Svipan"),
    abs_link("um-okkur/", "Um okkur"),
])
if inject("frettir/index.html", build_block("Skoðaðu vefinn", frettir_cards)):
    count += 1

# --- 2f. Skuggaborg (legacy project page) ---
skugga_cards = "".join([
    abs_link("saga/", "Saga Svipan"),
    abs_link("um-okkur/", "Um okkur"),
    abs_link("frettir/", "Greinasafn"),
    abs_link("spilaviti/", "Spilavítaumsagnir"),
])
if inject("skuggaborg/index.html", build_block("Tengt efni", skugga_cards)):
    count += 1

print(f"interlink: injected into {count} pages (base {URL_BASE})")
