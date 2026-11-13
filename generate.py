#!/usr/bin/env python3
"""
Bestiflokkurinn.is — BF Casino site generator
Öll content in English
"""
import os
import json
import sys
import re

# URL base path — "/" for production on bestiflokkurinn.is, "/slotoro-site/" for GitHub Pages
URL_BASE = "/" if "--production" in sys.argv else "/slotoro-site/"

# ============================================================
# PAGE DATA
# ============================================================

# 150 casino reviews
casinos = [
    {"slug": "bitstarz", "name": "BitStarz", "rating": 9.8, "bonus": "5 BTC + 200 FS", "type": "crypto", "desc": "Margverðlaunað dulritunarspilavíti með yfir 3.500 leikjum frá Pragmatic Play, Evolution og Play'n GO. Tekur við BTC, ETH, LTC, DOGE og fleiri myntum. Rekstraraðilinn segir útborganir í dulritunargjaldmiðlum afgreiddar á nokkrum mínútum. Curaçao leyfi."},
    {"slug": "stake", "name": "Stake", "rating": 9.6, "bonus": "200% + VIP", "type": "crypto", "desc": "Eitt vinsælasta dulritunarspilavíti heims með VIP kerfi, eigin Stake leikjum og íþróttaveðmálum. Styður 8 dulritunargjaldmiðla og birtir húsforskot á eigin leikjum."},
    {"slug": "bc-game", "name": "BC.Game", "rating": 9.4, "bonus": "300% up to 1 BTC", "type": "crypto", "desc": "Spilavíti með eigin crash, dice og limbo leikjum. Styður yfir 100 dulritunargjaldmiðla, þar á meðal BTC, ETH, SOL og DOGE. Daglegir bónusar og verkefnakerfi. Curaçao leyfi."},
    {"slug": "tonybet", "name": "TonyBet", "rating": 9.2, "bonus": "150% + 100 FS", "type": "classic", "desc": "Rótgróið spilavíti og veðmálasíða með sterkum lifandi spilavítishluta frá Evolution. Tekur við Visa, Mastercard, Skrill og dulritunargjaldmiðlum. Leyfi í Eistlandi (innan EES)."},
    {"slug": "epicbet", "name": "Epicbet", "rating": 9.0, "bonus": "100% up to €500", "type": "classic", "desc": "Nútímalegt spilavíti með skýru viðmóti, íslensku tungumáli og Apple Pay. Yfir 2.000 spilakassar frá NetEnt, Microgaming og Pragmatic Play."},
    {"slug": "respin", "name": "Respin Casino", "rating": 8.9, "bonus": "200% + 50 FS", "type": "classic", "desc": "Spilavíti með yfir 4.000 spilakössum, íslensku viðmóti og PIQ greiðslum. Vikuleg endurgreiðsla og endurnýjunartilboð fyrir núverandi leikmenn."},
    {"slug": "vegazone", "name": "VegaZone", "rating": 8.8, "bonus": "150% up to €300", "type": "classic", "desc": "Spilavíti með spilakassamótum, reglulegum tilboðum og tryggðarkerfi. Gott úrval lifandi borða og stuðningur við rafræn veski."},
    {"slug": "wildcoins", "name": "WildCoins", "rating": 8.7, "bonus": "250% + 100 FS", "type": "crypto", "desc": "Dulritunarspilavíti með háum hlutfallsbónusum. Styður Bitcoin, Ethereum, Litecoin og USDT."},
    {"slug": "katsubet", "name": "KatsuBet", "rating": 8.6, "bonus": "100% + 100 FS", "type": "crypto", "desc": "Japanskt þema og yfir 5.000 leikir frá 40+ framleiðendum. Tekur við BTC, ETH, LTC, DOGE, USDT og BCH. Vikuleg mót og fjögurra þrepa VIP kerfi."},
    {"slug": "winz", "name": "Winz.io", "rating": 8.5, "bonus": "300 FS no wager", "type": "crypto", "desc": "Spilavíti með bónusum án veðskilyrða — það sem þú vinnur geturðu tekið út. Styður 6 dulritunargjaldmiðla og yfir 5.000 leiki. Curaçao leyfi."},
    {"slug": "7bit", "name": "7Bit Casino", "rating": 8.5, "bonus": "200% + 100 FS", "type": "crypto", "desc": "Dulritunarspilavíti í retró stíl, starfrækt síðan 2014. Yfir 7.000 leikir, vikuleg endurgreiðsla og mánudagsbónusar."},
    {"slug": "mbitcasino", "name": "mBit Casino", "rating": 8.4, "bonus": "175% + 300 FS", "type": "crypto", "desc": "Eitt elsta dulritunarspilavítið, starfrækt síðan 2014. Tekur við Bitcoin, Ethereum, Litecoin, Dogecoin og Tether. Yfir 3.000 leikir."},
    {"slug": "cloudbet", "name": "Cloudbet", "rating": 8.4, "bonus": "100% up to 5 BTC", "type": "crypto", "desc": "Dulritunarspilavíti og veðmálasíða með háum borðmörkum fyrir stórspilara. Styður BTC, ETH, USDT og fleiri."},
    {"slug": "casinonic", "name": "Casinonic", "rating": 8.3, "bonus": "100% + 100 FS", "type": "classic", "desc": "Byrjendavænt spilavíti með einfaldri skráningu. Yfir 2.000 spilakassar, lifandi borð og vikuleg endurgreiðsla."},
    {"slug": "national-casino", "name": "National Casino", "rating": 8.3, "bonus": "100% + 100 FS", "type": "classic", "desc": "Spilavíti með gott úrval lifandi leikja frá Evolution og Pragmatic Play Live og nokkrar útborgunarleiðir."},
    {"slug": "20bet", "name": "20Bet", "rating": 8.2, "bonus": "100% up to €120", "type": "classic", "desc": "Spilavíti, lifandi spilavíti og veðmálasíða á einum stað. Yfir 6.000 leikir frá 70+ framleiðendum. Curaçao leyfi."},
    {"slug": "rocketplay", "name": "RocketSpila", "rating": 8.2, "bonus": "150% + 100 FS", "type": "crypto", "desc": "Spilavíti með geimþema og yfir 3.500 leikjum. Vikulegir endurnýjunarbónusar og fjögurra þrepa VIP kerfi."},
    {"slug": "hellspin", "name": "HellSpin", "rating": 8.1, "bonus": "150% + 50 FS", "type": "crypto", "desc": "Spilavíti með tíðum tilboðum og dökku viðmóti. Styður BTC, ETH, LTC og USDT. Yfir 3.000 leikir."},
    {"slug": "neospin", "name": "NeoSpin", "rating": 8.1, "bonus": "100% + 100 FS", "type": "crypto", "desc": "Nútímalegt spilavíti með yfir 5.000 leikjum og stuðningi við Bitcoin, Ethereum og Tether. Dagleg endurgreiðsla og vikuleg mót."},
    {"slug": "betpanda", "name": "BetPanda", "rating": 8.0, "bonus": "100% up to 1 BTC", "type": "crypto", "desc": "Dulritunarspilavíti með tiltölulega lágum veðskilyrðum (venjulega 30x). Styður BTC, ETH og USDT."},
]

