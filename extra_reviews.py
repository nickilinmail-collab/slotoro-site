# -*- coding: utf-8 -*-
"""Data-driven reviews for 98 popular lobby slots.
Facts (layout, ways, max win, volatility, release date, hit rate) scraped Nov 2026
from SlotCatalog game pages; RTP shown only when a >=95.9% top setting was found."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
PROV_FIX = {"Play'n Go": "Play'n GO", "Nolimit City": "NoLimit City", "Blueprint": "Blueprint Gaming",
            "BGAMING": "BGaming", "Merkur": "Merkur / Blueprint", "Reel Time Gaming": "Reel Time Gaming / Blueprint",
            "Reel Kingdom": "Reel Kingdom / Pragmatic Play", "Triple Edge Studios": "Triple Edge Studios / Games Global",
            "Stormcraft Studios": "Stormcraft Studios / Games Global"}
VOL_MAP = {"Low": "Low", "Med": "Medium", "Med-High": "Medium-High", "High": "High", "": ""}


def load(names):
    rows = json.load(open(os.path.join(HERE, "tools", "facts_top.json")))
    out = []
    for slug, _ok, prov, rtp, vol, mx, lay, ways, rel, hit in rows:
        out.append({
            "key": slug, "slug": slug[2:], "name": names[slug], "provider": PROV_FIX.get(prov, prov),
            "rtp": rtp if (rtp and rtp >= 95.9) else None, "volatility": VOL_MAP.get(vol, ""),
            "maxwin": f"x{int(float(mx))}" if mx else "", "layout": lay, "ways": ways.replace(" [ i ]", ""),
            "year": rel[:4] if rel else "", "hit": float(hit) if hit else None,
        })
    return out


def _grid(lay):
    parts = [p for p in lay.split("-") if p]
    if len(parts) == 2:
        return f"{parts[0]} hjólum og {parts[1]} röðum"
    if len(parts) > 2:
        return f"óreglulegu borði ({lay.replace('-', '–')} tákn á hjóli)"
    return f"{parts[0]} hjólum" if parts else "hefðbundnu borði"


def _ways(w):
    l = w.lower()
    if "cluster" in l: return "klasavinningum: 5 eða fleiri eins tákn sem snertast gefa vinning", "klasar"
    if "anywhere" in l or "scatter" in l: return "„borgað hvar sem er“ reglu: nógu mörg eins tákn hvar sem er á borðinu gefa vinning", "hvarsemer"
    m = re.match(r"(\d+)", w)
    if not m: return "breytilegum vinningsleiðum", ""
    n = int(m.group(1)); both = "báðar áttir" if "Bothway" in w else ""
    if n in (117649, 200704) or n >= 15625: return f"allt að {n:,} vinningsleiðum (breytilegur fjöldi tákna á hverju hjóli)".replace(",", "."), "megaways"
    if n >= 243: return f"{n:,} vinningsleiðum".replace(",", ".") + (" sem borga í báðar áttir" if both else ""), "leidir"
    return f"{n} föstum vinningslínum" + (" sem borga í báðar áttir" if both else ""), "linur"


def _series(name, all_names):
    base = re.sub(r"\s+(2|3|4|5|II|III|Megaways|Deluxe|Multihold|Reloaded|Apocalypse|XXXtreme|Megapays|Freeze|Epic Bloom|Stormchaser|Keeping it Reel)$", "", name).strip()
    if base != name and base in all_names:
        return base
    return None


def content(s, vol_is, maxwin_is, rtp_is, VOL_WHO, slot_url, all_names):
    grid = _grid(s["layout"]); ways, kind = _ways(s["ways"])
    p1 = f'{s["name"]} er spilakassi frá {s["provider"]}' + (f', gefinn út árið {s["year"]}' if s["year"] else "") + f'. Leikið er á {grid} með {ways}.'
    base = _series(s["name"], all_names)
    if base:
        p1 += f' Leikurinn byggir á <a href="{slot_url(base)}">{base}</a>' + (" og bætir við Megaways-kerfinu." if "Megaways" in s["name"] else " og er framhald eða ný útgáfa hans.")
    mw = s["maxwin"]
    if mw:
        n = int(mw[1:])
        level = ("mjög hátt" if n >= 50000 else "hátt" if n >= 10000 else "í meðallagi" if n >= 3000 else "frekar lágt")
        p2 = f'Hámarksvinningur er {maxwin_is(mw)} af veðmáli, sem er {level} miðað við nútíma spilakassa.'
    else:
        p2 = "Heimildir gefa ekki upp eitt ákveðið hámark, svo athugaðu vinningstöflu leiksins."
    if s["hit"]:
        p2 += f' Samkvæmt mælingum skilar um {str(round(s["hit"],1)).replace(".", ",")}% spuna einhverjum vinningi, eða u.þ.b. einn af hverjum {str(round(100/s["hit"],1)).replace(".", ",")} spunum.'
    vol = s["volatility"]
    who = VOL_WHO.get(vol, "Framleiðandinn gefur ekki upp sveiflustig, svo prófaðu kynningarham fyrst ef hann er í boði.")
    if kind == "megaways": who += " Megaways-kerfið gerir hvern spuna ólíkan, sem hentar þeim sem vilja mikla hreyfingu."
    elif kind == "klasar": who += " Klasakerfið gefur keðjuverkanir þegar ný tákn falla inn."
    elif kind == "linur" and s["layout"] in ("3-3", "5-3"): who += " Einfalt borð með fáum línum er auðvelt að fylgjast með fyrir byrjendur."
    rtp_txt = (f'Hæsta uppgefna RTP er {rtp_is(s["rtp"])}.' if s["rtp"] else
               "RTP er breytilegt eftir spilavíti (rekstraraðilar geta valið lægri útgáfu).")
    return p1, p2, who, rtp_txt


def faq(s, vol_is, maxwin_is, rtp_is):
    n = s["name"]
    out = [(f"Hvert er RTP í {n}?",
            (f"Hæsta uppgefna RTP er {rtp_is(s['rtp'])}. " if s["rtp"] else "RTP fer eftir útgáfunni sem spilavítið velur. ")
            + "Athugaðu upplýsingaskjá leiksins áður en þú spilar.")]
    if s["volatility"]:
        out.append((f"Hversu sveiflukenndur er {n}?", f"Sveiflan er {vol_is(s['volatility']).lower()}."))
    if s["maxwin"]:
        out.append((f"Hver er hámarksvinningurinn í {n}?", f"{maxwin_is(s['maxwin'])} af veðmáli. Hann er mjög sjaldgæfur."))
    out.append((f"Hvar get ég spilað {n}?", f"{n} er meðal leikja frá {s['provider']} sem Slotoro býður. Framboð getur verið mismunandi eftir landi."))
    return out
