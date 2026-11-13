#!/usr/bin/env python3
"""
Bestiflokkurinn.is — BF Casino site generator
Öll content in English
"""
import os
import json
import sys

# URL base path — "/" for production on bestiflokkurinn.is, "/slotoro-site/" for GitHub Pages
URL_BASE = "/" if "--production" in sys.argv else "/slotoro-site/"

# ============================================================
# PAGE DATA
# ============================================================

# 150 casino reviews
casinos = [
    {"slug": "bitstarz", "name": "BitStarz", "rating": 9.8, "bonus": "5 BTC + 200 FS", "type": "crypto", "desc": "Award-winning crypto casino with instant payouts. Over 3,500 games from top-tier providers including Pragmatic Play, Evolution, and Play'n GO. Accepts BTC, ETH, LTC, DOGE and more. Withdrawals processed in under 10 minutes. Curaçao licensed with provably fair games."},
    {"slug": "stake", "name": "Stake", "rating": 9.6, "bonus": "200% + VIP", "type": "crypto", "desc": "One of the most popular crypto casinos worldwide with an exclusive VIP programme, original Stake games, and a full sportsbook. Supports 8 cryptocurrencies. Known for fast withdrawals and transparent house edge on original games."},
    {"slug": "bc-game", "name": "BC.Game", "rating": 9.4, "bonus": "300% up to 1 BTC", "type": "crypto", "desc": "Innovative crypto casino with proprietary crash, dice, and limbo games. Supports 100+ cryptocurrencies including BTC, ETH, SOL, and DOGE. Daily bonuses, lucky spins, and a task-based reward system. Curaçao licence."},
    {"slug": "tonybet", "name": "TonyBet", "rating": 9.2, "bonus": "150% + 100 FS", "type": "classic", "desc": "Established sportsbook and casino platform with a strong live dealer section powered by Evolution. Accepts Visa, Mastercard, Skrill, and crypto. MGA-licensed with responsible gambling tools built in."},
    {"slug": "epicbet", "name": "Epicbet", "rating": 9.0, "bonus": "100% up to €500", "type": "classic", "desc": "Modern casino with a clean interface, fast card and e-wallet withdrawals, and responsive 24/7 support. Over 2,000 slots from NetEnt, Microgaming, and Pragmatic Play. Curaçao licensed."},
    {"slug": "respin", "name": "Respin Casino", "rating": 8.9, "bonus": "200% + 50 FS", "type": "classic", "desc": "Casino with a massive slot library exceeding 4,000 titles and generous deposit bonuses. Weekly cashback and reload offers for existing players. Supports multiple languages and currencies."},
    {"slug": "vegazone", "name": "VegaZone", "rating": 8.8, "bonus": "150% up to €300", "type": "classic", "desc": "Stylish casino featuring exclusive slot tournaments, regular promotions, and a loyalty programme with real rewards. Good selection of live tables and e-wallet payment support."},
    {"slug": "wildcoins", "name": "WildCoins", "rating": 8.7, "bonus": "250% + 100 FS", "type": "crypto", "desc": "Crypto-focused casino with high-percentage welcome bonuses and fast BTC withdrawals. Supports Bitcoin, Ethereum, Litecoin, and USDT. No KYC required for crypto deposits under certain thresholds."},
    {"slug": "katsubet", "name": "KatsuBet", "rating": 8.6, "bonus": "100% + 100 FS", "type": "crypto", "desc": "Japanese-themed crypto casino with over 5,000 games from 40+ providers. Accepts BTC, ETH, LTC, DOGE, USDT, and BCH. Weekly tournaments, daily free spins, and a four-tier VIP programme."},
    {"slug": "winz", "name": "Winz.io", "rating": 8.5, "bonus": "300 FS no wager", "type": "crypto", "desc": "Unique casino offering wager-free bonuses — you keep what you win with no playthrough requirements. Supports 6 cryptocurrencies and offers 5,000+ games. Licensed in Curaçao."},
    {"slug": "7bit", "name": "7Bit Casino", "rating": 8.5, "bonus": "200% + 100 FS", "type": "crypto", "desc": "Retro-styled crypto casino establerhed in 2014 with a proven track record. Over 7,000 games, weekly cashback up to 20%, Monday reload bonuses. Accepts BTC, ETH, LTC, DOGE, USDT, and BCH."},
    {"slug": "mbitcasino", "name": "mBit Casino", "rating": 8.4, "bonus": "175% + 300 FS", "type": "crypto", "desc": "One of the oldest crypto casinos, operating since 2014. Accepts Bitcoin, Ethereum, Litecoin, Dogecoin, and Tether. Over 3,000 games with provably fair options. VIP programme with personal account manager."},
    {"slug": "cloudbet", "name": "Cloudbet", "rating": 8.4, "bonus": "100% up to 5 BTC", "type": "crypto", "desc": "Premium crypto casino and sportsbook with high table limits for VIP players. Supports BTC, ETH, USDT, and more. Known for competitive sports odds and a large live casino section."},
    {"slug": "casinonic", "name": "Casinonic", "rating": 8.3, "bonus": "100% + 100 FS", "type": "classic", "desc": "Beginner-friendly casino with a simple registration process and intuitive navigation. Over 2,000 slots, live dealer tables, and weekly cashback. Accepts Visa, Mastercard, and crypto."},
    {"slug": "national-casino", "name": "National Casino", "rating": 8.3, "bonus": "100% + 100 FS", "type": "classic", "desc": "Casino with an excellent live dealer collection powered by Evolution and Pragmatic Play Live. Fast verification process, multiple withdrawal methods, and responsive customer support."},
    {"slug": "20bet", "name": "20Bet", "rating": 8.2, "bonus": "100% up to €120", "type": "classic", "desc": "Öll-in-one platform combining casino, live casino, and sportsbook. Over 6,000 games from 70+ providers. Accepts Visa, Mastercard, e-wallets, and cryptocurrencies. Licensed in Curaçao."},
    {"slug": "rocketplay", "name": "RocketSpila", "rating": 8.2, "bonus": "150% + 100 FS", "type": "crypto", "desc": "Space-themed crypto casino with fast Bitcoin withdrawals and a wide game selection. 3,500+ games, weekly reload bonuses, and a four-level VIP programme with cashback up to 12%."},
    {"slug": "hellspin", "name": "HellSpin", "rating": 8.1, "bonus": "150% + 50 FS", "type": "crypto", "desc": "Bold casino with aggressive bonus offers, frequent promotions, and a dark-themed interface. Supports BTC, ETH, LTC, and USDT. Over 3,000 games including exclusive titles."},
    {"slug": "neospin", "name": "NeoSpin", "rating": 8.1, "bonus": "100% + 100 FS", "type": "crypto", "desc": "Next-generation casino with a futuristic design, 5,000+ games, and support for Bitcoin, Ethereum, and Tether. Daily cashback, weekly tournaments, and instant crypto payouts."},
    {"slug": "betpanda", "name": "BetPanda", "rating": 8.0, "bonus": "100% up to 1 BTC", "type": "crypto", "desc": "Friendly crypto casino with low wagering requirements on bonuses (typically 30x). Supports BTC, ETH, and USDT. Simple interface, fast payouts, and no-KYC deposits up to certain limits."},
]