# Real slots only
slots_data = [
    {"slug": "gates-of-olympus", "name": "Gates of Olympus", "provider": "Pragmatic Play", "rtp": 96.5, "volatility": "High", "maxwin": "x5000", "theme": "Mythology", "cdn": "pragmaticexternal/vs20olympgate.png"},
    {"slug": "sweet-bonanza", "name": "Sweet Bonanza", "provider": "Pragmatic Play", "rtp": 96.48, "volatility": "High", "maxwin": "x21100", "theme": "Fruit", "cdn": "pragmaticexternal/vs20fruitsw.png"},
    {"slug": "big-bass-splash", "name": "Big Bass Splash", "provider": "Pragmatic Play", "rtp": 96.71, "volatility": "High", "maxwin": "x2100", "theme": "Fishing", "cdn": "pragmaticexternal/vs10bbsplash.png"},
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

# Casino categories (50 pages) — all in Icelandic
casino_categories = [
    {"slug": "luchshie-online-casino", "title": "Bestu netspilavítin", "desc": "Hæst metnu netspilavítin fyrir íslenska leikmenn."},
    {"slug": "crypto-casino", "title": "Dulritunargjaldmiðils spilavíti", "desc": "Spilavíti sem taka við Bitcoin, Ethereum og öðrum dulritunargjaldmiðlum."},
    {"slug": "novye-casino", "title": "Ný spilavíti 2026", "desc": "Nýjustu netspilavítin sem opnuðu árið 2026."},
    {"slug": "casino-s-bystrym-vyvodom", "title": "Hröð útborgun spilavíti", "desc": "Spilavíti þar sem útborganir eru afgreiddar á undir 24 klukkustundum."},
    {"slug": "casino-bez-verifikacii", "title": "Spilavíti án KYC", "desc": "Spilavíti sem krefjast ekki persónuskilríkja."},
    {"slug": "bitcoin-casino", "title": "Bitcoin spilavíti", "desc": "Bestu spilavítin fyrir Bitcoin innborganir og útborganir."},
    {"slug": "ethereum-casino", "title": "Ethereum spilavíti", "desc": "Spilavíti sem taka við Ethereum innborgunum og útborgunum."},
    {"slug": "usdt-casino", "title": "USDT spilavíti", "desc": "Spilavíti sem taka við USDT stablecoin."},
    {"slug": "litecoin-casino", "title": "Litecoin spilavíti", "desc": "Spilavíti með Litecoin innborgunum."},
    {"slug": "live-casino", "title": "Spilavíti í beinni", "desc": "Bestu spilavítin með lifandi spilastjórum."},
    {"slug": "casino-s-bonusom", "title": "Spilavíti með bónus", "desc": "Spilavíti sem bjóða rausnarlega velkomstbónusa."},
    {"slug": "casino-bez-depozita", "title": "Spilavíti án innborgunar", "desc": "Bónusar án innborgunarkröfu."},
    {"slug": "casino-s-frispinami", "title": "Ókeypis snúningar spilavíti", "desc": "Spilavíti sem bjóða ókeypis snúninga við skráningu."},
    {"slug": "mobilnoe-casino", "title": "Farsíma spilavíti", "desc": "Bestu spilavítin fyrir farsímaspilun á iPhone og Android."},
    {"slug": "casino-s-niskim-depozitom", "title": "Lág innborgun spilavíti", "desc": "Spilavíti þar sem þú getur spilað frá €1."},
    {"slug": "vip-casino", "title": "VIP spilavíti", "desc": "Spilavíti með bestu VIP og tryggðarkerfi."},
    {"slug": "megaways-casino", "title": "Megaways spilavíti", "desc": "Spilavíti með stórt úrval Megaways spilakassa."},
    {"slug": "jackpot-casino", "title": "Jackpot spilavíti", "desc": "Spilavíti með stigvaxandi jackpottum."},
    {"slug": "casino-s-vysokim-rtp", "title": "Hátt RTP spilavíti", "desc": "Spilavíti sem bjóða spilakassa með RTP yfir 97%."},
    {"slug": "casino-s-licenziej", "title": "Leyfisskyld spilavíti", "desc": "Staðfest og leyfisskyld netspilavíti."},
]

# 30 more categories — Icelandic titles
more_cats = [
    ("Curaçao spilavíti", "Spilavíti með Curaçao leyfi fyrir íslenska leikmenn."),
    ("Malta MGA spilavíti", "Spilavíti með Malta MGA leyfi."),
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
    live_games.append({"slug": slug, "name": name, "desc": f"{name} — spilaðu með lifandi spilastjóra á bestu spilavítunum fyrir Ísland."})

# Bónusar (80 pages) — all Icelandic
bonus_pages = [
    {"slug": "velkomstbonus", "title": "Velkomstbónus", "desc": "Bestu velkomstbónusarnir á netspilavítum sem eru í boði fyrir íslenska leikmenn."},
    {"slug": "frispiny-bez-depozita", "title": "Ókeypis snúningar án innborgunar", "desc": "Ókeypis snúningar án innborgunarkröfu — skráðu þig og sæktu."},
    {"slug": "bezdepozitnye-bonusy", "title": "Bónusar án innborgunar", "desc": "Allir bónusar án innborgunar á spilavítum sem taka við íslenskum leikmönnum."},
    {"slug": "keshbek", "title": "Endurgreiðslubónusar", "desc": "Spilavíti sem bjóða endurgreiðslu á nettótapi — fáðu hlutfall til baka vikulega."},
    {"slug": "bonus-za-registraciyu", "title": "Skráningarbónus", "desc": "Fáðu bónus strax eftir skráningu — engin innborgun þarf."},
    {"slug": "bonus-na-pervyj-depozit", "title": "Fyrsta innborgunarbónus", "desc": "Bestu bónusarnir á fyrstu innborgun hjá efstu spilavítum."},
    {"slug": "bonus-na-vtoroj-depozit", "title": "Önnur innborgunarbónus", "desc": "Bónusar á annarri innborgun — endurnýjunartilboð við næstu áfyllingu."},
    {"slug": "vejer", "title": "Hvað eru veðskilyrði", "desc": "Skilningur á veðskilyrðum — hvernig gegnumspilun virkar og hvað á að hafa í huga."},
    {"slug": "bonus-kody", "title": "Bónuskóðar spilavíta", "desc": "Virk afsláttarkóðar og bónuskóðar fyrir netspilavíti árið 2026."},
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
    {"slug": "kak-kupit-bitcoin", "title": "Hvernig á að kaupa Bitcoin", "desc": "Skref-fyrir-skref leiðbeiningar um kaup á Bitcoin fyrir spilavítainnborganir á Íslandi."},
    {"slug": "kak-kupit-ethereum", "title": "Hvernig á að kaupa Ethereum", "desc": "Hvar og hvernig á að kaupa Ethereum fyrir spilavítainnborganir."},
    {"slug": "obhod-blokirovok-bankov", "title": "Framhjá bankalokunum", "desc": "Hvernig á að komast framhjá lokun íslenskra banka á spilavítagreiðslum með dulritunargjaldmiðlum."},
    {"slug": "kripto-koshelki", "title": "Dulritunarveski", "desc": "Bestu dulritunarveskin fyrir spilavítainnborganir — MetaMask, Trust Wallet og fleira."},
    {"slug": "metamask-casino", "title": "MetaMask fyrir spilavíti", "desc": "Notkun MetaMask veskis fyrir innborganir og útborganir á netspilavítum."},
    {"slug": "trust-wallet-casino", "title": "Trust Wallet fyrir spilavíti", "desc": "Innborganir á spilavíti í gegnum Trust Wallet — fullkomin leiðbeining."},
    {"slug": "binance-casino", "title": "Binance fyrir spilavíti", "desc": "Hvernig á að millifæra fjármuni frá Binance kauphöll á spilavítareikninginn þinn."},
    {"slug": "coinbase-casino", "title": "Coinbase fyrir spilavíti", "desc": "Kaupa dulritunargjaldmiðil á Coinbase og leggja inn á netspilavíti."},
    {"slug": "kraken-casino", "title": "Kraken fyrir spilavíti", "desc": "Notkun Kraken kauphallar fyrir dulritunarfærslur í spilavítum."},
    {"slug": "vpn-casino", "title": "VPN fyrir spilavíti", "desc": "Þarftu VPN til að spila á netspilavítum frá Íslandi? Lagaleg samantekt."},
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
    ("Lágmarksinnborgun €1", "Spilavíti þar sem þú getur spilað frá €1."),
    ("Lágmarksinnborgun €5", "Spilavíti þar sem þú getur spilað frá €5."),
    ("Lágmarksinnborgun €10", "Spilavíti þar sem þú getur spilað frá €10."),
    ("Kortaútborganir", "Hvernig á að taka út vinninga á greiðslukort."),
    ("Hraðar dulritunarútborganir", "Hraðastar dulritunarútborganir á spilavítum."),
]
for title, desc in more_payments:
    slug = title.lower().replace("€", "eur").replace(" ", "-").replace("(", "").replace(")", "").replace("á", "a").replace("ú", "u")
    payment_pages.append({"slug": slug, "title": title, "desc": desc})

# Guides (60 pages) — all Icelandic
guide_pages = [
    {"slug": "kak-vybrat-casino", "title": "Hvernig á að velja netspilavíti", "desc": "Fullkomin leiðbeining um val á áreiðanlegu og öruggu netspilavíti."},
    {"slug": "chto-takoe-rtp", "title": "Hvað er RTP", "desc": "Skilningur á RTP (Return to Player) — hvað það þýðir fyrir spilun þína."},
    {"slug": "chto-takoe-volatilnost", "title": "Hvað er sveifla", "desc": "Munurinn á lágri, miðlungs og hárri sveiflu spilakassa útskýrður."},
    {"slug": "kak-igrat-v-sloty", "title": "Hvernig á að spila spilakassa", "desc": "Skref-fyrir-skref leiðbeining fyrir byrjendur — hvernig spilakassar virka."},
    {"slug": "strategii-blackjack", "title": "Blackjack aðferðir", "desc": "Grunn blackjack aðferð og aðferðakort — bættu líkurnar þínar."},
    {"slug": "pravila-ruletki", "title": "Rúlettureglur", "desc": "Hvernig á að spila rúlettu — fullkomnar reglur, veðmál og aðferðir."},
    {"slug": "pravila-bakkary", "title": "Baccarat reglur", "desc": "Hvernig á að spila baccarat — reglur, aðferðir og ráð."},
    {"slug": "kak-vyigrat-v-casino", "title": "Hvernig á að vinna á spilavítum", "desc": "Ráðleggingar og aðferðir til að bæta líkur þínar á netspilavítum."},
    {"slug": "otvetstvennaya-igra", "title": "Ábyrg spilun", "desc": "Hvernig á að spila á ábyrgan hátt — setja mörk og halda stjórn."},
    {"slug": "zakon-ob-azartnyh-igrah-islandiya", "title": "Fjárhættuspilalagaíslandi", "desc": "Lagaleg staða netspilavíta á Íslandi — hvað leikmenn þurfa að vita."},
    {"slug": "nalogi-na-vyigrysh", "title": "Skattar á spilavinninga", "desc": "Þarftu að borga skatta af fjárhættuspilvinningum á Íslandi?"},
    {"slug": "bezopasnost-v-casino", "title": "Öryggi spilavíta", "desc": "Hvernig á að vernda persónuupplýsingarnar þínar þegar þú spilar á netspilavítum."},
    {"slug": "glossarij-casino", "title": "Orðasafn spilavíta", "desc": "Orðasafn spilavíta — öll fjárhættuspilahugtök frá A til Ö útskýrð."},
    {"slug": "provajdery-igr", "title": "Leikjabirgjar", "desc": "Yfirlit yfir stærstu spilakassabirgjana og þróunaraðila."},
    {"slug": "megaways-sloty", "title": "Hvað eru Megaways spilakassar", "desc": "Hvernig Megaways vélbúnaðurinn virkar — allt að 117.649 leiðir til vinnings."},
    {"slug": "bonus-buy-sloty", "title": "Bonus Buy spilakassar", "desc": "Hvernig Bonus Buy spilakassar virka — farðu beint í bónuslotuna."},
    {"slug": "progressivnye-jackpoty", "title": "Stigvaxandi jackpottar", "desc": "Hvernig stigvaxandi jackpottar virka og hvernig á að vinna þá."},
    {"slug": "turniry-v-casino", "title": "Spilavítamót", "desc": "Hvernig spilakassamót virka — kepptu um peningaverðlaun."},
    {"slug": "vip-programmy", "title": "VIP kerfi", "desc": "Hvernig VIP og tryggðarkerfi virka á netspilavítum."},
    {"slug": "casino-na-telefone", "title": "Farsíma spilavíti", "desc": "Bestu farsíma spilavítin og spilavíti öppin fyrir iPhone og Android."},
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
    guide_pages.append({"slug": slug, "title": title, "desc": desc})

# About (10 pages)
about_pages = [
    {"slug": "o-nas", "title": "Um BF Casino", "desc": "Hverjir við erum og hvers vegna við stofnuðum BF Casino á Bestiflokkurinn.is."},
    {"slug": "kontakty", "title": "Hafa samband", "desc": "Hafðu samband við BF Casino teymið."},
    {"slug": "konfidencialnost", "title": "Persónuverndarstefna", "desc": "Hvernig við meðhöndlum gögnin þín — persónuverndarstefna okkar útskýrð."},
    {"slug": "usloviya", "title": "Notkunarskilmálar", "desc": "Notkunarskilmálar vefsíðunnar Bestiflokkurinn.is."},
    {"slug": "otkaz-ot-otvetstvennosti", "title": "Fyrirvari", "desc": "Mikilvægur lagalegur fyrirvari um spilavítaumsagnir okkar."},
    {"slug": "kak-my-ocenivaem", "title": "Hvernig við metum spilavíti", "desc": "Hvernig við metum og umsögnum netspilavíti — aðferðafræði okkar."},
    {"slug": "redakcionnaya-politika", "title": "Ritstjórnarstefna", "desc": "Ritstjórnarstefna okkar — sjálfstæði, nákvæmni og gagnsæi."},
    {"slug": "partnerstvo", "title": "Samstarf", "desc": "Samstarfstækifæri hjá BF Casino."},
    {"slug": "karta-sajta", "title": "Vefkort", "desc": "Fullkomið vefkort yfir allar síður á Bestiflokkurinn.is."},
    {"slug": "otvetstvennaya-igra-stranica", "title": "Ábyrg spilun", "desc": "Afstaða okkar til ábyrgrar spilunar og verndar leikmanna."},
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

def make_hero(title, subtitle, emoji, grad1="#1a0840", grad2="#3020a0", grad3="#6040c0"):
    """Generate a themed gradient hero card with emoji, title and subtitle."""
    return f'''<div class="slot-hero"><div class="slot-hero-bg" style="background:linear-gradient(135deg,{grad1},{grad2},{grad3});display:flex;flex-direction:column;align-items:center;justify-content:center;padding:24px;text-align:center;">
<span style="font-size:48px;margin-bottom:12px;filter:drop-shadow(0 4px 12px rgba(0,0,0,.3));">{emoji}</span>
<span style="font-family:\'Space Grotesk\',sans-serif;font-size:22px;font-weight:700;color:rgba(255,255,255,.9);text-shadow:0 2px 12px rgba(0,0,0,.4);line-height:1.2;">{title}</span>
<span style="font-size:13px;color:rgba(255,255,255,.5);margin-top:8px;">{subtitle}</span>
</div></div>'''

# ============================================================
# HTML TEMPLATE
# ============================================================

def get_nav():
    return f'''<nav class="nav">
  <a href="{URL_BASE}" class="nav-logo">
    <div class="nav-mark">BF</div>
    <div class="logo-text">BF Casino</div>
  </a>
  <div class="nav-links" id="nav-links">
    <a href="{URL_BASE}">Heim</a>
    <a href="{URL_BASE}entertainment/">Afþreying</a>
    <a href="{URL_BASE}casino/">Spilavíti</a>
    <a href="{URL_BASE}slots/">Spilakassar</a>
    <a href="{URL_BASE}bonusy/">Bónusar</a>
    <a href="{URL_BASE}live/">Í beinni</a>
    <a href="{URL_BASE}gajdy/">Leiðbeiningar</a>
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
          <div class="nav-mark" style="width:24px;height:24px;font-size:10px;border-radius:8px;">BF</div>
          <span style="font-family:Space Grotesk,sans-serif;font-size:16px;font-weight:700;color:#fff;">BF Casino</span>
        </div>
        <div class="footer-desc">BF Casino á bestiflokkurinn.is — óháð samanburðarvefur spilavíta. 18+ Spilaðu á ábyrgan hátt.</div>
      </div>
      <div class="footer-cols">
        <div><div class="footer-col-title">SPILAVÍTI</div><a href="{URL_BASE}casino/">Umsagnir</a><a href="{URL_BASE}bonusy/">Bónusar</a><a href="{URL_BASE}casino/crypto-casino/">Dulritunargjaldmiðill</a></div>
        <div><div class="footer-col-title">LEIKIR</div><a href="{URL_BASE}slots/">Spilakassar</a><a href="{URL_BASE}live/">Í beinni</a></div>
        <div><div class="footer-col-title">UPPLÝSINGAR</div><a href="{URL_BASE}o-nas/">Um okkur</a><a href="{URL_BASE}gajdy/">Leiðbeiningar</a><a href="{URL_BASE}platezhi/">Greiðslur</a><a href="{URL_BASE}konfidencialnost/">Persónuvernd</a><a href="#" data-cookie-settings>Vafrakökur</a></div>
      </div>
    </div>
    <div class="footer-help">Þarftu að tala við einhvern um spilavanda? Hjálparsíminn <a href="tel:1717">1717</a> hjá Rauða krossinum er ókeypis og opinn allan sólarhringinn. <a href="{URL_BASE}gajdy/otvetstvennaya-igra/">Ábyrg spilun →</a></div>
    <div class="footer-18">18+ | Fjárhættuspil geta verið ávanabindandi. Spilaðu á ábyrgan hátt. <a href="https://www.begambleaware.org" target="_blank" rel="noopener">BeGambleAware.org</a></div>
    <div class="footer-bottom"><span>© 2026 bestiflokkurinn.is</span><span>BF Casino — óháð umsagnarvefur</span></div>
  </div>
</footer>'''

def page_template(title, desc, breadcrumbs, content, canonical="", og_img="", schema_extra=None, show_byline=True):
    # Byline + affiliate disclosure under the first H1
    if show_byline and '</h1>' in content:
        byline = (f'<div class="byline">BF Casino ritstjórn · Uppfært nóvember 2026 · '
                  f'<a href="{URL_BASE}kak-my-ocenivaem/">Hvernig við metum</a></div>'
                  f'<div class="disclosure">Þessi síða inniheldur samstarfstengla. Við gætum fengið þóknun ef þú skráir þig, '
                  f'en það hefur ekki áhrif á einkunnir okkar. 18+</div>')
        content = content.replace('</h1>', '</h1>\n' + byline, 1)
    # JSON-LD
    site = "https://bestiflokkurinn.is"
    def abs_url(u):
        u = u.replace("{URL_BASE}", "/").replace(URL_BASE, "/")
        return site + (u if u.startswith("/") else "/" + u)
    crumbs = [{"@type":"ListItem","position":i+1,"name":n,**({"item":abs_url(u)} if u else {})} for i,(u,n) in enumerate(breadcrumbs)]
    graph = [
        {"@type":"WebSite","@id":site+"/#website","name":"BF Casino","url":site+"/","inLanguage":"is"},
        {"@type":"Organization","@id":site+"/#org","name":"BF Casino ritstjórn","url":site+"/"},
        {"@type":"Article","headline":title[:110],"description":desc,"inLanguage":"is",
         "datePublished":"2026-06-01","dateModified":"2026-11-14",
         "author":{"@id":site+"/#org"},"publisher":{"@id":site+"/#org"}},
        {"@type":"BreadcrumbList","itemListElement":crumbs},
    ] + (schema_extra or [])
    schema_json = json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False).replace("</","<\\/")
    bc_html = ' → '.join([f'<a href="{url.replace("{URL_BASE}", URL_BASE)}">{name}</a>' for url, name in breadcrumbs])
    site_url = "https://bestiflokkurinn.is"
    og_image = og_img if og_img else f"{site_url}/img/og-default.jpg"
    return f'''<!DOCTYPE html>
<html lang="is">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | BF Casino</title>
<meta name="description" content="{desc}">
{f'<link rel="canonical" href="{canonical}">' if canonical else ''}
<!-- Favicon -->
<link rel="icon" type="image/svg+xml" href="{URL_BASE}favicon.svg">
<link rel="icon" type="image/png" sizes="32x32" href="{URL_BASE}favicon-32.png">
<!-- Open Graph -->
<meta property="og:type" content="website">
<meta property="og:title" content="{title} | BF Casino">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="{og_image}">
<meta property="og:locale" content="is_IS">
<meta property="og:site_name" content="BF Casino — Bestiflokkurinn.is">
<meta name="twitter:card" content="summary_large_image">
<!-- Hreflang -->
<link rel="alternate" hreflang="is" href="{site_url}/">
<link rel="alternate" hreflang="x-default" href="{site_url}/">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#0c0618;--bg2:#140e28;--bg3:#1a1235;--card:rgba(25,15,50,.55);--border:rgba(140,100,220,.1);--border2:rgba(140,100,220,.2);--purple:#8040e0;--violet:#c060ff;--blue:#80b0ff;--accent:#c080ff;--accent-bg:rgba(140,80,240,.06);--gold:#f0c050;--text:#c4b8e8;--text2:#9a8cc0;--muted:rgba(180,160,220,.85);--muted2:rgba(140,120,180,.6);--warm1:#2a1040;--warm2:#1a0830;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{background:var(--bg);color:var(--text);font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}}
a{{text-decoration:none;color:inherit;}}
/* Ambient orbs */
body::before{{content:'';position:fixed;top:-200px;right:-5%;width:500px;height:500px;background:radial-gradient(circle,rgba(120,60,220,.12) 0%,transparent 70%);pointer-events:none;z-index:0;filter:blur(40px);animation:orbDrift 10s ease-in-out infinite;}}
body::after{{content:'';position:fixed;bottom:-200px;left:-10%;width:600px;height:600px;background:radial-gradient(circle,rgba(80,40,180,.08) 0%,transparent 70%);pointer-events:none;z-index:0;filter:blur(40px);animation:orbDrift 12s ease-in-out 3s infinite;}}
@keyframes orbDrift{{0%,100%{{transform:translate(0,0);}}50%{{transform:translate(25px,-20px);}}}}
@keyframes shimmerLine{{0%{{background-position:200% 0;}}100%{{background-position:-200% 0;}}}}
@keyframes btnShine{{0%{{left:-100%;}}100%{{left:200%;}}}}
@keyframes fadeUp{{from{{opacity:0;transform:translateY(16px);}}to{{opacity:1;transform:translateY(0);}}}}
/* Top accent line */
.top-accent{{height:3px;background:linear-gradient(90deg,#8040e0,#c060ff,#80b0ff,#c060ff,#8040e0);background-size:200% 100%;animation:shimmerLine 4s linear infinite;}}
/* Nav */
.nav{{background:rgba(10,6,24,.88);padding:12px 30px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100;backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);}}
.nav-logo{{display:flex;align-items:center;gap:10px;}}
.nav-mark{{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,#8040e0,#c060ff);display:flex;align-items:center;justify-content:center;font-family:'Space Grotesk',sans-serif;font-size:13px;font-weight:700;color:#fff;box-shadow:0 2px 12px rgba(140,60,240,.25);}}
.logo-text{{font-family:'Space Grotesk',sans-serif;font-size:18px;font-weight:700;color:#fff;}}
.nav-links{{display:flex;gap:20px;font-size:13px;font-weight:500;}}
.nav-links a{{color:var(--muted);transition:color .2s;}}
.nav-links a:hover{{color:#e0c0ff;}}
.nav-actions{{display:flex;gap:8px;align-items:center;}}
/* Liquid glass nav button */
.btn-signup{{display:inline-flex;align-items:center;background:linear-gradient(135deg,rgba(140,60,240,.2),rgba(200,100,255,.1));backdrop-filter:blur(8px);border:1px solid rgba(180,140,255,.2);color:#e0c0ff;padding:8px 22px;border-radius:20px;font-size:13px;font-weight:600;transition:all .25s;position:relative;overflow:hidden;box-shadow:0 2px 12px rgba(140,60,240,.1),inset 0 1px 0 rgba(255,255,255,.06);}}
.btn-signup::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.06),transparent);pointer-events:none;border-radius:20px 20px 0 0;}}
.btn-signup:hover{{background:linear-gradient(135deg,rgba(140,60,240,.35),rgba(200,100,255,.2));border-color:rgba(180,140,255,.4);color:#fff;box-shadow:0 4px 20px rgba(140,60,240,.25),inset 0 1px 0 rgba(255,255,255,.1);transform:translateY(-1px);}}
/* Breadcrumbs */
.breadcrumbs{{padding:14px 30px;font-size:11px;color:var(--muted2);border-bottom:1px solid var(--border);}}
.breadcrumbs a{{color:var(--muted);transition:color .15s;}}
.breadcrumbs a:hover{{color:#c080ff;}}
/* Layout */
.page-wrap{{max-width:1100px;margin:0 auto;padding:40px 30px 60px;display:grid;grid-template-columns:1fr 280px;gap:40px;position:relative;z-index:1;}}
.content{{animation:fadeUp .5s ease-out;}}
.content h1{{font-family:'Space Grotesk',sans-serif;font-size:32px;font-weight:700;margin-bottom:20px;line-height:1.2;color:#fff;}}
.content h2{{font-family:'Space Grotesk',sans-serif;font-size:21px;font-weight:700;margin:32px 0 14px;color:#e0d0f8;position:relative;padding-left:16px;}}
.content h2::before{{content:'';position:absolute;left:0;top:4px;bottom:4px;width:3px;border-radius:2px;background:linear-gradient(180deg,#8040e0,#c060ff);}}
.content h3{{font-size:16px;font-weight:600;margin:24px 0 10px;color:var(--text);}}
.content p{{color:var(--muted);font-size:15px;line-height:1.8;margin-bottom:16px;}}
.content ul,.content ol{{color:var(--muted);font-size:15px;line-height:1.8;margin:0 0 16px 20px;}}
.content li{{margin-bottom:8px;}}
.content a{{color:#c080ff;font-weight:500;transition:color .15s;}}
.content a:hover{{color:#e0c0ff;}}
/* Sidebar */
.sidebar{{animation:fadeUp .5s ease-out .1s both;}}
.sidebar-card{{background:var(--card);backdrop-filter:blur(12px);border:1px solid var(--border);border-radius:16px;padding:20px;margin-bottom:16px;position:relative;overflow:hidden;}}
.sidebar-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#8040e0,#c060ff);}}
.sidebar-card h4{{font-family:'Space Grotesk',sans-serif;font-size:14px;font-weight:700;color:#e0d0f8;margin-bottom:12px;}}
.sidebar-card a{{display:block;color:var(--muted);font-size:12px;line-height:2;transition:color .15s;}}
.sidebar-card a:hover{{color:#c080ff;}}
.sidebar-cta{{display:block;text-align:center;background:linear-gradient(135deg,rgba(140,60,240,.25),rgba(200,100,255,.12));backdrop-filter:blur(12px);color:#fff;padding:14px;border-radius:16px;font-size:13px;font-weight:700;border:1px solid rgba(180,140,255,.2);transition:all .3s;position:relative;overflow:hidden;box-shadow:0 4px 20px rgba(130,60,230,.15);}}
.sidebar-cta::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.06),transparent);pointer-events:none;border-radius:16px 16px 0 0;}}
.sidebar-cta:hover{{transform:translateY(-2px);box-shadow:0 6px 28px rgba(130,60,230,.25);border-color:rgba(180,140,255,.35);}}
/* Slot hero image */
.slot-hero{{width:100%;max-width:400px;aspect-ratio:4/3;border-radius:16px;overflow:hidden;margin:0 0 24px;border:1px solid var(--border2);transition:all .3s;box-shadow:0 4px 24px rgba(100,40,200,.12);position:relative;}}
.slot-hero::after{{content:'';position:absolute;inset:0;border-radius:16px;box-shadow:inset 0 -40px 40px -20px rgba(10,6,24,.6);pointer-events:none;}}
.slot-hero:hover{{border-color:rgba(180,140,255,.3);box-shadow:0 8px 36px rgba(100,40,200,.2);}}
.slot-hero-bg{{width:100%;height:100%;}}
.slot-hero-img{{width:100%;height:100%;object-fit:cover;display:block;}}
/* Info cards */
.info-box{{background:var(--card);backdrop-filter:blur(12px);border:1px solid var(--border);border-radius:16px;padding:20px 24px;margin:16px 0;transition:all .3s;position:relative;overflow:hidden;}}
.info-box::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.02),transparent);pointer-events:none;border-radius:16px 16px 0 0;}}
.info-box:hover{{border-color:var(--border2);box-shadow:0 4px 24px rgba(100,40,200,.1);transform:translateY(-2px);}}
.info-box p{{margin-bottom:6px;}}
.info-box p:last-child{{margin-bottom:0;}}
.info-box strong{{color:#fff;}}
.info-box a{{color:#c080ff;}}
/* Rating */
.rating-box{{display:inline-flex;align-items:center;gap:10px;background:rgba(140,60,240,.08);border:1px solid rgba(140,60,240,.15);border-radius:14px;padding:12px 24px;margin:12px 0;}}
.rating-box .score{{font-family:'DM Serif Display',serif;font-size:30px;font-weight:400;background:linear-gradient(135deg,#c080ff,#80b0ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.rating-box .label{{font-size:12px;color:var(--muted);}}
/* CTA */
.cta-box{{text-align:center;margin:36px 0;}}
/* Liquid Glass CTA — convex 3D capsule */
.cta-btn{{display:inline-block;background:linear-gradient(180deg,rgba(160,80,255,.35) 0%,rgba(120,50,220,.2) 100%);backdrop-filter:blur(14px);color:#fff;padding:18px 48px;border-radius:28px;font-size:15px;font-weight:700;letter-spacing:.3px;transition:all .3s;position:relative;overflow:hidden;border:1px solid rgba(200,160,255,.25);box-shadow:0 6px 28px rgba(130,60,230,.25),0 2px 0 rgba(255,255,255,.04) inset,0 -4px 16px rgba(100,40,200,.15);}}
.cta-btn::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.12),transparent);pointer-events:none;border-radius:28px 28px 0 0;}}
.cta-btn::after{{content:'';position:absolute;top:0;left:-100%;width:60%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.08),transparent);pointer-events:none;}}
.cta-btn:hover{{text-decoration:none;transform:translateY(-3px);box-shadow:0 10px 40px rgba(130,60,230,.4),0 2px 0 rgba(255,255,255,.06) inset,0 -6px 20px rgba(100,40,200,.2);border-color:rgba(200,160,255,.4);}}
.cta-btn:hover::after{{animation:btnShine .6s ease-out;}}
/* Game grid */
.game-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:16px;margin:20px 0;}}
.game-card{{background:var(--card);backdrop-filter:blur(8px);border:1px solid var(--border);border-radius:16px;overflow:hidden;transition:all .3s;position:relative;}}
.game-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#8040e0,#c060ff,#80b0ff);opacity:0;transition:opacity .3s;z-index:1;}}
.game-card:hover{{transform:translateY(-5px);border-color:rgba(180,140,255,.25);box-shadow:0 10px 32px rgba(100,40,200,.18);}}
.game-card:hover::before{{opacity:1;}}
.game-card-thumb{{width:100%;aspect-ratio:4/3;background-size:cover;background-position:center;}}
.game-card-info{{padding:12px 14px;}}
.game-card-name{{font-size:13px;font-weight:600;color:#fff;}}
.game-card-prov{{font-size:11px;color:var(--muted);margin-top:2px;}}
.byline{{font-size:13px;color:var(--muted);margin:-8px 0 8px;}}
.byline a{{color:#c080ff;}}
.disclosure{{font-size:12px;color:var(--muted2);margin-bottom:20px;padding:8px 12px;border-left:2px solid rgba(140,100,220,.3);background:rgba(140,80,240,.04);border-radius:0 8px 8px 0;}}
.footer-help{{text-align:center;font-size:13px;color:var(--text);margin-bottom:10px;}}
.footer-help a{{color:#fff;font-weight:700;}}
/* Share buttons */
.share{{margin:36px 0 8px;padding-top:22px;border-top:1px solid var(--border);display:flex;align-items:center;gap:14px;flex-wrap:wrap;}}
.share-label{{font-size:14px;color:var(--muted);margin-right:4px;}}
.share a{{position:relative;width:48px;height:48px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;transition:transform .2s,box-shadow .2s;box-shadow:0 4px 14px rgba(0,0,0,.35);}}
.share a::before{{content:'';position:absolute;top:-4px;left:0;width:48px;height:22px;background:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 -4 48 22'%3E%3Cpath fill='white' d='M3.5 11.5 A21 21 0 0 1 44.5 11.5 Q43 14.5 40.5 12.8 Q39.5 17.5 37 13.2 Q34 15 31.5 13 Q30 19 27.5 13.3 Q24.5 15.5 22 13.2 Q20.5 16.5 18 13 Q15 15.5 12.5 12.8 Q11 18 8.5 12.6 Q6 14.5 3.5 11.5 Z'/%3E%3C/svg%3E") no-repeat center/100% 100%;filter:drop-shadow(0 1px 1px rgba(0,0,0,.25));pointer-events:none;}}
.share a:hover{{transform:translateY(-3px);box-shadow:0 8px 20px rgba(0,0,0,.45);}}
.share a:focus-visible{{outline:2px solid #c080ff;outline-offset:3px;}}
.share svg{{width:22px;height:22px;fill:#fff;position:relative;}}
.share .s-fb{{background:#3b5998;}}
.share .s-in{{background:#4a77b8;}}
.share .s-wa{{background:#5dc46b;}}
.share .s-copy{{background:#5a3aa8;}}
/* Footer */
.footer{{background:rgba(6,4,18,.85);padding:28px 30px 14px;border-top:1px solid var(--border);position:relative;z-index:1;}}
.footer-inner{{max-width:1100px;margin:0 auto;}}
.footer-top{{display:flex;justify-content:space-between;margin-bottom:18px;gap:30px;}}
.footer-brand{{max-width:280px;}}
.footer-desc{{color:var(--muted2);font-size:10px;line-height:1.6;margin-top:6px;}}
.footer-cols{{display:flex;gap:30px;}}
.footer-col-title{{color:var(--muted2);font-size:9px;letter-spacing:1.5px;font-weight:600;margin-bottom:6px;}}
.footer-cols a{{display:block;color:var(--muted);font-size:11px;line-height:2.2;transition:color .15s;}}
.footer-cols a:hover{{color:#c080ff;}}
.footer-18{{text-align:center;padding:14px;border:1px solid var(--border);border-radius:12px;background:var(--bg2);margin-bottom:12px;font-size:12px;color:var(--muted2);}}
.footer-18 a{{color:#c080ff;}}
.footer-bottom{{border-top:1px solid var(--border);padding-top:10px;display:flex;justify-content:space-between;color:var(--muted2);font-size:9px;}}
@media(max-width:768px){{
  .page-wrap{{grid-template-columns:1fr;gap:24px;padding:24px 16px 40px;}}
  .nav{{padding:10px 16px;flex-wrap:wrap;gap:8px;}}
  .nav-links{{gap:16px;font-size:13px;width:100%;overflow-x:auto;white-space:nowrap;padding-bottom:4px;scrollbar-width:none;}}
  .nav-links::-webkit-scrollbar{{display:none;}}
  .content h1{{font-size:26px;}}
  .footer-top{{flex-direction:column;gap:14px;}}
  .game-grid{{grid-template-columns:repeat(2,1fr);}}
  .sidebar{{order:2;}}
}}
/* === Liquid glass capsule buttons === */
.btn-primary,.btn-secondary,.nav-cta,.btn-cta,.btn-glass,.promo-btn,.gc-play,.btn-signup,.cta-btn,.sidebar-cta{{
--rim:6px;position:relative;display:inline-flex;align-items:center;justify-content:center;gap:8px;
color:#fff!important;font-family:'Inter',system-ui,sans-serif;white-space:nowrap;font-weight:500;letter-spacing:.2px;
text-shadow:0 1px 2px rgba(0,0,0,.45);border-radius:999px;overflow:visible;isolation:isolate;
border:var(--rim) solid transparent;background-clip:padding-box;
background:
 radial-gradient(70% 95% at 14% 108%,rgba(255,165,60,1) 0%,rgba(255,120,50,.55) 35%,transparent 70%) padding-box,
 radial-gradient(85% 100% at 72% 112%,rgba(240,80,215,1) 0%,rgba(205,60,205,.55) 38%,transparent 72%) padding-box,
 linear-gradient(180deg,#24092a 0%,#34103c 45%,#5a1d68 100%) padding-box,
 linear-gradient(170deg,rgba(255,255,255,.85) 0%,rgba(255,255,255,.18) 35%,rgba(255,255,255,.08) 60%,rgba(255,190,150,.6) 100%) border-box;
box-shadow:
 0 0 0 1px rgba(255,255,255,.28),
 inset 0 0 0 1px rgba(255,255,255,.22),
 inset 0 4px 8px rgba(0,0,0,.45),
 inset 0 -4px 10px rgba(255,170,90,.35),
 0 14px 26px -10px rgba(225,60,200,.65),
 0 10px 22px -12px rgba(255,140,40,.6),
 0 2px 6px rgba(0,0,0,.35);
backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
transition:transform .25s,box-shadow .25s,filter .25s;}}
.btn-primary::before,.btn-secondary::before,.nav-cta::before,.btn-cta::before,.btn-glass::before,.promo-btn::before,.gc-play::before,.btn-signup::before,.cta-btn::before,.sidebar-cta::before{{
content:'';position:absolute;left:7%;right:7%;top:2px;height:16%;border-radius:999px;pointer-events:none;z-index:-1;
background:linear-gradient(180deg,rgba(255,255,255,.55),rgba(255,255,255,0));}}
.btn-primary::after,.btn-secondary::after,.nav-cta::after,.btn-cta::after,.btn-glass::after,.promo-btn::after,.gc-play::after,.btn-signup::after,.cta-btn::after,.sidebar-cta::after{{
content:'';position:absolute;left:6%;bottom:2px;width:30%;height:22%;border-radius:999px;pointer-events:none;z-index:-1;animation:none;
background:radial-gradient(closest-side,rgba(255,210,140,.7),transparent);}}
.btn-primary:hover,.btn-secondary:hover,.nav-cta:hover,.btn-cta:hover,.btn-glass:hover,.promo-btn:hover,.gc-play:hover,.btn-signup:hover,.cta-btn:hover,.sidebar-cta:hover{{
transform:translateY(-2px);filter:brightness(1.12) saturate(1.1);
box-shadow:0 0 0 1px rgba(255,255,255,.45),inset 0 1px 0 rgba(255,255,255,.45),inset 0 -3px 8px rgba(255,170,90,.35),0 18px 32px -10px rgba(225,60,200,.8),0 14px 26px -12px rgba(255,140,40,.75),0 3px 8px rgba(0,0,0,.35);}}
.btn-primary:focus-visible,.btn-secondary:focus-visible,.nav-cta:focus-visible,.btn-cta:focus-visible,.btn-glass:focus-visible,.promo-btn:focus-visible,.gc-play:focus-visible,.btn-signup:focus-visible,.cta-btn:focus-visible,.sidebar-cta:focus-visible{{outline:2px solid #ffb86b;outline-offset:4px;}}
.btn-primary,.btn-cta,.cta-btn{{padding:14px 40px;font-size:16px;}}
.sidebar-cta{{display:flex;padding:12px 20px;font-size:15px;}}
.nav-cta,.btn-glass,.btn-signup,.btn-secondary,.promo-btn{{--rim:4px;padding:8px 22px;font-size:14px;}}
.gc-play{{--rim:4px;display:flex;margin:0 12px 14px;padding:9px 0;font-size:14px;}}
.btn-secondary .play-icon{{background:rgba(255,255,255,.15);}}
@media (prefers-reduced-motion:reduce){{.btn-primary,.btn-cta,.cta-btn,.btn-glass,.btn-signup,.sidebar-cta,.nav-cta,.btn-secondary,.promo-btn,.gc-play{{transition:none;}}}}
/* Cookie banner */
.cookie-banner{{position:fixed;left:16px;right:16px;bottom:16px;z-index:1000;max-width:880px;margin:0 auto;display:flex;align-items:center;gap:20px;padding:18px 22px;border-radius:20px;background:rgba(20,12,38,.94);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid rgba(180,140,255,.22);box-shadow:0 18px 50px rgba(0,0,0,.55);color:#e6dcf8;font-family:'Inter',system-ui,sans-serif;}}
.cookie-banner[hidden]{{display:none;}}
.cookie-text{{flex:1;font-size:14px;line-height:1.55;}}
.cookie-text strong{{display:block;color:#fff;font-size:15px;margin-bottom:4px;}}
.cookie-text a{{color:#d8b4ff;text-decoration:underline;}}
.cookie-actions{{display:flex;gap:10px;flex-shrink:0;}}
.cookie-actions button{{cursor:pointer;min-width:170px;}}
@media(max-width:700px){{.cookie-banner{{flex-direction:column;align-items:stretch;gap:14px;}}.cookie-actions{{flex-direction:column;}}.cookie-actions button{{width:100%;}}}}
/* Burger menu */
.nav-burger{{display:none;width:44px;height:44px;border-radius:12px;border:1px solid rgba(180,140,255,.25);background:rgba(30,18,60,.7);cursor:pointer;flex-direction:column;align-items:center;justify-content:center;gap:5px;padding:0;margin-left:10px;}}
.nav-burger span{{display:block;width:20px;height:2px;border-radius:2px;background:#e8dcff;transition:transform .25s,opacity .2s;}}
.nav-burger:focus-visible{{outline:2px solid #ffb86b;outline-offset:2px;}}
.nav.open .nav-burger span:nth-child(1){{transform:translateY(7px) rotate(45deg);}}
.nav.open .nav-burger span:nth-child(2){{opacity:0;}}
.nav.open .nav-burger span:nth-child(3){{transform:translateY(-7px) rotate(-45deg);}}
.nav-right{{display:flex;align-items:center;}}
@media(max-width:768px){{
 .nav{{flex-wrap:nowrap!important;padding:10px 16px!important;gap:10px;}}
 .nav-burger{{display:flex;}}
 .nav-links{{display:none!important;position:absolute;top:100%;left:0;right:0;flex-direction:column;gap:0!important;width:auto!important;overflow:visible!important;white-space:normal!important;padding:8px 20px 20px!important;background:rgba(14,8,30,.97);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);border-bottom:1px solid rgba(180,140,255,.18);box-shadow:0 20px 40px rgba(0,0,0,.5);z-index:200;}}
 .nav.open .nav-links{{display:flex!important;animation:navDrop .22s ease-out;}}
 .nav-links a{{padding:15px 4px;font-size:17px!important;color:#e8dcff!important;border-bottom:1px solid rgba(180,140,255,.12);}}
 .nav-links a:last-child{{border-bottom:none;}}
 .nav-logo .logo-text,.nav-brand,.logo-t{{font-size:16px;}}
}}
@keyframes navDrop{{from{{opacity:0;transform:translateY(-8px);}}to{{opacity:1;transform:none;}}}}
@media (prefers-reduced-motion:reduce){{.nav.open .nav-links{{animation:none;}}.nav-burger span{{transition:none;}}}}
@media(max-width:768px){{html,body{{overflow-x:hidden;}}.hero-buttons{{flex-wrap:wrap;}}.btn-primary,.btn-secondary,.btn-cta,.cta-btn{{max-width:100%;white-space:normal;text-align:center;}}}}
/* Drawer menu */
.dr-overlay{{position:fixed;inset:0;background:rgba(5,2,14,.6);backdrop-filter:blur(3px);z-index:999;opacity:0;transition:opacity .25s;}}
.dr-overlay.on{{opacity:1;}}
.dr{{position:fixed;top:0;left:0;bottom:0;width:min(88vw,400px);z-index:1001;display:flex;flex-direction:column;background:linear-gradient(180deg,#1c0f36 0%,#150b2b 100%);border-right:1px solid rgba(180,140,255,.18);box-shadow:20px 0 60px rgba(0,0,0,.55);transform:translateX(-105%);transition:transform .3s cubic-bezier(.2,.8,.2,1);font-family:'Inter',system-ui,sans-serif;color:#ece4ff;}}
.dr.on{{transform:none;}}
.dr-head{{display:flex;align-items:center;gap:14px;padding:18px 18px 16px 22px;border-bottom:1px solid rgba(180,140,255,.14);}}
.dr-brand{{display:flex;align-items:center;gap:10px;text-decoration:none;}}
.dr-mark{{width:36px;height:36px;border-radius:10px;background:linear-gradient(135deg,#8040e0,#c060ff);display:flex;align-items:center;justify-content:center;font-weight:800;font-size:13px;color:#fff;}}
.dr-name{{font-family:'Space Grotesk',sans-serif;font-size:20px;font-weight:700;color:#fff;letter-spacing:-.2px;}}
.dr-name b{{color:#ff9f4a;font-weight:700;}}
.dr [hidden]{{display:none!important;}}
.dr-name b{{margin-left:5px;}}

.dr-title{{font-size:20px;color:rgba(236,228,255,.6);}}
.dr-close{{margin-left:auto;width:46px;height:46px;border-radius:50%;border:1px solid rgba(255,255,255,.2);background:rgba(255,255,255,.07);color:#fff;display:flex;align-items:center;justify-content:center;cursor:pointer;}}
.dr-close svg{{width:20px;height:20px;}}
.dr-body{{flex:1;overflow-y:auto;padding:14px 14px 20px;overscroll-behavior:contain;}}
.dr-item{{width:100%;display:flex;align-items:center;gap:16px;padding:14px 18px;margin:2px 0;border:0;border-radius:999px;background:none;color:#ece4ff;font:500 18px/1.2 'Inter',system-ui,sans-serif;text-align:left;text-decoration:none;cursor:pointer;transition:background .2s,color .2s;}}
.dr-item:hover{{background:rgba(255,255,255,.06);}}
.dr-item:focus-visible,.dr-sub a:focus-visible,.dr-close:focus-visible{{outline:2px solid #ff9f4a;outline-offset:2px;}}
.dr-ic{{width:24px;height:24px;flex-shrink:0;color:#c9b2ff;}}
.dr-item span{{flex:1;}}
.dr-badge{{font-style:normal;min-width:30px;height:28px;padding:0 9px;border-radius:9px;background:linear-gradient(135deg,#ff8a3d,#e8505b);color:#fff;font-size:14px;font-weight:700;display:inline-flex;align-items:center;justify-content:center;}}
.dr-chev{{width:20px;height:20px;color:rgba(236,228,255,.6);transition:transform .25s;}}
.dr-toggle[aria-expanded="true"]{{background:#fff;color:#1a0d30;box-shadow:0 8px 24px rgba(0,0,0,.35);}}
.dr-toggle[aria-expanded="true"] .dr-ic{{color:#1a0d30;}}
.dr-toggle[aria-expanded="true"] .dr-chev{{transform:rotate(180deg);color:#1a0d30;}}
.dr-sub{{margin:6px 0 10px 36px;padding-left:18px;border-left:2px solid rgba(180,140,255,.25);}}
.dr-sub a{{display:flex;align-items:center;gap:14px;padding:12px 10px;border-radius:12px;color:rgba(236,228,255,.85);font-size:16px;text-decoration:none;}}
.dr-sub a:hover{{background:rgba(255,255,255,.05);color:#fff;}}
.dr-fold{{width:20px;height:20px;flex-shrink:0;color:rgba(201,178,255,.7);}}
.dr-empty{{padding:16px 18px;color:rgba(236,228,255,.6);font-size:15px;}}
.dr-foot{{padding:14px 18px 18px;border-top:1px solid rgba(180,140,255,.14);background:rgba(10,5,22,.5);}}
.dr-search{{display:flex;align-items:center;gap:12px;padding:14px 22px;border-radius:999px;background:linear-gradient(135deg,#ff8a3d,#e0506a);box-shadow:0 10px 24px -8px rgba(255,120,60,.6);cursor:text;}}
.dr-search svg{{width:22px;height:22px;color:#fff;flex-shrink:0;}}
.dr-search input{{flex:1;min-width:0;border:0;background:none;color:#fff;font:600 17px 'Inter',system-ui,sans-serif;outline:none;}}
.dr-search input::placeholder{{color:rgba(255,255,255,.9);}}
.dr-rg{{margin-top:12px;text-align:center;font-size:14px;color:rgba(236,228,255,.7);}}
.dr-rg a{{color:#fff;font-weight:700;}}
.dr-18{{display:inline-flex;align-items:center;justify-content:center;padding:3px 9px;border-radius:999px;background:#d8394a;color:#fff;font-weight:800;font-size:13px;margin-right:4px;}}
body.dr-lock{{overflow:hidden;}}
@media(min-width:769px){{.dr,.dr-overlay{{display:none!important;}}}}
@media (prefers-reduced-motion:reduce){{.dr,.dr-overlay,.dr-chev{{transition:none;}}}}
</style>
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
<a href="{URL_BASE}casino/bitstarz/">BitStarz — 5 BTC + 200 FS</a>
<a href="{URL_BASE}casino/stake/">Stake — 200% + VIP</a>
<a href="{URL_BASE}casino/bc-game/">BC.Game — 300% allt að 1 BTC</a>
<a href="{URL_BASE}casino/katsubet/">KatsuBet — 100% + 100 FS</a>
<a href="{URL_BASE}casino/winz/">Winz.io — 300 FS án veðskilyrða</a>
</div>
<a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="sidebar-cta">Spila núna →</a>
<div class="sidebar-card" style="margin-top:16px;">
<h4>📖 Leiðbeiningar</h4>
<a href="{URL_BASE}gajdy/kak-vybrat-casino/">Hvernig á að velja spilavíti</a>
<a href="{URL_BASE}gajdy/chto-takoe-rtp/">Hvað er RTP?</a>
<a href="{URL_BASE}gajdy/chto-takoe-volatilnost/">Hvað er sveifla?</a>
<a href="{URL_BASE}gajdy/framhja-bankalokun/">Framhjá bankalokun</a>
<a href="{URL_BASE}gajdy/kaupa-bitcoin-island/">Kaupa Bitcoin á Íslandi</a>
<a href="{URL_BASE}gajdy/besta-crypto-spilaviti-island/">Besta crypto spilavítið</a>
<a href="{URL_BASE}gajdy/spilaviti-samanburdur/">Spilavíti samanburður</a>
<a href="{URL_BASE}gajdy/frisnuningar-an-innborgunar/">Frísnúningar án innborgunar</a>
</div>
<div class="sidebar-card">
<h4>🎰 Vinsælir spilakassar</h4>
<a href="{URL_BASE}slots/gates-of-olympus/">Gates of Olympus</a>
<a href="{URL_BASE}slots/sweet-bonanza/">Sweet Bonanza</a>
<a href="{URL_BASE}slots/book-of-dead/">Book of Dead</a>
<a href="{URL_BASE}slots/big-bass-splash/">Big Bass Splash</a>
</div>
</aside>
</div>
{get_footer()}
<script type="application/ld+json">{schema_json}</script>
<script>document.querySelectorAll('img[loading]').length||document.querySelectorAll('.slot-hero-img,.game-card-thumb img').forEach(function(i){{i.loading='lazy'}})</script>
<script>(function(){{var u=encodeURIComponent(location.href),t=encodeURIComponent(document.title);var m={{fb:'https://www.facebook.com/sharer/sharer.php?u='+u,in:'https://www.linkedin.com/sharing/share-offsite/?url='+u,wa:'https://wa.me/?text='+t+'%20'+u}};document.querySelectorAll('.share a').forEach(function(a){{var n=a.dataset.net;if(m[n])a.href=m[n];else if(n==='copy')a.addEventListener('click',function(e){{e.preventDefault();try{{navigator.clipboard.writeText(location.href);a.setAttribute('aria-label','Tengill afritaður');a.style.background='#2f8f5a';setTimeout(function(){{a.style.background='';}},1500);}}catch(_){{}}}});}});}})();</script>
<div id="cookie-banner" class="cookie-banner" role="dialog" aria-live="polite" aria-label="Vafrakökur" hidden>
<div class="cookie-text"><strong>🍪 Vafrakökur</strong><span>Við notum nauðsynlegar vafrakökur til að vefurinn virki og til að muna val þitt. Ef þú samþykkir allar má nota kökur til að mæla umferð. Samstarfstenglar geta sett kökur hjá þriðja aðila þegar þú smellir á þá. <a href="{URL_BASE}konfidencialnost/">Persónuverndarstefna</a></span></div>
<div class="cookie-actions"><button type="button" class="btn-signup" data-consent="necessary">Aðeins nauðsynlegar</button><button type="button" class="btn-signup" data-consent="all">Samþykkja allar</button></div>
</div>
<script>(function(){{var b=document.getElementById('cookie-banner');if(!b)return;var v=null;try{{v=localStorage.getItem('bf_cookie_consent');}}catch(e){{}}if(!v)b.hidden=false;b.querySelectorAll('[data-consent]').forEach(function(btn){{btn.addEventListener('click',function(){{try{{localStorage.setItem('bf_cookie_consent',btn.getAttribute('data-consent'));}}catch(e){{}}b.hidden=true;}});}});document.querySelectorAll('[data-cookie-settings]').forEach(function(a){{a.addEventListener('click',function(e){{e.preventDefault();b.hidden=false;}});}});}})();</script>

<div class="dr-overlay" data-dr-close hidden></div><aside class="dr" id="site-drawer" aria-label="Valmynd" aria-hidden="true" inert><div class="dr-head"><a href="{URL_BASE}" class="dr-brand"><span class="dr-mark">BF</span><span class="dr-name">BF<b>Casino</b></span></a><span class="dr-title">Valmynd</span><button class="dr-close" type="button" data-dr-close aria-label="Loka valmynd"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></div><nav class="dr-body"><a class="dr-item" href="{URL_BASE}"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/></svg><span>Heim</span></a><a class="dr-item" href="{URL_BASE}entertainment/"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l2.6 5.6 6 .6-4.5 4 1.3 6L12 16.8 6.6 19.2l1.3-6-4.5-4 6-.6z"/></svg><span>Afþreying</span></a><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg0"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8" cy="8" r="1.3"/><circle cx="16" cy="8" r="1.3"/><circle cx="12" cy="12" r="1.3"/><circle cx="8" cy="16" r="1.3"/><circle cx="16" cy="16" r="1.3"/></svg><span>Spilavíti</span><em class="dr-badge">7</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg0" hidden><a href="{URL_BASE}casino/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allar umsagnir</span></a><a href="{URL_BASE}gajdy/spilaviti-samanburdur/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Spilavíti samanburður</span></a><a href="{URL_BASE}gajdy/besta-crypto-spilaviti-island/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Besta crypto spilavítið</span></a><a href="{URL_BASE}casino/crypto-casino/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Crypto spilavíti</span></a><a href="{URL_BASE}casino/novye-casino/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Ný spilavíti 2026</span></a><a href="{URL_BASE}gajdy/spilaviti-islenskt-vidmot/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Íslenskt viðmót</span></a><a href="{URL_BASE}kak-my-ocenivaem/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Hvernig við metum</span></a></div></div><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg1"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="3"/><path d="M9 4v16M15 4v16"/></svg><span>Spilakassar</span><em class="dr-badge">6</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg1" hidden><a href="{URL_BASE}slots/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allir spilakassar</span></a><a href="{URL_BASE}slots/gates-of-olympus/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Gates of Olympus</span></a><a href="{URL_BASE}slots/sweet-bonanza/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Sweet Bonanza</span></a><a href="{URL_BASE}slots/book-of-dead/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Book of Dead</span></a><a href="{URL_BASE}slots/big-bass-splash/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Big Bass Splash</span></a><a href="{URL_BASE}gajdy/chto-takoe-rtp/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Hvað er RTP?</span></a></div></div><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg2"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="12" rx="2"/><path d="M8 21h8M12 17v4"/><circle cx="12" cy="11" r="2.5"/></svg><span>Í beinni</span><em class="dr-badge">5</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg2" hidden><a href="{URL_BASE}live/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allir lifandi leikir</span></a><a href="{URL_BASE}live/blackjack/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Blackjack</span></a><a href="{URL_BASE}live/roulette/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Rúletta</span></a><a href="{URL_BASE}live/crazy-time/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Crazy Time</span></a><a href="{URL_BASE}live/lightning-roulette/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Lightning Roulette</span></a></div></div><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg3"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="9" width="18" height="12" rx="2"/><path d="M3 13h18M12 9v12M12 9c-2-4-6-4-6-1s6 1 6 1 6 2 6-1-4-3-6 1"/></svg><span>Bónusar</span><em class="dr-badge">5</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg3" hidden><a href="{URL_BASE}bonusy/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allir bónusar</span></a><a href="{URL_BASE}bonusy/velkomstbonus/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Velkomstbónus</span></a><a href="{URL_BASE}gajdy/frisnuningar-an-innborgunar/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Frísnúningar án innborgunar</span></a><a href="{URL_BASE}bonusy/bezdepozitnye-bonusy/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Bónusar án innborgunar</span></a><a href="{URL_BASE}bonusy/vejer/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Hvað eru veðskilyrði?</span></a></div></div><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg4"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="5" width="20" height="14" rx="3"/><path d="M2 10h20M6 15h4"/></svg><span>Greiðslur</span><em class="dr-badge">7</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg4" hidden><a href="{URL_BASE}platezhi/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allar greiðsluleiðir</span></a><a href="{URL_BASE}gajdy/framhja-bankalokun/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Framhjá bankalokun</span></a><a href="{URL_BASE}gajdy/kaupa-bitcoin-island/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Kaupa Bitcoin á Íslandi</span></a><a href="{URL_BASE}gajdy/islenskir-bankar-spilaviti/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Íslenskir bankar</span></a><a href="{URL_BASE}gajdy/piq-greidslur-island/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>PIQ greiðslur</span></a><a href="{URL_BASE}gajdy/spilaviti-isk-kronur/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Spilavíti sem taka við ISK</span></a><a href="{URL_BASE}platezhi/usdt/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>USDT</span></a></div></div><div class="dr-group"><button class="dr-item dr-toggle" type="button" aria-expanded="false" aria-controls="drg5"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 4h6a3 3 0 0 1 3 3v13a2 2 0 0 0-2-2H4zM20 4h-6a3 3 0 0 0-3 3v13a2 2 0 0 1 2-2h7z"/></svg><span>Leiðbeiningar</span><em class="dr-badge">5</em><svg class="dr-chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg></button><div class="dr-sub" id="drg5" hidden><a href="{URL_BASE}gajdy/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Allar leiðbeiningar</span></a><a href="{URL_BASE}gajdy/zakon-ob-azartnyh-igrah-islandiya/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Lög á Íslandi</span></a><a href="{URL_BASE}gajdy/skattar-spilavinningar-island/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Skattar á vinninga</span></a><a href="{URL_BASE}gajdy/kak-vybrat-casino/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Hvernig á að velja spilavíti</span></a><a href="{URL_BASE}gajdy/otvetstvennaya-igra/"><svg class="dr-fold" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg><span>Ábyrg spilun</span></a></div></div><p class="dr-empty" hidden>Ekkert fannst</p></nav><div class="dr-foot"><label class="dr-search"><svg class="dr-ic" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg><input type="search" placeholder="Leita á vefnum" aria-label="Leita í valmynd" autocomplete="off"></label><div class="dr-rg"><span class="dr-18">18+</span> Spilaðu á ábyrgan hátt · <a href="tel:1717">1717</a></div></div></aside><script>(function(){{var d=document.getElementById('site-drawer');if(!d)return;var o=document.querySelector('.dr-overlay'),b=document.querySelector('.nav-burger'),last=null;
function open(){{last=document.activeElement;o.hidden=false;d.removeAttribute('inert');d.setAttribute('aria-hidden','false');requestAnimationFrame(function(){{o.classList.add('on');d.classList.add('on');}});document.body.classList.add('dr-lock');if(b)b.setAttribute('aria-expanded','true');setTimeout(function(){{d.querySelector('.dr-close').focus();}},50);}}
function close(){{o.classList.remove('on');d.classList.remove('on');d.setAttribute('aria-hidden','true');d.setAttribute('inert','');document.body.classList.remove('dr-lock');if(b)b.setAttribute('aria-expanded','false');setTimeout(function(){{o.hidden=true;}},300);if(last&&last.focus)last.focus();}}
if(b){{b.setAttribute('aria-controls','site-drawer');b.addEventListener('click',function(e){{e.stopImmediatePropagation();d.classList.contains('on')?close():open();}},true);}}
document.querySelectorAll('[data-dr-close]').forEach(function(x){{x.addEventListener('click',close);}});
document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&d.classList.contains('on'))close();}});
d.querySelectorAll('.dr-toggle').forEach(function(t){{t.addEventListener('click',function(){{var on=t.getAttribute('aria-expanded')!=='true';d.querySelectorAll('.dr-toggle').forEach(function(x){{x.setAttribute('aria-expanded','false');document.getElementById(x.getAttribute('aria-controls')).hidden=true;}});t.setAttribute('aria-expanded',on?'true':'false');document.getElementById(t.getAttribute('aria-controls')).hidden=!on;}});}});
var path=location.pathname;d.querySelectorAll('.dr-sub a').forEach(function(a){{if(a.getAttribute('href')===path){{a.setAttribute('aria-current','page');a.style.color='#fff';a.style.fontWeight='600';var t=a.closest('.dr-group').querySelector('.dr-toggle');t.setAttribute('aria-expanded','true');a.parentNode.hidden=false;}}}});
var q=d.querySelector('.dr-search input'),empty=d.querySelector('.dr-empty');q.addEventListener('input',function(){{var v=q.value.trim().toLowerCase(),any=false;d.querySelectorAll('.dr-group').forEach(function(g){{var sub=g.querySelector('.dr-sub'),t=g.querySelector('.dr-toggle'),hit=false;sub.querySelectorAll('a').forEach(function(a){{var m=!v||a.textContent.toLowerCase().indexOf(v)>-1;a.hidden=!m;if(m&&v)hit=true;}});if(v){{g.hidden=!hit;sub.hidden=!hit;t.setAttribute('aria-expanded',hit?'true':'false');if(hit)any=true;}}else{{g.hidden=false;sub.querySelectorAll('a').forEach(function(a){{a.hidden=false;}});sub.hidden=t.getAttribute('aria-expanded')!=='true';}}}});d.querySelectorAll('.dr-body > .dr-item').forEach(function(i){{i.hidden=!!v;}});empty.hidden=!v||any;}});
}})();</script>
</body>
</html>'''


# ============================================================
# PAGE GENERATION
# ============================================================

BASE = "/home/claude/slotoro-site"
count = 0

def write_page(path, html):
    global count
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1

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
<p>{"Tekur við Bitcoin, Ethereum, USDT, Litecoin og öðrum dulritunargjaldmiðlum." if c["type"]=="crypto" else "Tekur við Visa, Mastercard, dulritunargjaldmiðlum og rafrænum veskjum."} Þetta er sérstaklega mikilvægt fyrir íslenska leikmenn þar sem innlendir bankar loka oft á spilavíta-færslur.</p>
<h3>Leikir</h3>
<p>{c["name"]} býður upp á yfir 2000 leiki frá fremstu birgjum: Pragmatic Play, NetEnt, Play'n GO, Microgaming og fleiri.</p>
<h2>Kostir og gallar</h2>
<ul>
<li>✅ {c["bonus"]}</li>
<li>✅ {"Hraðar dulritunarútborganir (skv. rekstraraðila)" if c["type"]=="crypto" else "Nokkrar útborgunarleiðir"}</li>
<li>✅ {"Dulritunargreiðslur án lokunar" if c["type"]=="crypto" else "Fjölbreytt úrval greiðslumáta"}</li>
<li>✅ Stórt safn leikja</li>
<li>⚠️ Athugaðu hvort ISK sé í boði — flest erlend spilavíti nota EUR</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á {c["name"]} →</a></div>'''

    bc = [("{URL_BASE}", "Heim"), ("{URL_BASE}casino/", "Spilavíti"), ("", c["name"])]
    review = {"@type":"Review","itemReviewed":{"@type":"Organization","name":c["name"]},
              "reviewRating":{"@type":"Rating","ratingValue":c["rating"],"bestRating":10,"worstRating":0},
              "author":{"@id":"https://bestiflokkurinn.is/#org"},"inLanguage":"is"}
    html = page_template(f'{c["name"]} umsögn', c["desc"], bc, content, schema_extra=[review])
    write_page(f'casino/{c["slug"]}/index.html', html)

# 2. КАТЕГОРИИ КАЗИНО (50)
print("Generating casino categories...")
for cat in casino_categories:
    top_casinos = casinos[:10]
    cards = ""
    for c in top_casinos:
        cards += f'<div class="info-box"><p><strong>{c["name"]}</strong> — {c["bonus"]} (Einkunn: {c["rating"]}/10) <a href="{URL_BASE}casino/{c["slug"]}/">Umsögn →</a></p></div>\n'

    hero = make_hero(cat["title"], "Spilavítaflokkur", "🏆", "#180840", "#3018a0", "#5030e0")
    content = f'''<h1>{cat["title"]} á Íslandi 2026</h1>
{hero}
<p>{cat["desc"]}</p>
<h2>Topp 10 spilavíti í flokki</h2>
{cards}
<h2>Hvernig við veljum bestu spilavítin</h2>
<p>Teymi okkar metur hvert spilavíti út frá nokkrum forsendum: áreiðanleika leyfis, hraða útborgana, gæði leikja, bónustilboðum og aðgengi fyrir íslenska leikmenn.</p>
<p>Við leggjum sérstaka áherslu á stuðning við dulritunargjaldmiðla þar sem íslenskir bankar loka oft á spilavíta-færslur.</p>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}casino/", "Casino"), ("", cat["title"])]
    html = page_template(cat["title"], cat["desc"], bc, content)
    write_page(f'casino/{cat["slug"]}/index.html', html)

# 3. СЛОТЫ (250)
print("Generating slot reviews...")
for s in slots_data:
    cdn_img = f'<div class="slot-hero"><img src="{URL_BASE}img/slots/{s["slug"]}.jpg" alt="{s["name"]}" class="slot-hero-img" loading="lazy"></div>'
    content = f'''<h1>{s["name"]} — Spilakassaumsögn</h1>
{cdn_img}
<div class="info-box">
<p><strong>Birgi:</strong> {s["provider"]}</p>
<p><strong>RTP:</strong> {s["rtp"]}%</p>
<p><strong>Sveifla:</strong> {s["volatility"]}</p>
<p><strong>Hámarksvinninga:</strong> {s["maxwin"]}</p>
<p><strong>Þema:</strong> {s["theme"]}</p>
</div>
<h2>Um {s["name"]}</h2>
<p>{s["name"]} frá {s["provider"]} er einn vinsælasti spilakassinn í «{s["theme"]}» flokknum. Spilakassinn býður upp á {s["volatility"].lower()} sveiflur og hámarksvinninga upp á {s["maxwin"]}.</p>
<h3>RTP og sveifla</h3>
<p>RTP (Return to Player) á {s["name"]} er {s["rtp"]}%. Þetta þýðir að spilakassinn skilar fræðilega {s["rtp"]}% af öllum veðmálum til leikmanna til lengri tíma.</p>
<h3>Hvar á að spila {s["name"]}</h3>
<p>Þessi spilakassi er í boði á eftirfarandi spilavítum sem taka við íslenskum leikmönnum:</p>
<ul>
<li><a href="{URL_BASE}casino/bitstarz/">BitStarz</a> — 5 BTC + 200 FS</li>
<li><a href="{URL_BASE}casino/stake/">Stake</a> — 200% bonus</li>
<li><a href="{URL_BASE}casino/bc-game/">BC.Game</a> — 300% up to 1 BTC</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila {s["name"]} →</a></div>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}slots/", "Slots"), ("", s["name"])]
    html = page_template(f'{s["name"]} spilakassi', f'{s["name"]} frá {s["provider"]} — RTP {s["rtp"]}%, sveifla {s["volatility"]}, hámark {s["maxwin"]}', bc, content)
    write_page(f'slots/{s["slug"]}/index.html', html)

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
<li><a href="{URL_BASE}casino/bitstarz/">BitStarz</a> — besta úrval lifandi leikja</li>
<li><a href="{URL_BASE}casino/stake/">Stake</a> — einkaréttarborð</li>
<li><a href="{URL_BASE}casino/tonybet/">TonyBet</a> — breitt úrval af takmörkunum</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila {g["name"]} →</a></div>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}live/", "Live Casino"), ("", g["name"])]
    html = page_template(f'{g["name"]} Live', g["desc"], bc, content)
    write_page(f'live/{g["slug"]}/index.html', html)

# 5. БОНУСЫ (80)
print("Generating bonus pages...")
for b in bonus_pages:
    hero = make_hero(b["title"], "Bónus 2026", "🎁", "#280840", "#5020a0", "#8040e0")
    content = f'''<h1>{b["title"]}</h1>
{hero}
<p>{b["desc"]}</p>
<h2>Bestu tilboðin 2026</h2>
<div class="info-box">
<p><strong>BitStarz:</strong> 5 BTC + 200 free spins — <a href="{URL_BASE}casino/bitstarz/">Nánari upplýsingar →</a></p>
</div>
<div class="info-box">
<p><strong>BC.Game:</strong> 300% crypto bonus — <a href="{URL_BASE}casino/bc-game/">Nánari upplýsingar →</a></p>
</div>
<h2>Hvernig á að fá bónus</h2>
<p>Til að virkja bónus, skráðu þig á spilavítið, leggðu inn og bónusinn verður sjálfkrafa inneignaður. Athugaðu veðskilyrði.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Fá bónus →</a></div>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}bonusy/", "Bónusar"), ("", b["title"])]
    html = page_template(b["title"], b["desc"], bc, content)
    write_page(f'bonusy/{b["slug"]}/index.html', html)

# 6. ПЛАТЕЖИ (50)
print("Generating payment pages...")
for p in payment_pages:
    hero = make_hero(p["title"], "Greiðslumáti", "💳", "#081828", "#103060", "#2060a0")
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
<li><a href="{URL_BASE}casino/bitstarz/">BitStarz</a> — tafarlausar dulritunarútborganir</li>
<li><a href="{URL_BASE}casino/stake/">Stake</a> — styður 20+ dulritunargjaldmiðla</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Veldu spilavíti →</a></div>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}platezhi/", "Payments"), ("", p["title"])]
    html = page_template(p["title"], p["desc"], bc, content)
    write_page(f'platezhi/{p["slug"]}/index.html', html)

