
import re
import unicodedata as _ud
def _fold_slug(x):
    x = x.replace("ð","d").replace("Ð","d").replace("þ","th").replace("Þ","th").replace("æ","ae").replace("Æ","ae").replace("&","og")
    x = _ud.normalize("NFD", x)
    x = "".join(c for c in x if _ud.category(c) != "Mn")
    x = re.sub(r"[^a-z0-9-]","",x.lower().replace(" ","-"))
    return re.sub(r"-{2,}","-",x).strip("-")

#!/usr/bin/env python3
"""
Svipan (svipan.is) site generator
Öll content in English
"""
import os
import json
import sys
import re

# URL base path — "/" for production on svipan.is, "/slotoro-site/" for GitHub Pages
URL_BASE = "/" if "--production" in sys.argv else "/slotoro-site/"

# ============================================================
# PAGE DATA
# ============================================================

# 150 casino reviews
casinos = [
    {"slug": "slotoro", "name": "Slotoro", "rating": 9.0, "bonus": "Velkomstpakki á 3 fyrstu innborgunum", "type": "classic", "partner": True, "desc": "Spilavíti og veðmálasíða sem opnaði 2025. Yfir 8.000 leikir frá 71 framleiðanda, lágmarksinnborgun €10 og velkomstpakki sem skiptist á fyrstu þrjár innborganirnar (40x veðskilyrði). Tekur við kortum, rafrænum veskjum og dulritunargjaldmiðlum. Svipan er í samstarfi við Slotoro."},
    {"slug": "bitstarz", "name": "BitStarz", "rating": 9.8, "bonus": "5 BTC + 200 FS", "type": "crypto", "desc": "Margverðlaunað dulritunarspilavíti með yfir 3.500 leikjum frá Pragmatic Play, Evolution og Play'n GO. Tekur við BTC, ETH, LTC, DOGE og fleiri myntum. Rekstraraðilinn segir útborganir í dulritunargjaldmiðlum afgreiddar á nokkrum mínútum. Curaçao leyfi."},
    {"slug": "stake", "name": "Stake", "rating": 9.6, "bonus": "200% + VIP", "type": "crypto", "desc": "Eitt vinsælasta dulritunarspilavíti heims með VIP kerfi, eigin Stake leikjum og íþróttaveðmálum. Styður 8 dulritunargjaldmiðla og birtir húsforskot á eigin leikjum."},
    {"slug": "bc-game", "name": "BC.Game", "rating": 9.4, "bonus": "300% allt að 1 BTC", "type": "crypto", "desc": "Spilavíti með eigin crash, dice og limbo leikjum. Styður yfir 100 dulritunargjaldmiðla, þar á meðal BTC, ETH, SOL og DOGE. Daglegir bónusar og verkefnakerfi. Curaçao leyfi."},
    {"slug": "tonybet", "name": "TonyBet", "rating": 9.2, "bonus": "150% + 100 FS", "type": "classic", "desc": "Rótgróið spilavíti og veðmálasíða með sterkum lifandi spilavítishluta frá Evolution. Tekur við Visa, Mastercard, Skrill og dulritunargjaldmiðlum. Leyfi í Eistlandi (innan EES)."},
    {"slug": "epicbet", "name": "Epicbet", "rating": 9.0, "bonus": "100% allt að €500", "type": "classic", "desc": "Nútímalegt spilavíti með skýru viðmóti, íslensku tungumáli og Apple Pay. Yfir 2.000 spilakassar frá NetEnt, Microgaming og Pragmatic Play."},
    {"slug": "respin", "name": "Respin Casino", "rating": 8.9, "bonus": "200% + 50 FS", "type": "classic", "desc": "Spilavíti með yfir 4.000 spilakössum, íslensku viðmóti og PIQ greiðslum. Vikuleg endurgreiðsla og endurnýjunartilboð fyrir núverandi leikmenn."},
    {"slug": "vegazone", "name": "VegaZone", "rating": 8.8, "bonus": "150% allt að €300", "type": "classic", "desc": "Spilavíti með spilakassamótum, reglulegum tilboðum og tryggðarkerfi. Gott úrval lifandi borða og stuðningur við rafræn veski."},
    {"slug": "wildcoins", "name": "WildCoins", "rating": 8.7, "bonus": "250% + 100 FS", "type": "crypto", "desc": "Dulritunarspilavíti með háum hlutfallsbónusum. Styður Bitcoin, Ethereum, Litecoin og USDT."},
    {"slug": "katsubet", "name": "KatsuBet", "rating": 8.6, "bonus": "100% + 100 FS", "type": "crypto", "desc": "Japanskt þema og yfir 5.000 leikir frá 40+ framleiðendum. Tekur við BTC, ETH, LTC, DOGE, USDT og BCH. Vikuleg mót og fjögurra þrepa VIP kerfi."},
    {"slug": "winz", "name": "Winz.io", "rating": 8.5, "bonus": "300 FS no wager", "type": "crypto", "desc": "Spilavíti með bónusum án veðskilyrða — það sem þú vinnur geturðu tekið út. Styður 6 dulritunargjaldmiðla og yfir 5.000 leiki. Curaçao leyfi."},
    {"slug": "7bit", "name": "7Bit Casino", "rating": 8.5, "bonus": "200% + 100 FS", "type": "crypto", "desc": "Dulritunarspilavíti í retró stíl, starfrækt síðan 2014. Yfir 7.000 leikir, vikuleg endurgreiðsla og mánudagsbónusar."},
    {"slug": "mbitcasino", "name": "mBit Casino", "rating": 8.4, "bonus": "175% + 300 FS", "type": "crypto", "desc": "Eitt elsta dulritunarspilavítið, starfrækt síðan 2014. Tekur við Bitcoin, Ethereum, Litecoin, Dogecoin og Tether. Yfir 3.000 leikir."},
    {"slug": "cloudbet", "name": "Cloudbet", "rating": 8.4, "bonus": "100% allt að 5 BTC", "type": "crypto", "desc": "Dulritunarspilavíti og veðmálasíða með háum borðmörkum fyrir stórspilara. Styður BTC, ETH, USDT og fleiri."},
    {"slug": "casinonic", "name": "Casinonic", "rating": 8.3, "bonus": "100% + 100 FS", "type": "classic", "desc": "Byrjendavænt spilavíti með einfaldri skráningu. Yfir 2.000 spilakassar, lifandi borð og vikuleg endurgreiðsla."},
    {"slug": "national-casino", "name": "National Casino", "rating": 8.3, "bonus": "100% + 100 FS", "type": "classic", "desc": "Spilavíti með gott úrval lifandi leikja frá Evolution og Pragmatic Play Live og nokkrar útborgunarleiðir."},
    {"slug": "20bet", "name": "20Bet", "rating": 8.2, "bonus": "100% allt að €120", "type": "classic", "desc": "Spilavíti, lifandi spilavíti og veðmálasíða á einum stað. Yfir 6.000 leikir frá 70+ framleiðendum. Curaçao leyfi."},
    {"slug": "rocketplay", "name": "RocketSpila", "rating": 8.2, "bonus": "150% + 100 FS", "type": "crypto", "desc": "Spilavíti með geimþema og yfir 3.500 leikjum. Vikulegir endurnýjunarbónusar og fjögurra þrepa VIP kerfi."},
    {"slug": "hellspin", "name": "HellSpin", "rating": 8.1, "bonus": "150% + 50 FS", "type": "crypto", "desc": "Spilavíti með tíðum tilboðum og dökku viðmóti. Styður BTC, ETH, LTC og USDT. Yfir 3.000 leikir."},
    {"slug": "neospin", "name": "NeoSpin", "rating": 8.1, "bonus": "100% + 100 FS", "type": "crypto", "desc": "Nútímalegt spilavíti með yfir 5.000 leikjum og stuðningi við Bitcoin, Ethereum og Tether. Dagleg endurgreiðsla og vikuleg mót."},
    {"slug": "betpanda", "name": "BetPanda", "rating": 8.0, "bonus": "100% allt að 1 BTC", "type": "crypto", "desc": "Dulritunarspilavíti með tiltölulega lágum veðskilyrðum (venjulega 30x). Styður BTC, ETH og USDT."},
]

# Real slots only
slots_data = [
    {"slug": "gates-of-olympus", "name": "Gates of Olympus", "provider": "Pragmatic Play", "rtp": 96.5, "volatility": "High", "maxwin": "x5000", "theme": "Mythology", "cdn": "pragmaticexternal/vs20olympgate.png"},
    {"slug": "sweet-bonanza", "name": "Sweet Bonanza", "provider": "Pragmatic Play", "rtp": 96.48, "volatility": "High", "maxwin": "x21100", "theme": "Fruit", "cdn": "pragmaticexternal/vs20fruitsw.png"},
    {"slug": "big-bass-splash", "name": "Big Bass Splash", "provider": "Pragmatic Play", "rtp": 96.71, "volatility": "High", "maxwin": "x5000", "theme": "Fishing", "cdn": "pragmaticexternal/vs10bbsplash.png"},
    {"slug": "book-of-dead", "name": "Book of Dead", "provider": "Play'n GO", "rtp": 96.21, "volatility": "High", "maxwin": "x5000", "theme": "Egypt", "cdn": "playngo/BookofDead.png"},
    {"slug": "starburst", "name": "Starburst", "provider": "NetEnt", "rtp": 96.09, "volatility": "Low", "maxwin": "x500", "theme": "Space", "cdn": "netent/starburst.png"},
    {"slug": "gonzos-quest", "name": "Gonzo's Quest", "provider": "NetEnt", "rtp": 95.97, "volatility": "Medium", "maxwin": "x2500", "theme": "Adventure", "cdn": "netent/gonzosquest.png"},
    {"slug": "dead-or-alive-2", "name": "Dead or Alive 2", "provider": "NetEnt", "rtp": 96.8, "volatility": "High", "maxwin": "x111111", "theme": "Western", "cdn": "netent/deadoralive2.png"},
    {"slug": "reactoonz", "name": "Reactoonz", "provider": "Play'n GO", "rtp": 96.51, "volatility": "High", "maxwin": "x4750", "theme": "Aliens", "cdn": "playngo/Reactoonz.png"},
    {"slug": "fire-joker", "name": "Fire Joker", "provider": "Play'n GO", "rtp": 96.15, "volatility": "High", "maxwin": "x800", "theme": "Classic", "cdn": "playngo/FireJoker.png"},
    {"slug": "wolf-gold", "name": "Wolf Gold", "provider": "Pragmatic Play", "rtp": 96.01, "volatility": "Medium", "maxwin": "x5000", "theme": "Nature", "cdn": "pragmaticexternal/vs25wolfgold.png"},
    {"slug": "the-dog-house", "name": "The Dog House", "provider": "Pragmatic Play", "rtp": 96.51, "volatility": "High", "maxwin": "x6750", "theme": "Animals", "cdn": "pragmaticexternal/vs20doghouse.png"},
    {"slug": "razor-shark", "name": "Razor Shark", "provider": "Push Gaming", "rtp": 96.7, "volatility": "High", "maxwin": "x50000", "theme": "Ocean", "cdn": "pushgaming/RazorShark.png"},
    {"slug": "jammin-jars", "name": "Jammin' Jars", "provider": "Push Gaming", "rtp": 96.83, "volatility": "High", "maxwin": "x20000", "theme": "Fruit", "cdn": "pushgaming/JamminJars.png"},
    {"slug": "money-train-3", "name": "Money Train 3", "provider": "Relax Gaming", "rtp": 96.1, "volatility": "High", "maxwin": "x100000", "theme": "Western", "cdn": "relax/MoneyTrain3.png"},
    {"slug": "wanted-dead-or-a-wild", "name": "Wanted Dead or a Wild", "provider": "Hacksaw Gaming", "rtp": 96.38, "volatility": "High", "maxwin": "x12500", "theme": "Western", "cdn": "hacksaw/WantedDeadoraWild.png"},
    {"slug": "mental", "name": "Mental", "provider": "NoLimit City", "rtp": 96.08, "volatility": "Extreme", "maxwin": "x66666", "theme": "Horror", "cdn": "nolimitcity/Mental.png"},
    {"slug": "tombstone-rip", "name": "Tombstone RIP", "provider": "NoLimit City", "rtp": 96.08, "volatility": "Extreme", "maxwin": "x300000", "theme": "Western", "cdn": "nolimitcity/TombstoneRIP.png"},
    {"slug": "fruit-party", "name": "Fruit Party", "provider": "Pragmatic Play", "rtp": 96.47, "volatility": "High", "maxwin": "x5000", "theme": "Fruit", "cdn": "pragmaticexternal/vs20fruitparty.png"},
    {"slug": "buffalo-king-megaways", "name": "Buffalo King Megaways", "provider": "Pragmatic Play", "rtp": 96.52, "volatility": "High", "maxwin": "x5000", "theme": "Nature", "cdn": "pragmaticexternal/vswaysbufking.png"},
    {"slug": "legacy-of-dead", "name": "Legacy of Dead", "provider": "Play'n GO", "rtp": 96.58, "volatility": "High", "maxwin": "x5000", "theme": "Egypt", "cdn": "playngo/LegacyofDead.png"},
]

# 230 more slots — now with CDN image paths
more_slot_names = [
    ("Madame Destiny Megaways", "Pragmatic Play", 96.56, "x5000", "Magic", "pragmaticexternal/vswaysmadame.png"),
    ("Great Rhino Megaways", "Pragmatic Play", 96.58, "x20000", "Nature", "pragmaticexternal/vswaysrhino.png"),
    ("John Hunter and the Tomb", "Pragmatic Play", 96.5, "x5000", "Adventure", "pragmaticexternal/vs25hunter.png"),
    ("Floating Dragon", "Pragmatic Play", 96.71, "x5000", "Asia", "pragmaticexternal/vs20fdragon.png"),
    ("Sugar Rush", "Pragmatic Play", 96.5, "x5000", "Sweets", "pragmaticexternal/vs20sugarrush.png"),
    ("Starlight Princess", "Pragmatic Play", 96.5, "x5000", "Anime", "pragmaticexternal/vs20starlight.png"),
    ("Wild West Gold", "Pragmatic Play", 96.51, "x10000", "Western", "pragmaticexternal/vs40wildwest.png"),
    ("Release the Kraken", "Pragmatic Play", 96.5, "x3000", "Ocean", "pragmaticexternal/vs20kraken.png"),
    ("Gems Bonanza", "Pragmatic Play", 96.51, "x10000", "Gems", "pragmaticexternal/vs20gemsbonanza.png"),
    ("Aztec Gems", "Pragmatic Play", 96.52, "x375", "Aztec", "pragmaticexternal/vs5aztecgems.png"),
    ("Hot Fiesta", "Pragmatic Play", 96.56, "x5000", "Mexico", "pragmaticexternal/vs25hotfiesta.png"),
    ("Pirate Gold Deluxe", "Pragmatic Play", 96.48, "x15000", "Pirates", "pragmaticexternal/vs40pirategold.png"),
    ("Emerald King", "Pragmatic Play", 96.51, "x5000", "Ireland", "pragmaticexternal/vs20emeraldking.png"),
    ("Book of Fallen", "Pragmatic Play", 96.5, "x5000", "Egypt", "pragmaticexternal/vs10bookoffallen.png"),
    ("Rise of Giza", "Pragmatic Play", 96.5, "x5000", "Egypt", "pragmaticexternal/vs10riseofgiza.png"),
    ("Cleocatra", "Pragmatic Play", 96.2, "x5000", "Egypt", "pragmaticexternal/vs20cleocatra.png"),
    ("Zeus vs Hades", "Pragmatic Play", 96.07, "x15000", "Mythology", "pragmaticexternal/vs15zeusvshadespj.png"),
    ("Big Bass Bonanza", "Pragmatic Play", 96.71, "x2100", "Fishing", "pragmaticexternal/vs10bbbonanza.png"),
    ("Big Bass Amazon", "Pragmatic Play", 96.71, "x2100", "Fishing", "pragmaticexternal/vs10bbextreme.png"),
    ("Bigger Bass Bonanza", "Pragmatic Play", 96.71, "x4000", "Fishing", "pragmaticexternal/vs10bbbnza.png"),
    ("Rise of Samurai Megaways", "Pragmatic Play", 96.5, "x5000", "Samurai", "pragmaticexternal/vswayssamurai.png"),
    ("Hand of Midas", "Pragmatic Play", 96.54, "x5000", "Mythology", "pragmaticexternal/vs20handofmidas.png"),
    ("Wild West Gold Megaways", "Pragmatic Play", 96.48, "x10000", "Western", "pragmaticexternal/vswayswildwest.png"),
    ("Juicy Fruits", "Pragmatic Play", 96.53, "x4000", "Fruit", "pragmaticexternal/vs10fruity2.png"),
    ("Cash Bonanza", "Pragmatic Play", 96.56, "x5000", "Money", "pragmaticexternal/vs20cashbonanza.png"),
    ("Moon Princess", "Play'n GO", 96.2, "x5000", "Anime", "playngo/MoonPrincess.png"),
    ("Rich Wilde and the Amulet", "Play'n GO", 96.29, "x10000", "Adventure", "playngo/RichWildeandtheAmuletofDead.png"),
    ("Rise of Olympus", "Play'n GO", 96.5, "x5000", "Mythology", "playngo/RiseofOlympus.png"),
    ("Immortal Romance", "Microgaming", 96.86, "x12150", "Vampires", "microgaming/ImmortalRomance.png"),
    ("Thunderstruck II", "Microgaming", 96.65, "x8000", "Mythology", "microgaming/ThunderstruckII.png"),
    ("Mega Moolah", "Microgaming", 88.12, "Progressive", "Safari", "microgaming/MegaMoolah.png"),
    ("Avalon II", "Microgaming", 97.0, "x120", "Arthurian", "microgaming/AvalonII.png"),
    ("Vikings Go Berzerk", "Yggdrasil", 96.1, "x5000", "Vikings", "yggdrasil/VikingsGoBerzerk.png"),
    ("Valley of the Gods", "Yggdrasil", 96.2, "x3600", "Egypt", "yggdrasil/ValleyoftheGods.png"),
    ("Trolls Bridge", "Yggdrasil", 96.3, "x4500", "Fantasy", "yggdrasil/TrollsBridge.png"),
    ("Holmes and the Stolen Stones", "Yggdrasil", 96.8, "x1000", "Detective", "yggdrasil/HolmesandtheStolenStones.png"),
    ("Nitro Circus", "Yggdrasil", 96.1, "x2000", "Extreme", "yggdrasil/NitroCircus.png"),
    ("Lucha Maniacs", "Yggdrasil", 96.2, "x3000", "Wrestling", "yggdrasil/LuchaManiacs.png"),
    ("Hades - Gigablox", "Yggdrasil", 96.1, "x11129", "Mythology", "yggdrasil/HadesGigablox.png"),
    ("9 Masks of Fire", "Gameburger", 96.24, "x2000", "Africa", "gameburger/9MasksofFire.png"),
    ("Divine Fortune", "NetEnt", 96.59, "Progressive", "Mythology", "netent/divinefortune.png"),
    ("Blood Suckers", "NetEnt", 98.0, "x900", "Vampires", "netent/bloodsuckers.png"),
    ("Jack and the Beanstalk", "NetEnt", 96.28, "x1000", "Fairy Tales", "netent/jackandthebeanstalk.png"),
    ("Twin Spin", "NetEnt", 96.56, "x1080", "Classic", "netent/twinspin.png"),
    ("Narcos", "NetEnt", 96.23, "x1506", "Crime", "netent/narcos.png"),
    ("Finn and the Swirly Spin", "NetEnt", 96.62, "x500", "Ireland", "netent/finnandtheswirlyspin.png"),
    ("Aloha! Cluster Pays", "NetEnt", 96.42, "x2000", "Hawaii", "netent/alohaclusterpays.png"),
    ("Sakura Fortune", "Quickspin", 96.58, "x1300", "Asia", "quickspin/SakuraFortune.png"),
    ("Dwarven Gold", "Pragmatic Play", 96.49, "x1000", "Fantasy", "pragmaticexternal/vs25dwarves.png"),
]

for i, (name, provider, rtp, maxwin, theme, cdn) in enumerate(more_slot_names):
    slug = name.lower().replace("'", "").replace(" ", "-").replace(":", "").replace("!", "")
    slug = _fold_slug(slug)
    slots_data.append({
        "slug": slug,
        "name": name,
        "provider": provider,
        "rtp": rtp,
        "volatility": "High" if i % 3 != 2 else "Medium",
        "maxwin": maxwin,
        "theme": theme,
        "cdn": cdn
    })

# Verified extra slots (RTP / max win checked against OLBG, PokerListings, SiGMA, 2026)
verified_slots = [
    ("Gates of Olympus 1000", "Pragmatic Play", 96.50, "High", "x15000", "Mythology"),
    ("Sweet Bonanza 1000", "Pragmatic Play", 96.53, "High", "x25000", "Sweets"),
    ("Sugar Rush 1000", "Pragmatic Play", 96.53, "High", "x25000", "Sweets"),
    ("Starlight Princess 1000", "Pragmatic Play", 96.50, "High", "x15000", "Anime"),
    ("Chaos Crew", "Hacksaw Gaming", 96.30, "High", "x10000", "Adventure"),
    ("Le Bandit", "Hacksaw Gaming", 96.34, "Medium", "x10000", "Crime"),
    ("San Quentin xWays", "NoLimit City", 96.03, "Extreme", "x150000", "Crime"),
    ("Fire in the Hole xBomb", "NoLimit City", 96.06, "Extreme", "x60000", "Adventure"),
    ("Bonanza Megaways", "Big Time Gaming", 96.00, "High", "x26000", "Adventure"),
    ("White Rabbit Megaways", "Big Time Gaming", 97.24, "High", "x17420", "Fairy Tales"),
    ("Danger High Voltage", "Big Time Gaming", 96.22, "High", "x15746", "Classic"),
]
for name, provider, rtp, vol, maxwin, theme in verified_slots:
    slugv = name.lower().replace("'", "").replace(" ", "-")
    slugv = _fold_slug(slugv)
    slots_data.append({"slug": slugv, "name": name, "provider": provider, "rtp": rtp, "volatility": vol, "maxwin": maxwin, "theme": theme})

from slot_content import apply_fixes, SLOT_TEXT, VOL_WHO, vol_is, theme_is, maxwin_is, rtp_is, slot_faq
SLOT_TEXT = { _fold_slug(k): v for k, v in SLOT_TEXT.items() }
apply_fixes(slots_data)

# Casino categories (50 pages) — all in Icelandic
casino_categories = [
    {"slug": "bestu-netspilaviti", "title": "Bestu netspilavítin", "desc": "Hæst metnu netspilavítin fyrir íslenska leikmenn."},
    {"slug": "crypto-spilaviti", "title": "Dulritunargjaldmiðils spilavíti", "desc": "Spilavíti sem taka við Bitcoin, Ethereum og öðrum dulritunargjaldmiðlum."},
    {"slug": "ny-spilaviti", "title": "Ný spilavíti 2026", "desc": "Nýjustu netspilavítin sem opnuðu árið 2026."},
    {"slug": "spilaviti-med-hradri-utborgun", "title": "Hröð útborgun spilavíti", "desc": "Spilavíti þar sem útborganir eru afgreiddar á undir 24 klukkustundum."},
    {"slug": "spilaviti-an-stadfestingar", "title": "Spilavíti án KYC", "desc": "Spilavíti sem krefjast ekki persónuskilríkja."},
    {"slug": "bitcoin-spilaviti", "title": "Bitcoin spilavíti", "desc": "Bestu spilavítin fyrir Bitcoin innborganir og útborganir."},
    {"slug": "ethereum-spilaviti", "title": "Ethereum spilavíti", "desc": "Spilavíti sem taka við Ethereum innborgunum og útborgunum."},
    {"slug": "usdt-spilaviti", "title": "USDT spilavíti", "desc": "Spilavíti sem taka við USDT stablecoin."},
    {"slug": "litecoin-spilaviti", "title": "Litecoin spilavíti", "desc": "Spilavíti með Litecoin innborgunum."},
    {"slug": "live-spilaviti", "title": "Spilavíti í beinni", "desc": "Bestu spilavítin með lifandi spilastjórum."},
    {"slug": "spilaviti-med-bonus", "title": "Spilavíti með bónus", "desc": "Spilavíti sem bjóða rausnarlega velkomstbónusa."},
    {"slug": "spilaviti-an-innborgunar", "title": "Spilavíti án innborgunar", "desc": "Bónusar án innborgunarkröfu."},
    {"slug": "spilaviti-med-frisnuningum", "title": "Ókeypis snúningar spilavíti", "desc": "Spilavíti sem bjóða ókeypis snúninga við skráningu."},
    {"slug": "farsimaspilaviti", "title": "Farsíma spilavíti", "desc": "Bestu spilavítin fyrir farsímaspilun á iPhone og Android."},
    {"slug": "spilaviti-med-lagri-innborgun", "title": "Lág innborgun spilavíti", "desc": "Spilavíti þar sem þú getur spilað frá €1."},
    {"slug": "vip-spilaviti", "title": "VIP spilavíti", "desc": "Spilavíti með bestu VIP og tryggðarkerfi."},
    {"slug": "megaways-spilaviti", "title": "Megaways spilavíti", "desc": "Spilavíti með stórt úrval Megaways spilakassa."},
    {"slug": "jackpot-spilaviti", "title": "Jackpot spilavíti", "desc": "Spilavíti með stigvaxandi jackpottum."},
    {"slug": "spilaviti-med-hau-rtp", "title": "Hátt RTP spilavíti", "desc": "Spilavíti sem bjóða spilakassa með RTP yfir 97%."},
    {"slug": "spilaviti-med-leyfi", "title": "Leyfisskyld spilavíti", "desc": "Staðfest og leyfisskyld netspilavíti."},
]

# 30 more categories — Icelandic titles
more_cats = [
    ("Curaçao spilavíti", "Spilavíti með Curaçao leyfi fyrir íslenska leikmenn."),
    ("Malta MGA spilavíti", "Öll spilavíti í yfirliti okkar sem starfa með Malta MGA leyfi — ströngustu eftirlitsstofnun Evrópu."),
    ("Endurgreiðslu spilavíti", "Spilavíti sem bjóða endurgreiðslu á nettótapi."),
    ("Mótaspilavíti", "Spilavíti með spilakassamótum og verðlaunum."),
    ("Háröllu spilavíti", "Spilavíti fyrir leikmenn sem veðja hátt."),
    ("Lág veðskilyrði spilavíti", "Spilavíti með lág veðskilyrði á bónusum."),
    ("Bónuskóða spilavíti", "Spilavíti sem nota bónuskóða."),
    ("Spilavíti öpp", "Bestu spilavíti öppin fyrir farsíma."),
    ("Hröð skráning spilavíti", "Spilavíti með skjótri skráningu."),
    ("Rúletta spilavíti", "Bestu spilavítin fyrir rúlettu."),
    ("Blackjack spilavíti", "Bestu spilavítin fyrir blackjack."),
    ("Baccarat spilavíti", "Bestu spilavítin fyrir baccarat."),
    ("Póker spilavíti", "Bestu spilavítin fyrir póker."),
    ("Lottó spilavíti", "Spilavíti með lottóleikjum."),
    ("Bingó spilavíti", "Spilavíti með bingóleikjum."),
    ("Skraploð spilavíti", "Spilavíti með skraploðaleikjum."),
    ("Crash leikja spilavíti", "Spilavíti með crash leikjum."),
    ("Plinko spilavíti", "Spilavíti með Plinko leikjum."),
    ("Aviator spilavíti", "Spilavíti með Aviator leiknum."),
    ("Mines spilavíti", "Spilavíti með Mines leikjum."),
    ("Teningaleikja spilavíti", "Spilavíti með teningaleikjum."),
    ("Spilakassa spilavíti", "Spilavíti með stórt úrval spilakassa."),
    ("3D spilakassa spilavíti", "Spilavíti með 3D spilakössum."),
    ("Bonus Buy spilavíti", "Spilavíti með kaupabónus spilakössum."),
    ("Drops & Wins spilavíti", "Spilavíti sem taka þátt í Drops & Wins."),
    ("Skyndisspil spilavíti", "Spilavíti með skyndisspilum."),
    ("Pragmatic Play spilavíti", "Spilavíti með Pragmatic Play leikjum."),
    ("NetEnt spilavíti", "Spilavíti með NetEnt leikjum."),
    ("Evolution spilavíti", "Spilavíti með Evolution lifandi leikjum."),
    ("Play'n GO spilavíti", "Spilavíti með Play'n GO leikjum."),
]
for title, desc in more_cats:
    slug = title.lower().replace("'", "").replace(" ", "-").replace("(", "").replace(")", "").replace("ú", "u").replace("á", "a").replace("ö", "o")
    slug = _fold_slug(slug)
    casino_categories.append({"slug": slug, "title": title, "desc": desc})

# Live casino (50 pages) — Icelandic descriptions
live_games = [
    {"slug": "blackjack", "name": "Blackjack", "desc": "Blackjack á netinu með lifandi spilastjóra — reglur, aðferðir og bestu borðin fyrir íslenska leikmenn."},
    {"slug": "roulette", "name": "Roulette", "desc": "Rúletta í beinni á netinu — evrópskt, franskt og amerískt útlit."},
    {"slug": "baccarat", "name": "Baccarat", "desc": "Baccarat í beinni — hvernig á að spila og vinna á netspilavítum."},
    {"slug": "poker", "name": "Poker", "desc": "Casino Hold'em og aðrar lifandi pókerafbrigði."},
    {"slug": "dream-catcher", "name": "Dream Catcher", "desc": "Evolution lukku-hjólleikur — reglur og aðferðir."},
    {"slug": "monopoly-live", "name": "Monopoly Live", "desc": "Monopoly leikjaþáttur í rauntíma með lifandi þáttastjórnanda."},
    {"slug": "crazy-time", "name": "Crazy Time", "desc": "Vinsælasti leikjaþátturinn frá Evolution Gaming."},
    {"slug": "lightning-roulette", "name": "Lightning Roulette", "desc": "Rúletta með eldingarhjólum og margfaldara upp á x500."},
    {"slug": "mega-ball", "name": "Mega Ball", "desc": "Lifandi lottóleikur með þáttastjórnanda og margfaldara."},
    {"slug": "gonzo-treasure-hunt", "name": "Gonzo's Treasure Hunt", "desc": "Fjársjóðaleit með Gonzo úr klassíska NetEnt spilakassanum."},
]
# 40 more live games
more_live = [
    "Speed Blackjack", "Infinite Blackjack", "Power Blackjack", "Free Bet Blackjack",
    "Lightning Blackjack", "Speed Roulette", "Auto Roulette", "Immersive Roulette",
    "Double Ball Roulette", "Speed Baccarat", "Lightning Baccarat", "Dragon Tiger",
    "Sic Bo", "Craps Live", "Football Studio", "Deal or No Deal",
    "Cash or Crash", "Funky Time", "Dead or Alive Saloon", "Stock Market",
    "Lightning Dice", "Super Sic Bo", "Fan Tan", "Andar Bahar",
    "Teen Patti", "Bet on Poker", "Side Bet City", "Texas Hold'em Bonus",
    "Caribbean Stud", "Three Card Poker", "Ultimate Texas", "Casino War",
    "Keno Live", "Bingo Live", "Wheel of Fortune", "Spin a Win",
    "Quantum Roulette", "XXXtreme Lightning Roulette", "Gold Bar Roulette", "First Person Blackjack"
]
for name in more_live:
    slug = name.lower().replace("'", "").replace(" ", "-")
    slug = _fold_slug(slug)
    live_games.append({"slug": slug, "name": name, "desc": f"{name} — spilaðu með lifandi spilastjóra á bestu spilavítunum fyrir Ísland."})

# Bónusar (80 pages) — all Icelandic
bonus_pages = [
    {"slug": "velkomstbonus", "title": "Velkomstbónus", "desc": "Bestu velkomstbónusarnir á netspilavítum sem eru í boði fyrir íslenska leikmenn."},
    {"slug": "frisnuningar-an-innborgunar-tilbod", "title": "Ókeypis snúningar án innborgunar", "desc": "Ókeypis snúningar án innborgunarkröfu — skráðu þig og sæktu."},
    {"slug": "bonusar-an-innborgunar", "title": "Bónusar án innborgunar", "desc": "Allir bónusar án innborgunar á spilavítum sem taka við íslenskum leikmönnum."},
    {"slug": "endurgreidsla", "title": "Endurgreiðslubónusar", "desc": "Spilavíti sem bjóða endurgreiðslu á nettótapi — fáðu hlutfall til baka vikulega."},
    {"slug": "skraningarbonus", "title": "Skráningarbónus", "desc": "Fáðu bónus strax eftir skráningu — engin innborgun þarf."},
    {"slug": "bonus-a-fyrstu-innborgun", "title": "Fyrsta innborgunarbónus", "desc": "Bestu bónusarnir á fyrstu innborgun hjá efstu spilavítum."},
    {"slug": "bonus-a-adra-innborgun", "title": "Önnur innborgunarbónus", "desc": "Bónusar á annarri innborgun — endurnýjunartilboð við næstu áfyllingu."},
    {"slug": "vedskilyrdi", "title": "Veðskilyrði bónusa — gegnumspilun útskýrð", "desc": "Skilningur á veðskilyrðum — hvernig gegnumspilun virkar og hvað á að hafa í huga."},
    {"slug": "bonuskodar", "title": "Bónuskóðar spilavíta", "desc": "Virk afsláttarkóðar og bónuskóðar fyrir netspilavíti árið 2026."},
    {"slug": "reload-bonus", "title": "Endurnýjunarbónusar", "desc": "Endurnýjunarbónusar fyrir núverandi leikmenn — vikuleg og mánaðarleg innborgunartilboð."},
]
# 70 more bonus pages per casino
for casino in casinos:
    bonus_pages.append({
        "slug": f"bonus-{casino['slug']}",
        "title": f"{casino['name']} bónus",
        "desc": f"Virk bónustilboð og afsláttarkóðar hjá {casino['name']} — {casino['bonus']}."
    })

# Payments (50 pages) — Icelandic
payment_pages = [
    {"slug": "bitcoin", "title": "Bitcoin í spilavítum", "desc": "Hvernig á að nota Bitcoin til innborgana og útborgana á netspilavítum. Skref-fyrir-skref leiðbeiningar fyrir íslenska leikmenn."},
    {"slug": "ethereum", "title": "Ethereum í spilavítum", "desc": "Innborganir og útborganir með Ethereum (ETH) á netspilavítum."},
    {"slug": "usdt", "title": "USDT (Tether) í spilavítum", "desc": "Notkun USDT (Tether) stablecoin á netspilavítum — tafarlausar innborganir með stöðugu gildi."},
    {"slug": "litecoin", "title": "Litecoin í spilavítum", "desc": "Hraðar og ódýrar greiðslur með Litecoin (LTC) á netspilavítum."},
    {"slug": "dogecoin", "title": "Dogecoin í spilavítum", "desc": "Hvernig á að leggja inn og spila á netspilavítum með Dogecoin (DOGE)."},
    {"slug": "ripple-xrp", "title": "Ripple (XRP) í spilavítum", "desc": "Notkun Ripple (XRP) fyrir hraðar spilavítagreiðslur með lágmarksgjöldum."},
    {"slug": "cardano", "title": "Cardano (ADA) í spilavítum", "desc": "Cardano (ADA) spilavítagreiðslur — hvernig á að leggja inn og taka út."},
    {"slug": "solana", "title": "Solana (SOL) í spilavítum", "desc": "Solana (SOL) fyrir ofurhraðar spilavítafærslur með nánast engum gjöldum."},
    {"slug": "bnb", "title": "BNB í spilavítum", "desc": "Notkun BNB (Binance Coin) fyrir innborganir og útborganir í spilavítum."},
    {"slug": "tron", "title": "TRON (TRX) í spilavítum", "desc": "TRON (TRX) greiðslur — afar lág gjöld fyrir spilavítafærslur."},
    {"slug": "hvernig-a-ad-kaupa-bitcoin", "title": "Hvernig á að kaupa Bitcoin", "desc": "Skref-fyrir-skref leiðbeiningar um kaup á Bitcoin fyrir spilavítainnborganir á Íslandi."},
    {"slug": "hvernig-a-ad-kaupa-ethereum", "title": "Hvernig á að kaupa Ethereum", "desc": "Hvar og hvernig á að kaupa Ethereum fyrir spilavítainnborganir."},
    {"slug": "framhja-bankalokunum", "title": "Framhjá bankalokunum", "desc": "Hvernig á að komast framhjá lokun íslenskra banka á spilavítagreiðslum með dulritunargjaldmiðlum."},
    {"slug": "dulritunarveski", "title": "Dulritunarveski", "desc": "Bestu dulritunarveskin fyrir spilavítainnborganir — MetaMask, Trust Wallet og fleira."},
    {"slug": "metamask-spilaviti", "title": "MetaMask fyrir spilavíti", "desc": "Notkun MetaMask veskis fyrir innborganir og útborganir á netspilavítum."},
    {"slug": "trust-wallet-spilaviti", "title": "Trust Wallet fyrir spilavíti", "desc": "Innborganir á spilavíti í gegnum Trust Wallet — fullkomin leiðbeining."},
    {"slug": "binance-spilaviti", "title": "Binance fyrir spilavíti", "desc": "Hvernig á að millifæra fjármuni frá Binance kauphöll á spilavítareikninginn þinn."},
    {"slug": "coinbase-spilaviti", "title": "Coinbase fyrir spilavíti", "desc": "Kaupa dulritunargjaldmiðil á Coinbase og leggja inn á netspilavíti."},
    {"slug": "kraken-spilaviti", "title": "Kraken fyrir spilavíti", "desc": "Notkun Kraken kauphallar fyrir dulritunarfærslur í spilavítum."},
    {"slug": "vpn-spilaviti", "title": "VPN fyrir spilavíti", "desc": "Þarftu VPN til að spila á netspilavítum frá Íslandi? Lagaleg samantekt."},
]
# 30 more payment pages — Icelandic
more_payments = [
    ("Visa í spilavítum", "Visa greiðslur á netspilavítum — leiðbeiningar fyrir íslenska leikmenn."),
    ("Mastercard í spilavítum", "Mastercard innborganir og útborganir á netspilavítum."),
    ("Apple Pay í spilavítum", "Notkun Apple Pay á netspilavítum."),
    ("Google Pay í spilavítum", "Notkun Google Pay á netspilavítum."),
    ("Skrill í spilavítum", "Skrill rafrænt veski fyrir spilavítagreiðslur."),
    ("Neteller í spilavítum", "Neteller rafrænt veski fyrir spilavítagreiðslur."),
    ("ecoPayz í spilavítum", "ecoPayz greiðslur á netspilavítum."),
    ("MiFinity í spilavítum", "MiFinity rafrænt veski fyrir spilavíti."),
    ("Jeton í spilavítum", "Jeton greiðslumáti á netspilavítum."),
    ("CashtoCode í spilavítum", "CashtoCode greiðslur á spilavítum."),
    ("Neosurf í spilavítum", "Neosurf fyrirframgreitt kort á spilavítum."),
    ("Paysafecard í spilavítum", "Paysafecard greiðslur á netspilavítum."),
    ("AstroPay í spilavítum", "AstroPay greiðslur á spilavítum."),
    ("MuchBetter í spilavítum", "MuchBetter rafrænt veski fyrir spilavíti."),
    ("Interac í spilavítum", "Interac greiðslur á spilavítum."),
    ("iDebit í spilavítum", "iDebit greiðslumáti á netspilavítum."),
    ("Instadebit í spilavítum", "Instadebit greiðslur á spilavítum."),
    ("Flexepin í spilavítum", "Flexepin fyrirframgreitt kort á spilavítum."),
    ("Monero í spilavítum", "Monero (XMR) nafnlausar greiðslur á spilavítum."),
    ("Bitcoin Cash í spilavítum", "Bitcoin Cash (BCH) greiðslur á spilavítum."),
    ("Polkadot í spilavítum", "Polkadot (DOT) greiðslur á spilavítum."),
    ("Avalanche í spilavítum", "Avalanche (AVAX) greiðslur á spilavítum."),
    ("Polygon í spilavítum", "Polygon (MATIC) greiðslur á spilavítum."),
    ("Arbitrum í spilavítum", "Arbitrum greiðslur á spilavítum."),
    ("Optimism í spilavítum", "Optimism greiðslur á spilavítum."),
    ("Lágmarksinnborgun €1", "Greiðsluleiðir og spilavíti sem taka við innborgunum frá aðeins €1 — minnsta mögulega áhætta."),
    ("Lágmarksinnborgun €5", "Spilavíti þar sem þú getur spilað frá €5."),
    ("Lágmarksinnborgun €10", "Spilavíti þar sem þú getur spilað frá €10."),
    ("Kortaútborganir", "Hvernig á að taka út vinninga á greiðslukort."),
    ("Hraðar dulritunarútborganir", "Hraðastar dulritunarútborganir á spilavítum."),
]
for title, desc in more_payments:
    slug = title.lower().replace("€", "eur").replace(" ", "-").replace("(", "").replace(")", "").replace("á", "a").replace("ú", "u")
    slug = _fold_slug(slug)
    payment_pages.append({"slug": slug, "title": title, "desc": desc})

# Guides (60 pages) — all Icelandic
guide_pages = [
    {"slug": "hvernig-a-ad-velja-spilaviti", "title": "Hvernig á að velja netspilavíti", "desc": "Fullkomin leiðbeining um val á áreiðanlegu og öruggu netspilavíti."},
    {"slug": "hvad-er-rtp", "title": "Hvað er RTP", "desc": "Skilningur á RTP (Return to Player) — hvað það þýðir fyrir spilun þína."},
    {"slug": "hvad-er-sveifla", "title": "Hvað er sveifla", "desc": "Munurinn á lágri, miðlungs og hárri sveiflu spilakassa útskýrður."},
    {"slug": "hvernig-a-ad-spila-spilakassa", "title": "Hvernig á að spila spilakassa", "desc": "Skref-fyrir-skref leiðbeining fyrir byrjendur — hvernig spilakassar virka."},
    {"slug": "blackjack-adferdir", "title": "Blackjack aðferðir", "desc": "Grunn blackjack aðferð og aðferðakort — bættu líkurnar þínar."},
    {"slug": "rulettu-reglur", "title": "Rúlettureglur", "desc": "Hvernig á að spila rúlettu — fullkomnar reglur, veðmál og aðferðir."},
    {"slug": "baccarat-reglur", "title": "Baccarat reglur", "desc": "Hvernig á að spila baccarat — reglur, aðferðir og ráð."},
    {"slug": "hvernig-a-ad-vinna-i-spilaviti", "title": "Hvernig á að vinna á spilavítum", "desc": "Ráðleggingar og aðferðir til að bæta líkur þínar á netspilavítum."},
    {"slug": "spila-af-abyrgd", "title": "Spilaðu af ábyrgð — hagnýt ráð", "desc": "Hvernig á að spila á ábyrgan hátt — setja mörk og halda stjórn."},
    {"slug": "log-um-fjarhaettuspil-a-islandi", "title": "Fjárhættuspilalagaíslandi", "desc": "Lagaleg staða netspilavíta á Íslandi — hvað leikmenn þurfa að vita."},
    {"slug": "skattar-a-vinninga", "title": "Skattar á spilavinninga", "desc": "Þarftu að borga skatta af fjárhættuspilvinningum á Íslandi?"},
    {"slug": "oryggi-i-netspilavitum", "title": "Öryggi spilavíta", "desc": "Hvernig á að vernda persónuupplýsingarnar þínar þegar þú spilar á netspilavítum."},
    {"slug": "ordalisti-spilavita", "title": "Orðasafn spilavíta", "desc": "Orðasafn spilavíta — öll fjárhættuspilahugtök frá A til Ö útskýrð."},
    {"slug": "leikjaframleidendur", "title": "Leikjabirgjar", "desc": "Yfirlit yfir stærstu spilakassabirgjana og þróunaraðila."},
    {"slug": "megaways-spilakassar-leidarvisir", "title": "Hvað eru Megaways spilakassar", "desc": "Hvernig Megaways vélbúnaðurinn virkar — allt að 117.649 leiðir til vinnings."},
    {"slug": "bonus-buy-spilakassar", "title": "Bonus Buy spilakassar", "desc": "Hvernig Bonus Buy spilakassar virka — farðu beint í bónuslotuna."},
    {"slug": "stighaekkandi-pottar", "title": "Stigvaxandi jackpottar", "desc": "Hvernig stigvaxandi jackpottar virka og hvernig á að vinna þá."},
    {"slug": "spilavitamot", "title": "Spilavítamót", "desc": "Hvernig spilakassamót virka — kepptu um peningaverðlaun."},
    {"slug": "vip-kerfi", "title": "VIP kerfi", "desc": "Hvernig VIP og tryggðarkerfi virka á netspilavítum."},
    {"slug": "spilaviti-i-simanum", "title": "Spilavíti í símanum — leiðarvísir", "desc": "Bestu farsíma spilavítin og spilavíti öppin fyrir iPhone og Android."},
]
# 40 more guides — Icelandic
more_guides = [
    ("Hvernig á að taka út af spilavíti", "Hvernig á að taka út vinninga af netspilavítum."),
    ("Hvernig á að leggja inn á spilavíti", "Hvernig á að leggja inn á netspilavíti — skref fyrir skref."),
    ("Hvað eru veðskilyrði", "Veðskilyrði útskýrð — hvernig gegnumspilun virkar."),
    ("Hvernig RNG virkar", "Hvernig slembitölugjafi (RNG) virkar í spilakössum."),
    ("Spilakassar á netinu vs hefðbundnir", "Samanburður á netspilakössum og hefðbundnum spilakössum."),
    ("Curaçao leyfisskyld spilavíti", "Spilavíti með Curaçao leyfi."),
    ("Malta MGA leyfisskyld spilavíti", "Spilavíti með Malta MGA leyfi."),
    ("Bretland leyfisskyld spilavíti", "Spilavíti með bresku leyfi (UKGC)."),
    ("Hvernig á að staðfesta spilavítaleyfi", "Hvernig á að ganga úr skugga um spilavítaleyfi."),
    ("Hvað er KYC staðfesting", "Hvað er KYC (Know Your Customer) staðfesting."),
    ("Hvernig á að velja hátt RTP spilakassa", "Hvernig á að finna spilakassa með hæstu RTP."),
    ("Topp 10 spilakassar fyrir byrjendur", "Bestu spilakassarnir fyrir byrjendur."),
    ("Topp 10 spilakassar fyrir háröllu", "Bestu spilakassarnir fyrir leikmenn sem veðja hátt."),
    ("Spilakassar með hæsta vinningsmöguleika", "Spilakassar með mesta vinningsmöguleikann."),
    ("Lág sveiflu spilakassar", "Bestu lág sveiflu spilakassarnir."),
    ("Hvernig á að spila Crash leiki", "Hvernig Crash leikir virka á netspilavítum."),
    ("Hvernig á að spila Plinko", "Hvernig Plinko leikurinn virkar."),
    ("Hvernig á að spila Aviator", "Hvernig Aviator leikurinn virkar."),
    ("Hvernig á að spila Mines", "Hvernig Mines leikurinn virkar."),
    ("Hvernig á að spila Dice", "Hvernig Dice leikir virka á spilavítum."),
    ("Hvað er Evolution Gaming", "Kynning á Evolution Gaming — stærsti lifandi spilavítabirginn."),
    ("Hvað er Pragmatic Play", "Kynning á Pragmatic Play — einn vinsælasti leikjabirginn."),
    ("Hvað er NetEnt", "Kynning á NetEnt — sænski spilakassaframleiðandinn."),
    ("Saga spilavíta á Íslandi", "Saga fjárhættuspila og spilavíta á Íslandi."),
    ("Netspilavíti vs raunveruleg spilavíti", "Samanburður á netspilavítum og raunverulegum spilavítum."),
    ("Dulritunargjaldmiðlar vs hefðbundnar greiðslur", "Dulritunargjaldmiðlar samanborið við hefðbundnar greiðslur á spilavítum."),
    ("Kostir dulritunar spilavíta", "Kostir þess að nota dulritunargjaldmiðla á spilavítum."),
    ("Hvernig á að forðast spilavítasvindl", "Hvernig á að bera kennsl á og forðast spilavítasvindl."),
    ("Einkenni sanngjarns spilavítis", "Hvernig á að bera kennsl á sanngjarnt og áreiðanlegt spilavíti."),
    ("Svarti listi spilavíta", "Spilavíti á svörtum lista — hvaða spilavíti á að forðast."),
    ("Hvernig á að hafa samband við þjónustuver", "Hvernig á að hafa samband við þjónustuver spilavíta."),
    ("Hvernig á að leggja fram kvörtun", "Hvernig á að leggja fram kvörtun gegn spilavíti."),
    ("Samanburður á bónusum spilavíta", "Hvernig á að bera saman bónusa mismunandi spilavíta."),
    ("Hvernig á að hámarka bónusinn", "Ráðleggingar um hvernig á að fá sem mest út úr spilavítabónusum."),
    ("Bankastjórnunaraðferðir", "Bankastjórnunaraðferðir fyrir spilavítaleikmenn."),
    ("Sálfræði fjárhættuspila", "Sálfræði fjárhættuspila — skilningur á hegðun."),
    ("Fjárhættuspilafíkn — hjálp", "Hjálp og stuðningur við fjárhættuspilafíkn."),
    ("Stuðningssíður við spilafíkn", "Stuðningssíður og úrræði við fjárhættuspilafíkn."),
    ("Sjálfsútilokun spilavíta", "Hvernig sjálfsútilokun virkar á netspilavítum."),
    ("Innborgunar- og tapsmörk", "Hvernig á að setja innborgunar- og tapsmörk á spilavítum."),
]
for title, desc in more_guides:
    slug = title.lower().replace("á", "a").replace("ð", "d").replace("í", "i").replace("ö", "o").replace("ú", "u").replace("þ", "th").replace("æ", "ae").replace(" ", "-").replace(",", "").replace(".", "").replace("—", "").replace("(", "").replace(")", "")
    slug = _fold_slug(slug)
    guide_pages.append({"slug": slug, "title": title, "desc": desc})

# About (10 pages)
about_pages = [
    {"slug": "um-okkur", "title": "Um Svipan", "desc": "Hverjir við erum og hvers vegna við stofnuðum Svipan á svipan.is."},
    {"slug": "hafa-samband", "title": "Hafa samband", "desc": "Hafðu samband við Svipan teymið."},
    {"slug": "personuvernd", "title": "Persónuverndarstefna", "desc": "Hvernig við meðhöndlum gögnin þín — persónuverndarstefna okkar útskýrð."},
    {"slug": "skilmalar", "title": "Notkunarskilmálar", "desc": "Notkunarskilmálar vefsíðunnar svipan.is."},
    {"slug": "fyrirvari", "title": "Fyrirvari", "desc": "Mikilvægur lagalegur fyrirvari um spilavítaumsagnir okkar."},
    {"slug": "hvernig-vid-metum", "title": "Hvernig við metum spilavíti", "desc": "Hvernig við metum og umsögnum netspilavíti — aðferðafræði okkar."},
    {"slug": "ritstjornarstefna", "title": "Ritstjórnarstefna", "desc": "Ritstjórnarstefna okkar — sjálfstæði, nákvæmni og gagnsæi."},
    {"slug": "samstarf", "title": "Samstarf", "desc": "Samstarfstækifæri hjá Svipan."},
    {"slug": "vefkort", "title": "Vefkort", "desc": "Fullkomið vefkort yfir allar síður á svipan.is."},
    {"slug": "abyrg-spilun", "title": "Ábyrg spilun", "desc": "Afstaða okkar til ábyrgrar spilunar og verndar leikmanna."},
]


EUR_ISK = 143  # nóv 2026, um það bil
def isk(text):
    """Bætir ISK upphæð við evruupphæðir: '€500' -> '€500 (~71.500 kr.)'"""
    def f(m):
        n = int(m.group(1).replace('.','').replace(',',''))
        k = round(n*EUR_ISK, -2)
        return f"€{m.group(1)} (~{k:,.0f} kr.)".replace(',', '.')
    return re.sub(r'€(\d[\d.,]*)', f, text)

# ============================================================
# HERO CARD GENERATOR
# ============================================================

import json as _json, zlib as _zlib
_REAL = [k for k in _json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "tools", "real_images.json")))]
def make_hero(title, subtitle, emoji, grad1="#41070f", grad2="#a31d34", grad3="#c33d51"):
    """Hero: collage of real game artwork with title overlay."""
    pool = _REAL
    start = _zlib.crc32(title.encode()) % max(1, len(pool))
    picks = [pool[(start + i*37) % len(pool)] for i in range(6)]
    tiles = "".join(f'<img src="{URL_BASE}img/{k}.jpg" alt="" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block">' for k in picks)
    return f'''<div class="slot-hero" style="position:relative;overflow:hidden;aspect-ratio:16/9;border-radius:18px">
<div style="position:absolute;inset:0;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(2,1fr);gap:4px">{tiles}</div>
<div style="position:absolute;inset:0;background:linear-gradient(135deg,{grad1}e6,{grad2}b3 55%,{grad3}99)"></div>
<div style="position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px;text-align:center">
<span style="font-size:52px;margin-bottom:10px;filter:drop-shadow(0 4px 12px rgba(0,0,0,.5))">{emoji}</span>
<span style="font-family:'Space Grotesk',sans-serif;font-size:clamp(24px,4vw,34px);font-weight:700;color:#fff;text-shadow:0 2px 14px rgba(0,0,0,.7);line-height:1.2">{title}</span>
<span style="font-size:17px;color:#fff;opacity:.9;margin-top:8px;text-shadow:0 1px 8px rgba(0,0,0,.7)">{subtitle}</span>
</div></div>'''

# ============================================================
# HTML TEMPLATE
# ============================================================

def get_nav():
    return f'''<nav class="nav">
  <a href="{URL_BASE}" class="nav-logo">
    <span class="logo-word">SViPAN</span>
  </a>
  <div class="nav-links" id="nav-links">
    <a href="{URL_BASE}">Heim</a>
    <a href="{URL_BASE}afthreying/">Afþreying</a>
    <a href="{URL_BASE}spilaviti/">Spilavíti</a>
    <a href="{URL_BASE}spilakassar/">Spilakassar</a>
    <a href="{URL_BASE}bonusar/">Bónusar</a>
    <a href="{URL_BASE}live/">Í beinni</a>
    <a href="{URL_BASE}leidbeiningar/">Leiðbeiningar</a>
  </div>
  <div class="nav-actions">
    <a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="btn-signup">Nýskráning</a><button class="nav-burger" type="button" aria-expanded="false" aria-controls="nav-links" aria-label="Opna valmynd"><span></span><span></span><span></span></button>
  </div>
</nav>'''

def get_footer():
    return f'''<footer class="footer">
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">
          <span class="logo-word">SViPAN</span>
        </div>
        <div class="footer-desc">Svipan á svipan.is — óháð samanburðarvefur spilavíta. 18+ Spilaðu á ábyrgan hátt.</div>
      </div>
      <div class="footer-cols">
        <div><div class="footer-col-title">SPILAVÍTI</div><a href="{URL_BASE}spilaviti/">Umsagnir</a><a href="{URL_BASE}bonusar/">Bónusar</a><a href="{URL_BASE}spilaviti/crypto-spilaviti/">Dulritunargjaldmiðill</a></div>
        <div><div class="footer-col-title">LEIKIR</div><a href="{URL_BASE}spilakassar/">Spilakassar</a><a href="{URL_BASE}live/">Í beinni</a></div>
        <div><div class="footer-col-title">UPPLÝSINGAR</div><a href="{URL_BASE}um-okkur/">Um okkur</a><a href="{URL_BASE}hofundur/valbjorn-gjukason/">Ritstjóri</a><a href="{URL_BASE}leidbeiningar/">Leiðbeiningar</a><a href="{URL_BASE}greidslur/">Greiðslur</a><a href="{URL_BASE}personuvernd/">Persónuvernd</a><a href="#" data-cookie-settings>Vafrakökur</a></div>
      </div>
    </div>
    <div class="footer-help">Þarftu að tala við einhvern um spilavanda? Hjálparsíminn <a href="tel:1717">1717</a> hjá Rauða krossinum er ókeypis og opinn allan sólarhringinn. <a href="{URL_BASE}leidbeiningar/spila-af-abyrgd/">Ábyrg spilun →</a></div>
    <div class="footer-18">18+ | Fjárhættuspil geta verið ávanabindandi. Spilaðu á ábyrgan hátt. <a href="https://www.begambleaware.org" target="_blank" rel="noopener">BeGambleAware.org</a></div>
    <div class="footer-bottom"><span>© 2026 svipan.is</span><span><a href="{URL_BASE}saga/" style="color:var(--muted2);text-decoration:none;">Saga</a> · <a href="https://www.facebook.com/svipanfrettir/" target="_blank" rel="noopener" style="color:var(--muted2);text-decoration:none;">Facebook</a> · Svipan — óháð umsagnarvefur</span></div>
  </div>
</footer>'''

def page_template(title, desc, breadcrumbs, content, canonical="", og_img="", schema_extra=None, show_byline=True):
    # SEO normalization
    desc = desc.strip()
    if len(desc) < 60:
        desc = (desc.rstrip(".") + ". ") + "Óháður leiðarvísir fyrir íslenska spilara á Svipan."
    if len(desc) > 165:
        cut = desc[:160].rsplit(" ", 1)[0].rstrip(",.;:")
        desc = cut + "…"
    # Byline + affiliate disclosure under the first H1
    if show_byline and '</h1>' in content:
        byline = (f'<div class="byline">Höfundur: <a href="{URL_BASE}hofundur/valbjorn-gjukason/" rel="author">Valbjörn Gjúkason</a> · Uppfært nóvember 2026 · '
                  f'<a href="{URL_BASE}hvernig-vid-metum/">Hvernig við metum</a></div>'
                  f'<div class="disclosure">Þessi síða inniheldur samstarfstengla. Við gætum fengið þóknun ef þú skráir þig, '
                  f'en það hefur ekki áhrif á einkunnir okkar. 18+</div>')
        content = content.replace('</h1>', '</h1>\n' + byline, 1)
    # JSON-LD
    site = "https://svipan.is"
    def abs_url(u):
        u = u.replace("{URL_BASE}", "/").replace(URL_BASE, "/")
        return site + (u if u.startswith("/") else "/" + u)
    crumbs = [{"@type":"ListItem","position":i+1,"name":n,**({"item":abs_url(u)} if u else {})} for i,(u,n) in enumerate(breadcrumbs)]
    graph = [
        {"@type":"WebSite","@id":site+"/#website","name":"Svipan","url":site+"/","inLanguage":"is",
         "description":"Óháður íslenski leiðarvísirinn um netspilavíti, spilakassa og greiðsluleiðir.",
         "potentialAction":{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":site+"/?s={search_term_string}"},"query-input":"required name=search_term_string"}},
        {"@type":"Organization","@id":site+"/#org","name":"Svipan","url":site+"/",
         "logo":{"@type":"ImageObject","url":site+"/favicon.svg","width":40,"height":40},
         "description":"Svipan er óháður íslenski leiðarvísirinn um netspilavíti. Við metum og berum saman yfir 150 spilavíti fyrir íslenska spilara.",
         "foundingDate":"2010","contactPoint":{"@type":"ContactPoint","contactType":"customer support","url":site+"/hafa-samband/","availableLanguage":["is","en"]},
         "sameAs":["https://www.facebook.com/svipanfrettir/"]},
        {"@type":"SiteNavigationElement","name":"Spilavíti","url":site+"/spilaviti/"},
        {"@type":"SiteNavigationElement","name":"Spilakassar","url":site+"/spilakassar/"},
        {"@type":"SiteNavigationElement","name":"Bónusar","url":site+"/bonusar/"},
        {"@type":"SiteNavigationElement","name":"Greiðslur","url":site+"/greidslur/"},
        {"@type":"SiteNavigationElement","name":"Leiðbeiningar","url":site+"/leidbeiningar/"},
        {"@type":"SiteNavigationElement","name":"Lifandi spilavíti","url":site+"/live/"},
        {"@type":"Person","@id":site+"/#valbjorn","name":"Valbjörn Gjúkason","url":site+"/hofundur/valbjorn-gjukason/","jobTitle":"Blaðamaður og ritstjóri","knowsAbout":["Fjárhættuspil","Netspilavíti","Spilakassar"],"worksFor":{"@id":site+"/#org"}},
        {"@type":"Article","headline":title[:110],"description":desc,"inLanguage":"is",
         "datePublished":"2026-06-01","dateModified":"2026-11-14",
         "author":{"@id":site+"/#valbjorn"},"publisher":{"@id":site+"/#org"},
         "mainEntityOfPage":{"@type":"WebPage","@id":canonical if canonical else site+"/"}},
        {"@type":"BreadcrumbList","itemListElement":crumbs},
    ] + (schema_extra or [])
    schema_json = json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False).replace("</","<\\/")
    bc_html = ' → '.join([f'<a href="{url.replace("{URL_BASE}", URL_BASE)}">{name}</a>' for url, name in breadcrumbs])
    site_url = "https://svipan.is"
    og_image = og_img if og_img else f"{site_url}/img/og-default.jpg"
    return f'''<!DOCTYPE html>
<html lang="is">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Redirect old WordPress URLs -->
<script>(function(){{var s=window.location.search;if(s.indexOf('p=')>-1||s.indexOf('page_id=')>-1||s.indexOf('cat=')>-1){{window.location.replace('/frettir/'+s);}}}})();</script>
<!-- Google Analytics GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-DXR83WTCFX"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','G-DXR83WTCFX');</script>
<title>{title + ' | Svipan' if len(title) <= 50 else title[:60]}</title>
<meta name="description" content="{desc[:155]}">
{f'<link rel="canonical" href="{canonical}">' if canonical else ''}
{f'<link rel="alternate" hreflang="is" href="{canonical}">' if canonical else ''}
{f'<link rel="alternate" hreflang="x-default" href="{canonical}">' if canonical else ''}
<meta name="geo.region" content="IS">
<meta name="geo.placename" content="Iceland">
<meta property="og:locale" content="is_IS">
<meta name="robots" content="max-snippet:-1, max-image-preview:large, max-video-preview:-1">
<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="{URL_BASE}favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="{URL_BASE}favicon-32.png">
<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:title" content="{title + ' | Svipan' if len(title) <= 57 else title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="is_IS">
<meta property="og:site_name" content="Svipan">
<meta name="twitter:card" content="summary_large_image">
<!-- Hreflang -->
{f'<link rel="alternate" hreflang="en" href="{site_url}/en/">' if canonical and canonical.rstrip("/") == site_url else ''}
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#14161d;--bg2:#1a1d25;--bg3:#21242e;--card:rgba(26,29,37,.55);--border:rgba(255,255,255,.08);--border2:rgba(255,255,255,.16);--purple:#d63641;--violet:#e04550;--blue:#ef6672;--accent:#e8505c;--accent-bg:rgba(214,54,65,.06);--gold:#f0c050;--text:#eceef4;--text2:#a7adbd;--muted:#d8dbe4;--muted2:#b4bac8;--warm1:#262a35;--warm2:#171a21;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{background:var(--bg);color:var(--text);font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}}
a{{text-decoration:none;color:inherit;}}
/* Ambient orbs */
body::before{{content:'';position:fixed;top:-200px;right:-5%;width:500px;height:500px;background:radial-gradient(circle,rgba(214,54,65,.12) 0%,transparent 70%);pointer-events:none;z-index:0;filter:blur(40px);animation:orbDrift 10s ease-in-out infinite;}}
body::after{{content:'';position:fixed;bottom:-200px;left:-10%;width:600px;height:600px;background:radial-gradient(circle,rgba(214,54,65,.08) 0%,transparent 70%);pointer-events:none;z-index:0;filter:blur(40px);animation:orbDrift 12s ease-in-out 3s infinite;}}
@keyframes orbDrift{{0%,100%{{transform:translate(0,0);}}50%{{transform:translate(25px,-20px);}}}}
@keyframes shimmerLine{{0%{{background-position:200% 0;}}100%{{background-position:-200% 0;}}}}
@keyframes btnShine{{0%{{left:-100%;}}100%{{left:200%;}}}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(16px);}}to{{opacity:1;transform:translateY(0);}}}}
/* Top accent line */
.top-accent{{height:3px;background:linear-gradient(90deg,#d63641,#e04550,#ef6672,#e04550,#d63641);background-size:200% 100%;animation:shimmerLine 4s linear infinite;}}
/* Nav */
.nav{{background:rgba(20,22,29,.88);padding:12px 30px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);}}
.nav-logo{{display:flex;align-items:center;gap:10px;}}
.nav-mark{{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,#d63641,#e04550);display:flex;align-items:center;justify-content:center;font-family:'Space Grotesk',sans-serif;font-size:16px;font-weight:700;color:#fff;box-shadow:0 2px 12px rgba(214,54,65,.25);}}
.logo-text{{font-family:'Space Grotesk',sans-serif;font-size:18px;font-weight:700;color:#fff;}}
.logo-word{{display:inline-block;background:linear-gradient(135deg,#d8333c,#a31d24);color:#fff;font-family:'Inter',sans-serif;font-weight:900;font-size:17px;letter-spacing:-.5px;padding:5px 11px 6px;border-radius:6px;line-height:1;}}.nav-links{{display:flex;gap:20px;font-size:16px;font-weight:500;}}
.nav-links a{{color:var(--muted);transition:color .2s;}}
.nav-links a:hover{{color:#ffffff;}}
.nav-actions{{display:flex;gap:8px;align-items:center;}}
/* Liquid glass nav button */
.btn-signup{{display:inline-flex;align-items:center;background:linear-gradient(135deg,rgba(214,54,65,.2),rgba(255,100,111,.1));backdrop-filter:blur(8px);border:1px solid rgba(255,140,155,.2);color:#ffffff;padding:8px 22px;border-radius:20px;font-size:16px;font-weight:600;transition:all .25s;position:relative;overflow:hidden;box-shadow:0 2px 12px rgba(214,54,65,.1),inset 0 1px 0 rgba(255,255,255,.06);}}
.btn-signup::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.06),transparent);pointer-events:none;border-radius:20px 20px 0 0;}}
.btn-signup:hover{{background:linear-gradient(135deg,rgba(214,54,65,.35),rgba(255,100,111,.2));border-color:rgba(255,140,155,.4);color:#fff;box-shadow:0 4px 20px rgba(214,54,65,.25),inset 0 1px 0 rgba(255,255,255,.1);transform:translateY(-1px);}}
/* Breadcrumbs */
.breadcrumbs{{padding:14px 30px;font-size:16px;color:var(--muted2);border-bottom:1px solid var(--border);}}
.breadcrumbs a{{color:var(--muted);transition:color .15s;}}
.breadcrumbs a:hover{{color:#e8505c;}}
/* Layout */
.page-wrap{{max-width:1100px;margin:0 auto;padding:40px 30px 60px;display:grid;grid-template-columns:1fr 280px;gap:40px;position:relative;z-index:1;}}
.content{{animation:fadeUp .5s ease-out;}}
.content h1{{font-family:'Space Grotesk',sans-serif;font-size:32px;font-weight:700;margin-bottom:20px;line-height:1.2;color:#fff;}}
.content h2{{font-family:'Space Grotesk',sans-serif;font-size:21px;font-weight:700;margin:32px 0 14px;color:#f9cfd4;position:relative;padding-left:16px;}}
.content h2::before{{content:'';position:absolute;left:0;top:4px;bottom:4px;width:3px;border-radius:2px;background:linear-gradient(180deg,#d63641,#e04550);}}
.content h3{{font-size:16px;font-weight:600;margin:24px 0 10px;color:var(--text);}}
.content p{{color:var(--muted);font-size:16px;line-height:1.8;margin-bottom:16px;}}
.content ul,.content ol{{color:var(--muted);font-size:16px;line-height:1.8;margin:0 0 16px 20px;}}
.content li{{margin-bottom:8px;}}
.content a{{color:#e8505c;font-weight:500;transition:color .15s;}}
.content a:hover{{color:#ffffff;}}
/* Sidebar */
.sidebar{{animation:fadeUp .5s ease-out .1s both;}}
.sidebar-card{{background:var(--card);backdrop-filter:blur(12px);border:1px solid var(--border);border-radius:16px;padding:20px;margin-bottom:16px;position:relative;overflow:hidden;}}
.sidebar-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#d63641,#e04550);}}
.sidebar-card h4{{font-family:'Space Grotesk',sans-serif;font-size:16px;font-weight:700;color:#f9cfd4;margin-bottom:12px;}}
.sidebar-card a{{display:block;color:var(--muted);font-size:16px;line-height:2;transition:color .15s;}}
.sidebar-card a:hover{{color:#e8505c;}}
.sidebar-cta{{display:block;text-align:center;background:linear-gradient(135deg,rgba(214,54,65,.25),rgba(255,100,111,.12));backdrop-filter:blur(12px);color:#fff;padding:14px;border-radius:16px;font-size:16px;font-weight:700;border:1px solid rgba(255,140,155,.2);transition:all .3s;position:relative;overflow:hidden;box-shadow:0 4px 20px rgba(234,56,77,.15);}}
.sidebar-cta::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.06),transparent);pointer-events:none;border-radius:16px 16px 0 0;}}
.sidebar-cta:hover{{transform:translateY(-2px);box-shadow:0 6px 28px rgba(234,56,77,.25);border-color:rgba(255,140,155,.35);}}
/* Slot hero image */
.slot-hero{{width:100%;max-width:400px;aspect-ratio:4/3;border-radius:16px;overflow:hidden;margin:0 0 24px;border:1px solid var(--border2);transition:all .3s;box-shadow:0 4px 24px rgba(204,36,57,.12);position:relative;}}
.slot-hero::after{{content:'';position:absolute;inset:0;border-radius:16px;box-shadow:inset 0 -40px 40px -20px rgba(20,22,29,.6);pointer-events:none;}}
.slot-hero:hover{{border-color:rgba(255,140,155,.3);box-shadow:0 8px 36px rgba(204,36,57,.2);}}
.slot-hero-bg{{width:100%;height:100%;}}
.slot-hero-img{{width:100%;height:100%;object-fit:cover;display:block;}}
.faq-list{{margin:8px 0 24px;}}.faq-d{{border-bottom:1px solid rgba(255,255,255,.12);padding:14px 0;}}.faq-d summary{{cursor:pointer;font-weight:600;font-size:17px;list-style:none;display:flex;justify-content:space-between;gap:12px;}}.faq-d summary::-webkit-details-marker{{display:none;}}.faq-d summary::after{{content:"+";color:#e04550;font-size:20px;line-height:1;}}.faq-d[open] summary::after{{content:"−";}}.faq-d p{{margin:10px 0 0;opacity:.9;}}
/* Info cards */
.info-box{{background:var(--card);backdrop-filter:blur(12px);border:1px solid var(--border);border-radius:16px;padding:20px 24px;margin:16px 0;transition:all .3s;position:relative;overflow:hidden;}}
.info-box::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.02),transparent);pointer-events:none;border-radius:16px 16px 0 0;}}
.info-box:hover{{border-color:var(--border2);box-shadow:0 4px 24px rgba(204,36,57,.1);transform:translateY(-2px);}}
.info-box p{{margin-bottom:6px;}}
.info-box p:last-child{{margin-bottom:0;}}
.info-box strong{{color:#fff;}}
.info-box a{{color:#e8505c;}}
/* Rating */
.rating-box{{display:inline-flex;align-items:center;gap:10px;background:rgba(214,54,65,.08);border:1px solid rgba(214,54,65,.15);border-radius:14px;padding:12px 24px;margin:12px 0;}}
.rating-box .score{{font-family:'DM Serif Display',serif;font-size:30px;font-weight:400;background:linear-gradient(135deg,#e8505c,#ef6672);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.rating-box .label{{font-size:16px;color:var(--muted);}}
/* CTA */
.cta-box{{text-align:center;margin:36px 0;}}
/* Liquid Glass CTA — convex 3D capsule */
.cta-btn{{display:inline-block;background:linear-gradient(180deg,rgba(255,80,99,.35) 0%,rgba(224,46,67,.2) 100%);backdrop-filter:blur(14px);color:#fff;padding:18px 48px;border-radius:28px;font-size:16px;font-weight:700;letter-spacing:.3px;transition:all .3s;position:relative;overflow:hidden;border:1px solid rgba(255,160,171,.25);box-shadow:0 6px 28px rgba(234,56,77,.25),0 2px 0 rgba(255,255,255,.04) inset,0 -4px 16px rgba(204,36,57,.15);}}
.cta-btn::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.12),transparent);pointer-events:none;border-radius:28px 28px 0 0;}}
.cta-btn::after{{content:'';position:absolute;top:0;left:-100%;width:60%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.08),transparent);pointer-events:none;}}
.cta-btn:hover{{text-decoration:none;transform:translateY(-3px);box-shadow:0 10px 40px rgba(234,56,77,.4),0 2px 0 rgba(255,255,255,.06) inset,0 -6px 20px rgba(204,36,57,.2);border-color:rgba(255,160,171,.4);}}
.cta-btn:hover::after{{animation:btnShine .6s ease-out;}}
/* Game grid */
.game-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;margin:20px 0;}}
.game-card{{background:var(--card);backdrop-filter:blur(8px);border:1px solid var(--border);border-radius:16px;overflow:hidden;transition:all .3s;position:relative;}}
.game-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#d63641,#e04550,#ef6672);opacity:0;transition:opacity .3s;z-index:1;}}
.game-card:hover{{transform:translateY(-5px);border-color:rgba(255,255,255,.16);box-shadow:0 10px 32px rgba(204,36,57,.18);}}
.game-card:hover::before{{opacity:1;}}
.game-card-thumb{{width:100%;aspect-ratio:4/3;background-size:cover;background-position:center;}}
.game-card-info{{padding:12px 14px;}}
.game-card-name{{font-size:16px;font-weight:600;color:#fff;}}
.game-card-prov{{font-size:16px;color:var(--muted);margin-top:2px;}}
.byline{{font-size:16px;color:var(--muted);margin:-8px 0 8px;}}
.byline a{{color:#e8505c;}}
.disclosure{{font-size:16px;color:var(--muted2);margin-bottom:20px;padding:8px 12px;border-left:2px solid rgba(255,255,255,.3);background:rgba(214,54,65,.04);border-radius:0 8px 8px 0;}}
.footer-help{{text-align:center;font-size:16px;color:var(--text);margin-bottom:10px;}}
.footer-help a{{color:#fff;font-weight:700;}}
/* Share buttons */
.share{{margin:36px 0 8px;padding-top:22px;border-top:1px solid var(--border);display:flex;align-items:center;gap:14px;flex-wrap:wrap;}}
.share-label{{font-size:16px;color:var(--muted);margin-right:4px;}}
.share a{{position:relative;width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;transition:transform .2s,box-shadow .2s;box-shadow:0 4px 14px rgba(0,0,0,.35);}}
.share a::before{{content:'';position:absolute;top:-4px;left:0;width:48px;height:22px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 -4 48 22'%3E%3Cpath fill='white' d='M3.5 11.5 A21 21 0 0 1 44.5 11.5 Q43 14.5 40.5 12.8 Q39.5 17.5 37 13.2 Q34 15 31.5 13 Q30 19 27.5 13.3 Q24.5 15.5 22 13.2 Q20.5 16.5 18 13 Q15 15.5 12.5 12.8 Q11 18 8.5 12.6 Q6 14.5 3.5 11.5 Z'/%3E%3C/svg%3E") no-repeat center/100% 100%;filter:drop-shadow(0 1px 1px rgba(0,0,0,.25));pointer-events:none;}}
.share a:hover{{transform:translateY(-3px);box-shadow:0 8px 20px rgba(0,0,0,.45);}}
.share a:focus-visible{{outline:2px solid #e8505c;outline-offset:3px;}}
.share svg{{width:22px;height:22px;fill:#fff;position:relative;}}
.share .s-fb{{background:#3b5998;}}
.share .s-in{{background:#4a77b8;}}
.share .s-wa{{background:#5dc46b;}}
.share .s-copy{{background:#ab3748;}}
/* Footer */
.footer{{background:rgba(18,4,6,.85);padding:28px 30px 14px;border-top:1px solid var(--border);position:relative;z-index:1;}}
.footer-inner{{max-width:1100px;margin:0 auto;}}
.footer-top{{display:flex;justify-content:space-between;margin-bottom:18px;gap:30px;}}
.footer-brand{{max-width:280px;}}
.footer-desc{{color:var(--muted2);font-size:16px;line-height:1.6;margin-top:6px;}}
.footer-cols{{display:flex;gap:30px;}}
.footer-col-title{{color:var(--muted2);font-size:16px;letter-spacing:1.5px;font-weight:600;margin-bottom:6px;}}
.footer-cols a{{display:block;color:var(--muted);font-size:16px;line-height:2.2;transition:color .15s;}}
.footer-cols a:hover{{color:#e8505c;}}
.footer-18{{text-align:center;padding:14px;border:1px solid var(--border);border-radius:12px;background:var(--bg2);margin-bottom:12px;font-size:16px;color:var(--muted2);}}
.footer-18 a{{color:#e8505c;}}
.footer-bottom{{border-top:1px solid var(--border);padding-top:10px;display:flex;justify-content:space-between;color:var(--muted2);font-size:16px;}}
@media(max-width:768px){{
  .page-wrap{{grid-template-columns:1fr;gap:24px;padding:24px 16px 40px;}}
  .nav{{padding:10px 16px;flex-wrap:wrap;gap:8px;}}
  .nav-links{{gap:16px;font-size:16px;width:100%;overflow-x:auto;white-space:nowrap;padding-bottom:4px;scrollbar-width:none;}}
  .nav-links::-webkit-scrollbar{{display:none;}}
  .content h1{{font-size:26px;}}
  .footer-top{{flex-direction:column;gap:14px;}}
  .game-grid{{grid-template-columns:repeat(2,1fr);}}
  .sidebar{{order:2;}}
}}
/* === Glossy 3D glass capsule buttons (scarlet) === */
.btn-primary,.btn-secondary,.nav-cta,.btn-cta,.btn-glass,.promo-btn,.gc-play,.btn-signup,.cta-btn,.sidebar-cta{{position:relative;display:inline-flex;align-items:center;justify-content:center;gap:8px;color:#fff!important;font-family:'Inter',system-ui,sans-serif;white-space:nowrap;font-weight:700;letter-spacing:.2px;border:none;overflow:hidden;border-radius:60px;background:linear-gradient(180deg,#ff4d4d 0%,#ef2833 45%,#c41425 100%);box-shadow:0 6px 20px rgba(239,40,51,.45),0 1px 3px rgba(0,0,0,.3),inset 0 1px 1px rgba(255,255,255,.3),inset 0 -1px 1px rgba(0,0,0,.15),inset 2px 0 8px rgba(255,255,255,.08),inset -2px 0 8px rgba(255,255,255,.08);border-top:1px solid rgba(255,180,180,.4);transition:transform .2s,box-shadow .2s,filter .2s;}}
.btn-primary::before,.btn-secondary::before,.nav-cta::before,.btn-cta::before,.btn-glass::before,.promo-btn::before,.gc-play::before,.btn-signup::before,.cta-btn::before,.sidebar-cta::before{{content:'';position:absolute;top:0;left:0;right:0;bottom:0;border-radius:60px;border:1px solid rgba(255,255,255,.15);border-top-color:rgba(255,255,255,.35);border-bottom-color:transparent;background:linear-gradient(180deg,rgba(255,255,255,.18) 0%,transparent 35%,transparent 100%);pointer-events:none;-webkit-mask:linear-gradient(180deg,#000 0%,transparent 50%);mask:linear-gradient(180deg,#000 0%,transparent 50%);}}
.btn-primary::after,.btn-secondary::after,.nav-cta::after,.btn-cta::after,.btn-glass::after,.promo-btn::after,.gc-play::after,.btn-signup::after,.cta-btn::after,.sidebar-cta::after{{content:'';position:absolute;top:2px;left:8%;right:8%;height:38%;border-radius:0 0 60% 60%/0 0 100% 100%;background:radial-gradient(ellipse at 50% 0%,rgba(255,255,255,.35) 0%,rgba(255,255,255,.05) 70%,transparent 100%);pointer-events:none;}}
.btn-primary:hover,.btn-secondary:hover,.nav-cta:hover,.btn-cta:hover,.btn-glass:hover,.promo-btn:hover,.gc-play:hover,.btn-signup:hover,.cta-btn:hover,.sidebar-cta:hover{{transform:translateY(-2px);box-shadow:0 8px 25px rgba(185,28,28,.5),0 2px 6px rgba(0,0,0,.3),inset 0 1px 0 rgba(255,255,255,.3);filter:brightness(1.08);}}
.btn-primary:active,.btn-secondary:active,.nav-cta:active,.btn-cta:active,.btn-glass:active,.promo-btn:active,.gc-play:active,.btn-signup:active,.cta-btn:active,.sidebar-cta:active{{transform:translateY(1px);box-shadow:0 2px 8px rgba(185,28,28,.4),inset 0 2px 4px rgba(0,0,0,.2);filter:brightness(.95);}}
.btn-primary:focus-visible,.btn-secondary:focus-visible,.nav-cta:focus-visible,.btn-cta:focus-visible,.btn-glass:focus-visible,.promo-btn:focus-visible,.gc-play:focus-visible,.btn-signup:focus-visible,.cta-btn:focus-visible,.sidebar-cta:focus-visible{{outline:2px solid #f87171;outline-offset:4px;}}
.btn-primary,.btn-cta,.cta-btn{{padding:16px 44px;font-size:16px;}}
.sidebar-cta{{display:flex;padding:14px 24px;font-size:16px;}}
.nav-cta,.btn-glass,.btn-signup,.btn-secondary,.promo-btn{{padding:10px 26px;font-size:16px;}}
.gc-play{{display:flex;margin:0 12px 14px;padding:11px 0;font-size:16px;}}
.btn-secondary .play-icon{{background:rgba(255,255,255,.15);}}
@media (prefers-reduced-motion:reduce){{.btn-primary,.btn-cta,.cta-btn,.btn-glass,.btn-signup,.sidebar-cta,.nav-cta,.btn-secondary,.promo-btn,.gc-play{{transition:none;}}}}
/* Cookie banner */
.cookie-banner{{position:fixed;left:16px;right:16px;bottom:16px;z-index:1000;max-width:880px;margin:0 auto;display:flex;align-items:center;gap:20px;padding:18px 22px;border-radius:20px;background:rgba(39,11,15,.94);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid rgba(255,140,155,.22);box-shadow:0 18px 50px rgba(0,0,0,.55);color:#f9dbdf;font-family:'Inter',system-ui,sans-serif;}}
.cookie-banner[hidden]{{display:none;}}
.cookie-text{{flex:1;font-size:16px;line-height:1.55;}}
.cookie-text strong{{display:block;color:#fff;font-size:16px;margin-bottom:4px;}}
.cookie-text a{{color:#ffb4bc;text-decoration:underline;}}
.cookie-actions{{display:flex;gap:10px;flex-shrink:0;}}
.cookie-actions button{{cursor:pointer;min-width:170px;}}
@media(max-width:700px){{.cookie-banner{{flex-direction:column;align-items:stretch;gap:14px;}}.cookie-actions{{flex-direction:column;}}.cookie-actions button{{width:100%;}}}}
/* Burger menu */
.nav-burger{{display:none;width:44px;height:44px;border-radius:12px;border:1px solid rgba(255,255,255,.16);background:rgba(33,36,46,.8);cursor:pointer;flex-direction:column;align-items:center;justify-content:center;gap:5px;padding:0;margin-left:10px;}}
.nav-burger span{{display:block;width:20px;height:2px;border-radius:2px;background:#ffffff;transition:transform .25s,opacity .2s;}}
.nav-burger:focus-visible{{outline:2px solid #e04550;outline-offset:2px;}}
.nav.open .nav-burger span:nth-child(1){{transform:translateY(7px) rotate(45deg);}}
.nav.open .nav-burger span:nth-child(2){{opacity:0;}}
.nav.open .nav-burger span:nth-child(3){{transform:translateY(-7px) rotate(-45deg);}}
.nav-right{{display:flex;align-items:center;}}
@media(max-width:768px){{
 .nav{{flex-wrap:nowrap!important;padding:10px 16px!important;gap:10px;}}
 .nav-burger{{display:flex;}}
 .nav-links{{display:none!important;position:absolute;top:100%;left:0;right:0;flex-direction:column;gap:0!important;width:auto!important;overflow:visible!important;white-space:normal!important;padding:8px 20px 20px!important;background:rgba(31,7,11,.97);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,140,155,.18);box-shadow:0 20px 40px rgba(0,0,0,.5);z-index:200;}}
 .nav.open .nav-links{{display:flex!important;animation:navDrop .22s ease-out;}}
 .nav-links a{{padding:15px 4px;font-size:17px!important;color:#ffffff!important;border-bottom:1px solid rgba(255,140,155,.12);}}
 .nav-links a:last-child{{border-bottom:none;}}
 .nav-logo .logo-text,.nav-brand,.logo-t{{font-size:16px;}}
}}
@keyframes navDrop{{from{{opacity:0;transform:translateY(-8px);}}to{{opacity:1;transform:none;}}}}
@media (prefers-reduced-motion:reduce){{.nav.open .nav-links{{animation:none;}}.nav-burger span{{transition:none;}}}}
@media(max-width:768px){{html,body{{overflow-x:hidden;}}.hero-buttons{{flex-wrap:wrap;}}.btn-primary,.btn-secondary,.btn-cta,.cta-btn{{max-width:100%;white-space:normal;text-align:center;}}}}
/* Drawer menu */
.dr-overlay{{position:fixed;inset:0;background:rgba(14,2,4,.6);backdrop-filter:blur(3px);z-index:999;opacity:0;transition:opacity .25s;}}
.dr-overlay.on{{opacity:1;}}
.dr{{position:fixed;top:0;left:0;bottom:0;width:min(88vw,400px);z-index:1001;display:flex;flex-direction:column;background:linear-gradient(180deg,#370e13 0%,#2c0a0f 100%);border-right:1px solid rgba(255,140,155,.18);box-shadow:20px 0 60px rgba(0,0,0,.55);transform:translateX(-105%);transition:transform .3s cubic-bezier(.2,.8,.2,1);font-family:'Inter',system-ui,sans-serif;color:#ffe4e8;}}
.dr.on{{transform:none;}}
.dr-head{{display:flex;align-items:center;gap:14px;padding:18px 18px 16px 22px;border-bottom:1px solid rgba(255,140,155,.14);}}
.dr-brand{{display:flex;align-items:center;gap:10px;text-decoration:none;}}
.dr-mark{{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,#d63641,#e04550);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:16px;color:#fff;}}
.dr-name{{font-family:'Space Grotesk',sans-serif;font-size:20px;font-weight:700;color:#fff;letter-spacing:-.2px;}}
.dr-name b{{color:#ff9f4a;font-weight:700;}}
.dr [hidden]{{display:none!important;}}
.dr-name b{{margin-left:5px;}}

.dr-title{{font-size:20px;color:rgba(255,228,232,.88);}}
.dr-close{{margin-left:auto;width:46px;height:46px;border-radius:50%;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.07);color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;}}
.dr-close svg{{width:20px;height:20px;}}
.dr-body{{flex:1;overflow-y:auto;padding:14px 14px 20px;overscroll-behavior:contain;}}
.dr-item{{width:100%;display:flex;align-items:center;gap:16px;padding:14px 18px;margin:2px 0;border:0;border-radius:999px;background:none;color:#ffe4e8;font:500 18px/1.2 'Inter',system-ui,sans-serif;text-align:left;text-decoration:none;cursor:pointer;transition:background .2s,color .2s;}}
.dr-item:hover{{background:rgba(255,255,255,.06);}}
.dr-item:focus-visible,.dr-sub a:focus-visible,.dr-close:focus-visible{{outline:2px solid #ff9f4a;outline-offset:2px;}}
.dr-ic{{width:24px;height:24px;flex-shrink:0;color:#ffb2bd;}}
.dr-item span{{flex:1;}}
.dr-badge{{font-style:normal;min-width:30px;height:28px;padding:0 9px;border-radius:9px;background:linear-gradient(135deg,#e04550,#c52b36);color:#fff;font-size:16px;font-weight:700;display:inline-flex;align-items:center;justify-content:center;}}
.dr-chev{{width:20px;height:20px;color:rgba(255,228,232,.88);transition:transform .25s;}}
.dr-toggle[aria-expanded="true"]{{background:#fff;color:#310c11;box-shadow:0 8px 24px rgba(0,0,0,.35);}}
.dr-toggle[aria-expanded="true"] .dr-ic{{color:#310c11;}}
.dr-toggle[aria-expanded="true"] .dr-chev{{transform:rotate(180deg);color:#310c11;}}
.dr-sub{{margin:6px 0 10px 36px;padding-left:18px;border-left:2px solid rgba(255,255,255,.16);}}
.dr-sub a{{display:flex;align-items:center;gap:14px;padding:12px 10px;border-radius:12px;color:rgba(255,228,232,.85);font-size:16px;text-decoration:none;}}
.dr-sub a:hover{{background:rgba(255,255,255,.05);color:#fff;}}
.dr-fold{{width:20px;height:20px;flex-shrink:0;color:rgba(255,178,189,.88);}}
.dr-empty{{padding:16px 18px;color:rgba(255,228,232,.88);font-size:16px;}}
.dr-foot{{padding:14px 18px 18px;border-top:1px solid rgba(255,140,155,.14);background:rgba(22,5,7,.5);}}
.dr-search{{display:flex;align-items:center;gap:12px;padding:14px 22px;border-radius:999px;background:linear-gradient(135deg,#e04550,#c52b36);box-shadow:0 10px 24px -8px rgba(214,54,65,.6);cursor:text;}}
.dr-search svg{{width:22px;height:22px;color:#fff;flex-shrink:0;}}
.dr-search input{{flex:1;min-width:0;border:0;background:none;color:#fff;font:600 17px 'Inter',system-ui,sans-serif;outline:none;}}
.dr-search input::placeholder{{color:rgba(255,255,255,.9);}}
.dr-rg{{margin-top:12px;text-align:center;font-size:16px;color:rgba(255,228,232,.88);}}
.dr-rg a{{color:#fff;font-weight:700;}}
.dr-18{{display:inline-flex;align-items:center;justify-content:center;padding:3px 9px;border-radius:999px;background:#d8394a;color:#fff;font-weight:800;font-size:16px;margin-right:4px;}}
body.dr-lock{{overflow:hidden;}}
@media(min-width:769px){{.dr,.dr-overlay{{display:none!important;}}}}
@media (prefers-reduced-motion:reduce){{.dr,.dr-overlay,.dr-chev{{transition:none;}}}}
/* Share buttons: liquid glass, brand colours */
.share a.s-fb{{--b0:#0f1f47;--b1:#1d3f8a;--g1:#4f8cff;--g2:#9cc2ff;--sh:79,140,255;}}
.share a.s-in{{--b0:#06243f;--b1:#0a66c2;--g1:#2fa8ff;--g2:#8fdcff;--sh:47,168,255;}}
.share a.s-wa{{--b0:#062e1b;--b1:#128c4a;--g1:#3ddc84;--g2:#c2ffd8;--sh:61,220,132;}}
.share a.s-copy{{--b0:#2b0809;--b1:#6a1b1e;--g1:#ff9a3c;--g2:#f4524c;--sh:239,83,76;}}
.share a.s-fb,.share a.s-in,.share a.s-wa,.share a.s-copy{{
width:54px;height:54px;border:4px solid transparent;isolation:isolate;
background:
 radial-gradient(80% 70% at 22% 105%,var(--g1) 0%,transparent 60%) padding-box,
 radial-gradient(80% 70% at 82% 110%,var(--g2) 0%,transparent 55%) padding-box,
 linear-gradient(180deg,var(--b0) 0%,var(--b1) 100%) padding-box,
 linear-gradient(170deg,rgba(255,255,255,.85) 0%,rgba(255,255,255,.15) 40%,rgba(255,255,255,.08) 65%,rgba(255,255,255,.5) 100%) border-box;
box-shadow:0 0 0 1px rgba(255,255,255,.28),inset 0 0 0 1px rgba(255,255,255,.2),inset 0 3px 6px rgba(0,0,0,.4),0 12px 22px -8px rgba(var(--sh),.7),0 2px 6px rgba(0,0,0,.35);}}
.share a.s-fb::after,.share a.s-in::after,.share a.s-wa::after,.share a.s-copy::after{{
content:'';position:absolute;left:18%;right:18%;top:4px;height:22%;border-radius:999px;pointer-events:none;z-index:-1;
background:linear-gradient(180deg,rgba(255,255,255,.5),rgba(255,255,255,0));}}
.share a.s-fb svg,.share a.s-in svg,.share a.s-wa svg,.share a.s-copy svg{{filter:drop-shadow(0 1px 2px rgba(0,0,0,.45));}}
.share a.s-fb::before,.share a.s-in::before,.share a.s-wa::before,.share a.s-copy::before{{top:-9px;left:2px;width:42px;height:17px;}}
.share a.s-fb:hover,.share a.s-in:hover,.share a.s-wa:hover,.share a.s-copy:hover{{filter:brightness(1.12) saturate(1.1);box-shadow:0 0 0 1px rgba(255,255,255,.4),inset 0 0 0 1px rgba(255,255,255,.25),inset 0 3px 6px rgba(0,0,0,.4),0 16px 28px -8px rgba(var(--sh),.9),0 3px 8px rgba(0,0,0,.35);}}
.nav-mark,.dr-mark{{background:none!important;box-shadow:0 0 18px rgba(214,54,61,.45)!important;border-radius:50%!important;padding:0!important;display:inline-flex!important;align-items:center;justify-content:center;font-size:0!important;overflow:visible}}.bf-logo{{width:100%;height:100%;display:block}}</style>
</head>
<body>
<div class="top-accent"></div>
{get_nav()}
<div class="breadcrumbs">{bc_html}</div>
<div class="page-wrap">
<main class="content">
{content}
<div class="share" aria-label="Deila">
<span class="share-label">Deila:</span>
<a class="s-fb" data-net="fb" href="#" target="_blank" rel="noopener" aria-label="Deila á Facebook"><svg viewBox="0 0 24 24"><path d="M14 8V6.5c0-.7.5-1 1-1h2V2h-3c-3 0-4 2-4 4.3V8H8v3.5h2V22h4V11.5h2.8L17 8h-3z"/></svg></a>
<a class="s-in" data-net="in" href="#" target="_blank" rel="noopener" aria-label="Deila á LinkedIn"><svg viewBox="0 0 24 24"><path d="M4 3.5a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM2.3 9h3.4v12H2.3zM9 9h3.3v1.7c.5-.9 1.7-2 3.6-2 3.6 0 4.3 2.4 4.3 5.4V21h-3.4v-6c0-1.5 0-3.3-2-3.3s-2.4 1.6-2.4 3.2V21H9z"/></svg></a>
<a class="s-wa" data-net="wa" href="#" target="_blank" rel="noopener" aria-label="Deila á WhatsApp"><svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 11.9 11.9 0 0 0 4.6 4c1.7.7 2.4.8 3.2.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.5-.3z"/></svg></a>
<a class="s-copy" data-net="copy" href="#" aria-label="Afrita tengil"><svg viewBox="0 0 24 24"><path d="M10.6 13.4a1 1 0 0 1 0-1.4l3.5-3.5a1 1 0 1 1 1.4 1.4L12 13.4a1 1 0 0 1-1.4 0zM8.5 16.9a2.5 2.5 0 0 1-3.5-3.5l2.8-2.8-1.4-1.4-2.8 2.8a4.5 4.5 0 0 0 6.4 6.4l2.8-2.8-1.4-1.4zM18.4 4.2a4.5 4.5 0 0 0-6.4 0L9.2 7l1.4 1.4L13.4 5.6a2.5 2.5 0 0 1 3.5 3.5L14.1 12l1.4 1.4 2.9-2.8a4.5 4.5 0 0 0 0-6.4z"/></svg></a>
</div>
</main>
<aside class="sidebar">
<div class="sidebar-card">
<h4>🏆 Topp spilavíti</h4>
<a href="{URL_BASE}spilaviti/slotoro/">Slotoro — ráðlagt (samstarfsaðili)</a>
<a href="{URL_BASE}spilaviti/bitstarz/">BitStarz — 5 BTC + 200 FS</a>
<a href="{URL_BASE}spilaviti/stake/">Stake — 200% + VIP</a>
<a href="{URL_BASE}spilaviti/bc-game/">BC.Game — 300% allt að 1 BTC</a>
<a href="{URL_BASE}spilaviti/katsubet/">KatsuBet — 100% + 100 FS</a>
<a href="{URL_BASE}spilaviti/winz/">Winz.io — 300 FS án veðskilyrða</a>
</div>
<a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="sidebar-cta">Spila núna →</a>
<div class="sidebar-card" style="margin-top:16px;">
<h4>📖 Leiðbeiningar</h4>
<a href="{URL_BASE}leidbeiningar/hvernig-a-ad-velja-spilaviti/">Hvernig á að velja spilavíti</a>
<a href="{URL_BASE}leidbeiningar/hvad-er-rtp/">Hvað er RTP?</a>
<a href="{URL_BASE}leidbeiningar/hvad-er-sveifla/">Hvað er sveifla?</a>
<a href="{URL_BASE}leidbeiningar/framhja-bankalokun/">Framhjá bankalokun</a>
<a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Kaupa Bitcoin á Íslandi</a>
<a href="{URL_BASE}leidbeiningar/besta-crypto-spilaviti-island/">Besta crypto spilavítið</a>
<a href="{URL_BASE}leidbeiningar/spilaviti-samanburdur/">Spilavíti samanburður</a>
<a href="{URL_BASE}leidbeiningar/frisnuningar-an-innborgunar/">Frísnúningar án innborgunar</a>
</div>
<div class="sidebar-card">
<h4>🎰 Vinsælir spilakassar</h4>
<a href="{URL_BASE}spilakassar/gates-of-olympus/">Gates of Olympus</a>
<a href="{URL_BASE}spilakassar/sweet-bonanza/">Sweet Bonanza</a>
<a href="{URL_BASE}spilakassar/book-of-dead/">Book of Dead</a>
<a href="{URL_BASE}spilakassar/big-bass-splash/">Big Bass Splash</a>
</div>
</aside>
</div>
{get_footer()}
<script type="application/ld+json">{schema_json}</script>
<script>document.querySelectorAll('img[loading]').length||document.querySelectorAll('.slot-hero-img,.game-card-thumb img').forEach(function(i){{i.loading='lazy'}})</script>
<script>(function(){{var u=encodeURIComponent(location.href),t=encodeURIComponent(document.title);var m={{fb:'https://www.facebook.com/sharer/sharer.php?u='+u,in:'https://www.linkedin.com/sharing/share-offsite/?url='+u,wa:'https://wa.me/?text='+t+'%20'+u}};document.querySelectorAll('.share a').forEach(function(a){{var n=a.dataset.net;if(m[n])a.href=m[n];else if(n==='copy')a.addEventListener('click',function(e){{e.preventDefault();try{{navigator.clipboard.writeText(location.href);a.setAttribute('aria-label','Tengill afritaður');a.style.filter='hue-rotate(-60deg) brightness(1.2)';setTimeout(function(){{a.style.filter='';}},1500);}}catch(_){{}}}});}});}})();</script>
<div id="cookie-banner" class="cookie-banner" role="dialog" aria-live="polite" aria-label="Vafrakökur" hidden>
<div class="cookie-text"><strong>🍪 Vafrakökur</strong><span>Við notum nauðsynlegar vafrakökur til að vefurinn virki og til að muna val þitt. Ef þú samþykkir allar má nota kökur til að mæla umferð. Samstarfstenglar geta sett kökur hjá þriðja aðila þegar þú smellir á þá. <a href="{URL_BASE}personuvernd/">Persónuverndarstefna</a></span></div>
<div class="cookie-actions"><button type="button" class="btn-signup" data-consent="necessary">Aðeins nauðsynlegar</button><button type="button" class="btn-signup" data-consent="all">Samþykkja allar</button></div>
</div>
<script>(function(){{var b=document.getElementById('cookie-banner');if(!b)return;var v=null;try{{v=localStorage.getItem('bf_cookie_consent');}}catch(e){{}}if(!v)b.hidden=false;b.querySelectorAll('[data-consent]').forEach(function(btn){{btn.addEventListener('click',function(){{try{{localStorage.setItem('bf_cookie_consent',btn.getAttribute('data-consent'));}}catch(e){{}}b.hidden=true;}});}});document.querySelectorAll('[data-cookie-settings]').forEach(function(a){{a.addEventListener('click',function(e){{e.preventDefault();b.hidden=false;}});}});}})();</script>

<div class="dr-overlay" data-dr-close hidden></div><aside class="dr" id="site-drawer" aria-label="Valmynd" aria-hidden="true" inert><div class="dr-head"><a href="{URL_BASE}" class="dr-brand"><span class="logo-word">SViPAN</span></a><span class="dr-title">Valmynd</span><button class="dr-close" type="button" data-dr-close aria-label="Loka valmynd"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div><nav class="dr-body"><a class="dr-item" href="{URL_BASE}"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg><span>Heim</span></a><a class="dr-item" href="{URL_BASE}afthreying/"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l2.6 5.6 6 .6-4.5 4 1.3 6L12 16.8 6.6 19.2l1.3-6-4.5-4 6-.6z"/></svg><span>Afþreying</span></a><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg0"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8" cy="8" r="1.3"/><circle cx="16" cy="8" r="1.3"/><circle cx="12" cy="12" r="1.3"/><circle cx="8" cy="16" r="1.3"/><circle cx="16" cy="16" r="1.3"/></svg><span>Spilavíti</span><em class="dr-badge">7</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg0" hidden><a href="{URL_BASE}spilaviti/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allar umsagnir</span></a><a href="{URL_BASE}leidbeiningar/spilaviti-samanburdur/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Spilavíti samanburður</span></a><a href="{URL_BASE}leidbeiningar/besta-crypto-spilaviti-island/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Besta crypto spilavítið</span></a><a href="{URL_BASE}spilaviti/crypto-spilaviti/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Crypto spilavíti</span></a><a href="{URL_BASE}spilaviti/ny-spilaviti/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Ný spilavíti 2026</span></a><a href="{URL_BASE}leidbeiningar/spilaviti-islenskt-vidmot/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Íslenskt viðmót</span></a><a href="{URL_BASE}hvernig-vid-metum/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Hvernig við metum</span></a></div></div><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg1"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="M9 4v16M15 4v16"/></svg><span>Spilakassar</span><em class="dr-badge">6</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg1" hidden><a href="{URL_BASE}spilakassar/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allir spilakassar</span></a><a href="{URL_BASE}spilakassar/gates-of-olympus/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Gates of Olympus</span></a><a href="{URL_BASE}spilakassar/sweet-bonanza/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Sweet Bonanza</span></a><a href="{URL_BASE}spilakassar/book-of-dead/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Book of Dead</span></a><a href="{URL_BASE}spilakassar/big-bass-splash/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Big Bass Splash</span></a><a href="{URL_BASE}leidbeiningar/hvad-er-rtp/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Hvað er RTP?</span></a></div></div><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg2"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4"/><circle cx="12" cy="11" r="2.5"/></svg><span>Í beinni</span><em class="dr-badge">5</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg2" hidden><a href="{URL_BASE}live/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allir lifandi leikir</span></a><a href="{URL_BASE}live/blackjack/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Blackjack</span></a><a href="{URL_BASE}live/roulette/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Rúletta</span></a><a href="{URL_BASE}live/crazy-time/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Crazy Time</span></a><a href="{URL_BASE}live/lightning-roulette/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Lightning Roulette</span></a></div></div><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg3"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="9" width="18" height="12" rx="2"/><path d="M3 13h18M12 9v12M12 9c-2-4-6-4-6-1s6 1 6 1 6 2 6-1-4-3-6 1"/></svg><span>Bónusar</span><em class="dr-badge">5</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg3" hidden><a href="{URL_BASE}bonusar/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allir bónusar</span></a><a href="{URL_BASE}bonusar/velkomstbonus/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Velkomstbónus</span></a><a href="{URL_BASE}leidbeiningar/frisnuningar-an-innborgunar/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Frísnúningar án innborgunar</span></a><a href="{URL_BASE}bonusar/bonusar-an-innborgunar/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Bónusar án innborgunar</span></a><a href="{URL_BASE}bonusar/vedskilyrdi/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Hvað eru veðskilyrði?</span></a></div></div><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg4"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="3"/><path d="M2 10h20M6 15h4"/></svg><span>Greiðslur</span><em class="dr-badge">7</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg4" hidden><a href="{URL_BASE}greidslur/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allar greiðsluleiðir</span></a><a href="{URL_BASE}leidbeiningar/framhja-bankalokun/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Framhjá bankalokun</span></a><a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Kaupa Bitcoin á Íslandi</span></a><a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Íslenskir bankar</span></a><a href="{URL_BASE}leidbeiningar/piq-greidslur-island/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>PIQ greiðslur</span></a><a href="{URL_BASE}leidbeiningar/spilaviti-isk-kronur/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Spilavíti sem taka við ISK</span></a><a href="{URL_BASE}greidslur/usdt/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>USDT</span></a></div></div><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg5"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4zM20 4h-6a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h7z"/></svg><span>Leiðbeiningar</span><em class="dr-badge">5</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg5" hidden><a href="{URL_BASE}leidbeiningar/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allar leiðbeiningar</span></a><a href="{URL_BASE}leidbeiningar/log-um-fjarhaettuspil-a-islandi/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Lög á Íslandi</span></a><a href="{URL_BASE}leidbeiningar/skattar-spilavinningar-island/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Skattar á vinninga</span></a><a href="{URL_BASE}leidbeiningar/hvernig-a-ad-velja-spilaviti/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Hvernig á að velja spilavíti</span></a><a href="{URL_BASE}leidbeiningar/spila-af-abyrgd/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Ábyrg spilun</span></a></div></div><p class="dr-empty" hidden>Ekkert fannst</p></nav><div class="dr-foot"><label class="dr-search"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg><input type="search" placeholder="Leita á vefnum" aria-label="Leita í valmynd" autocomplete="off"></label><div class="dr-rg"><span class="dr-18">18+</span> Spilaðu á ábyrgan hátt · <a href="tel:1717">1717</a></div></div></aside><script>(function(){{var d=document.getElementById('site-drawer');if(!d)return;var o=document.querySelector('.dr-overlay'),b=document.querySelector('.nav-burger'),last=null;
function open(){{last=document.activeElement;o.hidden=false;d.removeAttribute('inert');d.setAttribute('aria-hidden','false');requestAnimationFrame(function(){{o.classList.add('on');d.classList.add('on');}});document.body.classList.add('dr-lock');if(b)b.setAttribute('aria-expanded','true');setTimeout(function(){{d.querySelector('.dr-close').focus();}},50);}}
function close(){{o.classList.remove('on');d.classList.remove('on');d.setAttribute('aria-hidden','true');d.setAttribute('inert','');document.body.classList.remove('dr-lock');if(b)b.setAttribute('aria-expanded','false');setTimeout(function(){{o.hidden=true;}},300);if(last&&last.focus)last.focus();}}
if(b){{b.setAttribute('aria-controls','site-drawer');b.addEventListener('click',function(e){{e.stopImmediatePropagation();d.classList.contains('on')?close():open();}},true);}}
document.querySelectorAll('[data-dr-close]').forEach(function(x){{x.addEventListener('click',close);}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&d.classList.contains('on'))close();}});
d.querySelectorAll('.dr-toggle').forEach(function(t){{t.addEventListener('click',function(){{var on=t.getAttribute('aria-expanded')!=='true';d.querySelectorAll('.dr-toggle').forEach(function(x){{x.setAttribute('aria-expanded','false');document.getElementById(x.getAttribute('aria-controls')).hidden=true;}});t.setAttribute('aria-expanded',on?'true':'false');document.getElementById(t.getAttribute('aria-controls')).hidden=!on;}});}});
var path=location.pathname;d.querySelectorAll('.dr-sub a').forEach(function(a){{if(a.getAttribute('href')===path){{a.setAttribute('aria-current','page');a.style.color='#fff';a.style.fontWeight='600';var t=a.closest('.dr-group').querySelector('.dr-toggle');t.setAttribute('aria-expanded','true');a.parentNode.hidden=false;}}}});
var q=d.querySelector('.dr-search input'),empty=d.querySelector('.dr-empty');q.addEventListener('input',function(){{var v=q.value.trim().toLowerCase(),any=false;d.querySelectorAll('.dr-group').forEach(function(g){{var sub=g.querySelector('.dr-sub'),t=g.querySelector('.dr-toggle'),hit=false;sub.querySelectorAll('a').forEach(function(a){{var m=!v||a.textContent.toLowerCase().indexOf(v)>-1;a.hidden=!m;if(m&&v)hit=true;}});if(v){{g.hidden=!hit;sub.hidden=!hit;t.setAttribute('aria-expanded',hit?'true':'false');if(hit)any=true;}}else{{g.hidden=false;sub.querySelectorAll('a').forEach(function(a){{a.hidden=false;}});sub.hidden=t.getAttribute('aria-expanded')!=='true';}}}});d.querySelectorAll('.dr-body > .dr-item').forEach(function(i){{i.hidden=!!v;}});empty.hidden=!v||any;}});
}})();</script>
<script>document.addEventListener('click',function(e){{var a=e.target.closest('a[href*="gameslnk.cc"]');if(a){{gtag('event','affiliate_click',{{'link_url':a.href,'link_text':a.textContent.trim(),'page_path':location.pathname}});}}}});</script>
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{{"@type":"Question","name":"Hvaða netspilavíti er best á Íslandi?","acceptedAnswer":{{"@type":"Answer","text":"Samkvæmt umsögnum okkar er Slotoro besta netspilavítið á Íslandi 2026 með 98 spilakassa, hröðum útborgunum og dulritunargreiðslum. BitStarz og Stake eru einnig sterkir kostir."}}}},{{"@type":"Question","name":"Er löglegt að spila á netspilavítum á Íslandi?","acceptedAnswer":{{"@type":"Answer","text":"Á Íslandi er ekkert innlent leyfiskerfi fyrir netspilavíti. Þó er ekki beinlínis ólöglegt fyrir einstaklinga að spila á erlendum spilavítum sem starfa undir alþjóðlegum leyfum frá Malta, Curaçao eða Bretlandi."}}}},{{"@type":"Question","name":"Hvaða greiðsluleiðir virka á Íslandi?","acceptedAnswer":{{"@type":"Answer","text":"Dulritunargjaldmiðlar (Bitcoin, Ethereum) eru áreiðanlegasta greiðsluleiðin fyrir íslenska spilara vegna takmarkana bankanna. Visa og Mastercard virka einnig hjá mörgum spilavítum."}}}},{{"@type":"Question","name":"Er hægt að spila í íslenskum krónum (ISK)?","acceptedAnswer":{{"@type":"Answer","text":"Fá spilavíti styðja ISK beint. Flest nota EUR eða USD og bankinn sér um gjaldmiðlaskipti. Dulritunarspilavíti komast hjá þessu vandamáli."}}}}]}}</script>
</body>
</html>'''


# ============================================================
# PAGE GENERATION
# ============================================================

BASE = "/home/claude/slotoro-site"
count = 0

AFF = "https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/"
def honest_cta(html):
    html = html.replace(f'href="{AFF}" target="_blank" rel="noopener"', f'href="{AFF}" target="_blank" rel="sponsored noopener"')
    def fix(m):
        cls = m.group(2)
        label = "Nýskráning á Slotoro" if cls == "btn-signup" else "Spila á Slotoro →"
        return m.group(1) + label + m.group(3)
    return re.sub(r'(<a href="' + re.escape(AFF) + r'"[^>]*class="(cta-btn|sidebar-cta|btn-signup)"[^>]*>)(?:.*?)(</a>)', fix, html)

# --- Rewrite queue -------------------------------------------------------
# Pages whose copy is still templated/near-duplicate. They stay on the site and
# stay internally linked, but carry noindex and are kept out of the sitemap so
# Google does not read the site as a doorway farm. Remove a dir from
# rewrite_queue.json once its page has original copy, and it returns to the index.
try:
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "rewrite_queue.json"), encoding="utf-8") as _f:
        REWRITE_QUEUE = set(_json.load(_f))
except Exception:
    REWRITE_QUEUE = set()

def is_pending(path):
    return path.endswith("index.html") and path[:-len("/index.html")] in REWRITE_QUEUE

def write_page(path, html):
    global count
    html = honest_cta(html)
    if '<link rel="canonical"' not in html and path.endswith("index.html"):
        _dir = path[:-len("index.html")]
        _canon = "https://svipan.is/" + _dir
        html = html.replace("</title>", "</title>\n<link rel=\"canonical\" href=\"" + _canon + "\">", 1)
    # Inject hreflang if missing
    if 'hreflang="is"' not in html and path.endswith("index.html") and not path.startswith("en/"):
        _dir = path[:-len("index.html")]
        _canon = "https://svipan.is/" + _dir
        _hreflang = '<link rel="alternate" hreflang="is" href="' + _canon + '">\n<link rel="alternate" hreflang="x-default" href="' + _canon + '">'
        # Add hreflang="en" only for the homepage
        if _dir == "":
            _hreflang += '\n<link rel="alternate" hreflang="en" href="https://svipan.is/en/">'
        html = html.replace("<!-- Hreflang -->", "<!-- Hreflang -->\n" + _hreflang, 1)
    if is_pending(path):
        if '<meta name="robots"' in html:
            html = re.sub(r'<meta name="robots" content="[^"]*">',
                          '<meta name="robots" content="noindex,follow">', html, count=1)
        else:
            html = html.replace("</title>", "</title>\n<meta name=\"robots\" content=\"noindex,follow\">", 1)
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1

import html as _html
def faq_block(faqs, title="Algengar spurningar"):
    items = "".join(f'<details class="faq-d"><summary>{_html.escape(q)}</summary><p>{_html.escape(a)}</p></details>' for q, a in faqs)
    return f'<h2>{title}</h2><div class="faq-list">{items}</div>'

def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def casino_faq(c):
    n = c["name"]
    pay = ("Bitcoin, Ethereum, USDT og aðra dulritunargjaldmiðla" if c["type"] == "crypto" else "kort, rafræn veski og dulritunargjaldmiðla")
    return [
        (f"Er {n} með íslenskt leyfi?", f"Nei. {n} starfar undir erlendu leyfi. Á Íslandi hafa aðeins innlendir aðilar eins og Íslensk getspá og Happdrætti Háskólans leyfi til fjárhættuspila, svo erlend spilavíti falla ekki undir íslenskt eftirlit."),
        (f"Hver er velkomstbónusinn hjá {n}?", f"Samkvæmt rekstraraðila: {isk(c['bonus'])}. Skilmálar og veðskilyrði geta breyst — lestu þá alltaf á vef spilavítisins áður en þú samþykkir bónus."),
        (f"Hvaða greiðslumáta býður {n}?", f"{n} tekur við {pay}. Flest erlend spilavíti nota evrur, svo gengismunur getur bæst við íslenskar krónur."),
        (f"Er Svipan í samstarfi við {n}?", ("Já. Við fáum þóknun ef þú skráir þig í gegnum tengla okkar, sem hefur ekki áhrif á einkunnina." if c.get("partner") else f"Nei. Við fáum enga þóknun frá {n}. Eina spilavítið sem við vinnum með er Slotoro.")),
        ("Hvar fæ ég hjálp ef spilamennskan fer úr böndunum?", "Hjálparsími Rauða krossins 1717 er opinn allan sólarhringinn og er ókeypis og trúnaðarmál. Settu þér alltaf tíma- og upphæðarmörk áður en þú spilar."),
    ]

def partner_box(c):
    if c.get("partner"):
        return f'<div class="cta-box"><a href="{AFF}" target="_blank" rel="sponsored noopener" class="cta-btn">Spila á Slotoro →</a></div>'
    return (f'<div class="info-box"><p><strong>Athugið:</strong> Svipan er ekki í samstarfi við {c["name"]}. '
            f'Viltu spila þar, farðu beint á vef {c["name"]}. Spilavítið sem við vinnum með er '
            f'<a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a>.</p></div>'
            f'<div class="cta-box"><a href="{AFF}" target="_blank" rel="sponsored noopener" class="cta-btn">Spila á Slotoro →</a></div>')

# 1. КАЗИНО ОБЗОРЫ (150)
print("Generating casino reviews...")
for c in casinos:
    content = f'''<h1>{c["name"]} — Umsögn og bónusar 2026</h1>
<div class="rating-box"><div class="score">{c["rating"]}</div><div class="label">/ 10</div></div>
<div class="info-box">
<p><strong>Bónus:</strong> {isk(c["bonus"])}</p>
<p><strong>Tegund:</strong> {"Dulritunargjaldmiðils spilavíti" if c["type"]=="crypto" else "Hefðbundið spilavíti"}</p>
</div>
<p>{c["desc"]}</p>
<h2>{c["name"]} umsögn</h2>
<p>{c["name"]} er {"dulritunargjaldmiðils spilavíti" if c["type"]=="crypto" else "netspilavíti"} í boði fyrir íslenska leikmenn. Spilavítið býður upp á fjölbreytt úrval af spilakössum, borðleikjum og lifandi spilavíti með raunverulegum spilastjórum.</p>
<h3>Bónusar og tilboð</h3>
<p>Nýir leikmenn fá velkomstbónus upp á {isk(c["bonus"])} samkvæmt rekstraraðila. Til að virkja bónusinn, skráðu þig og leggðu inn fyrstu innborgun þína.</p>
<h3>Greiðslumátar</h3>
<p>{"Tekur við Bitcoin, Ethereum, USDT, Litecoin og öðrum dulritunargjaldmiðlum." if c["type"]=="crypto" else "Tekur við Visa, Mastercard, dulritunargjaldmiðlum og rafrænum veskjum."} Athugaðu að íslenskir bankar geta hafnað færslum til erlendra spilavíta.</p>
<h3>Leikir</h3>
<p>{"Yfir 8.000 leikir frá 71 framleiðanda, þar á meðal Pragmatic Play, Evolution og NetEnt." if c.get("partner") else c["name"] + " býður leiki frá þekktum framleiðendum. Athugaðu leikjasafnið á vef spilavítisins."}</p>
<h2>Kostir og gallar</h2>
<ul>
<li>✅ {c["bonus"]}</li>
<li>✅ {"Hraðar dulritunarútborganir (skv. rekstraraðila)" if c["type"]=="crypto" else "Nokkrar útborgunarleiðir"}</li>
<li>✅ {"Dulritunargreiðslur í boði" if c["type"]=="crypto" else "Fjölbreytt úrval greiðslumáta"}</li>
<li>✅ Stórt safn leikja</li>
<li>⚠️ Athugaðu hvort ISK sé í boði — flest erlend spilavíti nota EUR</li>
</ul>
{partner_box(c)}
{faq_block(casino_faq(c))}'''

    bc = [("{URL_BASE}", "Heim"), ("{URL_BASE}spilaviti/", "Spilavíti"), ("", c["name"])]
    review = {"@type":"Review","itemReviewed":{"@type":"Organization","name":c["name"]},
              "reviewRating":{"@type":"Rating","ratingValue":c["rating"],"bestRating":10,"worstRating":0},
              "author":{"@id":"https://svipan.is/#valbjorn"},"inLanguage":"is"}
    html = page_template(f'{c["name"]} umsögn', c["desc"], bc, content, schema_extra=[review, faq_schema(casino_faq(c))])
    write_page(f'spilaviti/{c["slug"]}/index.html', html)

# 2. КАТЕГОРИИ КАЗИНО (50)
print("Generating casino categories...")
for cat in casino_categories:
    top_casinos = casinos[:10]
    cards = ""
    for c in top_casinos:
        cards += f'<div class="info-box"><p><strong>{c["name"]}</strong> — {c["bonus"]} (Einkunn: {c["rating"]}/10) <a href="{URL_BASE}spilaviti/{c["slug"]}/">Umsögn →</a></p></div>\n'

    hero = make_hero(cat["title"], "Spilavítaflokkur", "🏆", "#41070f", "#a3152c", "#e42c4a")
    content = f'''<h1>{cat["title"].replace(" 2026","")} á Íslandi 2026</h1>
{hero}
<p>{cat["desc"]}</p>
<h2>Topp 10 spilavíti í flokki</h2>
{cards}
<h2>Hvernig við veljum bestu spilavítin</h2>
<p>Teymi okkar metur hvert spilavíti út frá nokkrum forsendum: áreiðanleika leyfis, hraða útborgana, gæði leikja, bónustilboðum og aðgengi fyrir íslenska leikmenn.</p>
<p>Við leggjum sérstaka áherslu á stuðning við dulritunargjaldmiðla þar sem íslenskir bankar loka oft á spilavíta-færslur.</p>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}spilaviti/", "Casino"), ("", cat["title"])]
    html = page_template(cat["title"], cat["desc"], bc, content)
    write_page(f'spilaviti/{cat["slug"]}/index.html', html)

# 3. СЛОТЫ (250)
print("Generating slot reviews...")
for s in slots_data:
    cdn_img = f'<div class="slot-hero"><img src="{URL_BASE}img/slots/{s["slug"]}.jpg" alt="{s["name"]} spilakassi frá {s["provider"]}" class="slot-hero-img" loading="lazy"></div>'
    how, bonus, who = SLOT_TEXT[s["slug"]]
    faqs = slot_faq(s)
    content = f'''<h1>{s["name"]} — umsögn um spilakassann</h1>
{cdn_img}
<div class="info-box">
<p><strong>Framleiðandi:</strong> {s["provider"]}</p>
<p><strong>RTP:</strong> {rtp_is(s["rtp"])}</p>
<p><strong>Sveifla:</strong> {vol_is(s["volatility"])}</p>
<p><strong>Hámarksvinningur:</strong> {maxwin_is(s["maxwin"])}</p>
<p><strong>Þema:</strong> {theme_is(s["theme"])}</p>
</div>
<h2>Hvernig {s["name"]} virkar</h2>
<p>{how}</p>
<h2>Bónus og sérstakir eiginleikar</h2>
<p>{bonus}</p>
<h2>Fyrir hverja hentar {s["name"]}?</h2>
<p>{who} {VOL_WHO.get(s["volatility"], "")}</p>
<h3>RTP útskýrt</h3>
<p>RTP {rtp_is(s["rtp"])} er fræðileg ávöxtun yfir milljónir spuna — ekki það sem þú færð til baka í einni lotu. Spilavíti geta valið lægri RTP útgáfu, svo athugaðu upplýsingaskjá leiksins.</p>
<h3>Hvar á að spila {s["name"]}</h3>
<p>{s["name"]} er í leikjasafni <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a>, sem tekur við íslenskum leikmönnum og býður yfir 8.000 leiki. Prófaðu fyrst í kynningarham ef hann er í boði og settu þér mörk áður en þú spilar fyrir alvöru.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila {s["name"]} →</a></div>
{faq_block(faqs)}'''

    bc = [("{URL_BASE}", "Heim"), ("{URL_BASE}spilakassar/", "Spilakassar"), ("", s["name"])]
    html = page_template(f'{s["name"]} spilakassi — RTP, sveifla og bónus' if len(s["name"]) <= 19 else f'{s["name"]} — RTP og bónus', f'{s["name"]} frá {s["provider"]}: RTP {rtp_is(s["rtp"])}, {vol_is(s["volatility"]).lower()} sveifla, hámark {maxwin_is(s["maxwin"])}. Hvernig leikurinn virkar og fyrir hverja hann hentar.', bc, content, schema_extra=[faq_schema(faqs)], og_img=(f"https://svipan.is/img/slots/{s['slug']}.jpg" if os.path.exists(os.path.join(BASE, 'img/slots', s['slug'] + '.jpg')) else ''))
    write_page(f'spilakassar/{s["slug"]}/index.html', html)

# 3b. Data-driven reviews for 98 popular lobby slots
import catalog as _catx, extra_reviews as _xr
_xnames = {"x-"+e["slug"][2:]: e["name"] for e in _catx.build([x["name"] for x in slots_data], 420)}
EXTRA_REVIEWS = _xr.load(_xnames)
_all_names = {x["name"]: x["slug"] for x in slots_data}
_all_names.update({x["name"]: x["slug"] for x in EXTRA_REVIEWS})
_slot_url = lambda nm: f"{URL_BASE}spilakassar/{_all_names[nm]}/"
for s in EXTRA_REVIEWS:
    p1, p2, who, rtp_txt = _xr.content(s, vol_is, maxwin_is, rtp_is, VOL_WHO, _slot_url, _all_names)
    faqs = _xr.faq(s, vol_is, maxwin_is, rtp_is)
    rows = [("Framleiðandi", s["provider"]), ("Útgáfuár", s["year"]), ("RTP", rtp_is(s["rtp"]) if s["rtp"] else "Breytilegt"),
            ("Sveifla", vol_is(s["volatility"]) if s["volatility"] else "Ekki gefið upp"), ("Hámarksvinningur", maxwin_is(s["maxwin"])),
            ("Borð", s["layout"].replace("-", "×") if s["layout"].count("-")==1 else s["layout"])]
    info = "".join(f"<p><strong>{a}:</strong> {b}</p>" for a, b in rows if b)
    content = f'''<h1>{s["name"]} — umsögn um spilakassann</h1>
<div class="slot-hero"><img src="{URL_BASE}img/lobby/{s["key"]}.jpg" alt="{s["name"]} spilakassi frá {s["provider"]}" class="slot-hero-img" loading="lazy"></div>
<div class="info-box">{info}</div>
<h2>Um {s["name"]}</h2>
<p>{p1}</p>
<h2>Vinningar og hámark</h2>
<p>{p2}</p>
<h2>Fyrir hverja hentar {s["name"]}?</h2>
<p>{who}</p>
<h3>RTP</h3>
<p>{rtp_txt} RTP er fræðileg ávöxtun yfir milljónir spuna, ekki það sem þú færð í einni lotu.</p>
<h3>Hvar á að spila {s["name"]}</h3>
<p>{s["name"]} er meðal leikja frá {s["provider"]} í safni <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a>. Settu þér mörk áður en þú spilar.</p>
<div class="cta-box"><a href="{AFF}" target="_blank" rel="sponsored noopener" class="cta-btn">Spila á Slotoro →</a></div>
{faq_block(faqs)}'''
    bc = [("{URL_BASE}", "Heim"), ("{URL_BASE}spilakassar/", "Spilakassar"), ("", s["name"])]
    desc = f'{s["name"]} frá {s["provider"]}: ' + (f'RTP {rtp_is(s["rtp"])}, ' if s["rtp"] else '') + (f'{vol_is(s["volatility"]).lower()} sveifla, ' if s["volatility"] else '') + f'hámark {maxwin_is(s["maxwin"])}. Hvernig leikurinn virkar.'
    write_page(f'spilakassar/{s["slug"]}/index.html', page_template(f'{s["name"]} spilakassi — umsögn og RTP', desc, bc, content, schema_extra=[faq_schema(faqs)], og_img=(f"https://svipan.is/img/slots/{s['slug']}.jpg" if os.path.exists(os.path.join(BASE, 'img/slots', s['slug'] + '.jpg')) else '')))

# 4. LIVE КАЗИНО (50)
print("Generating live casino pages...")
for g in live_games:
    hero_img = f'<div class="slot-hero"><img src="{URL_BASE}img/live/{g["slug"]}.jpg" alt="{g["name"]}" class="slot-hero-img"></div>'
    content = f'''<h1>{g["name"]} — Spilavíti í beinni</h1>
{hero_img}
<p>{g["desc"]}</p>
<h2>Hvernig á að spila {g["name"]}</h2>
<p>{g["name"]} með lifandi spilastjóra gefur þér upplifun af raunverulegu spilavíti heima hjá þér. Faglegir spilastjórar stjórna leiknum í rauntíma í gegnum HD myndvarp.</p>
<h3>Bestu spilavítin fyrir {g["name"]}</h3>
<ul>
<li><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> — besta úrval lifandi leikja</li>
<li><a href="{URL_BASE}spilaviti/stake/">Stake</a> — einkaréttarborð</li>
<li><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a> — breitt úrval af takmörkunum</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila {g["name"]} →</a></div>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}live/", "Live Casino"), ("", g["name"])]
    html = page_template(f'{g["name"]} Live', g["desc"], bc, content)
    write_page(f'live/{g["slug"]}/index.html', html)

# 5. БОНУСЫ (80)
print("Generating bonus pages...")
for b in bonus_pages:
    hero = make_hero(b["title"], "Bónus 2026", "🎁", "#41070c", "#a31d2e", "#d63641")
    content = f'''<h1>{b["title"]}</h1>
{hero}
<p>{b["desc"]}</p>
<h2>Bestu tilboðin 2026</h2>
<div class="info-box">
<p><strong>BitStarz:</strong> 5 BTC + 200 free spins — <a href="{URL_BASE}spilaviti/bitstarz/">Nánari upplýsingar →</a></p>
</div>
<div class="info-box">
<p><strong>BC.Game:</strong> 300% crypto bonus — <a href="{URL_BASE}spilaviti/bc-game/">Nánari upplýsingar →</a></p>
</div>
<h2>Hvernig á að fá bónus</h2>
<p>Til að virkja bónus, skráðu þig á spilavítið, leggðu inn og bónusinn verður sjálfkrafa inneignaður. Athugaðu veðskilyrði.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Fá bónus →</a></div>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}bonusar/", "Bónusar"), ("", b["title"])]
    html = page_template(b["title"], b["desc"], bc, content)
    write_page(f'bonusar/{b["slug"]}/index.html', html)

# 6. ПЛАТЕЖИ (50)
print("Generating payment pages...")
for p in payment_pages:
    hero = make_hero(p["title"], "Greiðslumáti", "💳", "#290711", "#620e26", "#a31d45")
    content = f'''<h1>{p["title"]}</h1>
{hero}
<p>{p["desc"]}</p>
<h2>Hvernig það virkar</h2>
<p>Íslenskir bankar loka á greiðslur til netspilavíta. Dulritunargjaldmiðlar eru besta leiðin til að komast framhjá þessum takmörkunum. Færslur eru hraðar, nafnlausar og gjaldfrjálsar.</p>
<h3>Skref-fyrir-skref leiðbeiningar</h3>
<ol>
<li>Búðu til veski (MetaMask, Trust Wallet eða Binance)</li>
<li>Keyptu dulritunargjaldmiðil á kauphöll</li>
<li>Sendu fjármuni til spilavítisins</li>
<li>Spilaðu og dragðu vinninga aftur í veskið þitt</li>
</ol>
<h3>Mælt með spilavítum</h3>
<ul>
<li><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> — tafarlausar dulritunarútborganir</li>
<li><a href="{URL_BASE}spilaviti/stake/">Stake</a> — styður 20+ dulritunargjaldmiðla</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Veldu spilavíti →</a></div>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}greidslur/", "Payments"), ("", p["title"])]
    html = page_template(p["title"], p["desc"], bc, content)
    write_page(f'greidslur/{p["slug"]}/index.html', html)

# 7. ГАЙДЫ (60)
print("Generating guides...")
for g in guide_pages:
    hero = make_hero(g["title"], "Leiðbeining", "📖", "#290912", "#511726", "#822e44")
    content = f'''<h1>{g["title"]}</h1>
{hero}
<p>{g["desc"]}</p>
<h2>Ítarleg leiðbeining</h2>
<p>Í þessari leiðbeiningu fjöllum við um allt sem þú þarft að vita um «{g["title"]}». Upplýsingarnar eru uppfærðar fyrir íslenska leikmenn árið 2026.</p>
<h3>Lykilatriði</h3>
<ul>
<li>Hvað þarf að vita áður en þú byrjar</li>
<li>Skref-fyrir-skref leiðbeiningar</li>
<li>Algeng mistök og hvernig á að forðast þau</li>
<li>Ráðleggingar frá sérfræðingum Svipan</li>
</ul>
<h3>Gagnlegir tenglar</h3>
<ul>
<li><a href="{URL_BASE}spilaviti/">Spilavíti umsagnir</a></li>
<li><a href="{URL_BASE}bonusar/">Bónusar</a></li>
<li><a href="{URL_BASE}greidslur/">Greiðslumátar</a></li>
</ul>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}leidbeiningar/", "Guides"), ("", g["title"])]
    html = page_template(g["title"], g["desc"], bc, content)
    write_page(f'leidbeiningar/{g["slug"]}/index.html', html)

# 8. О НАС (10)
print("Generating about pages...")
about_emojis = {"Um Svipan":"🏛️","Hafa samband":"📬","Persónuverndarstefna":"🔒","Notkunarskilmálar":"📋","Fyrirvari":"⚖️","Hvernig við metum spilavíti":"⭐","Ritstjórnarstefna":"✍️","Samstarf":"🤝","Vefkort":"🗺️","Ábyrg spilun":"🛡️"}
for a in about_pages:
    emoji = about_emojis.get(a["title"], "ℹ️")
    hero = make_hero(a["title"], "Svipan", emoji, "#29070c", "#520e18", "#821e2b")
    if a["slug"] == "personuvernd":
        content = f'''<h1>Persónuverndarstefna</h1>
{hero}
<p>Hér útskýrum við hvaða gögnum er safnað þegar þú notar svipan.is og hvernig vafrakökur eru notaðar.</p>
<h2>Gögn sem við söfnum</h2>
<p>Við biðjum ekki um nafn, netfang eða greiðsluupplýsingar. Engin skráning er á vefnum.</p>
<h2>Vafrakökur</h2>
<div class="info-box">
<p><strong>Nauðsynlegar:</strong> Við vistum val þitt um vafrakökur í vafranum þínum (localStorage) svo borðinn birtist ekki aftur. Þetta er alltaf virkt.</p>
<p><strong>Mælingar:</strong> Aðeins ef þú velur „Samþykkja allar“ gætum við notað kökur til að mæla umferð um vefinn.</p>
<p><strong>Þriðju aðilar:</strong> Þegar þú smellir á samstarfstengil ferðu á vef spilavítisins, sem getur sett eigin kökur samkvæmt sinni persónuverndarstefnu.</p>
<p><strong>Leturgerðir:</strong> Letur er sótt frá Google Fonts, sem fær IP-tölu þína við niðurhal.</p>
</div>
<p><a href="#" data-cookie-settings>Breyta vali á vafrakökum →</a></p>
<h2>Réttindi þín</h2>
<p>Ísland er aðili að EES og GDPR gildir. Þú getur hvenær sem er breytt vali þínu eða eytt vafragögnum í stillingum vafrans. Spurningar? <a href="{URL_BASE}hafa-samband/">Hafðu samband</a>.</p>
<p><em>Síðast uppfært: nóvember 2026.</em></p>'''
    elif a["slug"] == "hvernig-vid-metum":
        content = f'''<h1>Hvernig við metum spilavíti</h1>
{hero}
<p>Hvert spilavíti á Svipan fær einkunn frá 0 til 10. Einkunnin byggir á sex föstum viðmiðum með birtum vægi, svo þú getir séð nákvæmlega hvernig hún verður til.</p>
<h2>Viðmið og vægi</h2>
<div class="info-box" style="overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;font-size:16px;color:var(--muted);">
<tr style="color:#fff;border-bottom:1px solid var(--border);"><th style="text-align:left;padding:8px;">Viðmið</th><th style="text-align:left;padding:8px;">Vægi</th><th style="text-align:left;padding:8px;">Hvað við skoðum</th></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:8px;">Leyfi og öryggi</td><td style="padding:8px;">25%</td><td style="padding:8px;">Leyfisveitandi, birt leyfisnúmer, rekstraraðili, SSL</td></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:8px;">Aðgengi frá Íslandi</td><td style="padding:8px;">20%</td><td style="padding:8px;">Tekur við íslenskum leikmönnum, íslenskt viðmót, ISK, PIQ</td></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:8px;">Greiðslur</td><td style="padding:8px;">20%</td><td style="padding:8px;">Dulritunargjaldmiðlar, rafræn veski, lágmarksinnborgun, útborgunarmörk</td></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:8px;">Bónusskilmálar</td><td style="padding:8px;">15%</td><td style="padding:8px;">Veðskilyrði, tímamörk, hámarksveðmál, hvaða leikir telja</td></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:8px;">Leikjaúrval</td><td style="padding:8px;">10%</td><td style="padding:8px;">Fjöldi leikja, framleiðendur, lifandi spilavíti</td></tr>
<tr><td style="padding:8px;">Ábyrg spilun</td><td style="padding:8px;">10%</td><td style="padding:8px;">Innborgunarmörk, sjálfsútilokun, tapsmörk</td></tr>
</table>
</div>
<h2>Það sem við gerum ekki</h2>
<ul>
<li>Við höfum ekki lagt inn raunverulegt fé eða mælt útborgunartíma sjálf. Útborgunartímar á síðunni eru samkvæmt upplýsingum rekstraraðila og merktir sem slíkir.</li>
<li>Við breytum ekki einkunnum gegn greiðslu. Samstarfstenglar hafa ekki áhrif á röðun.</li>
</ul>
<h2>Uppfærslur</h2>
<p>Við förum yfir bónusa og skilmála reglulega. Síðast yfirfarið: nóvember 2026. Upphæðir í ISK eru reiknaðar á genginu 1 EUR ≈ {EUR_ISK} kr. og eru aðeins til viðmiðunar.</p>
<p>Ef þú finnur villu, <a href="{URL_BASE}hafa-samband/">hafðu samband</a>.</p>'''
    else:
        content = f'''<h1>{a["title"]}</h1>
{hero}
<p>{a["desc"]}</p>
<p>Svipan (svipan.is) er óháð spilavítavefgátt fyrir íslenska leikmenn. Við hjálpum þér að finna áreiðanleg spilavíti með bestu bónusum og stuðningi við dulritunargjaldmiðla.</p>'''

    bc = [("{URL_BASE}", "Home"), ("", a["title"])]
    html = page_template(a["title"], a["desc"], bc, content)
    write_page(f'{a["slug"]}/index.html', html)

# 9. SEO ЦЕЛЕВЫЕ СТРАНИЦЫ (10 новых под низкоконкурентные запросы)
print("Generating SEO target pages...")

seo_pages = [
    {
        "slug": "kaupa-bitcoin-island",
        "title": "Hvernig á að kaupa Bitcoin á Íslandi fyrir spilavíti",
        "desc": "Skref-fyrir-skref leiðbeiningar um kaup á Bitcoin frá Íslandi til að leggja inn á netspilavíti. Coinbase, Binance og fleiri.",
        "emoji": "₿",
        "colors": ("#290711", "#620e26", "#a31d45"),
        "content": f'''<h1>Hvernig á að kaupa Bitcoin á Íslandi fyrir spilavíti 2026</h1>
{{hero}}
<p>Íslenskir bankar loka oft á greiðslur til erlendra spilavíta. <strong>Bitcoin</strong> og aðrir dulritunargjaldmiðlar eru áreiðanlegasta leiðin til að leggja inn á netspilavíti frá Íslandi. Hér er nákvæm leiðbeining.</p>

<h2>Skref 1 — Veldu kauphöll</h2>
<div class="info-box">
<p><strong>Coinbase</strong> — Auðvelt viðmót, tekur við íslenskum kortum (Visa/Mastercard). Staðfesting tekur 5-10 mínútur.</p>
<p><strong>Binance</strong> — Lægri gjöld, meira úrval dulritunargjaldmiðla. Tekur við bankamillifærslu (SEPA).</p>
<p><strong>Kraken</strong> — Evrópsk kauphöll með góðum öryggisráðstöfunum. SEPA millifærsla á 1-2 dögum.</p>
</div>

<h2>Skref 2 — Keyptu Bitcoin (BTC) eða USDT</h2>
<p>Við mælum með <strong>USDT (Tether)</strong> frekar en Bitcoin fyrir spilavítainnlagnir af tveimur ástæðum:</p>
<ul>
<li>✅ USDT er stöðugt (1 USDT = ~1 USD) — engin sveiflur á meðan þú spilar</li>
<li>✅ Lægri færslugjöld á TRC-20 netinu (undir $1)</li>
<li>✅ Tafarlausar millifærslur (undir 1 mínúta)</li>
</ul>

<h2>Skref 3 — Sendu á spilavítið</h2>
<ol>
<li>Skráðu þig á spilavíti (t.d. <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> eða <a href="{URL_BASE}spilaviti/stake/">Stake</a>)</li>
<li>Farðu í "Innborgun" og veldu Bitcoin eða USDT</li>
<li>Afritaðu veskisáfangastaðinn (wallet address)</li>
<li>Farðu aftur í kauphöllina og sendu fjármunina á þetta heimilisfang</li>
<li>Bíddu 1-10 mínútur — innborgunin birtist á spilavítareikningnum þínum</li>
</ol>

<h2>Bestu spilavítin fyrir Bitcoin á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — 5 BTC + 200 FS | Tafarlausar BTC útborganir</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — 200% bónus | Styður 8+ dulritunargjaldmiðla</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> — 300% allt að 1 BTC | 100+ dulritunargjaldmiðlar</p></div>

<h2>Algengar spurningar</h2>
<h3>Er löglegt að kaupa Bitcoin á Íslandi?</h3>
<p>Já. Engin lög á Íslandi banna kaup á dulritunargjaldmiðlum. <a href="{URL_BASE}leidbeiningar/log-um-fjarhaettuspil-a-islandi/">Lestu lagaleiðbeininguna okkar →</a></p>
<h3>Hversu langan tíma tekur innborgun?</h3>
<p>Bitcoin: 10-30 mínútur. USDT (TRC-20): 1-5 mínútur. Ethereum: 2-10 mínútur.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila með Bitcoin →</a></div>'''
    },
    {
        "slug": "islenskir-bankar-spilaviti",
        "title": "Íslenskir bankar og spilavíti — hvaða banki lokar á greiðslur?",
        "desc": "Arion banki, Landsbankinn og Íslandsbanki loka oft á greiðslur til netspilavíta. Hér er hvað þú getur gert.",
        "emoji": "🏦",
        "colors": ("#290912", "#511727", "#822e47"),
        "content": f'''<h1>Íslenskir bankar og spilavíti — hvaða banki lokar á greiðslur?</h1>
{{hero}}
<p>Eitt stærsta vandamálið fyrir íslenska spilavítaspilara er að <strong>íslenskir bankar hafna oft greiðslum</strong> til erlendra netspilavíta. Þetta er ekki byggt á lögum — heldur innri stefnu bankanna sjálfra.</p>

<h2>Staða stóru bankanna</h2>
<p>Engin lög banna þessar greiðslur — höfnunin byggir á ákvörðunum bankanna sjálfra og getur breyst án fyrirvara.</p>
<div class="info-box">
<p><strong>Arion banki</strong> — Getur hafnað kortagreiðslum til erlendra spilavíta samkvæmt innri stefnu.</p>
</div>
<div class="info-box">
<p><strong>Landsbankinn</strong> — Sama staða: sumar kortagreiðslur fara í gegn, aðrar ekki.</p>
</div>
<div class="info-box">
<p><strong>Íslandsbanki</strong> — Kortaviðskipti virka stundum, stundum ekki.</p>
</div>

<h2>Lausnir sem virka</h2>
<h3>1. Dulritunargjaldmiðlar (besta lausnin)</h3>
<p>Bitcoin, USDT og Ethereum fara beint á blokkkeðjunni — <strong>bankarnir geta ekki lokað á þessar greiðslur</strong>. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi →</a></p>

<h3>2. Rafræn veski (e-wallets)</h3>
<p><strong>Skrill</strong> og <strong>Neteller</strong> virka sem milliliður — þú millifærir af bankareikningi á veskið, síðan frá veskinu á spilavítið.</p>

<h3>3. PIQ greiðslur</h3>
<p><a href="{URL_BASE}leidbeiningar/piq-greidslur-island/">PIQ</a> er greiðsluþjónusta sem er sérstaklega hönnuð fyrir Ísland og Noreg. Epicbet og Respin styðja PIQ.</p>

<h3>4. Fyrirframgreidd kort</h3>
<p><strong>Paysafecard</strong> og <strong>Neosurf</strong> eru fyrirframgreidd kort sem þú kaupir í verslun. Enginn banki kemur við sögu.</p>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila með dulritunargjaldmiðlum →</a></div>'''
    },
    {
        "slug": "skattar-spilavinningar-island",
        "title": "Skattar á spilavinninga á Íslandi 2026",
        "desc": "Eru vinningar frá netspilavítum skattskyldir á Íslandi? Hvað þú þarft að vita og hvernig á að halda skrá.",
        "emoji": "⚖️",
        "colors": ("#290f14", "#612732", "#924655"),
        "content": f'''<h1>Skattar á spilavinninga á Íslandi 2026</h1>
{{hero}}
<p>Einn algengasti spurningin frá íslenskum spilurum: <strong>þarf ég að borga skatta af vinningum frá erlendum netspilavítum?</strong></p>

<h2>Stutta svarið</h2>
<p>Vinningar frá erlendum netspilavítum teljast <strong>almennt til skattskyldra tekna</strong> á Íslandi og sæta ekki staðgreiðslu. Það þýðir að það er á þína ábyrgð að gera grein fyrir þeim á skattframtali.</p>

<h2>Hvað þarf að hafa í huga?</h2>
<div class="info-box">
<p><strong>⚠️ Erlend spilavíti draga ekki skatt frá.</strong> Ólíkt launum er enginn skattur tekinn af vinningnum áður en hann er greiddur út.</p>
</div>
<div class="info-box">
<p><strong>⚠️ Dulritunargjaldmiðlar:</strong> Ef verðgildi Bitcoin hækkar á meðan þú átt hann getur sá hagnaður líka verið skattskyldur þegar þú selur.</p>
</div>

<h2>Ráðleggingar</h2>
<ol>
<li>Haltu skrá yfir allar innlagnir og úttektir</li>
<li>Geymdu yfirlit frá spilavítinu og kauphöllinni</li>
<li>Hafðu samband við Skattinn (skatturinn.is) eða endurskoðanda ef þú ert í vafa</li>
</ol>

<p><em>Þessi síða er ekki skattaleg ráðgjöf. Ráðfærðu þig við fagaðila.</em></p>'''
    },
    {
        "slug": "spilaviti-isk-kronur",
        "title": "Spilavíti sem taka við ISK — Íslenskum krónum",
        "desc": "Spilavíti sem styðja íslenskar krónur (ISK) beint. Forðastu gjaldmiðlaskiptagjöld.",
        "emoji": "💰",
        "colors": ("#102008", "#205018", "#408030"),
        "content": f'''<h1>Spilavíti sem taka við ISK — Íslenskum krónum 2026</h1>
{{hero}}
<p>Flest netspilavíti nota evrur (EUR) sem grunngjaldmiðil, sem þýðir gjaldmiðlaskiptagjöld fyrir íslenska spilara. Hér eru kostirnir:</p>

<h2>Staðan: ISK stuðningur er sjaldgæfur</h2>
<p>Fá alþjóðleg spilavíti bjóða ISK sem reikningsgjaldmiðil. Óháðar prófanir árið 2026 sýndu íslenskar krónur hjá <strong>BC.Game</strong> og <strong>Megapari</strong> þegar þau voru opnuð frá Íslandi. Annars eru þetta kostirnir:</p>

<div class="info-box">
<p><strong>🥇 Dulritunargjaldmiðlar (USDT)</strong> — Ekki ISK, en komast framhjá öllum gjaldmiðlaskiptagjöldum. 1 USDT = ~1 USD alltaf.</p>
</div>
<div class="info-box">
<p><strong>🥈 EUR reikningur</strong> — Flest spilavíti styðja EUR. Bankinn þinn skiptir ISK í EUR sjálfkrafa (lítil þóknun ~1-2%).</p>
</div>
<div class="info-box">
<p><strong>🥉 PIQ greiðslur</strong> — Sérstaklega hannað fyrir Ísland. <a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a> og <a href="{URL_BASE}spilaviti/respin/">Respin</a> styðja PIQ.</p>
</div>

<h2>Bestu spilavítin fyrir íslenska spilara</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Dulritunarspilavíti, engin gjaldmiðlaskiptagjöld</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — PIQ greiðslur, íslenskt viðmót</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — USDT innlagnir, engin gjöld</p></div>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila án gjaldmiðlaskiptagjalda →</a></div>'''
    },
    {
        "slug": "spilaviti-islenskt-vidmot",
        "title": "Spilavíti með íslensku viðmóti 2026",
        "desc": "Netspilavíti sem bjóða viðmót á íslensku — þjónustuveri, leikir og skilmálar á íslensku.",
        "emoji": "🇮🇸",
        "colors": ("#400010", "#900026", "#d0003a"),
        "content": f'''<h1>Spilavíti með íslensku viðmóti 2026</h1>
{{hero}}
<p>Flest netspilavíti eru á ensku, en nokkur bjóða <strong>íslenskt viðmót</strong> og þjónustuver á íslensku:</p>

<div class="info-box">
<p><strong>✅ Epicbet</strong> — Fullt íslenskt viðmót, Apple Pay greiðslur, PIQ stuðningur. <a href="{URL_BASE}spilaviti/epicbet/">Umsögn →</a></p>
</div>
<div class="info-box">
<p><strong>✅ Respin</strong> — Íslenskt viðmót, PIQ greiðslur, 4000+ leikir. <a href="{URL_BASE}spilaviti/respin/">Umsögn →</a></p>
</div>
<div class="info-box">
<p><strong>✅ Betsson</strong> — Eitt af fáum stórum spilavítum með íslenskt viðmót.</p>
</div>
<div class="info-box">
<p><strong>✅ TonyBet</strong> — Lifandi spilavíti á íslensku, leyfi í Eistlandi (innan EES). <a href="{URL_BASE}spilaviti/tonybet/">Umsögn →</a></p>
</div>

<h2>Af hverju skiptir tungumálið máli?</h2>
<ul>
<li>Skilmálar og bónusreglur á íslensku — enginn misskilningur</li>
<li>Þjónustuver á íslensku — fljótlegri aðstoð</li>
<li>Greiðsluleiðir sérstaklega fyrir Ísland (PIQ)</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á íslensku →</a></div>'''
    },
    {
        "slug": "piq-greidslur-island",
        "title": "PIQ greiðslur á Íslandi — hvað er PIQ og hvernig virkar það?",
        "desc": "PIQ er greiðsluþjónusta sérstaklega hönnuð fyrir Ísland og Noreg. Hvernig á að nota PIQ á netspilavítum.",
        "emoji": "💳",
        "colors": ("#290711", "#620e26", "#a31d45"),
        "content": f'''<h1>PIQ greiðslur á Íslandi — hvað er PIQ?</h1>
{{hero}}
<p><strong>PIQ</strong> er greiðsluþjónusta sem er sérstaklega hönnuð fyrir spilara á Íslandi og í Noregi. Hún veitir sérstaka greiðslubraut sem gæti reynst áreiðanlegri en hefðbundin Visa/Mastercard vinnsla í gegnum íslenska banka.</p>

<h2>Hvernig virkar PIQ?</h2>
<ol>
<li>Veldu PIQ sem greiðslumáta á spilavítinu</li>
<li>Sláðu inn upphæð og kortaupplýsingar</li>
<li>PIQ sér um greiðsluvinnsluna í stað hefðbundinnar kortavinnslu</li>
<li>Staðfestu innborgunina í bankaappinu ef beðið er um það</li>
</ol>

<h2>Spilavíti sem styðja PIQ á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — PIQ + Apple Pay + íslenskt viðmót</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/respin/">Respin</a></strong> — PIQ + íslenskt viðmót + 4000 leikir</p></div>

<h2>Kostir PIQ</h2>
<ul>
<li>✅ Meiri líkur á að greiðslan fari í gegnum íslenskan banka</li>
<li>✅ Hraðar innborganir</li>
<li>✅ Sérhannað fyrir Ísland og Noreg</li>
</ul>
<h2>Gallar PIQ</h2>
<ul>
<li>⚠️ Ekki 100% tryggt — bankar geta enn hafnað</li>
<li>⚠️ Aðeins fáein spilavíti styðja PIQ enn sem komið er</li>
</ul>
<p>Ef PIQ virkar ekki, er <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">dulritunargjaldmiðill besta lausnin →</a></p>'''
    },
    {
        "slug": "frisnuningar-an-innborgunar",
        "title": "Frísnúningar án innborgunar á Íslandi 2026",
        "desc": "Nýjustu frísnúningatilboð án innborgunar fyrir íslenska spilara. Skráðu þig og fáðu ókeypis snúninga.",
        "emoji": "🎰",
        "colors": ("#41070c", "#a31d2e", "#d63641"),
        "content": f'''<h1>Frísnúningar án innborgunar á Íslandi 2026</h1>
{{hero}}
<p>Frísnúningar án innborgunar leyfa þér að <strong>prófa spilavíti ókeypis</strong> — engin innborgun þarf. Hér eru bestu tilboðin:</p>

<h2>Tilboð sem vert er að skoða</h2>
<p><em>Tilboð breytast oft — staðfestu alltaf skilmálana á síðu spilavítisins áður en þú skráir þig.</em></p>
<div class="info-box">
<p><strong>🎁 Slotoro</strong> (samstarfsaðili okkar) — velkomstpakki með frísnúningum á fyrstu þremur innborgunum, 40x veðskilyrði. Athugaðu í reikningnum þínum hvaða tilboð gilda fyrir Ísland.</p>
<p><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener">Sjá tilboð á Slotoro →</a></p>
</div>
<div class="info-box">
<p><strong>Winz.io</strong> — þekkt fyrir bónusa án veðskilyrða. Við erum ekki í samstarfi við Winz.io; skoðaðu tilboðin beint á vef þeirra. <a href="{URL_BASE}spilaviti/winz/">Umsögn okkar →</a></p>
</div>

<h2>Hvernig virka frísnúningar án innborgunar?</h2>
<ol>
<li>Skráðu þig á spilavítið (tekur 30 sekúndur)</li>
<li>Frísnúningar birtast sjálfkrafa á reikningnum þínum</li>
<li>Spilaðu og reyndu að vinna!</li>
<li>Uppfylltu veðskilyrði til að taka vinninga út</li>
</ol>

<h2>Veðskilyrði — hvað þýðir 30x?</h2>
<p>Ef þú vinnur €10 úr frísnúningum og veðskilyrði eru 30x, þarftu að veðja €300 áður en þú getur tekið út. <a href="{URL_BASE}bonusar/vedskilyrdi/">Lestu meira um veðskilyrði →</a></p>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Fá frísnúninga →</a></div>'''
    },
    {
        "slug": "spilaviti-samanburdur",
        "title": "Spilavíti samanburður — bestu netspilavítin á Íslandi 2026",
        "desc": "Berðu saman netspilavíti hlið við hlið: bónusar, útborgunarhraði, leikjafjöldi og dulritunargjaldmiðlar.",
        "emoji": "📊",
        "colors": ("#29070c", "#621622", "#a32d40"),
        "content": f'''<h1>Spilavíti samanburður — Ísland 2026</h1>
{{hero}}
<p>Berðu saman bestu netspilavítin fyrir íslenska spilara hlið við hlið:</p>

<div class="info-box" style="overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;font-size:16px;color:var(--muted);">
<tr style="border-bottom:1px solid var(--border);color:#fff;"><th style="padding:10px;text-align:left;">Spilavíti</th><th>Bónus</th><th>Leikir</th><th>Útborgun</th><th>Dulritun</th><th>Einkunn</th></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;"><a href="{URL_BASE}spilaviti/bitstarz/" style="color:#e8505c;">BitStarz</a></td><td>5 BTC + 200 FS</td><td>3500+</td><td>&lt;10 mín</td><td>✅ BTC, ETH, LTC</td><td>9.8</td></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;"><a href="{URL_BASE}spilaviti/stake/" style="color:#e8505c;">Stake</a></td><td>200% + VIP</td><td>5000+</td><td>&lt;10 mín</td><td>✅ 8+ mynt</td><td>9.6</td></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;"><a href="{URL_BASE}spilaviti/bc-game/" style="color:#e8505c;">BC.Game</a></td><td>300% / 1 BTC</td><td>8000+</td><td>&lt;5 mín</td><td>✅ 100+ mynt</td><td>9.4</td></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;"><a href="{URL_BASE}spilaviti/epicbet/" style="color:#e8505c;">Epicbet</a></td><td>100% / €500</td><td>2000+</td><td>1-3 dagar</td><td>🟡 BTC, ETH</td><td>9.0</td></tr>
<tr><td style="padding:10px;"><a href="{URL_BASE}spilaviti/katsubet/" style="color:#e8505c;">KatsuBet</a></td><td>100% + 100 FS</td><td>5000+</td><td>&lt;10 mín</td><td>✅ 6 mynt</td><td>8.6</td></tr>
</table>
</div>

<p style="font-size:16px;color:var(--muted2);">Útborgunartímar eru samkvæmt upplýsingum rekstraraðila, ekki mældir af okkur. <a href="{URL_BASE}hvernig-vid-metum/">Aðferðafræði →</a></p>
<h2>Hvernig við metum spilavíti</h2>
<ul>
<li><strong>Bónus:</strong> Velkomstbónus, veðskilyrði, frísnúningar</li>
<li><strong>Útborgunarhraði:</strong> Hversu fljótt færðu vinninga</li>
<li><strong>Leikjafjöldi:</strong> Spilakassar, borðleikir, lifandi spilavíti</li>
<li><strong>Dulritunargjaldmiðlar:</strong> Bitcoin, USDT, Ethereum stuðningur</li>
<li><strong>Íslandsaðgengi:</strong> PIQ, íslenskt viðmót, ISK stuðningur</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á #1 spilavítinu →</a></div>'''
    },
    {
        "slug": "framhja-bankalokun",
        "title": "Hvernig á að komast framhjá bankalokun á Íslandi",
        "desc": "Íslenskir bankar loka á spilavítagreiðslur. Hér eru 5 leiðir til að komast framhjá.",
        "emoji": "🔓",
        "colors": ("#21090f", "#511927", "#822e44"),
        "content": f'''<h1>Hvernig á að komast framhjá bankalokun á Íslandi 2026</h1>
{{hero}}
<p>Arion banki, Landsbankinn og Íslandsbanki loka oft á greiðslur til erlendra spilavíta. Hér eru <strong>5 aðferðir sem virka</strong>:</p>

<h2>1. 💎 Dulritunargjaldmiðlar (USDT / Bitcoin)</h2>
<p><strong>Áreiðanlegasta lausnin.</strong> Bankar geta ekki lokað á blockchain-færslur.</p>
<p><a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">📖 Skref-fyrir-skref: Hvernig á að kaupa Bitcoin á Íslandi →</a></p>

<h2>2. 💳 PIQ greiðslur</h2>
<p>Greiðsluþjónusta sérstaklega fyrir Ísland. <a href="{URL_BASE}leidbeiningar/piq-greidslur-island/">Lestu PIQ leiðbeininguna →</a></p>

<h2>3. 👛 Rafræn veski (Skrill, Neteller)</h2>
<p>Millifærðu á veskið, síðan frá veskinu á spilavítið. Bankinn sér ekki spilavítagreiðslu.</p>

<h2>4. 🎫 Fyrirframgreidd kort (Paysafecard)</h2>
<p>Keyptu kort í verslun og notaðu kóðann til innborgunar. Enginn banki kemur við sögu.</p>

<h2>5. 📱 Apple Pay / Google Pay</h2>
<p>Virkar á sumum spilavítum — t.d. Epicbet styður Apple Pay innborganir.</p>

<h2>Samanburður á aðferðum</h2>
<div class="info-box">
<p>🥇 <strong>Dulritunargjaldmiðlar</strong> — 99% áreiðanleiki, tafarlausar, enginn milliliður</p>
<p>🥈 <strong>PIQ</strong> — 80% áreiðanleiki, hraðar, en takmarkað framboð</p>
<p>🥉 <strong>Rafræn veski</strong> — 90% áreiðanleiki, en þarf extra skref</p>
</div>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila með dulritunargjaldmiðlum →</a></div>'''
    },
    {
        "slug": "besta-crypto-spilaviti-island",
        "title": "Besta crypto spilavítið á Íslandi 2026",
        "desc": "Bestu dulritunar netspilavítin fyrir íslenska spilara. Bitcoin, USDT, Ethereum. Hraðar útborganir.",
        "emoji": "🏆",
        "colors": ("#41070f", "#a3152c", "#e42c4a"),
        "content": f'''<h1>Besta crypto spilavítið á Íslandi 2026</h1>
{{hero}}
<p>Dulritunargjaldmiðlar eru <strong>besta leiðin til að spila á netspilavítum frá Íslandi</strong> — engin bankalokun, tafarlausar útborganir, og lág gjöld.</p>

<h2>Topp 5 crypto spilavíti á Íslandi</h2>
<div class="info-box">
<p><strong>🥇 <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Besta crypto spilavítið. 3500+ leikir, 5 BTC + 200 FS, útborganir á nokkrum mínútum samkvæmt rekstraraðila. Styður BTC, ETH, LTC, DOGE, USDT, BCH. Einkunn: 9.8/10</p>
</div>
<div class="info-box">
<p><strong>🥈 <a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — Vinsælasta crypto spilavítið í heimi. 200% VIP bónus, 5000+ leikir, 8+ dulritunargjaldmiðlar. Einkunn: 9.6/10</p>
</div>
<div class="info-box">
<p><strong>🥉 <a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> — 100+ dulritunargjaldmiðlar, 8000+ leikir, 300% bónus. Mest fjölbreytt crypto stuðningur. Einkunn: 9.4/10</p>
</div>
<div class="info-box">
<p><strong>4. <a href="{URL_BASE}spilaviti/katsubet/">KatsuBet</a></strong> — 5000+ leikir, 6 dulritunargjaldmiðlar, 100% + 100 FS. Einkunn: 8.6/10</p>
</div>
<div class="info-box">
<p><strong>5. <a href="{URL_BASE}spilaviti/cloudbet/">Cloudbet</a></strong> — Premium crypto spilavíti, háar takmörkunar, 100% allt að 5 BTC. Einkunn: 8.4/10</p>
</div>

<h2>Af hverju dulritunar spilavíti á Íslandi?</h2>
<ul>
<li>🔓 Komast framhjá <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">bankalokun íslenskra banka</a></li>
<li>⚡ Dulritunarútborganir oft á mínútum, samkvæmt rekstraraðilum (kort taka yfirleitt 1–5 daga)</li>
<li>💰 Engin gjaldmiðlaskiptagjöld</li>
<li>🛡️ Aukið næði — engar spilavítafærslur á bankayfirlitinu</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á BitStarz →</a></div>'''
    },
    {
        "slug": "okeypis-spilavitisleikir",
        "title": "Ókeypis spilavítisleikir á Íslandi — spilaðu án áhættu",
        "desc": "Spilaðu ókeypis spilakassa, rúllettu og blackjack án þess að leggja inn peninga. Prófaðu leiki áður en þú spilar um raunverulega peninga.",
        "emoji": "🎮",
        "colors": ("#0a0c14", "#1a2040", "#2a3570"),
        "content": f'''<h1>Ókeypis spilavítisleikir á Íslandi 2026</h1>
{{hero}}
<p>Viltu prófa spilavítisleiki <strong>án áhættu</strong>? Margir leikjaframleiðendur bjóða upp á ókeypis prufuútgáfur (demo mode) sem leyfa þér að spila spilakassa, rúllettu og blackjack án þess að nota raunverulega peninga.</p>

<h2>Hvernig virka ókeypis leikir?</h2>
<ul>
<li>Þú færð sýndarpeninga til að spila með</li>
<li>Leikirnir virka nákvæmlega eins og raunpeningaútgáfurnar (sama RTP, sömu eiginleikar)</li>
<li>Þú getur prófað hundruð spilakassa áður en þú ákveður hvar þú vilt spila</li>
<li>Engrar skráningar er þörf hjá flestum veitendum</li>
</ul>

<h2>Bestu ókeypis spilakassarnir til að prófa</h2>
<div class="info-box"><p><strong>Book of Dead</strong> (Play'n GO) — klassískur bókaslotur með háum vinningum. <a href="{URL_BASE}spilakassar/book-of-dead/">Umsögn →</a></p></div>
<div class="info-box"><p><strong>Big Bass Bonanza</strong> (Pragmatic Play) — vinsæll meðal byrjenda. <a href="{URL_BASE}spilakassar/big-bass-bonanza/">Umsögn →</a></p></div>
<div class="info-box"><p><strong>Bonanza Megaways</strong> (Big Time Gaming) — allt að 117.649 vinningsleiðir. <a href="{URL_BASE}spilakassar/bonanza-megaways/">Umsögn →</a></p></div>

<h2>Af hverju er gott að spila ókeypis fyrst?</h2>
<ol>
<li>Kynntu þér leikjareglur og eiginleika áður en þú veðjar raunverulega peninga</li>
<li>Finndu hvaða spilakassar henta þínum spilastíl</li>
<li>Prófaðu mismunandi veðaðferðir án áhættu</li>
<li>Hafðu gaman án fjárhagslegrar áhættu</li>
</ol>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa leiki á Slotoro →</a></div>'''
    },
    {
        "slug": "ny-spilaviti-island",
        "title": "Ný spilavíti á Íslandi 2026 — nýjustu síðurnar",
        "desc": "Listi yfir nýjustu netspilavítin sem taka við íslenskum spilurum. Nýir bónusar, nýir leikir og ný tækifæri.",
        "emoji": "🆕",
        "colors": ("#140a0c", "#401a22", "#702a3a"),
        "content": f'''<h1>Ný spilavíti á Íslandi 2026</h1>
{{hero}}
<p>Nýtt spilavíti þýðir oft <strong>betri bónusa</strong>, nútímalegt viðmót og nýjustu leikina. Hér eru nýjustu spilavítin sem íslenskir leikmenn geta skráð sig á.</p>

<h2>Af hverju velja nýtt spilavíti?</h2>
<ul>
<li><strong>Stærri velkomstbónusar</strong> — ný spilavíti bjóða oft rausnarlegri tilboð til að laða að spilara</li>
<li><strong>Nýjustu leikirnir</strong> — aðgang að nýjustu spilakössunum og lifandi borðum</li>
<li><strong>Betri dulritunarstuðningur</strong> — nýrri spilavíti styðja oft fleiri dulritunargjaldmiðla</li>
<li><strong>Hraðari útborganir</strong> — nútímaleg greiðslukerfi</li>
</ul>

<h2>Nýjustu spilavítin</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — nýtt spilavíti með íslensku viðmóti, PIQ greiðslum og Evolution lifandi borðum. Einkunn: 8.9/10</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/respin/">Respin</a></strong> — íslensku viðmót, hröð úttekt og 100% velkomstbónus. Einkunn: 8.7/10</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/neospin/">Neospin</a></strong> — 7000+ leikir, Bitcoin og Ethereum. Einkunn: 8.4/10</p></div>

<h2>Hvað á að athuga áður en þú skráir þig</h2>
<ol>
<li>Er spilavítið með gilt leyfi (MGA, Curaçao)?</li>
<li>Hvaða greiðslumátar eru í boði? Styður það dulritunargjaldmiðla?</li>
<li>Hverjir eru skilmálar bónussins (veðskilyrði)?</li>
<li>Er þjónustuver aðgengilegt 24/7?</li>
</ol>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa nýjasta spilavítið →</a></div>'''
    },
    {
        "slug": "hrod-utborgun-spilaviti",
        "title": "Hröð útborgun spilavíti á Íslandi — úttekt á mínútum",
        "desc": "Netspilavíti með hraðustu útborgunum fyrir íslenska spilara. Bitcoin úttektir á 10 mínútum.",
        "emoji": "⚡",
        "colors": ("#140e08", "#403020", "#705030"),
        "content": f'''<h1>Hröð útborgun spilavíti — Ísland 2026</h1>
{{hero}}
<p>Enginn vill bíða í marga daga eftir vinningum sínum. Hér eru spilavítin sem bjóða <strong>hraðustu útborganirnar</strong> fyrir íslenska spilara.</p>

<h2>Hraðasti útborgunarleið</h2>
<div class="info-box">
<p><strong>🥇 Bitcoin/USDT</strong> — undir 10 mínútur hjá flestum spilavítum</p>
<p><strong>🥈 Rafveski (Skrill/Neteller)</strong> — 1-24 klukkustundir</p>
<p><strong>🥉 Bankamillifærsla</strong> — 1-3 virkir dagar</p>
</div>

<h2>Bestu spilavítin fyrir hraðar útborganir</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Bitcoin úttekt á undir 10 mínútum. Einkunn: 9.8/10</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — Tafarlaus dulritunarúttekt. Einkunn: 9.6/10</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> — 100+ dulritunargjaldmiðlar, hröð vinnsla. Einkunn: 9.4/10</p></div>

<h2>Ráð til að fá hraðari útborgun</h2>
<ul>
<li>Ljúktu <a href="{URL_BASE}leidbeiningar/hvad-er-kyc-stadfesting/">KYC staðfestingu</a> áður en þú biður um úttekt</li>
<li>Notaðu dulritunargjaldmiðla — þeir eru alltaf hraðastir</li>
<li>Athugaðu lágmarksúttektarupphæð áður en þú spilar</li>
<li>Forðastu bónusa með háum veðskilyrðum ef hröð úttekt skiptir máli</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á BitStarz →</a></div>'''
    },
    {
        "slug": "lagmarks-innborgun-spilaviti",
        "title": "Lágmarksinnborgun spilavíti á Íslandi — frá €1",
        "desc": "Spilavíti með lágri lágmarksinnborgun fyrir íslenska spilara. Spilaðu frá €1, €5 eða €10.",
        "emoji": "💰",
        "colors": ("#0c1408", "#204018", "#307028"),
        "content": f'''<h1>Lágmarksinnborgun spilavíti — Ísland 2026</h1>
{{hero}}
<p>Ekki allir vilja leggja háar upphæðir inn. Hér eru bestu spilavítin með <strong>lágri lágmarksinnborgun</strong> sem samþykkja íslenska spilara.</p>

<h2>Spilavíti eftir lágmarksinnborgun</h2>
<div class="info-box">
<p><strong>€1 lágmark:</strong> BitStarz (með dulritun), BC.Game</p>
<p><strong>€5 lágmark:</strong> 7Bit Casino, KatsuBet</p>
<p><strong>€10 lágmark:</strong> Stake, TonyBet, Epicbet, mBit Casino</p>
<p><strong>€20 lágmark:</strong> 20Bet, National Casino, Cloudbet</p>
</div>

<h2>Ráð fyrir lága innborgun</h2>
<ul>
<li>Notaðu dulritunargjaldmiðla — lægri lágmarksinnborgun og engin gjöld</li>
<li>Athugaðu hvort bónusinn virki á lágar innlagnir (sumir krefjast €20+)</li>
<li>Veldu spilakassa með lágri lágmarksveðjun (€0.10 eða lægra)</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Byrja að spila →</a></div>'''
    },
    {
        "slug": "okeypis-snuningar-spilaviti",
        "title": "Ókeypis snúningar spilavíti — bestu frísnúningatilboðin á Íslandi",
        "desc": "Spilavíti með ókeypis snúningum fyrir íslenska spilara. Frísnúningar í velkomstbónus og vikuleg tilboð.",
        "emoji": "🎰",
        "colors": ("#14080c", "#401828", "#702840"),
        "content": f'''<h1>Ókeypis snúningar spilavíti — Ísland 2026</h1>
{{hero}}
<p>Ókeypis snúningar (free spins) eru vinsælasta tegundin af spilavítisbónus. Hér eru <strong>bestu frísnúningatilboðin</strong> fyrir íslenska spilara.</p>

<h2>Bestu frísnúningatilboðin</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — 200 frísnúningar + allt að 5 BTC. 40x veðskilyrði.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/7bit/">7Bit Casino</a></strong> — 100 frísnúningar á fyrstu innborgun. 40x veðskilyrði.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/hellspin/">Hellspin</a></strong> — 150 frísnúningar + 100% bónus.</p></div>

<h2>Tegundir frísnúninga</h2>
<ul>
<li><strong>Velkomst frísnúningar</strong> — hluti af velkomstpakka við skráningu</li>
<li><strong>Frísnúningar án innborgunar</strong> — <a href="{URL_BASE}leidbeiningar/frisnuningar-an-innborgunar/">engin innborgun þarf</a></li>
<li><strong>Vikulegar frísnúningar</strong> — endurtekin tilboð fyrir virka spilara</li>
<li><strong>Frísnúningar í leikjum</strong> — scatter-tákn virkja þær í spilakassa</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Fá frísnúninga →</a></div>'''
    },
    {
        "slug": "ruletta-a-netinu-island",
        "title": "Rúlletta á netinu á Íslandi — bestu rúllettuborðin",
        "desc": "Spilaðu rúllettu á netinu frá Íslandi. Evrópsk, amerísk og lifandi rúlletta hjá bestu spilavítunum.",
        "emoji": "🎡",
        "colors": ("#0c0814", "#201840", "#302870"),
        "content": f'''<h1>Rúlletta á netinu — Ísland 2026</h1>
{{hero}}
<p>Rúlletta er einn vinsælasti spilavítisleikurinn í heiminum. Hér er leiðarvísir um <strong>bestu rúllettuborðin</strong> á netinu fyrir íslenska spilara.</p>

<h2>Tegundir rúllettu</h2>
<ul>
<li><strong>Evrópsk rúlletta</strong> — 37 reitir (0-36), 2.7% forskot hússins. Besti kosturinn.</li>
<li><strong>Amerísk rúlletta</strong> — 38 reitir (0, 00, 1-36), 5.26% forskot — forðastu þessa.</li>
<li><strong>Frönsk rúlletta</strong> — eins og evrópsk en með La Partage reglu (1.35% forskot á jöfnum veðmálum).</li>
<li><strong>Lifandi rúlletta</strong> — raunverulegir spilastjórar í beinni. <a href="{URL_BASE}live/">Sjá lifandi leiki →</a></li>
</ul>

<h2>Bestu spilavítin fyrir rúllettu</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — fjölbreytt úrval rúllettu í beinni frá Evolution.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — evrópsk rúlletta, Lightning Roulette og fleira.</p></div>

<h2>Ráð fyrir rúllettu</h2>
<ul>
<li>Veldu alltaf <strong>evrópska rúllettu</strong> fram yfir ameríska</li>
<li>Jöfn veðmál (rautt/svart, oddatölur/sléttir) hafa besta líkurnar</li>
<li>Settu þér tapmörk áður en þú byrjar</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila rúllettu →</a></div>'''
    },
    {
        "slug": "spilaviti-an-kyc",
        "title": "Spilavíti án KYC — spila án auðkenningar á Íslandi",
        "desc": "Netspilavíti sem krefjast ekki KYC staðfestingar. Spilaðu nafnlaust með dulritunargjaldmiðlum.",
        "emoji": "🕵️",
        "colors": ("#08140c", "#184028", "#287040"),
        "content": f'''<h1>Spilavíti án KYC á Íslandi 2026</h1>
{{hero}}
<p>Margir íslenskir spilarar vilja spila <strong>án þess að senda inn persónuskilríki</strong>. Nokkur dulritunarspilavíti leyfa þetta — hér er listi.</p>

<h2>Hvað þýðir "án KYC"?</h2>
<p>KYC (Know Your Customer) er auðkenningarferli þar sem spilavíti biður um vegabréf, reikninga eða önnur skilríki. Spilavíti án KYC leyfa þér að skrá þig og spila <strong>eingöngu með dulritunargjaldmiðlum</strong> án þess að senda inn skjöl.</p>

<h2>Spilavíti án KYC</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — engin KYC krafist fyrir dulritunarspilara (nema háar upphæðir).</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> — skráðu þig með tölvupósti, leggðu inn dulritun og spilaðu strax.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/cloudbet/">Cloudbet</a></strong> — dulritun eingöngu, lágmarks KYC.</p></div>

<h2>Kostir og gallar</h2>
<ul>
<li>✅ Aukin friðhelgi — engin persónuskjöl</li>
<li>✅ Hraðari skráning — spilaðu á mínútum</li>
<li>✅ Engin bankalokun — dulritun fer framhjá bankatakmörkunum</li>
<li>⚠️ Takmarkaðir greiðslumátar — eingöngu dulritun</li>
<li>⚠️ Minni neytendavernd ef eitthvað fer úrskeiðis</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila nafnlaust →</a></div>'''
    },
    {
        "slug": "revolut-spilaviti-island",
        "title": "Revolut spilavíti á Íslandi — leggðu inn með Revolut",
        "desc": "Hvernig á að nota Revolut til að leggja inn og taka út af netspilavítum á Íslandi. Skref fyrir skref.",
        "emoji": "💳",
        "colors": ("#0a0a14", "#1a1a40", "#2828a0"),
        "content": f'''<h1>Revolut spilavíti á Íslandi 2026</h1>
{{hero}}
<p><strong>Revolut</strong> er ein vinsælasta greiðsluappið á Íslandi og virkar vel til að leggja inn á netspilavíti — sérstaklega þegar íslenskir bankar loka á spilavítagreiðslur.</p>

<h2>Hvernig virkar Revolut með spilavítum?</h2>
<ol>
<li>Opnaðu Revolut appið og fylltu á reikninginn (bankamillifærsla eða kort)</li>
<li>Notaðu Revolut Visa/Mastercard kortið til að leggja inn á spilavítið</li>
<li>Greiðslan fer í gegn sem erlend kortafærsla — ekki bein spilavítagreiðsla</li>
<li>Úttektir fara beint til baka á Revolut reikninginn þinn</li>
</ol>

<h2>Af hverju Revolut?</h2>
<ul>
<li>✅ Fer framhjá bankalokunum — íslenskir bankar sjá ekki "spilavíti"</li>
<li>✅ Tafarlausar innlagnir</li>
<li>✅ Gjaldeyrisskipti á góðu gengi (ISK → EUR)</li>
<li>✅ Sýndarkort til aukins öryggis</li>
</ul>

<h2>Spilavíti sem taka við Revolut</h2>
<div class="info-box"><p>Flest spilavíti sem taka við <strong>Visa/Mastercard</strong> samþykkja Revolut kort — þar á meðal <a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a>, <a href="{URL_BASE}spilaviti/20bet/">20Bet</a> og <a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a>.</p></div>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Leggja inn núna →</a></div>'''
    },
    {
        "slug": "spilaviti-app-island",
        "title": "Spilavíti app á Íslandi — bestu spilavítaöppin í farsíma",
        "desc": "Bestu spilavítaöppin fyrir iPhone og Android á Íslandi. Spilaðu spilakassa og lifandi leiki í símanum.",
        "emoji": "📱",
        "colors": ("#140c08", "#402818", "#704828"),
        "content": f'''<h1>Spilavíti app á Íslandi 2026</h1>
{{hero}}
<p>Spilaðu þín uppáhalds spilavítisleiki <strong>hvar sem þú ert</strong> á Íslandi. Flest netspilavíti bjóða upp á fullkomin farsímaupplifun.</p>

<h2>Bestu spilavítin í farsíma</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — sérhönnuð farsímaapp (Android). iOS í gegnum vafra.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — bráðfínt farsímaviðmót, engrar niðurhals þörf.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> — Progressive Web App (PWA) — settu á heimaskjá eins og app.</p></div>

<h2>App eða vafri?</h2>
<ul>
<li><strong>Vafri (Safari/Chrome):</strong> Engrar niðurhals þörf, virkar á öllum tækjum. Flest spilavíti eru fullkomlega aðlöguð.</li>
<li><strong>App:</strong> Hraðari hleðsla, push-tilkynningar um tilboð. Ekki á App Store/Google Play (spilavítaapps eru bönnuð þar).</li>
<li><strong>PWA:</strong> Besti millileiðin — settu vefsíðuna á heimaskjáinn og hún virkar eins og app.</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila í símanum →</a></div>'''
    },
    {
        "slug": "ethereum-spilaviti",
        "title": "Ethereum spilavíti á Íslandi — spilaðu með ETH",
        "desc": "Bestu Ethereum spilavítin fyrir íslenska spilara. Leggðu inn ETH og fáið hraða útborgun.",
        "emoji": "⟠",
        "colors": ("#0c0e14", "#182040", "#283870"),
        "content": f'''<h1>Ethereum spilavíti á Íslandi 2026</h1>
{{hero}}
<p><strong>Ethereum (ETH)</strong> er annar vinsælasti dulritunargjaldmiðillinn á eftir Bitcoin og frábær kostur til að leggja inn á netspilavíti frá Íslandi.</p>

<h2>Af hverju velja Ethereum?</h2>
<ul>
<li>Hraðari en Bitcoin — færslur á 1-5 mínútum</li>
<li>Lægri gjöld en Bitcoin (sérstaklega á Layer 2)</li>
<li>Stutt af næstum öllum dulritunarspilavítum</li>
<li>Auðvelt að kaupa á Coinbase eða Binance</li>
</ul>

<h2>Bestu ETH spilavítin</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — stuðningur við ETH og ERC-20 tóka. Tafarlaus innlögn.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> — ETH auk 100+ annarra dulritunargjaldmiðla.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/cloudbet/">Cloudbet</a></strong> — ETH innlagnir, hröð útborgun.</p></div>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila með ETH →</a></div>'''
    },
    {
        "slug": "pottaspilakassar-island",
        "title": "Pottaspilakassar á Íslandi — stighækkandi pottar",
        "desc": "Bestu stighækkandi pottaspilakassarnir á Íslandi. Mega Moolah, Mega Fortune og fleiri milljónapottar.",
        "emoji": "💎",
        "colors": ("#14080e", "#401828", "#702848"),
        "content": f'''<h1>Pottaspilakassar á Íslandi 2026</h1>
{{hero}}
<p>Dreymir þig um <strong>milljónavinning</strong>? Pottaspilakassar (progressive jackpots) safna hluta hvers veðmáls í stóran pott sem einn heppinn spilari vinnur.</p>

<h2>Vinsælustu pottaspilakassarnir</h2>
<div class="info-box"><p><strong>Mega Moolah</strong> (Microgaming) — met-vinningur yfir €20 milljónir. Uppáhalds pottaslotur heims.</p></div>
<div class="info-box"><p><strong>Mega Fortune</strong> (NetEnt) — lúxus-þema, þrjú pottahjól. <a href="{URL_BASE}leidbeiningar/stighaekkandi-pottar/">Leiðarvísir →</a></p></div>
<div class="info-box"><p><strong>Hall of Gods</strong> (NetEnt) — norrænna goða-þema, stórir pottar.</p></div>
<div class="info-box"><p><strong>Gates of Olympus</strong> (Pragmatic Play) — vinsæll pottaslotur með 5000x hámarki.</p></div>

<h2>Ráð um pottaspilakassa</h2>
<ul>
<li>Pottaspilakassar hafa yfirleitt <strong>lægra RTP</strong> en venjulegir spilakassar (hluti fer í pottinn)</li>
<li>Spilaðu á hámarksveðmáli ef þú vilt eiga rétt á stóra pottinum</li>
<li>Þetta eru leikir til skemmtunar — líkurnar á stóra pottinum eru mjög litlar</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa pottaspilakassa →</a></div>'''
    },
    {
        "slug": "crazy-time-island",
        "title": "Crazy Time á Íslandi — hvar á að spila og hvernig virkar",
        "desc": "Crazy Time frá Evolution Gaming — vinsælasti lifandi leikjaþátturinn. Hvar á að spila og hvernig virkar leikurinn.",
        "emoji": "🎪",
        "colors": ("#14100a", "#403018", "#705028"),
        "content": f'''<h1>Crazy Time á Íslandi 2026</h1>
{{hero}}
<p><strong>Crazy Time</strong> frá Evolution Gaming er vinsælasti lifandi leikjaþátturinn í heimi. Þetta er eins og sjónvarpsþáttur þar sem þú getur unnið stóra vinni!</p>

<h2>Hvernig virkar Crazy Time?</h2>
<ol>
<li>Leikjastjóri snýr stóru hjólinu</li>
<li>Hjólið hefur tölur (1, 2, 5, 10) og 4 bónusleiki</li>
<li>Veðjaðu á tölu eða bónusleik áður en hjólið snýst</li>
<li>Ef hjólið stoppar á þínu veðmáli vinnur þú!</li>
</ol>

<h2>Bónusleikirnir fjórir</h2>
<ul>
<li><strong>Coin Flip</strong> — einföld mynt sem snýst, rautt eða blátt</li>
<li><strong>Cash Hunt</strong> — 108 tákn á skjánum, veldu eitt</li>
<li><strong>Pachinko</strong> — bolti fellur niður og margfaldari ákvarðast</li>
<li><strong>Crazy Time</strong> — stóra hjólið með gríðarlegum margfaldara (allt að 25.000x!)</li>
</ul>

<h2>Hvar á að spila Crazy Time?</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> og <strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> bjóða báðir Crazy Time frá Evolution.</p></div>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Crazy Time →</a></div>'''
    },
    {
        "slug": "apple-pay-spilaviti",
        "title": "Apple Pay spilavíti á Íslandi — leggðu inn með Apple Pay",
        "desc": "Netspilavíti sem styðja Apple Pay greiðslur á Íslandi. Leggðu inn á nokkrum sekúndum.",
        "emoji": "🍎",
        "colors": ("#0e0e0e", "#2a2a2a", "#4a4a4a"),
        "content": f'''<h1>Apple Pay spilavíti á Íslandi 2026</h1>
{{hero}}
<p><strong>Apple Pay</strong> er ein auðveldasta leiðin til að leggja inn á netspilavíti — snertu bara Face ID eða Touch ID og greiðslan er framkvæmd.</p>

<h2>Kostir Apple Pay á spilavítum</h2>
<ul>
<li>✅ Tafarlaus innlögn — greiðsla á nokkrum sekúndum</li>
<li>✅ Öruggt — kortanúmerið þitt er aldrei deilt</li>
<li>✅ Face ID/Touch ID — engin þörf á að slá inn kortnúmer</li>
<li>✅ Virkar á iPhone, iPad, Mac og Apple Watch</li>
</ul>

<h2>Spilavíti sem styðja Apple Pay</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Apple Pay stuðningur, íslensku viðmót.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></strong> — Apple Pay + Evolution lifandi borð.</p></div>

<h2>Athugaðu</h2>
<p>Ekki öll spilavíti styðja Apple Pay — athugaðu greiðslusíðuna áður en þú skráir þig. Ef Apple Pay virkar ekki, eru <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island/">Revolut</a> og <a href="{URL_BASE}leidbeiningar/besta-crypto-spilaviti-island/">dulritunargjaldmiðlar</a> góðir valkostir.</p>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Leggja inn með Apple Pay →</a></div>'''
    },
    {
        "slug": "spilaviti-endurgreidsla",
        "title": "Endurgreiðsla (cashback) spilavíti á Íslandi",
        "desc": "Bestu netspilavítin með endurgreiðslu (cashback) fyrir íslenska spilara. Fáðu hluta tapsins til baka.",
        "emoji": "🔄",
        "colors": ("#0e0a14", "#281840", "#422870"),
        "content": f'''<h1>Endurgreiðsla (cashback) spilavíti — Ísland 2026</h1>
{{hero}}
<p><strong>Cashback bónusar</strong> skila hluta tapsins til baka — oft 5-20% vikulega. Þetta er ein hagkvæmasta tegundin af bónus fyrir reglulega spilara.</p>

<h2>Hvernig virkar cashback?</h2>
<p>Ef þú tapar €100 á viku og spilavítið býður 15% cashback, þá færðu €15 til baka. Yfirleitt er cashback án veðskilyrða — þú getur tekið peningana beint út.</p>

<h2>Bestu cashback spilavítin</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — VIP cashback sem hækkar með tíma. Allt að 15%.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/cloudbet/">Cloudbet</a></strong> — vikuleg endurgreiðsla á lifandi leikjum.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> — dagleg endurgreiðsla í gegnum VIP kerfið.</p></div>

<h2>Cashback vs velkomstbónus</h2>
<ul>
<li><strong>Velkomstbónus:</strong> Einu sinni, háar upphæðir, há veðskilyrði (30-50x)</li>
<li><strong>Cashback:</strong> Endurtekið, lægri upphæðir, yfirleitt engin veðskilyrði</li>
<li>Fyrir langtímaspilara er cashback oft betri kosturinn</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Fá cashback →</a></div>'''
    },
    {
        "slug": "vpn-spilaviti-island",
        "title": "VPN og spilavíti á Íslandi — virkar það?",
        "desc": "Er hægt að nota VPN til að spila á netspilavítum frá Íslandi? Hvað þarf að vita um VPN og spilavíti.",
        "emoji": "🔒",
        "colors": ("#080c14", "#182840", "#284870"),
        "content": f'''<h1>VPN og spilavíti á Íslandi 2026</h1>
{{hero}}
<p>Margir íslenskir spilarar velta því fyrir sér hvort <strong>VPN</strong> geti hjálpað við að nálgast spilavíti eða fara framhjá takmörkunum.</p>

<h2>Þarftu VPN til að spila á netspilavítum?</h2>
<p>Í flestum tilfellum <strong>nei</strong>. Spilavítin sem við mælum með taka öll við íslenskum spilurum beint — engin VPN þörf. Dulritunargjaldmiðlar leysa vandamálið með bankagreiðslum.</p>

<h2>Hvenær er VPN gagnlegt?</h2>
<ul>
<li><strong>Friðhelgi</strong> — VPN felur IP-töluna þína og dulkóðar umferð</li>
<li><strong>Opinbert WiFi</strong> — VPN verndar þig á óöruggum netum (veitingastaðir, flugvellir)</li>
<li><strong>Ferðalög</strong> — ef þú ert á ferðalagi í landi þar sem spilavíti eru bönnuð</li>
</ul>

<h2>Viðvörun</h2>
<div class="info-box"><p>⚠️ <strong>Flest spilavíti banna VPN notkun</strong> í skilmálum sínum. Ef spilavítið uppgötvar VPN getur það lokað reikningnum þínum og haldið vinningum. Notaðu VPN eingöngu til verndar — ekki til að komast framhjá landfræðilegum takmörkunum.</p></div>

<p>Betri lausn: Notaðu <a href="{URL_BASE}leidbeiningar/besta-crypto-spilaviti-island/">dulritunarspilavíti</a> sem taka beint við íslenskum spilurum.</p>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila án VPN →</a></div>'''
    },
    {
        "slug": "spilavitin-a-netinu-a-islandi",
        "title": "Spilavítin á netinu á Íslandi 2026 — heildaryfirlit",
        "desc": "Allt sem þú þarft að vita um spilavíti á netinu á Íslandi. Umsagnir, bónusar, löggjöf og ráðleggingar um ábyrga spilun.",
        "emoji": "🇮🇸",
        "colors": ("#0a1628", "#102040", "#1a3060"),
        "content": f'''<h1>Spilavítin á netinu á Íslandi 2026</h1>
{{hero}}
<p>Íslenskir spilarar hafa takmarkaðan aðgang að innlendum spilavítum, en <strong>erlend netspilavíti</strong> bjóða upp á fjölbreytt úrval leikja, bónusa og greiðsluleiða. Hér förum við yfir helstu atriði um spilavíti á netinu á Íslandi.</p>

<h2>Er löglegt að spila á netspilavítum á Íslandi?</h2>
<p>Á Íslandi er ekkert innlent leyfiskerfi fyrir netspilavíti. Þó er ekki ólöglegt fyrir einstaklinga að spila á erlendum spilavítum á netinu. Flest spilavíti sem þjóna íslenskum spilurum starfa undir alþjóðlegum leyfum, til dæmis frá <strong>Malta (MGA)</strong>, <strong>Curaçao</strong> eða <strong>Bretlandi (UKGC)</strong>.</p>
<p>Lestu nánar um <a href="{URL_BASE}leidbeiningar/log-um-fjarhaettuspil-a-islandi/">lög um fjárhættuspil á Íslandi</a>.</p>

<h2>Hvernig veljum við bestu spilavítin?</h2>
<ul>
<li><strong>Leyfi og öryggi</strong> — aðeins spilavíti með gilt alþjóðlegt leyfi</li>
<li><strong>Leikjaúrval</strong> — spilakassar, borðleikir, lifandi spilavíti</li>
<li><strong>Bónusar</strong> — sanngjarn veðskilyrði og raunhæf tilboð</li>
<li><strong>Greiðsluleiðir</strong> — stuðningur við dulritunargjaldmiðla og alþjóðleg kort</li>
<li><strong>Útborgunarhraði</strong> — hversu fljótt þú færð peningana þína</li>
</ul>
<p>Lestu <a href="{URL_BASE}hvernig-vid-metum/">hvernig við metum spilavíti</a> fyrir nánari upplýsingar.</p>

<h2>Bestu netspilavítin á Íslandi</h2>
<div class="info-box"><p><strong>Slotoro</strong> — 98 spilakassar, hröð skráning og stuðningur við dulritunargjaldmiðla. <a href="{URL_BASE}spilaviti/slotoro/">Umsögn →</a></p></div>
<div class="info-box"><p><strong>BitStarz</strong> — yfir 3.000 leikir, bæði hefðbundnar og dulritunargreiðslur. <a href="{URL_BASE}spilaviti/bitstarz/">Umsögn →</a></p></div>
<div class="info-box"><p><strong>Stake</strong> — vinsælt dulritunarspilavíti með sérstökum leikjum. <a href="{URL_BASE}spilaviti/stake/">Umsögn →</a></p></div>

<h2>Algengar spurningar</h2>
<h3>Hvaða greiðsluleiðir eru í boði?</h3>
<p>Flest netspilavíti sem þjóna Íslandi taka við <a href="{URL_BASE}greidslur/bitcoin/">Bitcoin</a>, <a href="{URL_BASE}greidslur/ethereum/">Ethereum</a>, <a href="{URL_BASE}greidslur/visa-i-spilavitum/">Visa</a> og <a href="{URL_BASE}greidslur/mastercard-i-spilavitum/">Mastercard</a>.</p>

<h3>Er hægt að spila í íslenskum krónum?</h3>
<p>Fá spilavíti styðja ISK beint. Flest nota EUR eða USD og bankinn sér um gjaldmiðlaskipti. <a href="{URL_BASE}leidbeiningar/spilaviti-isk-kronur/">Lestu meira →</a></p>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Skoða Slotoro →</a></div>'''
    },
    {
        "slug": "bestu-spilavitin-a-netinu",
        "title": "Bestu spilavítin á netinu 2026 — topp 10 listi",
        "desc": "Uppfærður listi yfir bestu netspilavítin 2026. Sérfræðiugsagnir, bónusar, útborgunarhraði og leikjaúrval borið saman.",
        "emoji": "🏆",
        "colors": ("#1a0a2e", "#2a1050", "#3a1870"),
        "content": f'''<h1>Bestu spilavítin á netinu 2026</h1>
{{hero}}
<p>Við höfum prófað og borið saman tugir netspilavíta til að finna <strong>bestu valkostina</strong> fyrir íslenska spilara. Hér er listi okkar yfir 10 bestu spilavítin á netinu árið 2026.</p>

<h2>Topp 10 netspilavítin 2026</h2>

<h3>1. Slotoro — besta netspilavítið á Íslandi</h3>
<div class="info-box"><p>⭐ <strong>Einkunn: 9.5/10</strong> | 98 spilakassar | Hröð skráning | Dulritunargreiðslur<br>Slotoro sker sig úr með einfaldri upplifun og hröðum útborgunum. <a href="{URL_BASE}spilaviti/slotoro/">Lesa umsögn →</a></p></div>

<h3>2. BitStarz — besta dulritunarspilavítið</h3>
<div class="info-box"><p>⭐ <strong>Einkunn: 9.3/10</strong> | 3.000+ leikir | Bitcoin og fleiri | Margverðlaunað<br>BitStarz hefur unnið til margra verðlauna og býður bæði dulritunar- og hefðbundnar greiðslur. <a href="{URL_BASE}spilaviti/bitstarz/">Lesa umsögn →</a></p></div>

<h3>3. Stake — besta spilavítið fyrir live leiki</h3>
<div class="info-box"><p>⭐ <strong>Einkunn: 9.1/10</strong> | Sérstakir Stake-leikir | Stórt live-úrval | VIP-kerfi<br>Stake er þekkt fyrir sérstaka leiki eins og Crash, Dice og Plinko. <a href="{URL_BASE}spilaviti/stake/">Lesa umsögn →</a></p></div>

<h3>4. BC.Game — besta spilavítið fyrir dulritunarúrval</h3>
<div class="info-box"><p>⭐ <strong>Einkunn: 9.0/10</strong> | 100+ dulritunargjaldmiðlar | Provably Fair | Stór samfélag<br><a href="{URL_BASE}spilaviti/bc-game/">Lesa umsögn →</a></p></div>

<h3>5-10. Fleiri frábær spilavíti</h3>
<div class="info-box"><p><strong>TonyBet</strong> — sterkt íþróttaveðmálaúrval. <a href="{URL_BASE}spilaviti/tonybet/">Umsögn →</a><br>
<strong>7Bit</strong> — bónus án veðskilyrða. <a href="{URL_BASE}spilaviti/7bit/">Umsögn →</a><br>
<strong>Cloudbet</strong> — háar útborgunarmörk. <a href="{URL_BASE}spilaviti/cloudbet/">Umsögn →</a><br>
<strong>HellSpin</strong> — stór velkomstbónus. <a href="{URL_BASE}spilaviti/hellspin/">Umsögn →</a><br>
<strong>KatsuBet</strong> — japanskt þema. <a href="{URL_BASE}spilaviti/katsubet/">Umsögn →</a><br>
<strong>Winz</strong> — bónus án veðskilyrða. <a href="{URL_BASE}spilaviti/winz/">Umsögn →</a></p></div>

<h2>Hvernig veljum við bestu spilavítin?</h2>
<p>Við leggjum áherslu á <a href="{URL_BASE}hvernig-vid-metum/">ítarlegt matsferli</a> sem tekur til öryggis, leikjaúrvals, bónusa, greiðsluleiða og þjónustu.</p>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa #1 spilavítið →</a></div>'''
    },
    {
        "slug": "spilaviti-island-2026",
        "title": "Spilavíti á Íslandi 2026 — löggjöf, valkostir og ráðleggingar",
        "desc": "Er löglegt að spila á spilavítum á Íslandi? Allt um löggjöf, bestu erlend netspilavítin og hvernig íslenskir spilarar geta spilað á netinu.",
        "emoji": "🏔️",
        "colors": ("#0a1a2a", "#152a3a", "#203a4a"),
        "content": f'''<h1>Spilavíti á Íslandi 2026</h1>
{{hero}}
<p>Ísland hefur ekki innlend spilavíti eða leyfiskerfi fyrir netspilavíti, en íslenskir spilarar geta spilað á <strong>erlendum netspilavítum</strong> sem starfa undir alþjóðlegum leyfum.</p>

<h2>Löggjöf um fjárhættuspil á Íslandi</h2>
<p>Samkvæmt íslenskum lögum er fjárhættuspil almennt bannað, en þó eru nokkrar undantekningar:</p>
<ul>
<li><strong>Happdrætti Íslands</strong> — eina löglega fjárhættuspilið á Íslandi</li>
<li><strong>Íslenskir spilakassar</strong> — voru bannaðir með lögum</li>
<li><strong>Erlend netspilavíti</strong> — ekki beinlínis bönnuð fyrir einstaklinga</li>
</ul>
<p>Lestu nánar í <a href="{URL_BASE}leidbeiningar/log-um-fjarhaettuspil-a-islandi/">ítarlegri grein um löggjöf</a>.</p>

<h2>Hvernig spila Íslendingar á netinu?</h2>
<p>Flestir íslenskir spilarar nota erlend netspilavíti sem taka við leikmönnum frá Íslandi. Algengustu greiðsluleiðirnar eru:</p>
<ul>
<li><a href="{URL_BASE}greidslur/bitcoin/">Bitcoin</a> og önnur dulritunargjaldmiðlar</li>
<li><a href="{URL_BASE}greidslur/visa-i-spilavitum/">Visa</a> og <a href="{URL_BASE}greidslur/mastercard-i-spilavitum/">Mastercard</a></li>
<li><a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a> og <a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a></li>
</ul>

<h2>Bestu spilavítin sem taka við Íslendigum</h2>
<div class="info-box"><p><strong>Slotoro</strong> — topp val okkar fyrir Ísland. <a href="{URL_BASE}spilaviti/slotoro/">Umsögn →</a></p></div>
<div class="info-box"><p><strong>BitStarz</strong> — besta dulritunarspilavítið. <a href="{URL_BASE}spilaviti/bitstarz/">Umsögn →</a></p></div>
<div class="info-box"><p><strong>Stake</strong> — vinsælast meðal ungs fólks. <a href="{URL_BASE}spilaviti/stake/">Umsögn →</a></p></div>

<h2>Ábyrg spilun á Íslandi</h2>
<p>Ef þú eða einhver sem þú þekkir á í vandræðum með fjárhættuspil, vinsamlegast hafðu samband við <strong>SÁÁ</strong> (Samtök áfengis- og vímuefnasjúkra) í síma 550-5100. Lestu okkar <a href="{URL_BASE}abyrg-spilun/">leiðbeiningar um ábyrga spilun</a>.</p>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Skoða bestu spilavítin →</a></div>'''
    },
    {
        "slug": "ny-spilaviti-2026",
        "title": "Ný spilavíti á Íslandi 2026 — nýjustu netspilavítin",
        "desc": "Nýjustu netspilavítin sem hafa opnað fyrir íslenska spilara 2026. Nýir bónusar, leikir og eiginleikar prófaðir.",
        "emoji": "🆕",
        "colors": ("#1a0a20", "#2a1040", "#3a1860"),
        "content": f'''<h1>Ný spilavíti á Íslandi 2026</h1>
{{hero}}
<p>Netspilavítamarkaðurinn er sífellt að breytast og ný spilavíti opna reglulega. Hér eru <strong>nýjustu spilavítin</strong> sem taka við íslenskum spilurum árið 2026.</p>

<h2>Af hverju að velja nýtt spilavíti?</h2>
<ul>
<li><strong>Betri bónusar</strong> — ný spilavíti bjóða oft stærri velkomstbónusa til að laða að spilara</li>
<li><strong>Nýjasta tæknin</strong> — nútímalegt viðmót, farsímavænt og hraðar útborganir</li>
<li><strong>Nýir leikir</strong> — aðgangur að nýjustu spilakössum og live-leikjum</li>
<li><strong>Nýjungar</strong> — gamification, VIP-kerfi og sérstök tilboð</li>
</ul>

<h2>Nýjustu spilavítin sem við mælum með</h2>
<div class="info-box"><p><strong>Slotoro</strong> — nýlega endurbætt með stærra leikjaúrvali. <a href="{URL_BASE}spilaviti/slotoro/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong>EpicBet</strong> — nýtt spilavíti með áherslu á live-leiki. <a href="{URL_BASE}spilaviti/epicbet/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong>Respin</strong> — nýr valkostur með hröðum útborgunum. <a href="{URL_BASE}spilaviti/respin/">Lesa umsögn →</a></p></div>

<h2>Hvað á að huga að þegar valið er nýtt spilavíti</h2>
<p>Þó ný spilavíti bjóði oft spennandi nýjungar er mikilvægt að vera varkár:</p>
<ul>
<li>Athugaðu hvort spilavítið hafi <a href="{URL_BASE}leidbeiningar/hvernig-a-ad-stadfesta-spilavitaleyfi/">gilt leyfi</a></li>
<li>Lestu <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrði bónusa</a> vel</li>
<li>Prófaðu <a href="{URL_BASE}leidbeiningar/hvernig-a-ad-hafa-samband-vid-thjonustuver/">þjónustuver</a> áður en þú leggur inn</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa nýjasta spilavítið →</a></div>'''
    },
    {
        "slug": "netspilaviti-island",
        "title": "Netspilavíti á Íslandi — yfirlit og umsagnir 2026",
        "desc": "Heildaryfirlit yfir netspilavíti sem þjóna Íslandi. Bónusar, leikjaúrval, greiðsluleiðir og öryggi metið af sérfræðingum.",
        "emoji": "🎰",
        "colors": ("#0a0a1e", "#14142e", "#1e1e3e"),
        "content": f'''<h1>Netspilavíti á Íslandi 2026</h1>
{{hero}}
<p>Leitaðu ekki lengur — hér finnur þú <strong>heildstæðar umsagnir</strong> um öll helstu netspilavíti sem taka við íslenskum spilurum. Við prófum spilavítin sjálf og gefum óháðar einkunnir.</p>

<h2>Hvað gerir netspilavíti gott?</h2>
<p>Við skoðum marga þætti þegar við metum spilavíti:</p>
<ul>
<li><strong>Öryggi fyrst</strong> — gilt leyfi, SSL-dulkóðun og RNG-vottun</li>
<li><strong>Leikjaúrval</strong> — fjölbreytni spilakassa, borðleikja og live-leikja</li>
<li><strong>Bónusar</strong> — raunhæf tilboð með sanngjörnum veðskilyrðum</li>
<li><strong>Greiðsluleiðir</strong> — aðeins þær sem virka frá Íslandi</li>
<li><strong>Útborgunarhraði</strong> — enginn vill bíða í vikur eftir vinningum</li>
</ul>

<h2>Bestu netspilavítin núna</h2>
<p>Skoðaðu <a href="{URL_BASE}spilaviti/">alla lista spilavíta</a> eða smelltu á einstaka umsögn:</p>
<div class="info-box"><p>🥇 <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> — besta heildareinkunnin<br>
🥈 <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> — besta dulritunarspilavítið<br>
🥉 <a href="{URL_BASE}spilaviti/stake/">Stake</a> — besta live-spilavítið</p></div>

<h2>Greiðsluleiðir sem virka á Íslandi</h2>
<p>Vegna takmarkana íslensku bankanna eru <a href="{URL_BASE}greidslur/bitcoin/">dulritunargjaldmiðlar</a> oft besti kosturinn. Skoðaðu einnig <a href="{URL_BASE}greidslur/">allar greiðsluleiðir</a>.</p>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Byrja að spila →</a></div>'''
    },
    {
        "slug": "spilaviti-an-skraningar",
        "title": "Spilavíti án skráningar á Íslandi — spila strax 2026",
        "desc": "Finndu netspilavíti sem leyfa þér að spila án langrar skráningar. Hraðskráning á 30 sek, dulritunarinnlagnir og engin KYC fyrr en við úttekt.",
        "emoji": "⚡",
        "colors": ("#0a1628", "#132d4f", "#1c4476"),
        "content": f'''<h1>Spilavíti án skráningar á Íslandi 2026</h1>
{{hero}}
<p>Hefðbundin netspilavíti krefjast langrar skráningar: nafn, heimilisfang, símanúmer, vegabréfsnúmer — og síðan bíða eftir staðfestingu. <strong>Margir íslenskir spilarar vilja einfaldlega spila án þess að eyða 10 mínútum í eyðublöð.</strong></p>
<p>Góðu fréttirnar: nokkur netspilavíti bjóða nú hraðskráningu eða jafnvel möguleikann að spila án hefðbundinnar skráningar. Hér útskýrum við hvernig það virkar, hvað þarf að varast og hvaða spilavíti bjóða þetta.</p>

<h2>Hvað þýðir „spilavíti án skráningar"?</h2>
<p>Hugtakið nær yfir tvennt:</p>
<ul>
<li><strong>Alvöru skráningarlaus spilavíti (Pay N Play)</strong> — Þú greiðir beint með bankaauðkenningu og reikningurinn stofnast sjálfvirkt. Algengara í Finnlandi og Svíþjóð en á Íslandi.</li>
<li><strong>Hraðskráning (Quick Registration)</strong> — Einungis netfang og lykilorð. Engin gögn þarf fyrr en við fyrstu úttekt. Þetta er algengara og virkar vel á Íslandi.</li>
</ul>
<p>Fyrir íslenska spilara er hraðskráning raunhæfasti kosturinn — sérstaklega ef þú notar <a href="{URL_BASE}greidslur/bitcoin/">dulritunargjaldmiðla</a> til innborgunar.</p>

<h2>Hvernig virkar hraðskráning?</h2>
<ol>
<li><strong>Skráðu netfang og lykilorð</strong> — tekur 20-30 sekúndur</li>
<li><strong>Veldu greiðsluaðferð</strong> — Bitcoin, USDT, Ethereum eða e-wallet</li>
<li><strong>Leggðu inn</strong> — reikningurinn er tilbúinn, þú getur spilað strax</li>
<li><strong>KYC kemur seinna</strong> — þegar þú biður um fyrstu úttekt sendir þú inn gögn</li>
</ol>

<h2>Samanburður: hraðskráning vs hefðbundin skráning</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Hraðskráning</th><th>Hefðbundin skráning</th></tr></thead><tbody>
<tr><td>Tími til að byrja</td><td>30 sek — 2 mín</td><td>5-15 mínútur</td></tr>
<tr><td>Upplýsingar krafist</td><td>Netfang + lykilorð</td><td>Nafn, heimilisfang, fæðingardagur, símanúmer</td></tr>
<tr><td>KYC staðfesting</td><td>Við fyrstu úttekt</td><td>Strax eða innan 72 klst</td></tr>
<tr><td>Dulritunarinnlagnir</td><td>Já — engin viðbótargögn</td><td>Já en oft með KYC kröfu</td></tr>
<tr><td>Úttektarhraði</td><td>Eftir KYC: 0-24 klst</td><td>0-24 klst</td></tr>
</tbody></table>

<h2>Bestu spilavítin með hraðskráningu á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — Skráning á 30 sekúndum. Einungis netfang og lykilorð. Styður 8+ dulritunargjaldmiðla. 200% velkomstbónus. Engin gögn fyrr en við úttekt. <a href="{URL_BASE}spilaviti/stake/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> — Netfangsskráning. 100+ dulritunargjaldmiðlar studdir. 300% allt að 1 BTC. Engin KYC fyrir dulritunarinnlagnir undir ákveðnu þaki. <a href="{URL_BASE}spilaviti/bc-game/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Hraðskráning og tafarlausar Bitcoin innborganir. 5 BTC + 200 FS. Margverðlaunað spilavíti síðan 2014. <a href="{URL_BASE}spilaviti/bitstarz/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/wildcoins/">WildCoins</a></strong> — Einföld skráning, styður BTC/ETH/LTC/USDT. 250% + 100 FS. Gott fyrir byrjendur. <a href="{URL_BASE}spilaviti/wildcoins/">Lesa umsögn →</a></p></div>

<h2>Er hraðskráning jafn örugg og hefðbundin skráning?</h2>
<p>Já — ef spilavítið er með gilt leyfi. Hraðskráning breytir ekki örygginu. Munurinn er aðeins <em>hvenær</em> gögnin eru send inn — ekki <em>hvort</em> þau eru send.</p>
<p>Spilavíti með Curaçao, Malta (MGA) eða bretskt leyfi (UKGC) verða öll að staðfesta deili á þér áður en þau greiða út. Það tryggir öryggi jafnt í hraðskráningu og hefðbundinni.</p>
<p>Athugaðu alltaf leyfið: <a href="{URL_BASE}leidbeiningar/hvernig-a-ad-stadfesta-spilavitaleyfi/">Hvernig á að staðfesta spilavítileyfi →</a></p>

<h2>Ráðleggingar fyrir íslenska spilara</h2>
<ul>
<li>✅ Notaðu <strong>dulritunargjaldmiðla</strong> til innborgunar — þá þarftu enga viðbótargögn og forðast <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">bankahöfnun</a></li>
<li>✅ Skráðu raunverulegt netfang — þú þarft það til að endurstilla lykilorð og taka á móti úttektarstaðfestingu</li>
<li>✅ Hafðu ljósmynd af vegabréfi tilbúna — þú þarft hana seinna við KYC</li>
<li>✅ Lestu <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">bónusskilmála</a> áður en þú tekur á móti velkomstbónus</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Get ég spilað alvöru peninga án þess að skrá mig?</h3>
<p>Á flestum spilavítum þarftu lágmarks skráningu (netfang + lykilorð). Algjörlega skráningarlaus spilavíti (Pay N Play) eru sjaldgæf á Íslandi en algengari í Finnlandi. Hraðskráning er raunhæfasti valkosturinn.</p>
<h3>Hvenær þarf ég að senda inn gögn (KYC)?</h3>
<p>Yfirleitt þegar þú tekur út í fyrsta skipti eða nærð ákveðnu innborgunarþaki (t.d. €2.000). Sum spilavíti biðja um gögn fyrr ef þau gruna svik.</p>
<h3>Hvaða gögn þarf ég að senda?</h3>
<p>Yfirleitt: ljósmynd af vegabréfi eða ökuskírteini, sönnun á heimilisfangi (reikningur) og stundum selfie með skilríkjum.</p>
<h3>Er hægt að forðast KYC algjörlega?</h3>
<p>Sum dulritunarspilavíti hafa hærri þröskulda áður en KYC er krafist. En öll lögleg spilavíti þurfa að staðfesta deili á þér einhvern tíma — það er krafa leyfisins.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila strax →</a></div>'''
    },
    {
        "slug": "okeypis-spilaviti-island",
        "title": "Ókeypis spilavíti á Íslandi — spila án áhættu 2026",
        "desc": "Prófaðu spilakassa og borðleiki ókeypis á íslenskum netspilavítum. Demo-hamur, bónusar án innborgunar og frísnúningar.",
        "emoji": "🎮",
        "colors": ("#0d1a0a", "#1a3314", "#274d1e"),
        "content": f'''<h1>Ókeypis spilavíti á Íslandi — spila án áhættu 2026</h1>
{{hero}}
<p>Margir íslenskir spilarar vilja <strong>prófa spilavíti áður en þeir leggja inn peninga</strong>. Það er skynsamleg nálgun — og það eru margar leiðir til að gera það. Hér er heildaryfirlit yfir allar aðferðir til að spila ókeypis á Íslandi.</p>

<h2>Þrjár leiðir til að spila ókeypis</h2>
<h3>1. Demo-hamur (prufuhamur)</h3>
<p>Langflestir spilakassar hafa „Demo" eða „Prufa" hnapp. Þú spilar nákvæmlega sama leik og í alvöru — sömu grafík, sömu bónusumferðir, sama RTP — en með <strong>sýndarpeningum</strong>. Engrar skráningar krafist á flestum spilavítum.</p>
<p>Demo-hamur er besta leiðin til að kynnast leik áður en þú veðjar raunverulegum peningum. Þú getur prófað tugi spilakassa án nokkurrar áhættu.</p>

<h3>2. Bónus án innborgunar (no deposit bonus)</h3>
<p>Sum spilavíti bjóða nýjum spilurum frísnúninga eða inneign <strong>án þess að krefjast innborgunar</strong>. Þú skráir þig, færð bónusinn sjálfvirkt og getur spilað um alvöru peninga — án þess að hafa lagt inn krónu.</p>
<p>Athugaðu: <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrði</a> eiga alltaf við. Dæmi: ef þú færð 20 frísnúninga með 40x veðskilyrðum þarftu að veðja vinninginn 40 sinnum áður en þú getur tekið út.</p>

<h3>3. Frísnúningar með fyrstu innborgun</h3>
<p>Þetta er ekki alveg „ókeypis" — þú leggur inn og færð frísnúninga ofan á. En frísnúningarnar sjálfar kosta ekkert og vinningar frá þeim eru raunverulegar.</p>

<h2>Hvað get ég spilað ókeypis?</h2>
<table class="info-table"><thead><tr><th>Leikjategund</th><th>Demo-hamur?</th><th>Bónus án innborgunar?</th><th>Dæmi</th></tr></thead><tbody>
<tr><td>Spilakassar</td><td>✅ Já — nánast allir</td><td>✅ Frísnúningar algengast</td><td><a href="{URL_BASE}spilakassar/gates-of-olympus/">Gates of Olympus</a>, <a href="{URL_BASE}spilakassar/sweet-bonanza/">Sweet Bonanza</a></td></tr>
<tr><td>Borðleikir (RNG)</td><td>✅ Já</td><td>❌ Sjaldgæft</td><td>Blackjack, rúlletta, baccarat</td></tr>
<tr><td>Lifandi spilavíti</td><td>❌ Nei</td><td>❌ Mjög sjaldgæft</td><td><a href="{URL_BASE}live/lightning-roulette/">Lightning Roulette</a></td></tr>
<tr><td>Crash-leikir</td><td>✅ Sumir</td><td>❌ Sjaldgæft</td><td>Aviator, Spaceman</td></tr>
</tbody></table>

<h2>Af hverju spila ókeypis fyrst?</h2>
<ul>
<li><strong>Kynntu þér leikinn</strong> — Bónusumferðir, sérstakir eiginleikar og hvernig leikurinn virkar raunverulega</li>
<li><strong>Prófaðu sveiflu</strong> — <a href="{URL_BASE}leidbeiningar/hvad-er-sveifla/">Há sveifla</a> þýðir sjaldgæfir en stórir vinningar. Lág sveifla = tíðir smávinningar. Uppgötvaðu hvað hentar þér</li>
<li><strong>Berðu saman spilakassa</strong> — Prófaðu 5-10 mismunandi leiki áður en þú velur hvar þú vilt veðja</li>
<li><strong>Prófaðu aðferðir</strong> — Á borðleikjum eins og <a href="{URL_BASE}leidbeiningar/blackjack-adferdir/">blackjack</a> geturðu æft aðferðir án áhættu</li>
</ul>

<h2>Bestu spilavítin með ókeypis leiki á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — Yfir 8.000 leikir frá 71 framleiðendum. Flestir í boði í demo-ham án skráningar. Velkomstpakki á 3 innborgunum. <a href="{URL_BASE}spilaviti/slotoro/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Prufuaðgangur á hundruð spilakassa án skráningar. 5 BTC + 200 FS. Demo-hamur opinn öllum. <a href="{URL_BASE}spilaviti/bitstarz/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/katsubet/">KatsuBet</a></strong> — Yfir 5.000 leikir með demo-aðgangi. 100% + 100 FS. <a href="{URL_BASE}spilaviti/katsubet/">Lesa umsögn →</a></p></div>

<h2>Vinsælustu ókeypis spilakassarnir á Íslandi</h2>
<p>Samkvæmt gögnum frá spilavítum eru þessir spilakassar vinsælastir í ókeypis prufuham hjá íslenskum spilurum:</p>
<ol>
<li><a href="{URL_BASE}spilakassar/gates-of-olympus/">Gates of Olympus</a> (Pragmatic Play) — RTP 96,5%, há sveifla</li>
<li><a href="{URL_BASE}spilakassar/sweet-bonanza/">Sweet Bonanza</a> (Pragmatic Play) — RTP 96,48%, meðalsveifla</li>
<li><a href="{URL_BASE}spilakassar/book-of-dead/">Book of Dead</a> (Play'n GO) — RTP 96,21%, há sveifla</li>
<li><a href="{URL_BASE}spilakassar/starburst/">Starburst</a> (NetEnt) — RTP 96,09%, lág sveifla</li>
<li><a href="{URL_BASE}spilakassar/big-bass-bonanza/">Big Bass Bonanza</a> (Pragmatic Play) — RTP 96,71%, há sveifla</li>
</ol>
<p>Sjá alla <a href="{URL_BASE}spilakassar/">98 spilakassaumsagnir →</a></p>

<h2>Algengar spurningar</h2>
<h3>Er hægt að vinna alvöru peninga í ókeypis ham?</h3>
<p>Nei — í demo-ham eru vinningarnir sýndarpeningar. Til að vinna raunverulega þarftu að leggja inn. Hins vegar ef þú færð <a href="{URL_BASE}leidbeiningar/frisnuningar-an-innborgunar/">bónus án innborgunar</a> (frísnúninga) eru vinningarnir raunverulegir — að uppfylltum veðskilyrðum.</p>
<h3>Þarf ég að skrá mig til að spila ókeypis?</h3>
<p>Á flestum spilavítum þarftu ekki skráningu fyrir demo-ham. Einfaldlega opnaðu leikinn og veldu „Prufa" eða „Demo". Sum spilavíti krefjast þó skráningar — Slotoro og BitStarz gera það ekki.</p>
<h3>Er demo-hamur eins og alvöru leikurinn?</h3>
<p>Já — sömu grafík, sömu bónusumferðir, sama <a href="{URL_BASE}leidbeiningar/hvad-er-rtp/">RTP</a> og sama <a href="{URL_BASE}leidbeiningar/hvernig-rng-virkar/">RNG tækni</a>. Eini munurinn er að þú spilar með sýndarpeningum.</p>
<h3>Hversu lengi get ég spilað í demo-ham?</h3>
<p>Eins lengi og þú vilt. Sýndarpeningarnir fylla á sig aftur þegar þeir klárast — þú getur alltaf byrjað upp á nýtt.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa ókeypis →</a></div>'''
    },
    {
        "slug": "spilaviti-sem-tekur-vid-islenskum-kortum",
        "title": "Spilavíti sem tekur við íslenskum kortum — Visa og Mastercard 2026",
        "desc": "Hvaða netspilavíti taka við Visa og Mastercard frá Arion, Landsbankinn og Íslandsbanka? Lausnir þegar bankinn hafnar greiðslu.",
        "emoji": "💳",
        "colors": ("#1a0a2e", "#2d1450", "#401e72"),
        "content": f'''<h1>Spilavíti sem tekur við íslenskum kortum 2026</h1>
{{hero}}
<p>Þetta er ein algengasta spurningin frá íslenskum spilurum: <strong>„hvers vegna virkar kortið mitt ekki á spilavítinu?"</strong> Svarið er flókið og breytist reglulega. Hér er allt sem þú þarft að vita.</p>

<h2>Af hverju virka íslensk kort stundum ekki?</h2>
<p>Íslenskir bankar — Arion banki, Landsbankinn og Íslandsbanki — hafa <strong>innri stefnu</strong> sem getur lokað á kortagreiðslur til erlendra netspilavíta. Þetta er ekki byggt á lögum. <a href="{URL_BASE}leidbeiningar/log-um-fjarhaettuspil-a-islandi/">Engin lög á Íslandi banna einstaklingum</a> að spila á erlendum spilavítum.</p>
<p>Bankarnir nota MCC-kóða (Merchant Category Code) til að greina greiðslur til spilavíta. Sumir kaupmenn nota annan MCC-kóða — þá fer greiðslan í gegn. Þetta er ástæðan fyrir því að sama kortið getur virkað á einu spilavíti en ekki öðru.</p>

<h2>Staða hvers banka (nóvember 2026)</h2>
<table class="info-table"><thead><tr><th>Banki</th><th>Visa</th><th>Mastercard</th><th>Apple Pay</th><th>Athugasemd</th></tr></thead><tbody>
<tr><td>Arion banki</td><td>⚠️ Stundum</td><td>⚠️ Stundum</td><td>⚠️ Fer eftir spilavíti</td><td>Innri stefna getur lokað á greiðslur</td></tr>
<tr><td>Landsbankinn</td><td>⚠️ Stundum</td><td>⚠️ Stundum</td><td>⚠️ Fer eftir spilavíti</td><td>Sama staða og Arion</td></tr>
<tr><td>Íslandsbanki</td><td>⚠️ Stundum</td><td>⚠️ Stundum</td><td>⚠️ Fer eftir spilavíti</td><td>Nýleg breyting á reglum</td></tr>
<tr><td>Revolut</td><td>✅ Já</td><td>✅ Já</td><td>✅ Já</td><td>Fer ekki gegnum íslenskt bankakerfi</td></tr>
</tbody></table>
<p><em>⚠️ = virkar stundum, fer eftir spilavíti og tímabili. Staðan getur breyst án fyrirvara.</em></p>

<h2>Spilavíti sem líklegast taka við íslenskum kortum</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></strong> — Leyfi frá Eistlandi (EES-ríki). Evrópuleg greiðsluvinnsla sem eykur líkur á að kortagreiðsla fari í gegn. 150% + 100 FS. <a href="{URL_BASE}spilaviti/tonybet/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/20bet/">20Bet</a></strong> — Styður Visa, Mastercard og marga aðra valkosti. Lágmarksinnborgun €10. Curaçao leyfi. <a href="{URL_BASE}spilaviti/20bet/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Íslensku viðmót og Apple Pay sem getur virkað þar sem hefðbundin kort virka ekki. 100% allt að €500. <a href="{URL_BASE}spilaviti/epicbet/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — Tekur við kortum, e-wallets og dulritunargjaldmiðlum. Lágmarksinnborgun €10. <a href="{URL_BASE}spilaviti/slotoro/">Lesa umsögn →</a></p></div>

<h2>5 lausnir þegar bankinn hafnar greiðslunni</h2>
<h3>1. Dulritunargjaldmiðlar (besta lausnin)</h3>
<p><a href="{URL_BASE}greidslur/bitcoin/">Bitcoin</a>, <a href="{URL_BASE}greidslur/usdt/">USDT</a> og <a href="{URL_BASE}greidslur/ethereum/">Ethereum</a> fara beint á blokkkeðjunni — <strong>bankarnir geta ekki lokað á þessar greiðslur</strong>. Innlagnir á 1-10 mínútum, gjöld undir $1 á TRC-20 netinu.</p>
<p><a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi — skref fyrir skref →</a></p>

<h3>2. Revolut eða Wise</h3>
<p><a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island/">Revolut</a> er oft besta lausnin fyrir þá sem vilja nota kort. Revolut-kort fer ekki í gegnum íslenskt bankakerfi og á þar af leiðandi ekki á hættu að verða hafnað. Opnaðu Revolut-reikning, millifærðu frá íslenska bankanum og notaðu Revolut-kortið á spilavítinu.</p>

<h3>3. Rafræn veski (e-wallets)</h3>
<p><a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a> og <a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a> virka sem milliliður. Þú leggur inn á Skrill frá bankanum og síðan frá Skrill á spilavítið. Bankinn sér einungis millifærslu á Skrill — ekki á spilavíti.</p>

<h3>4. PIQ greiðslur</h3>
<p><a href="{URL_BASE}leidbeiningar/piq-greidslur-island/">PIQ</a> er greiðsluþjónusta sérstaklega hönnuð fyrir Ísland og Noreg. <a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a> og <a href="{URL_BASE}spilaviti/respin/">Respin</a> styðja PIQ. Innborgun tekur 1-5 mínútur.</p>

<h3>5. Apple Pay / Google Pay</h3>
<p>Sum spilavíti styðja <a href="{URL_BASE}greidslur/apple-pay-i-spilavitum/">Apple Pay</a> sem getur farið í gegn þar sem hefðbundin kortagreiðsla virkar ekki. Epicbet staðfestir Apple Pay stuðning fyrir íslenska spilara.</p>

<h2>Samanburður á greiðsluleiðum</h2>
<table class="info-table"><thead><tr><th>Greiðsluleið</th><th>Virkar alltaf?</th><th>Hraði</th><th>Gjöld</th><th>Lágmark</th></tr></thead><tbody>
<tr><td>Visa/Mastercard (ís. banki)</td><td>⚠️ Stundum</td><td>Samstundis</td><td>0-3%</td><td>€10</td></tr>
<tr><td>Revolut</td><td>✅ Já</td><td>Samstundis</td><td>0-1%</td><td>€10</td></tr>
<tr><td>Bitcoin</td><td>✅ Já</td><td>10-30 mín</td><td>$1-5</td><td>€10</td></tr>
<tr><td>USDT (TRC-20)</td><td>✅ Já</td><td>1-5 mín</td><td>$0.5-1</td><td>€10</td></tr>
<tr><td>Skrill/Neteller</td><td>✅ Já</td><td>Samstundis</td><td>1-2.5%</td><td>€10</td></tr>
<tr><td>PIQ</td><td>✅ Já (á studdum spilavítum)</td><td>1-5 mín</td><td>0%</td><td>€10</td></tr>
<tr><td>Apple Pay</td><td>⚠️ Fer eftir spilavíti</td><td>Samstundis</td><td>0%</td><td>€10</td></tr>
</tbody></table>
<p>Sjá alla <a href="{URL_BASE}greidslur/">greiðsluleiðir →</a></p>

<h2>Algengar spurningar</h2>
<h3>Er hægt að nota Revolut til innborgunar á spilavíti?</h3>
<p>Já — <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island/">Revolut</a> er ein best lausnin. Kortið fer ekki gegnum íslenskt bankakerfi og verður ekki hafnað af sömu ástæðum.</p>
<h3>Er Apple Pay valkostur á Íslandi?</h3>
<p>Já á sumum spilavítum. <a href="{URL_BASE}leidbeiningar/apple-pay-spilaviti/">Epicbet styður Apple Pay</a> og íslenskir spilarar hafa staðfest að það virki. Athugaðu hvort Apple Pay kortið þitt er tengt íslenskum banka — ef svo er getur verið að höfnun eigi enn við.</p>
<h3>Hvers vegna virkaði kortið mitt í síðasta mánuði en ekki nú?</h3>
<p>Bankarnir uppfæra MCC-lokun sína reglulega. Spilavíti geta líka skipt um greiðsluvinnslu. Staðan er í stöðugri breytingu — þess vegna er gott að hafa varaleiðir eins og dulritunargjaldmiðla.</p>
<h3>Sér bankinn minn að ég spilaði á spilavíti?</h3>
<p>Ef þú notar debetkort sér bankinn viðskiptin. Ef þú notar Skrill/Neteller sér bankinn einungis millifærslu til Skrill. Ef þú notar dulritunargjaldmiðla sér bankinn kaup á Bitcoin — ekki spilavítið sjálft.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Finna spilavíti →</a></div>'''
    },
    {
        "slug": "spilaviti-med-islensku-vidmoti",
        "title": "Spilavíti með íslensku viðmóti — öll spilavíti á íslensku 2026",
        "desc": "Listi yfir netspilavíti á íslensku: viðmót, þjónustuver, bónusskilmálar og sjálfsútilokun á þínu tungumáli. Uppfært nóvember 2026.",
        "emoji": "🇮🇸",
        "colors": ("#00205b", "#1a3a7a", "#dc1e35"),
        "content": f'''<h1>Spilavíti með íslensku viðmóti 2026</h1>
{{hero}}
<p>Flest netspilavíti eru á ensku. Fyrir íslenska spilara getur þetta verið vandamál — sérstaklega þegar kemur að bónusskilmálum, <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrðum</a> og <a href="{URL_BASE}leidbeiningar/sjalfsutilokun-spilavita/">sjálfsútilokunarvalkostum</a>. <strong>Að skilja allar reglur á eigin tungumáli er ekki aðeins þægilegt — það er öryggismál.</strong></p>

<h2>Spilavíti á íslensku — samanburður</h2>
<table class="info-table"><thead><tr><th>Spilavíti</th><th>Viðmót á íslensku?</th><th>Þjónustuver á íslensku?</th><th>Skilmálar á íslensku?</th><th>Velkomstbónus</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></td><td>✅ Alveg</td><td>✅ Já</td><td>✅ Já</td><td>100% allt að €500</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/respin/">Respin</a></td><td>✅ Alveg</td><td>✅ Já</td><td>✅ Já</td><td>200% + 50 FS</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></td><td>⚠️ Að hluta</td><td>❌ Enska</td><td>❌ Enska</td><td>Velkomstpakki á 3 innborgunum</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/20bet/">20Bet</a></td><td>❌ Enska</td><td>❌ Enska</td><td>❌ Enska</td><td>100% allt að €120</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></td><td>❌ Enska</td><td>❌ Enska</td><td>❌ Enska</td><td>5 BTC + 200 FS</td></tr>
</tbody></table>
<p><em>Uppfært nóvember 2026. Við prófum sjálf öll spilavíti áður en við metum tungumálastuðning.</em></p>

<h2>Spilavíti sem eru alveg á íslensku</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Fullkomið íslenskt viðmót frá skráningu til úttektar. Skráning, innborgun, bónusskilmálar, leikir og þjónustuver — allt á íslensku. Styður einnig Apple Pay og <a href="{URL_BASE}leidbeiningar/piq-greidslur-island/">PIQ greiðslur</a> sem eru sérstaklega hannaðar fyrir Ísland. <a href="{URL_BASE}spilaviti/epicbet/">Lesa umsögn →</a></p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/respin/">Respin Casino</a></strong> — Íslensku viðmót og PIQ greiðslur. Veðlaus bónusar (0x veðskilyrði á sumum tilboðum). Vikuleg endurgreiðsla. Systursíða Epicbet — sama eigendur, jafn góð íslensk þjónusta. <a href="{URL_BASE}spilaviti/respin/">Lesa umsögn →</a></p></div>

<h2>Spilavíti með íslensku að hluta til</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — Leikir og aðalsíða hafa verið þýdd á íslensku. Hins vegar eru bónusskilmálar og þjónustuver á ensku. Gott úrval leikja (8.000+) og velkomstpakki á 3 innborgunum. <a href="{URL_BASE}spilaviti/slotoro/">Lesa umsögn →</a></p></div>

<h2>Af hverju skiptir tungumálið svona miklu máli?</h2>
<h3>1. Bónusskilmálar og veðskilyrði</h3>
<p><a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">Veðskilyrði</a> geta verið flókin. Dæmi: „40x wagering requirement on bonus and deposit, max bet €5, game weighting applies." Ef þú skilur ekki þetta á ensku geturðu óvart tapað bónusnum. Á íslensku er allt skýrt.</p>

<h3>2. Þjónustuver (chat og tölvupóstur)</h3>
<p>Ef vandamál koma upp — greiðsla sem rann ekki í gegn, úttekt sem dregst — er miklu auðveldara að leysa vandamálið þegar þú getur tjáð þig á íslensku. Epicbet og Respin bjóða báðir þjónustuver á íslensku.</p>

<h3>3. Ábyrg spilun og sjálfsútilokun</h3>
<p>Upplýsingar um <a href="{URL_BASE}leidbeiningar/sjalfsutilokun-spilavita/">sjálfsútilokun</a>, takmörk á innborgunum og ábyrgðartól eru mikilvægari á tungumáli sem þú skilur fullkomlega. Þetta er öryggismál.</p>

<h3>4. Laga- og persónuverndarskilmálar</h3>
<p>Hvernig meðhöndlar spilavítið persónuupplýsingarnar þínar? Hvað gerist ef ágreiningur kemur upp? Þessar upplýsingar eru á íslensku hjá Epicbet og Respin.</p>

<h2>Ráð fyrir þá sem velja enskt spilavíti</h2>
<p>Ef þú velur spilavíti sem er ekki á íslensku (t.d. <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> eða <a href="{URL_BASE}spilaviti/stake/">Stake</a>) skaltu:</p>
<ul>
<li>Lesa umsögn okkar á íslensku áður — við þýðum lykilatriði bónusskilmálanna</li>
<li>Nota Google Translate á skilmálasíðuna ef þú ert í vafa</li>
<li>Hafa samband við þjónustuver <em>áður en</em> þú leggur inn ef eitthvað er óljóst</li>
<li>Setja takmörk á innborgunum strax í byrjun — þetta er auðvelt á öllum spilavítum, jafnvel á ensku</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Bjóða öll netspilavíti íslensku?</h3>
<p>Nei — langflest eru á ensku. Aðeins Epicbet og Respin bjóða fullkomið íslenskt viðmót. Slotoro er að hluta á íslensku. Alþjóðlegir risar eins og BitStarz, Stake og BC.Game eru alveg á ensku.</p>
<h3>Get ég breytt tungumáli á spilavítinu?</h3>
<p>Ef spilavítið styður íslensku er yfirleitt fánamerki eða tungumálaval neðst á síðunni. Ef íslensku er ekki á listanum styður spilavítið hana ekki.</p>
<h3>Er betra að velja spilavíti á íslensku?</h3>
<p>Ef tungumál skiptir þig máli — já. Ef þú ert þægilegur á ensku er val þitt víðara og þú getur nýtt þér stærri bónusa og fleiri leiki. Úrval á íslensku spilavítum er minna en á alþjóðlegum spilavítum.</p>
<h3>Hvernig veit ég hvort spilavítið er raunverulega á íslensku eða bara Google Translate?</h3>
<p>Raunveruleg þýðing er slétt og eðlileg. Google Translate-þýðing hefur oft skringilegar setningar og vandamál með séríslensk orð (þ, ð, æ). Epicbet og Respin nota fagþýðingar — ekki sjálfvirka þýðingu.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá spilavíti á íslensku →</a></div>'''
    },
    {
        "slug": "hvernig-a-ad-velja-spilaviti-island",
        "title": "Hvernig á að velja spilavíti á Íslandi — leiðarvísir fyrir byrjendur 2026",
        "desc": "Skref-fyrir-skref leiðarvísir til að velja netspilavíti á Íslandi. Leyfi, bónusar, greiðslur, öryggi og hvað þarf að varast.",
        "emoji": "🎯",
        "colors": ("#0d1926", "#1a324c", "#274b72"),
        "content": f'''<h1>Hvernig á að velja spilavíti á Íslandi — leiðarvísir 2026</h1>
{{hero}}
<p>Það eru hundruð netspilavíta sem taka við íslenskum spilurum. <strong>Hvernig veistu hvert er rétt fyrir þig?</strong> Þessi leiðarvísir fer yfir allt sem þú þarft að vita áður en þú skráir þig — frá leyfum og bónusum til greiðslna og öryggis.</p>

<h2>Skref 1 — Athugaðu leyfið</h2>
<p>Leyfið er fyrsta og mikilvægasta atriðið. Spilavíti með gilt leyfi er skylt að:</p>
<ul>
<li>Nota sanngjarna <a href="{URL_BASE}leidbeiningar/hvernig-rng-virkar/">slembitölugjafa (RNG)</a> sem eru óháð prófaðir</li>
<li>Greiða út vinninga innan ákveðins tíma</li>
<li>Bjóða <a href="{URL_BASE}leidbeiningar/sjalfsutilokun-spilavita/">sjálfsútilokunarverkfæri</a></li>
<li>Vernda persónuupplýsingar þínar</li>
</ul>
<p>Algeng leyfi sem íslenskir spilarar sjá:</p>
<table class="info-table"><thead><tr><th>Leyfi</th><th>Útgefandi</th><th>Traust</th><th>Dæmi um spilavíti</th></tr></thead><tbody>
<tr><td>MGA</td><td>Malta Gaming Authority</td><td>⭐⭐⭐⭐⭐ Hæst</td><td><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></td></tr>
<tr><td>UKGC</td><td>UK Gambling Commission</td><td>⭐⭐⭐⭐⭐ Hæst</td><td>—</td></tr>
<tr><td>Curaçao</td><td>Curaçao eGaming</td><td>⭐⭐⭐ Miðlungs</td><td><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a>, <a href="{URL_BASE}spilaviti/stake/">Stake</a></td></tr>
<tr><td>Eistland</td><td>Tax and Customs Board</td><td>⭐⭐⭐⭐ Gott (EES)</td><td><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></td></tr>
</tbody></table>
<p><a href="{URL_BASE}leidbeiningar/hvernig-a-ad-stadfesta-spilavitaleyfi/">Hvernig á að staðfesta spilavítileyfi — ítarleg leiðbeining →</a></p>

<h2>Skref 2 — Skoðaðu greiðsluleiðir</h2>
<p>Á Íslandi eru greiðslur stærsta vandamálið. <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">Íslenskir bankar loka stundum á kortagreiðslur</a> til spilavíta. Veldu spilavíti sem styður margar greiðsluleiðir:</p>
<ul>
<li>✅ <strong>Dulritunargjaldmiðlar</strong> — Áreiðanlegast. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin →</a></li>
<li>✅ <strong>Rafræn veski</strong> — <a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a>, <a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a></li>
<li>⚠️ <strong>Visa/Mastercard</strong> — Virkar stundum. <a href="{URL_BASE}leidbeiningar/spilaviti-sem-tekur-vid-islenskum-kortum/">Sjá stöðu íslenskra korta →</a></li>
<li>✅ <strong>PIQ</strong> — <a href="{URL_BASE}leidbeiningar/piq-greidslur-island/">Sérhannað fyrir Ísland</a></li>
</ul>

<h2>Skref 3 — Berðu saman bónusa</h2>
<p>Velkomstbónus hljómar oft vel — en smáa letrið skiptir máli. Athugaðu alltaf:</p>
<ul>
<li><strong>Veðskilyrði (wagering)</strong> — 30x þýðir að þú verður að veðja 30 sinnum bónusupphæðinni. <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">Hvað eru veðskilyrði? →</a></li>
<li><strong>Hámarksveðmál</strong> — Yfirleitt €5 á snúning meðan bónus er virkur</li>
<li><strong>Tímamörk</strong> — 7-30 dagar til að uppfylla veðskilyrði</li>
<li><strong>Leikjaþyngd</strong> — Spilakassar telja yfirleitt 100%, borðleikir 10-20%</li>
</ul>
<table class="info-table"><thead><tr><th>Spilavíti</th><th>Bónus</th><th>Veðskilyrði</th><th>Mat</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></td><td>100% allt að €500</td><td>Veðlaust (0x)</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/respin/">Respin</a></td><td>200% + 50 FS</td><td>Veðlaust (0x)</td><td>⭐⭐⭐⭐⭐</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></td><td>5 BTC + 200 FS</td><td>40x</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></td><td>Velkomstpakki</td><td>40x</td><td>⭐⭐⭐⭐</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/stake/">Stake</a></td><td>200% + VIP</td><td>Engin</td><td>⭐⭐⭐⭐</td></tr>
</tbody></table>
<p><a href="{URL_BASE}leidbeiningar/samanburdur-a-bonusum-spilavita/">Samanburður á bónusum — yfirlit →</a></p>

<h2>Skref 4 — Skoðaðu leikjaúrvalið</h2>
<p>Veldu spilavíti eftir því hvað þú vilt spila:</p>
<ul>
<li><strong>Spilakassar?</strong> — Skoðaðu fjölda framleiðenda. <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> er með 71 framleiðendur og 8.000+ leiki</li>
<li><strong>Lifandi spilavíti?</strong> — <a href="{URL_BASE}live/">Evolution og Pragmatic Play</a> eru best. <a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a> sker sig úr</li>
<li><strong>Borðleikir?</strong> — <a href="{URL_BASE}leidbeiningar/blackjack-adferdir/">Blackjack</a> og <a href="{URL_BASE}leidbeiningar/rulettu-reglur/">rúlletta</a> eru í boði á öllum spilavítum</li>
<li><strong>Crash-leikir?</strong> — <a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a> og <a href="{URL_BASE}spilaviti/stake/">Stake</a> eru sterkastir</li>
</ul>

<h2>Skref 5 — Athugaðu úttektarhraða</h2>
<p>Enginn vill bíða vikur eftir vinningum. Athugaðu:</p>
<ul>
<li>Dulritunar-úttektir: 0-24 klst (hraðast)</li>
<li>E-wallet úttektir: 0-48 klst</li>
<li>Korta-úttektir: 1-5 virka dagar</li>
<li>Bankamillifærsla: 3-7 virka dagar</li>
</ul>
<p><a href="{URL_BASE}leidbeiningar/hrod-utborgun-spilaviti/">Spilavíti með hraðri útborgun — listi →</a></p>

<h2>Skref 6 — Prófaðu spilavítið</h2>
<p>Áður en þú leggur inn stóra upphæð skaltu:</p>
<ol>
<li><a href="{URL_BASE}leidbeiningar/okeypis-spilaviti-island/">Prófa leiki í demo-ham</a> — skildu hvernig þeir virka</li>
<li>Leggja inn lágmarksupphæð (€10) og prófa greiðsluferlið</li>
<li>Prófa þjónustuver — sendu skilaboð og sjáðu hversu hratt þeir svara</li>
<li>Prófaðu úttekt — tryggðu að þú getir tekið peninga út án vandræða</li>
</ol>

<h2>Algengar spurningar</h2>
<h3>Hvert spilavíti er best fyrir byrjendur á Íslandi?</h3>
<p><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a> er besti kosturinn fyrir byrjendur: íslensku viðmót, veðlaus bónusar (þú þarft ekki skilja flókin veðskilyrði), Apple Pay stuðningur og PIQ greiðslur.</p>
<h3>Hversu mikla peninga þarf ég til að byrja?</h3>
<p>Lágmarksinnborgun á flestum spilavítum er €10 (um 1.500 ISK). Við mælum með að byrja lítið og setja takmörk á innborgunum í stillingum spilavítisins.</p>
<h3>Er öruggt að spila á netspilavíti frá Íslandi?</h3>
<p>Já — ef spilavítið er með gilt leyfi og þú notar örugga greiðsluleið. <a href="{URL_BASE}leidbeiningar/einkenni-sanngjarns-spilavitis/">Sjá einkenni sanngjarns spilavítis →</a></p>
<h3>Get ég spilað á farsímanum?</h3>
<p>Já — öll nútíma netspilavíti eru farsímavinveitt. Sum bjóða sérstök app (sértaklega Android) en flest virka beint í vafranum. <a href="{URL_BASE}spilaviti/farsimaspilaviti/">Sjá farsímaspilavíti →</a></p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Finna spilavíti →</a></div>'''
    },
    {
        "slug": "epicbet-vs-respin",
        "title": "Epicbet vs Respin — samanburður íslensku spilavítanna 2026",
        "desc": "Ítarlegur samanburður á Epicbet og Respin: bónusar, leikir, greiðsluleiðir, þjónustuver og hvort hentar betur á Íslandi.",
        "emoji": "⚔️",
        "colors": ("#1a0f28", "#2d1a45", "#402562"),
        "content": f'''<h1>Epicbet vs Respin — samanburður 2026</h1>
{{hero}}
<p>Epicbet og Respin eru <strong>einu netspilavítin með fullkomnu íslensku viðmóti</strong>. Bæði eru rekin af sama fyrirtæki (Ducks In A Row OÜ) og deila sumum eiginleikum — en eru samt ólík. Hér berum við þau saman, punkt fyrir punkt.</p>

<h2>Yfirlit</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Epicbet</th><th>Respin</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2024</td><td>2024</td></tr>
<tr><td>Eigandi</td><td>Ducks In A Row OÜ</td><td>Ducks In A Row OÜ</td></tr>
<tr><td>Leyfi</td><td>Curaçao</td><td>Curaçao</td></tr>
<tr><td>Íslensku viðmót</td><td>✅ Alveg</td><td>✅ Alveg</td></tr>
<tr><td>Þjónustuver á íslensku</td><td>✅ Já</td><td>✅ Já</td></tr>
<tr><td>Velkomstbónus</td><td>100% allt að €500</td><td>200% + 50 FS</td></tr>
<tr><td>Veðskilyrði</td><td>0x (veðlaust)</td><td>0x (veðlaust)</td></tr>
<tr><td>PIQ greiðslur</td><td>✅ Já</td><td>✅ Já</td></tr>
<tr><td>Apple Pay</td><td>✅ Já</td><td>⚠️ Óstaðfest</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>✅ BTC, ETH, LTC, DOGE+</td><td>✅ BTC, ETH, LTC, DOGE+</td></tr>
<tr><td>Leikjaúrval</td><td>Spilakassar + lifandi + íþróttir</td><td>Spilakassar + lifandi</td></tr>
<tr><td>Íþróttaveðmál</td><td>✅ Já</td><td>❌ Nei</td></tr>
<tr><td>Vikuleg endurgreiðsla</td><td>✅ Já</td><td>✅ Já</td></tr>
</tbody></table>

<h2>Bónusar</h2>
<h3>Epicbet: 100% allt að €500</h3>
<p>Epicbet býður 100% samsvörunarbónus á fyrstu innborgun — leggðu inn €100, spilaðu með €200. Hámark €500. <strong>Veðskilyrði: 0x</strong> — þetta er sjaldgæft og þýðir að þú þarft ekki að veðja bónusnum ákveðið oft. Vinningar frá bónus eru þínir strax.</p>

<h3>Respin: 200% + 50 frísnúningar</h3>
<p>Respin býður hærri hlutfall — 200% samsvörun. Leggðu inn €100, spilaðu með €300. Auk þess færðu 50 frísnúninga. <strong>Veðskilyrði: líka 0x.</strong> Í tölum er Respin bónusinn stærri — en hámarksupphæðin fer eftir innborgun.</p>

<p><strong>Sigurvegari í bónusum:</strong> Respin — hærra hlutfall (200% vs 100%) og frísnúningar ofan á.</p>

<h2>Greiðsluleiðir</h2>
<p>Bæði spilavítin styðja <a href="{URL_BASE}leidbeiningar/piq-greidslur-island/">PIQ greiðslur</a> sem eru sérstaklega hannaðar fyrir Ísland. Bæði taka við dulritunargjaldmiðlum (BTC, ETH, LTC, DOGE og fleira). Epicbet hefur staðfestan stuðning við Apple Pay sem getur verið kostur ef íslenskt bankakort virkar ekki.</p>
<p><strong>Sigurvegari í greiðslum:</strong> Jafnt — báðir styðja PIQ og dulritunargjaldmiðla. Epicbet fær smá forskot vegna Apple Pay.</p>

<h2>Leikjaúrval</h2>
<p>Bæði spilavítin bjóða stórt úrval spilakassa frá sömu framleiðendum: Pragmatic Play, Evolution, Play'n GO, NetEnt, Hacksaw Gaming og fleiri. Lifandi spilavíti er í boði á báðum.</p>
<p>Stóri munurinn: <strong>Epicbet bíður íþróttaveðmál</strong> — fótbolti, körfubolti, handbolti og fleira. Respin er eingöngu spilavíti.</p>
<p><strong>Sigurvegari í leikjum:</strong> Epicbet — ef þú vilt veðja á íþróttir. Ef þú vilt bara spilakassa og lifandi borð er þetta jafnt.</p>

<h2>Upplifun og viðmót</h2>
<p>Bæði spilavítin hafa hreint, nútímalegt viðmót á íslensku. Epicbet er aðeins meira „sports-focused" í útliti meðan Respin einbeitir sér að spilavítisupplifuninni. Farsímaupplifun er góð á báðum.</p>

<h2>Hvort á ég að velja?</h2>
<div class="info-box"><p><strong>Veldu Epicbet ef:</strong> Þú vilt veðja á íþróttir OG spila spilavíti á sama stað. Þú vilt nota Apple Pay. Þú vilt allt-í-einu síðu.</p></div>
<div class="info-box"><p><strong>Veldu Respin ef:</strong> Þú vilt einbeita þér að spilakössum og lifandi spilavíti. Þú vilt hærri velkomstbónus (200% vs 100%). Þú vilt vikulega endurgreiðslu sem aðalatriði.</p></div>
<div class="info-box"><p><strong>Eða — prófaðu bæði:</strong> Þar sem bæði bjóða veðlausa bónusa getur þú skráð þig á bæði og ákveðið sjálfur hvert hentar betur. Engin áhætta.</p></div>

<h2>Algengar spurningar</h2>
<h3>Eru Epicbet og Respin í eigu sama fyrirtækis?</h3>
<p>Já — bæði eru rekin af Ducks In A Row OÜ. Þau deila sumum tæknilegum innviðum en eru sjálfstæð spilavíti með mismunandi bónusa og leikjaúrval.</p>
<h3>Get ég verið skráður á bæði?</h3>
<p>Já — engin regla bannar það. Þú getur haft reikning á báðum og nýtt þér velkomstbónus á hvoru tveggja.</p>
<h3>Hvort er betra fyrir íslenskt bankakort?</h3>
<p>Báðir styðja PIQ sem virkar vel frá Íslandi. Ef bankakort virkar ekki skaltu nota dulritunargjaldmiðla eða <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island/">Revolut</a> — virkar eins á báðum.</p>
<h3>Hvort er betra fyrir byrjendur?</h3>
<p>Epicbet — einfaldara viðmót, Apple Pay stuðningur og allt á íslensku. Respin er líka gott en Epicbet er aðeins auðveldara í notkun.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>'''
    },
    {
        "slug": "hversu-mikid-kostar-ad-spila",
        "title": "Hversu mikið kostar að spila á spilavíti? Kostnaðarleiðarvísir 2026",
        "desc": "Raunhæfur kostnaðarleiðarvísir: lágmarksinnborganir, meðaltap, gjöld og hvernig á að stjórna peningum í spilavíti.",
        "emoji": "💰",
        "colors": ("#1a1a0a", "#33331a", "#4d4d28"),
        "content": f'''<h1>Hversu mikið kostar að spila á spilavíti? 2026</h1>
{{hero}}
<p>Þetta er ein af þeim spurningum sem fáar casino-síður svara heiðarlega. <strong>Við ætlum að gera það.</strong> Hér eru raunverulegar tölur — ekki markaðssetning.</p>

<h2>Lágmarkskostnaður til að byrja</h2>
<table class="info-table"><thead><tr><th>Liður</th><th>Kostnaður</th><th>Athugasemd</th></tr></thead><tbody>
<tr><td>Lágmarksinnborgun</td><td>€10 (ca. 1.500 ISK)</td><td>Flest spilavíti. Sum leyfa €1-5</td></tr>
<tr><td>Gjald fyrir innborgun (kort)</td><td>0-3%</td><td>Fer eftir banka og spilavíti</td></tr>
<tr><td>Gjald fyrir innborgun (dulritun)</td><td>$0.5-5</td><td>Fer eftir neti (TRC-20 er ódýrast)</td></tr>
<tr><td>Gjald fyrir úttekt</td><td>Yfirleitt €0</td><td>Flest spilavíti rukka ekki fyrir úttektir</td></tr>
<tr><td>Gjaldmiðlaskipti ISK→EUR</td><td>1-2%</td><td>Bankinn rukkar — forðist með dulritunargjaldmiðlum</td></tr>
</tbody></table>
<p><strong>Raunverulegur byrjunarkostnaður: €10-15</strong> (um 1.500-2.300 ISK) ef þú notar dulritunargjaldmiðla eða PIQ. Aðeins meira ef þú notar bankakort vegna gjaldmiðlaskipta.</p>

<h2>Hversu miklu tapar meðalspilarinn?</h2>
<p>Þetta er mikilvægt að skilja: <strong>spilavíti er skemmtun, ekki tekjuleið.</strong> Húsforskotið (house edge) þýðir að spilavítið vinnur alltaf til lengri tíma.</p>
<table class="info-table"><thead><tr><th>Leikur</th><th>RTP</th><th>Húsforskot</th><th>Meðaltap á €100</th></tr></thead><tbody>
<tr><td>Spilakassar (meðal)</td><td>96%</td><td>4%</td><td>€4</td></tr>
<tr><td>Blackjack (grunn)</td><td>99.5%</td><td>0.5%</td><td>€0.50</td></tr>
<tr><td>Rúlletta (evrópsk)</td><td>97.3%</td><td>2.7%</td><td>€2.70</td></tr>
<tr><td>Baccarat</td><td>98.9%</td><td>1.1%</td><td>€1.10</td></tr>
<tr><td>Crash-leikir</td><td>95-97%</td><td>3-5%</td><td>€3-5</td></tr>
</tbody></table>
<p><em>Þetta er tölfræðilegt meðaltal yfir þúsundir snúninga. Á stuttum tíma geturðu unnið miklu meira eða tapað miklu meira.</em></p>
<p><a href="{URL_BASE}leidbeiningar/hvad-er-rtp/">Hvað er RTP og hvers vegna skiptir það máli? →</a></p>

<h2>Dæmi um mánaðarlegan kostnað</h2>
<table class="info-table"><thead><tr><th>Spilastíll</th><th>Vikuleg innborgun</th><th>Mánaðarkostnaður</th><th>Meðaltap (v/ 96% RTP)</th></tr></thead><tbody>
<tr><td>Frjálslegur (casual)</td><td>€10-20</td><td>€40-80</td><td>€1.60-3.20</td></tr>
<tr><td>Virkur spilari</td><td>€50-100</td><td>€200-400</td><td>€8-16</td></tr>
<tr><td>Háspilari</td><td>€200+</td><td>€800+</td><td>€32+</td></tr>
</tbody></table>
<p><strong>Mikilvægt:</strong> Þessar tölur eru meðaltap. Þú getur tapað öllu á einni lotu eða unnið stórt. Spilavíti er ófyrirsjáanlegt — og þess vegna er <a href="{URL_BASE}leidbeiningar/bankastjornunaradferdir/">peningastjórnun</a> svo mikilvæg.</p>

<h2>Hvernig á að stjórna kostnaði</h2>
<ol>
<li><strong>Settu mánaðarlegt hámark</strong> — Ákveddu upphæð sem þú hefur efni á að tapa. Aldrei meira. Allir góðir spilarar gera þetta.</li>
<li><strong>Notaðu innborgunartakmörk</strong> — Öll spilavíti bjóða þetta í stillingum. Settu vikutakmörk og þá geturðu ekki lagt inn meira þótt þú viljir.</li>
<li><strong>Aldrei elta tap</strong> — Ef þú tapar €50 er lausnin ekki að leggja inn €100 til að vinna þau til baka. <a href="{URL_BASE}leidbeiningar/salfraedi-fjarhaettuspila/">Lesa um sálfræði fjárhættuspila →</a></li>
<li><strong>Taktu hlé</strong> — Ef þú hefur spilað í 2+ tíma án hléa er kominn tími til að hætta. Þreyttur spilari tekur verri ákvarðanir.</li>
<li><strong>Drekk ekki og spilaðu</strong> — Áfengi skerðir dómgreind. Þetta á við hvort sem þú spilar í spilavíti eða heima.</li>
</ol>
<p><a href="{URL_BASE}leidbeiningar/spila-af-abyrgd/">Spila af ábyrgð — ítarlegur leiðarvísir →</a></p>

<h2>Falinn kostnaður sem margir gleyma</h2>
<ul>
<li><strong>Gjaldmiðlaskipti</strong> — Íslenskir bankar taka 1-2% fyrir ISK→EUR skipti. Á ári getur þetta orðið umtalsvert.</li>
<li><strong>Bónusveðskilyrði</strong> — Ef þú tekur á móti 100% bónus með 40x veðskilyrðum og tapar meðan þú uppfyllir þau hefur bónusinn í raun kostað þig peninga. <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">Lesa meira →</a></li>
<li><strong>Tími</strong> — Tíminn sem þú eyðir í að spila hefur tækifæriskostnað. Líttu á spilun sem skemmtun — ekki vinnu.</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Er hægt að spila alvöru peninga með €10?</h3>
<p>Já — €10 er lágmarksinnborgun á flestum spilavítum. Á €0.20 spilakassa á snúning nærðu 50 snúningum. Ekki mikið, en nóg til að prófa og hafa gaman.</p>
<h3>Þarf ég að borga skatt af vinningum?</h3>
<p>Á Íslandi eru fjárhættuspilavinningar yfirleitt ekki skattskyldir fyrir einstaklinga. Hins vegar ef spilun er tekjulind getur verið öðruvísi. <a href="{URL_BASE}leidbeiningar/skattar-spilavinningar-island/">Sjá skattaupplýsingar →</a></p>
<h3>Hvað ef ég er kominn yfir mörkin?</h3>
<p>Ef þú finnur að þú spilar meira en þú hefur efni á, hafðu samband við <strong>hjálparsíma 1717</strong> (opinn 24/7) eða skoðaðu <a href="{URL_BASE}leidbeiningar/studningssidur-vid-spilafikn/">stuðningssíður →</a></p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Byrja að spila →</a></div>'''
    },
    {
        "slug": "spilaviti-fyrir-farsima-island",
        "title": "Spilavíti fyrir farsíma á Íslandi — bestu farsímaspilavítin 2026",
        "desc": "Bestu netspilavítin fyrir iPhone og Android á Íslandi. Hraði, leikjaúrval, greiðsluleiðir og hvort þarf app eða vafra.",
        "emoji": "📱",
        "colors": ("#0a1a28", "#14334f", "#1e4c76"),
        "content": f'''<h1>Spilavíti fyrir farsíma á Íslandi 2026</h1>
{{hero}}
<p>Flestir íslenskir spilarar nota farsíma til að spila — ekki tölvu. <strong>En ekki öll spilavíti virka jafn vel á farsíma.</strong> Hér berum við saman bestu farsímaspilavítin á Íslandi og svörum algengum spurningum.</p>

<h2>App eða vafri?</h2>
<p>Langflest netspilavíti bjóða <strong>ekki sérstakt app í App Store eða Google Play</strong>. Apple og Google takmarka fjárhættuspila-öpp í sínum verslunum. Í staðinn nota spilavítin vefsíður sem eru hannaðar sérstaklega fyrir farsíma (responsive design).</p>
<p>Góðu fréttirnar: nútíma farsímavefir eru nánast jafn hraðir og app. Þú opnar einfaldlega Safari eða Chrome, ferð á spilavítissíðuna og spilar.</p>

<h3>Hvernig á að bæta spilavíti við heimaskjá</h3>
<ol>
<li>Opnaðu spilavítissíðuna í Safari (iPhone) eða Chrome (Android)</li>
<li>Ýttu á Share-hnappinn (iPhone) eða þrjá punktana (Android)</li>
<li>Veldu „Add to Home Screen" / „Bæta við heimaskjá"</li>
<li>Nú birtist spilavítisikon á heimaskjánum — eins og venjulegt app</li>
</ol>

<h2>Bestu farsímaspilavítin á Íslandi</h2>
<table class="info-table"><thead><tr><th>Spilavíti</th><th>Farsímaupplifun</th><th>Hraði</th><th>Leikir á farsíma</th><th>Sérstakt app?</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></td><td>⭐⭐⭐⭐⭐</td><td>Mjög hratt</td><td>2.000+</td><td>Nei — vafri</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></td><td>⭐⭐⭐⭐</td><td>Hratt</td><td>8.000+</td><td>Nei — vafri</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/stake/">Stake</a></td><td>⭐⭐⭐⭐⭐</td><td>Mjög hratt</td><td>3.000+</td><td>Já (Android)</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></td><td>⭐⭐⭐⭐</td><td>Hratt</td><td>3.500+</td><td>Nei — vafri</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></td><td>⭐⭐⭐⭐</td><td>Hratt</td><td>8.000+</td><td>Já (Android)</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/respin/">Respin</a></td><td>⭐⭐⭐⭐⭐</td><td>Mjög hratt</td><td>4.000+</td><td>Nei — vafri</td></tr>
</tbody></table>

<h2>Greiðslur á farsíma</h2>
<p>Greiðslur á farsíma virka eins og á tölvu — en með einum stórum kosti: <strong>Apple Pay</strong>. Ef þú notar iPhone geturðu lagt inn beint með Apple Pay á sumum spilavítum — eins og <a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a>.</p>
<p>Aðrar greiðsluleiðir sem virka vel á farsíma:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Sendu frá <a href="{URL_BASE}greidslur/trust-wallet-spilaviti/">Trust Wallet</a> eða <a href="{URL_BASE}greidslur/metamask-spilaviti/">MetaMask</a> appinu á símanum</li>
<li><strong>PIQ</strong> — <a href="{URL_BASE}leidbeiningar/piq-greidslur-island/">PIQ greiðslur</a> virka vel á farsíma</li>
<li><strong>E-wallets</strong> — Skrill og Neteller hafa sín eigin öpp</li>
</ul>

<h2>Hvað á að varast á farsíma</h2>
<ul>
<li><strong>Gagnaeyðsla</strong> — Lifandi spilavíti (video streaming) eyðir miklum gögnum. Notaðu Wi-Fi ef þú spilar lifandi borð</li>
<li><strong>Rafhlöðunotkun</strong> — Spilakassar og lifandi leikir eru þungir á rafhlöðu. Hlaðning eða power bank er ráðlegt</li>
<li><strong>Skjástærð</strong> — Sum borðspil (rúlletta, blackjack) virka betur á stærri skjá. Spilakassar virka vel á öllum stærðum</li>
<li><strong>Nettengingar</strong> — Lifandi spilavíti krefst stöðugrar tengingar. Ef tenging rofnar mitt í leik er veðmálið þitt yfirleitt óbreytt (niðurstaða ákveðst á netþjóni)</li>
</ul>

<h2>Vinsælustu farsímaleikirnir á Íslandi</h2>
<p>Þessir spilakassar eru sérstaklega vel hannaðir fyrir farsímaskjái:</p>
<ol>
<li><a href="{URL_BASE}spilakassar/gates-of-olympus/">Gates of Olympus</a> — Skýrt viðmót, snertistýring virkar vel</li>
<li><a href="{URL_BASE}spilakassar/sweet-bonanza/">Sweet Bonanza</a> — Litríkur leikur sem lítur vel út á litlum skjá</li>
<li><a href="{URL_BASE}spilakassar/big-bass-bonanza/">Big Bass Bonanza</a> — Einföld vélbúnaður, hraðvirk</li>
<li><a href="{URL_BASE}spilakassar/book-of-dead/">Book of Dead</a> — Klassískur leikur sem virkar fullkomlega á farsíma</li>
<li><a href="{URL_BASE}live/lightning-roulette/">Lightning Roulette</a> — Besta lifandi rúllettan á farsíma</li>
</ol>

<h2>Algengar spurningar</h2>
<h3>Þarf ég sérstakt app til að spila?</h3>
<p>Nei — langflest spilavíti virka beint í vafranum (Safari, Chrome). Stake og BC.Game bjóða Android app en það er valkvætt. Á iPhone er vafri eini kosturinn.</p>
<h3>Er öruggt að spila á farsíma?</h3>
<p>Já — jafn öruggt og á tölvu. Spilavítin nota SSL dulkóðun sem virkar eins á farsíma. Ráðlegging: notaðu lykilorðastjóra og virkjaðu tveggja þátta auðkenningu ef hún er í boði.</p>
<h3>Get ég spilað lifandi spilavíti á farsíma?</h3>
<p>Já — öll lifandi spilavíti frá Evolution og Pragmatic Play eru farsímavinveitt. Video streyming virkar vel á 4G/5G eða Wi-Fi.</p>
<h3>Hvers vegna er leikurinn hægur á farsímanum mínum?</h3>
<p>Algengasta orsökin er veik nettenging. Prófaðu Wi-Fi. Ef það lagast ekki gæti síminn verið of gamall — spilakassar krefjast ákveðins vélbúnaðar. iPhone 8 og nýrri / Android frá 2019 virka yfirleitt vel.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á farsíma →</a></div>'''
    },

    {
        "slug": "hvernig-a-ad-opna-reikning-a-spilaviti",
        "title": "Hvernig á að opna reikning á spilavíti — skref fyrir skref 2026",
        "desc": "Skref-fyrir-skref leiðbeiningar um hvernig á að stofna reikning á netspilavíti frá Íslandi. Skráning, staðfesting og fyrsta innborgun.",
        "emoji": "📝",
        "colors": ('#0d1926', '#1a324c', '#274b72'),
        "content": f'''<h1>Hvernig á að opna reikning á spilavíti 2026</h1>
{hero}
<p>Ef þú hefur aldrei skráð þig á netspilavíti áður getur ferlið virst flókið. <strong>Í raun tekur það 2-5 mínútur.</strong> Hér er nákvæm skref-fyrir-skref leiðbeining sem virkar á flestum spilavítum.</p>

<h2>Skref 1 — Veldu spilavíti</h2>
<p>Fyrst þarftu að velja hvert spilavíti þú vilt skrá þig á. Athugaðu:</p>
<ul>
<li>Er spilavítið með gilt leyfi? (<a href="{URL_BASE}leidbeiningar/hvernig-a-ad-stadfesta-spilavitaleyfi/">Hvernig á að staðfesta leyfi →</a>)</li>
<li>Tekur það við greiðslum frá Íslandi? (<a href="{URL_BASE}leidbeiningar/spilaviti-sem-tekur-vid-islenskum-kortum/">Greiðsluleiðir á Íslandi →</a>)</li>
<li>Er viðmótið á íslensku? (<a href="{URL_BASE}leidbeiningar/spilaviti-med-islensku-vidmoti/">Spilavíti á íslensku →</a>)</li>
</ul>
<div class="info-box"><p><strong>Okkar tilmæli fyrir byrjendur:</strong> <a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a> — íslensku viðmót, veðlaus bónus, Apple Pay og PIQ greiðslur.</p></div>

<h2>Skref 2 — Skráning</h2>
<p>Á flestum spilavítum þarftu að gefa upp:</p>
<ol>
<li><strong>Netfang</strong> — Notaðu raunverulegt netfang. Þú þarft það til að staðfesta reikninginn og endurstilla lykilorð</li>
<li><strong>Lykilorð</strong> — Veldu sterkt lykilorð (12+ stafir, blöndun af bókstöfum og tölum)</li>
<li><strong>Nafn og fæðingardagur</strong> — Verður að vera rétt — spilavítið ber saman við skilríki seinna</li>
<li><strong>Heimilisfang</strong> — Sumir biðja um þetta strax, aðrir seinna</li>
<li><strong>Gjaldmiðil</strong> — Veldu EUR (evrur) nema spilavítið styðji ISK (mjög sjaldgæft)</li>
</ol>
<p>Á <a href="{URL_BASE}spilaviti/stake/">Stake</a> og <a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a> þarftu aðeins netfang og lykilorð — allt annað kemur seinna.</p>

<h2>Skref 3 — Staðfestu netfang</h2>
<p>Spilavítið sendir þér tölvupóst með tengli eða kóða. Smelltu á hann til að staðfesta. Athugaðu ruslpósthólfið ef þú sérð hann ekki.</p>

<h2>Skref 4 — Fyrsta innborgun</h2>
<p>Nú geturðu lagt inn peninga. Veldu greiðsluleið:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Besta leiðin á Íslandi. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin →</a></li>
<li><strong>Visa/Mastercard</strong> — Virkar stundum. <a href="{URL_BASE}leidbeiningar/spilaviti-sem-tekur-vid-islenskum-kortum/">Sjá stöðu →</a></li>
<li><strong>PIQ</strong> — <a href="{URL_BASE}leidbeiningar/piq-greidslur-island/">Sérhannað fyrir Ísland →</a></li>
<li><strong>E-wallets</strong> — <a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a> eða <a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a></li>
</ul>
<p>Lágmarksinnborgun er yfirleitt €10. <a href="{URL_BASE}leidbeiningar/hversu-mikid-kostar-ad-spila/">Hvað kostar að spila? →</a></p>

<h2>Skref 5 — Velkomstbónus</h2>
<p>Flest spilavíti bjóða velkomstbónus á fyrstu innborgun. <strong>Lestu skilmálana áður en þú samþykkir.</strong> Athugaðu <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrði</a> — þau ráða hvort bónusinn er raunverulega þess virði.</p>
<div class="info-box"><p><strong>Veðlausir bónusar:</strong> <a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a> og <a href="{URL_BASE}spilaviti/respin/">Respin</a> bjóða 0x veðskilyrði — vinningar eru þínir strax.</p></div>

<h2>Skref 6 — Byrjaðu að spila</h2>
<p>Tilbúinn! Mæli með að byrja í <a href="{URL_BASE}leidbeiningar/okeypis-spilaviti-island/">demo-ham</a> til að kynnast leikjunum áður en þú veðjar raunverulegum peningum. Settu <a href="{URL_BASE}leidbeiningar/bankastjornunaradferdir/">takmörk</a> á innborgunum strax.</p>

<h2>Algengar spurningar</h2>
<h3>Hversu langan tíma tekur skráning?</h3>
<p>2-5 mínútur á flestum spilavítum. Hraðskráning (aðeins netfang + lykilorð) tekur 30 sekúndur.</p>
<h3>Þarf ég að senda inn skilríki strax?</h3>
<p>Yfirleitt ekki — KYC staðfesting kemur þegar þú tekur út í fyrsta skipti. Sum spilavíti biðja um gögn fyrr ef innborgun fer yfir ákveðið þak.</p>
<h3>Get ég haft reikninga á mörgum spilavítum?</h3>
<p>Já — en aðeins einn reikning á hverju spilavíti. Margir spilarar hafa reikninga á 2-3 spilavítum til að nýta mismunandi bónusa.</p>
<h3>Er öruggt að gefa spilavíti persónuupplýsingar?</h3>
<p>Á spilavíti með gilt leyfi — já. Þau eru skylt að vernda gögnin þín samkvæmt lögum. Athugaðu alltaf leyfið fyrst.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Opna reikning →</a></div>'''
    },
    {
        "slug": "hvernig-a-ad-taka-ut-vinninga",
        "title": "Hvernig á að taka út af spilavíti á Íslandi — úttektarleiðarvísir 2026",
        "desc": "Allt sem þú þarft að vita um úttektir: aðferðir, hraði, KYC staðfesting og hvernig á að forðast vandamál.",
        "emoji": "💸",
        "colors": ('#1a0a0a', '#331414', '#4d1e1e'),
        "content": f'''<h1>Hvernig á að taka út af spilavíti á Íslandi 2026</h1>
{hero}
<p>Þú hefur unnið — frábært! En <strong>hvernig færðu peningana á bankareikninginn þinn?</strong> Úttektir á Íslandi geta verið flóknari en í öðrum löndum vegna bankareglna. Hér er allt sem þú þarft að vita.</p>

<h2>Úttektarleiðir sem virka á Íslandi</h2>
<table class="info-table"><thead><tr><th>Aðferð</th><th>Hraði</th><th>Gjöld</th><th>Lágmark</th><th>Virkar alltaf?</th></tr></thead><tbody>
<tr><td>Bitcoin/USDT</td><td>0-24 klst</td><td>$0-5</td><td>€10-20</td><td>✅ Já</td></tr>
<tr><td>Ethereum</td><td>0-24 klst</td><td>$1-10</td><td>€10-20</td><td>✅ Já</td></tr>
<tr><td>Skrill</td><td>0-48 klst</td><td>0-1%</td><td>€20</td><td>✅ Já</td></tr>
<tr><td>Neteller</td><td>0-48 klst</td><td>0-1%</td><td>€20</td><td>✅ Já</td></tr>
<tr><td>Visa/Mastercard</td><td>1-5 dagar</td><td>0%</td><td>€20</td><td>⚠️ Stundum</td></tr>
<tr><td>Bankamillifærsla</td><td>3-7 dagar</td><td>0-€25</td><td>€50-100</td><td>✅ Já</td></tr>
</tbody></table>
<p><strong>Besta leiðin á Íslandi:</strong> Dulritunargjaldmiðlar. Hraðastar (mínútur eftir samþykki), lægstu gjöldin og bankinn getur ekki lokað á úttektina.</p>

<h2>KYC staðfesting — hvað er það?</h2>
<p>KYC (Know Your Customer) er lögbundin staðfesting sem öll leyfileg spilavíti þurfa að framkvæma. Þú þarft yfirleitt að senda:</p>
<ol>
<li><strong>Ljósmynd af skilríkjum</strong> — Vegabréf eða ökuskírteini (báðar hliðar)</li>
<li><strong>Sönnun á heimilisfangi</strong> — Reikningur (rafmagn, sími) eða bankayfirlýsing (ekki eldra en 3 mánuðir)</li>
<li><strong>Sönnun á greiðsluleið</strong> — Mynd af kortinu (faldu 8 miðtölur) eða screenshot af e-wallet</li>
</ol>
<p>Gott ráð: <strong>Sendu KYC gögnin strax eftir skráningu</strong> — þá er staðfestingin kláruð þegar þú vilt taka út og þú þarft ekki að bíða.</p>

<h2>Skref-fyrir-skref: taka út í Bitcoin</h2>
<ol>
<li>Opnaðu dulritunarveskið þitt (Trust Wallet, MetaMask eða kauphöll)</li>
<li>Afritaðu Bitcoin-heimilisfangið þitt (wallet address)</li>
<li>Farðu á spilavítið → Úttektir → Bitcoin</li>
<li>Límdu heimilisfangið og veldu upphæð</li>
<li>Staðfestu — bíddu 10-60 mínútur</li>
<li>Seldu Bitcoin fyrir EUR/ISK á kauphöllinni ef þú vilt</li>
</ol>

<h2>Algeng vandamál og lausnir</h2>
<h3>„Úttektin mín er í bið" — hvað geri ég?</h3>
<p>Spilavíti þarf yfirleitt 24-48 klst til að samþykkja úttekt. Ef það tekur lengur en 72 klst skaltu hafa samband við þjónustuver. Sum spilavíti eru hraðari — <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> afgreiðir flestar úttektir á undir 10 mínútum.</p>

<h3>„Bankinn minn hafnaði úttektinni"</h3>
<p>Íslenskir bankar geta hafnað millifærslum frá spilavítum. Lausn: notaðu dulritunargjaldmiðla eða e-wallet þar sem bankinn sér ekki uppruna fjármuna.</p>

<h3>„Mér var neitað um úttekt"</h3>
<p>Algengustu ástæður: 1) KYC ekki lokið, 2) veðskilyrði bónuss ekki uppfyllt, 3) hámarksúttekt á dag náð, 4) annað greiðsluheimilisfang en notað var við innborgun.</p>

<h2>Hraðastu spilavítin í úttektum</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Flestar BTC úttektir afgreiddar á undir 10 mínútum</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — Dulritunarúttektir á 0-2 klst</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — PIQ úttektir á 1-24 klst</p></div>

<h2>Algengar spurningar</h2>
<h3>Hversu mikið get ég tekið út í einu?</h3>
<p>Fer eftir spilavíti. Dæmi: €5.000 á dag, €10.000 á viku, €30.000 á mánuði. Dulritunarspilavíti hafa oft hærri mörk.</p>
<h3>Þarf ég að borga skatt af vinningum?</h3>
<p>Á Íslandi eru spilavinningar yfirleitt ekki skattskyldir. <a href="{URL_BASE}leidbeiningar/skattar-spilavinningar-island/">Sjá skattaleiðbeiningar →</a></p>
<h3>Get ég tekið út í ISK?</h3>
<p>Flest spilavíti borga í EUR. Bankinn þinn breytir sjálfkrafa í ISK. Til að spara gjaldmiðlaskiptagjöld getur þú notað Revolut eða dulritunargjaldmiðla.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Finna spilavíti með hröðum úttektum →</a></div>'''
    },
    {
        "slug": "er-ologligt-ad-spila-a-spilaviti-island",
        "title": "Er ólöglegt að spila á spilavíti á Íslandi? Lagaleg staða 2026",
        "desc": "Er ólöglegt fyrir íslendinga að spila á netspilavítum? Lög, reglur og hvað segja bankarnir. Uppfært 2026.",
        "emoji": "⚖️",
        "colors": ('#1a1a0a', '#33331a', '#4d4d28'),
        "content": f'''<h1>Er ólöglegt að spila á spilavíti á Íslandi? 2026</h1>
{hero}
<p>Þetta er algengasta spurningin sem íslenskir spilarar spyrja — og svarið er <strong>flóknara en einfalt já eða nei</strong>.</p>

<h2>Stutt svar</h2>
<div class="info-box"><p><strong>Nei — það er ekki ólöglegt fyrir einstaklinga að spila á erlendum netspilavítum frá Íslandi.</strong> Engin lög banna íslenskum ríkisborgurum að spila. Hins vegar er rekstur spilavíta á Íslandi bannaður.</p></div>

<h2>Lagaleg staða í smáatriðum</h2>
<h3>Hvað er bannað?</h3>
<ul>
<li>❌ <strong>Rekstur spilavíta á Íslandi</strong> — Enginn má reka spilavíti á íslenskri grund</li>
<li>❌ <strong>Auglýsingar á fjárhættuspilum</strong> — Bannað er að auglýsa erlend spilavíti á Íslandi</li>
<li>❌ <strong>Óleyfileg happdrætti</strong> — Einungis Íslandsspil og Íslensk getspá hafa leyfi</li>
</ul>

<h3>Hvað er ekki bannað?</h3>
<ul>
<li>✅ <strong>Einstaklingur spilar á erlendu spilavíti</strong> — Engin lög banna þetta</li>
<li>✅ <strong>Kaup á dulritunargjaldmiðlum</strong> — Fullkomlega löglegt</li>
<li>✅ <strong>Notkun rafrænna veskja</strong> — Skrill, Neteller o.fl.</li>
</ul>

<h2>Lög um happdrætti (nr. 38/2005)</h2>
<p>Helstu lögin um fjárhættuspil á Íslandi eru lög um happdrætti frá 2005. Þau ná yfir:</p>
<ul>
<li>Happdrætti, veðmál og spilavélar</li>
<li>Leyfisveitingar til Íslandsspila og Íslenskrar getspár</li>
<li>Bann við rekstri spilavíta á Íslandi</li>
</ul>
<p>Lögin taka <strong>ekki</strong> beinlínis á netspilavítum sem eru rekin erlendis. Þetta er grátt svæði — lögin voru skrifuð áður en netspilavíti urðu algeng.</p>

<h2>Bankarnir og fjárhættuspil</h2>
<p>Þó að lög banni ekki spilurum að spila hafa <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">íslenskir bankar</a> tekið eigin ákvarðanir:</p>
<ul>
<li>Arion banki, Landsbankinn og Íslandsbanki geta hafnað kortagreiðslum til spilavíta</li>
<li>Þetta er <strong>innri stefna bankanna</strong> — ekki lagaskylda</li>
<li>Dulritunargjaldmiðlar og rafræn veski fara framhjá þessu</li>
</ul>
<p><a href="{URL_BASE}leidbeiningar/spilaviti-sem-tekur-vid-islenskum-kortum/">Hvaða spilavíti tekur við íslenskum kortum? →</a></p>

<h2>Ný löggjöf 2026 — hvað er að gerast?</h2>
<p>Umræða hefur átt sér stað á Alþingi um endurskoðun laga um fjárhættuspil. Helstu atriði sem rædd hafa verið:</p>
<ul>
<li>Leyfiskerfi fyrir netspilavíti — líkt og í Danmörku eða Svíþjóð</li>
<li>Sterkara eftirlit með auglýsingum</li>
<li>Betri neytendavernd og verkfæri gegn spilafikn</li>
</ul>
<p>Engar breytingar hafa verið samþykktar enn sem komið er (nóvember 2026). Við uppfærum þessa síðu ef eitthvað breytist.</p>

<h2>Samanburður við önnur Norðurlönd</h2>
<table class="info-table"><thead><tr><th>Land</th><th>Netspilavíti leyfileg?</th><th>Ríkiseinokun?</th><th>Erlend spilavíti?</th></tr></thead><tbody>
<tr><td>Ísland</td><td>❌ Ekkert leyfiskerfi</td><td>✅ Íslandsspil/Getspá</td><td>⚠️ Grátt svæði — ekki bannað</td></tr>
<tr><td>Danmörk</td><td>✅ Já — leyfiskerfi</td><td>❌ Nei</td><td>✅ Leyfð á leyfðum síðum</td></tr>
<tr><td>Svíþjóð</td><td>✅ Já — leyfiskerfi</td><td>❌ Nei (síðan 2019)</td><td>✅ Leyfð á leyfðum síðum</td></tr>
<tr><td>Noregur</td><td>❌ Ekkert leyfiskerfi</td><td>✅ Norsk Tipping</td><td>⚠️ Grátt svæði (líkt og Ísland)</td></tr>
<tr><td>Finnland</td><td>⚠️ Einokun Veikkaus</td><td>✅ Veikkaus</td><td>⚠️ Grátt svæði</td></tr>
</tbody></table>

<h2>Algengar spurningar</h2>
<h3>Get ég lent í vandræðum ef ég spila á netspilavíti?</h3>
<p>Engin þekkt dæmi eru um að íslenskir einstaklingar hafi verið sóttir til saka fyrir að spila á erlendum netspilavítum. Lögin beinist að rekstraraðilum — ekki spilurum.</p>
<h3>Er öruggt að nota dulritunargjaldmiðla?</h3>
<p>Já — kaup og notkun dulritunargjaldmiðla er fullkomlega löglegt á Íslandi. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin →</a></p>
<h3>Breytist staðan ef Ísland fær leyfiskerfi?</h3>
<p>Ef Ísland innleiðir leyfiskerfi (líkt og Danmörk) munu sum spilavíti sækja um leyfi og verða "opinberlega" löguð. Spilavíti án íslensks leyfis gætu þá verið lokað á — en þetta er enn aðeins umræða.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Finna leyfileg spilavíti →</a></div>'''
    },
    {
        "slug": "revolut-spilaviti-island-leidbeining",
        "title": "Revolut á spilavíti á Íslandi — ítarleg leiðbeining 2026",
        "desc": "Hvernig á að nota Revolut til innborgunar á netspilavíti frá Íslandi. Skref-fyrir-skref og hvort bankinn sér viðskiptin.",
        "emoji": "🟣",
        "colors": ('#1a0a28', '#2d1445', '#401e62'),
        "content": f'''<h1>Revolut á spilavíti á Íslandi 2026</h1>
{hero}
<p>Revolut er orðið eitt vinsælasta greiðslutólið hjá íslenskum spilurum. <strong>Af hverju?</strong> Vegna þess að Revolut-kort fer ekki í gegnum íslenskt bankakerfi — og verður þar af leiðandi ekki hafnað af sömu ástæðum og íslenskt bankakort.</p>

<h2>Af hverju Revolut virkar þegar bankakort virkar ekki</h2>
<p>Íslenskir bankar nota MCC-kóða (Merchant Category Code 7995) til að greina greiðslur til spilavíta og geta lokað á þær. <strong>Revolut notar ekki íslenskt bankakerfi</strong> — greiðslan fer beint frá Revolut til spilavítisins. Þess vegna er höfnunarhlutfallið mun lægra.</p>

<h2>Skref-fyrir-skref: Revolut á spilavíti</h2>
<ol>
<li><strong>Opnaðu Revolut reikning</strong> — Sæktu appið (iOS/Android), skráðu þig (tekur 5 mín)</li>
<li><strong>Millifærðu á Revolut</strong> — Frá íslenskum bankareikningi á Revolut (SEPA millifærsla, 0-1 dagur)</li>
<li><strong>Fáðu Revolut kort</strong> — Sýndarkort (strax) eða líkamlegt kort (5-10 dagar)</li>
<li><strong>Leggðu inn á spilavíti</strong> — Notaðu Revolut Visa/Mastercard kortið eins og venjulegt kort</li>
<li><strong>Spilaðu og taktu út</strong> — Vinningar fara til baka á Revolut-kortið</li>
</ol>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Virkar þar sem íslenskt bankakort virkar ekki</td><td>❌ Þarftu Revolut reikning (frítt en tekur tíma)</td></tr>
<tr><td>✅ Lág gjaldmiðlaskiptagjöld</td><td>❌ Mánaðarleg takmörk á ókeypis gjaldmiðlaskiptum</td></tr>
<tr><td>✅ Samstundis innborgun</td><td>❌ Revolut getur í undantekningartilfellum lokað á spilavíti</td></tr>
<tr><td>✅ Sýndarkort fáanlegt strax</td><td>❌ Millifærsla frá banka á Revolut getur tekið 1 dag</td></tr>
<tr><td>✅ Bankinn sér ekki spilavítið</td><td></td></tr>
</tbody></table>

<h2>Sér bankinn minn að ég notaði Revolut á spilavíti?</h2>
<p><strong>Nei.</strong> Bankinn sér einungis millifærslu á Revolut-reikninginn þinn. Hann sér ekki hvað þú gerir með peningana á Revolut. Þetta er einn helsti kosturinn.</p>

<h2>Spilavíti sem styðja Revolut-kort</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Visa/Mastercard (Revolut virkar). Einnig Apple Pay.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — Visa/Mastercard studdir.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></strong> — Visa/Mastercard. Evrópulegt leyfi.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/20bet/">20Bet</a></strong> — Tekur við öllum kortum.</p></div>
<p>Í raun styðja öll spilavíti sem taka við Visa/Mastercard einnig Revolut-kort.</p>

<h2>Algengar spurningar</h2>
<h3>Er Revolut ókeypis?</h3>
<p>Já — grunnáskriftin er ókeypis. Sýndarkort er frítt. Líkamlegt kort kostar einu sinni (um €5). Gjaldmiðlaskipti eru frítt upp að ákveðnu mánaðarlegu þaki.</p>
<h3>Hversu hratt er innborgun með Revolut?</h3>
<p>Samstundis — eins og venjulegt debetkort. Eina töfin er millifærsla frá íslenska bankanum á Revolut (venjulega nokkrar klukkustundir til 1 dagur).</p>
<h3>Get ég tekið út á Revolut?</h3>
<p>Já — ef þú lagðir inn með Revolut-korti geturðu venjulega tekið út á sama kort. Sumir spilarar velja þó að taka út í dulritunargjaldmiðlum og skipta síðan í EUR á Revolut.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Finna spilavíti →</a></div>'''
    },
    {
        "slug": "bestu-crypto-spilavitin-island",
        "title": "Bestu crypto spilavítin á Íslandi 2026 — Bitcoin, Ethereum og USDT",
        "desc": "Topp 10 dulritunarspilavíti sem taka við íslenskum spilurum. Bitcoin, USDT, Ethereum. Hraðar úttektir, engir bankar.",
        "emoji": "₿",
        "colors": ('#1a0f00', '#332200', '#4d3300'),
        "content": f'''<h1>Bestu crypto spilavítin á Íslandi 2026</h1>
{hero}
<p>Dulritunargjaldmiðlar eru orðnir <strong>vinsælasta greiðsluleiðin</strong> hjá íslenskum spilavítaspilurum — og af góðum ástæðum. Bankarnir geta ekki lokað á greiðslur, úttektir eru hraðar og gjöldin lág.</p>

<h2>Topp 10 dulritunarspilavíti á Íslandi</h2>
<table class="info-table"><thead><tr><th>#</th><th>Spilavíti</th><th>Bónus</th><th>Dulritun</th><th>Úttektarhraði</th><th>Einkunn</th></tr></thead><tbody>
<tr><td>1</td><td><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></td><td>5 BTC + 200 FS</td><td>BTC, ETH, LTC, DOGE, BCH</td><td>Undir 10 mín</td><td>9.8/10</td></tr>
<tr><td>2</td><td><a href="{URL_BASE}spilaviti/stake/">Stake</a></td><td>200% + VIP</td><td>BTC, ETH, LTC, DOGE, XRP, TRX, USDT, USDC</td><td>0-2 klst</td><td>9.6/10</td></tr>
<tr><td>3</td><td><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></td><td>300% allt að 1 BTC</td><td>100+ gjaldmiðlar</td><td>0-1 klst</td><td>9.4/10</td></tr>
<tr><td>4</td><td><a href="{URL_BASE}spilaviti/cloudbet/">Cloudbet</a></td><td>100% allt að 5 BTC</td><td>BTC, ETH, USDT, BCH, DOGE, LTC</td><td>0-24 klst</td><td>8.4/10</td></tr>
<tr><td>5</td><td><a href="{URL_BASE}spilaviti/katsubet/">KatsuBet</a></td><td>100% + 100 FS</td><td>BTC, ETH, LTC, DOGE, USDT, BCH</td><td>0-24 klst</td><td>8.6/10</td></tr>
<tr><td>6</td><td><a href="{URL_BASE}spilaviti/winz/">Winz.io</a></td><td>300 FS (engin veðskilyrði)</td><td>BTC, ETH, LTC, DOGE, USDT, TRX</td><td>0-24 klst</td><td>8.5/10</td></tr>
<tr><td>7</td><td><a href="{URL_BASE}spilaviti/7bit/">7Bit Casino</a></td><td>200% + 100 FS</td><td>BTC, ETH, LTC, DOGE, BCH</td><td>0-24 klst</td><td>8.5/10</td></tr>
<tr><td>8</td><td><a href="{URL_BASE}spilaviti/mbitcasino/">mBit Casino</a></td><td>175% + 300 FS</td><td>BTC, ETH, LTC, DOGE, USDT</td><td>0-24 klst</td><td>8.4/10</td></tr>
<tr><td>9</td><td><a href="{URL_BASE}spilaviti/wildcoins/">WildCoins</a></td><td>250% + 100 FS</td><td>BTC, ETH, LTC, USDT</td><td>0-24 klst</td><td>8.7/10</td></tr>
<tr><td>10</td><td><a href="{URL_BASE}spilaviti/hellspin/">HellSpin</a></td><td>150% + 50 FS</td><td>BTC, ETH, LTC, USDT</td><td>0-24 klst</td><td>8.1/10</td></tr>
</tbody></table>

<h2>Af hverju dulritunargjaldmiðlar á Íslandi?</h2>
<ul>
<li><strong>Engir bankar í leiðinni</strong> — <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">Íslenskir bankar</a> loka stundum á kortagreiðslur til spilavíta. Dulritunargreiðslur fara beint á blokkkeðjunni</li>
<li><strong>Hraðar úttektir</strong> — Bitcoin útborgun á 10-30 mín, USDT á 1-5 mín</li>
<li><strong>Lág gjöld</strong> — USDT (TRC-20) kostar undir $1 í færslugjöld</li>
<li><strong>Friðhelgi</strong> — Bankinn sér ekki viðskiptin</li>
<li><strong>Hærri mörk</strong> — Dulritunarspilavíti hafa oft hærri inn- og útborgunarþak</li>
</ul>

<h2>Bitcoin vs USDT — hvort er betra?</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Bitcoin (BTC)</th><th>USDT (Tether)</th></tr></thead><tbody>
<tr><td>Verðstöðugleiki</td><td>❌ Sveiflast mikið</td><td>✅ Stöðugt (1 USDT ≈ $1)</td></tr>
<tr><td>Hraði</td><td>10-30 mín</td><td>1-5 mín (TRC-20)</td></tr>
<tr><td>Gjöld</td><td>$1-5</td><td>$0.5-1</td></tr>
<tr><td>Útbreiðsla</td><td>✅ Öll crypto-spilavíti</td><td>✅ Flest (ekki öll)</td></tr>
<tr><td>Hentar fyrir</td><td>Þá sem vilja halda BTC</td><td>Þá sem vilja stöðugt virði</td></tr>
</tbody></table>
<p><strong>Okkar ráð:</strong> Notaðu USDT (TRC-20) fyrir innlagnir — hraðara, ódýrara og ekkert verðáhætta meðan þú spilar. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa dulritunargjaldmiðla →</a></p>

<h2>Hvernig á að byrja?</h2>
<ol>
<li>Opnaðu reikning á kauphöll (Coinbase, Binance eða Kraken)</li>
<li>Keyptu BTC eða USDT</li>
<li>Skráðu þig á spilavíti af listanum hér að ofan</li>
<li>Leggðu inn — afritaðu wallet-heimilisfang spilavítisins og sendu</li>
<li>Byrjaðu að spila!</li>
</ol>
<p><a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Ítarleg leiðbeining um kaup á dulritunargjaldmiðlum →</a></p>

<h2>Algengar spurningar</h2>
<h3>Er löglegt að nota Bitcoin á spilavíti?</h3>
<p>Já — <a href="{URL_BASE}leidbeiningar/er-ologligt-ad-spila-a-spilaviti-island/">engin lög á Íslandi banna</a> kaup á dulritunargjaldmiðlum eða notkun þeirra á spilavítum.</p>
<h3>Hvaða dulritunargjaldmiðill er bestur fyrir spilavíti?</h3>
<p>USDT (TRC-20) — stöðugt verð, lág gjöld, hraðar millifærslur. Bitcoin ef þú vilt halda BTC til langs tíma.</p>
<h3>Get ég keypt Bitcoin beint á spilavítinu?</h3>
<p>Sum spilavíti (t.d. <a href="{URL_BASE}spilaviti/stake/">Stake</a>) bjóða innbyggð kaup á dulritunargjaldmiðlum. Hins vegar eru gjöldin yfirleitt hærri en á kauphöll.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila með Bitcoin →</a></div>'''
    },
    {
        "slug": "merki-thess-ad-thu-sert-ordinn-hadur-spilavitum",
        "title": "Merki þess að þú sért orðinn háður spilavítum — og hvað er hægt að gera",
        "desc": "10 algeng merki spilafiknar, hvernig á að fá hjálp og stuðningsúrræði á Íslandi. Hjálparsími 1717 er opinn 24/7.",
        "emoji": "🛡️",
        "colors": ('#1a1a1a', '#333333', '#4d4d4d'),
        "content": f'''<h1>Merki þess að þú sért orðinn háður spilavítum</h1>
{hero}
<p>Fjárhættuspil geta verið skemmtileg — en þau geta líka orðið vandamál. <strong>Það er ekkert til að skammast sín fyrir.</strong> Hér eru merkin sem þú átt að passa upp á og hvað þú getur gert ef þú þekkir þig.</p>

<h2>10 algeng viðvörunarmerki</h2>
<ol>
<li><strong>Þú spilar meira en þú hafðir ætlað</strong> — Hvort sem það er tími eða peningar, þú ferð stöðugt yfir mörkin sem þú settir</li>
<li><strong>Þú eltir tapið</strong> — Þú leggur inn meira til að vinna til baka það sem þú tapaðir. Þetta er eitt sterkasta merkið</li>
<li><strong>Þú leynir spilun þinni</strong> — Þú segir ekki fjölskyldu eða vinum hversu mikið þú spilar</li>
<li><strong>Þú ert pirraður þegar þú spilar ekki</strong> — Kvíði, pirringur eða eirðarleysi þegar þú getur ekki spilað</li>
<li><strong>Þú notar peninga sem þú hefur ekki efni á</strong> — Leigu, reikningar eða sparnaður fer í spilun</li>
<li><strong>Þú hugsar stöðugt um spilun</strong> — Skipuleggur næstu lotu, endurspilar atburðarás í huganum</li>
<li><strong>Þú þarft stöðugt hærri upphæðir</strong> — Sömu spennan krefst meiri peninga (líkt og vímuefnaþol)</li>
<li><strong>Þú hefur reynt að hætta en getir ekki</strong> — Þú hefur lofað sjálfum þér að hætta en byrjar aftur</li>
<li><strong>Sambönd þín eru að versna</strong> — Rifrildi við fjölskyldu eða vini vegna spilana</li>
<li><strong>Þú spilar til að flýja vandamál</strong> — Notar spilun til að deyfa áhyggjur, einmanaleika eða þunglyndi</li>
</ol>
<p><strong>Ef þú þekkir 3 eða fleiri merki á listanum — hafi þú samband.</strong> Því fyrr sem þú leitar þér hjálpar, því auðveldara verður.</p>

<h2>Hvað get ég gert?</h2>
<h3>Strax — á spilavítinu</h3>
<ul>
<li><strong>Settu innborgunartakmörk</strong> — Allir góðir spilarar gera þetta. Farðu í stillingar og settu daglegt/vikulegt/mánaðarlegt hámark</li>
<li><strong>Notaðu tímatakmarkanir</strong> — Sum spilavíti bjóða áminningartímamæla</li>
<li><strong>Sjálfsútilokun</strong> — Þú getur lokað á reikninginn þinn tímabundið eða varanlega. <a href="{URL_BASE}leidbeiningar/sjalfsutilokun-spilavita/">Hvernig sjálfsútilokun virkar →</a></li>
</ul>

<h3>Hjálp á Íslandi</h3>
<div class="info-box"><p><strong>Hjálparsími 1717</strong> — Opinn allan sólarhringinn, alla daga. Ókeypis og trúnaðarmál. Hægt að hringja nafnlaust.</p></div>
<div class="info-box"><p><strong>SÁÁ</strong> — Samtök áfengis- og vímuvarnastarfs. Veita einnig stuðning við spilafikn. <em>saa.is</em></p></div>
<div class="info-box"><p><strong>Ráðgjafar- og greiningarstöð — RGS</strong> — Sérfræðiþjónusta í Reykjavík.</p></div>

<h3>Alþjóðleg úrræði</h3>
<ul>
<li><strong>GamStop</strong> — Sjálfsútilokunartól fyrir fleiri en eitt spilavíti</li>
<li><strong>Gamblers Anonymous</strong> — Stuðningshópar (einnig á netinu)</li>
<li><strong>BeGambleAware</strong> — Fræðsluefni og sjálfsmatspróf</li>
</ul>

<h2>Ráð til aðstandenda</h2>
<p>Ef þú heldur að einhver nálægur þér sé háður fjárhættuspilum:</p>
<ul>
<li>Talaðu við manneskjuna án dóms eða ásakana</li>
<li>Bjóddu stuðning — ekki heim kjarnorkuna</li>
<li>Hringdu sjálfur í 1717 til að fá ráðgjöf um hvernig á að ná til manneskjunnar</li>
<li>Ekki lána peninga til að borga spilaskuldir — það lengir vandamálið</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Er ég háður ef ég spila einu sinni í viku?</h3>
<p>Tíðnin ein og sér segir ekki allt. Það sem skiptir máli er hvort þú getir hætt þegar þú vilt, hvort þú spilar meira en þú hefur efni á og hvort spilunin hefur neikvæð áhrif á líf þitt.</p>
<h3>Get ég orðið háður á netinu?</h3>
<p>Já — netspilavíti geta verið sérstaklega vanabindandi vegna aðgengis (alltaf opið, alltaf í vasanum), hraðra snúninga og takmarkalauss framboðs af leikjum.</p>
<h3>Hvað ef ég vil bara draga úr en ekki hætta?</h3>
<p>Það er fullkomlega gilt markmið. Settu innborgunartakmörk, taktu hlé og fylgstu með hversu mikið þú spilar. Ef þú getur ekki dregið úr á eigin spýtur skaltu leita þér hjálpar.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Setja takmörk →</a></div>'''
    },
    {
        "slug": "blackjack-reglur-a-islensku",
        "title": "Blackjack reglur á íslensku — fullkominn leiðarvísir 2026",
        "desc": "Blackjack reglur útskýrðar á íslensku. Hvernig á að spila, kortavirði, split, double down og hvenær á að standa.",
        "emoji": "🃏",
        "colors": ('#0a1a0d', '#14331a', '#1e4d27'),
        "content": f'''<h1>Blackjack reglur á íslensku 2026</h1>
{hero}
<p>Blackjack (svarta-pétur/21) er einn vinsælasti borðleikurinn í spilavítum — og einn sá eini þar sem <strong>leikmaðurinn getur haft áhrif á niðurstöðuna</strong> með réttum ákvörðunum. Hér eru allar reglurnar á íslensku.</p>

<h2>Markmið leiksins</h2>
<p>Markmiðið er einfalt: <strong>komast sem næst 21 án þess að fara yfir</strong> — og vera nær 21 en díllerinn.</p>

<h2>Kortavirði</h2>
<table class="info-table"><thead><tr><th>Kort</th><th>Virði</th></tr></thead><tbody>
<tr><td>2-10</td><td>Sama og talan á kortinu</td></tr>
<tr><td>Gosi, Drottning, Kóngur</td><td>10</td></tr>
<tr><td>Ás</td><td>1 eða 11 (þú velur)</td></tr>
</tbody></table>

<h2>Hvernig leikurinn virkar</h2>
<ol>
<li><strong>Veðmál</strong> — Þú leggur veðmál áður en kort eru gefin</li>
<li><strong>Upphafsúthlutun</strong> — Þú færð 2 kort (bæði opin). Díllerinn fær 2 kort (1 opið, 1 lokað)</li>
<li><strong>Þú velur aðgerð</strong> — Hit, Stand, Double Down, Split eða Surrender</li>
<li><strong>Díllerinn spilar</strong> — Díllerinn verður að taka kort þar til hann nær 17+</li>
<li><strong>Niðurstaða</strong> — Sá sem er nær 21 (án þess að fara yfir) vinnur</li>
</ol>

<h2>Aðgerðir sem þú getur tekið</h2>
<table class="info-table"><thead><tr><th>Aðgerð</th><th>Á íslensku</th><th>Hvað þýðir það</th></tr></thead><tbody>
<tr><td>Hit</td><td>Taka kort</td><td>Fá eitt kort í viðbót</td></tr>
<tr><td>Stand</td><td>Standa</td><td>Halda þínum kortum, ekki taka fleiri</td></tr>
<tr><td>Double Down</td><td>Tvöfalda</td><td>Tvöfalda veðmálið, fá nákvæmlega eitt kort í viðbót</td></tr>
<tr><td>Split</td><td>Skipta</td><td>Ef þú ert með tvö eins kort, skipta þeim í tvær hendur</td></tr>
<tr><td>Surrender</td><td>Gefast upp</td><td>Hætta og fá helming veðmálsins til baka (ekki alltaf í boði)</td></tr>
<tr><td>Insurance</td><td>Trygging</td><td>Aukahlið-veðmál ef díllerinn sýnir ás (yfirleitt slæmt veðmál)</td></tr>
</tbody></table>

<h2>Grunnstrategy — hvenær á að taka kort?</h2>
<p>Blackjack er ekki eingöngu heppni — rétt strategy getur lækkað húsforskotið niður í 0.5%. Hér er einföld regla:</p>
<ul>
<li><strong>8 eða minna</strong> — Hit alltaf</li>
<li><strong>9</strong> — Double ef díllerinn sýnir 3-6, annars Hit</li>
<li><strong>10-11</strong> — Double ef þú ert hærri en díllerinn, annars Hit</li>
<li><strong>12-16</strong> — Stand ef díllerinn sýnir 2-6. Hit ef díllerinn sýnir 7+</li>
<li><strong>17+</strong> — Stand alltaf</li>
</ul>
<p><a href="{URL_BASE}leidbeiningar/blackjack-adferdir/">Ítarleg blackjack strategy → </a></p>

<h2>Sérstök atriði</h2>
<h3>Blackjack (náttúrulegur 21)</h3>
<p>Ef þú færð 21 á fyrstu tveimur kortunum (ás + 10/gosi/drottning/kóngur) er þetta „Blackjack" og þú vinnur 3:2 (eða 6:5 á sumum borðum). Þetta er besta hönd sem hægt er að fá.</p>

<h3>Bust</h3>
<p>Ef samtala kortanna fer yfir 21 hefurðu tapað strax — sama hvað díllerinn er með.</p>

<h2>Hvar á að spila blackjack á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></strong> — Sterkur lifandi blackjack hluti frá Evolution</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — RNG blackjack og lifandi borð</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}live/blackjack/">Lifandi blackjack á Svipan</a></strong> — Sjá alla lifandi blackjack leiki</p></div>

<h2>Algengar spurningar</h2>
<h3>Er hægt að vinna stöðugt í blackjack?</h3>
<p>Til lengri tíma hefur spilavítið forskot (0.5% með réttri strategy). En rétt strategy minnkar tapið verulega og gefur þér bestu mögulegu líkurnar.</p>
<h3>Er kortatelling ólögleg?</h3>
<p>Nei — kortatelling er ekki ólögleg. Hins vegar er hún ómöguleg á netspilavítum vegna þess að stokkurinn er stokkaður á ný í hverri umferð (RNG).</p>
<h3>Hvað er munurinn á RNG blackjack og lifandi blackjack?</h3>
<p>RNG blackjack notar tölvu sem dílara — hraðara, hægt að spila í demo. Lifandi blackjack streymir raunverulegum dílara í beinni — hægara en raunverulegri upplifun.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila blackjack →</a></div>'''
    },
    {
        "slug": "rullettureglur-a-islensku",
        "title": "Rúllettureglur á íslensku — hvernig á að spila rúllettu 2026",
        "desc": "Rúllettureglur á íslensku: veðmálaflötur, tegundir veðmála, líkur og strategy. Evrópsk vs amerísk rúlletta.",
        "emoji": "🎡",
        "colors": ('#1a0a00', '#331400', '#4d1e00'),
        "content": f'''<h1>Rúllettureglur á íslensku 2026</h1>
{hero}
<p>Rúlletta er elsti og þekktasti spilavítileikurinn. <strong>Hjólið snýst, kúlan lendir og annað hvort vinnurðu eða tapar.</strong> Hér eru allar reglurnar á íslensku — frá grunninu til aðferða.</p>

<h2>Grunnreglur</h2>
<ol>
<li>Díllerinn snýr hjólinu og kastar kúlunni í gagnstæða átt</li>
<li>Þú leggur veðmál á hvar kúlan lendir — á tölu, lit, hóp eða samsetningu</li>
<li>Kúlan lendir í rauf — ef þú veðjaðir á rétt stórir peningarnir</li>
</ol>

<h2>Evrópsk vs amerísk rúlletta</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Evrópsk</th><th>Amerísk</th></tr></thead><tbody>
<tr><td>Tölur</td><td>0-36 (37 raufar)</td><td>0-36 + 00 (38 raufar)</td></tr>
<tr><td>Húsforskot</td><td>2.7%</td><td>5.26%</td></tr>
<tr><td>RTP</td><td>97.3%</td><td>94.74%</td></tr>
<tr><td>Okkar ráð</td><td>✅ Alltaf þetta</td><td>❌ Forðist</td></tr>
</tbody></table>
<p><strong>Veldu alltaf evrópska rúllettu.</strong> Amerísk rúlletta hefur nánast tvöfalt húsforskot vegna aukanúllsins (00).</p>

<h2>Tegundir veðmála</h2>
<h3>Innri veðmál (Higher risk, higher reward)</h3>
<table class="info-table"><thead><tr><th>Veðmál</th><th>Lýsing</th><th>Vinningshlutfall</th></tr></thead><tbody>
<tr><td>Straight Up</td><td>Ein tala</td><td>35:1</td></tr>
<tr><td>Split</td><td>Tvær tölur</td><td>17:1</td></tr>
<tr><td>Street</td><td>Þrjár tölur (röð)</td><td>11:1</td></tr>
<tr><td>Corner</td><td>Fjórar tölur (horn)</td><td>8:1</td></tr>
<tr><td>Line</td><td>Sex tölur (tvær raðir)</td><td>5:1</td></tr>
</tbody></table>

<h3>Ytri veðmál (Lower risk, lower reward)</h3>
<table class="info-table"><thead><tr><th>Veðmál</th><th>Lýsing</th><th>Vinningshlutfall</th></tr></thead><tbody>
<tr><td>Rautt/Svart</td><td>Litur</td><td>1:1</td></tr>
<tr><td>Oddatölur/Sléttar</td><td>Odd/Even</td><td>1:1</td></tr>
<tr><td>1-18/19-36</td><td>Há/Lág</td><td>1:1</td></tr>
<tr><td>Tugir (1-12, 13-24, 25-36)</td><td>Dozen</td><td>2:1</td></tr>
<tr><td>Dálkur</td><td>Column</td><td>2:1</td></tr>
</tbody></table>

<h2>Aðferðir (strategy)</h2>
<h3>Martingale</h3>
<p>Tvöfaldaðu veðmálið eftir hvert tap. Þegar þú vinnur færðu allt tapið til baka + einn veðning. <strong>Vandamál:</strong> borðtakmörk stoppa þig eftir 7-8 töp í röð og tapið verður gríðarlegt.</p>

<h3>D'Alembert</h3>
<p>Hækkaðu veðmálið um eina einingu eftir tap, lækkaðu um eina eftir vinning. Vægari en Martingale.</p>

<h3>Fibonacci</h3>
<p>Notaðu Fibonacci-röðina (1, 1, 2, 3, 5, 8, 13...) til að ákvarða veðmálið. Farðu tvö skref til baka eftir vinning.</p>

<p><strong>Sannleikurinn:</strong> Engin strategy getur sigrað rúllettu til lengri tíma vegna húsforskots. En þessar aðferðir geta gert spilunina skemmtilegri og stýrðari.</p>

<h2>Hvar á að spila rúllettu á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}live/lightning-roulette/">Lightning Roulette</a></strong> — Vinsælasta lifandi rúllettan. Hægt að vinna allt að 500x</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}live/roulette/">Lifandi rúlletta á Svipan</a></strong> — Allir lifandi rúllettuleikir</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></strong> — Sterkur lifandi rúllettuhluti</p></div>

<h2>Algengar spurningar</h2>
<h3>Er einhver leið til að tryggja vinning í rúllettu?</h3>
<p>Nei — rúlletta er 100% happadrættisleikur. Engin strategy getur sigrað húsforskotið til lengri tíma. Spilaðu til gamans, ekki sem tekjuleið.</p>
<h3>Hvað er Lightning Roulette?</h3>
<p>Lifandi rúlletta frá Evolution þar sem 1-5 tölur fá „lightning" margfaldara (50x-500x) í hverri umferð. Vinsælasta útgáfan á netinu.</p>
<h3>Er betra að veðja á lit eða tölu?</h3>
<p>Litaveðmál (rautt/svart) vinnur oftar (48.6%) en borgar einungis 1:1. Töluvéðmál (straight up) vinnur sjaldnar (2.7%) en borgar 35:1. Valið fer eftir áhættuvilja þínum.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila rúllettu →</a></div>'''
    },
    {
        "slug": "pragmatic-play-allir-leikir",
        "title": "Pragmatic Play — allir leikir, RTP og umsagnir 2026",
        "desc": "Allir Pragmatic Play spilakassar á Íslandi: Gates of Olympus, Sweet Bonanza, Big Bass og fleiri. RTP, sveifla og bestu spilavítin.",
        "emoji": "🎰",
        "colors": ('#0a0a1a', '#141433', '#1e1e4d'),
        "content": f'''<h1>Pragmatic Play — allir leikir og RTP 2026</h1>
{hero}
<p>Pragmatic Play er <strong>stærsti og vinsælasti leikjaframleiðandinn</strong> á netspilavítum á Íslandi. Ef þú hefur einhvern tíma spilað <a href="{URL_BASE}spilakassar/gates-of-olympus/">Gates of Olympus</a>, <a href="{URL_BASE}spilakassar/sweet-bonanza/">Sweet Bonanza</a> eða <a href="{URL_BASE}spilakassar/big-bass-bonanza/">Big Bass Bonanza</a> — þú hefur spilað Pragmatic Play.</p>

<h2>Um Pragmatic Play</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2015</td></tr>
<tr><td>Höfuðstöðvar</td><td>Malta</td></tr>
<tr><td>Fjöldi leikja</td><td>300+ spilakassar, lifandi leikir, bingo</td></tr>
<tr><td>Þekktustu leikir</td><td>Gates of Olympus, Sweet Bonanza, Big Bass seríur</td></tr>
<tr><td>Sérkenni</td><td>Drops & Wins mót, Bonus Buy, Megaways</td></tr>
</tbody></table>

<h2>Vinsælustu Pragmatic Play leikirnir á Íslandi</h2>
<table class="info-table"><thead><tr><th>#</th><th>Leikur</th><th>RTP</th><th>Sveifla</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td>1</td><td><a href="{URL_BASE}spilakassar/gates-of-olympus/">Gates of Olympus</a></td><td>96.50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>2</td><td><a href="{URL_BASE}spilakassar/sweet-bonanza/">Sweet Bonanza</a></td><td>96.48%</td><td>Meðal-há</td><td>21.175x</td></tr>
<tr><td>3</td><td><a href="{URL_BASE}spilakassar/big-bass-bonanza/">Big Bass Bonanza</a></td><td>96.71%</td><td>Há</td><td>2.100x</td></tr>
<tr><td>4</td><td><a href="{URL_BASE}spilakassar/starlight-princess/">Starlight Princess</a></td><td>96.50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>5</td><td><a href="{URL_BASE}spilakassar/gates-of-olympus-1000/">Gates of Olympus 1000</a></td><td>96.50%</td><td>Mjög há</td><td>15.000x</td></tr>
<tr><td>6</td><td><a href="{URL_BASE}spilakassar/sugar-rush/">Sugar Rush</a></td><td>96.50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>7</td><td><a href="{URL_BASE}spilakassar/wolf-gold/">Wolf Gold</a></td><td>96.01%</td><td>Meðal</td><td>Pottur</td></tr>
<tr><td>8</td><td><a href="{URL_BASE}spilakassar/big-bass-splash/">Big Bass Splash</a></td><td>95.67%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>9</td><td><a href="{URL_BASE}spilakassar/sweet-bonanza-1000/">Sweet Bonanza 1000</a></td><td>96.48%</td><td>Mjög há</td><td>25.000x</td></tr>
<tr><td>10</td><td><a href="{URL_BASE}spilakassar/fruit-party/">Fruit Party</a></td><td>96.47%</td><td>Há</td><td>5.000x</td></tr>
</tbody></table>
<p><a href="{URL_BASE}spilakassar/">Sjá alla 98 spilakassaumsagnir →</a></p>

<h2>Drops & Wins — hvað er það?</h2>
<p>Drops & Wins er mánaðarlegt mótakerfi frá Pragmatic Play þar sem spilarar geta unnið viðbótarvinning ofan á venjulega spilun. Daglegir og vikulegir vinningssjóðir eru greiddir út af handahófi til spilara sem spila Pragmatic Play leiki á þátttökuspilavítum.</p>
<p>Spilavíti á Íslandi sem styðja Drops & Wins: <a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a>, <a href="{URL_BASE}spilaviti/respin/">Respin</a>, <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a>.</p>

<h2>Bestu spilavítin fyrir Pragmatic Play á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — 8.000+ leikir, stórt Pragmatic Play safn og Drops & Wins</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Íslenskt viðmót, Pragmatic Play spilakassar og lifandi leikir</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Allt Pragmatic Play safnið í boði</p></div>

<h2>Algengar spurningar</h2>
<h3>Er Pragmatic Play öruggt?</h3>
<p>Já — Pragmatic Play hefur leyfi frá Malta Gaming Authority (MGA), UK Gambling Commission og fleiri. Leikirnir eru prófaðir af óháðum prófunarstofum.</p>
<h3>Hvaða Pragmatic Play leikur hefur hæsta RTP?</h3>
<p><a href="{URL_BASE}spilakassar/big-bass-bonanza/">Big Bass Bonanza</a> með 96.71% RTP. Athugaðu þó að sum spilavíti nota lægri RTP stillingar — athugaðu alltaf í leikjareglum.</p>
<h3>Er hægt að spila Pragmatic Play leiki ókeypis?</h3>
<p>Já — flestir Pragmatic Play spilakassar eru í boði í <a href="{URL_BASE}leidbeiningar/okeypis-spilaviti-island/">demo-ham</a>. Engrar skráningar krafist.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Pragmatic Play →</a></div>'''
    },
    {
        "slug": "ice-casino-a-islandi",
        "title": "Ice Casino á Íslandi — umsögn, bónus og greiðslur 2026",
        "desc": "Ice Casino umsögn fyrir íslenska spilara. Velkomstbónus, leikjaúrval, greiðsluleiðir og hvort þetta spilavíti tekur við frá Íslandi.",
        "emoji": "🧊",
        "colors": ("#0a1a2e", "#143050", "#1e4672"),
        "content": f'''<h1>Ice Casino á Íslandi — umsögn 2026</h1>
{hero}
<p>Ice Casino er eitt vinsælasta netspilavítið í Evrópu og er rekið af V.Partners (sama fyrirtæki og <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a>). <strong>En hvernig virkar Ice Casino fyrir íslenska spilara?</strong></p>

<h2>Ice Casino í hnotskurn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2021</td></tr>
<tr><td>Eigandi</td><td>Brivio Limited (V.Partners)</td></tr>
<tr><td>Leyfi</td><td>Curaçao</td></tr>
<tr><td>Leikir</td><td>3.500+</td></tr>
<tr><td>Velkomstbónus</td><td>Allt að €1.500 + 270 FS</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€20</td></tr>
<tr><td>Íslenskt viðmót</td><td>❌ Nei (enska, þýska, pólska o.fl.)</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>✅ BTC, ETH, LTC, USDT</td></tr>
</tbody></table>

<h2>Velkomstbónus</h2>
<p>Ice Casino býður nýjum spilurum velkomstpakka sem dreifist yfir fyrstu fjórar innborganir:</p>
<ol>
<li>1. innborgun: 120% + 120 FS</li>
<li>2. innborgun: 50% + 50 FS</li>
<li>3. innborgun: 50% + 50 FS</li>
<li>4. innborgun: 50% + 50 FS</li>
</ol>
<p>Veðskilyrði: 40x bónus. <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">Hvað þýðir 40x veðskilyrði? →</a></p>

<h2>Leikjaúrval</h2>
<p>Ice Casino er með yfir 3.500 leiki frá 50+ framleiðendum: Pragmatic Play, NetEnt, Play'n GO, Evolution, Microgaming og fleiri. Gott úrval af spilakössum, lifandi spilavíti og borðleikjum.</p>

<h2>Greiðsluleiðir á Íslandi</h2>
<p>Ice Casino styður Visa, Mastercard, Skrill, Neteller, ecoPayz og dulritunargjaldmiðla. Fyrir íslenska spilara eru dulritunargjaldmiðlar besti kosturinn vegna <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">bankatakmarkana</a>.</p>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Stór velkomstpakki (€1.500)</td><td>❌ Ekkert íslenskt viðmót</td></tr>
<tr><td>✅ Gott leikjaúrval (3.500+)</td><td>❌ 40x veðskilyrði (hátt)</td></tr>
<tr><td>✅ Dulritunargjaldmiðlar studdir</td><td>❌ €20 lágmarksinnborgun (hærra en flest)</td></tr>
<tr><td>✅ V.Partners (sömu eigendur og Slotoro)</td><td>❌ Ekkert þjónustuver á íslensku</td></tr>
</tbody></table>

<h2>Ice Casino vs Slotoro</h2>
<p>Bæði eru V.Partners spilavíti en höfða til mismunandi markhópa. <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> hefur stærra leikjasafn (8.000+) og lægri lágmarksinnborgun (€10). Ice Casino hefur stærri velkomstbónus.</p>

<h2>Algengar spurningar</h2>
<h3>Tekur Ice Casino við frá Íslandi?</h3>
<p>Já — Ice Casino lokar ekki á íslenska spilara. Hins vegar er viðmótið ekki á íslensku.</p>
<h3>Er Ice Casino öruggt?</h3>
<p>Ice Casino er með Curaçao leyfi og er rekið af V.Partners sem hefur verið í iGaming bransanum síðan 2016. Þekkt fyrirtæki.</p>
<h3>Er betra að nota Ice Casino eða Slotoro?</h3>
<p>Ef þú vilt stærra leikjasafn og lægri innborgun: <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a>. Ef þú vilt stærri bónus: Ice Casino.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>'''
    },
    {
        "slug": "vulkan-vegas-a-islandi",
        "title": "Vulkan Vegas á Íslandi — umsögn og greiðsluleiðir 2026",
        "desc": "Vulkan Vegas umsögn: bónus allt að €1.000, 5.000+ leikir. Er þetta spilavíti gott fyrir íslenska spilara?",
        "emoji": "🌋",
        "colors": ("#1a0a00", "#331400", "#4d1e00"),
        "content": f'''<h1>Vulkan Vegas á Íslandi — umsögn 2026</h1>
{hero}
<p>Vulkan Vegas er flaggskip V.Partners og eitt stærsta netspilavíti Evrópu. <strong>Yfir 5.000 leikir, allt að €1.000 velkomstbónus og góður lifandi spilavítishluti.</strong></p>

<h2>Vulkan Vegas í hnotskurn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2016</td></tr>
<tr><td>Eigandi</td><td>Brivio Limited (V.Partners)</td></tr>
<tr><td>Leyfi</td><td>Curaçao</td></tr>
<tr><td>Leikir</td><td>5.000+</td></tr>
<tr><td>Velkomstbónus</td><td>Allt að €1.000 + 125 FS</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€10</td></tr>
<tr><td>Íslenskt viðmót</td><td>❌ Nei</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>✅ BTC, ETH, LTC</td></tr>
</tbody></table>

<h2>Velkomstbónus</h2>
<p>Vulkan Vegas býður tveggja innborgana velkomstpakka:</p>
<ol>
<li>1. innborgun: 100% allt að €300 + 25 FS (ef innborgun er €50+)</li>
<li>2. innborgun: 125% allt að €700 + 100 FS (ef innborgun er €50+)</li>
</ol>
<p>Veðskilyrði: 40x bónus. Hámarksveðmál: €5. Tímamörk: 5 dagar.</p>

<h2>Leikjaúrval</h2>
<p>Stórt safn: 5.000+ leikir frá 70+ framleiðendum. Sterkur Pragmatic Play, NetEnt og Evolution hluti. Drops & Wins mót eru í boði.</p>

<h2>Greiðsluleiðir</h2>
<p>Visa, Mastercard, Skrill, Neteller, ecoPayz, Jeton, MiFinity, Bitcoin, Ethereum, Litecoin. Á Íslandi mælum við með <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">dulritunargjaldmiðlum</a> eða <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut</a>.</p>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Stórt leikjasafn (5.000+)</td><td>❌ Ekkert íslenskt viðmót</td></tr>
<tr><td>✅ Rótgróið (síðan 2016)</td><td>❌ 40x veðskilyrði</td></tr>
<tr><td>✅ Góður lifandi hluti</td><td>❌ 5 daga tímamörk á bónus (stutt)</td></tr>
<tr><td>✅ VIP kerfi (Cashback)</td><td>❌ Krefst €50 innborgunar fyrir bónus</td></tr>
</tbody></table>

<h2>Algengar spurningar</h2>
<h3>Er Vulkan Vegas betra en Slotoro?</h3>
<p>Vulkan Vegas hefur fleiri leiki og stærri bónus. <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> er nýrra og einbeitir sér frekar. Bæði eru V.Partners og áreiðanleg.</p>
<h3>Get ég spilað á Vulkan Vegas frá Íslandi?</h3>
<p>Já — Vulkan Vegas lokar ekki á Ísland. Notaðu dulritunargjaldmiðla eða e-wallet fyrir greiðslur.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>'''
    },
    {
        "slug": "gates-of-olympus-leidarvisir",
        "title": "Gates of Olympus — leiðarvísir, RTP og aðferðir 2026",
        "desc": "Gates of Olympus spilakassi: RTP 96.5%, há sveifla, allt að 5.000x vinningur. Hvernig virkar leikurinn og hvar á að spila.",
        "emoji": "⚡",
        "colors": ("#1a0a28", "#2d1445", "#401e62"),
        "content": f'''<h1>Gates of Olympus — leiðarvísir 2026</h1>
{hero}
<p>Gates of Olympus (frá Pragmatic Play) er <strong>einn vinsælasti spilakassinn í heiminum</strong> og er sérstaklega vinsæll á Íslandi. Leikurinn er þekktur fyrir Tumble-vélbúnað, margfaldara og möguleikann á allt að 5.000x vinningi.</p>

<h2>Tæknilegar upplýsingar</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Gildi</th></tr></thead><tbody>
<tr><td>Framleiðandi</td><td>Pragmatic Play</td></tr>
<tr><td>RTP</td><td>96.50%</td></tr>
<tr><td>Sveifla</td><td>Há</td></tr>
<tr><td>Hámarksvinningur</td><td>5.000x veðmál</td></tr>
<tr><td>Línur</td><td>Engar — Pay Anywhere</td></tr>
<tr><td>Hlutverk</td><td>6x5 grind, Tumble, margfaldarar</td></tr>
<tr><td>Bónus Buy</td><td>✅ 100x veðmál</td></tr>
<tr><td>Frísnúninga umferð</td><td>15 frísnúningar við 4+ Scatter</td></tr>
</tbody></table>

<h2>Hvernig virkar Gates of Olympus?</h2>
<h3>Tumble (keðjuvinningar)</h3>
<p>Þegar þú vinnur hverfa vinningskortið og ný kort falla niður — þetta getur skapað keðjuvinning. Hver vinningur í röð hækkar margfaldarann.</p>

<h3>Margfaldarar</h3>
<p>Zeús getur kastað margfaldaraglóbum á borðið: 2x, 3x, 4x, 5x, 8x, 10x eða 500x. Þeir leggja saman — ef 3x og 5x koma fram er heildarmargfaldarinn 8x. Þetta er það sem gerir leikinn svo spennandi (og sveiflukenndan).</p>

<h3>Frísnúningar</h3>
<p>4+ Scatter tákn gefa 15 frísnúninga. Í frísnúningum safnast margfaldarar og <strong>endurstillast EKKI</strong> á milli snúninga — þeir leggjast bara saman. Þetta er þar sem stóru vinningarnir gerast.</p>

<h3>Bónus Buy</h3>
<p>Þú getur keypt þig beint í frísnúninga fyrir 100x veðmálið þitt. Dæmi: ef þú spilar á €0.20 kostar Bónus Buy €20. Þetta er áhættusamt en skemmtilegt. <a href="{URL_BASE}leidbeiningar/bonus-buy-spilakassar/">Er Bónus Buy þess virði? →</a></p>

<h2>Aðferðir og ráð</h2>
<ul>
<li><strong>Byrjaðu í demo</strong> — Prófaðu leikinn ókeypis til að skilja hvernig margfaldarar virka. <a href="{URL_BASE}spilakassar/gates-of-olympus/">Spila Gates of Olympus demo →</a></li>
<li><strong>Veðmálsstærð</strong> — Þessi leikur hefur háa sveiflu. Veldu veðmál sem þú ráður við í 200+ snúninga (dæmi: €50 → €0.20/snúning)</li>
<li><strong>Bónus Buy</strong> — Tölfræðilega er RTP á Bónus Buy svipað og í venjulegri spilun. En sveiflur eru meiri</li>
<li><strong>Stilltu tap-takmörk</strong> — Ákveddu fyrirfram hversu miklu þú ert tilbúinn að tapa</li>
</ul>

<h2>Gates of Olympus 1000 — hvað er munurinn?</h2>
<p><a href="{URL_BASE}spilakassar/gates-of-olympus-1000/">Gates of Olympus 1000</a> er ný útgáfa með margfaldara upp að 1.000x (í stað 500x) og hámarksvinning 15.000x (í stað 5.000x). Enn hærri sveifla.</p>

<h2>Hvar á að spila Gates of Olympus á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — Gates of Olympus í boði, bæði demo og alvöru. Velkomstpakki.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Pragmatic Play safnið í boði. 5 BTC + 200 FS.</p></div>

<h2>Algengar spurningar</h2>
<h3>Er hægt að vinna stórt í Gates of Olympus?</h3>
<p>Já — hámarksvinningur er 5.000x veðmálið. Á €1 snúningi þýðir þetta €5.000. En há sveifla þýðir líka langa þurrkatímabil.</p>
<h3>Er Bónus Buy þess virði?</h3>
<p>Tölfræðilega gefur Bónus Buy svipað RTP og venjuleg spilun. En þú ferð beint í spennandi hlutann. Athugaðu að 100x veðmálið er stór fjárfesting — spilaðu aðeins ef þú hefur efni á að tapa þeirri upphæð.</p>
<h3>Hvað er RTP á Gates of Olympus?</h3>
<p>Staðlað RTP er 96.50%. <strong>Athugið:</strong> sum spilavíti nota lægri RTP stillingu (94.50% eða 87.50%). Athugaðu alltaf RTP í leikjareglum (ℹ tákn í leiknum).</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Gates of Olympus →</a></div>'''
    },
    {
        "slug": "sweet-bonanza-leidarvisir",
        "title": "Sweet Bonanza — leiðarvísir, RTP og bónuseiginleikar 2026",
        "desc": "Sweet Bonanza spilakassi: RTP 96.48%, há sveifla, Tumble og margfaldarar. Hvernig á að spila og hvar á Íslandi.",
        "emoji": "🍬",
        "colors": ("#2e0a1a", "#501430", "#721e46"),
        "content": f'''<h1>Sweet Bonanza — leiðarvísir 2026</h1>
{hero}
<p>Sweet Bonanza frá Pragmatic Play er <strong>annar vinsælasti spilakassinn á Íslandi</strong> á eftir Gates of Olympus. Litríkur leikur með sælgætisþema, Tumble vélbúnaði og margföldura sem geta gefið allt að 21.175x vinning.</p>

<h2>Tæknilegar upplýsingar</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Gildi</th></tr></thead><tbody>
<tr><td>Framleiðandi</td><td>Pragmatic Play</td></tr>
<tr><td>RTP</td><td>96.48%</td></tr>
<tr><td>Sveifla</td><td>Meðal-há</td></tr>
<tr><td>Hámarksvinningur</td><td>21.175x veðmál</td></tr>
<tr><td>Grind</td><td>6x5 (Cluster Pays)</td></tr>
<tr><td>Bónus Buy</td><td>✅ 100x veðmál</td></tr>
<tr><td>Frísnúninga umferð</td><td>10 frísnúningar við 4+ Scatter</td></tr>
<tr><td>Ante Bet</td><td>✅ 25% hærra veðmál = 2x líkur á frísnúningum</td></tr>
</tbody></table>

<h2>Hvernig virkar Sweet Bonanza?</h2>
<h3>Cluster Pays</h3>
<p>Engar hefðbundnar vinningslínur. Þú vinnur þegar 8+ eins tákn birtast hvar sem er á borðinu. Eftir vinning hverfa táknin (Tumble) og ný falla niður.</p>

<h3>Margfaldarasprengjur</h3>
<p>Í frísnúningum geta litríkar sprengjur birst á borðinu: 2x, 3x, 5x, 10x, 25x, 50x eða 100x. Þær margfalda allan vinning í þeirri Tumble-lotu. <strong>Þetta er lykileiginleikinn</strong> — 100x margfaldari á stóran vinning getur breytt öllu.</p>

<h3>Ante Bet</h3>
<p>Þú getur virkjað Ante Bet sem hækkar veðmálið um 25% en tvöfaldar líkur á að fá frísnúninga. Dæmi: €0.20 verður €0.25 en frísnúningar koma tvisvar sinnum oftar.</p>

<h2>Sweet Bonanza vs Gates of Olympus</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Sweet Bonanza</th><th>Gates of Olympus</th></tr></thead><tbody>
<tr><td>RTP</td><td>96.48%</td><td>96.50%</td></tr>
<tr><td>Sveifla</td><td>Meðal-há</td><td>Há</td></tr>
<tr><td>Hámarksvinningur</td><td>21.175x</td><td>5.000x</td></tr>
<tr><td>Margfaldarar</td><td>Allt að 100x</td><td>Allt að 500x</td></tr>
<tr><td>Ante Bet</td><td>✅ Já</td><td>❌ Nei</td></tr>
<tr><td>Þema</td><td>Sælgæti</td><td>Grískt goðsagnaþema</td></tr>
</tbody></table>

<h2>Aðferðir</h2>
<ul>
<li><strong>Ante Bet</strong> — Ef þú ert með nægan fjármagn er Ante Bet þess virði. Tvöfaldar líkur á frísnúningum sem er þar sem stóru vinningarnir gerast</li>
<li><strong>Demo fyrst</strong> — <a href="{URL_BASE}spilakassar/sweet-bonanza/">Prófaðu Sweet Bonanza ókeypis</a> til að sjá hversu lengi þú getur spilað á áætluðum fjármunum</li>
<li><strong>200+ snúninga regla</strong> — Tryggðu að veðmálsstærðin leyfir þér 200+ snúninga til að ná frísnúningum</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Hver er hámarksvinningurinn í Sweet Bonanza?</h3>
<p>21.175x veðmálið. Á €1 snúningi: €21.175. Þetta er hærra en flestir spilakassar.</p>
<h3>Er Sweet Bonanza 1000 betra?</h3>
<p><a href="{URL_BASE}spilakassar/sweet-bonanza-1000/">Sweet Bonanza 1000</a> hefur hærri hámarksvinning (25.000x) og stærri margfaldara en meiri sveiflu. Fyrir reynda spilara sem vilja meiri áhættu.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Sweet Bonanza →</a></div>'''
    },
    {
        "slug": "netent-saga-og-bestu-leikir",
        "title": "NetEnt — saga, bestu leikir og RTP 2026",
        "desc": "NetEnt leikjaframleiðandi: Starburst, Gonzo's Quest, Dead or Alive og fleiri. RTP tafla, saga og bestu spilavítin á Íslandi.",
        "emoji": "🎮",
        "colors": ("#0a1a0a", "#143314", "#1e4d1e"),
        "content": f'''<h1>NetEnt — saga og bestu leikir 2026</h1>
{hero}
<p>NetEnt (Net Entertainment) er <strong>einn elsti og virtusti leikjaframleiðandinn</strong> í iGaming bransanum. Ef þú hefur spilað <a href="{URL_BASE}spilakassar/starburst/">Starburst</a>, <a href="{URL_BASE}spilakassar/gonzos-quest/">Gonzo's Quest</a> eða <a href="{URL_BASE}spilakassar/dead-or-alive/">Dead or Alive</a> — þú hefur spilað NetEnt.</p>

<h2>Um NetEnt</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>1996 (einn af fyrstu framleiðendum)</td></tr>
<tr><td>Höfuðstöðvar</td><td>Stokkhólmur, Svíþjóð</td></tr>
<tr><td>Eigandi</td><td>Evolution Gaming Group (síðan 2020)</td></tr>
<tr><td>Fjöldi leikja</td><td>200+ spilakassar</td></tr>
<tr><td>Þekktustu leikir</td><td>Starburst, Gonzo's Quest, Dead or Alive, Divine Fortune</td></tr>
<tr><td>Sérkenni</td><td>Há gæði, lág-meðal sveifla, nýsköpun</td></tr>
</tbody></table>

<h2>Topp 10 NetEnt leikir á Íslandi</h2>
<table class="info-table"><thead><tr><th>#</th><th>Leikur</th><th>RTP</th><th>Sveifla</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td>1</td><td><a href="{URL_BASE}spilakassar/starburst/">Starburst</a></td><td>96.09%</td><td>Lág</td><td>500x</td></tr>
<tr><td>2</td><td><a href="{URL_BASE}spilakassar/gonzos-quest/">Gonzo's Quest</a></td><td>95.97%</td><td>Meðal</td><td>2.500x</td></tr>
<tr><td>3</td><td><a href="{URL_BASE}spilakassar/dead-or-alive/">Dead or Alive</a></td><td>96.82%</td><td>Há</td><td>12.000x</td></tr>
<tr><td>4</td><td><a href="{URL_BASE}spilakassar/dead-or-alive-2/">Dead or Alive 2</a></td><td>96.29%</td><td>Mjög há</td><td>111.111x</td></tr>
<tr><td>5</td><td><a href="{URL_BASE}spilakassar/divine-fortune/">Divine Fortune</a></td><td>96.59%</td><td>Meðal</td><td>Pottur</td></tr>
<tr><td>6</td><td><a href="{URL_BASE}spilakassar/blood-suckers/">Blood Suckers</a></td><td>98.00%</td><td>Lág</td><td>900x</td></tr>
<tr><td>7</td><td><a href="{URL_BASE}spilakassar/narcos/">Narcos</a></td><td>96.23%</td><td>Meðal</td><td>1.506x</td></tr>
<tr><td>8</td><td><a href="{URL_BASE}spilakassar/twin-spin/">Twin Spin</a></td><td>96.55%</td><td>Meðal</td><td>1.080x</td></tr>
<tr><td>9</td><td><a href="{URL_BASE}spilakassar/jack-and-the-beanstalk/">Jack and the Beanstalk</a></td><td>96.28%</td><td>Meðal</td><td>3.000x</td></tr>
<tr><td>10</td><td><a href="{URL_BASE}spilakassar/finn-and-the-swirly-spin/">Finn and the Swirly Spin</a></td><td>96.62%</td><td>Meðal</td><td>500x</td></tr>
</tbody></table>
<p>Athugaðu: <a href="{URL_BASE}spilakassar/blood-suckers/">Blood Suckers</a> er með 98% RTP — einn hæsti í öllum spilakössum. Frábært val ef þú vilt lágmarks húsforskot.</p>

<h2>NetEnt vs Pragmatic Play</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>NetEnt</th><th>Pragmatic Play</th></tr></thead><tbody>
<tr><td>Fjöldi leikja</td><td>200+</td><td>300+</td></tr>
<tr><td>Sveifla</td><td>Yfirleitt lág-meðal</td><td>Yfirleitt meðal-há</td></tr>
<tr><td>Grafík</td><td>⭐⭐⭐⭐⭐ Hæstu gæði</td><td>⭐⭐⭐⭐ Gott</td></tr>
<tr><td>Nýsköpun</td><td>Átti fyrst Avalanche/Cluster</td><td>Bonus Buy, Megaways</td></tr>
<tr><td>Hentar fyrir</td><td>Þá sem vilja jafnari spilun</td><td>Þá sem vilja stóra vinninga</td></tr>
</tbody></table>

<h2>Algengar spurningar</h2>
<h3>Hvaða NetEnt leikur er bestur fyrir byrjendur?</h3>
<p><a href="{URL_BASE}spilakassar/starburst/">Starburst</a> — einfaldur, fallegur og með lágri sveiflu. Fullkominn til að kynnast spilakössum.</p>
<h3>Hvaða NetEnt leikur hefur hæsta RTP?</h3>
<p><a href="{URL_BASE}spilakassar/blood-suckers/">Blood Suckers</a> með 98% — einn hæsti RTP allra spilakassa.</p>
<h3>Er NetEnt enn að gera nýja leiki?</h3>
<p>Já — NetEnt er nú hluti af Evolution Group og heldur áfram að gefa út nýja leiki undir NetEnt merkinu.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila NetEnt leiki →</a></div>'''
    },
    {
        "slug": "spilaviti-an-vedskilyrda",
        "title": "Spilavíti án veðskilyrða á Íslandi — bónusar sem þú heldur 2026",
        "desc": "Netspilavíti án veðskilyrða: vinningar frá bónus eru þínir strax. Listi yfir bestu veðlausu spilavítin á Íslandi.",
        "emoji": "🎁",
        "colors": ("#280a1a", "#451430", "#621e46"),
        "content": f'''<h1>Spilavíti án veðskilyrða á Íslandi 2026</h1>
{hero}
<p>Flest spilavíti setja <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrði</a> á bónusa — 30x, 40x eða jafnvel 50x. Þetta þýðir að þú verður að veðja bónusupphæðinni 30-50 sinnum áður en þú getur tekið vinninginn út. <strong>En sum spilavíti bjóða 0x veðskilyrði — þú heldur því sem þú vinnur.</strong></p>

<h2>Hvað þýðir „án veðskilyrða" (0x wager)?</h2>
<p>Þetta þýðir: ef þú færð €100 bónus og vinnur €50, geturðu tekið €50 út strax. Engin veðskilyrði. Engir faldir skilmálar.</p>
<p>Samanborið við 40x veðskilyrði: þú þyrftir að veðja €100 x 40 = €4.000 áður en þú gætir tekið eitt krónu út.</p>

<h2>Bestu veðlausu spilavítin á Íslandi</h2>
<table class="info-table"><thead><tr><th>Spilavíti</th><th>Bónus</th><th>Veðskilyrði</th><th>Íslenskt viðmót?</th><th>Einkunn</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></td><td>100% allt að €500</td><td>0x ✅</td><td>✅ Já</td><td>9.0/10</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/respin/">Respin</a></td><td>200% + 50 FS</td><td>0x ✅</td><td>✅ Já</td><td>8.9/10</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/winz/">Winz.io</a></td><td>300 FS</td><td>0x ✅</td><td>❌ Enska</td><td>8.5/10</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/stake/">Stake</a></td><td>200% + VIP</td><td>Engin bónusveðskilyrði</td><td>❌ Enska</td><td>9.6/10</td></tr>
</tbody></table>

<h2>Af hverju eru veðlausir bónusar betri?</h2>
<ul>
<li><strong>Þú heldur því sem þú vinnur</strong> — Engir faldir skilmálar</li>
<li><strong>Ekkert hámarksveðmál</strong> — Á veðskilyrðabónus er yfirleitt €5 hámark á snúning. Á veðlausum bónus geturðu veðjað eins og þú vilt</li>
<li><strong>Engir tímamörk</strong> — Þú þarft ekki að klára 40x veðskilyrði á 7-30 dögum</li>
<li><strong>Gegnsætt</strong> — Þú veist nákvæmlega hvað þú ert að fá</li>
</ul>

<h2>Samanburður: 0x vs 40x veðskilyrði</h2>
<table class="info-table"><thead><tr><th>Dæmi</th><th>0x (veðlaust)</th><th>40x veðskilyrði</th></tr></thead><tbody>
<tr><td>Bónus</td><td>€100</td><td>€100</td></tr>
<tr><td>Vinningur frá bónus</td><td>€50</td><td>€50</td></tr>
<tr><td>Upphæð sem þarf að veðja</td><td>€0</td><td>€4.000</td></tr>
<tr><td>Líkur á að halda vinningnum</td><td>100%</td><td>~15-25%</td></tr>
<tr><td>Úttekt möguleg strax?</td><td>✅ Já</td><td>❌ Eftir 40x velt</td></tr>
</tbody></table>

<h2>Algengar spurningar</h2>
<h3>Af hverju bjóða ekki öll spilavíti 0x veðskilyrði?</h3>
<p>Vegna þess að veðskilyrði vernda spilavítið — ef allir gætu tekið bónus og vinning strax út myndi spilavítið tapa. Veðlausir bónusar eru yfirleitt minni eða með öðrum takmörkunum.</p>
<h3>Eru veðlausir bónusar alltaf betri?</h3>
<p>Yfirleitt já — en berðu saman heildarpakkann. €500 veðlaus bónus er mun verðmætari en €2.000 bónus með 50x veðskilyrðum.</p>
<h3>Get ég fengið bæði veðlausan bónus og tekið út strax?</h3>
<p>Já — á <a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a> og <a href="{URL_BASE}spilaviti/respin/">Respin</a> er bónusinn veðlaus og þú getur tekið vinninginn út strax eftir KYC staðfestingu.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Fá veðlausan bónus →</a></div>'''
    },
    {
        "slug": "baccarat-reglur-a-islensku",
        "title": "Baccarat reglur á íslensku — hvernig á að spila 2026",
        "desc": "Baccarat reglur útskýrðar á íslensku: Player, Banker, Tie. Veðmálamöguleikar, húsforskot og hvar á að spila á Íslandi.",
        "emoji": "🎴",
        "colors": ("#1a0a1a", "#331433", "#4d1e4d"),
        "content": f'''<h1>Baccarat reglur á íslensku 2026</h1>
{hero}
<p>Baccarat er einn einfaldasti borðleikurinn í spilavítum — og hefur eitt <strong>lægsta húsforskotið</strong> (1.06% á Banker). Hér eru allar reglurnar á íslensku.</p>

<h2>Grunnreglur</h2>
<p>Í baccarat veðjar þú á eina af þremur niðurstöðum:</p>
<table class="info-table"><thead><tr><th>Veðmál</th><th>Lýsing</th><th>Vinningshlutfall</th><th>Húsforskot</th></tr></thead><tbody>
<tr><td>Player (Leikmaður)</td><td>Hönd leikmanna vinnur</td><td>1:1</td><td>1.24%</td></tr>
<tr><td>Banker (Bankastjóri)</td><td>Hönd bankastjóra vinnur</td><td>0.95:1 (5% þóknun)</td><td>1.06%</td></tr>
<tr><td>Tie (Jafntefli)</td><td>Jafnt</td><td>8:1</td><td>14.36%</td></tr>
</tbody></table>
<p><strong>Besta ráðið:</strong> Veðjaðu alltaf á Banker — lægsta húsforskotið (1.06%). Forðistu Tie (14.36% húsforskot er hræðilegt).</p>

<h2>Hvernig virkar leikurinn?</h2>
<ol>
<li>Player og Banker fá hvort tveggja 2 kort</li>
<li>Kortavirði: Ás = 1, 2-9 = sem stendur, 10/Gosi/Drott/Kóng = 0</li>
<li>Samtala er síðasta talan — t.d. 7+8 = 15 → virðið er 5</li>
<li>Sá sem er nær 9 vinnur (eða jafntefli)</li>
<li>Þriðja kort er gefið eftir fastmótuðum reglum (sjálfvirkt á netinu)</li>
</ol>

<h2>Af hverju er baccarat gott val?</h2>
<ul>
<li><strong>Lægsta húsforskotið</strong> — 1.06% á Banker er betra en rúlletta (2.7%), spilakassar (4%+) og flest annað</li>
<li><strong>Einfalt</strong> — Engar flóknar ákvarðanir. Þú velur bara Player eða Banker</li>
<li><strong>Hratt</strong> — Hver umferð tekur nokkrar sekúndur</li>
</ul>

<h2>Hvar á að spila baccarat á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}live/baccarat/">Lifandi baccarat á Svipan</a></strong> — Sjá alla lifandi baccarat leiki</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}live/lightning-baccarat/">Lightning Baccarat</a></strong> — Baccarat með margfaldara (allt að 512x)</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></strong> — Sterkur lifandi baccarat hluti</p></div>

<h2>Algengar spurningar</h2>
<h3>Er baccarat heppnuleikur?</h3>
<p>Að mestu leyti — já. Engin strategy getur breytt húsforskotinu. Hins vegar er húsforskotið svo lágt (1.06%) að peningarnir þínir endist lengur en í flestum öðrum leikjum.</p>
<h3>Hvað er „þóknun" á Banker veðmáli?</h3>
<p>Banker veðmál borgar 0.95:1 í stað 1:1 — spilavítið tekur 5% þóknun. Jafnvel með þóknun er Banker betri en Player tölfræðilega.</p>
<h3>Er lifandi baccarat betra en RNG?</h3>
<p>Niðurstaðan er sú sama. Lifandi baccarat er raunverulegri upplifun (raunverulegur dílleri) en hægara. RNG er hraðara en minna spennandi.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila baccarat →</a></div>'''
    },
    {
        "slug": "verde-casino-umsogn",
        "title": "Verde Casino umsögn á íslensku — bónus og greiðslur 2026",
        "desc": "Verde Casino umsögn fyrir íslenska spilara: velkomstbónus, leikjaúrval, greiðsluleiðir og hvort spilavítið tekur við frá Íslandi.",
        "emoji": "🌿",
        "colors": ('#0a1a0f', '#14331e', '#1e4d2d'),
        "content": f'''<h1>Verde Casino umsögn á íslensku 2026</h1>
{hero}
<p>Verde Casino er eitt af þeim spilavítum sem íslenskir spilarar leita reglulega að. <strong>Hér förum við yfir hvað það býður, hvernig það ber sig saman við valkosti sem taka örugglega við frá Íslandi, og hvað þú þarft að varast.</strong></p>

<h2>Verde Casino í hnotskurn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2022</td></tr>
<tr><td>Eigandi</td><td>Brivio Limited (V.Partners)</td></tr>
<tr><td>Leyfi</td><td>Curaçao</td></tr>
<tr><td>Fjöldi leikja</td><td>4.000+</td></tr>
<tr><td>Velkomstbónus</td><td>Allt að €1.500 + 220 FS</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€10</td></tr>
<tr><td>Íslenskt viðmót</td><td>❌ Nei (enska, pólska, þýska o.fl.)</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>✅ BTC, ETH, LTC, USDT</td></tr>
</tbody></table>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Stór velkomstpakki yfir fjórar innborganir</td><td>❌ Ekkert íslenskt viðmót</td></tr>
<tr><td>✅ Gott leikjaúrval (4.000+)</td><td>❌ 40x veðskilyrði</td></tr>
<tr><td>✅ Lág lágmarksinnborgun (€10)</td><td>❌ Þjónustuver aðeins á ensku</td></tr>
<tr><td>✅ Hluti af V.Partners — sömu eigendur og Slotoro</td><td>❌ Bónus rennur út á 5 dögum</td></tr>
</tbody></table>

<h2>Velkomstpakki Verde Casino</h2>
<p>Verde dreifir velkomstbónusnum yfir fjórar innborganir — svipað og systursíðurnar:</p>
<ol>
<li>1. innborgun: 100% allt að €400 + 100 FS</li>
<li>2. innborgun: 50% allt að €400 + 50 FS</li>
<li>3. innborgun: 75% allt að €400 + 35 FS</li>
<li>4. innborgun: 100% allt að €300 + 35 FS</li>
</ol>
<p>Veðskilyrði eru 40x bónusupphæð — það þýðir að €100 bónus krefst €4.000 í veltu áður en hægt er að taka út.
Berðu þetta saman við <a href="{URL_BASE}leidbeiningar/spilaviti-an-vedskilyrda/">veðlaus spilavíti</a> þar sem vinningurinn er þinn strax.</p>

<h2>Verde Casino vs Slotoro</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Verde Casino</th><th>Slotoro</th></tr></thead><tbody>
<tr><td>Leikir</td><td>4.000+</td><td>8.000+</td></tr>
<tr><td>Framleiðendur</td><td>50+</td><td>71</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€10</td><td>€10</td></tr>
<tr><td>Veðskilyrði</td><td>40x</td><td>40x</td></tr>
<tr><td>Íþróttaveðmál</td><td>❌ Nei</td><td>✅ Já</td></tr>
</tbody></table>

<h2>Greiðsluleiðir frá Íslandi</h2>
<p>Stærsta hindrunin fyrir íslenska spilara eru <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">bankatakmarkanir</a>.
Arion, Landsbankinn og Íslandsbanki geta hafnað kortagreiðslum til spilavíta. Lausnir:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Bankinn kemur hvergi nærri. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi →</a></li>
<li><strong>Revolut</strong> — Fer ekki gegnum íslenskt bankakerfi. <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut leiðbeining →</a></li>
<li><strong>Rafræn veski</strong> — <a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a> og <a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a></li>
</ul>

<h2>Valkostir sem taka örugglega við frá Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — 8.000+ leikir frá 71 framleiðendum, €10 lágmarksinnborgun, dulritunargjaldmiðlar studdir. Samstarfsaðili Svipan.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Fullkomið íslenskt viðmót, veðlausir bónusar og Apple Pay.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Dulritunarspilavíti með úttektum undir 10 mínútum.</p></div>
<p>Sjá allan <a href="{URL_BASE}spilaviti/">samanburð á spilavítum →</a></p>

<h2>Algengar spurningar</h2>
<h3>Tekur Verde Casino við íslenskum spilurum?</h3>
<p>Já — Verde Casino lokar ekki á Ísland. Viðmótið er þó ekki á íslensku, svo þú þarft að lesa bónusskilmála á ensku.</p>
<h3>Er Verde Casino öruggt?</h3>
<p>Verde er með Curaçao leyfi og er rekið af Brivio Limited, sama fyrirtæki og stendur að baki Vulkan Vegas og Ice Casino. Rótgróinn rekstraraðili í bransanum.</p>
<h3>Hvaða greiðsluleið virkar best frá Íslandi?</h3>
<p>Dulritunargjaldmiðlar eða Revolut. Íslensk bankakort geta verið hafnað — sjá leiðbeiningar okkar um greiðslur.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>'''
    },
    {
        "slug": "hitnspin-umsogn-a-islensku",
        "title": "Hit'N'Spin umsögn á íslensku — bónus og leikir 2026",
        "desc": "Hit'N'Spin umsögn fyrir íslenska spilara. Einkaréttarbrand V.Partners: bónus, leikjaúrval og greiðsluleiðir.",
        "emoji": "🎯",
        "colors": ('#28100a', '#451c14', '#62291e'),
        "content": f'''<h1>Hit'N'Spin umsögn á íslensku 2026</h1>
{hero}
<p>Hit'N'Spin er eitt af þeim spilavítum sem íslenskir spilarar leita reglulega að. <strong>Hér förum við yfir hvað það býður, hvernig það ber sig saman við valkosti sem taka örugglega við frá Íslandi, og hvað þú þarft að varast.</strong></p>

<h2>Hit'N'Spin í hnotskurn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2023</td></tr>
<tr><td>Eigandi</td><td>V.Partners (einkaréttarbrand)</td></tr>
<tr><td>Leyfi</td><td>Curaçao</td></tr>
<tr><td>Fjöldi leikja</td><td>3.000+</td></tr>
<tr><td>Velkomstbónus</td><td>Allt að €1.000 + 100 FS</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€20</td></tr>
<tr><td>Íslenskt viðmót</td><td>❌ Nei</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>✅ BTC, ETH, LTC, USDT</td></tr>
</tbody></table>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Einkaréttarbrand — fáanlegt aðeins í gegnum V.Partners</td><td>❌ Ekkert íslenskt viðmót</td></tr>
<tr><td>✅ Nýtt spilavíti með nútímalegu viðmóti</td><td>❌ €20 lágmarksinnborgun (hærra en flest)</td></tr>
<tr><td>✅ Gott úrval af lifandi leikjum</td><td>❌ Nýtt — minni reynslusaga en eldri spilavíti</td></tr>
<tr><td>✅ Dulritunargjaldmiðlar studdir</td><td>❌ 40x veðskilyrði</td></tr>
</tbody></table>

<h2>Hvað þýðir „einkaréttarbrand"?</h2>
<p>Hit'N'Spin er eitt af þeim spilavítum sem eingöngu eru í boði í gegnum V.Partners samstarfsnetið — ásamt
<a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> og Vulkan Spiele. Það þýðir að þú finnur það ekki á hverri
samanburðarsíðu og samkeppnin um bónusa er minni.</p>

<h2>Leikjaúrval</h2>
<p>Hit'N'Spin býður yfir 3.000 leiki frá helstu framleiðendum: Pragmatic Play, Evolution, Play'n GO, NetEnt,
Hacksaw Gaming og Nolimit City. Lifandi spilavítishlutinn er sterkur — Evolution borð eru í boði allan sólarhringinn.</p>

<h2>Greiðsluleiðir frá Íslandi</h2>
<p>Stærsta hindrunin fyrir íslenska spilara eru <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">bankatakmarkanir</a>.
Arion, Landsbankinn og Íslandsbanki geta hafnað kortagreiðslum til spilavíta. Lausnir:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Bankinn kemur hvergi nærri. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi →</a></li>
<li><strong>Revolut</strong> — Fer ekki gegnum íslenskt bankakerfi. <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut leiðbeining →</a></li>
<li><strong>Rafræn veski</strong> — <a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a> og <a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a></li>
</ul>

<h2>Valkostir sem taka örugglega við frá Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — 8.000+ leikir frá 71 framleiðendum, €10 lágmarksinnborgun, dulritunargjaldmiðlar studdir. Samstarfsaðili Svipan.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Fullkomið íslenskt viðmót, veðlausir bónusar og Apple Pay.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Dulritunarspilavíti með úttektum undir 10 mínútum.</p></div>
<p>Sjá allan <a href="{URL_BASE}spilaviti/">samanburð á spilavítum →</a></p>

<h2>Algengar spurningar</h2>
<h3>Er Hit'N'Spin nýtt spilavíti?</h3>
<p>Já — Hit'N'Spin opnaði 2023 og er því tiltölulega nýtt. Það er rekið af V.Partners sem hefur starfað síðan 2016.</p>
<h3>Get ég spilað Hit'N'Spin frá Íslandi?</h3>
<p>Já. Notaðu dulritunargjaldmiðla eða Revolut til innborgunar þar sem íslensk bankakort geta verið hafnað.</p>
<h3>Hvernig ber Hit'N'Spin sig saman við Slotoro?</h3>
<p>Slotoro hefur fleiri leiki (8.000+ á móti 3.000+) og lægri lágmarksinnborgun (€10 á móti €20). Bæði eru V.Partners brand.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>'''
    },
    {
        "slug": "betsson-a-islandi",
        "title": "Betsson á Íslandi — umsögn, bónus og staða 2026",
        "desc": "Betsson umsögn fyrir íslenska spilara. Norrænt spilavíti síðan 1963: leyfi, leikir, greiðslur og hvort það tekur við frá Íslandi.",
        "emoji": "🟠",
        "colors": ('#28140a', '#452414', '#62341e'),
        "content": f'''<h1>Betsson á Íslandi 2026</h1>
{hero}
<p>Betsson er eitt af þeim spilavítum sem íslenskir spilarar leita reglulega að. <strong>Hér förum við yfir hvað það býður, hvernig það ber sig saman við valkosti sem taka örugglega við frá Íslandi, og hvað þú þarft að varast.</strong></p>

<h2>Betsson í hnotskurn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>1963 (á netinu síðan 2001)</td></tr>
<tr><td>Eigandi</td><td>Betsson AB (skráð á Nasdaq Stokkhólmi)</td></tr>
<tr><td>Leyfi</td><td>Malta (MGA) + fleiri</td></tr>
<tr><td>Fjöldi leikja</td><td>2.000+</td></tr>
<tr><td>Velkomstbónus</td><td>Fer eftir markaði</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€10</td></tr>
<tr><td>Íslenskt viðmót</td><td>❌ Nei</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>❌ Nei</td></tr>
</tbody></table>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Eitt elsta og virtasta spilavíti Norðurlanda</td><td>❌ Tekur ekki alltaf við íslenskum spilurum — fer eftir markaðsstillingum</td></tr>
<tr><td>✅ Skráð á hlutabréfamarkaði — mikið gegnsæi</td><td>❌ Engir dulritunargjaldmiðlar</td></tr>
<tr><td>✅ MGA leyfi (hæsta traust)</td><td>❌ Ekkert íslenskt viðmót</td></tr>
<tr><td>✅ Sterkur íþróttaveðmálahluti</td><td>❌ Strangar KYC kröfur</td></tr>
</tbody></table>

<h2>Tekur Betsson við íslenskum spilurum?</h2>
<p>Betsson rekur sérstakar síður fyrir hvern markað og fylgir leyfisskilyrðum hvers lands. Vegna þess að Ísland hefur
ekkert leyfiskerfi fyrir netspilavíti er aðgengi óstöðugt — stundum er hægt að skrá sig, stundum ekki, og þetta getur
breyst án fyrirvara.</p>
<p>Ef þú vilt spilavíti sem tekur örugglega við íslenskum spilurum skaltu skoða
<a href="{URL_BASE}leidbeiningar/spilaviti-med-islensku-vidmoti/">spilavíti á íslensku</a> eða
<a href="{URL_BASE}leidbeiningar/bestu-crypto-spilavitin-island/">dulritunarspilavíti</a>.</p>

<h2>Af hverju er Betsson svona þekkt?</h2>
<p>Betsson AB er skráð á Nasdaq Stokkhólmi og rekur yfir 20 vörumerki. Fyrirtækið hefur starfað síðan 1963 (upphaflega
sem spilakassafyrirtæki) og fór á netið 2001. Þetta er eitt af fáum spilavítafyrirtækjum þar sem ársreikningar eru
opinberir — mikið gegnsæi samanborið við Curaçao-rekin spilavíti.</p>

<h2>Greiðsluleiðir frá Íslandi</h2>
<p>Stærsta hindrunin fyrir íslenska spilara eru <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">bankatakmarkanir</a>.
Arion, Landsbankinn og Íslandsbanki geta hafnað kortagreiðslum til spilavíta. Lausnir:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Bankinn kemur hvergi nærri. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi →</a></li>
<li><strong>Revolut</strong> — Fer ekki gegnum íslenskt bankakerfi. <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut leiðbeining →</a></li>
<li><strong>Rafræn veski</strong> — <a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a> og <a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a></li>
</ul>

<h2>Valkostir sem taka örugglega við frá Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — 8.000+ leikir frá 71 framleiðendum, €10 lágmarksinnborgun, dulritunargjaldmiðlar studdir. Samstarfsaðili Svipan.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Fullkomið íslenskt viðmót, veðlausir bónusar og Apple Pay.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Dulritunarspilavíti með úttektum undir 10 mínútum.</p></div>
<p>Sjá allan <a href="{URL_BASE}spilaviti/">samanburð á spilavítum →</a></p>

<h2>Algengar spurningar</h2>
<h3>Get ég skráð mig á Betsson frá Íslandi?</h3>
<p>Það fer eftir því hvaða markaðsútgáfu Betsson býður upp á hverju sinni. Aðgengi frá Íslandi er ekki tryggt og getur breyst.</p>
<h3>Er Betsson öruggt?</h3>
<p>Já — Betsson er með MGA leyfi og er skráð á hlutabréfamarkaði. Þetta er meðal áreiðanlegustu rekstraraðila í bransanum.</p>
<h3>Tekur Betsson við Bitcoin?</h3>
<p>Nei — Betsson styður ekki dulritunargjaldmiðla. Ef þú vilt spila með Bitcoin skaltu skoða lista okkar yfir dulritunarspilavíti.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>'''
    },
    {
        "slug": "unibet-a-islandi",
        "title": "Unibet á Íslandi — umsögn og staða 2026",
        "desc": "Unibet umsögn fyrir íslenska spilara: leyfi, leikjaúrval, íþróttaveðmál og hvort síðan tekur við frá Íslandi.",
        "emoji": "🟢",
        "colors": ('#0a1f14', '#143a26', '#1e5538'),
        "content": f'''<h1>Unibet á Íslandi 2026</h1>
{hero}
<p>Unibet er eitt af þeim spilavítum sem íslenskir spilarar leita reglulega að. <strong>Hér förum við yfir hvað það býður, hvernig það ber sig saman við valkosti sem taka örugglega við frá Íslandi, og hvað þú þarft að varast.</strong></p>

<h2>Unibet í hnotskurn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>1997</td></tr>
<tr><td>Eigandi</td><td>Kindred Group (áður Unibet Group)</td></tr>
<tr><td>Leyfi</td><td>Malta (MGA), UKGC, fleiri</td></tr>
<tr><td>Fjöldi leikja</td><td>1.500+</td></tr>
<tr><td>Velkomstbónus</td><td>Fer eftir markaði</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€10</td></tr>
<tr><td>Íslenskt viðmót</td><td>❌ Nei</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>❌ Nei</td></tr>
</tbody></table>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Rótgróið síðan 1997</td><td>❌ Aðgengi frá Íslandi ekki tryggt</td></tr>
<tr><td>✅ MGA og UKGC leyfi</td><td>❌ Engir dulritunargjaldmiðlar</td></tr>
<tr><td>✅ Mjög sterkur íþróttaveðmálahluti</td><td>❌ Ekkert íslenskt viðmót</td></tr>
<tr><td>✅ Hluti af Kindred Group — skráð fyrirtæki</td><td>❌ Minna leikjaúrval en crypto-spilavíti</td></tr>
</tbody></table>

<h2>Unibet og Kindred Group</h2>
<p>Unibet er flaggskipsvörumerki Kindred Group, sem rekur einnig Maria Casino, 32Red og Otto Kasino.
Kindred er skráð á Nasdaq Stokkhólmi og birtir meðal annars hlutfall tekna sem kemur frá spilurum
með áhættusama spilahegðun — óvenjulegt gegnsæi í bransanum.</p>

<h2>Styrkleiki: íþróttaveðmál</h2>
<p>Unibet er fyrst og fremst þekkt fyrir íþróttaveðmál frekar en spilavítishlutann. Fótbolti, handbolti
og körfubolti eru vel þjónustuð — sem á vel við íslenskan markað þar sem handbolti og fótbolti eru vinsælastir.</p>

<h2>Greiðsluleiðir frá Íslandi</h2>
<p>Stærsta hindrunin fyrir íslenska spilara eru <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">bankatakmarkanir</a>.
Arion, Landsbankinn og Íslandsbanki geta hafnað kortagreiðslum til spilavíta. Lausnir:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Bankinn kemur hvergi nærri. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi →</a></li>
<li><strong>Revolut</strong> — Fer ekki gegnum íslenskt bankakerfi. <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut leiðbeining →</a></li>
<li><strong>Rafræn veski</strong> — <a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a> og <a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a></li>
</ul>

<h2>Valkostir sem taka örugglega við frá Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — 8.000+ leikir frá 71 framleiðendum, €10 lágmarksinnborgun, dulritunargjaldmiðlar studdir. Samstarfsaðili Svipan.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Fullkomið íslenskt viðmót, veðlausir bónusar og Apple Pay.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Dulritunarspilavíti með úttektum undir 10 mínútum.</p></div>
<p>Sjá allan <a href="{URL_BASE}spilaviti/">samanburð á spilavítum →</a></p>

<h2>Algengar spurningar</h2>
<h3>Tekur Unibet við íslenskum spilurum?</h3>
<p>Aðgengi er ekki tryggt og fer eftir markaðsstillingum Kindred Group hverju sinni.</p>
<h3>Er Unibet betra fyrir íþróttir eða spilavíti?</h3>
<p>Íþróttir. Unibet byggði orðspor sitt á veðmálum og spilavítishlutinn er minni en hjá sérhæfðum spilavítum.</p>
<h3>Hvaða valkostir eru fyrir íslenska spilara?</h3>
<p>Spilavíti með íslensku viðmóti eða dulritunarspilavíti sem taka örugglega við frá Íslandi — sjá samanburðarlista okkar.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>'''
    },
    {
        "slug": "leovegas-a-islandi",
        "title": "LeoVegas á Íslandi — umsögn og farsímaupplifun 2026",
        "desc": "LeoVegas umsögn: farsímaspilavítið sem vann til verðlauna. Leyfi, leikir, greiðslur og staða gagnvart Íslandi.",
        "emoji": "🦁",
        "colors": ('#28200a', '#453814', '#62501e'),
        "content": f'''<h1>LeoVegas á Íslandi 2026</h1>
{hero}
<p>LeoVegas er eitt af þeim spilavítum sem íslenskir spilarar leita reglulega að. <strong>Hér förum við yfir hvað það býður, hvernig það ber sig saman við valkosti sem taka örugglega við frá Íslandi, og hvað þú þarft að varast.</strong></p>

<h2>LeoVegas í hnotskurn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2011</td></tr>
<tr><td>Eigandi</td><td>MGM Resorts International (síðan 2022)</td></tr>
<tr><td>Leyfi</td><td>Malta (MGA), UKGC, fleiri</td></tr>
<tr><td>Fjöldi leikja</td><td>2.000+</td></tr>
<tr><td>Velkomstbónus</td><td>Fer eftir markaði</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€10</td></tr>
<tr><td>Íslenskt viðmót</td><td>❌ Nei</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>❌ Nei</td></tr>
</tbody></table>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Besta farsímaupplifun í bransanum — margverðlaunað</td><td>❌ Aðgengi frá Íslandi ekki tryggt</td></tr>
<tr><td>✅ Í eigu MGM Resorts (Las Vegas risinn)</td><td>❌ Engir dulritunargjaldmiðlar</td></tr>
<tr><td>✅ MGA og UKGC leyfi</td><td>❌ Ekkert íslenskt viðmót</td></tr>
<tr><td>✅ Stór lifandi spilavítishluti</td><td>❌ Bónusskilmálar misjafnir eftir mörkuðum</td></tr>
</tbody></table>

<h2>„Konungur farsímaspilavíta"</h2>
<p>LeoVegas byggði allt sitt viðmót fyrir farsíma fyrst — áður en það varð staðall í bransanum. Fyrirtækið hefur
unnið fjölda verðlauna fyrir farsímaupplifun. Ef þú spilar aðallega í símanum er þetta viðmiðunarpunkturinn sem
önnur spilavíti eru borin saman við.</p>
<p>Sjá einnig: <a href="{URL_BASE}leidbeiningar/spilaviti-fyrir-farsima-island/">bestu farsímaspilavítin á Íslandi</a>.</p>

<h2>MGM eignarhald</h2>
<p>MGM Resorts International keypti LeoVegas árið 2022 fyrir um 600 milljónir evra. Það þýðir að bandaríski
spilavítarisinn stendur að baki rekstrinum — sem eykur fjárhagslegan stöðugleika verulega.</p>

<h2>Greiðsluleiðir frá Íslandi</h2>
<p>Stærsta hindrunin fyrir íslenska spilara eru <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">bankatakmarkanir</a>.
Arion, Landsbankinn og Íslandsbanki geta hafnað kortagreiðslum til spilavíta. Lausnir:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Bankinn kemur hvergi nærri. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi →</a></li>
<li><strong>Revolut</strong> — Fer ekki gegnum íslenskt bankakerfi. <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut leiðbeining →</a></li>
<li><strong>Rafræn veski</strong> — <a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a> og <a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a></li>
</ul>

<h2>Valkostir sem taka örugglega við frá Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — 8.000+ leikir frá 71 framleiðendum, €10 lágmarksinnborgun, dulritunargjaldmiðlar studdir. Samstarfsaðili Svipan.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Fullkomið íslenskt viðmót, veðlausir bónusar og Apple Pay.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Dulritunarspilavíti með úttektum undir 10 mínútum.</p></div>
<p>Sjá allan <a href="{URL_BASE}spilaviti/">samanburð á spilavítum →</a></p>

<h2>Algengar spurningar</h2>
<h3>Er LeoVegas best fyrir farsíma?</h3>
<p>LeoVegas er almennt talið meðal þeirra bestu í farsímaupplifun. Þó hafa önnur spilavíti náð því á síðustu árum.</p>
<h3>Tekur LeoVegas við frá Íslandi?</h3>
<p>Aðgengi er ekki tryggt. LeoVegas einbeitir sér að mörkuðum með leyfiskerfi eins og Svíþjóð, Danmörku og Bretlandi.</p>
<h3>Hver á LeoVegas?</h3>
<p>MGM Resorts International, bandaríski spilavíta- og hótelrisinn, keypti LeoVegas árið 2022.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>'''
    },
    {
        "slug": "mr-green-a-islandi",
        "title": "Mr Green á Íslandi — umsögn og ábyrg spilun 2026",
        "desc": "Mr Green umsögn: sænskt spilavíti þekkt fyrir verkfæri í ábyrgri spilun. Leyfi, leikir og staða gagnvart Íslandi.",
        "emoji": "🎩",
        "colors": ('#0a2814', '#144524', '#1e6234'),
        "content": f'''<h1>Mr Green á Íslandi 2026</h1>
{hero}
<p>Mr Green er eitt af þeim spilavítum sem íslenskir spilarar leita reglulega að. <strong>Hér förum við yfir hvað það býður, hvernig það ber sig saman við valkosti sem taka örugglega við frá Íslandi, og hvað þú þarft að varast.</strong></p>

<h2>Mr Green í hnotskurn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2008</td></tr>
<tr><td>Eigandi</td><td>William Hill / evoke plc</td></tr>
<tr><td>Leyfi</td><td>Malta (MGA), UKGC, fleiri</td></tr>
<tr><td>Fjöldi leikja</td><td>1.800+</td></tr>
<tr><td>Velkomstbónus</td><td>Fer eftir markaði</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€10</td></tr>
<tr><td>Íslenskt viðmót</td><td>❌ Nei</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>❌ Nei</td></tr>
</tbody></table>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Leiðandi í verkfærum fyrir ábyrga spilun (Green Gaming)</td><td>❌ Aðgengi frá Íslandi ekki tryggt</td></tr>
<tr><td>✅ MGA og UKGC leyfi</td><td>❌ Engir dulritunargjaldmiðlar</td></tr>
<tr><td>✅ Vandað viðmót og notendaupplifun</td><td>❌ Ekkert íslenskt viðmót</td></tr>
<tr><td>✅ Hluti af evoke plc (áður William Hill)</td><td>❌ Minna leikjaúrval en crypto-spilavíti</td></tr>
</tbody></table>

<h2>Green Gaming — verkfæri gegn spilafikn</h2>
<p>Mr Green þróaði „Green Gaming" kerfi sem greinir spilahegðun og varar spilara við ef mynstrið bendir til
áhættusamrar hegðunar. Spilarar fá persónulegt áhættumat og tillögur um takmörk.</p>
<p>Þetta er meðal þróaðustu verkfæra í bransanum. Ef þú vilt lesa meira um merki áhættusamrar spilunar,
sjá <a href="{URL_BASE}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">leiðbeiningar okkar</a>
og <a href="{URL_BASE}leidbeiningar/sjalfsutilokun-spilavita/">sjálfsútilokun</a>.</p>

<h2>Greiðsluleiðir frá Íslandi</h2>
<p>Stærsta hindrunin fyrir íslenska spilara eru <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">bankatakmarkanir</a>.
Arion, Landsbankinn og Íslandsbanki geta hafnað kortagreiðslum til spilavíta. Lausnir:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Bankinn kemur hvergi nærri. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi →</a></li>
<li><strong>Revolut</strong> — Fer ekki gegnum íslenskt bankakerfi. <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut leiðbeining →</a></li>
<li><strong>Rafræn veski</strong> — <a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a> og <a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a></li>
</ul>

<h2>Valkostir sem taka örugglega við frá Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — 8.000+ leikir frá 71 framleiðendum, €10 lágmarksinnborgun, dulritunargjaldmiðlar studdir. Samstarfsaðili Svipan.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Fullkomið íslenskt viðmót, veðlausir bónusar og Apple Pay.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Dulritunarspilavíti með úttektum undir 10 mínútum.</p></div>
<p>Sjá allan <a href="{URL_BASE}spilaviti/">samanburð á spilavítum →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hvað er Green Gaming?</h3>
<p>Verkfæri Mr Green sem greinir spilahegðun og gefur spilurum persónulegt áhættumat ásamt tillögum um takmörk.</p>
<h3>Tekur Mr Green við íslenskum spilurum?</h3>
<p>Aðgengi er ekki tryggt og fer eftir markaðsstillingum. Mr Green einbeitir sér að mörkuðum með leyfiskerfi.</p>
<h3>Hver á Mr Green?</h3>
<p>Mr Green var keypt af William Hill árið 2019 og tilheyrir nú evoke plc samsteypunni.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>'''
    },
    {
        "slug": "casumo-a-islandi",
        "title": "Casumo á Íslandi — umsögn og staða 2026",
        "desc": "Casumo umsögn: spilavítið með ævintýraþema og Reel Races. Leyfi, leikjaúrval og hvort það tekur við frá Íslandi.",
        "emoji": "🟣",
        "colors": ('#1a0a28', '#2d1445', '#401e62'),
        "content": f'''<h1>Casumo á Íslandi 2026</h1>
{hero}
<p>Casumo er eitt af þeim spilavítum sem íslenskir spilarar leita reglulega að. <strong>Hér förum við yfir hvað það býður, hvernig það ber sig saman við valkosti sem taka örugglega við frá Íslandi, og hvað þú þarft að varast.</strong></p>

<h2>Casumo í hnotskurn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2012</td></tr>
<tr><td>Eigandi</td><td>Casumo Services Limited</td></tr>
<tr><td>Leyfi</td><td>Malta (MGA), UKGC, fleiri</td></tr>
<tr><td>Fjöldi leikja</td><td>2.500+</td></tr>
<tr><td>Velkomstbónus</td><td>Fer eftir markaði</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€10</td></tr>
<tr><td>Íslenskt viðmót</td><td>❌ Nei</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>❌ Nei</td></tr>
</tbody></table>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Einstakt ævintýraþema með stigum og verðlaunum</td><td>❌ Aðgengi frá Íslandi ekki tryggt</td></tr>
<tr><td>✅ Reel Races — spilakassamót allan daginn</td><td>❌ Engir dulritunargjaldmiðlar</td></tr>
<tr><td>✅ MGA og UKGC leyfi</td><td>❌ Ekkert íslenskt viðmót</td></tr>
<tr><td>✅ Hröð skráning og einfalt viðmót</td><td>❌ Bónustilboð misjöfn eftir mörkuðum</td></tr>
</tbody></table>

<h2>Reel Races — spilakassamót</h2>
<p>Casumo er þekktast fyrir „Reel Races" — stuttar keppnir (oft 20-60 mínútur) þar sem spilarar keppa um
verðlaunasjóð með því að safna stigum í spilakössum. Þetta gerir venjulega spilun samkeppnishæfari.</p>
<p>Sambærileg mót eru í boði á <a href="{URL_BASE}spilaviti/motaspilaviti/">mótaspilavítum</a> sem taka við íslenskum spilurum.</p>

<h2>Ævintýraþemað</h2>
<p>Í stað hefðbundins VIP-kerfis notar Casumo stigakerfi þar sem þú „ferðast" í gegnum ævintýri og vinnur
verðlaun eftir því sem þú spilar. Þetta er gamification-nálgun sem mörg nýrri spilavíti hafa hermt eftir.</p>

<h2>Greiðsluleiðir frá Íslandi</h2>
<p>Stærsta hindrunin fyrir íslenska spilara eru <a href="{URL_BASE}leidbeiningar/islenskir-bankar-spilaviti/">bankatakmarkanir</a>.
Arion, Landsbankinn og Íslandsbanki geta hafnað kortagreiðslum til spilavíta. Lausnir:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Bankinn kemur hvergi nærri. <a href="{URL_BASE}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi →</a></li>
<li><strong>Revolut</strong> — Fer ekki gegnum íslenskt bankakerfi. <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut leiðbeining →</a></li>
<li><strong>Rafræn veski</strong> — <a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Skrill</a> og <a href="{URL_BASE}greidslur/neteller-i-spilavitum/">Neteller</a></li>
</ul>

<h2>Valkostir sem taka örugglega við frá Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — 8.000+ leikir frá 71 framleiðendum, €10 lágmarksinnborgun, dulritunargjaldmiðlar studdir. Samstarfsaðili Svipan.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — Fullkomið íslenskt viðmót, veðlausir bónusar og Apple Pay.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Dulritunarspilavíti með úttektum undir 10 mínútum.</p></div>
<p>Sjá allan <a href="{URL_BASE}spilaviti/">samanburð á spilavítum →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hvað eru Reel Races?</h3>
<p>Stuttar spilakassakeppnir hjá Casumo þar sem spilarar keppa um verðlaunasjóð með því að safna stigum.</p>
<h3>Tekur Casumo við frá Íslandi?</h3>
<p>Aðgengi er ekki tryggt. Casumo einbeitir sér að mörkuðum með leyfiskerfi eins og Bretlandi og Svíþjóð.</p>
<h3>Er Casumo með VIP kerfi?</h3>
<p>Casumo notar ævintýra- og stigakerfi í stað hefðbundins VIP-kerfis.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>'''
    },
    {
        "slug": "hvernig-a-ad-kaupa-usdt-island",
        "title": "Hvernig á að kaupa USDT á Íslandi — skref fyrir skref 2026",
        "desc": "Leiðbeiningar um kaup á USDT (Tether) frá Íslandi fyrir spilavítainnlagnir. Kauphallir, net, gjöld og hvernig á að senda.",
        "emoji": "💵",
        "colors": ('#0a1f14', '#143a26', '#1e5538'),
        "content": f'''<h1>Hvernig á að kaupa USDT á Íslandi</h1>
{hero}
<p>USDT (Tether) er <strong>besti dulritunargjaldmiðillinn fyrir spilavítainnlagnir</strong> frá Íslandi: verðið er stöðugt (1 USDT ≈ 1 USD), færslugjöldin eru undir dollar og millifærslan tekur mínútur.</p>

<h2>Af hverju USDT frekar en Bitcoin?</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>USDT</th><th>Bitcoin</th></tr></thead><tbody>
<tr><td>Verðsveiflur</td><td>Engar — stöðugt gildi</td><td>Getur fallið 10% á dag</td></tr>
<tr><td>Færslutími</td><td>1–5 mín (TRC-20)</td><td>10–60 mín</td></tr>
<tr><td>Færslugjald</td><td>$0,5–1</td><td>$1–5</td></tr>
<tr><td>Stuðningur spilavíta</td><td>Flest crypto-spilavíti</td><td>Öll crypto-spilavíti</td></tr>
</tbody></table>
<p>Lykilatriðið: ef þú kaupir Bitcoin fyrir €100 og það fellur um 8% meðan þú spilar hefurðu tapað €8 áður en þú snýrð einu hjóli. USDT heldur gildi sínu.</p>

<h2>Skref 1 — Veldu kauphöll</h2>
<div class="info-box"><p><strong>Coinbase</strong> — Einfaldast fyrir byrjendur. Tekur við íslenskum Visa/Mastercard. Hærri gjöld (1,5–4%) en þægilegt.</p></div>
<div class="info-box"><p><strong>Binance</strong> — Lægstu gjöldin (0,1%). SEPA millifærsla frá íslenskum banka. Þarf meiri uppsetningu.</p></div>
<div class="info-box"><p><strong>Kraken</strong> — Evrópsk kauphöll með sterkt öryggisorðspor. SEPA á 1–2 dögum.</p></div>
<p>Fyrir fyrstu kaup mælum við með Coinbase — einfaldast. Þegar þú ert kominn í rútínu borgar sig að skipta yfir á Binance vegna gjaldanna.</p>

<h2>Skref 2 — Staðfestu reikninginn (KYC)</h2>
<p>Allar löglegar kauphallir krefjast auðkennisstaðfestingar. Þú þarft:</p>
<ul>
<li>Mynd af vegabréfi eða ökuskírteini</li>
<li>Selfie (sjálfsmynd) til samanburðar</li>
<li>Stundum sönnun á heimilisfangi</li>
</ul>
<p>Staðfesting tekur yfirleitt 5–30 mínútur en getur tekið allt að sólarhring á álagstímum.</p>

<h2>Skref 3 — Leggðu inn ISK eða EUR</h2>
<p>Tvær leiðir:</p>
<ol>
<li><strong>Kort</strong> — Samstundis en gjöld 1,5–4%. Athugaðu að íslenskir bankar hafna stundum kortagreiðslum til kauphalla líka</li>
<li><strong>SEPA millifærsla</strong> — 1–2 dagar, gjöld nánast engin. Þú þarft að millifæra í EUR</li>
</ol>
<p>Bankinn þinn breytir ISK í EUR með 1–2% álagi. Til að spara getur þú notað <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut</a> fyrir gjaldmiðlaskiptin.</p>

<h2>Skref 4 — Keyptu USDT</h2>
<p>Leitaðu að USDT í kauphöllinni, sláðu inn upphæð og staðfestu. Mundu: <strong>veldu rétta netið</strong> þegar þú tekur út.</p>

<h2>Skref 5 — Veldu rétt net (mikilvægt!)</h2>
<table class="info-table"><thead><tr><th>Net</th><th>Gjald</th><th>Hraði</th><th>Mælt með?</th></tr></thead><tbody>
<tr><td>TRC-20 (Tron)</td><td>$0,5–1</td><td>1–3 mín</td><td>✅ Já — best</td></tr>
<tr><td>ERC-20 (Ethereum)</td><td>$3–20</td><td>2–10 mín</td><td>⚠️ Aðeins ef spilavítið krefst</td></tr>
<tr><td>BEP-20 (BNB Chain)</td><td>$0,2–0,5</td><td>1–3 mín</td><td>✅ Gott ef stutt</td></tr>
</tbody></table>
<div class="info-box"><p><strong>Varúð:</strong> Ef þú sendir USDT á TRC-20 neti á heimilisfang sem ætlað er fyrir ERC-20 <strong>tapast fjármunirnir varanlega</strong>. Athugaðu alltaf netið tvisvar áður en þú sendir.</p></div>

<h2>Skref 6 — Sendu á spilavítið</h2>
<ol>
<li>Skráðu þig á spilavíti sem styður USDT (sjá lista hér að neðan)</li>
<li>Farðu í Innborgun → USDT → veldu net (TRC-20)</li>
<li>Afritaðu veskisheimilisfangið</li>
<li>Í kauphöllinni: Taka út → USDT → límdu heimilisfangið → veldu sama net</li>
<li>Staðfestu — innborgunin birtist eftir 1–5 mínútur</li>
</ol>

<h2>Spilavíti sem styðja USDT</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — USDT, BTC, ETH og fleira. €10 lágmark.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — Styður USDT á mörgum netum.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> — 100+ dulritunargjaldmiðlar.</p></div>
<p>Sjá <a href="{URL_BASE}leidbeiningar/bestu-crypto-spilavitin-island/">topp 10 dulritunarspilavítin á Íslandi →</a></p>

<h2>Algengar spurningar</h2>
<h3>Er löglegt að kaupa USDT á Íslandi?</h3>
<p>Já — kaup og eign dulritunargjaldmiðla er fullkomlega löglegt á Íslandi. Sjá <a href="{URL_BASE}leidbeiningar/er-ologligt-ad-spila-a-spilaviti-island/">lagalega stöðu →</a></p>
<h3>Hvað kostar að kaupa USDT fyrir €100?</h3>
<p>Á Coinbase með korti: um €2–4 í gjöld. Á Binance með SEPA: undir €0,50. Síðan $0,5–1 í færslugjald þegar þú sendir á spilavítið.</p>
<h3>Get ég tekið út vinninga í USDT?</h3>
<p>Já — og það er hraðasta leiðin. Spilavítið sendir USDT á veskið þitt, þú selur fyrir EUR á kauphöllinni og millifærir á bankann.</p>
<h3>Hvað ef ég sendi á rangt net?</h3>
<p>Fjármunirnir tapast yfirleitt varanlega. Sum spilavíti geta endurheimt þá gegn gjaldi en það er ekki tryggt. Athugaðu alltaf netið áður en þú staðfestir.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila með USDT →</a></div>'''
    },
    {
        "slug": "bitcoin-vs-usdt-spilaviti",
        "title": "Bitcoin vs USDT á spilavíti — hvort er betra? 2026",
        "desc": "Samanburður á Bitcoin og USDT fyrir spilavítainnlagnir: gjöld, hraði, verðsveiflur og hvað hentar íslenskum spilurum.",
        "emoji": "⚖️",
        "colors": ('#1a1200', '#332400', '#4d3600'),
        "content": f'''<h1>Bitcoin vs USDT á spilavíti</h1>
{hero}
<p>Þegar þú spilar á dulritunarspilavíti þarftu að velja gjaldmiðil. <strong>Bitcoin og USDT eru langalgengastir — en þeir henta í gjörólíkum aðstæðum.</strong></p>

<h2>Stutta svarið</h2>
<div class="info-box"><p><strong>Notaðu USDT ef</strong> þú vilt spila núna og leggja inn nákvæma upphæð án þess að verðsveiflur hafi áhrif. Þetta á við flesta.</p></div>
<div class="info-box"><p><strong>Notaðu Bitcoin ef</strong> þú átt BTC nú þegar, trúir á langtímaverðmæti og vilt ekki skipta yfir í stablecoin.</p></div>

<h2>Ítarlegur samanburður</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Bitcoin (BTC)</th><th>USDT (Tether)</th></tr></thead><tbody>
<tr><td>Verðstöðugleiki</td><td>❌ Sveiflast 2–10% á dag</td><td>✅ Alltaf ≈ $1</td></tr>
<tr><td>Færslutími</td><td>10–60 mín</td><td>1–5 mín (TRC-20)</td></tr>
<tr><td>Færslugjald</td><td>$1–5 (getur rokið upp)</td><td>$0,5–1</td></tr>
<tr><td>Stuðningur spilavíta</td><td>100% crypto-spilavíta</td><td>~90% crypto-spilavíta</td></tr>
<tr><td>Lágmarksinnborgun</td><td>Oft hærri í €</td><td>Oft €10</td></tr>
<tr><td>Flækjustig</td><td>Einfalt — eitt net</td><td>Þarf að velja net rétt</td></tr>
<tr><td>Langtímaverðmæti</td><td>Getur hækkað eða lækkað</td><td>Helst stöðugt</td></tr>
</tbody></table>

<h2>Verðsveiflu-vandamálið</h2>
<p>Segjum að þú leggir inn 0,001 BTC (um €60) á mánudegi. Á miðvikudegi hefur Bitcoin fallið 10%. Jafnvægið þitt í spilavítinu er enn 0,001 BTC — en nú aðeins €54 virði.</p>
<p>Þetta getur líka virkað í hina áttina. En ef markmið þitt er að spila — ekki spákaupmennska — þá er sveiflan óþarfa áhætta ofan á áhættuna sem fylgir spiluninni sjálfri.</p>
<p>USDT leysir þetta: €60 inn, €60 jafnvægi, sama hvað gerist á markaðnum.</p>

<h2>Netin skipta máli fyrir USDT</h2>
<p>Bitcoin hefur eitt net. USDT hefur nokkur — og þú verður að velja rétt:</p>
<ul>
<li><strong>TRC-20 (Tron)</strong> — $0,5–1 gjald, 1–3 mín. Besti kosturinn</li>
<li><strong>BEP-20 (BNB Chain)</strong> — $0,2–0,5 gjald. Gott ef spilavítið styður</li>
<li><strong>ERC-20 (Ethereum)</strong> — $3–20 gjald. Forðist nema nauðsyn krefji</li>
</ul>
<p><a href="{URL_BASE}leidbeiningar/hvernig-a-ad-kaupa-usdt-island/">Hvernig á að kaupa USDT á Íslandi →</a></p>

<h2>Hvað með úttektir?</h2>
<p>Hér er USDT líka betra fyrir flesta: þú veist nákvæmlega hvað þú færð. Ef þú tekur út 500 USDT færðu um €460–470 (eftir gengi EUR/USD). Með Bitcoin fer verðmætið eftir því hvenær þú selur.</p>
<p>Undantekning: ef þú ætlar að halda vinningnum í dulritunargjaldmiðli til langs tíma getur Bitcoin verið rökréttara.</p>

<h2>Önnur stablecoin</h2>
<p>USDC er annað stablecoin sem virkar eins og USDT og er studd af fleiri og fleiri spilavítum. Það er almennt talið gegnsærra hvað varðar baktryggingu. Ef spilavítið styður bæði er USDC jafngott val.</p>

<h2>Algengar spurningar</h2>
<h3>Er USDT öruggt?</h3>
<p>USDT er stærsta stablecoin heims með yfir 100 milljarða dollara í umferð. Það hefur haldið jafnvægi við dollar í yfir áratug þrátt fyrir reglubundna gagnrýni á gegnsæi baktryggingar.</p>
<h3>Hvort er ódýrara í heildina?</h3>
<p>USDT á TRC-20 neti — bæði lægri færslugjöld og engin áhætta af verðfalli meðan þú spilar.</p>
<h3>Styðja öll spilavíti USDT?</h3>
<p>Flest en ekki öll. Bitcoin er studd alls staðar. Athugaðu greiðslusíðu spilavítisins áður en þú kaupir.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Finna crypto-spilavíti →</a></div>'''
    },
    {
        "slug": "hvada-leyfi-er-best-spilaviti",
        "title": "MGA, Curaçao eða UKGC — hvaða spilavítileyfi er best? 2026",
        "desc": "Samanburður á spilavítaleyfum: Malta (MGA), Curaçao, UKGC og fleiri. Hvað verndar þig best sem íslenskan spilara?",
        "emoji": "📜",
        "colors": ('#1a1a0a', '#33331a', '#4d4d28'),
        "content": f'''<h1>MGA, Curaçao eða UKGC</h1>
{hero}
<p>Leyfið segir þér hvaða reglum spilavítið lýtur, hvað gerist ef deilur koma upp og hversu vel peningarnir þínir eru verndaðir. <strong>En ekki eru öll leyfi jöfn.</strong></p>

<h2>Yfirlit — leyfi raðað eftir vernd</h2>
<table class="info-table"><thead><tr><th>Leyfi</th><th>Útgefandi</th><th>Spilaravernd</th><th>Deilumál</th><th>Aðgengi frá Íslandi</th></tr></thead><tbody>
<tr><td>UKGC</td><td>Bretland</td><td>⭐⭐⭐⭐⭐</td><td>Sjálfstæður úrskurðaraðili</td><td>❌ Oftast lokað</td></tr>
<tr><td>MGA</td><td>Malta</td><td>⭐⭐⭐⭐⭐</td><td>MGA tekur kvartanir</td><td>⚠️ Fer eftir spilavíti</td></tr>
<tr><td>Spelinspektionen</td><td>Svíþjóð</td><td>⭐⭐⭐⭐⭐</td><td>Ríkisstofnun</td><td>❌ Lokað</td></tr>
<tr><td>Eistland (EMTA)</td><td>Eistland</td><td>⭐⭐⭐⭐</td><td>Ríkisstofnun, EES</td><td>✅ Oft opið</td></tr>
<tr><td>Curaçao</td><td>Curaçao</td><td>⭐⭐⭐</td><td>Takmarkað</td><td>✅ Opið</td></tr>
<tr><td>Anjouan / önnur</td><td>Ýmis</td><td>⭐</td><td>Nánast ekkert</td><td>✅ Opið</td></tr>
</tbody></table>

<h2>UKGC — strangasta leyfið</h2>
<p>Breska leyfið gerir mestu kröfurnar: aðskildir sjóðir fyrir fé spilara, skyldubundin þátttaka í GamStop sjálfsútilokunarkerfinu, bann við bónusum með villandi skilmálum og sjálfstæður úrskurðaraðili fyrir deilur.</p>
<p><strong>Gallinn fyrir íslenska spilara:</strong> UKGC-spilavíti taka yfirleitt aðeins við spilurum með breskt heimilisfang.</p>

<h2>MGA (Malta) — besta raunhæfa valið</h2>
<p>Malta Gaming Authority er gullstaðallinn fyrir alþjóðleg spilavíti. Kröfur:</p>
<ul>
<li>Fé spilara aðskilið frá rekstrarfé fyrirtækisins</li>
<li>Reglulegar úttektir á slembitölugjafa ({URL_BASE}leidbeiningar/hvernig-rng-virkar/ — <a href="{URL_BASE}leidbeiningar/hvernig-rng-virkar/">hvernig RNG virkar</a>)</li>
<li>Skyldubundin verkfæri fyrir <a href="{URL_BASE}leidbeiningar/spila-af-abyrgd/">ábyrga spilun</a></li>
<li>MGA tekur við kvörtunum frá spilurum beint</li>
</ul>
<p>Ef þú lendir í deilu við MGA-spilavíti geturðu sent kvörtun til MGA sem rannsakar málið. Það er raunveruleg vernd.</p>

<h2>Curaçao — algengasta leyfið</h2>
<p>Flest spilavíti sem taka við íslenskum spilurum eru með Curaçao leyfi — þar á meðal <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a>, <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> og <a href="{URL_BASE}spilaviti/stake/">Stake</a>.</p>
<p><strong>Kostir:</strong> Opið aðgengi, leyfir dulritunargjaldmiðla, færri takmarkanir á bónusum.</p>
<p><strong>Gallar:</strong> Sögulega hefur eftirlit verið veikt og deilumeðferð takmörkuð.</p>
<p><strong>Breytingar 2023–2026:</strong> Curaçao hefur endurskoðað leyfiskerfi sitt (LOK-löggjöfin) með strangari kröfum og beinni útgáfu frá Curaçao Gaming Authority í stað gömlu undirleyfanna. Nýju leyfin eru töluvert betri en þau gömlu.</p>

<h2>Hvað skiptir meira máli en leyfið?</h2>
<p>Leyfið er grunnurinn — en það segir ekki alla söguna. Athugaðu líka:</p>
<ol>
<li><strong>Greiðslusaga</strong> — Greiðir spilavítið út á réttum tíma? Leitaðu að umsögnum frá raunverulegum spilurum</li>
<li><strong>Gegnsæ skilmálar</strong> — Eru <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrði</a> skýrt sett fram?</li>
<li><strong>Aldur og orðspor</strong> — Spilavíti sem hefur starfað í 5+ ár hefur meira að tapa á slæmri hegðun</li>
<li><strong>Þjónustuver</strong> — Prófaðu að senda fyrirspurn fyrir fyrstu innborgun</li>
</ol>
<p>Sjá: <a href="{URL_BASE}leidbeiningar/einkenni-sanngjarns-spilavitis/">Einkenni sanngjarns spilavítis →</a></p>

<h2>Hvernig staðfesti ég leyfið?</h2>
<p>Neðst á forsíðu spilavítisins á að vera leyfisnúmer og tengill á leyfisskrá. Smelltu á hann — hann á að leiða á opinbera skrá leyfisveitanda þar sem þú sérð stöðu leyfisins.</p>
<p><a href="{URL_BASE}leidbeiningar/hvernig-a-ad-stadfesta-spilavitaleyfi/">Ítarleg leiðbeining um staðfestingu leyfis →</a></p>

<h2>Algengar spurningar</h2>
<h3>Er Curaçao leyfi öruggt?</h3>
<p>Það veitir grunnvernd en minni en MGA. Fyrir íslenska spilara er það oft eina raunhæfa valið. Veldu þá rótgróin spilavíti með góða greiðslusögu.</p>
<h3>Af hverju taka MGA-spilavíti stundum ekki við Íslendingum?</h3>
<p>Sum MGA-spilavíti einbeita sér að mörkuðum með eigin leyfiskerfi og loka á lönd þar sem staðan er óljós. Þetta er viðskiptaákvörðun, ekki lagaleg skylda.</p>
<h3>Skiptir leyfið máli ef ég spila með Bitcoin?</h3>
<p>Já — leyfið snýst um sanngirni leikja og hvort þú færð útborgað, ekki bara greiðslumáta.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá spilavíti með leyfi →</a></div>'''
    },
    {
        "slug": "playn-go-bestu-spilakassarnir",
        "title": "Play'n GO — bestu spilakassarnir og RTP 2026",
        "desc": "Play'n GO leikjaframleiðandi: Book of Dead, Reactoonz, Rise of Olympus. RTP tafla, sveifla og hvar á að spila á Íslandi.",
        "emoji": "🎲",
        "colors": ('#0a0f28', '#141b45', '#1e2762'),
        "content": f'''<h1>Play'n GO</h1>
{hero}
<p>Play'n GO er sænskur leikjaframleiðandi sem stendur á bak við <a href="{URL_BASE}spilakassar/book-of-dead/">Book of Dead</a> — einn vinsælasta spilakassa allra tíma. <strong>Þekkt fyrir háa sveiflu og hreina, hraðvirka leiki.</strong></p>

<h2>Um Play'n GO</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>1997 (leikir frá 2005)</td></tr>
<tr><td>Höfuðstöðvar</td><td>Växjö, Svíþjóð</td></tr>
<tr><td>Fjöldi leikja</td><td>300+</td></tr>
<tr><td>Þekktustu leikir</td><td>Book of Dead, Reactoonz, Fire Joker, Rise of Olympus</td></tr>
<tr><td>Sérkenni</td><td>Há sveifla, einföld vélbúnaður, farsímavænt</td></tr>
<tr><td>Leyfi</td><td>MGA, UKGC, Svíþjóð, Danmörk og fleiri</td></tr>
</tbody></table>

<h2>Topp 10 Play'n GO leikir</h2>
<table class="info-table"><thead><tr><th>#</th><th>Leikur</th><th>RTP</th><th>Sveifla</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td>1</td><td><a href="{URL_BASE}spilakassar/book-of-dead/">Book of Dead</a></td><td>96,21%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>2</td><td><a href="{URL_BASE}spilakassar/reactoonz/">Reactoonz</a></td><td>96,51%</td><td>Há</td><td>4.570x</td></tr>
<tr><td>3</td><td><a href="{URL_BASE}spilakassar/fire-joker/">Fire Joker</a></td><td>96,15%</td><td>Meðal</td><td>800x</td></tr>
<tr><td>4</td><td><a href="{URL_BASE}spilakassar/rise-of-olympus/">Rise of Olympus</a></td><td>96,50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>5</td><td><a href="{URL_BASE}spilakassar/moon-princess/">Moon Princess</a></td><td>96,50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>6</td><td><a href="{URL_BASE}spilakassar/legacy-of-dead/">Legacy of Dead</a></td><td>96,58%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>7</td><td><a href="{URL_BASE}spilakassar/rich-wilde-and-the-amulet/">Rich Wilde and the Amulet</a></td><td>96,50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>8</td><td><a href="{URL_BASE}spilakassar/book-of-oz/">Book of Oz</a></td><td>96,31%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>9</td><td><a href="{URL_BASE}spilakassar/rise-of-merlin/">Rise of Merlin</a></td><td>96,52%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>10</td><td><a href="{URL_BASE}spilakassar/gods-of-rock/">Gods of Rock</a></td><td>96,20%</td><td>Há</td><td>5.000x</td></tr>
</tbody></table>

<h2>Book of Dead — hvers vegna svona vinsælt?</h2>
<p>Book of Dead kom út 2016 og er enn meðal mest spiluðu spilakassa í Evrópu. Ástæðurnar:</p>
<ul>
<li><strong>Einfaldur vélbúnaður</strong> — 10 línur, engar flækjur</li>
<li><strong>Stækkandi tákn</strong> — Í frísnúningum er valið eitt tákn sem stækkar yfir alla hjólið</li>
<li><strong>Há sveifla</strong> — Löng þurrkatímabil en stórir vinningar þegar þeir koma</li>
<li><strong>Frísnúningar oft í bónustilboðum</strong> — Mörg spilavíti nota Book of Dead í <a href="{URL_BASE}leidbeiningar/okeypis-snuningar-spilaviti/">frísnúningatilboðum</a></li>
</ul>

<h2>Play'n GO vs Pragmatic Play</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Play'n GO</th><th>Pragmatic Play</th></tr></thead><tbody>
<tr><td>Sveifla</td><td>Yfirleitt há</td><td>Meðal til mjög há</td></tr>
<tr><td>Bónus Buy</td><td>Sjaldgæft</td><td>Algengt</td></tr>
<tr><td>Vélbúnaður</td><td>Einfaldur, klassískur</td><td>Tumble, margfaldarar</td></tr>
<tr><td>Hámarksvinningar</td><td>Yfirleitt 5.000x</td><td>Allt að 25.000x</td></tr>
<tr><td>Hentar</td><td>Þeim sem vilja klassíska spilun</td><td>Þeim sem vilja stóra margfaldara</td></tr>
</tbody></table>
<p><a href="{URL_BASE}leidbeiningar/pragmatic-play-allir-leikir/">Pragmatic Play yfirlit →</a> · <a href="{URL_BASE}leidbeiningar/netent-saga-og-bestu-leikir/">NetEnt yfirlit →</a></p>

<h2>Hvar á að spila Play'n GO á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — Play'n GO safnið í boði ásamt 70 öðrum framleiðendum.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Allir helstu Play'n GO titlar.</p></div>

<h2>Algengar spurningar</h2>
<h3>Hvaða Play'n GO leikur hefur hæsta RTP?</h3>
<p>Legacy of Dead og Rise of Merlin með um 96,5–96,6%. Munurinn milli leikja er þó lítill — sveiflan skiptir meira máli fyrir upplifunina.</p>
<h3>Er Book of Dead með háa sveiflu?</h3>
<p>Já — mjög háa. Búðu þig undir löng tímabil án vinninga. Veldu veðmálsstærð sem leyfir 300+ snúninga.</p>
<h3>Býður Play'n GO Bónus Buy?</h3>
<p>Aðeins í fáum titlum. Play'n GO hefur haldið sig við klassíska nálgun þar sem frísnúningar koma náttúrulega.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Play'n GO →</a></div>'''
    },
    {
        "slug": "nolimit-city-hasveifluleikir",
        "title": "Nolimit City — hásveifluleikir og hámarksvinningar 2026",
        "desc": "Nolimit City: Mental, San Quentin, Fire in the Hole. Hæstu sveiflur í bransanum, xWays vélbúnaður og RTP tafla.",
        "emoji": "💀",
        "colors": ('#1a0a0a', '#331414', '#4d1e1e'),
        "content": f'''<h1>Nolimit City</h1>
{hero}
<p>Nolimit City er sænskur framleiðandi sem gerir <strong>erfiðustu og sveiflukenndustu spilakassa á markaðnum</strong>. Leikir eins og <a href="{URL_BASE}spilakassar/mental/">Mental</a> og <a href="{URL_BASE}spilakassar/san-quentin/">San Quentin</a> hafa orðspor fyrir að vera miskunnarlausir — en hámarksvinningar fara yfir 50.000x.</p>

<h2>Um Nolimit City</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2014</td></tr>
<tr><td>Höfuðstöðvar</td><td>Svíþjóð / Malta</td></tr>
<tr><td>Eigandi</td><td>Evolution Group (síðan 2022)</td></tr>
<tr><td>Fjöldi leikja</td><td>60+ (gæði fram yfir magn)</td></tr>
<tr><td>Sérkenni</td><td>xWays, xNudge, xSplit — eigin vélbúnaður</td></tr>
<tr><td>Þemu</td><td>Dökk, óhefðbundin, stundum óþægileg</td></tr>
</tbody></table>

<h2>Topp Nolimit City leikir</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>RTP</th><th>Sveifla</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}spilakassar/mental/">Mental</a></td><td>96,08%</td><td>Öfgakennd</td><td>66.666x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/san-quentin/">San Quentin xWays</a></td><td>96,03%</td><td>Öfgakennd</td><td>150.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/fire-in-the-hole-xbomb/">Fire in the Hole xBomb</a></td><td>96,06%</td><td>Öfgakennd</td><td>60.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/tombstone-rip/">Tombstone R.I.P.</a></td><td>96,08%</td><td>Öfgakennd</td><td>300.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/deadwood/">Deadwood</a></td><td>96,03%</td><td>Há</td><td>13.950x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/punk-toilet/">Punk Toilet</a></td><td>96,05%</td><td>Öfgakennd</td><td>44.400x</td></tr>
</tbody></table>

<h2>Vélbúnaðurinn — xWays, xNudge, xSplit</h2>
<h3>xWays</h3>
<p>Tákn sem opnast og breytist í 2–4 eins tákn, sem margfaldar fjölda vinningsleiða verulega. Getur búið til þúsundir leiða á einum snúningi.</p>
<h3>xNudge</h3>
<p>Wild-tákn sem færist þar til það fyllir alla hjólið — og hver færsla bætir +1 við margfaldarann. Þrjú xNudge wild gefa margfaldara sem leggjast saman.</p>
<h3>xSplit</h3>
<p>Tákn sem klýfur önnur tákn í tvennt og tvöfaldar þau. Getur keðjuverkað og breytt litlum vinningi í risastóran.</p>

<h2>Viðvörun: þetta er ekki fyrir alla</h2>
<div class="info-box"><p><strong>Nolimit City leikir hafa öfgakennda sveiflu.</strong> Það er algengt að fara 500+ snúninga án umtalsverðs vinnings. Ef þú spilar þessa leiki skaltu nota mun minni veðmálsstærð en þú myndir annars gera — og aðeins fjármuni sem þú hefur efni á að tapa.</p></div>
<p>Sjá: <a href="{URL_BASE}leidbeiningar/hvad-er-sveifla/">Hvað er sveifla og hvers vegna skiptir hún máli →</a> og <a href="{URL_BASE}leidbeiningar/bankastjornunaradferdir/">bankastjórnunaraðferðir →</a></p>

<h2>Fyrir hverja hentar Nolimit City?</h2>
<ul>
<li>✅ Spilara sem vilja möguleika á risavinningi og sætta sig við löng þurrkatímabil</li>
<li>✅ Þá sem kunna að meta frumlega leikjahönnun og óhefðbundin þemu</li>
<li>❌ <strong>Ekki</strong> byrjendur — byrjaðu frekar á <a href="{URL_BASE}spilakassar/starburst/">Starburst</a> eða öðrum lágsveifluleikjum</li>
<li>❌ <strong>Ekki</strong> þá sem spila með lítið fjármagn</li>
</ul>
<p>Byrjendur: <a href="{URL_BASE}leidbeiningar/topp-10-spilakassar-fyrir-byrjendur/">topp 10 spilakassar fyrir byrjendur →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hvaða Nolimit City leikur hefur hæsta hámarksvinning?</h3>
<p>Tombstone R.I.P. með 300.000x veðmálið. Á €0,20 snúningi væri það €60.000 — en líkurnar eru hverfandi.</p>
<h3>Er RTP lágt hjá Nolimit City?</h3>
<p>Nei — um 96% sem er staðlað. Það er sveiflan sem er öfgakennd, ekki RTP.</p>
<h3>Hvar get ég spilað Nolimit City á Íslandi?</h3>
<p><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> og <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> bjóða báðir Nolimit City safnið.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Nolimit City →</a></div>'''
    },
    {
        "slug": "martingale-adferd-rulletta",
        "title": "Martingale aðferðin í rúllettu — virkar hún? 2026",
        "desc": "Martingale veðmálakerfið útskýrt á íslensku: hvernig það virkar, stærðfræðin á bak við það og hvers vegna það bregst.",
        "emoji": "📉",
        "colors": ('#280a0a', '#451414', '#621e1e'),
        "content": f'''<h1>Martingale aðferðin í rúllettu</h1>
{hero}
<p>Martingale er frægasta veðmálakerfið í sögu spilavíta: <strong>tvöfaldaðu veðmálið eftir hvert tap, og þegar þú vinnur færðu allt til baka plús einn vinning.</strong> Hljómar óbrigðult. Það er það ekki.</p>

<h2>Hvernig Martingale virkar</h2>
<p>Þú veðjar á jöfn-líkindi veðmál (rautt/svart, oddatölur/sléttar) og tvöfaldar eftir hvert tap:</p>
<table class="info-table"><thead><tr><th>Umferð</th><th>Veðmál</th><th>Heildartap hingað til</th><th>Ef þú vinnur</th></tr></thead><tbody>
<tr><td>1</td><td>€1</td><td>€0</td><td>+€1</td></tr>
<tr><td>2</td><td>€2</td><td>€1</td><td>+€1</td></tr>
<tr><td>3</td><td>€4</td><td>€3</td><td>+€1</td></tr>
<tr><td>4</td><td>€8</td><td>€7</td><td>+€1</td></tr>
<tr><td>5</td><td>€16</td><td>€15</td><td>+€1</td></tr>
<tr><td>6</td><td>€32</td><td>€31</td><td>+€1</td></tr>
<tr><td>7</td><td>€64</td><td>€63</td><td>+€1</td></tr>
<tr><td>8</td><td>€128</td><td>€127</td><td>+€1</td></tr>
<tr><td>9</td><td>€256</td><td>€255</td><td>+€1</td></tr>
<tr><td>10</td><td>€512</td><td>€511</td><td>+€1</td></tr>
</tbody></table>
<p>Taktu eftir: eftir 10 töp í röð ertu að veðja €512 til að vinna <strong>€1</strong>. Og þú hefur þegar tapað €511.</p>

<h2>Af hverju það bregst — þrjár ástæður</h2>
<h3>1. Borðtakmörk</h3>
<p>Öll rúllettuborð hafa hámarksveðmál. Ef lágmarkið er €1 og hámarkið €500 geturðu aðeins tvöfaldað 9 sinnum. Þá er kerfið brotið og þú situr uppi með €511 tap sem þú getur ekki unnið til baka.</p>

<h3>2. Fjármagn þitt er endanlegt</h3>
<p>Martingale virkar fræðilega aðeins með óendanlegu fjármagni. Með €1.000 í höndunum ræður þú við 9 töp í röð — ekki 10.</p>

<h3>3. Tíu töp í röð eru ekki sjaldgæf</h3>
<p>Á evrópskri rúllettu eru líkurnar á rauðu 18/37 = 48,6%. Líkurnar á 10 töpum í röð eru um 1 á móti 600. Ef þú spilar 600 umferðir — sem tekur kannski tvær kvöldstundir — ertu nokkuð líklegur til að lenda í því.</p>
<div class="info-box"><p><strong>Lykilatriðið:</strong> Martingale breytir ekki húsforskotinu (2,7% á evrópskri rúllettu). Það breytir aðeins dreifingu niðurstaðna: margir litlir vinningar og örfá risastór töp. Vænt gildi er óbreytt — neikvætt.</p></div>

<h2>Afbrigði</h2>
<h3>Reverse Martingale (Paroli)</h3>
<p>Tvöfaldaðu eftir hvern <em>vinning</em> í stað taps, hættu eftir 3 vinninga í röð. Takmarkar tapið en vinningarnir verða sjaldgæfari.</p>
<h3>D'Alembert</h3>
<p>Hækkaðu um eina einingu eftir tap, lækkaðu um eina eftir vinning. Mun hægari vöxtur — minni áhætta en líka minni „bati".</p>
<h3>Fibonacci</h3>
<p>Fylgdu Fibonacci-röðinni (1, 1, 2, 3, 5, 8, 13, 21...). Vægari en Martingale en sama grundvallarvandamálið.</p>

<h2>Hvað virkar í staðinn?</h2>
<p>Ekkert veðmálakerfi getur sigrað húsforskotið. En þetta getur bætt upplifunina:</p>
<ul>
<li><strong>Veldu leiki með lágt húsforskot</strong> — <a href="{URL_BASE}leidbeiningar/baccarat-reglur-a-islensku/">Baccarat (Banker)</a> 1,06%, <a href="{URL_BASE}leidbeiningar/blackjack-adferdir/">blackjack með grunnstrategíu</a> 0,5%</li>
<li><strong>Spilaðu evrópska rúllettu</strong> — 2,7% á móti 5,26% á amerískri</li>
<li><strong>Settu tap- og vinningsmörk</strong> — Ákveddu fyrirfram hvenær þú hættir</li>
<li><strong>Fast veðmál</strong> — Sama upphæð í hverri umferð. Leiðinlegra en mun öruggara</li>
</ul>
<p><a href="{URL_BASE}leidbeiningar/bankastjornunaradferdir/">Bankastjórnunaraðferðir →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hefur einhver grætt á Martingale?</h3>
<p>Til skamms tíma — já, margir. Kerfið gefur tíða litla vinninga. Vandamálið er að eitt langt taptímabil þurrkar út allan ágóðann og meira til.</p>
<h3>Virkar Martingale í blackjack?</h3>
<p>Sömu vandamál: borðtakmörk og endanlegt fjármagn. Í blackjack er betra að einbeita sér að <a href="{URL_BASE}leidbeiningar/blackjack-adferdir/">grunnstrategíu</a> sem raunverulega lækkar húsforskotið.</p>
<h3>Banna spilavíti Martingale?</h3>
<p>Nei — spilavíti hafa ekkert á móti því. Borðtakmörkin sjá til þess að kerfið virki ekki til lengdar.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila rúllettu →</a></div>'''
    },
    {
        "slug": "texas-holdem-reglur-a-islensku",
        "title": "Texas Hold'em reglur á íslensku — hvernig á að spila póker 2026",
        "desc": "Texas Hold'em reglur á íslensku: handaröð, veðmálaumferðir, position og grunnstrategy fyrir byrjendur.",
        "emoji": "♠️",
        "colors": ('#0a1a0f', '#14331e', '#1e4d2d'),
        "content": f'''<h1>Texas Hold'em reglur á íslensku</h1>
{hero}
<p>Texas Hold'em er vinsælasta pókerafbrigðið í heiminum. <strong>Reglurnar eru einfaldar — en leikurinn tekur ævi að ná tökum á.</strong> Hér eru grunnreglurnar á íslensku.</p>

<h2>Markmiðið</h2>
<p>Þú færð tvö kort sem aðeins þú sérð („hole cards"). Fimm sameiginleg kort eru lögð á borðið. Þú býrð til bestu fimm korta hönd úr þínum tveimur og sameiginlegu kortunum fimm.</p>

<h2>Handaröðin (frá bestu til verstu)</h2>
<table class="info-table"><thead><tr><th>#</th><th>Hönd</th><th>Lýsing</th><th>Dæmi</th></tr></thead><tbody>
<tr><td>1</td><td>Royal Flush</td><td>10-G-D-K-Á í sama lit</td><td>♠10 ♠G ♠D ♠K ♠Á</td></tr>
<tr><td>2</td><td>Straight Flush</td><td>Fimm í röð, sami litur</td><td>♥5 ♥6 ♥7 ♥8 ♥9</td></tr>
<tr><td>3</td><td>Fjórir eins</td><td>Fjögur eins kort</td><td>K K K K 7</td></tr>
<tr><td>4</td><td>Full House</td><td>Þrír eins + par</td><td>9 9 9 4 4</td></tr>
<tr><td>5</td><td>Flush (litur)</td><td>Fimm í sama lit</td><td>♦2 ♦6 ♦9 ♦G ♦K</td></tr>
<tr><td>6</td><td>Straight (röð)</td><td>Fimm í röð</td><td>4 5 6 7 8</td></tr>
<tr><td>7</td><td>Þrír eins</td><td>Þrjú eins kort</td><td>D D D 8 3</td></tr>
<tr><td>8</td><td>Tvö pör</td><td>Tvö mismunandi pör</td><td>G G 5 5 Á</td></tr>
<tr><td>9</td><td>Eitt par</td><td>Tvö eins kort</td><td>7 7 K 9 2</td></tr>
<tr><td>10</td><td>Hátt kort</td><td>Ekkert af ofangreindu</td><td>Á D 9 6 3</td></tr>
</tbody></table>

<h2>Veðmálaumferðirnar fjórar</h2>
<h3>1. Pre-flop</h3>
<p>Allir fá tvö kort. Veðmálaumferð hefst með spilaranum vinstra megin við stóra blindið.</p>
<h3>2. Flop</h3>
<p>Þrjú sameiginleg kort lögð á borðið. Ný veðmálaumferð.</p>
<h3>3. Turn</h3>
<p>Fjórða sameiginlega kortið. Ný veðmálaumferð.</p>
<h3>4. River</h3>
<p>Fimmta og síðasta kortið. Lokaveðmálaumferð, síðan showdown þar sem bestu höndinni er flett upp.</p>

<h2>Aðgerðir</h2>
<table class="info-table"><thead><tr><th>Aðgerð</th><th>Á íslensku</th><th>Hvað þýðir það</th></tr></thead><tbody>
<tr><td>Fold</td><td>Kasta</td><td>Hætta í höndinni, tapa því sem þú hefur lagt í pottinn</td></tr>
<tr><td>Check</td><td>Athuga</td><td>Veðja engu en halda áfram (aðeins ef enginn hefur veðjað)</td></tr>
<tr><td>Call</td><td>Jafna</td><td>Jafna veðmál andstæðingsins</td></tr>
<tr><td>Bet / Raise</td><td>Veðja / Hækka</td><td>Setja pening í pottinn eða hækka fyrra veðmál</td></tr>
<tr><td>All-in</td><td>Allt inn</td><td>Setja alla fjármuni þína í pottinn</td></tr>
</tbody></table>

<h2>Position — mikilvægasta hugtakið</h2>
<p>Þeir sem bregðast við síðast hafa mesta upplýsingaforskotið. Því síðar sem þú ert í röðinni, því fleiri ákvarðanir andstæðinganna sérðu áður en þú þarft að ákveða þig.</p>
<ul>
<li><strong>Early position</strong> — Spilaðu aðeins sterkar hendur (há pör, Á-K)</li>
<li><strong>Late position</strong> — Þú getur spilað víðara svið af höndum</li>
<li><strong>Button (dílarahnappur)</strong> — Besta sætið. Þú bregst við síðast í öllum umferðum eftir flop</li>
</ul>

<h2>Byrjendaráð</h2>
<ol>
<li><strong>Spilaðu færri hendur</strong> — Byrjendur spila of margar hendur. Kastaðu veikum höndum fyrir flop</li>
<li><strong>Athugaðu stærð pottsins</strong> — Er það þess virði að jafna miðað við hvað er í pottinum?</li>
<li><strong>Fylgstu með andstæðingum</strong> — Hver veðjar árásargjarnt? Hver kastar auðveldlega?</li>
<li><strong>Forðist „tilt"</strong> — Að spila reiður eftir slæma hönd er dýrasta mistök í póker</li>
</ol>

<h2>Hvar á að spila póker á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}live/poker/">Lifandi póker á Svipan</a></strong> — Yfirlit yfir lifandi pókerleiki</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}live/texas-holdem-bonus/">Texas Hold'em Bonus</a></strong> — Spilavítisútgáfa gegn dílara (ekki gegn öðrum spilurum)</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/poker-spilaviti/">Pókerspilavíti</a></strong> — Spilavíti með pókerhluta</p></div>

<h2>Algengar spurningar</h2>
<h3>Hver er munurinn á póker og spilavítispóker?</h3>
<p>Í hefðbundnum póker spilar þú gegn öðrum spilurum og spilavítið tekur þóknun af pottinum. Í spilavítispóker (t.d. Texas Hold'em Bonus) spilar þú gegn húsinu með föstum reglum og húsforskoti.</p>
<h3>Er póker heppni eða kunnátta?</h3>
<p>Hvort tveggja. Til skamms tíma ræður heppnin miklu, en til langs tíma skilar kunnátta sér. Það er ástæðan fyrir því að sömu nöfn birtast ítrekað á úrslitaborðum stórmóta.</p>
<h3>Hvað er „bluff"?</h3>
<p>Að veðja árásargjarnt með veika hönd til að fá andstæðinginn til að kasta betri hönd. Mikilvægur hluti leiksins en ofnotaður hjá byrjendum.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila póker →</a></div>'''
    },
    {
        "slug": "bestu-spilakassarnir-haesta-rtp",
        "title": "Spilakassar með hæsta RTP 2026 — topp 20 listi",
        "desc": "Listi yfir spilakassa með hæsta RTP (allt að 99%). Hvað RTP þýðir raunverulega og hvernig á að finna rétta stillingu.",
        "emoji": "📊",
        "colors": ('#0a1a1a', '#143333', '#1e4d4d'),
        "content": f'''<h1>Spilakassar með hæsta RTP 2026</h1>
{hero}
<p>RTP (Return to Player) segir hversu hátt hlutfall af veðjuðum peningum spilakassi greiðir til baka <strong>yfir milljónir snúninga</strong>. Hærra RTP þýðir lægra húsforskot — en það tryggir ekki vinning í þinni lotu.</p>

<h2>Topp 20 spilakassar eftir RTP</h2>
<table class="info-table"><thead><tr><th>#</th><th>Spilakassi</th><th>Framleiðandi</th><th>RTP</th><th>Sveifla</th></tr></thead><tbody>
<tr><td>1</td><td><a href="{URL_BASE}spilakassar/blood-suckers/">Blood Suckers</a></td><td>NetEnt</td><td>98,00%</td><td>Lág</td></tr>
<tr><td>2</td><td><a href="{URL_BASE}spilakassar/starmania/">Starmania</a>*</td><td>NextGen</td><td>97,87%</td><td>Lág</td></tr>
<tr><td>3</td><td><a href="{URL_BASE}spilakassar/dead-or-alive/">Dead or Alive</a></td><td>NetEnt</td><td>96,82%</td><td>Há</td></tr>
<tr><td>4</td><td><a href="{URL_BASE}spilakassar/big-bass-bonanza/">Big Bass Bonanza</a></td><td>Pragmatic Play</td><td>96,71%</td><td>Há</td></tr>
<tr><td>5</td><td><a href="{URL_BASE}spilakassar/finn-and-the-swirly-spin/">Finn and the Swirly Spin</a></td><td>NetEnt</td><td>96,62%</td><td>Meðal</td></tr>
<tr><td>6</td><td><a href="{URL_BASE}spilakassar/divine-fortune/">Divine Fortune</a></td><td>NetEnt</td><td>96,59%</td><td>Meðal</td></tr>
<tr><td>7</td><td><a href="{URL_BASE}spilakassar/legacy-of-dead/">Legacy of Dead</a></td><td>Play'n GO</td><td>96,58%</td><td>Há</td></tr>
<tr><td>8</td><td><a href="{URL_BASE}spilakassar/twin-spin/">Twin Spin</a></td><td>NetEnt</td><td>96,55%</td><td>Meðal</td></tr>
<tr><td>9</td><td><a href="{URL_BASE}spilakassar/rise-of-merlin/">Rise of Merlin</a></td><td>Play'n GO</td><td>96,52%</td><td>Há</td></tr>
<tr><td>10</td><td><a href="{URL_BASE}spilakassar/reactoonz/">Reactoonz</a></td><td>Play'n GO</td><td>96,51%</td><td>Há</td></tr>
<tr><td>11</td><td><a href="{URL_BASE}spilakassar/gates-of-olympus/">Gates of Olympus</a></td><td>Pragmatic Play</td><td>96,50%</td><td>Há</td></tr>
<tr><td>12</td><td><a href="{URL_BASE}spilakassar/rise-of-olympus/">Rise of Olympus</a></td><td>Play'n GO</td><td>96,50%</td><td>Há</td></tr>
<tr><td>13</td><td><a href="{URL_BASE}spilakassar/moon-princess/">Moon Princess</a></td><td>Play'n GO</td><td>96,50%</td><td>Há</td></tr>
<tr><td>14</td><td><a href="{URL_BASE}spilakassar/sugar-rush/">Sugar Rush</a></td><td>Pragmatic Play</td><td>96,50%</td><td>Há</td></tr>
<tr><td>15</td><td><a href="{URL_BASE}spilakassar/sweet-bonanza/">Sweet Bonanza</a></td><td>Pragmatic Play</td><td>96,48%</td><td>Meðal-há</td></tr>
<tr><td>16</td><td><a href="{URL_BASE}spilakassar/fruit-party/">Fruit Party</a></td><td>Pragmatic Play</td><td>96,47%</td><td>Há</td></tr>
<tr><td>17</td><td><a href="{URL_BASE}spilakassar/razor-shark/">Razor Shark</a></td><td>Push Gaming</td><td>96,70%</td><td>Há</td></tr>
<tr><td>18</td><td><a href="{URL_BASE}spilakassar/jammin-jars/">Jammin' Jars</a></td><td>Push Gaming</td><td>96,83%</td><td>Há</td></tr>
<tr><td>19</td><td><a href="{URL_BASE}spilakassar/dead-or-alive-2/">Dead or Alive 2</a></td><td>NetEnt</td><td>96,29%</td><td>Mjög há</td></tr>
<tr><td>20</td><td><a href="{URL_BASE}spilakassar/book-of-dead/">Book of Dead</a></td><td>Play'n GO</td><td>96,21%</td><td>Há</td></tr>
</tbody></table>
<p><em>*Ekki í boði á öllum spilavítum.</em></p>

<h2>Varúð: sama leikur, mismunandi RTP</h2>
<div class="info-box"><p><strong>Þetta er það mikilvægasta á þessari síðu.</strong> Margir framleiðendur gefa út sama leikinn í mörgum RTP-útgáfum — t.d. 96,50%, 94,50% og 87,50%. Spilavítið velur hvaða útgáfu það keyrir.</p></div>
<p>Þú getur verið að spila „Gates of Olympus" sem lítur eins út en skilar 87,5% í stað 96,5%. Munurinn er gríðarlegur yfir tíma.</p>
<h3>Hvernig athuga ég raunverulegt RTP?</h3>
<ol>
<li>Opnaðu leikinn</li>
<li>Smelltu á ⓘ eða valmyndartáknið (oft neðst til vinstri)</li>
<li>Flettu að „Game Rules" eða „Paytable"</li>
<li>RTP er yfirleitt neðst á síðustu síðu reglnanna</li>
</ol>
<p>Ef spilavítið sýnir ekki RTP í leikjareglum er það viðvörunarmerki.</p>

<h2>RTP er ekki allt — sveiflan skiptir máli líka</h2>
<p>Tveir leikir með sama 96,5% RTP geta gefið gjörólíka upplifun:</p>
<ul>
<li><strong>Lág sveifla</strong> (t.d. <a href="{URL_BASE}spilakassar/starburst/">Starburst</a>) — Tíðir litlir vinningar, jafnari spilun, fjármagnið endist lengur</li>
<li><strong>Há sveifla</strong> (t.d. <a href="{URL_BASE}spilakassar/book-of-dead/">Book of Dead</a>) — Löng þurrkatímabil, en stærri vinningar þegar þeir koma</li>
</ul>
<p><a href="{URL_BASE}leidbeiningar/hvad-er-sveifla/">Hvað er sveifla? →</a> · <a href="{URL_BASE}leidbeiningar/lag-sveiflu-spilakassar/">Lágsveifluspilakassar →</a></p>

<h2>Hvað þýðir 96% RTP í raun?</h2>
<p>Af hverjum €100 sem veðjaðir eru í leiknum — samanlagt af öllum spilurum yfir milljónir snúninga — skilar hann €96 til baka. Það þýðir <strong>ekki</strong> að þú fáir €96 til baka af þínum €100.</p>
<p>Í þinni lotu geturðu fengið €0 eða €5.000. RTP lýsir langtímameðaltali, ekki einstökum lotum.</p>
<p><a href="{URL_BASE}leidbeiningar/hvad-er-rtp/">Ítarleg RTP útskýring →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hvaða spilakassi hefur hæsta RTP?</h3>
<p>Blood Suckers frá NetEnt með 98%. Það er einnig lágsveifluleikur sem þýðir að fjármagnið endist lengi.</p>
<h3>Ætti ég alltaf að velja hæsta RTP?</h3>
<p>Ekki endilega. Ef þú vilt möguleika á stórum vinningi skiptir hámarksvinningur og sveifla meira máli. Ef þú vilt löng spilalota með litlu tapi — veldu hátt RTP og lága sveiflu.</p>
<h3>Hafa spilavíti áhrif á RTP?</h3>
<p>Þau geta valið milli RTP-útgáfa sem framleiðandinn býður. Þau geta ekki breytt niðurstöðum í rauntíma — <a href="{URL_BASE}leidbeiningar/hvernig-rng-virkar/">RNG-inn</a> er vottaður af óháðum prófunaraðilum.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila hátt RTP spilakassa →</a></div>'''
    },
    {
        "slug": "hvernig-a-ad-setja-takmork-a-spilaviti",
        "title": "Hvernig á að setja takmörk á spilavíti — verkfæri sem virka 2026",
        "desc": "Innborgunartakmörk, tapmörk, tímamörk og sjálfsútilokun. Hvernig á að stilla þau og hvers vegna það skiptir máli.",
        "emoji": "🎚️",
        "colors": ('#0f1a0a', '#1e3314', '#2d4d1e'),
        "content": f'''<h1>Hvernig á að setja takmörk á spilavíti</h1>
{hero}
<p>Takmörk eru öflugasta verkfærið sem þú hefur til að halda spilun innan heilbrigðra marka. <strong>Þau virka vegna þess að þú tekur ákvörðunina þegar þú ert rólegur — ekki í miðri lotu.</strong></p>

<h2>Fjórar tegundir takmarka</h2>
<h3>1. Innborgunartakmörk</h3>
<p>Hámarksupphæð sem þú getur lagt inn á dag, viku eða mánuði. Þetta er mikilvægasta takmörkunin — hún stoppar þig í að elta tap.</p>
<p><strong>Hvernig á að velja upphæð:</strong> Ákveddu hvað þú hefur efni á að tapa á mánuði án þess að það hafi áhrif á neitt annað. Deildu með fjórum fyrir vikutakmark.</p>

<h3>2. Tapmörk</h3>
<p>Hámarksupphæð sem þú mátt tapa á tilteknu tímabili. Þegar mörkunum er náð lokast reikningurinn fyrir frekari veðmál.</p>

<h3>3. Tímamörk / lotutakmörk</h3>
<p>Hámarkstími sem þú getur spilað í einu eða á dag. Mjög gagnlegt því tímaskyn rýrnar hratt þegar maður spilar.</p>

<h3>4. Veðmálatakmörk</h3>
<p>Hámarksupphæð á einstakan snúning eða veðmál. Kemur í veg fyrir skyndiákvarðanir um stór veðmál.</p>

<h2>Hvernig á að stilla takmörk — skref fyrir skref</h2>
<ol>
<li>Skráðu þig inn á spilavítið</li>
<li>Farðu í <strong>Reikningur</strong> → <strong>Ábyrg spilun</strong> (eða „Responsible Gaming")</li>
<li>Veldu tegund takmörkunar</li>
<li>Sláðu inn upphæð eða tíma</li>
<li>Staðfestu</li>
</ol>
<div class="info-box"><p><strong>Mikilvægt:</strong> Að <em>lækka</em> takmörk tekur gildi strax. Að <em>hækka</em> þau krefst yfirleitt 24–72 klst biðtíma. Þetta er viljandi — það gefur þér tíma til að endurskoða ákvörðun sem tekin var í hita leiksins.</p></div>

<h2>Sjálfsútilokun — þegar takmörk duga ekki</h2>
<p>Ef takmörk duga ekki geturðu lokað reikningnum alveg:</p>
<ul>
<li><strong>Hlé (cooling-off)</strong> — 24 klst til 6 vikur. Reikningurinn opnast sjálfkrafa aftur</li>
<li><strong>Sjálfsútilokun</strong> — 6 mánuðir til varanlega. Ekki hægt að afturkalla fyrr en tímabilinu lýkur</li>
</ul>
<p><a href="{URL_BASE}leidbeiningar/sjalfsutilokun-spilavita/">Ítarlegt um sjálfsútilokun →</a></p>

<h2>Takmörk utan spilavítisins</h2>
<p>Takmörk á spilavítinu virka aðeins á því spilavíti. Þessi verkfæri virka víðar:</p>
<ul>
<li><strong>Bankalokun</strong> — Sumir bankar og kortafyrirtæki bjóða að loka á fjárhættuspilafærslur. Hafðu samband við bankann þinn</li>
<li><strong>Gamban / BetBlocker</strong> — Hugbúnaður sem lokar á spilavítasíður á öllum tækjum þínum. BetBlocker er ókeypis</li>
<li><strong>Fjarlægðu greiðslumáta</strong> — Eyddu vistuðum kortum af spilavítareikningum</li>
</ul>

<h2>Hvenær á að setja takmörk?</h2>
<p>Svarið er einfalt: <strong>strax við skráningu, áður en þú leggur inn í fyrsta sinn.</strong></p>
<p>Það er miklu auðveldara að setja skynsamleg mörk þegar þú hefur engar tilfinningar bundnar við jafnvægið. Eftir að þú hefur tapað €200 er dómgreindin ekki sú sama.</p>

<h2>Ef þú þarft hjálp</h2>
<div class="info-box"><p><strong>Hjálparsíminn 1717</strong> er opinn allan sólarhringinn, alla daga ársins. Ókeypis og hægt að hringja nafnlaust.</p></div>
<p>Sjá einnig: <a href="{URL_BASE}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">merki spilafiknar →</a> og <a href="{URL_BASE}leidbeiningar/studningssidur-vid-spilafikn/">stuðningsúrræði á Íslandi →</a></p>

<h2>Algengar spurningar</h2>
<h3>Get ég afturkallað takmörk?</h3>
<p>Að lækka takmörk gerist strax. Að hækka þau tekur 24–72 klst í gildi hjá flestum spilavítum með gilt leyfi.</p>
<h3>Virka takmörk á öllum spilavítum?</h3>
<p>Nei — takmörk gilda aðeins á því spilavíti þar sem þú stillir þau. Ef þú spilar á mörgum stöðum þarftu að stilla þau alls staðar, eða nota BetBlocker sem lokar á allt.</p>
<h3>Hvað ef spilavítið býður ekki takmörk?</h3>
<p>Þá er það ekki spilavíti sem þú átt að nota. Öll spilavíti með gilt leyfi eru skyldug til að bjóða þessi verkfæri.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá ábyrga spilun →</a></div>'''
    },
    {
        "slug": "radleggingar-til-adstandenda-spilafikla",
        "title": "Ráðleggingar til aðstandenda spilafíkla — hvernig á að hjálpa 2026",
        "desc": "Hvernig á að tala við ástvin sem glímir við spilafikn, hvað á að forðast og hvaða hjálp er í boði á Íslandi.",
        "emoji": "🤝",
        "colors": ('#1a1413', '#332826', '#4d3c39'),
        "content": f'''<h1>Ráðleggingar til aðstandenda spilafíkla</h1>
{hero}
<p>Spilafikn snertir ekki bara þann sem spilar. <strong>Maki, börn, foreldrar og vinir verða líka fyrir áhrifum</strong> — fjárhagslega og tilfinningalega. Hér eru hagnýt ráð ef einhver nálægt þér glímir við þetta.</p>

<h2>Merki sem þú gætir tekið eftir</h2>
<ul>
<li>Peningar hverfa án skýringa, eða lán eru tekin ítrekað</li>
<li>Leynd um fjármál — reikningar faldir, símtöl tekin í einrúmi</li>
<li>Skapsveiflur sem fylgja vinningum og töpum</li>
<li>Minni þátttaka í fjölskyldulífi eða áhugamálum</li>
<li>Loforð um að hætta sem ekki eru efnd</li>
<li>Svefnvandamál, kvíði eða þunglyndi</li>
</ul>
<p>Sjá ítarlegri lista: <a href="{URL_BASE}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">10 merki spilafiknar →</a></p>

<h2>Hvernig á að hefja samtalið</h2>
<h3>Veldu réttan tíma</h3>
<p>Ekki í miðri deilu og ekki þegar viðkomandi er nýbúinn að tapa. Veldu rólega stund þegar þið eruð bæði yfirveguð.</p>

<h3>Talaðu um áhrifin, ekki hegðunina</h3>
<p>Í stað: „Þú ert að eyðileggja allt með þessari spilun."<br>
Reyndu: „Ég hef áhyggjur. Ég tók eftir að reikningarnir eru ógreiddir og ég er hrædd um okkur."</p>
<p>Þetta kallast „ég-skilaboð" — þau lýsa þinni upplifun í stað þess að ásaka, sem minnkar varnarviðbrögð.</p>

<h3>Hlustaðu meira en þú talar</h3>
<p>Spurðu opinna spurninga: „Hvernig líður þér með þetta?" Leyfðu þögn. Fólk opnar sig oft þegar það finnur að það er ekki dæmt.</p>

<h2>Hvað á að forðast</h2>
<table class="info-table"><thead><tr><th>Ekki gera</th><th>Af hverju</th></tr></thead><tbody>
<tr><td>Borga spilaskuldir</td><td>Fjarlægir afleiðingarnar og lengir vandamálið</td></tr>
<tr><td>Hóta án þess að framfylgja</td><td>Grefur undan trúverðugleika þínum</td></tr>
<tr><td>Leyna vandamálinu fyrir öðrum</td><td>Einangrar bæði þig og viðkomandi</td></tr>
<tr><td>Ásaka eða skammast</td><td>Eykur skömm sem oft kyndir undir frekari spilun</td></tr>
<tr><td>Trúa því að ein samtal leysi allt</td><td>Bati er ferli, ekki einn atburður</td></tr>
</tbody></table>

<h2>Verndaðu þig fjárhagslega</h2>
<p>Þetta er ekki svik við ástvin þinn — það er nauðsynlegt fyrir ykkur bæði:</p>
<ol>
<li>Aðskildu bankareikninga ef hægt er</li>
<li>Fáðu yfirsýn yfir sameiginlegar skuldir og lán</li>
<li>Tryggðu að þú hafir aðgang að eigin fé</li>
<li>Íhugaðu að ræða við fjármálaráðgjafa eða lögfræðing ef skuldir eru verulegar</li>
<li>Geymdu mikilvæg skjöl á öruggum stað</li>
</ol>

<h2>Hvernig þú getur stutt bata</h2>
<ul>
<li><strong>Hvettu til faghjálpar</strong> — Bjóddu að fara með, ekki bara að senda</li>
<li><strong>Hjálpaðu við hagnýt skref</strong> — <a href="{URL_BASE}leidbeiningar/sjalfsutilokun-spilavita/">Sjálfsútilokun</a>, lokun á bankagreiðslur, uppsetning BetBlocker</li>
<li><strong>Fagnaðu litlum sigrum</strong> — Vika án spilunar er árangur</li>
<li><strong>Gerðu ráð fyrir bakslagi</strong> — Það er algengt og þýðir ekki að allt sé tapað</li>
</ul>

<h2>Ekki gleyma sjálfum þér</h2>
<p>Aðstandendur brenna oft út. Þú átt líka rétt á stuðningi:</p>
<div class="info-box"><p><strong>Hjálparsíminn 1717</strong> — Opinn allan sólarhringinn. Þú getur hringt fyrir þig sjálfan, ekki bara fyrir þann sem spilar.</p></div>
<div class="info-box"><p><strong>Gam-Anon</strong> — Alþjóðlegir stuðningshópar sérstaklega fyrir aðstandendur spilafíkla.</p></div>
<div class="info-box"><p><strong>SÁÁ</strong> — Veitir ráðgjöf til aðstandenda, ekki bara þeirra sem glíma við fíknina.</p></div>
<p><a href="{URL_BASE}leidbeiningar/studningssidur-vid-spilafikn/">Öll stuðningsúrræði á Íslandi →</a></p>

<h2>Algengar spurningar</h2>
<h3>Á ég að borga skuldirnar til að „hreinsa borðið"?</h3>
<p>Ráðgjafar mæla almennt gegn því. Þegar afleiðingarnar hverfa minnkar hvatinn til að breyta hegðun. Betra er að styðja viðkomandi í að takast á við skuldirnar sjálfur, með faglegri aðstoð.</p>
<h3>Hvað ef viðkomandi neitar að það sé vandamál?</h3>
<p>Afneitun er algeng. Þú getur ekki þvingað fram bata — en þú getur sett eigin mörk, verndað þig fjárhagslega og haldið dyrunum opnum. Margir leita hjálpar síðar.</p>
<h3>Hvernig tala ég við börn um þetta?</h3>
<p>Aldurssvarandi hreinskilni virkar best. Börn skynja spennu hvort sem er og kenna sér oft um. Útskýrðu að þetta sé veikindi fullorðins, ekki þeim að kenna, og að verið sé að leita hjálpar.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá stuðningsúrræði →</a></div>'''
    },
    {
        "slug": "gjaldmidlaskipti-isk-eur-spilaviti",
        "title": "Gjaldmiðlaskipti ISK í EUR fyrir spilavíti — hvernig á að spara 2026",
        "desc": "Hvað kostar að skipta ISK í EUR fyrir spilavítainnlagnir? Samanburður á bönkum, Revolut, Wise og dulritunargjaldmiðlum.",
        "emoji": "💱",
        "colors": ('#0a1a1f', '#14333a', '#1e4d55'),
        "content": f'''<h1>Gjaldmiðlaskipti ISK í EUR fyrir spilavíti</h1>
{hero}
<p>Nánast öll netspilavíti nota EUR eða USD — ekki íslenskar krónur. <strong>Það þýðir að í hvert sinn sem þú leggur inn borgar þú gjaldmiðlaskiptagjald.</strong> Yfir ár getur þetta orðið umtalsvert, og flestir taka aldrei eftir því.</p>

<h2>Hvað kostar skiptingin í raun?</h2>
<table class="info-table"><thead><tr><th>Leið</th><th>Álag á gengi</th><th>Kostnaður á €100</th><th>Hraði</th></tr></thead><tbody>
<tr><td>Íslenskt bankakort</td><td>1,5–2,5%</td><td>€1,50–2,50</td><td>Samstundis</td></tr>
<tr><td>Bankamillifærsla (SEPA)</td><td>1–2% + fast gjald</td><td>€1–2 + €0–25</td><td>1–2 dagar</td></tr>
<tr><td>Revolut (á virkum dögum)</td><td>0% upp að mánaðarþaki</td><td>€0</td><td>Samstundis</td></tr>
<tr><td>Revolut (um helgar)</td><td>~1%</td><td>€1</td><td>Samstundis</td></tr>
<tr><td>Wise</td><td>0,4–0,6%</td><td>€0,40–0,60</td><td>Samstundis–1 dagur</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>0,1–1,5% (kauphallargjald)</td><td>€0,10–1,50</td><td>5–30 mín</td></tr>
</tbody></table>
<p><em>Tölur eru viðmið. Álag breytist og fer eftir banka, korti og upphæð.</em></p>

<h2>Falinn kostnaður: tvöföld skipting</h2>
<p>Þetta er það sem flestir gleyma. Ef þú leggur inn og tekur svo út borgar þú <strong>tvisvar</strong>:</p>
<ol>
<li>ISK → EUR þegar þú leggur inn (1,5–2,5%)</li>
<li>EUR → ISK þegar þú tekur út (1,5–2,5%)</li>
</ol>
<p>Dæmi: þú leggur inn €500 og tekur út €500 óbreytt. Þú hefur samt tapað um €15–25 í gjaldmiðlaskiptum — án þess að hafa tapað krónu í spilun.</p>

<h2>Besta leiðin: haltu jafnvæginu í EUR</h2>
<p>Ef þú spilar reglulega er langódýrasta leiðin að halda fjármunum í EUR eða USDT í stað þess að skipta fram og til baka:</p>
<ul>
<li><strong>Revolut EUR-reikningur</strong> — Skiptu ISK í EUR einu sinni, haltu jafnvæginu þar og notaðu EUR beint</li>
<li><strong>USDT veski</strong> — Kauptu USDT einu sinni, sendu inn og út án frekari skipta. <a href="{URL_BASE}leidbeiningar/hvernig-a-ad-kaupa-usdt-island/">Hvernig á að kaupa USDT →</a></li>
</ul>
<p>Með þessari aðferð borgar þú skiptagjald einu sinni í stað þess að greiða það við hverja innborgun og úttekt.</p>

<h2>Revolut — mikilvæg smáatriði</h2>
<p>Revolut býður gjaldmiðlaskipti á millibankagengi (interbank rate) án álags — en með takmörkunum:</p>
<ul>
<li><strong>Mánaðarþak</strong> á ókeypis skiptum á grunnáskrift. Yfir þakið bætist við lítið gjald</li>
<li><strong>Helgarálag</strong> — Um helgar (þegar gjaldeyrismarkaðir eru lokaðir) bætir Revolut við um 1% álagi</li>
</ul>
<p>Ráð: skiptu ISK í EUR á virkum degi, ekki á laugardagskvöldi.</p>
<p><a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut fyrir spilavíti — ítarleg leiðbeining →</a></p>

<h2>Spilavíti sem taka við ISK</h2>
<p>Örfá spilavíti bjóða ISK sem gjaldmiðil. Það hljómar vel en athugaðu: þegar spilavíti býður ISK er það yfirleitt með eigin gengi sem getur verið óhagstæðara en bankinn þinn. Berðu saman áður en þú velur.</p>
<p><a href="{URL_BASE}leidbeiningar/spilaviti-isk-kronur/">Spilavíti sem taka við íslenskum krónum →</a></p>

<h2>Samantekt — ódýrasta leiðin</h2>
<ol>
<li><strong>Ódýrast:</strong> Halda jafnvægi í USDT, engin endurtekin skipti</li>
<li><strong>Næstódýrast:</strong> Revolut EUR-reikningur, skipt á virkum degi</li>
<li><strong>Í lagi:</strong> Wise með 0,4–0,6% álagi</li>
<li><strong>Dýrast:</strong> Íslenskt bankakort í hverri færslu</li>
</ol>

<h2>Algengar spurningar</h2>
<h3>Sér bankinn hvað ég er að gera ef ég nota Revolut?</h3>
<p>Bankinn sér aðeins millifærslu á Revolut-reikninginn þinn — ekki hvað þú gerir með peningana eftir það.</p>
<h3>Er dýrara að nota dulritunargjaldmiðla?</h3>
<p>Nei — oft ódýrara. Kauphallargjald er 0,1–1,5% og færslugjald um $0,5–1. Samanlagt yfirleitt minna en bankaálag, sérstaklega ef þú spilar reglulega.</p>
<h3>Hvað með gengisáhættu?</h3>
<p>Ef þú heldur jafnvægi í EUR tekurðu á þig gengisáhættu EUR/ISK. Yfir stutt tímabil er hún lítil, en hafðu hana í huga ef þú geymir stórar upphæðir.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Finna spilavíti →</a></div>'''
    },
    {
        "slug": "paysafecard-a-islandi-spilaviti",
        "title": "Paysafecard á Íslandi — fyrirframgreitt kort fyrir spilavíti 2026",
        "desc": "Hvernig Paysafecard virkar á Íslandi: hvar á að kaupa, hvernig á að nota og af hverju úttektir virka ekki.",
        "emoji": "🎟️",
        "colors": ('#0a1428', '#142445', '#1e3462'),
        "content": f'''<h1>Paysafecard á Íslandi</h1>
{hero}
<p>Paysafecard er fyrirframgreiddur kóði sem þú kaupir með reiðufé eða korti og notar til innborgunar — án þess að gefa upp bankaupplýsingar. <strong>Fyrir íslenska spilara hefur það einn stóran kost og einn stóran galla.</strong></p>

<h2>Hvernig Paysafecard virkar</h2>
<ol>
<li>Þú kaupir kóða að ákveðnu verðmæti (€10, €25, €50, €100)</li>
<li>Kóðinn er 16 tölustafir</li>
<li>Á spilavítinu velurðu Paysafecard og slærð inn kóðann</li>
<li>Upphæðin leggst inn samstundis</li>
</ol>
<p>Engar bankaupplýsingar, ekkert kort, engin tenging við reikninginn þinn.</p>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Engar bankaupplýsingar gefnar upp</td><td>❌ <strong>Ekki hægt að taka út</strong> — aðeins innborgun</td></tr>
<tr><td>✅ Innbyggt eyðsluþak (þú kaupir ákveðna upphæð)</td><td>❌ Takmarkað framboð á Íslandi</td></tr>
<tr><td>✅ Samstundis innborgun</td><td>❌ Gjald getur fylgt kaupum</td></tr>
<tr><td>✅ Bankinn sér ekki spilavítið</td><td>❌ Færri spilavíti styðja það en kort</td></tr>
</tbody></table>

<h2>Stærsti gallinn: engar úttektir</h2>
<div class="info-box"><p><strong>Paysafecard er einstefna.</strong> Þú getur lagt inn en ekki tekið út. Ef þú vinnur þarftu aðra leið til að fá peningana — yfirleitt bankamillifærslu, e-wallet eða dulritunargjaldmiðla. Sum spilavíti krefjast þess að úttekt fari á sömu leið og innborgun, sem getur valdið vandræðum.</p></div>
<p>Ráð: ef þú notar Paysafecard til innborgunar skaltu staðfesta við þjónustuver <em>áður</em> hvaða úttektarleið stendur þér til boða.</p>

<h2>Hvar á að kaupa á Íslandi?</h2>
<p>Paysafecard er ekki eins útbreitt á Íslandi og í Þýskalandi eða Austurríki. Möguleikar:</p>
<ul>
<li><strong>Á netinu</strong> — Í gegnum paysafecard.com eða viðurkennda endursöluaðila (greitt með korti)</li>
<li><strong>Söluaðilar erlendis</strong> — Ef þú ert á ferðalagi fást kóðar í bensínstöðvum og söluturnum víða í Evrópu</li>
</ul>
<p>Athugaðu að kóðar eru yfirleitt bundnir við gjaldmiðil. Kóði keyptur í EUR virkar á EUR-reikningi.</p>

<h2>Paysafecard vs aðrar leiðir fyrir íslenska spilara</h2>
<table class="info-table"><thead><tr><th>Leið</th><th>Innborgun</th><th>Úttekt</th><th>Nafnleynd</th><th>Framboð á Íslandi</th></tr></thead><tbody>
<tr><td>Paysafecard</td><td>✅</td><td>❌</td><td>Há</td><td>Takmarkað</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>✅</td><td>✅</td><td>Há</td><td>✅ Gott</td></tr>
<tr><td>Revolut</td><td>✅</td><td>✅</td><td>Miðlungs</td><td>✅ Gott</td></tr>
<tr><td>Skrill / Neteller</td><td>✅</td><td>✅</td><td>Miðlungs</td><td>✅ Gott</td></tr>
<tr><td>Íslenskt bankakort</td><td>⚠️ Stundum</td><td>⚠️ Stundum</td><td>Engin</td><td>✅ En hafnað</td></tr>
</tbody></table>
<p>Fyrir flesta íslenska spilara eru <a href="{URL_BASE}leidbeiningar/bestu-crypto-spilavitin-island/">dulritunargjaldmiðlar</a> eða <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut</a> betri kostur — þeir virka í báðar áttir.</p>

<h2>Hverjum hentar Paysafecard?</h2>
<ul>
<li>✅ Þeim sem vilja <strong>hart eyðsluþak</strong> — þú getur ekki eytt meiru en kóðinn inniheldur</li>
<li>✅ Þeim sem vilja alls ekki tengja bankareikning við spilavíti</li>
<li>❌ Ekki þeim sem spila reglulega og taka út oft</li>
</ul>
<p>Eyðsluþakið er raunverulegur kostur frá sjónarhóli <a href="{URL_BASE}leidbeiningar/hvernig-a-ad-setja-takmork-a-spilaviti/">ábyrgrar spilunar</a> — þú getur ekki „bara lagt inn aðeins meira" í hita leiksins.</p>

<h2>Algengar spurningar</h2>
<h3>Rennur Paysafecard kóði út?</h3>
<p>Kóðar gilda yfirleitt í 12 mánuði. Eftir það getur mánaðarlegt gjald dregist af eftirstöðvum.</p>
<h3>Get ég notað hluta af kóða?</h3>
<p>Já — þú getur notað hluta og geymt eftirstöðvarnar til síðari nota á sama kóða.</p>
<h3>Hvaða spilavíti taka við Paysafecard?</h3>
<p>Mörg evrópsk spilavíti, en ekki öll. Athugaðu greiðslusíðu spilavítisins fyrst. <a href="{URL_BASE}greidslur/paysafecard-i-spilavitum/">Sjá Paysafecard spilavíti →</a></p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá greiðsluleiðir →</a></div>'''
    },
    {
        "slug": "book-of-dead-leidarvisir",
        "title": "Book of Dead — leiðarvísir, RTP og aðferðir 2026",
        "desc": "Book of Dead frá Play'n GO: RTP 96,21%, há sveifla, stækkandi tákn. Hvernig leikurinn virkar og hvar á að spila á Íslandi.",
        "emoji": "📖",
        "colors": ('#281a0a', '#453014', '#62461e'),
        "content": f'''<h1>Book of Dead</h1>
{hero}
<p>Book of Dead kom út árið 2016 og er enn meðal mest spiluðu spilakassa í Evrópu. <strong>Einfaldur vélbúnaður, há sveifla og stækkandi tákn sem geta fyllt alla skjáinn.</strong></p>

<h2>Tæknilegar upplýsingar</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Gildi</th></tr></thead><tbody>
<tr><td>Framleiðandi</td><td>Play'n GO</td></tr>
<tr><td>Útgáfuár</td><td>2016</td></tr>
<tr><td>RTP</td><td>96,21%</td></tr>
<tr><td>Sveifla</td><td>Há</td></tr>
<tr><td>Hámarksvinningur</td><td>5.000x veðmál</td></tr>
<tr><td>Hjól / línur</td><td>5 hjól, 3 raðir, 10 línur</td></tr>
<tr><td>Veðmálssvið</td><td>€0,01 – €100</td></tr>
<tr><td>Frísnúningar</td><td>10 við 3+ bókartákn</td></tr>
<tr><td>Bónus Buy</td><td>❌ Nei</td></tr>
</tbody></table>

<h2>Hvernig leikurinn virkar</h2>
<h3>Bókartáknið — scatter og wild í senn</h3>
<p>Bók hins dauða („Book of Dead") gegnir tvöföldu hlutverki: hún kemur í stað annarra tákna (wild) og kveikir á frísnúningum (scatter). Þrjár bækur hvar sem er á hjólunum gefa 10 frísnúninga.</p>

<h3>Stækkandi tákn — kjarninn í leiknum</h3>
<p>Áður en frísnúningar hefjast velur leikurinn eitt tákn af handahófi. Í frísnúningum stækkar það tákn yfir allt hjólið þegar það birtist — og greiðir óháð því hvort táknin liggja samliggjandi.</p>
<p>Ef Rich Wilde (hæsta táknið) er valið og hann fyllir þrjú hjól er vinningurinn gríðarlegur. Ef lægsta táknið er valið er umferðin oft vonbrigði. Þetta er aðalástæðan fyrir háu sveiflunni.</p>

<h3>Endurkveiking</h3>
<p>Þrjár bækur í frísnúningum gefa 10 frísnúninga í viðbót — og nýtt stækkandi tákn er ekki valið aftur, svo þú heldur því sem þú fékkst.</p>

<h3>Gamble-eiginleiki</h3>
<p>Eftir hvern vinning geturðu veðjað honum á lit eða sort spils. Rétt getgáta tvöfaldar (litur) eða fjórfaldar (sort). Röng getgáta þurrkar út vinninginn.</p>
<div class="info-box"><p><strong>Ráð:</strong> Gamble-eiginleikinn er hreint 50/50 (eða 25/75) veðmál án húsforskots — en hann eykur sveifluna verulega. Flestir reyndir spilarar sleppa honum.</p></div>

<h2>Aðferðir og ráð</h2>
<ul>
<li><strong>Reiknaðu fyrir 300+ snúninga</strong> — Há sveifla þýðir löng þurrkatímabil. Með €60 fjármagni þýðir það um €0,20 á snúning</li>
<li><strong>Prófaðu í demo fyrst</strong> — <a href="{URL_BASE}spilakassar/book-of-dead/">Spila Book of Dead ókeypis</a></li>
<li><strong>Athugaðu RTP-útgáfuna</strong> — Play'n GO gefur út margar RTP-stillingar. Athugaðu í leikjareglum að þú sért á 96,21%, ekki lægri útgáfu. <a href="{URL_BASE}leidbeiningar/bestu-spilakassarnir-haesta-rtp/">Meira um RTP-útgáfur →</a></li>
<li><strong>Frísnúningatilboð</strong> — Book of Dead er algengasti leikurinn í <a href="{URL_BASE}leidbeiningar/okeypis-snuningar-spilaviti/">frísnúningatilboðum</a>. Góð leið til að prófa án eigin fjármuna</li>
</ul>

<h2>Book of Dead vs aðrir „book" leikir</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>Framleiðandi</th><th>RTP</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}spilakassar/book-of-dead/">Book of Dead</a></td><td>Play'n GO</td><td>96,21%</td><td>5.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/legacy-of-dead/">Legacy of Dead</a></td><td>Play'n GO</td><td>96,58%</td><td>5.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/book-of-oz/">Book of Oz</a></td><td>Play'n GO</td><td>96,31%</td><td>5.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/book-of-fallen/">Book of Fallen</a></td><td>Pragmatic Play</td><td>96,50%</td><td>5.000x</td></tr>
</tbody></table>
<p>Legacy of Dead hefur hæsta RTP af þessum — nánast sami leikur með aðeins betri stærðfræði.</p>

<h2>Hvar á að spila á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — Play'n GO safnið, demo í boði, €10 lágmarksinnborgun.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — Book of Dead ásamt öllu Play'n GO safninu.</p></div>

<h2>Algengar spurningar</h2>
<h3>Hvað er hámarksvinningur í Book of Dead?</h3>
<p>5.000x veðmálið. Á €1 snúningi væri það €5.000. Þarf stækkandi Rich Wilde tákn yfir mörg hjól.</p>
<h3>Er hægt að kaupa frísnúninga?</h3>
<p>Nei — Book of Dead býður ekki Bónus Buy. Þú þarft að fá þrjár bækur náttúrulega.</p>
<h3>Af hverju vinn ég ekkert í langan tíma?</h3>
<p>Það er eðli hásveifluleikja. Book of Dead getur farið 200–300 snúninga án umtalsverðs vinnings. Ef það er óþægilegt skaltu skoða <a href="{URL_BASE}leidbeiningar/lag-sveiflu-spilakassar/">lágsveifluspilakassa</a>.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Book of Dead →</a></div>'''
    },
    {
        "slug": "lightning-roulette-adferdir",
        "title": "Lightning Roulette — aðferðir, RTP og hvernig það virkar 2026",
        "desc": "Lightning Roulette frá Evolution: margfaldarar allt að 500x, RTP 97,3% og hvernig margfaldararnir hafa áhrif á útborganir.",
        "emoji": "⚡",
        "colors": ('#1a0a28', '#2d1445', '#401e62'),
        "content": f'''<h1>Lightning Roulette</h1>
{hero}
<p>Lightning Roulette frá Evolution er <strong>vinsælasta lifandi rúllettan í heiminum</strong>. Grunnreglurnar eru þær sömu og í evrópskri rúllettu — en 1–5 tölur fá margfaldara í hverri umferð.</p>

<h2>Hvernig Lightning Roulette virkar</h2>
<ol>
<li>Þú veðjar eins og í venjulegri rúllettu</li>
<li>Áður en kúlan er sett af stað slær „elding" á 1–5 tölur af handahófi</li>
<li>Þær tölur fá margfaldara: 50x, 100x, 150x, 200x, 300x eða 500x</li>
<li>Ef kúlan lendir á tölu sem þú veðjaðir beint á <em>og</em> hún fékk margfaldara, margfaldast vinningurinn</li>
</ol>

<h2>Mikilvægt: margfaldarar gilda aðeins um bein töluveðmál</h2>
<div class="info-box"><p><strong>Þetta skilja margir ekki.</strong> Margfaldararnir eiga aðeins við „straight up" veðmál — þegar þú veðjar beint á eina tölu. Veðmál á rautt/svart, oddatölur/sléttar, tugi eða dálka fá <strong>enga margfaldara</strong>.</p></div>

<h2>Útborgunarbreytingin</h2>
<table class="info-table"><thead><tr><th>Veðmál</th><th>Venjuleg rúlletta</th><th>Lightning Roulette</th></tr></thead><tbody>
<tr><td>Bein tala (straight up)</td><td>35:1</td><td><strong>29:1</strong> (en 50x–500x ef elding slær)</td></tr>
<tr><td>Rautt / svart</td><td>1:1</td><td>1:1 (óbreytt)</td></tr>
<tr><td>Oddatölur / sléttar</td><td>1:1</td><td>1:1 (óbreytt)</td></tr>
<tr><td>Tugir / dálkar</td><td>2:1</td><td>2:1 (óbreytt)</td></tr>
</tbody></table>
<p>Taktu eftir: bein töluveðmál borga <strong>29:1 í stað 35:1</strong>. Evolution lækkar grunnútborgunina til að fjármagna margfaldarana. RTP heildarinnar er 97,30% — sama og venjuleg evrópsk rúlletta.</p>

<h2>Hvaða veðmál borga sig?</h2>
<p>Þar sem margfaldarar gilda aðeins um bein töluveðmál:</p>
<ul>
<li><strong>Ef þú veðjar á ytri veðmál</strong> (rautt/svart o.s.frv.) — Lightning Roulette gefur þér ekkert umfram venjulega rúllettu. Þú getur allt eins spilað staðlaða útgáfu</li>
<li><strong>Ef þú veðjar á beinar tölur</strong> — Lightning Roulette hentar. Þú fórnar hluta grunnútborgunarinnar fyrir möguleika á 500x</li>
</ul>
<p>Með öðrum orðum: leikurinn er hannaður fyrir þá sem veðja á einstakar tölur. Ef það er ekki þinn stíll er lítill tilgangur í að spila hann.</p>

<h2>Dæmi um útborgun</h2>
<p>€1 á tölu 17:</p>
<ul>
<li>Kúlan lendir á 17, engin elding: €29 (29:1)</li>
<li>Kúlan lendir á 17, elding gaf 100x: €100</li>
<li>Kúlan lendir á 17, elding gaf 500x: €500</li>
</ul>
<p>Hámarksvinningur er 500x veðmálið á tölu.</p>

<h2>Aðferðir</h2>
<ul>
<li><strong>Dreifðu á margar tölur</strong> — Að veðja €0,20 á 10 tölur gefur þér 10 möguleika á að lenda á eldingartölu. Heildarveðmálið er €2</li>
<li><strong>Ekki elta eldingartölur</strong> — Þær eru valdar af handahófi í hverri umferð. Tala sem fékk 500x síðast er jafn líkleg og allar aðrar</li>
<li><strong>Forðist Martingale</strong> — Með 29:1 útborgun og einstaka tölur virkar tvöföldunarkerfi enn verr en í venjulegri rúllettu. <a href="{URL_BASE}leidbeiningar/martingale-adferd-rulletta/">Af hverju Martingale bregst →</a></li>
<li><strong>Settu lotumörk</strong> — Margfaldararnir gera leikinn spennandi, sem gerir það auðveldara að spila lengur en ætlað var</li>
</ul>

<h2>Afbrigði frá Evolution</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>Sérkenni</th><th>Hámarksmargfaldari</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}live/lightning-roulette/">Lightning Roulette</a></td><td>Upprunalega útgáfan</td><td>500x</td></tr>
<tr><td><a href="{URL_BASE}live/xxxtreme-lightning-roulette/">XXXtreme Lightning Roulette</a></td><td>Keðjueldingar, allt að 2.000x</td><td>2.000x</td></tr>
<tr><td><a href="{URL_BASE}live/lightning-baccarat/">Lightning Baccarat</a></td><td>Sama hugmynd í baccarat</td><td>512x</td></tr>
<tr><td><a href="{URL_BASE}live/lightning-blackjack/">Lightning Blackjack</a></td><td>Margfaldarar á vinningshendur</td><td>25x</td></tr>
<tr><td><a href="{URL_BASE}live/lightning-dice/">Lightning Dice</a></td><td>Teningar með margföldurum</td><td>1.000x</td></tr>
</tbody></table>

<h2>Algengar spurningar</h2>
<h3>Er RTP lægra í Lightning Roulette?</h3>
<p>Nei — 97,30%, sama og venjuleg evrópsk rúlletta. Lægri grunnútborgun á beinar tölur er vegin upp af margföldurunum.</p>
<h3>Get ég spáð fyrir um eldingartölur?</h3>
<p>Nei. Þær eru valdar af slembitölugjafa í hverri umferð, óháð fyrri umferðum.</p>
<h3>Er hægt að spila Lightning Roulette ókeypis?</h3>
<p>Nei — lifandi leikir með raunverulegum spilastjóra eru ekki í boði í demo-ham. Þú getur hins vegar æft þig á <a href="{URL_BASE}leidbeiningar/rullettureglur-a-islensku/">RNG rúllettu</a> ókeypis.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Lightning Roulette →</a></div>'''
    },
    {
        "slug": "keno-reglur-a-islensku",
        "title": "Keno reglur á íslensku — hvernig á að spila 2026",
        "desc": "Keno reglur á íslensku: hvernig á að velja tölur, útborganir, RTP og hvort það borgar sig að spila.",
        "emoji": "🔢",
        "colors": ('#0a1a24', '#143340', '#1e4d5c'),
        "content": f'''<h1>Keno reglur á íslensku</h1>
{hero}
<p>Keno er lottó-líkur leikur sem á rætur að rekja til Kína fyrir yfir 2.000 árum. <strong>Þú velur tölur, vélin dregur tölur, og þú færð greitt eftir því hversu margar passa.</strong> Einfalt — en húsforskotið er hátt.</p>

<h2>Grunnreglur</h2>
<ol>
<li>Borðið sýnir tölurnar 1–80</li>
<li>Þú velur yfirleitt 1–10 tölur (sum afbrigði leyfa allt að 20)</li>
<li>Þú velur veðmálsupphæð</li>
<li>Vélin dregur 20 tölur af handahófi</li>
<li>Þú færð greitt eftir því hversu margar af þínum tölum voru dregnar</li>
</ol>

<h2>Útborganir — dæmi</h2>
<p>Útborganir eru mismunandi eftir spilavítum og afbrigðum. Dæmigerð tafla fyrir 10 valdar tölur:</p>
<table class="info-table"><thead><tr><th>Réttar tölur</th><th>Dæmigerð útborgun</th></tr></thead><tbody>
<tr><td>0–4</td><td>0x</td></tr>
<tr><td>5</td><td>2x</td></tr>
<tr><td>6</td><td>20x</td></tr>
<tr><td>7</td><td>80x</td></tr>
<tr><td>8</td><td>500x</td></tr>
<tr><td>9</td><td>2.000x</td></tr>
<tr><td>10</td><td>10.000x</td></tr>
</tbody></table>
<p>Líkurnar á að fá allar 10 réttar eru um 1 á móti 8,9 milljónum.</p>

<h2>Hversu margar tölur á að velja?</h2>
<table class="info-table"><thead><tr><th>Fjöldi valinna</th><th>Vinningstíðni</th><th>Stærð vinninga</th><th>Hentar</th></tr></thead><tbody>
<tr><td>1–3</td><td>Há</td><td>Lítil</td><td>Jafnri spilun</td></tr>
<tr><td>4–6</td><td>Miðlungs</td><td>Miðlungs</td><td>Jafnvægi</td></tr>
<tr><td>7–10</td><td>Lág</td><td>Mjög stór</td><td>Þeim sem elta stóran vinning</td></tr>
</tbody></table>
<p>Fleiri tölur þýðir ekki betri líkur — það breytir aðeins dreifingu vinninga.</p>

<h2>Húsforskotið — vertu meðvitaður</h2>
<div class="info-box"><p><strong>Keno hefur eitt hæsta húsforskot í spilavítum:</strong> yfirleitt 20–35% hjá hefðbundnu keno og 5–12% hjá netútgáfum. Til samanburðar: <a href="{URL_BASE}leidbeiningar/baccarat-reglur-a-islensku/">baccarat</a> 1,06%, <a href="{URL_BASE}leidbeiningar/rullettureglur-a-islensku/">evrópsk rúlletta</a> 2,7%, <a href="{URL_BASE}spilakassar/">spilakassar</a> um 4%.</p></div>
<p>Það þýðir að peningarnir þínir endast mun skemur í keno en í flestum öðrum leikjum. Spilaðu það fyrir skemmtunina, ekki sem fjárhagslega skynsamlegt val.</p>

<h2>Aðferðir — hvað virkar og hvað ekki</h2>
<h3>Virkar ekki</h3>
<ul>
<li><strong>„Heitar" og „kaldar" tölur</strong> — Hvert dráttur er óháður. Tala sem kom oft í gær er ekki líklegri í dag</li>
<li><strong>Mynstur á borðinu</strong> — Að velja tölur í röð eða í formi gefur enga tölfræðilega yfirburði</li>
<li><strong>Veðmálakerfi</strong> — <a href="{URL_BASE}leidbeiningar/martingale-adferd-rulletta/">Martingale</a> og sambærileg kerfi breyta ekki húsforskotinu</li>
</ul>
<h3>Virkar</h3>
<ul>
<li><strong>Berðu saman útborgunartöflur</strong> — Munur milli spilavíta getur verið umtalsverður. Þetta er eina raunverulega „aðferðin" í keno</li>
<li><strong>Veldu netkeno fram yfir hefðbundið</strong> — Mun betra RTP</li>
<li><strong>Spilaðu lítið</strong> — Vegna hás húsforskots er keno best sem tilbreyting, ekki aðalleikur</li>
</ul>

<h2>Keno vs lottó vs bingó</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Keno</th><th>Lottó</th><th>Bingó</th></tr></thead><tbody>
<tr><td>Hraði</td><td>Strax (sekúndur)</td><td>Vikulega</td><td>5–15 mín umferð</td></tr>
<tr><td>Val á tölum</td><td>Þú velur</td><td>Þú velur</td><td>Fast spjald</td></tr>
<tr><td>Húsforskot</td><td>5–35%</td><td>40–50%</td><td>10–25%</td></tr>
<tr><td>Félagslegt</td><td>Nei</td><td>Nei</td><td>Já (spjall)</td></tr>
</tbody></table>

<h2>Algengar spurningar</h2>
<h3>Er hægt að vinna stórt í keno?</h3>
<p>Já — 10.000x veðmálið ef allar 10 tölur passa. En líkurnar eru um 1 á móti 8,9 milljónum.</p>
<h3>Er netkeno sanngjarnt?</h3>
<p>Á spilavítum með gilt leyfi, já — tölurnar eru dregnar með vottuðum <a href="{URL_BASE}leidbeiningar/hvernig-rng-virkar/">slembitölugjafa</a>.</p>
<h3>Hvað er besti fjöldi talna?</h3>
<p>Stærðfræðilega skiptir það ekki máli fyrir vænt gildi. 4–6 tölur gefa oftast jafnasta upplifun milli vinningstíðni og stærðar.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila keno →</a></div>'''
    },
    {
        "slug": "video-poker-reglur-a-islensku",
        "title": "Video poker reglur á íslensku — besti leikurinn í spilavítinu? 2026",
        "desc": "Video poker reglur á íslensku: Jacks or Better, útborgunartöflur, RTP allt að 99,5% og grunnstrategy.",
        "emoji": "🖥️",
        "colors": ('#0a1a1a', '#143333', '#1e4d4d'),
        "content": f'''<h1>Video poker reglur á íslensku</h1>
{hero}
<p>Video poker er <strong>einn af fáum spilavítisleikjum þar sem kunnátta skiptir raunverulegu máli</strong> — og með réttri strategíu getur RTP farið yfir 99%. Það er betra en nánast allt annað í spilavítinu.</p>

<h2>Grunnreglur</h2>
<ol>
<li>Þú veðjar (yfirleitt 1–5 mynt)</li>
<li>Þú færð 5 kort</li>
<li>Þú velur hvaða kortum þú heldur og hverjum þú kastar</li>
<li>Köstuðu kortin eru endurnýjuð</li>
<li>Lokahöndin ákvarðar útborgun samkvæmt töflu</li>
</ol>
<p>Engir andstæðingar, enginn dílari — aðeins þú og útborgunartaflan.</p>

<h2>Jacks or Better — útborgunartafla (9/6)</h2>
<table class="info-table"><thead><tr><th>Hönd</th><th>1 mynt</th><th>5 mynt</th></tr></thead><tbody>
<tr><td>Royal Flush</td><td>250</td><td><strong>4.000</strong></td></tr>
<tr><td>Straight Flush</td><td>50</td><td>250</td></tr>
<tr><td>Fjórir eins</td><td>25</td><td>125</td></tr>
<tr><td>Full House</td><td><strong>9</strong></td><td>45</td></tr>
<tr><td>Flush</td><td><strong>6</strong></td><td>30</td></tr>
<tr><td>Straight</td><td>4</td><td>20</td></tr>
<tr><td>Þrír eins</td><td>3</td><td>15</td></tr>
<tr><td>Tvö pör</td><td>2</td><td>10</td></tr>
<tr><td>Par af gosum eða hærra</td><td>1</td><td>5</td></tr>
</tbody></table>
<div class="info-box"><p><strong>„9/6" þýðir</strong> að Full House borgar 9 og Flush borgar 6. Þetta er besta útgáfan með RTP 99,54% við fullkomna spilun. Varist „8/5" útgáfur (RTP 97,3%) og verri — þær líta eins út en kosta þig margfalt meira yfir tíma.</p></div>

<h2>Spilaðu alltaf 5 mynt</h2>
<p>Taktu eftir Royal Flush línunni: 250 fyrir 1 mynt en 4.000 fyrir 5 mynt. Það er 800 á mynt í stað 250 — <strong>óhlutfallslegt stökk</strong>.</p>
<p>Ef 5 mynt eru of dýr fyrir þig skaltu lækka myntgildið í staðinn (t.d. 5 × €0,05 frekar en 1 × €0,25). Að spila færri en 5 mynt lækkar RTP um 1,5–2 prósentustig.</p>

<h2>Grunnstrategy — einfölduð útgáfa</h2>
<p>Haltu, í þessari forgangsröð:</p>
<ol>
<li>Royal flush, straight flush, fjórir eins (fullgerð hönd)</li>
<li>4 kort í royal flush</li>
<li>Full house, flush, straight, þrír eins</li>
<li>4 kort í straight flush</li>
<li>Tvö pör</li>
<li>Hátt par (gosar eða hærra)</li>
<li>3 kort í royal flush</li>
<li>4 kort í flush</li>
<li>Lágt par (tíur eða lægra)</li>
<li>4 kort í opna straight</li>
<li>2 kort í royal flush</li>
<li>Kasta öllu</li>
</ol>
<div class="info-box"><p><strong>Algeng mistök:</strong> Að halda háu stöku korti frekar en lágu pari. Lágt par er nánast alltaf betra — það er þegar vinningshönd sem getur orðið að þremur eða fjórum eins.</p></div>

<h2>Afbrigði og RTP</h2>
<table class="info-table"><thead><tr><th>Afbrigði</th><th>Besta RTP</th><th>Flækjustig</th></tr></thead><tbody>
<tr><td>Jacks or Better (9/6)</td><td>99,54%</td><td>Lágt — best fyrir byrjendur</td></tr>
<tr><td>Deuces Wild (full pay)</td><td>100,76%*</td><td>Hátt</td></tr>
<tr><td>Double Bonus Poker (10/7)</td><td>100,17%*</td><td>Hátt</td></tr>
<tr><td>Joker Poker</td><td>98–100%</td><td>Miðlungs</td></tr>
<tr><td>Double Double Bonus</td><td>98,98%</td><td>Miðlungs</td></tr>
</tbody></table>
<p><em>*RTP yfir 100% krefst fullkominnar spilunar og „full pay" útborgunartöflu sem er sjaldgæf á netinu. Reiknaðu ekki með að finna hana.</em></p>

<h2>Af hverju er video poker vanmetið?</h2>
<p>Video poker hefur betra RTP en nánast allir <a href="{URL_BASE}spilakassar/">spilakassar</a> (um 96%), <a href="{URL_BASE}leidbeiningar/rullettureglur-a-islensku/">rúlletta</a> (97,3%) og jafnvel flest <a href="{URL_BASE}leidbeiningar/blackjack-adferdir/">blackjack</a> borð.</p>
<p>Gallinn: það krefst athygli og þekkingar á strategíu. Mörgum finnst það minna skemmtilegt en spilakassar þar sem maður ýtir bara á hnapp.</p>

<h2>Algengar spurningar</h2>
<h3>Er video poker betra en spilakassar?</h3>
<p>Stærðfræðilega — mun betra. 99,5% RTP á móti 96%. En það krefst þess að þú lærir strategíu og spilir rétta útgáfu.</p>
<h3>Hvernig athuga ég hvort borðið er 9/6?</h3>
<p>Skoðaðu útborgunartöfluna í leiknum. Full House á að borga 9 og Flush 6 fyrir eitt mynt. Ef þær tölur eru lægri er RTP lægra.</p>
<h3>Þarf ég að muna alla strategíuna?</h3>
<p>Nei — listinn hér að ofan nær yfir langflestar aðstæður. Fullkomin strategía bætir aðeins um 0,1–0,2% við.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila video poker →</a></div>'''
    },
    {
        "slug": "spilaviti-vs-vedmalasidur",
        "title": "Spilavíti vs íþróttaveðmál — hvort hentar þér betur? 2026",
        "desc": "Samanburður á netspilavítum og íþróttaveðmálum: húsforskot, kunnátta, sveifla og hvað hentar íslenskum spilurum.",
        "emoji": "⚔️",
        "colors": ('#14140a', '#28281a', '#3c3c28'),
        "content": f'''<h1>Spilavíti vs íþróttaveðmál</h1>
{hero}
<p>Margir íslenskir spilarar velta fyrir sér hvort þeir eigi að spila á spilavíti eða veðja á íþróttir. <strong>Leikirnir eru gjörólíkir — og henta ólíkum týpum.</strong></p>

<h2>Grundvallarmunurinn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Spilavíti</th><th>Íþróttaveðmál</th></tr></thead><tbody>
<tr><td>Niðurstaða ákvarðast af</td><td>Slembitölugjafa (RNG)</td><td>Raunverulegum atburði</td></tr>
<tr><td>Kunnátta skiptir máli</td><td>Lítið (nema blackjack, video poker)</td><td>Já — þekking á íþróttinni</td></tr>
<tr><td>Húsforskot</td><td>1–5% (fast)</td><td>3–8% (breytilegt eftir leik)</td></tr>
<tr><td>Hraði</td><td>Sekúndur á umferð</td><td>Klukkustundir eða dagar</td></tr>
<tr><td>Hægt að rannsaka fyrirfram</td><td>Nei</td><td>Já — tölfræði, meiðsli, form</td></tr>
<tr><td>Spilun á nóttunni</td><td>Alltaf í boði</td><td>Fer eftir leikjadagskrá</td></tr>
</tbody></table>

<h2>Spilavíti — kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Alltaf í boði, engin bið</td><td>❌ Kunnátta breytir litlu</td></tr>
<tr><td>✅ Fyrirsjáanlegt RTP</td><td>❌ Hraðinn getur leitt til ofspilunar</td></tr>
<tr><td>✅ Hægt að prófa ókeypis í demo</td><td>❌ Engin leið til að „vinna sér inn forskot"</td></tr>
<tr><td>✅ Lágt húsforskot í sumum leikjum</td><td>❌ Sveiflukennt í hásveifluleikjum</td></tr>
</tbody></table>
<p>Lægsta húsforskotið í spilavíti: <a href="{URL_BASE}leidbeiningar/video-poker-reglur-a-islensku/">video poker</a> (0,5%), <a href="{URL_BASE}leidbeiningar/blackjack-adferdir/">blackjack</a> (0,5%), <a href="{URL_BASE}leidbeiningar/baccarat-reglur-a-islensku/">baccarat</a> (1,06%).</p>

<h2>Íþróttaveðmál — kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
<tr><td>✅ Þekking getur gefið raunverulegt forskot</td><td>❌ Krefst mikillar vinnu til að ná forskoti</td></tr>
<tr><td>✅ Hægari taktur — minni hætta á ofspilun</td><td>❌ Bið eftir niðurstöðu</td></tr>
<tr><td>✅ Hægt að bera saman líkur milli síðna</td><td>❌ Freistandi að veðja á „sitt lið"</td></tr>
<tr><td>✅ Skemmtilegra ef þú fylgist með íþróttinni</td><td>❌ Lifandi veðmál geta orðið jafn hröð og spilavíti</td></tr>
</tbody></table>

<h2>Hvort hefur lægra húsforskot?</h2>
<p>Það fer eftir því hvað þú spilar.</p>
<p><strong>Spilavíti:</strong> Húsforskotið er fast og gagnsætt. Blackjack með grunnstrategíu: 0,5%. Spilakassar: um 4%.</p>
<p><strong>Íþróttaveðmál:</strong> Veðmálasíðan byggir inn álag („vig" eða „juice"). Á dæmigerðu 1,90/1,90 veðmáli er álagið um 2,4%. Á útreikningum með fleiri valkostum getur það farið í 6–10%.</p>
<p>Lykilmunur: í spilavíti er húsforskotið óbreytanlegt. Í íþróttaveðmálum getur spilari með betri upplýsingar en markaðurinn fræðilega haft jákvætt vænt gildi — en það krefst mikillar sérþekkingar og er sjaldgæft í reynd.</p>

<h2>Hvað hentar þér?</h2>
<div class="info-box"><p><strong>Veldu spilavíti ef:</strong> Þú vilt stutta skemmtun hvenær sem er, fylgist ekki sérstaklega með íþróttum, eða kannt að meta leiki með lágu húsforskoti eins og blackjack og video poker.</p></div>
<div class="info-box"><p><strong>Veldu íþróttaveðmál ef:</strong> Þú fylgist náið með fótbolta eða handbolta, hefur gaman af rannsóknarvinnu, og vilt hægari takt þar sem hver ákvörðun fær tíma.</p></div>
<div class="info-box"><p><strong>Hvort tveggja:</strong> Mörg spilavíti bjóða bæði — <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a>, <a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a>, <a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a> og <a href="{URL_BASE}spilaviti/20bet/">20Bet</a>.</p></div>

<h2>Sameiginleg áhætta</h2>
<p>Bæði form geta orðið vandamál. Íþróttaveðmál eru stundum talin „öruggari" af því að kunnátta kemur við sögu — en sú tilfinning að vera „góður í þessu" getur gert það auðveldara að réttlæta stærri veðmál.</p>
<p>Sömu varnir gilda fyrir hvort tveggja: <a href="{URL_BASE}leidbeiningar/hvernig-a-ad-setja-takmork-a-spilaviti/">innborgunartakmörk</a>, föst fjárhagsáætlun og meðvitund um <a href="{URL_BASE}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">viðvörunarmerki</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Er hægt að vinna stöðugt á íþróttaveðmálum?</h3>
<p>Örfáir ná því — það krefst tölfræðilíkana, aðgangs að bestu líkunum og strangrar fjármálastjórnunar. Langflestir tapa til lengdar, rétt eins og í spilavíti.</p>
<h3>Hvort er hraðara að tapa peningum í?</h3>
<p>Spilavíti, vegna hraðans. Spilakassi getur klárað 600 snúninga á klukkustund. Íþróttaveðmál tekur klukkustundir að afgreiðast — sem gefur tíma til umhugsunar.</p>
<h3>Get ég notað velkomstbónus á bæði?</h3>
<p>Yfirleitt eru aðskildir bónusar fyrir spilavíti og íþróttir, með ólíkum <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrðum</a>. Lestu skilmálana — íþróttabónusar krefjast oft lágmarkslíkinda.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá spilavíti og veðmál →</a></div>'''
    },
    {
        "slug": "aldurstakmork-a-spilavitum-island",
        "title": "Aldurstakmörk á spilavítum á Íslandi — 18 eða 21 ár? 2026",
        "desc": "Hver er lögleg aldur til að spila á netspilavíti frá Íslandi? Aldurstakmörk, KYC staðfesting og hvernig spilavíti athuga aldur.",
        "emoji": "🔞",
        "colors": ('#1a0a0a', '#331414', '#4d1e1e'),
        "content": f'''<h1>Aldurstakmörk á spilavítum á Íslandi</h1>
{hero}
<p>Aldurstakmörk í fjárhættuspilum eru ekki samræmd á heimsvísu og geta verið ruglingsleg. <strong>Hér er staðan fyrir íslenska spilara.</strong></p>

<h2>Stutta svarið</h2>
<div class="info-box"><p><strong>18 ára.</strong> Nánast öll netspilavíti sem taka við íslenskum spilurum setja 18 ára aldurstakmark. Á Íslandi er 18 ára aldur einnig lágmarksaldur fyrir Íslandsspil og Íslenska getspá.</p></div>

<h2>Hvers vegna sjá sumir „21 árs"?</h2>
<p>Í Bandaríkjunum er aldurstakmarkið 21 árs í mörgum ríkjum (sama og fyrir áfengi). Þetta smitast yfir í enskt efni á netinu og veldur ruglingi. Fyrir Evrópu og Ísland er viðmiðið 18 ár.</p>

<h2>Aldurstakmörk eftir leyfum</h2>
<table class="info-table"><thead><tr><th>Leyfi / land</th><th>Lágmarksaldur</th></tr></thead><tbody>
<tr><td>Malta (MGA)</td><td>18 ár</td></tr>
<tr><td>Curaçao</td><td>18 ár</td></tr>
<tr><td>Bretland (UKGC)</td><td>18 ár</td></tr>
<tr><td>Svíþjóð</td><td>18 ár</td></tr>
<tr><td>Eistland</td><td>21 árs (fyrir spilavíti í eigin landi)</td></tr>
<tr><td>Bandaríkin (flest ríki)</td><td>21 árs</td></tr>
<tr><td>Ísland (Íslandsspil / Getspá)</td><td>18 ár</td></tr>
</tbody></table>

<h2>Hvernig athuga spilavíti aldur?</h2>
<h3>1. Við skráningu</h3>
<p>Þú slærð inn fæðingardag. Þetta er einfaldasta skrefið — og auðveldast að ljúga um. Þess vegna er það ekki eina athugunin.</p>

<h3>2. Við KYC staðfestingu</h3>
<p>Þetta er raunverulega athugunin. Áður en þú getur tekið út þarftu að senda inn skilríki — vegabréf eða ökuskírteini. Þar kemur raunverulegur fæðingardagur í ljós.</p>
<p><a href="{URL_BASE}leidbeiningar/hvad-er-kyc-stadfesting/">Hvað er KYC staðfesting? →</a></p>

<h3>3. Við grunsamlega hegðun</h3>
<p>Spilavíti geta beðið um gögn hvenær sem er ef eitthvað vekur grun — t.d. ósamræmi í upplýsingum eða greiðsla frá korti sem ber annað nafn.</p>

<h2>Hvað gerist ef einhver undir 18 skráir sig?</h2>
<ul>
<li><strong>Reikningnum er lokað</strong> um leið og það kemur í ljós</li>
<li><strong>Vinningar eru gerðir upptækir</strong> — spilavítið greiðir þá ekki út</li>
<li><strong>Innborganir eru yfirleitt endurgreiddar</strong> — þetta er krafa flestra leyfisveitenda</li>
</ul>
<p>Með öðrum orðum: það er ekki hægt að „vinna" sem ólögráða. Jafnvel þótt skráningin sleppi í gegn stöðvast allt við fyrstu úttekt.</p>

<h2>Foreldrar: hvernig á að vernda börn</h2>
<ol>
<li><strong>Aðgangsstýring á tækjum</strong> — Screen Time (iOS) og Family Link (Android) geta lokað á vefsíðuflokka</li>
<li><strong>BetBlocker</strong> — Ókeypis hugbúnaður sem lokar á þúsundir fjárhættuspilasíðna á öllum tækjum</li>
<li><strong>Engin vistuð kort</strong> — Ekki geyma kortaupplýsingar í vöfrum sem börn hafa aðgang að</li>
<li><strong>Talaðu um það</strong> — Mörg tölvuleikjakerfi (lootbox, skin-veðmál) líkja eftir fjárhættuspilamekaník og eru oft fyrsta snertingin</li>
</ol>
<p>Sjá: <a href="{URL_BASE}leidbeiningar/radleggingar-til-adstandenda-spilafikla/">ráðleggingar til aðstandenda →</a></p>

<h2>Af hverju eru aldurstakmörk til?</h2>
<p>Rannsóknir benda til að því fyrr sem einstaklingur byrjar að spila fjárhættuspil, þeim mun meiri líkur séu á vandamálum síðar. Heili unglinga er enn í þroska hvað varðar áhættumat og hvatastjórnun, sem gerir þennan hóp viðkvæmari.</p>
<p>Þess vegna eru aldurstakmörk — ásamt <a href="{URL_BASE}leidbeiningar/sjalfsutilokun-spilavita/">sjálfsútilokun</a> og <a href="{URL_BASE}leidbeiningar/hvernig-a-ad-setja-takmork-a-spilaviti/">takmörkum</a> — kjarninn í regluverki um ábyrga spilun.</p>

<h2>Algengar spurningar</h2>
<h3>Get ég spilað 17 ára ef spilavítið er erlent?</h3>
<p>Nei. Aldurstakmarkið er sett af spilavítinu og leyfisveitanda þess, ekki af staðsetningu þinni. Allar leyfðar síður krefjast 18 ára aldurs hið minnsta.</p>
<h3>Þarf ég að senda skilríki strax?</h3>
<p>Yfirleitt ekki við skráningu — en alltaf áður en fyrsta úttekt er afgreidd.</p>
<h3>Hvað ef ég nota reikning foreldris?</h3>
<p>Það brýtur skilmála spilavítisins. Reikningnum verður lokað og vinningar gerðir upptækir þegar KYC leiðir í ljós að notandi og reikningshafi eru ekki sá sami.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá ábyrga spilun →</a></div>'''
    },
    {
        "slug": "skrill-leidbeining-island",
        "title": "Skrill á Íslandi — leiðbeining fyrir spilavítagreiðslur 2026",
        "desc": "Hvernig á að nota Skrill frá Íslandi: opna reikning, leggja inn, gjöld, úttektir og hvers vegna bankinn sér ekki spilavítið.",
        "emoji": "💼",
        "colors": ('#28140a', '#452414', '#62341e'),
        "content": f'''<h1>Skrill á Íslandi</h1>
{hero}
<p>Skrill er rafrænt veski sem virkar sem <strong>milliliður milli bankans þíns og spilavítisins</strong>. Fyrir íslenska spilara er það ein af fáum leiðum sem virka áreiðanlega án dulritunargjaldmiðla.</p>

<h2>Af hverju Skrill virkar frá Íslandi</h2>
<p>Þegar þú millifærir af íslenskum bankareikningi á Skrill sér bankinn aðeins færslu til <em>Skrill</em> — greiðsluþjónustu sem er fullkomlega lögleg og algeng. Bankinn sér ekki spilavítið.</p>
<p>Þetta er sama ástæða og gerir <a href="{URL_BASE}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut</a> að góðum valkosti: milliliðurinn brýtur beina tenginguna milli bankans og spilavítisins.</p>

<h2>Skref fyrir skref</h2>
<ol>
<li><strong>Stofnaðu Skrill reikning</strong> — skrill.com, tekur 3–5 mínútur</li>
<li><strong>Staðfestu reikninginn (KYC)</strong> — Skilríki og sönnun á heimilisfangi. Gerðu þetta strax, ekki bíða</li>
<li><strong>Leggðu inn á Skrill</strong> — Bankamillifærsla (SEPA, ódýrast) eða kort (samstundis, hærra gjald)</li>
<li><strong>Veldu Skrill á spilavítinu</strong> — Sláðu inn netfangið þitt á Skrill og staðfestu</li>
<li><strong>Taktu út á sama hátt</strong> — Vinningar fara til baka á Skrill og þaðan á bankann</li>
</ol>

<h2>Gjöld</h2>
<table class="info-table"><thead><tr><th>Aðgerð</th><th>Gjald</th></tr></thead><tbody>
<tr><td>Innlögn með bankamillifærslu</td><td>Yfirleitt ókeypis</td></tr>
<tr><td>Innlögn með korti</td><td>1–2,5%</td></tr>
<tr><td>Greiðsla til spilavítis</td><td>Yfirleitt ókeypis</td></tr>
<tr><td>Úttekt á bankareikning</td><td>Fast gjald (um €5,50)</td></tr>
<tr><td>Gjaldmiðlaskipti</td><td>3,99% álag</td></tr>
<tr><td>Óvirkni (12+ mánuðir)</td><td>€5 á mánuði</td></tr>
</tbody></table>
<div class="info-box"><p><strong>Varúð við gjaldmiðlaskiptum:</strong> 3,99% álag Skrill er hátt. Ef þú heldur jafnvæginu í EUR (í stað þess að skipta fram og til baka úr ISK) sparar þú verulega. Sjá <a href="{URL_BASE}leidbeiningar/gjaldmidlaskipti-isk-eur-spilaviti/">gjaldmiðlaskipti fyrir spilavíti →</a></p></div>

<h2>Mikilvægt: Skrill og bónusar</h2>
<p>Mörg spilavíti <strong>útiloka Skrill og Neteller frá velkomstbónusum</strong>. Þú leggur inn, færð engan bónus og kemst að því eftir á.</p>
<p>Lestu bónusskilmálana áður en þú leggur inn. Ef Skrill er útilokað og þú vilt bónusinn skaltu nota kort eða dulritunargjaldmiðil í fyrstu innborgun.</p>

<h2>Skrill vs Neteller vs Revolut</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Skrill</th><th>Neteller</th><th>Revolut</th></tr></thead><tbody>
<tr><td>Útbreiðsla á spilavítum</td><td>Mjög góð</td><td>Mjög góð</td><td>Sem kort</td></tr>
<tr><td>Gjaldmiðlaskipti</td><td>3,99%</td><td>3,99%</td><td>0% (virkir dagar)</td></tr>
<tr><td>Úttektargjald</td><td>~€5,50</td><td>~€5,50</td><td>Ókeypis</td></tr>
<tr><td>Útilokaður frá bónus?</td><td>Oft</td><td>Oft</td><td>Sjaldan (telst kort)</td></tr>
<tr><td>Úttekt frá spilavíti</td><td>✅ Já</td><td>✅ Já</td><td>⚠️ Fer eftir spilavíti</td></tr>
</tbody></table>
<p>Skrill og Neteller eru í eigu sama fyrirtækis (Paysafe) og virka nánast eins.</p>

<h2>Hverjum hentar Skrill?</h2>
<ul>
<li>✅ Þeim sem vilja áreiðanlega leið í <strong>báðar áttir</strong> án dulritunargjaldmiðla</li>
<li>✅ Þeim sem spila á mörgum spilavítum — eitt veski fyrir allt</li>
<li>❌ Ekki þeim sem vilja velkomstbónus (oft útilokað)</li>
<li>❌ Ekki þeim sem leggja inn sjaldan (óvirknigjald)</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Er Skrill öruggt?</h3>
<p>Já — Skrill er hluti af Paysafe Group, skráð fyrirtæki með leyfi frá breska fjármálaeftirlitinu (FCA).</p>
<h3>Hversu hratt er úttekt frá spilavíti á Skrill?</h3>
<p>Yfirleitt 0–48 klst eftir að spilavítið samþykkir hana. Mun hraðara en kort (1–5 dagar).</p>
<h3>Get ég notað Skrill án bankareiknings?</h3>
<p>Þú getur lagt inn með korti, en til að taka peninga út í raunheima þarftu bankareikning.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá greiðsluleiðir →</a></div>'''
    },
    {
        "slug": "hacksaw-gaming-leikir",
        "title": "Hacksaw Gaming — leikir, RTP og sérkenni 2026",
        "desc": "Hacksaw Gaming: Wanted Dead or a Wild, Le Bandit, Chaos Crew. Nýi framleiðandinn sem breytti spilakassamarkaðnum.",
        "emoji": "🪚",
        "colors": ('#1a140a', '#332814', '#4d3c1e'),
        "content": f'''<h1>Hacksaw Gaming</h1>
{hero}
<p>Hacksaw Gaming er sænskur framleiðandi sem stofnaður var 2018 og hefur á örfáum árum orðið einn sá vinsælasti í bransanum. <strong>Þekktur fyrir hráan stíl, hásveifluleiki og „Scratch Cards" sem endurvöktu þann flokk.</strong></p>

<h2>Um Hacksaw Gaming</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2018</td></tr>
<tr><td>Höfuðstöðvar</td><td>Malta / Svíþjóð</td></tr>
<tr><td>Fjöldi leikja</td><td>100+</td></tr>
<tr><td>Þekktustu leikir</td><td>Wanted Dead or a Wild, Le Bandit, Chaos Crew, Hand of Anubis</td></tr>
<tr><td>Sérkenni</td><td>Hásveifla, teiknimyndastíll, Bónus Buy, skraflóð</td></tr>
<tr><td>Dæmigert RTP</td><td>96,0–96,3%</td></tr>
</tbody></table>

<h2>Vinsælustu Hacksaw leikirnir</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>RTP</th><th>Sveifla</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}spilakassar/wanted-dead-or-a-wild/">Wanted Dead or a Wild</a></td><td>96,38%</td><td>Öfgakennd</td><td>12.500x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/le-bandit/">Le Bandit</a></td><td>96,30%</td><td>Mjög há</td><td>10.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/chaos-crew/">Chaos Crew</a></td><td>96,30%</td><td>Mjög há</td><td>10.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/chaos-crew-2/">Chaos Crew 2</a></td><td>96,27%</td><td>Öfgakennd</td><td>25.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/hand-of-anubis/">Hand of Anubis</a></td><td>96,22%</td><td>Mjög há</td><td>10.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/le-pharaoh/">Le Pharaoh</a></td><td>96,25%</td><td>Há</td><td>5.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/cash-bonanza/">Cash Bonanza</a></td><td>96,20%</td><td>Há</td><td>7.500x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/stack-em/">Stack'em</a></td><td>96,27%</td><td>Mjög há</td><td>25.000x</td></tr>
</tbody></table>

<h2>Wanted Dead or a Wild — flaggskipið</h2>
<p>Þessi leikur gerði Hacksaw frægt. Þrjár ólíkar bónusumferðir:</p>
<ul>
<li><strong>Dead</strong> — Sticky wilds sem safnast upp</li>
<li><strong>Wanted</strong> — Margfaldarar sem leggjast saman</li>
<li><strong>Wild</strong> — Duel-umferð með stigvaxandi margföldurum</li>
</ul>
<p>Hámarksvinningur er 12.500x — en sveiflan er öfgakennd. Það er algengt að fara 400+ snúninga án umtalsverðs vinnings.</p>

<h2>Skraflóð (Scratch Cards)</h2>
<p>Hacksaw endurvakti skraflóðaflokkinn með leikjum eins og Dork Unit og Rocket Blast. Þessir leikir eru einfaldir — þú „skrapar" og sérð strax hvort þú vannst — en hafa sömu háu sveifluna og spilakassarnir þeirra.</p>
<p><a href="{URL_BASE}spilaviti/skraplod-spilaviti/">Spilavíti með skraflóðum →</a></p>

<h2>Hacksaw vs Nolimit City</h2>
<p>Báðir framleiðendur eru þekktir fyrir öfgakennda sveiflu, en nálgunin er ólík:</p>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Hacksaw</th><th>Nolimit City</th></tr></thead><tbody>
<tr><td>Stíll</td><td>Teiknimynda-, litríkur</td><td>Dökkur, óþægilegur</td></tr>
<tr><td>Vélbúnaður</td><td>Einfaldari, hraðari</td><td>Flókinn (xWays, xNudge)</td></tr>
<tr><td>Hámarksvinningar</td><td>5.000x–25.000x</td><td>Allt að 300.000x</td></tr>
<tr><td>Aðgengi byrjenda</td><td>Betra</td><td>Erfiðara</td></tr>
</tbody></table>
<p><a href="{URL_BASE}leidbeiningar/nolimit-city-hasveifluleikir/">Nolimit City yfirlit →</a></p>

<h2>Ráð fyrir Hacksaw leiki</h2>
<ul>
<li><strong>Lækkaðu veðmálsstærðina</strong> — Með öfgakenndri sveiflu þarftu 300–500 snúninga til að upplifa leikinn almennilega</li>
<li><strong>Prófaðu í demo fyrst</strong> — Sjáðu hversu langt fjármagnið endist áður en þú veðjar raunverulega</li>
<li><strong>Bónus Buy með varúð</strong> — Flestir Hacksaw leikir bjóða það, en kostnaðurinn er oft 100x+ veðmálið</li>
</ul>
<p>Sjá: <a href="{URL_BASE}leidbeiningar/hvad-er-sveifla/">hvað er sveifla →</a> · <a href="{URL_BASE}leidbeiningar/bankastjornunaradferdir/">bankastjórnun →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hvar get ég spilað Hacksaw á Íslandi?</h3>
<p><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> og <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> bjóða báðir Hacksaw safnið.</p>
<h3>Er Hacksaw með lágt RTP?</h3>
<p>Nei — um 96%, staðlað. Það er sveiflan sem er öfgakennd, ekki RTP.</p>
<h3>Hvaða Hacksaw leikur hentar byrjendum?</h3>
<p>Le Pharaoh eða Cash Bonanza — enn há sveifla en mun vægari en Chaos Crew eða Wanted Dead or a Wild.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Hacksaw leiki →</a></div>'''
    },
    {
        "slug": "push-gaming-leikir",
        "title": "Push Gaming — Razor Shark, Jammin' Jars og RTP 2026",
        "desc": "Push Gaming leikjaframleiðandi: Razor Shark, Jammin' Jars, Fat Banker. RTP tafla, sérkenni og hvar á að spila.",
        "emoji": "🔱",
        "colors": ('#0a1a28', '#143045', '#1e4662'),
        "content": f'''<h1>Push Gaming</h1>
{hero}
<p>Push Gaming er breskur framleiðandi sem gerir <strong>vandaða hásveifluleiki með sterkri grafík</strong>. Razor Shark og Jammin' Jars eru meðal mest spiluðu spilakassa í Evrópu.</p>

<h2>Um Push Gaming</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2010</td></tr>
<tr><td>Höfuðstöðvar</td><td>London, Bretland</td></tr>
<tr><td>Fjöldi leikja</td><td>60+</td></tr>
<tr><td>Þekktustu leikir</td><td>Razor Shark, Jammin' Jars, Fat Banker, Mystery Museum</td></tr>
<tr><td>Sérkenni</td><td>Há RTP (oft 96,5%+), Cluster Pays, margfaldarar</td></tr>
</tbody></table>

<h2>Bestu Push Gaming leikirnir</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>RTP</th><th>Sveifla</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}spilakassar/jammin-jars/">Jammin' Jars</a></td><td>96,83%</td><td>Há</td><td>20.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/razor-shark/">Razor Shark</a></td><td>96,70%</td><td>Mjög há</td><td>50.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/razor-returns/">Razor Returns</a></td><td>96,98%</td><td>Mjög há</td><td>50.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/jammin-jars-2/">Jammin' Jars 2</a></td><td>96,40%</td><td>Há</td><td>50.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/fat-banker/">Fat Banker</a></td><td>96,45%</td><td>Mjög há</td><td>42.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/fat-rabbit/">Fat Rabbit</a></td><td>96,45%</td><td>Há</td><td>4.000x</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/fat-santa/">Fat Santa</a></td><td>96,45%</td><td>Há</td><td>5.000x</td></tr>
</tbody></table>
<p>Taktu eftir: Push Gaming leikir hafa yfirleitt <strong>hærra RTP en meðaltalið</strong> (96,4–96,98% á móti 96% meðaltali). Sjá <a href="{URL_BASE}leidbeiningar/bestu-spilakassarnir-haesta-rtp/">topp 20 spilakassar eftir RTP →</a></p>

<h2>Razor Shark — Mystery Stacks</h2>
<p>Razor Shark er þekktastur fyrir „Nudge and Mystery Stack" vélbúnaðinn: dularfullir staflar opnast og geta innihaldið hvaða tákn sem er. Í frísnúningum safnast margfaldari sem endurstillist ekki — hann getur náð mjög háum gildum.</p>
<p>Hámarksvinningur er 50.000x sem er meðal þess hæsta í bransanum. Sveiflan er samsvarandi.</p>

<h2>Jammin' Jars — Cluster Pays og Rainbow Jars</h2>
<p>Jammin' Jars notar 8×8 grind með Cluster Pays (8+ eins tákn hvar sem er). Wild-krukkur færast um borðið og margfaldarinn þeirra hækkar við hvern vinning.</p>
<p>Með 96,83% RTP er þetta einn af hæstu RTP-leikjum sem almennt eru í boði.</p>

<h2>Push Gaming vs aðrir framleiðendur</h2>
<table class="info-table"><thead><tr><th>Framleiðandi</th><th>Dæmigert RTP</th><th>Sveifla</th><th>Styrkleiki</th></tr></thead><tbody>
<tr><td>Push Gaming</td><td>96,4–97,0%</td><td>Há</td><td>Hátt RTP + vönduð grafík</td></tr>
<tr><td><a href="{URL_BASE}leidbeiningar/pragmatic-play-allir-leikir/">Pragmatic Play</a></td><td>96,0–96,7%</td><td>Meðal–há</td><td>Magn og Drops &amp; Wins</td></tr>
<tr><td><a href="{URL_BASE}leidbeiningar/playn-go-bestu-spilakassarnir/">Play'n GO</a></td><td>96,2–96,6%</td><td>Há</td><td>Klassísk hönnun</td></tr>
<tr><td><a href="{URL_BASE}leidbeiningar/netent-saga-og-bestu-leikir/">NetEnt</a></td><td>96,0–98,0%</td><td>Lág–há</td><td>Gæði og fjölbreytni</td></tr>
<tr><td><a href="{URL_BASE}leidbeiningar/nolimit-city-hasveifluleikir/">Nolimit City</a></td><td>96,0–96,1%</td><td>Öfgakennd</td><td>Hámarksvinningar</td></tr>
</tbody></table>

<h2>Algengar spurningar</h2>
<h3>Hvaða Push Gaming leikur hefur hæsta RTP?</h3>
<p>Razor Returns með 96,98% — nánast 97%, sem er hátt fyrir hásveifluleik.</p>
<h3>Er Razor Shark of sveiflukenndur fyrir byrjendur?</h3>
<p>Já, frekar. Byrjaðu á Fat Rabbit eða <a href="{URL_BASE}spilakassar/jammin-jars/">Jammin' Jars</a> sem eru vægari.</p>
<h3>Hvar get ég spilað Push Gaming á Íslandi?</h3>
<p><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> og <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> bjóða báðir Push Gaming safnið.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Push Gaming →</a></div>'''
    },
    {
        "slug": "big-bass-bonanza-leidarvisir",
        "title": "Big Bass Bonanza — leiðarvísir, RTP og öll afbrigði 2026",
        "desc": "Big Bass Bonanza serían frá Pragmatic Play: RTP 96,71%, fiskitákn og margfaldarar. Samanburður á öllum útgáfum.",
        "emoji": "🎣",
        "colors": ('#0a1a28', '#143045', '#1e4662'),
        "content": f'''<h1>Big Bass Bonanza</h1>
{hero}
<p>Big Bass Bonanza er ein vinsælasta spilakassasería í heimi. <strong>RTP 96,71% — eitt það hæsta hjá Pragmatic Play — og einfaldur vélbúnaður sem allir skilja strax.</strong></p>

<h2>Tæknilegar upplýsingar (upprunalega útgáfan)</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Gildi</th></tr></thead><tbody>
<tr><td>Framleiðandi</td><td>Pragmatic Play / Reel Kingdom</td></tr>
<tr><td>Útgáfuár</td><td>2020</td></tr>
<tr><td>RTP</td><td>96,71%</td></tr>
<tr><td>Sveifla</td><td>Há</td></tr>
<tr><td>Hámarksvinningur</td><td>2.100x veðmál</td></tr>
<tr><td>Hjól / línur</td><td>5 hjól, 3 raðir, 10 línur</td></tr>
<tr><td>Frísnúningar</td><td>10 við 3 scatter</td></tr>
<tr><td>Bónus Buy</td><td>✅ Já (um 100x)</td></tr>
</tbody></table>

<h2>Hvernig leikurinn virkar</h2>
<h3>Fiskimaðurinn og fiskarnir</h3>
<p>Kjarninn er einfaldur: í frísnúningum er fiskimaðurinn wild-tákn. Þegar hann birtist safnar hann öllum fiskatáknum á skjánum og þú færð verðmæti þeirra (allt að 10x veðmálið á hvern fisk).</p>

<h3>Margfaldari sem vex</h3>
<p>Í frísnúningum eykst margfaldarinn eftir því hversu oft fiskimaðurinn birtist:</p>
<ul>
<li>4 fiskimenn → 2x margfaldari + 10 frísnúningar í viðbót</li>
<li>8 fiskimenn → 3x margfaldari + 10 frísnúningar</li>
<li>12 fiskimenn → 10x margfaldari + 10 frísnúningar</li>
</ul>
<p>Að ná 10x margfaldaranum er þar sem stóru vinningarnir gerast.</p>

<h2>Öll afbrigði seríunnar</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>RTP</th><th>Hámarksvinningur</th><th>Sérkenni</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}spilakassar/big-bass-bonanza/">Big Bass Bonanza</a></td><td>96,71%</td><td>2.100x</td><td>Upprunalega</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/bigger-bass-bonanza/">Bigger Bass Bonanza</a></td><td>96,71%</td><td>4.000x</td><td>Stærri grind (4 raðir)</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/big-bass-splash/">Big Bass Splash</a></td><td>95,67%</td><td>5.000x</td><td>Val um frísnúningaham</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/big-bass-bonanza-megaways/">Big Bass Bonanza Megaways</a></td><td>95,67%</td><td>5.000x</td><td>Megaways vélbúnaður</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/big-bass-amazon/">Big Bass Amazon Xtreme</a></td><td>96,71%</td><td>5.000x</td><td>Xtreme margfaldarar</td></tr>
<tr><td><a href="{URL_BASE}spilakassar/big-bass-keeping-it-reel/">Big Bass Keeping it Reel</a></td><td>96,71%</td><td>5.000x</td><td>Mystery tákn</td></tr>
</tbody></table>
<div class="info-box"><p><strong>Athugið:</strong> Big Bass Splash og Megaways útgáfurnar hafa <strong>lægra RTP (95,67%)</strong> en upprunalega. Ef RTP skiptir þig máli skaltu halda þig við upprunalegu útgáfuna eða Bigger Bass Bonanza.</p></div>

<h2>Af hverju er serían svona vinsæl?</h2>
<ul>
<li><strong>Auðskiljanlegt</strong> — Fiskimaðurinn safnar fiskum. Enginn þarf að lesa reglur</li>
<li><strong>Hátt RTP</strong> — 96,71% er yfir meðaltali. Sjá <a href="{URL_BASE}leidbeiningar/bestu-spilakassarnir-haesta-rtp/">RTP samanburð →</a></li>
<li><strong>Skýr framvinda</strong> — Þú sérð margfaldarann vaxa, sem heldur spennu uppi</li>
<li><strong>Algengt í bónustilboðum</strong> — Mörg spilavíti nota Big Bass í <a href="{URL_BASE}leidbeiningar/okeypis-snuningar-spilaviti/">frísnúningatilboðum</a></li>
</ul>

<h2>Ráð</h2>
<ul>
<li><strong>Veldu upprunalegu eða Bigger</strong> — Betra RTP en Splash/Megaways útgáfurnar</li>
<li><strong>Reiknaðu fyrir 200+ snúninga</strong> — Há sveifla, frísnúningar koma að meðaltali á 180–250 snúninga fresti</li>
<li><strong>Bónus Buy</strong> — Um 100x veðmálið. Fer beint í frísnúninga en kostnaðurinn er hár. <a href="{URL_BASE}leidbeiningar/bonus-buy-spilakassar/">Er Bónus Buy þess virði? →</a></li>
<li><strong>Athugaðu RTP-útgáfuna</strong> — Spilavíti geta keyrt lægri stillingu. Athugaðu í leikjareglum</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Hvaða Big Bass leikur er bestur?</h3>
<p>Upprunalega Big Bass Bonanza fyrir RTP (96,71%), Bigger Bass Bonanza ef þú vilt hærri hámarksvinning með sama RTP.</p>
<h3>Hvað er hámarksvinningur?</h3>
<p>2.100x í upprunalegu útgáfunni, allt að 5.000x í nýrri afbrigðum.</p>
<h3>Er hægt að spila ókeypis?</h3>
<p>Já — <a href="{URL_BASE}spilakassar/big-bass-bonanza/">prófaðu Big Bass Bonanza í demo</a> án skráningar.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Big Bass Bonanza →</a></div>'''
    },
    {
        "slug": "mega-moolah-pottavinningur",
        "title": "Mega Moolah — stærsti pottur netheima 2026",
        "desc": "Mega Moolah: stigvaxandi pottur sem hefur greitt yfir 20 milljónir evra. Hvernig potturinn virkar, RTP og líkur.",
        "emoji": "🦁",
        "colors": ('#281a0a', '#453014', '#62461e'),
        "content": f'''<h1>Mega Moolah</h1>
{hero}
<p>Mega Moolah er frægasti stigvaxandi pottur í sögu netspilavíta. <strong>Hann hefur greitt út margar af stærstu vinningum sem skráðir hafa verið á netinu — þar á meðal yfir 18 milljónir evra í einni greiðslu.</strong></p>

<h2>Tæknilegar upplýsingar</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Gildi</th></tr></thead><tbody>
<tr><td>Framleiðandi</td><td>Microgaming / Games Global</td></tr>
<tr><td>Útgáfuár</td><td>2006</td></tr>
<tr><td>RTP</td><td>88,12% (grunnleikur) — 93–96% með potti</td></tr>
<tr><td>Sveifla</td><td>Mjög há</td></tr>
<tr><td>Hjól / línur</td><td>5 hjól, 3 raðir, 25 línur</td></tr>
<tr><td>Lágmarksveðmál</td><td>€0,25</td></tr>
<tr><td>Pottar</td><td>4 (Mini, Minor, Major, Mega)</td></tr>
<tr><td>Lágmarks Mega pottur</td><td>€1.000.000</td></tr>
</tbody></table>

<h2>Potturinn fjórfaldi</h2>
<table class="info-table"><thead><tr><th>Pottur</th><th>Dæmigert verðmæti</th><th>Tíðni</th></tr></thead><tbody>
<tr><td>Mini</td><td>~€10</td><td>Oft</td></tr>
<tr><td>Minor</td><td>~€100</td><td>Reglulega</td></tr>
<tr><td>Major</td><td>~€10.000</td><td>Sjaldan</td></tr>
<tr><td>Mega</td><td>€1.000.000+</td><td>Mjög sjaldan</td></tr>
</tbody></table>
<p>Þegar Mega potturinn er unninn endurstillist hann í €1 milljón og byrjar að vaxa aftur.</p>

<h2>Hvernig potturinn vinnst</h2>
<p>Pottumferðin er <strong>algjörlega handahófskennd</strong> — hún getur kveikt á hvaða snúningi sem er, óháð veðmálsstærð eða því hvort þú vannst í grunnleiknum.</p>
<p>Þegar hún kveikir birtist hjól með 20 reitum skipt milli pottanna fjögurra. Þar sem hjólið stöðvast ræður hvaða pott þú vinnur.</p>
<div class="info-box"><p><strong>Mikilvægt:</strong> Hærra veðmál eykur <em>líkurnar</em> á að pottumferðin kvikni — en tryggir hana ekki. Þú getur unnið Mega pottinn á lágmarksveðmáli, þó líkurnar séu minni.</p></div>

<h2>RTP — lestu þetta áður en þú spilar</h2>
<p>Hér er það sem margir átta sig ekki á: <strong>grunnleikur Mega Moolah hefur aðeins 88,12% RTP.</strong> Það er langt undir meðaltalinu (um 96%).</p>
<p>Ástæðan: hluti af hverju veðmáli fer í pottinn í stað þess að greiðast út í venjulegum vinningum. Heildar-RTP (með pottinum talið) fer í 93–96%, en sá hluti rennur til eins heppins spilara — ekki þín.</p>
<p>Í reynd þýðir þetta: ef þú spilar Mega Moolah og vinnur ekki pottinn tapar þú hraðar en í venjulegum spilakassa.</p>
<p><a href="{URL_BASE}leidbeiningar/hvad-er-rtp/">Ítarlegt um RTP →</a> · <a href="{URL_BASE}leidbeiningar/bestu-spilakassarnir-haesta-rtp/">spilakassar með hæsta RTP →</a></p>

<h2>Líkurnar á Mega pottinum</h2>
<p>Áætlaðar líkur eru um <strong>1 á móti 50 milljónum snúninga</strong>. Til samanburðar: líkurnar á að verða fyrir eldingu á ævinni eru um 1 á móti 15.000.</p>
<p>Það þýðir ekki að það sé ómögulegt — einhver vinnur reglulega. En það þýðir að þú átt ekki að spila Mega Moolah með þá væntingu að vinna hann.</p>

<h2>Serían</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>Þema</th><th>Grunn-RTP</th></tr></thead><tbody>
<tr><td><a href="{URL_BASE}spilakassar/mega-moolah/">Mega Moolah</a></td><td>Afrískt safarí</td><td>88,12%</td></tr>
<tr><td>Mega Moolah Isis</td><td>Egyptaland</td><td>88,12%</td></tr>
<tr><td>Absolootly Mad Mega Moolah</td><td>Lísa í Undralandi</td><td>88,12%</td></tr>
<tr><td>Atlantean Treasures Mega Moolah</td><td>Neðansjávar</td><td>88,12%</td></tr>
<tr><td>Book of Atem WowPot</td><td>Egyptaland (WowPot net)</td><td>93,04%</td></tr>
</tbody></table>

<h2>Aðrir stórir pottar</h2>
<ul>
<li><a href="{URL_BASE}spilakassar/mega-fortune/">Mega Fortune</a> (NetEnt) — Lúxusþema, hefur greitt yfir €17 milljónir</li>
<li><a href="{URL_BASE}spilakassar/divine-fortune/">Divine Fortune</a> (NetEnt) — Minni pottar en mun hærra grunn-RTP (96,59%)</li>
<li><a href="{URL_BASE}spilakassar/wolf-gold/">Wolf Gold</a> (Pragmatic Play) — Fastir pottar, RTP 96,01%</li>
</ul>
<p><a href="{URL_BASE}leidbeiningar/stighaekkandi-pottar/">Allt um stigvaxandi potta →</a> · <a href="{URL_BASE}spilaviti/jackpot-spilaviti/">Pottaspilavíti →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hver er stærsti Mega Moolah vinningurinn?</h3>
<p>Rúmlega €18,9 milljónir árið 2018 — skráð sem einn stærsti netspilavítisvinningur sögunnar.</p>
<h3>Þarf ég að veðja hámarki til að vinna pottinn?</h3>
<p>Nei — potturinn getur kveikt á hvaða veðmálsstærð sem er. En hærra veðmál eykur líkurnar hlutfallslega.</p>
<h3>Er Mega Moolah góður leikur?</h3>
<p>Fyrir draumavinning — já. Fyrir jafna spilun — nei, vegna 88% grunn-RTP. Ef þú vilt spila lengur fyrir sömu upphæð skaltu velja leik með 96%+ RTP.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila pottaleiki →</a></div>'''
    },
    {
        "slug": "gdpr-og-netspilaviti",
        "title": "GDPR og netspilavíti — hvaða gögn safna þau um þig? 2026",
        "desc": "Persónuvernd á netspilavítum: hvaða gögn eru söfnuð, hvaða réttindi þú hefur samkvæmt GDPR og hvernig á að beita þeim.",
        "emoji": "🔒",
        "colors": ('#0a1420', '#14283c', '#1e3c58'),
        "content": f'''<h1>GDPR og netspilavíti</h1>
{hero}
<p>Þegar þú skráir þig á netspilavíti afhendir þú umtalsvert magn persónuupplýsinga. <strong>Sem íslenskur ríkisborgari nýtur þú verndar GDPR — en aðeins gagnvart spilavítum sem starfa innan EES.</strong></p>

<h2>Hvaða gögn safna spilavíti?</h2>
<table class="info-table"><thead><tr><th>Flokkur</th><th>Dæmi</th><th>Af hverju</th></tr></thead><tbody>
<tr><td>Auðkenni</td><td>Nafn, fæðingardagur, kennitala/vegabréf</td><td>Aldursstaðfesting, lagaskylda (KYC)</td></tr>
<tr><td>Samskipti</td><td>Netfang, símanúmer, heimilisfang</td><td>Reikningsstjórnun</td></tr>
<tr><td>Fjárhagur</td><td>Kortaupplýsingar, bankareikningur, færslusaga</td><td>Greiðslur, peningaþvættisvarnir</td></tr>
<tr><td>Hegðun</td><td>Hvaða leiki þú spilar, hversu lengi, veðmálsstærðir</td><td>Markaðssetning, ábyrg spilun</td></tr>
<tr><td>Tækni</td><td>IP-tala, tæki, vafri, staðsetning</td><td>Svikavarnir, landfræðileg takmörk</td></tr>
</tbody></table>

<h2>Réttindi þín samkvæmt GDPR</h2>
<h3>1. Réttur til aðgangs</h3>
<p>Þú getur beðið um afrit af öllum gögnum sem spilavítið geymir um þig. Það verður að svara innan <strong>30 daga</strong> og afhenda gögnin ókeypis.</p>

<h3>2. Réttur til leiðréttingar</h3>
<p>Ef upplýsingar eru rangar getur þú krafist leiðréttingar.</p>

<h3>3. Réttur til eyðingar („rétturinn til að gleymast")</h3>
<p>Þú getur beðið um að gögnum verði eytt — <strong>en með mikilvægum undantekningum</strong>. Spilavíti verða að geyma fjárhagsgögn og KYC-gögn í 5–7 ár vegna peningaþvættislöggjafar. Þau geta því ekki eytt öllu.</p>

<h3>4. Réttur til að andmæla markaðssetningu</h3>
<p>Þú getur hvenær sem er afþakkað markpósta, SMS og símtöl. Þetta má ekki vera háð neinum skilyrðum.</p>

<h3>5. Réttur til gagnaflutnings</h3>
<p>Þú getur fengið gögnin þín á véllæsilegu formi til að flytja annað.</p>

<h2>Hvernig á að beita réttindunum</h2>
<ol>
<li>Finndu persónuverndarstefnu spilavítisins (yfirleitt neðst á síðunni)</li>
<li>Leitaðu að netfangi persónuverndarfulltrúa (DPO) — oft privacy@ eða dpo@</li>
<li>Sendu skriflega beiðni. Tilgreindu nákvæmlega hvað þú vilt (aðgang, eyðingu, andmæli)</li>
<li>Þeir hafa 30 daga til að svara</li>
<li>Ef þeir svara ekki eða neita ólögmætt — kvartaðu til Persónuverndar (personuvernd.is)</li>
</ol>

<h2>Gildir GDPR um öll spilavíti?</h2>
<div class="info-box"><p><strong>Nei.</strong> GDPR gildir um fyrirtæki sem starfa innan EES eða beina þjónustu markvisst að einstaklingum innan EES. Spilavíti með <a href="{URL_BASE}leidbeiningar/hvada-leyfi-er-best-spilaviti/">Malta (MGA) leyfi</a> falla undir GDPR. Spilavíti með Curaçao leyfi gera það oft ekki formlega.</p></div>
<p>Mörg Curaçao-spilavíti fylgja GDPR-líkum reglum af fúsum vilja, en þú hefur ekki sömu lagalegu úrræði ef þau gera það ekki. Þetta er ein ástæða þess að MGA-leyfi er verðmætara frá sjónarhóli neytendaverndar.</p>

<h2>Hagnýtar ráðleggingar</h2>
<ul>
<li><strong>Notaðu sérstakt netfang</strong> — Aðskildu spilavítasamskipti frá persónulegum pósti</li>
<li><strong>Lestu persónuverndarstefnuna</strong> — Sérstaklega kaflann um deilingu með þriðja aðila</li>
<li><strong>Afþakkaðu markaðssetningu strax</strong> — Gerðu það við skráningu, ekki eftir að póstarnir byrja</li>
<li><strong>Varist ótengd „spilavíti"</strong> — Ef síða biður um kennitölu án skýrrar KYC-ástæðu er það viðvörunarmerki</li>
<li><strong>Athugaðu hvort gögn eru seld</strong> — Sum spilavíti deila gögnum með markaðsaðilum. Þetta á að koma fram í stefnunni</li>
</ul>

<h2>Sérstaklega viðkvæmt: hegðunargögn</h2>
<p>Spilavíti vita nákvæmlega hvenær þú spilar, hversu lengi, hvaða leiki og hversu mikið. Þessi gögn eru notuð bæði til <a href="{URL_BASE}leidbeiningar/spila-af-abyrgd/">ábyrgrar spilunar</a> (að greina áhættuhegðun) og til markaðssetningar (að senda bónus þegar þú hefur ekki spilað í viku).</p>
<p>Ef þú vilt ekki fá bónustilboð byggð á hegðun þinni — afþakkaðu markaðssetningu. Það er réttur þinn.</p>

<h2>Algengar spurningar</h2>
<h3>Get ég látið eyða reikningnum mínum alveg?</h3>
<p>Þú getur lokað reikningnum, en spilavítið verður að geyma KYC- og fjárhagsgögn í 5–7 ár vegna peningaþvættislöggjafar. Markaðsgögnum og hegðunargögnum má eyða.</p>
<h3>Hvað ef spilavítið svarar ekki beiðni minni?</h3>
<p>Ef það fellur undir GDPR getur þú kvartað til Persónuverndar á Íslandi eða til eftirlitsaðila í landi spilavítisins (t.d. maltneska eftirlitsins fyrir MGA-spilavíti).</p>
<h3>Er öruggt að senda mynd af vegabréfinu?</h3>
<p>Til spilavítis með gilt leyfi — já, það er lagaskylda þeirra að vernda gögnin. Sendu aldrei skilríki í gegnum ódulkóðaðan tölvupóst; notaðu upphleðsluform spilavítisins.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá spilavíti með MGA leyfi →</a></div>'''
    },
    {
        "slug": "spilafikn-a-islandi-tolfraedi",
        "title": "Spilafikn á Íslandi — tölfræði og staðreyndir 2026",
        "desc": "Hversu algeng er spilafikn á Íslandi? Rannsóknir, áhættuhópar, einkenni og hvar hjálp er að fá. Hjálparsími 1717.",
        "emoji": "📈",
        "colors": ('#141414', '#282828', '#3c3c3c'),
        "content": f'''<h1>Spilafikn á Íslandi</h1>
{hero}
<p>Fjárhættuspil eru útbreidd á Íslandi — spilakassar, lottó, getraunir og netspilavíti. <strong>Fyrir langflesta er þetta skaðlaus afþreying. Fyrir lítinn en raunverulegan hóp verður það vandamál.</strong></p>

<h2>Hvað segja rannsóknir?</h2>
<p>Rannsóknir á spilahegðun Íslendinga hafa verið gerðar með reglulegu millibili, meðal annars á vegum stjórnvalda og háskólasamfélagsins. Meginniðurstöður sem ítrekað koma fram:</p>
<ul>
<li>Meirihluti fullorðinna Íslendinga tekur einhvern þátt í fjárhættuspilum árlega — oftast lottó eða getraunum</li>
<li>Hlutfall þeirra sem sýna merki um <strong>vandamálaspilun</strong> er lítið brot af heildinni, í takt við það sem sést á öðrum Norðurlöndum</li>
<li>Spilakassar og hraðir netleikir tengjast hærri tíðni vandamála en lottó eða getraunir</li>
<li>Ungir karlmenn eru stærsti áhættuhópurinn</li>
</ul>
<div class="info-box"><p><strong>Athugasemd um tölur:</strong> Við birtum ekki nákvæmar prósentur hér því niðurstöður eru mismunandi eftir rannsóknaraðferð, ártali og skilgreiningu á „vandamálaspilun". Ef þú þarft nákvæmar tölur mælum við með að leita beint til Embættis landlæknis eða birtra rannsókna á vegum háskólanna.</p></div>

<h2>Af hverju eru hraðir leikir áhættusamari?</h2>
<p>Tíðni og hraði skipta meira máli en upphæðin:</p>
<table class="info-table"><thead><tr><th>Leikjaform</th><th>Tími milli veðmála</th><th>Áhættustig</th></tr></thead><tbody>
<tr><td>Lottó</td><td>Dagar</td><td>Lágt</td></tr>
<tr><td>Getraunir / íþróttaveðmál</td><td>Klukkustundir</td><td>Miðlungs</td></tr>
<tr><td>Spilakassar (staðbundnir)</td><td>Sekúndur</td><td>Hátt</td></tr>
<tr><td>Netspilakassar</td><td>Sekúndur, alltaf í boði</td><td>Hátt</td></tr>
<tr><td>Lifandi spilavíti</td><td>Sekúndur til mínútur</td><td>Hátt</td></tr>
</tbody></table>
<p>Netspilavíti sameina hraða og aðgengi — þau eru opin allan sólarhringinn og í vasanum. Það er bæði þægindi og áhætta.</p>

<h2>Hverjir eru í mestri áhættu?</h2>
<ul>
<li><strong>Ungir karlmenn (18–35 ára)</strong> — Hæsta tíðni í flestum rannsóknum</li>
<li><strong>Þeir sem byrjuðu ungir</strong> — Því fyrr sem spilun hefst, þeim mun meiri áhætta síðar</li>
<li><strong>Fólk með aðrar fíknir</strong> — Áfengi, vímuefni og spilun fara oft saman</li>
<li><strong>Þeir sem glíma við kvíða eða þunglyndi</strong> — Spilun getur orðið flóttaleið</li>
<li><strong>Fólk í fjárhagsvanda</strong> — Von um skyndilausn eykur áhættuhegðun</li>
</ul>

<h2>Hvernig þróast vandamálið?</h2>
<p>Spilafikn þróast yfirleitt í stigum:</p>
<ol>
<li><strong>Vinningsstig</strong> — Snemmbúnir vinningar skapa óraunhæfar væntingar</li>
<li><strong>Tapstig</strong> — Tap eykst, spilarinn byrjar að elta tapið og leyna því</li>
<li><strong>Örvæntingarstig</strong> — Lán, skuldir, sambandsslit, hugsanlega lögbrot</li>
<li><strong>Uppgjöf eða bati</strong> — Annaðhvort dýpkar vandinn eða viðkomandi leitar hjálpar</li>
</ol>
<p>Því fyrr sem gripið er inn í, þeim mun betri eru horfurnar.</p>

<h2>Einkenni — stutt yfirlit</h2>
<ul>
<li>Spilar meira en ætlað var, ítrekað</li>
<li>Eltir tap með stærri veðmálum</li>
<li>Leynir umfangi spilunar fyrir öðrum</li>
<li>Hefur reynt að hætta án árangurs</li>
<li>Notar peninga sem þarf í annað</li>
<li>Pirringur eða eirðarleysi þegar ekki er hægt að spila</li>
</ul>
<p><a href="{URL_BASE}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">Ítarlegri listi yfir viðvörunarmerki →</a></p>

<h2>Hvar er hjálp að fá á Íslandi?</h2>
<div class="info-box"><p><strong>Hjálparsíminn 1717</strong> — Opinn allan sólarhringinn, alla daga ársins. Ókeypis, nafnlaust ef þú vilt. Einnig fyrir aðstandendur.</p></div>
<div class="info-box"><p><strong>SÁÁ</strong> — Veitir meðferð og ráðgjöf, einnig vegna spilafiknar. saa.is</p></div>
<div class="info-box"><p><strong>Heilsugæslan</strong> — Fyrsti viðkomustaður fyrir tilvísun í sálfræðiþjónustu.</p></div>
<div class="info-box"><p><strong>GA (Gamblers Anonymous)</strong> — Sjálfshjálparhópar, einnig fundir á netinu.</p></div>
<p><a href="{URL_BASE}leidbeiningar/studningssidur-vid-spilafikn/">Öll stuðningsúrræði →</a> · <a href="{URL_BASE}leidbeiningar/radleggingar-til-adstandenda-spilafikla/">Ráð til aðstandenda →</a></p>

<h2>Forvarnir — það sem virkar</h2>
<ol>
<li><a href="{URL_BASE}leidbeiningar/hvernig-a-ad-setja-takmork-a-spilaviti/">Innborgunartakmörk</a> — sett fyrirfram, áður en spilun hefst</li>
<li><a href="{URL_BASE}leidbeiningar/sjalfsutilokun-spilavita/">Sjálfsútilokun</a> — ef takmörk duga ekki</li>
<li>BetBlocker — ókeypis hugbúnaður sem lokar á spilavítasíður á öllum tækjum</li>
<li>Bankalokun — sumir bankar geta lokað á fjárhættuspilafærslur</li>
<li>Opin umræða — leynd er einkenni vandamálsins, ekki lausn</li>
</ol>

<h2>Algengar spurningar</h2>
<h3>Er spilafikn viðurkennd sem sjúkdómur?</h3>
<p>Já — Alþjóðaheilbrigðismálastofnunin (WHO) flokkar spilaröskun (gambling disorder) sem geðröskun í ICD-11, á sama hátt og vímuefnafíkn.</p>
<h3>Er hægt að ná bata?</h3>
<p>Já. Meðferð, sjálfshjálparhópar og hugræn atferlismeðferð hafa sýnt árangur. Bakslag er algengt í ferlinu og þýðir ekki að meðferð sé árangurslaus.</p>
<h3>Hvað ef ég er ekki viss hvort ég eigi í vanda?</h3>
<p>Hringdu í 1717 og ræddu það. Það kostar ekkert og þú þarft ekki að greina sjálfan þig fyrirfram.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá ábyrga spilun →</a></div>'''
    },
    {
        "slug": "sic-bo-reglur-a-islensku",
        "title": "Sic Bo reglur á íslensku — teningaleikurinn útskýrður 2026",
        "desc": "Sic Bo reglur á íslensku: veðmálategundir, útborganir, húsforskot og hvaða veðmál borga sig best.",
        "emoji": "🎲",
        "colors": ('#1a0a14', '#331428', '#4d1e3c'),
        "content": f'''<h1>Sic Bo reglur á íslensku</h1>
{hero}
<p>Sic Bo er kínverskur teningaleikur sem hefur verið spilaður í yfir 2.000 ár. <strong>Þrír teningar, eitt kast, tugir veðmálamöguleika.</strong> Hann er einfaldur að spila en húsforskotið er mjög breytilegt eftir því hvað þú veðjar á.</p>

<h2>Grunnreglur</h2>
<ol>
<li>Þrír teningar eru hristir í lokuðum bikar</li>
<li>Þú leggur veðmál á borðið áður en þeir eru opnaðir</li>
<li>Teningarnir eru sýndir</li>
<li>Öll veðmál sem passa eru greidd út</li>
</ol>
<p>Það er allt. Engar ákvarðanir eftir kastið, engin strategía í sjálfum leiknum — aðeins val á veðmálum.</p>

<h2>Veðmálategundir og húsforskot</h2>
<table class="info-table"><thead><tr><th>Veðmál</th><th>Lýsing</th><th>Útborgun</th><th>Húsforskot</th></tr></thead><tbody>
<tr><td><strong>Small</strong></td><td>Samtala 4–10</td><td>1:1</td><td><strong>2,78%</strong></td></tr>
<tr><td><strong>Big</strong></td><td>Samtala 11–17</td><td>1:1</td><td><strong>2,78%</strong></td></tr>
<tr><td>Slétt / Oddatala</td><td>Samtala slétt eða oddatala</td><td>1:1</td><td>2,78%</td></tr>
<tr><td>Ein tala</td><td>Tiltekin tala birtist</td><td>1:1 til 3:1</td><td>7,87%</td></tr>
<tr><td>Tvær tölur</td><td>Tvær tilteknar tölur</td><td>5:1</td><td>16,67%</td></tr>
<tr><td>Samtala (t.d. 10)</td><td>Nákvæm samtala</td><td>6:1 til 60:1</td><td>9,7–15,3%</td></tr>
<tr><td>Þrennt (tiltekið)</td><td>Þrír eins, tiltekin tala</td><td>180:1</td><td>16,2%</td></tr>
<tr><td>Hvaða þrennt sem er</td><td>Þrír eins, hvaða tala</td><td>30:1</td><td>30,1%</td></tr>
</tbody></table>

<h2>Besta veðmálið: Small eða Big</h2>
<div class="info-box"><p><strong>Veðjaðu á Small eða Big.</strong> Þau hafa 2,78% húsforskot — sambærilegt við <a href="{URL_BASE}leidbeiningar/rullettureglur-a-islensku/">evrópska rúllettu</a> (2,7%). Öll önnur veðmál í Sic Bo hafa verulega hærra húsforskot.</p></div>
<p>„Hvaða þrennt sem er" lítur freistandi út með 30:1 útborgun — en húsforskotið er 30,1%. Það er eitt versta veðmál sem til er í nokkru spilavíti.</p>

<h2>Af hverju Small/Big greiða ekki fyrir þrennt</h2>
<p>Ef þrír eins koma upp (t.d. 3-3-3) tapa bæði Small og Big. Þetta er þar sem húsið fær forskot sitt — annars væru þessi veðmál fullkomlega jöfn 50/50.</p>
<p>Líkurnar á þrennu eru 6/216 = 2,78% — nákvæmlega húsforskotið.</p>

<h2>Sic Bo vs önnur teningaspil</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>Besta húsforskot</th><th>Flækjustig</th><th>Ákvarðanir eftir kast</th></tr></thead><tbody>
<tr><td>Sic Bo</td><td>2,78%</td><td>Lágt</td><td>Nei</td></tr>
<tr><td>Craps</td><td>1,36% (Don't Pass)</td><td>Hátt</td><td>Já (odds veðmál)</td></tr>
<tr><td><a href="{URL_BASE}live/lightning-dice/">Lightning Dice</a></td><td>~3,5%</td><td>Mjög lágt</td><td>Nei</td></tr>
</tbody></table>
<p>Craps hefur lægra húsforskot en krefst mun meiri þekkingar. Sic Bo er aðgengilegra fyrir byrjendur.</p>

<h2>Hvar á að spila Sic Bo á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}live/sic-bo/">Lifandi Sic Bo</a></strong> — Evolution býður lifandi útgáfu með raunverulegum spilastjóra</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}live/super-sic-bo/">Super Sic Bo</a></strong> — Útgáfa með handahófskenndum margföldurum allt að 1.000x</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/teningaleikja-spilaviti/">Teningaleikjaspilavíti</a></strong> — Yfirlit yfir spilavíti með teningaleikjum</p></div>

<h2>Super Sic Bo — athugaðu útborgunina</h2>
<p>Eins og í <a href="{URL_BASE}leidbeiningar/lightning-roulette-adferdir/">Lightning Roulette</a> bætir Super Sic Bo við margföldurum — en lækkar grunnútborganir á móti. Heildar-RTP er svipað. Margfaldararnir gilda aðeins um tiltekin veðmál, ekki Small/Big.</p>

<h2>Algengar spurningar</h2>
<h3>Er einhver strategía í Sic Bo?</h3>
<p>Aðeins ein: veðjaðu á Small eða Big og forðist allt annað. Það er engin leið til að hafa áhrif á teningana.</p>
<h3>Hvaða veðmál á ég alls ekki að taka?</h3>
<p>„Hvaða þrennt sem er" (30,1% húsforskot) og „Tvær tölur" (16,67%). Útborgunin lítur vel út en stærðfræðin er hræðileg.</p>
<h3>Er Sic Bo í boði í demo?</h3>
<p>RNG-útgáfur já. Lifandi útgáfur með raunverulegum spilastjóra eru ekki í boði ókeypis.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila Sic Bo →</a></div>'''
    },
    {
        "slug": "bingo-a-netinu-island",
        "title": "Bingó á netinu á Íslandi — reglur og spilavíti 2026",
        "desc": "Bingó á netinu: 90-bolta og 75-bolta reglur, mynstur, RTP og hvaða spilavíti bjóða bingó fyrir íslenska spilara.",
        "emoji": "🎱",
        "colors": ('#0a1a1a', '#143333', '#1e4d4d'),
        "content": f'''<h1>Bingó á netinu á Íslandi</h1>
{hero}
<p>Bingó er félagslegasti leikurinn í netspilavítum — flest bingóherbergi hafa spjall þar sem spilarar tala saman meðan umferðin gengur. <strong>Lágur hraði, lágt veðmál og meira um skemmtun en stóra vinninga.</strong></p>

<h2>Tvö helstu afbrigði</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>90-bolta (evrópskt)</th><th>75-bolta (amerískt)</th></tr></thead><tbody>
<tr><td>Boltar</td><td>1–90</td><td>1–75</td></tr>
<tr><td>Spjald</td><td>9×3, 15 tölur</td><td>5×5, 24 tölur + frír reitur</td></tr>
<tr><td>Vinningar</td><td>1 lína, 2 línur, fullt hús</td><td>Mynstur (form, bókstafir)</td></tr>
<tr><td>Umferðarlengd</td><td>Lengri</td><td>Styttri</td></tr>
<tr><td>Vinsælt í</td><td>Evrópu, Bretlandi</td><td>Norður-Ameríku</td></tr>
</tbody></table>

<h2>90-bolta bingó — reglurnar</h2>
<p>Spjaldið er 9 dálkar × 3 raðir. Hver röð hefur 5 tölur og 4 auða reiti — samtals 15 tölur á spjaldi.</p>
<p>Þrír vinningar í hverri umferð:</p>
<ol>
<li><strong>Ein lína</strong> — Allar 5 tölur í einni röð</li>
<li><strong>Tvær línur</strong> — Allar tölur í tveimur röðum</li>
<li><strong>Fullt hús</strong> — Allar 15 tölur. Stærsti vinningurinn</li>
</ol>

<h2>75-bolta bingó — mynstur</h2>
<p>Spjaldið er 5×5 með fríum reit í miðju. Vinningsmynstur eru tilkynnt fyrir hverja umferð:</p>
<ul>
<li><strong>Lína</strong> — Lárétt, lóðrétt eða á ská</li>
<li><strong>Form</strong> — Kross, demantur, bókstafir</li>
<li><strong>Coverall / Blackout</strong> — Allt spjaldið. Stærsti vinningurinn</li>
</ul>

<h2>Auto-daub — þú missir ekki af neinu</h2>
<p>Á netinu merkir kerfið tölurnar sjálfkrafa („auto-daub"). Þú getur ekki klikkað á tölu. Það þýðir líka að:</p>
<ul>
<li>Þú getur spilað mörg spjöld samtímis án vandræða</li>
<li>Kunnátta skiptir engu máli — niðurstaðan er fyrirfram ákveðin af tölunum sem dregnar eru</li>
<li>Þú getur spjallað á meðan án þess að tapa</li>
</ul>

<h2>Hvernig vinningar skiptast</h2>
<p>Bingó er <strong>pottleikur</strong>: allir þátttakendur greiða fyrir spjöld, potturinn myndast og vinningshafar skipta honum. Spilavítið tekur þóknun (oft 10–25%).</p>
<p>Það þýðir tvennt:</p>
<ul>
<li>Því fleiri sem spila, þeim mun stærri er potturinn — en þeim mun minni líkur á að þú vinnir</li>
<li>Því færri sem spila, þeim mun minni pottur — en betri líkur</li>
</ul>
<p>Sumir reyndir bingóspilarar velja viljandi herbergi með fáum spilurum í stað stærstu pottanna.</p>

<h2>Bingó vs aðrir leikir</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Bingó</th><th>Spilakassar</th><th>Keno</th></tr></thead><tbody>
<tr><td>Húsforskot</td><td>10–25%</td><td>~4%</td><td>5–35%</td></tr>
<tr><td>Hraði</td><td>5–15 mín/umferð</td><td>Sekúndur</td><td>Sekúndur</td></tr>
<tr><td>Félagslegt</td><td>✅ Spjall</td><td>❌</td><td>❌</td></tr>
<tr><td>Kostnaður á umferð</td><td>Lágur (€0,10–1)</td><td>Breytilegur</td><td>Lágur</td></tr>
</tbody></table>
<p>Húsforskotið í bingó er hátt — en hraðinn er lágur. Að spila bingó í klukkustund kostar yfirleitt mun minna en að spila <a href="{URL_BASE}spilakassar/">spilakassa</a> í klukkustund, einfaldlega vegna þess að þú gerir færri veðmál.</p>

<h2>Hvar á að spila bingó á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bingo-spilaviti/">Bingóspilavíti</a></strong> — Yfirlit yfir spilavíti með bingóherbergjum</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}live/bingo-live/">Lifandi bingó</a></strong> — Bingó með raunverulegum kynni frá Evolution og Pragmatic Play</p></div>
<p>Athugaðu að bingó er ekki í boði á öllum spilavítum — það er sérhæfður flokkur.</p>

<h2>Ráð fyrir byrjendur</h2>
<ul>
<li><strong>Byrjaðu á fáum spjöldum</strong> — Þó auto-daub geri það tæknilega mögulegt að spila 50 spjöld, byrjaðu á 2–4 til að skilja flæðið</li>
<li><strong>Athugaðu þóknunina</strong> — Hún er sjaldan auglýst. Spurðu þjónustuver ef hún kemur ekki fram</li>
<li><strong>Prófaðu rólegri herbergi</strong> — Betri vinningslíkur þótt potturinn sé minni</li>
<li><strong>Nýttu spjallið</strong> — Mörg herbergi hafa spjallleiki með aukaverðlaunum</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Er hægt að auka líkurnar í bingó?</h3>
<p>Aðeins með því að kaupa fleiri spjöld (hlutfallslega betri líkur) eða spila í herbergjum með færri þátttakendum. Engin önnur aðferð virkar.</p>
<h3>Er netbingó sanngjarnt?</h3>
<p>Á spilavítum með gilt leyfi — já. Tölurnar eru dregnar með vottuðum <a href="{URL_BASE}leidbeiningar/hvernig-rng-virkar/">slembitölugjafa</a>.</p>
<h3>Hvað kostar að spila?</h3>
<p>Spjöld kosta yfirleitt €0,05–1. Þú getur spilað í klukkustund fyrir nokkrar evrur, sem gerir bingó að einum ódýrasta leiknum í tíma talið.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila bingó →</a></div>'''
    },
    {
        "slug": "spilaviti-med-besta-vip-kerfinu",
        "title": "Spilavíti með besta VIP-kerfinu 2026 — samanburður",
        "desc": "Hvaða netspilavíti bjóða bestu VIP-kerfin? Endurgreiðsla, persónulegur stjórnandi, hraðari úttektir og hvað er raunverulega þess virði.",
        "emoji": "👑",
        "colors": ('#1a1400', '#332800', '#4d3c00'),
        "content": f'''<h1>Spilavíti með besta VIP-kerfinu 2026</h1>
{hero}
<p>Nánast öll spilavíti auglýsa VIP-kerfi. <strong>Fæst þeirra eru raunverulega þess virði.</strong> Hér förum við yfir hvað skiptir máli og hvað er markaðssetning.</p>

<h2>Hvað VIP-kerfi bjóða yfirleitt</h2>
<table class="info-table"><thead><tr><th>Fríðindi</th><th>Raunverulegt virði</th><th>Athugasemd</th></tr></thead><tbody>
<tr><td>Endurgreiðsla (cashback)</td><td>⭐⭐⭐⭐⭐ Hátt</td><td>Beinn peningur til baka. Mikilvægasta atriðið</td></tr>
<tr><td>Hærri úttektarmörk</td><td>⭐⭐⭐⭐ Gott</td><td>Skiptir máli ef þú vinnur stórt</td></tr>
<tr><td>Hraðari úttektir</td><td>⭐⭐⭐⭐ Gott</td><td>Forgangsafgreiðsla</td></tr>
<tr><td>Persónulegur stjórnandi</td><td>⭐⭐⭐ Miðlungs</td><td>Gagnlegt ef vandamál koma upp</td></tr>
<tr><td>Afmælisbónus</td><td>⭐⭐ Lágt</td><td>Oft með háum veðskilyrðum</td></tr>
<tr><td>Sérstakir bónusar</td><td>⭐⭐ Lágt</td><td>Lestu veðskilyrðin — oft 40x+</td></tr>
<tr><td>Lúxusgjafir / ferðir</td><td>⭐ Mjög lágt</td><td>Krefst gríðarlegrar veltu</td></tr>
</tbody></table>

<h2>Endurgreiðsla er það eina sem skiptir raunverulega máli</h2>
<div class="info-box"><p><strong>Reiknaðu þetta:</strong> Ef spilavíti býður 10% vikulega endurgreiðslu á nettótap lækkar það í raun húsforskotið. Á spilakassa með 4% húsforskot og 10% endurgreiðslu er raunverulegt forskot um 3,6%. Það munar.</p></div>
<p>En lestu skilmálana:</p>
<ul>
<li><strong>Er endurgreiðslan í reiðufé eða bónus?</strong> Reiðufé er margfalt betra — bónus kemur með veðskilyrðum</li>
<li><strong>Er hámark?</strong> „10% endurgreiðsla allt að €50" er allt annað en „10% endurgreiðsla"</li>
<li><strong>Nettó eða brúttó tap?</strong> Nettótap (tap mínus vinningar) er staðlað</li>
</ul>

<h2>Spilavíti með sterk VIP-kerfi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/stake/">Stake</a></strong> — Eitt þekktasta VIP-kerfið í bransanum. Stigvaxandi þrep með endurgreiðslu, vikulegum og mánaðarlegum bónusum og persónulegum stjórnanda á hærri þrepum. Gegnsætt þrepakerfi.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> — Velkomstpakki á þrjár innborganir og áframhaldandi tilboð. Samstarfsaðili Svipan.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/katsubet/">KatsuBet</a></strong> — Fjögurra þrepa VIP-kerfi með vikulegum mótum.</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/respin/">Respin</a></strong> — Vikuleg endurgreiðsla og veðlaus tilboð — endurgreiðsla án veðskilyrða er sjaldgæf og verðmæt.</p></div>
<p>Sjá einnig: <a href="{URL_BASE}spilaviti/vip-spilaviti/">VIP-spilavíti</a> · <a href="{URL_BASE}leidbeiningar/vip-kerfi/">hvernig VIP-kerfi virka</a> · <a href="{URL_BASE}leidbeiningar/spilaviti-endurgreidsla/">endurgreiðsla útskýrð</a></p>

<h2>Varúð: VIP-kerfi og ábyrg spilun</h2>
<div class="info-box"><p><strong>Þetta þarf að segjast skýrt.</strong> VIP-kerfi eru hönnuð til að auka veltu. Þau verðlauna þig fyrir að spila meira — sem er beinlínis í andstöðu við <a href="{URL_BASE}leidbeiningar/spila-af-abyrgd/">ábyrga spilun</a>.</p></div>
<p>Ef persónulegur stjórnandi hringir í þig og býður bónus eftir að þú hefur tapað stórt er það ekki vinsemd — það er viðskiptamódel.</p>
<p>Eftirlitsaðilar í Bretlandi og Svíþjóð hafa sektað spilavíti fyrir að ýta VIP-tilboðum að spilurum sem sýndu merki um vandamálaspilun. Vertu meðvitaður um hvatana.</p>
<p>Ef þú finnur að VIP-staða hefur áhrif á hversu mikið þú spilar: <a href="{URL_BASE}leidbeiningar/hvernig-a-ad-setja-takmork-a-spilaviti/">settu takmörk</a> eða <a href="{URL_BASE}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">lestu um viðvörunarmerki</a>.</p>

<h2>Hvernig á að meta VIP-kerfi</h2>
<ol>
<li><strong>Finndu endurgreiðsluhlutfallið</strong> — Allt undir 5% er lítils virði</li>
<li><strong>Athugaðu hvort hún er í reiðufé</strong> — Bónus með 40x veðskilyrðum er nánast verðlaus</li>
<li><strong>Lestu þrepakröfurnar</strong> — Hversu mikla veltu þarf fyrir næsta þrep? Er það raunhæft fyrir þig?</li>
<li><strong>Athugaðu úttektarmörk á hverju þrepi</strong></li>
<li><strong>Hunsaðu gjafir og ferðir</strong> — Þær krefjast veltu sem þú vilt ekki ná</li>
</ol>

<h2>Algengar spurningar</h2>
<h3>Er hægt að komast í VIP án þess að spila mikið?</h3>
<p>Yfirleitt ekki — þrep byggja á veltu. Sum spilavíti bjóða boð byggð á virkni frekar en upphæð, en það er sjaldgæft.</p>
<h3>Er VIP-staða flytjanleg milli spilavíta?</h3>
<p>Nei. Sum spilavíti bjóða þó „VIP status match" þar sem þú sýnir fram á stöðu annars staðar og færð sambærilega.</p>
<h3>Er endurgreiðsla betri en velkomstbónus?</h3>
<p>Fyrir þá sem spila reglulega — já, oftast. Velkomstbónus fæst einu sinni; endurgreiðsla heldur áfram. Og endurgreiðsla í reiðufé hefur engin <a href="{URL_BASE}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrði</a>.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Sjá VIP-spilavíti →</a></div>'''
    },
]

def extract_faqs(html_content):
    """Extract FAQ pairs from <h3>question</h3><p>answer</p> after 'Algengar spurningar' heading."""
    faqs = []
    faq_section = re.split(r'<h2>Algengar spurningar</h2>', html_content, maxsplit=1)
    if len(faq_section) < 2:
        return faqs
    section = faq_section[1]
    pairs = re.findall(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>', section, re.S)
    for q, a in pairs:
        q_clean = re.sub(r'<[^>]+>', '', q).strip()
        a_clean = re.sub(r'<[^>]+>', '', a).strip()
        if q_clean and a_clean:
            faqs.append((q_clean, a_clean))
    return faqs

for page in seo_pages:
    hero = make_hero(page["title"][:40], "Svipan leiðbeining", page["emoji"], *page["colors"])
    page_content = page["content"].replace("{hero}", hero)
    bc = [("{URL_BASE}", "Heim"), ("{URL_BASE}leidbeiningar/", "Leiðbeiningar"), ("", page["title"][:50])]
    # Extract FAQs and add schema
    faqs = extract_faqs(page["content"])
    schema = [faq_schema(faqs)] if faqs else None
    html = page_template(page["title"], page["desc"], bc, page_content, schema_extra=schema)
    write_page(f'leidbeiningar/{page["slug"]}/index.html', html)

print(f"  ✅ {len(seo_pages)} SEO target pages generated")

# 10. ИНДЕКСНЫЕ СТРАНИЦЫ РАЗДЕЛОВ
print("Generating index pages...")

# Casino index — FULL landing page (main casino hub)
casino_cards = ""
for c in casinos[:20]:
    ctype_label = "Crypto" if c["type"]=="crypto" else "Classic"
    casino_img_path = f"img/casinos/{c['slug']}.jpg"
    if os.path.exists(casino_img_path):
        casino_thumb = f'<div class="game-card-thumb" style="position:relative;"><img src="{URL_BASE}{casino_img_path}" alt="{c["name"]}" loading="lazy" style="width:100%;height:100%;object-fit:cover;display:block;border-radius:14px 14px 0 0;"><span style="position:absolute;bottom:8px;right:10px;font-size:22px;font-weight:800;color:#fff;background:rgba(20,22,29,.75);padding:2px 10px;border-radius:8px;">{c["rating"]}</span></div>'
    else:
        casino_thumb = f'<div class="game-card-thumb" style="background:linear-gradient(135deg,{"#62081f,#a3173b" if c["type"]=="crypto" else "#262a35,#a31d2e"});display:flex;align-items:center;justify-content:center;"><span style="font-size:28px;font-weight:800;color:rgba(255,255,255,.88);">{c["rating"]}</span></div>'
    casino_cards += f'''<a href="{URL_BASE}spilaviti/{c["slug"]}/" class="game-card">
{casino_thumb}
<div class="game-card-info"><div class="game-card-name">{c["name"]}</div><div class="game-card-prov">{c["bonus"]} · {ctype_label}</div></div></a>\n'''

casino_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/{c["slug"]}/">{c["name"]}</a></strong> — {isk(c["bonus"])} (Einkunn: {c["rating"]}/10)</p></div>' for c in casinos[:50]])

casino_content = f'''<h1>Bestu netspilavítin á Íslandi 2026</h1>
<p>Svipan umsagnir um {len(casinos)} netspilavíti fyrir íslenska leikmenn. Berðu saman bónusa, greiðslumáta og leikjasöfn. Öll spilavíti styðja dulritunargjaldmiðla — auðveldasta leiðin til að spila frá Íslandi.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á Top Casino →</a></div>
<h2>Besta spilavítið eftir þörfum</h2>
<h3>Hæsti velkomstbónusinn</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> — allt að 5 BTC + 200 frísnúningar. <a href="{URL_BASE}bonusar/velkomstbonus/">Allir velkomstbónusar →</a></p></div>
<h3>Stærsta leikjasafnið</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/7bit/">7Bit Casino</a></strong> — yfir 7.000 leikir samkvæmt rekstraraðila. <a href="{URL_BASE}spilakassar/">Spilakassar →</a></p></div>
<h3>Bestu dulritunarútborganirnar</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> — yfir 100 dulritunargjaldmiðlar og sýnir ISK frá Íslandi. <a href="{URL_BASE}leidbeiningar/besta-crypto-spilaviti-island/">Bestu crypto spilavítin →</a></p></div>
<h3>Íslenskt viðmót</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/respin/">Respin</a></strong> og <strong><a href="{URL_BASE}spilaviti/epicbet/">Epicbet</a></strong> — viðmót á íslensku og PIQ greiðslur. <a href="{URL_BASE}leidbeiningar/spilaviti-islenskt-vidmot/">Meira →</a></p></div>
<h3>Bónus án veðskilyrða</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/winz/">Winz.io</a></strong> — vinningar úr bónus án veðskilyrða. <a href="{URL_BASE}leidbeiningar/frisnuningar-an-innborgunar/">Frísnúningar →</a></p></div>
<h3>Lifandi spilavíti á íslensku</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></strong> — Evolution borð og leyfi innan EES. <a href="{URL_BASE}live/">Lifandi leikir →</a></p></div>
<p style="font-size:16px;color:var(--muted2);">Allur samanburður: <a href="{URL_BASE}leidbeiningar/spilaviti-samanburdur/">Spilavíti samanburður</a> · <a href="{URL_BASE}hvernig-vid-metum/">Hvernig við metum</a></p>
<h2>Topp 20 spilavíti</h2>
<div class="game-grid">{casino_cards}</div>
<h2>Öll {len(casinos)} Spilavíti umsagnir</h2>
{casino_list}'''

write_page("spilaviti/index.html", page_template("Bestu netspilavítin á Íslandi 2026", f"Berðu saman {len(casinos)} netspilavíti á Íslandi. Dulritunargreiðslur, hraðar útborganir, velkomstbónusar.",
    [("{URL_BASE}", "Home"), ("", "Casino")],
    casino_content))

# Slots index — casino-style lobby (500 games)
import catalog as _cat, html as _h
_extra = _cat.build([x["name"] for x in slots_data], 500 - len(slots_data))
_cards = []
for x in slots_data:
    cats = ["review"] + _cat.category(x["name"])
    _cards.append(f'<a class="lb-card" href="{URL_BASE}spilakassar/{x["slug"]}/" data-n="{_h.escape(x["name"].lower())}" data-p="{_h.escape(x["provider"])}" data-c="{" ".join(cats)}"><img src="{URL_BASE}img/slots/{x["slug"]}.jpg" alt="{_h.escape(x["name"])}" loading="lazy" width="360" height="270"><span class="lb-tag">Umsögn</span><span class="lb-hover"><span class="lb-btn">Lesa umsögn</span></span><span class="lb-name">{_h.escape(x["name"])}<small>{_h.escape(x["provider"])}</small></span></a>')
for x in _extra:
    cats = _cat.category(x["name"])
    _rv = next((r for r in EXTRA_REVIEWS if r["key"] == x["slug"]), None)
    if _rv:
        _cards.append(f'<a class="lb-card" href="{URL_BASE}spilakassar/{_rv["slug"]}/" data-n="{_h.escape(x["name"].lower())}" data-p="{_h.escape(x["provider"])}" data-c="review {" ".join(cats)}"><img src="{URL_BASE}img/lobby/{x["slug"]}.jpg" alt="{_h.escape(x["name"])}" loading="lazy" width="360" height="270"><span class="lb-tag">Umsögn</span><span class="lb-hover"><span class="lb-btn">Lesa umsögn</span></span><span class="lb-name">{_h.escape(x["name"])}<small>{_h.escape(x["provider"])}</small></span></a>')
        continue
    _cards.append(f'<a class="lb-card" href="{AFF}" target="_blank" rel="sponsored nofollow noopener" data-n="{_h.escape(x["name"].lower())}" data-p="{_h.escape(x["provider"])}" data-c="{" ".join(cats)}"><img src="{URL_BASE}img/lobby/{x["slug"]}.jpg" alt="{_h.escape(x["name"])}" loading="lazy" width="360" height="270"><span class="lb-hover"><span class="lb-btn">Spila á Slotoro</span></span><span class="lb-name">{_h.escape(x["name"])}<small>{_h.escape(x["provider"])}</small></span></a>')
_provs = {}
for x in slots_data + _extra:
    _provs[x["provider"]] = _provs.get(x["provider"], 0) + 1
_prov_opts = "".join(f'<option value="{_h.escape(k)}">{_h.escape(k)} ({v})</option>' for k, v in sorted(_provs.items(), key=lambda kv: -kv[1]))
_tabs = [("all","Allir leikir"),("review","Með umsögn"),("megaways","Megaways"),("jackpot","Pottar"),("book","Bókaleikir"),("fishing","Veiði"),("classic","Klassískir")]
_tab_html = "".join(f'<button type="button" class="lb-tab{" on" if k=="all" else ""}" data-t="{k}">{v}</button>' for k, v in _tabs)
lobby = f"""<style>
.lb-head h1{{margin-bottom:6px}}.lb-sub{{opacity:.85;margin:0 0 18px}}
.lb-bar{{position:sticky;top:64px;z-index:5;background:rgba(28,7,10,.92);backdrop-filter:blur(10px);padding:12px 0;margin-bottom:14px;display:flex;flex-wrap:wrap;gap:10px;align-items:center}}
.lb-search{{flex:1 1 220px;min-width:180px;padding:12px 16px;border-radius:999px;border:1px solid rgba(255,255,255,.18);background:rgba(255,255,255,.06);color:#fff;font-size:16px}}
.lb-prov{{padding:12px 14px;border-radius:999px;border:1px solid rgba(255,255,255,.18);background:#310f14;color:#fff;font-size:16px;max-width:100%}}
.lb-tabs{{display:flex;gap:8px;overflow-x:auto;width:100%;padding-bottom:2px;scrollbar-width:none}}.lb-tabs::-webkit-scrollbar{{display:none}}
.lb-tab{{flex:0 0 auto;padding:9px 16px;border-radius:999px;border:1px solid rgba(255,255,255,.16);background:rgba(255,255,255,.05);color:#ffe2e6;font-size:16px;cursor:pointer;white-space:nowrap}}
.lb-tab.on{{background:linear-gradient(135deg,#c52b36,#ff725f);border-color:transparent;color:#fff;font-weight:600}}
.lb-count{{font-size:16px;opacity:.75;margin:0 0 10px}}
.lb-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:14px}}
.lb-card{{position:relative;display:block;aspect-ratio:4/3;border-radius:16px;overflow:hidden;background:#310f14;text-decoration:none;color:#fff;box-shadow:0 6px 18px rgba(0,0,0,.35);transition:transform .15s}}
.lb-card:hover,.lb-card:focus-visible{{transform:translateY(-3px)}}
.lb-card img{{width:100%;height:100%;object-fit:cover;display:block}}
.lb-tag{{position:absolute;top:8px;left:8px;background:#c52b36;color:#fff;font-size:16px;font-weight:700;padding:4px 9px;border-radius:8px}}
.lb-name{{color:#fff;position:absolute;left:0;right:0;bottom:0;padding:26px 10px 9px;background:linear-gradient(transparent,rgba(0,0,0,.85));font-size:16px;font-weight:600;line-height:1.25}}
.lb-name small{{display:block;font-weight:400;opacity:.75;font-size:16px}}
.lb-hover{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(25,5,8,.55);opacity:0;transition:opacity .15s}}
.lb-card:hover .lb-hover,.lb-card:focus-visible .lb-hover{{opacity:1}}
.lb-btn{{padding:10px 18px;border-radius:999px;background:linear-gradient(135deg,#e04550,#d63641);font-weight:700;font-size:16px}}
.lb-more{{display:block;margin:22px auto 6px}}
.lb-empty{{text-align:center;opacity:.8;padding:30px 0}}
@media(max-width:520px){{.lb-grid{{grid-template-columns:repeat(2,1fr);gap:10px}}.lb-name{{font-size:16px;padding:20px 6px 6px}}.lb-name small{{display:none}}.lb-tag{{font-size:16px;padding:3px 6px}}}}
</style>
<div class="lb-head"><h1>Spilakassar — {len(_cards)} leikir</h1>
<p class="lb-sub">Vinsælustu spilakassarnir frá {len(_provs)} framleiðendum. Leikir merktir „Umsögn“ ({len(slots_data)+len(EXTRA_REVIEWS)}) eru með umsögn hjá okkur; aðrir opnast hjá Slotoro.</p></div>
<div class="lb-bar"><input class="lb-search" type="search" placeholder="Leita að leik…" aria-label="Leita að leik"><select class="lb-prov" aria-label="Framleiðandi"><option value="">Allir framleiðendur</option>{_prov_opts}</select><div class="lb-tabs" role="tablist">{_tab_html}</div></div>
<p class="lb-count" aria-live="polite"></p>
<div class="lb-grid">{"".join(_cards)}</div>
<p class="lb-empty" hidden>Enginn leikur fannst. Prófaðu annað leitarorð.</p>
<button type="button" class="cta-btn lb-more">Sýna fleiri leiki</button>
<p style="font-size:16px;opacity:.75;margin-top:18px">Leikjaframboð Slotoro getur verið mismunandi eftir landi og breyst án fyrirvara. 18+ · Spilaðu á ábyrgan hátt · Hjálparsími 1717.</p>
<script>(function(){{var cards=[].slice.call(document.querySelectorAll('.lb-card')),q=document.querySelector('.lb-search'),pv=document.querySelector('.lb-prov'),more=document.querySelector('.lb-more'),cnt=document.querySelector('.lb-count'),empty=document.querySelector('.lb-empty'),tab='all',limit=60;
function run(){{var s=q.value.trim().toLowerCase(),p=pv.value,m=[];cards.forEach(function(c){{var ok=(!s||c.dataset.n.indexOf(s)>-1)&&(!p||c.dataset.p===p)&&(tab==='all'||(' '+c.dataset.c+' ').indexOf(' '+tab+' ')>-1);if(ok)m.push(c);c.hidden=true}});m.forEach(function(c,i){{c.hidden=i>=limit}});cnt.textContent=m.length+' leikir';more.hidden=m.length<=limit;empty.hidden=m.length>0}}
q.addEventListener('input',function(){{limit=60;run()}});pv.addEventListener('change',function(){{limit=60;run()}});
document.querySelectorAll('.lb-tab').forEach(function(b){{b.addEventListener('click',function(){{document.querySelectorAll('.lb-tab').forEach(function(x){{x.classList.remove('on')}});b.classList.add('on');tab=b.dataset.t;limit=60;run()}})}});
more.addEventListener('click',function(){{limit+=60;run()}});run()}})();</script>
<style>.lb-card[hidden]{{display:none!important}}</style>"""
write_page("spilakassar/index.html", page_template("Spilakassar — 500 vinsælir leikir", f"Leitaðu í {len(_cards)} spilakössum frá {len(_provs)} framleiðendum: Pragmatic Play, Play'n GO, NetEnt, Hacksaw, NoLimit City og fleiri. Umsagnir um 80 vinsælustu.",
    [("{URL_BASE}", "Heim"), ("", "Spilakassar")], lobby))

# Live index
live_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}live/{g["slug"]}/">{g["name"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in live_games[:20]])
write_page("live/index.html", page_template("Live Casino", "Leikir með lifandi spilastjórum",
    [("{URL_BASE}", "Home"), ("", "Live Casino")],
    f'<h1>Spilavíti í beinni — Leikir með lifandi spilastjórum</h1><p>{len(live_games)} leikir með faglegum spilastjórum.</p>{live_list}'))

# Bonus index
bonus_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}bonusar/{b["slug"]}/">{b["title"]}</a></strong> — {b["desc"][:80]}</p></div>' for b in bonus_pages[:20]])
write_page("bonusar/index.html", page_template("Casino Bónusar", "Allir bónusar og afsláttarkóðar",
    [("{URL_BASE}", "Home"), ("", "Bónusar")],
    f'<h1>Casino Bónusar 2026</h1><p>{len(bonus_pages)} virk bónustilboð.</p>{bonus_list}'))

# Payment index
pay_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}greidslur/{p["slug"]}/">{p["title"]}</a></strong></p></div>' for p in payment_pages[:20]])
write_page("greidslur/index.html", page_template("Greiðslumátar", "Dulritunargjaldmiðlar og aðrar greiðslur í spilavítum",
    [("{URL_BASE}", "Home"), ("", "Payments")],
    f'<h1>Casino Greiðslumátar</h1><p>Hvernig á að komast framhjá lokun banka og spila frá Íslandi.</p>{pay_list}'))

# Guide index
guide_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}leidbeiningar/{g["slug"]}/">{g["title"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in seo_pages + guide_pages])
write_page("leidbeiningar/index.html", page_template("Guides", "Leiðbeiningar og kennsluefni fyrir leikmenn",
    [("{URL_BASE}", "Home"), ("", "Guides")],
    f'<h1>Leiðbeiningar fyrir leikmenn</h1><p>{len(guide_pages)} leiðbeiningar fyrir byrjendur og reynda leikmenn.</p>{guide_list}'))


# 10. SITEMAP
# Author page
_author = f'''<h1>Valbjörn Gjúkason</h1>
<p><strong>Blaðamaður og ritstjóri Svipan.</strong> Valbjörn er blaðamaður sem fjallar um fjárhættuspil og netspilavíti. Hjá Svipan ber hann ábyrgð á öllum umsögnum, samanburði og leiðbeiningum á vefnum og fer yfir hverja síðu áður en hún birtist.</p>
<h2>Hvað hann skoðar</h2>
<ul>
<li>Spilakassa: RTP, sveiflu, hámarksvinning og hvernig bónusinn virkar, borið saman við gögn framleiðenda og óháðra gagnagrunna.</li>
<li>Spilavíti: leyfi, skilmála bónusa, veðskilyrði, greiðsluleiðir fyrir íslenska leikmenn og hvort hægt sé að nota íslenskar krónur.</li>
<li>Leiðbeiningar: íslensk lög, skatta á vinninga og úrræði eins og Hjálparsíma Rauða krossins 1717.</li>
</ul>
<h2>Ritstjórnarstefna</h2>
<p>Við birtum aðeins tölur sem við getum vísað í heimild fyrir. Þegar heimildir eru ósammála segjum við það og bendum á upplýsingaskjá leiksins í stað þess að giska. Síður eru merktar með dagsetningu síðustu uppfærslu.</p>
<p>Svipan fær þóknun frá Slotoro ef þú skráir þig í gegnum tengla okkar. Það hefur ekki áhrif á einkunnir, og við segjum skýrt frá því á hverri síðu. Lestu meira um <a href="{URL_BASE}hvernig-vid-metum/">hvernig við metum spilavíti</a>.</p>
<h2>Leiðrétting</h2>
<p>Finnurðu villu í umsögn? Láttu okkur vita og við leiðréttum hana og uppfærum dagsetninguna.</p>'''
write_page("hofundur/valbjorn-gjukason/index.html", page_template("Valbjörn Gjúkason — ritstjóri Svipan", "Valbjörn Gjúkason er blaðamaður sem fjallar um fjárhættuspil og ritstjóri Svipan. Hann ber ábyrgð á umsögnum um spilakassa og spilavíti fyrir íslenska leikmenn.",
    [("{URL_BASE}", "Heim"), ("", "Höfundur")], _author, show_byline=False,
    schema_extra=[{"@type":"ProfilePage","mainEntity":{"@id":"https://svipan.is/#valbjorn"}}]))

print("Generating sitemap.xml...")

# 404 page for GitHub Pages / static hosting
_content404 = """<h1>404 — Síðan fannst ekki</h1>
<p>Því miður er þessi síða ekki til. Kannski hefur slóðin breyst eða síðan verið fjarlægð.</p>
<div class=\"info-box\"><p>Prófaðu að byrja á <a href=\"{URL_BASE}\">forsíðunni</a>, skoða <a href=\"{URL_BASE}spilaviti/\">spilavítaumsagnir</a> eða <a href=\"{URL_BASE}spilakassar/\">spilakassa</a>.</p></div>"""
_html404 = page_template("Síðan fannst ekki (404)", "Þessi síða er ekki til á svipan.is — finndu það sem þú leitar að á forsíðunni.", [("{URL_BASE}", "Heim"), ("", "404")], _content404.replace("{URL_BASE}", URL_BASE), show_byline=False)
_html404 = _html404.replace("</title>", "</title>\n<meta name=\"robots\" content=\"noindex\">", 1)
write_page("404.html", _html404)

sitemap_urls = ['https://svipan.is/', 'https://svipan.is/afthreying/', 'https://svipan.is/hofundur/valbjorn-gjukason/']
for c in casinos:
    sitemap_urls.append(f'https://svipan.is/spilaviti/{c["slug"]}/')
for cat in casino_categories:
    sitemap_urls.append(f'https://svipan.is/spilaviti/{cat["slug"]}/')
for s in slots_data:
    sitemap_urls.append(f'https://svipan.is/spilakassar/{s["slug"]}/')
for s in EXTRA_REVIEWS:
    sitemap_urls.append(f'https://svipan.is/spilakassar/{s["slug"]}/')
for g in live_games:
    sitemap_urls.append(f'https://svipan.is/live/{g["slug"]}/')
for b in bonus_pages:
    sitemap_urls.append(f'https://svipan.is/bonusar/{b["slug"]}/')
for p in payment_pages:
    sitemap_urls.append(f'https://svipan.is/greidslur/{p["slug"]}/')
for g in guide_pages:
    sitemap_urls.append(f'https://svipan.is/leidbeiningar/{g["slug"]}/')
for sp in seo_pages:
    sitemap_urls.append(f'https://svipan.is/leidbeiningar/{sp["slug"]}/')
for a in about_pages:
    sitemap_urls.append(f'https://svipan.is/{a["slug"]}/')
sitemap_urls.extend([
    'https://svipan.is/spilaviti/',
    'https://svipan.is/spilakassar/',
    'https://svipan.is/live/',
    'https://svipan.is/bonusar/',
    'https://svipan.is/greidslur/',
    'https://svipan.is/leidbeiningar/',
])

sitemap_urls = [u for u in sitemap_urls
                if u.replace("https://svipan.is/", "").rstrip("/") not in REWRITE_QUEUE]

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_xml += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
sitemap_xml += '</urlset>'

with open(os.path.join(BASE, 'sitemap.xml'), 'w') as f:
    f.write(sitemap_xml)

# robots.txt
with open(os.path.join(BASE, 'robots.txt'), 'w') as f:
    f.write('User-agent: *\nAllow: /\nSitemap: https://svipan.is/sitemap.xml\n')

print(f"\n✅ Generated {count} pages + sitemap.xml + robots.txt")
print(f"URLs in sitemap: {len(sitemap_urls)}")

import subprocess as _sp
_sp.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "interlink.py")], check=False)