# Generate 130 more casinos
extra_casino_names = [
    "LuckyStar", "IceBet", "NordicSlots", "FrostBet", "SnowCasino", "AuroraBet",
    "VikingSlots", "ThunderBet", "GlacierCasino", "BorealerBet", "CrystalSlots",
    "MidnightSun", "VolcanoBet", "GeyserCasino", "RuneBet", "ValhallaCasino",
    "OdinSlots", "ThorBet", "FreyaCasino", "LokiBet", "FenrirSlots",
    "JormungandrBet", "MidgardCasino", "AsgardSlots", "BifrostBet", "YggdrasilCasino",
    "RagnarokBet", "HelCasino", "TyrSlots", "BaldurBet", "HeimdallCasino",
    "NjordBet", "SkadiSlots", "SifCasino", "BragiBet", "IdunnSlots",
    "MimirCasino", "NornBet", "EinherjSlots", "WyrdCasino", "SagaBet",
    "EddaSlots", "RunicCasino", "GaldurBet", "SeidrSlots", "VolvaCasino",
    "DrakkarBet", "LongshipSlots", "ShieldCasino", "AxeBet", "SwordSlots",
    "HammerCasino", "SpearBet", "BowSlots", "HelmCasino", "ChainmailBet",
    "FjordSlots", "TundraCasino", "PermafrostBet", "IcebergSlots", "BlizzardCasino",
    "AvalancheBet", "SnowstormSlots", "FrostbiteCasino", "GlacialBet", "ArcticSlots",
    "PolarCasino", "NorthernBet", "MidwinterSlots", "SolsticeCasino", "EquinoxBet",
    "TwilightSlots", "DawnCasino", "DuskBet", "StarfallSlots", "MeteorCasino",
    "CometBet", "NebulSlots", "PulsarCasino", "QuasarBet", "NovaSlots",
    "ZenithCasino", "ApexBet", "PeakSlots", "SummitCasino", "RidgeBet",
    "CliffSlots", "ValleyCasino", "RiverBet", "OceanSlots", "TideCasino",
    "WaveBet", "CurrentSlots", "DepthCasino", "AbyssBet", "TrenchSlots",
    "CoralCasino", "ReefBet", "LagoonSlots", "BayCasino", "CoveBet",
    "HarborSlots", "PortCasino", "DockBet", "AnchorSlots", "SailCasino",
    "WindBet", "StormSlots", "RainCasino", "HailBet", "SnowSlots",
    "MistCasino", "FogBet", "CloudSlots", "SkyCasino", "SunBet",
    "MoonSlots", "EclipseCasino", "PrismBet", "SpectrumSlots", "RainbowCasino",
    "GoldBet", "SilverSlots", "PlatinumCasino", "DiamondBet", "RubyCasino",
    "EmeraldBet", "SapphireSlots", "TopazCasino", "AmethystBet"
]