# 7. ГАЙДЫ (60)
print("Generating guides...")
for g in guide_pages:
    hero = make_hero(g["title"], "Leiðbeining", "📖", "#0a1828", "#182850", "#304880")
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
<li>Ráðleggingar frá sérfræðingum BF Casino</li>
</ul>
<h3>Gagnlegir tenglar</h3>
<ul>
<li><a href="{URL_BASE}casino/">Spilavíti umsagnir</a></li>
<li><a href="{URL_BASE}bonusy/">Bónusar</a></li>
<li><a href="{URL_BASE}platezhi/">Greiðslumátar</a></li>
</ul>'''

    bc = [("{URL_BASE}", "Home"), ("{URL_BASE}gajdy/", "Guides"), ("", g["title"])]
    html = page_template(g["title"], g["desc"], bc, content)
    write_page(f'gajdy/{g["slug"]}/index.html', html)

# 8. О НАС (10)
print("Generating about pages...")
about_emojis = {"Um BF Casino":"🏛️","Hafa samband":"📬","Persónuverndarstefna":"🔒","Notkunarskilmálar":"📋","Fyrirvari":"⚖️","Hvernig við metum spilavíti":"⭐","Ritstjórnarstefna":"✍️","Samstarf":"🤝","Vefkort":"🗺️","Ábyrg spilun":"🛡️"}
for a in about_pages:
    emoji = about_emojis.get(a["title"], "ℹ️")
    hero = make_hero(a["title"], "BF Casino", emoji, "#100828", "#201050", "#402080")
    if a["slug"] == "konfidencialnost":
        content = f'''<h1>Persónuverndarstefna</h1>
{hero}
<p>Hér útskýrum við hvaða gögnum er safnað þegar þú notar bestiflokkurinn.is og hvernig vafrakökur eru notaðar.</p>
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
<p>Ísland er aðili að EES og GDPR gildir. Þú getur hvenær sem er breytt vali þínu eða eytt vafragögnum í stillingum vafrans. Spurningar? <a href="{URL_BASE}kontakty/">Hafðu samband</a>.</p>
<p><em>Síðast uppfært: nóvember 2026.</em></p>'''
    elif a["slug"] == "kak-my-ocenivaem":
        content = f'''<h1>Hvernig við metum spilavíti</h1>
{hero}
<p>Hvert spilavíti á BF Casino fær einkunn frá 0 til 10. Einkunnin byggir á sex föstum viðmiðum með birtum vægi, svo þú getir séð nákvæmlega hvernig hún verður til.</p>
<h2>Viðmið og vægi</h2>
<div class="info-box" style="overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;font-size:14px;color:var(--muted);">
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
<p>Ef þú finnur villu, <a href="{URL_BASE}kontakty/">hafðu samband</a>.</p>'''
    else:
        content = f'''<h1>{a["title"]}</h1>
{hero}
<p>{a["desc"]}</p>
<p>BF Casino (bestiflokkurinn.is) er óháð spilavítavefgátt fyrir íslenska leikmenn. Við hjálpum þér að finna áreiðanleg spilavíti með bestu bónusum og stuðningi við dulritunargjaldmiðla.</p>'''

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
        "colors": ("#081828", "#103060", "#2060a0"),
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
<li>Skráðu þig á spilavíti (t.d. <a href="{URL_BASE}casino/bitstarz/">BitStarz</a> eða <a href="{URL_BASE}casino/stake/">Stake</a>)</li>
<li>Farðu í "Innborgun" og veldu Bitcoin eða USDT</li>
<li>Afritaðu veskisáfangastaðinn (wallet address)</li>
<li>Farðu aftur í kauphöllina og sendu fjármunina á þetta heimilisfang</li>
<li>Bíddu 1-10 mínútur — innborgunin birtist á spilavítareikningnum þínum</li>
</ol>

<h2>Bestu spilavítin fyrir Bitcoin á Íslandi</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/bitstarz/">BitStarz</a></strong> — 5 BTC + 200 FS | Tafarlausar BTC útborganir</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/stake/">Stake</a></strong> — 200% bónus | Styður 8+ dulritunargjaldmiðla</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/bc-game/">BC.Game</a></strong> — 300% allt að 1 BTC | 100+ dulritunargjaldmiðlar</p></div>

<h2>Algengar spurningar</h2>
<h3>Er löglegt að kaupa Bitcoin á Íslandi?</h3>
<p>Já. Engin lög á Íslandi banna kaup á dulritunargjaldmiðlum. <a href="{URL_BASE}gajdy/zakon-ob-azartnyh-igrah-islandiya/">Lestu lagaleiðbeininguna okkar →</a></p>
<h3>Hversu langan tíma tekur innborgun?</h3>
<p>Bitcoin: 10-30 mínútur. USDT (TRC-20): 1-5 mínútur. Ethereum: 2-10 mínútur.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila með Bitcoin →</a></div>'''
    },
    {
        "slug": "islenskir-bankar-spilaviti",
        "title": "Íslenskir bankar og spilavíti — hvaða banki lokar á greiðslur?",
        "desc": "Arion banki, Landsbankinn og Íslandsbanki loka oft á greiðslur til netspilavíta. Hér er hvað þú getur gert.",
        "emoji": "🏦",
        "colors": ("#0a1828", "#183050", "#305880"),
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
<p>Bitcoin, USDT og Ethereum fara beint á blokkkeðjunni — <strong>bankarnir geta ekki lokað á þessar greiðslur</strong>. <a href="{URL_BASE}gajdy/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi →</a></p>

<h3>2. Rafræn veski (e-wallets)</h3>
<p><strong>Skrill</strong> og <strong>Neteller</strong> virka sem milliliður — þú millifærir af bankareikningi á veskið, síðan frá veskinu á spilavítið.</p>

<h3>3. PIQ greiðslur</h3>
<p><a href="{URL_BASE}gajdy/piq-greidslur-island/">PIQ</a> er greiðsluþjónusta sem er sérstaklega hönnuð fyrir Ísland og Noreg. Epicbet og Respin styðja PIQ.</p>

<h3>4. Fyrirframgreidd kort</h3>
<p><strong>Paysafecard</strong> og <strong>Neosurf</strong> eru fyrirframgreidd kort sem þú kaupir í verslun. Enginn banki kemur við sögu.</p>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila með dulritunargjaldmiðlum →</a></div>'''
    },
    {
        "slug": "skattar-spilavinningar-island",
        "title": "Skattar á spilavinninga á Íslandi 2026",
        "desc": "Eru vinningar frá netspilavítum skattskyldir á Íslandi? Hvað þú þarft að vita og hvernig á að halda skrá.",
        "emoji": "⚖️",
        "colors": ("#101028", "#282860", "#484890"),
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
<p><strong>🥉 PIQ greiðslur</strong> — Sérstaklega hannað fyrir Ísland. <a href="{URL_BASE}casino/epicbet/">Epicbet</a> og <a href="{URL_BASE}casino/respin/">Respin</a> styðja PIQ.</p>
</div>

<h2>Bestu spilavítin fyrir íslenska spilara</h2>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/bitstarz/">BitStarz</a></strong> — Dulritunarspilavíti, engin gjaldmiðlaskiptagjöld</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/epicbet/">Epicbet</a></strong> — PIQ greiðslur, íslenskt viðmót</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/stake/">Stake</a></strong> — USDT innlagnir, engin gjöld</p></div>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila án gjaldmiðlaskiptagjalda →</a></div>'''
    },
    {
        "slug": "spilaviti-islenskt-vidmot",
        "title": "Spilavíti með íslensku viðmóti 2026",
        "desc": "Netspilavíti sem bjóða viðmót á íslensku — þjónustuveri, leikir og skilmálar á íslensku.",
        "emoji": "🇮🇸",
        "colors": ("#001040", "#003090", "#0050d0"),
        "content": f'''<h1>Spilavíti með íslensku viðmóti 2026</h1>
{{hero}}
<p>Flest netspilavíti eru á ensku, en nokkur bjóða <strong>íslenskt viðmót</strong> og þjónustuver á íslensku:</p>

<div class="info-box">
<p><strong>✅ Epicbet</strong> — Fullt íslenskt viðmót, Apple Pay greiðslur, PIQ stuðningur. <a href="{URL_BASE}casino/epicbet/">Umsögn →</a></p>
</div>
<div class="info-box">
<p><strong>✅ Respin</strong> — Íslenskt viðmót, PIQ greiðslur, 4000+ leikir. <a href="{URL_BASE}casino/respin/">Umsögn →</a></p>
</div>
<div class="info-box">
<p><strong>✅ Betsson</strong> — Eitt af fáum stórum spilavítum með íslenskt viðmót.</p>
</div>
<div class="info-box">
<p><strong>✅ TonyBet</strong> — Lifandi spilavíti á íslensku, leyfi í Eistlandi (innan EES). <a href="{URL_BASE}casino/tonybet/">Umsögn →</a></p>
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
        "colors": ("#081828", "#103060", "#2060a0"),
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
<div class="info-box"><p><strong><a href="{URL_BASE}casino/epicbet/">Epicbet</a></strong> — PIQ + Apple Pay + íslenskt viðmót</p></div>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/respin/">Respin</a></strong> — PIQ + íslenskt viðmót + 4000 leikir</p></div>

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
<p>Ef PIQ virkar ekki, er <a href="{URL_BASE}gajdy/kaupa-bitcoin-island/">dulritunargjaldmiðill besta lausnin →</a></p>'''
    },
    {
        "slug": "frisnuningar-an-innborgunar",
        "title": "Frísnúningar án innborgunar á Íslandi 2026",
        "desc": "Nýjustu frísnúningatilboð án innborgunar fyrir íslenska spilara. Skráðu þig og fáðu ókeypis snúninga.",
        "emoji": "🎰",
        "colors": ("#280840", "#5020a0", "#8040e0"),
        "content": f'''<h1>Frísnúningar án innborgunar á Íslandi 2026</h1>
{{hero}}
<p>Frísnúningar án innborgunar leyfa þér að <strong>prófa spilavíti ókeypis</strong> — engin innborgun þarf. Hér eru bestu tilboðin:</p>

<h2>Tilboð sem vert er að skoða</h2>
<p><em>Tilboð breytast oft — staðfestu alltaf skilmálana á síðu spilavítisins áður en þú skráir þig.</em></p>
<div class="info-box">
<p><strong>🎁 BitStarz</strong> — Velkomstpakki allt að 5 BTC + 200 frísnúningar. Athugaðu síðuna fyrir núverandi tilboð án innborgunar.</p>
<p><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener">Sækja frísnúninga →</a></p>
</div>
<div class="info-box">
<p><strong>🎁 Winz.io</strong> — 300 frísnúningar (án veðskilyrða!) — vinninga geymdir sem peningar</p>
<p><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener">Sækja frísnúninga →</a></p>
</div>

<h2>Hvernig virka frísnúningar án innborgunar?</h2>
<ol>
<li>Skráðu þig á spilavítið (tekur 30 sekúndur)</li>
<li>Frísnúningar birtast sjálfkrafa á reikningnum þínum</li>
<li>Spilaðu og reyndu að vinna!</li>
<li>Uppfylltu veðskilyrði til að taka vinninga út</li>
</ol>

<h2>Veðskilyrði — hvað þýðir 30x?</h2>
<p>Ef þú vinnur €10 úr frísnúningum og veðskilyrði eru 30x, þarftu að veðja €300 áður en þú getur tekið út. <a href="{URL_BASE}bonusy/vejer/">Lestu meira um veðskilyrði →</a></p>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Fá frísnúninga →</a></div>'''
    },
    {
        "slug": "spilaviti-samanburdur",
        "title": "Spilavíti samanburður — bestu netspilavítin á Íslandi 2026",
        "desc": "Berðu saman netspilavíti hlið við hlið: bónusar, útborgunarhraði, leikjafjöldi og dulritunargjaldmiðlar.",
        "emoji": "📊",
        "colors": ("#100828", "#281860", "#4830a0"),
        "content": f'''<h1>Spilavíti samanburður — Ísland 2026</h1>
{{hero}}
<p>Berðu saman bestu netspilavítin fyrir íslenska spilara hlið við hlið:</p>

<div class="info-box" style="overflow-x:auto;">
<table style="width:100%;border-collapse:collapse;font-size:13px;color:var(--muted);">
<tr style="border-bottom:1px solid var(--border);color:#fff;"><th style="padding:10px;text-align:left;">Spilavíti</th><th>Bónus</th><th>Leikir</th><th>Útborgun</th><th>Dulritun</th><th>Einkunn</th></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;"><a href="{URL_BASE}casino/bitstarz/" style="color:#c080ff;">BitStarz</a></td><td>5 BTC + 200 FS</td><td>3500+</td><td>&lt;10 mín</td><td>✅ BTC, ETH, LTC</td><td>9.8</td></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;"><a href="{URL_BASE}casino/stake/" style="color:#c080ff;">Stake</a></td><td>200% + VIP</td><td>5000+</td><td>&lt;10 mín</td><td>✅ 8+ mynt</td><td>9.6</td></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;"><a href="{URL_BASE}casino/bc-game/" style="color:#c080ff;">BC.Game</a></td><td>300% / 1 BTC</td><td>8000+</td><td>&lt;5 mín</td><td>✅ 100+ mynt</td><td>9.4</td></tr>
<tr style="border-bottom:1px solid var(--border);"><td style="padding:10px;"><a href="{URL_BASE}casino/epicbet/" style="color:#c080ff;">Epicbet</a></td><td>100% / €500</td><td>2000+</td><td>1-3 dagar</td><td>🟡 BTC, ETH</td><td>9.0</td></tr>
<tr><td style="padding:10px;"><a href="{URL_BASE}casino/katsubet/" style="color:#c080ff;">KatsuBet</a></td><td>100% + 100 FS</td><td>5000+</td><td>&lt;10 mín</td><td>✅ 6 mynt</td><td>8.6</td></tr>
</table>
</div>

<p style="font-size:13px;color:var(--muted2);">Útborgunartímar eru samkvæmt upplýsingum rekstraraðila, ekki mældir af okkur. <a href="{URL_BASE}kak-my-ocenivaem/">Aðferðafræði →</a></p>
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
        "colors": ("#0a1020", "#1a2850", "#304880"),
        "content": f'''<h1>Hvernig á að komast framhjá bankalokun á Íslandi 2026</h1>
{{hero}}
<p>Arion banki, Landsbankinn og Íslandsbanki loka oft á greiðslur til erlendra spilavíta. Hér eru <strong>5 aðferðir sem virka</strong>:</p>

<h2>1. 💎 Dulritunargjaldmiðlar (USDT / Bitcoin)</h2>
<p><strong>Áreiðanlegasta lausnin.</strong> Bankar geta ekki lokað á blockchain-færslur.</p>
<p><a href="{URL_BASE}gajdy/kaupa-bitcoin-island/">📖 Skref-fyrir-skref: Hvernig á að kaupa Bitcoin á Íslandi →</a></p>

<h2>2. 💳 PIQ greiðslur</h2>
<p>Greiðsluþjónusta sérstaklega fyrir Ísland. <a href="{URL_BASE}gajdy/piq-greidslur-island/">Lestu PIQ leiðbeininguna →</a></p>

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
        "colors": ("#180840", "#3018a0", "#5030e0"),
        "content": f'''<h1>Besta crypto spilavítið á Íslandi 2026</h1>
{{hero}}
<p>Dulritunargjaldmiðlar eru <strong>besta leiðin til að spila á netspilavítum frá Íslandi</strong> — engin bankalokun, tafarlausar útborganir, og lág gjöld.</p>

<h2>Topp 5 crypto spilavíti á Íslandi</h2>
<div class="info-box">
<p><strong>🥇 <a href="{URL_BASE}casino/bitstarz/">BitStarz</a></strong> — Besta crypto spilavítið. 3500+ leikir, 5 BTC + 200 FS, útborganir á nokkrum mínútum samkvæmt rekstraraðila. Styður BTC, ETH, LTC, DOGE, USDT, BCH. Einkunn: 9.8/10</p>
</div>
<div class="info-box">
<p><strong>🥈 <a href="{URL_BASE}casino/stake/">Stake</a></strong> — Vinsælasta crypto spilavítið í heimi. 200% VIP bónus, 5000+ leikir, 8+ dulritunargjaldmiðlar. Einkunn: 9.6/10</p>
</div>
<div class="info-box">
<p><strong>🥉 <a href="{URL_BASE}casino/bc-game/">BC.Game</a></strong> — 100+ dulritunargjaldmiðlar, 8000+ leikir, 300% bónus. Mest fjölbreytt crypto stuðningur. Einkunn: 9.4/10</p>
</div>
<div class="info-box">
<p><strong>4. <a href="{URL_BASE}casino/katsubet/">KatsuBet</a></strong> — 5000+ leikir, 6 dulritunargjaldmiðlar, 100% + 100 FS. Einkunn: 8.6/10</p>
</div>
<div class="info-box">
<p><strong>5. <a href="{URL_BASE}casino/cloudbet/">Cloudbet</a></strong> — Premium crypto spilavíti, háar takmörkunar, 100% allt að 5 BTC. Einkunn: 8.4/10</p>
</div>

<h2>Af hverju dulritunar spilavíti á Íslandi?</h2>
<ul>
<li>🔓 Komast framhjá <a href="{URL_BASE}gajdy/islenskir-bankar-spilaviti/">bankalokun íslenskra banka</a></li>
<li>⚡ Dulritunarútborganir oft á mínútum, samkvæmt rekstraraðilum (kort taka yfirleitt 1–5 daga)</li>
<li>💰 Engin gjaldmiðlaskiptagjöld</li>
<li>🛡️ Aukið næði — engar spilavítafærslur á bankayfirlitinu</li>
</ul>

<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á BitStarz →</a></div>'''
    },
]

for page in seo_pages:
    hero = make_hero(page["title"][:40], "BF Casino leiðbeining", page["emoji"], *page["colors"])
    page_content = page["content"].replace("{hero}", hero)
    bc = [("{URL_BASE}", "Heim"), ("{URL_BASE}gajdy/", "Leiðbeiningar"), ("", page["title"][:50])]
    html = page_template(page["title"], page["desc"], bc, page_content)
    write_page(f'gajdy/{page["slug"]}/index.html', html)

print(f"  ✅ {len(seo_pages)} SEO target pages generated")

# 10. ИНДЕКСНЫЕ СТРАНИЦЫ РАЗДЕЛОВ
print("Generating index pages...")

# Casino index — FULL landing page (main casino hub)
casino_cards = ""
for c in casinos[:20]:
    ctype_label = "Crypto" if c["type"]=="crypto" else "Classic"
    casino_cards += f'''<a href="{URL_BASE}casino/{c["slug"]}/" class="game-card">
<div class="game-card-thumb" style="background:linear-gradient(135deg,{'#0a2060,#1a40a0' if c['type']=='crypto' else '#2a1040,#5020a0'});display:flex;align-items:center;justify-content:center;"><span style="font-size:28px;font-weight:800;color:rgba(255,255,255,.15);">{c["rating"]}</span></div>
<div class="game-card-info"><div class="game-card-name">{c["name"]}</div><div class="game-card-prov">{c["bonus"]} · {ctype_label}</div></div></a>\n'''