for i, name in enumerate(extra_casino_names[:130]):
    slug = name.lower().replace(" ", "-")
    rating = round(8.0 - (i * 0.015), 1)
    rating = max(rating, 6.0)
    ctype = "crypto" if i % 3 == 0 else "classic"
    bonus_options = ["100% up to €200", "150% + 50 FS", "200% up to €500", "50 FS no deposit", "100% up to 0.5 BTC", "125% + 75 FS", "100% up to €300"]
    bonus = bonus_options[i % len(bonus_options)]
    casinos.append({
        "slug": slug,
        "name": name,
        "rating": rating,
        "bonus": bonus,
        "type": ctype,
        "desc": f"{name} is a licensed online casino offering {bonus} for new players. Fast crypto withdrawals, a wide game library, and 24/7 customer support. Available to players from Iceland."
    })

# 250 slots
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

# Add 180 more slots with CDN-mapped provider folders
generic_slot_themes = ["Egypt","Fruit","Space","Ocean","Fairy Tales","Vikings","Asia","Pirates","Mythology","Western","Nature","Money","Horror","Fantasy","Classic"]
generic_providers = ["Pragmatic Play","NetEnt","Play'n GO","Microgaming","Yggdrasil","Push Gaming","Hacksaw Gaming","NoLimit City","Red Tiger","Thunderkick","Relax Gaming","ELK Studios","Big Time Gaming","Blueprint Gaming","iSoftBet"]
cdn_provider_map = {
    "Pragmatic Play": "pragmaticexternal",
    "NetEnt": "netent",
    "Play'n GO": "playngo",
    "Microgaming": "microgaming",
    "Yggdrasil": "yggdrasil",
    "Push Gaming": "pushgaming",
    "Hacksaw Gaming": "hacksaw",
    "NoLimit City": "nolimitcity",
    "Red Tiger": "redtiger",
    "Thunderkick": "thunderkick",
    "Relax Gaming": "relax",
    "ELK Studios": "elk",
    "Big Time Gaming": "bigtimegaming",
    "Blueprint Gaming": "blueprint",
    "iSoftBet": "isoftbet",
}
for i in range(180):
    n = f"Slot Game {i+70}"
    slug = f"slot-game-{i+70}"
    prov = generic_providers[i % len(generic_providers)]
    cdn_folder = cdn_provider_map.get(prov, prov.lower().replace(" ", ""))
    slots_data.append({
        "slug": slug,
        "name": n,
        "provider": prov,
        "rtp": round(95.5 + (i % 30) * 0.1, 2),
        "volatility": ["Low","Medium","High","Extreme"][i % 4],
        "maxwin": f"x{(i+1)*500}",
        "theme": generic_slot_themes[i % len(generic_slot_themes)],
        "cdn": f"{cdn_folder}/SlotGame{i+70}.png"
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
for casino in casinos[:70]:
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


# ============================================================
# HTML TEMPLATE
# ============================================================

def get_nav():
    return f'''<nav class="nav">
  <a href="{URL_BASE}" class="nav-logo">
    <div class="nav-mark">BF</div>
    <div class="logo-text">BF Casino</div>
  </a>
  <div class="nav-links">
    <a href="{URL_BASE}">Heim</a>
    <a href="{URL_BASE}entertainment/">Afþreying</a>
    <a href="{URL_BASE}casino/">Spilavíti</a>
    <a href="{URL_BASE}slots/">Spilakassar</a>
    <a href="{URL_BASE}bonusy/">Bónusar</a>
    <a href="{URL_BASE}live/">Í beinni</a>
    <a href="{URL_BASE}gajdy/">Leiðbeiningar</a>
  </div>
  <div class="nav-actions">
    <a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="btn-signup">Nýskráning</a>
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
        <div><div class="footer-col-title">UPPLÝSINGAR</div><a href="{URL_BASE}o-nas/">Um okkur</a><a href="{URL_BASE}gajdy/">Leiðbeiningar</a><a href="{URL_BASE}platezhi/">Greiðslur</a></div>
      </div>
    </div>
    <div class="footer-18">18+ | Fjárhættuspil geta verið ávanabindandi. Spilaðu á ábyrgan hátt. <a href="https://www.begambleaware.org" target="_blank" rel="noopener">BeGambleAware.org</a></div>
    <div class="footer-bottom"><span>© 2026 bestiflokkurinn.is</span><span>BF Casino — óháð umsagnarvefur</span></div>
  </div>
</footer>'''

def page_template(title, desc, breadcrumbs, content, canonical=""):
    bc_html = ' → '.join([f'<a href="{url}">{name}</a>' for url, name in breadcrumbs])
    return f'''<!DOCTYPE html>
<html lang="is">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | BF Casino</title>
<meta name="description" content="{desc}">
{f'<link rel="canonical" href="{canonical}">' if canonical else ''}
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display&family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#0c0618;--bg2:#140e28;--bg3:#1a1235;--card:rgba(25,15,50,.55);--border:rgba(140,100,220,.1);--border2:rgba(140,100,220,.2);--purple:#8040e0;--violet:#c060ff;--blue:#80b0ff;--accent:#c080ff;--accent-bg:rgba(140,80,240,.06);--gold:#f0c050;--text:#c4b8e8;--text2:#9a8cc0;--muted:rgba(160,140,200,.6);--muted2:rgba(100,80,150,.4);--warm1:#2a1040;--warm2:#1a0830;}}
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
.nav-actions{{display:flex;gap:8px;}}
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
.content h1{{font-family:'DM Serif Display',serif;font-size:32px;font-weight:400;margin-bottom:20px;line-height:1.2;color:#fff;background:linear-gradient(135deg,#fff 60%,#c080ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.content h2{{font-family:'Space Grotesk',sans-serif;font-size:21px;font-weight:700;margin:32px 0 14px;color:#e0d0f8;position:relative;padding-left:16px;}}
.content h2::before{{content:'';position:absolute;left:0;top:4px;bottom:4px;width:3px;border-radius:2px;background:linear-gradient(180deg,#8040e0,#c060ff);}}
.content h3{{font-size:16px;font-weight:600;margin:24px 0 10px;color:var(--text);}}
.content p{{color:var(--muted);font-size:14px;line-height:1.75;margin-bottom:16px;}}
.content ul,.content ol{{color:var(--muted);font-size:14px;line-height:1.75;margin:0 0 16px 20px;}}
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
.slot-hero-bg{{width:100%;height:100%;background-size:cover;background-position:center;}}
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
.footer-18{{text-align:center;padding:14px;border:1px solid var(--border);border-radius:12px;background:var(--bg2);margin-bottom:12px;font-size:10px;color:var(--muted2);}}
.footer-18 a{{color:#c080ff;}}
.footer-bottom{{border-top:1px solid var(--border);padding-top:10px;display:flex;justify-content:space-between;color:var(--muted2);font-size:9px;}}
@media(max-width:768px){{
  .page-wrap{{grid-template-columns:1fr;gap:24px;padding:24px 16px 40px;}}
  .nav{{padding:10px 16px;flex-wrap:wrap;gap:8px;}}
  .nav-links{{gap:12px;font-size:11px;}}
  .content h1{{font-size:26px;}}
  .footer-top{{flex-direction:column;gap:14px;}}
  .game-grid{{grid-template-columns:repeat(2,1fr);}}
  .sidebar{{order:2;}}
}}
</style>
</head>
<body>
<div class="top-accent"></div>
{get_nav()}
<div class="breadcrumbs">{bc_html}</div>
<div class="page-wrap">
<main class="content">
{content}
</main>
<aside class="sidebar">
<div class="sidebar-card">
<h4>🏆 Topp spilavíti</h4>
<a href="{URL_BASE}casino/bitstarz/">BitStarz — 5 BTC + 200 FS</a>
<a href="{URL_BASE}casino/stake/">Stake — 200% + VIP</a>
<a href="{URL_BASE}casino/bc-game/">BC.Game — 300% up to 1 BTC</a>
<a href="{URL_BASE}casino/katsubet/">KatsuBet — 100% + 100 FS</a>
<a href="{URL_BASE}casino/winz/">Winz.io — 300 FS no wager</a>
</div>
<a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="sidebar-cta">Spila núna →</a>
<div class="sidebar-card" style="margin-top:16px;">
<h4>📖 Leiðbeiningar</h4>
<a href="{URL_BASE}gajdy/kak-vybrat-casino/">Hvernig á að velja spilavíti</a>
<a href="{URL_BASE}gajdy/chto-takoe-rtp/">Hvað er RTP?</a>
<a href="{URL_BASE}gajdy/chto-takoe-volatilnost/">Hvað er sveifla?</a>
<a href="{URL_BASE}platezhi/bitcoin/">Bitcoin greiðslur</a>
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
<p><strong>Bónus:</strong> {c["bonus"]}</p>
<p><strong>Tegund:</strong> {"Dulritunargjaldmiðils spilavíti" if c["type"]=="crypto" else "Hefðbundið spilavíti"}</p>
</div>
<p>{c["desc"]}</p>
<h2>{c["name"]} umsögn</h2>
<p>{c["name"]} er {"dulritunargjaldmiðils spilavíti" if c["type"]=="crypto" else "netspilavíti"} í boði fyrir íslenska leikmenn. Spilavítið býður upp á fjölbreytt úrval af spilakössum, borðleikjum og lifandi spilavíti með raunverulegum spilastjórum.</p>
<h3>Bónusar og tilboð</h3>
<p>Nýir leikmenn fá velkomstbónus upp á {c["bonus"]}. Til að virkja bónusinn, skráðu þig og leggðu inn fyrstu innborgun þína.</p>
<h3>Greiðslumátar</h3>
<p>{"Tekur við Bitcoin, Ethereum, USDT, Litecoin og öðrum dulritunargjaldmiðlum." if c["type"]=="crypto" else "Tekur við Visa, Mastercard, dulritunargjaldmiðlum og rafrænum veskjum."} Þetta er sérstaklega mikilvægt fyrir íslenska leikmenn þar sem innlendir bankar loka oft á spilavíta-færslur.</p>
<h3>Leikir</h3>
<p>{c["name"]} býður upp á yfir 2000 leiki frá fremstu birgjum: Pragmatic Play, NetEnt, Play'n GO, Microgaming og fleiri.</p>
<h2>Kostir og gallar</h2>
<ul>
<li>✅ {c["bonus"]}</li>
<li>✅ Hraðar útborganir</li>
<li>✅ {"Dulritunargreiðslur án lokunar" if c["type"]=="crypto" else "Fjölbreytt úrval greiðslumáta"}</li>
<li>✅ Stórt safn leikja</li>
<li>⚠️ Tekur ekki við íslenskum krónum beint</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á {c["name"]} →</a></div>'''

    bc = [("{URL_BASE}", "Heim"), ("{URL_BASE}casino/", "Spilavíti"), ("", c["name"])]
    html = page_template(f'{c["name"]} umsögn', c["desc"], bc, content)
    write_page(f'casino/{c["slug"]}/index.html', html)

# 2. КАТЕГОРИИ КАЗИНО (50)
print("Generating casino categories...")
for cat in casino_categories:
    top_casinos = casinos[:10]
    cards = ""
    for c in top_casinos:
        cards += f'<div class="info-box"><p><strong>{c["name"]}</strong> — {c["bonus"]} (Einkunn: {c["rating"]}/10) <a href="{URL_BASE}casino/{c["slug"]}/">Umsögn →</a></p></div>\n'

    content = f'''<h1>{cat["title"]} á Íslandi 2026</h1>
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
    cdn_img = ""
    if s.get("cdn"):
        cdn_img = f'<div class="slot-hero"><div class="slot-hero-bg" style="background:url(\'https://cdn.softswiss.net/i/s3/{s["cdn"]}\') center/cover,linear-gradient(135deg,#0a1040,#1a2070);"></div></div>'
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
    content = f'''<h1>{g["name"]} — Spilavíti í beinni</h1>
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
    content = f'''<h1>{b["title"]}</h1>
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
    content = f'''<h1>{p["title"]}</h1>
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
    content = f'''<h1>{g["title"]}</h1>
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
for a in about_pages:
    content = f'''<h1>{a["title"]}</h1>
<p>{a["desc"]}</p>
<p>BF Casino (bestiflokkurinn.is) er óháð spilavítavefgátt fyrir íslenska leikmenn. Við hjálpum þér að finna áreiðanleg spilavíti með bestu bónusum og stuðningi við dulritunargjaldmiðla.</p>'''

    bc = [("{URL_BASE}", "Home"), ("", a["title"])]
    html = page_template(a["title"], a["desc"], bc, content)
    write_page(f'{a["slug"]}/index.html', html)

# 9. ИНДЕКСНЫЕ СТРАНИЦЫ РАЗДЕЛОВ
print("Generating index pages...")

# Casino index — FULL landing page (main casino hub)
casino_cards = ""
for c in casinos[:20]:
    ctype_label = "Crypto" if c["type"]=="crypto" else "Classic"
    casino_cards += f'''<a href="{URL_BASE}casino/{c["slug"]}/" class="game-card">
<div class="game-card-thumb" style="background:linear-gradient(135deg,{'#0a2060,#1a40a0' if c['type']=='crypto' else '#2a1040,#5020a0'});display:flex;align-items:center;justify-content:center;"><span style="font-size:28px;font-weight:800;color:rgba(255,255,255,.15);">{c["rating"]}</span></div>
<div class="game-card-info"><div class="game-card-name">{c["name"]}</div><div class="game-card-prov">{c["bonus"]} · {ctype_label}</div></div></a>\n'''

casino_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}casino/{c["slug"]}/">{c["name"]}</a></strong> — {c["bonus"]} (Einkunn: {c["rating"]}/10)</p></div>' for c in casinos[:50]])

casino_content = f'''<h1>Bestu netspilavítin á Íslandi 2026</h1>
<p>BF Casino umsagnir um {len(casinos)} netspilavíti fyrir íslenska leikmenn. Berðu saman bónusa, greiðslumáta og leikjasöfn. Öll spilavíti styðja dulritunargjaldmiðla — auðveldasta leiðin til að spila frá Íslandi.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á Top Casino →</a></div>
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
guide_list = "\n".join([f'<div class="info-box"><p><strong><a href="{URL_BASE}gajdy/{g["slug"]}/">{g["title"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in guide_pages[:20]])
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