casino_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}casino/{c["slug"]}/">{c["name"]}</a></strong> — {isk(c["bonus"])} (Einkunn: {c["rating"]}/10)</p></div>' for c in casinos[:50]])

casino_content = f'''<h1>Bestu netspilavítin á Íslandi 2026</h1>
<p>BF Casino umsagnir um {len(casinos)} netspilavíti fyrir íslenska leikmenn. Berðu saman bónusa, greiðslumáta og leikjasöfn. Öll spilavíti styðja dulritunargjaldmiðla — auðveldasta leiðin til að spila frá Íslandi.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á Top Casino →</a></div>
<h2>Besta spilavítið eftir þörfum</h2>
<h3>Hæsti velkomstbónusinn</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/bitstarz/">BitStarz</a></strong> — allt að 5 BTC + 200 frísnúningar. <a href="{URL_BASE}bonusy/velkomstbonus/">Allir velkomstbónusar →</a></p></div>
<h3>Stærsta leikjasafnið</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/7bit/">7Bit Casino</a></strong> — yfir 7.000 leikir samkvæmt rekstraraðila. <a href="{URL_BASE}slots/">Spilakassar →</a></p></div>
<h3>Bestu dulritunarútborganirnar</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/bc-game/">BC.Game</a></strong> — yfir 100 dulritunargjaldmiðlar og sýnir ISK frá Íslandi. <a href="{URL_BASE}gajdy/besta-crypto-spilaviti-island/">Bestu crypto spilavítin →</a></p></div>
<h3>Íslenskt viðmót</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/respin/">Respin</a></strong> og <strong><a href="{URL_BASE}casino/epicbet/">Epicbet</a></strong> — viðmót á íslensku og PIQ greiðslur. <a href="{URL_BASE}gajdy/spilaviti-islenskt-vidmot/">Meira →</a></p></div>
<h3>Bónus án veðskilyrða</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/winz/">Winz.io</a></strong> — vinningar úr bónus án veðskilyrða. <a href="{URL_BASE}gajdy/frisnuningar-an-innborgunar/">Frísnúningar →</a></p></div>
<h3>Lifandi spilavíti á íslensku</h3>
<div class="info-box"><p><strong><a href="{URL_BASE}casino/tonybet/">TonyBet</a></strong> — Evolution borð og leyfi innan EES. <a href="{URL_BASE}live/">Lifandi leikir →</a></p></div>
<p style="font-size:13px;color:var(--muted2);">Allur samanburður: <a href="{URL_BASE}gajdy/spilaviti-samanburdur/">Spilavíti samanburður</a> · <a href="{URL_BASE}kak-my-ocenivaem/">Hvernig við metum</a></p>
<h2>Topp 20 spilavíti</h2>
<div class="game-grid">{casino_cards}</div>
<h2>Öll {len(casinos)} Spilavíti umsagnir</h2>
{casino_list}'''

write_page("casino/index.html", page_template("Bestu netspilavítin á Íslandi 2026", f"Berðu saman {len(casinos)} netspilavíti á Íslandi. Dulritunargreiðslur, hraðar útborganir, velkomstbónusar.",
    [("{URL_BASE}", "Home"), ("", "Casino")],
    casino_content))

# Slots index
slots_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}slots/{s["slug"]}/">{s["name"]}</a></strong> — {s["provider"]} | RTP {s["rtp"]}% | {s["maxwin"]}</p></div>' for s in slots_data[:30]])
write_page("slots/index.html", page_template("Allir spilakassar", "Umsagnir um vinsæla spilakassa",
    [("{URL_BASE}", "Home"), ("", "Slots")],
    f'<h1>Vinsælir spilakassar 2026</h1><p>Umsagnir um {len(slots_data)} spilakassa frá fremstu birgjum.</p>{slots_list}'))

# Live index
live_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}live/{g["slug"]}/">{g["name"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in live_games[:20]])
write_page("live/index.html", page_template("Live Casino", "Leikir með lifandi spilastjórum",
    [("{URL_BASE}", "Home"), ("", "Live Casino")],
    f'<h1>Spilavíti í beinni — Leikir með lifandi spilastjórum</h1><p>{len(live_games)} leikir með faglegum spilastjórum.</p>{live_list}'))

# Bonus index
bonus_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}bonusy/{b["slug"]}/">{b["title"]}</a></strong> — {b["desc"][:80]}</p></div>' for b in bonus_pages[:20]])
write_page("bonusy/index.html", page_template("Casino Bónusar", "Allir bónusar og afsláttarkóðar",
    [("{URL_BASE}", "Home"), ("", "Bónusar")],
    f'<h1>Casino Bónusar 2026</h1><p>{len(bonus_pages)} virk bónustilboð.</p>{bonus_list}'))

# Payment index
pay_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}platezhi/{p["slug"]}/">{p["title"]}</a></strong></p></div>' for p in payment_pages[:20]])
write_page("platezhi/index.html", page_template("Greiðslumátar", "Dulritunargjaldmiðlar og aðrar greiðslur í spilavítum",
    [("{URL_BASE}", "Home"), ("", "Payments")],
    f'<h1>Casino Greiðslumátar</h1><p>Hvernig á að komast framhjá lokun banka og spila frá Íslandi.</p>{pay_list}'))

# Guide index
guide_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}gajdy/{g["slug"]}/">{g["title"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in seo_pages + guide_pages])
write_page("gajdy/index.html", page_template("Guides", "Leiðbeiningar og kennsluefni fyrir leikmenn",
    [("{URL_BASE}", "Home"), ("", "Guides")],
    f'<h1>Leiðbeiningar fyrir leikmenn</h1><p>{len(guide_pages)} leiðbeiningar fyrir byrjendur og reynda leikmenn.</p>{guide_list}'))


# 10. SITEMAP
print("Generating sitemap.xml...")
sitemap_urls = ['https://bestiflokkurinn.is/']
for c in casinos:
    sitemap_urls.append(f'https://bestiflokkurinn.is/casino/{c["slug"]}/')
for cat in casino_categories:
    sitemap_urls.append(f'https://bestiflokkurinn.is/casino/{cat["slug"]}/')
for s in slots_data:
    sitemap_urls.append(f'https://bestiflokkurinn.is/slots/{s["slug"]}/')
for g in live_games:
    sitemap_urls.append(f'https://bestiflokkurinn.is/live/{g["slug"]}/')
for b in bonus_pages:
    sitemap_urls.append(f'https://bestiflokkurinn.is/bonusy/{b["slug"]}/')
for p in payment_pages:
    sitemap_urls.append(f'https://bestiflokkurinn.is/platezhi/{p["slug"]}/')
for g in guide_pages:
    sitemap_urls.append(f'https://bestiflokkurinn.is/gajdy/{g["slug"]}/')
for sp in seo_pages:
    sitemap_urls.append(f'https://bestiflokkurinn.is/gajdy/{sp["slug"]}/')
for a in about_pages:
    sitemap_urls.append(f'https://bestiflokkurinn.is/{a["slug"]}/')
sitemap_urls.extend([
    'https://bestiflokkurinn.is/casino/',
    'https://bestiflokkurinn.is/slots/',
    'https://bestiflokkurinn.is/live/',
    'https://bestiflokkurinn.is/bonusy/',
    'https://bestiflokkurinn.is/platezhi/',
    'https://bestiflokkurinn.is/gajdy/',
])

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_xml += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
sitemap_xml += '</urlset>'

with open(os.path.join(BASE, 'sitemap.xml'), 'w') as f:
    f.write(sitemap_xml)

# robots.txt
with open(os.path.join(BASE, 'robots.txt'), 'w') as f:
    f.write('User-agent: *\nAllow: /\nSitemap: https://bestiflokkurinn.is/sitemap.xml\n')

print(f"\n✅ Generated {count} pages + sitemap.xml + robots.txt")
print(f"URLs in sitemap: {len(sitemap_urls)}")
