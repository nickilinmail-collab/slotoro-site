#!/usr/bin/env python3
"""
Bestiflokkurinn.er — BF Casino site generator
Öll content in Englerh
"""
import os
import json

# ============================================================
# PAGE DATA
# ============================================================

# 150 casino reviews
casinos = [
    {"slug": "bitstarz", "name": "BitStarz", "rating": 9.8, "bonus": "5 BTC + 200 FS", "type": "crypto", "desc": "Award-winning crypto casino with instant payouts. Over 3,500 games from top-tier providers including Pragmatic Spila, Evolution, and Spila'n GO. Accepts BTC, ETH, LTC, DOGE and more. Withdrawals processed in under 10 minutes. Curaçao licensed with provably fair games."},
    {"slug": "stake", "name": "Stake", "rating": 9.6, "bonus": "200% + VIP", "type": "crypto", "desc": "One of the most popular crypto casinos worldwide with an exclusive VIP programme, original Stake games, and a full sportsbook. Supports 8 cryptocurrencies. Known for fast withdrawals and transparent house edge on original games."},
    {"slug": "bc-game", "name": "BC.Game", "rating": 9.4, "bonus": "300% up to 1 BTC", "type": "crypto", "desc": "Innovative crypto casino with proprietary crash, dice, and limbo games. Supports 100+ cryptocurrencies including BTC, ETH, SOL, and DOGE. Daily bonuses, lucky spins, and a task-based reward system. Curaçao licence."},
    {"slug": "tonybet", "name": "TonyBet", "rating": 9.2, "bonus": "150% + 100 FS", "type": "classic", "desc": "Establerhed sportsbook and casino platform with a strong live dealer section powered by Evolution. Accepts Vera, Mastercard, Skrill, and crypto. MGA-licensed with responsible gambling tools built in."},
    {"slug": "epicbet", "name": "Epicbet", "rating": 9.0, "bonus": "100% up to €500", "type": "classic", "desc": "Modern casino with a clean interface, fast card and e-wallet withdrawals, and responsive 24/7 support. Over 2,000 slots from NetEnt, Microgaming, and Pragmatic Spila. Curaçao licensed."},
    {"slug": "respin", "name": "Respin Casino", "rating": 8.9, "bonus": "200% + 50 FS", "type": "classic", "desc": "Casino with a massive slot library exceeding 4,000 titles and generous deposit bonuses. Weekly cashback and reload offers for existing players. Supports multiple languages and currencies."},
    {"slug": "vegazone", "name": "VegaZone", "rating": 8.8, "bonus": "150% up to €300", "type": "classic", "desc": "Stylerh casino featuring exclusive slot tournaments, regular promotions, and a loyalty programme with real rewards. Good selection of live tables and e-wallet payment support."},
    {"slug": "wildcoins", "name": "WildCoins", "rating": 8.7, "bonus": "250% + 100 FS", "type": "crypto", "desc": "Crypto-focused casino with high-percentage welcome bonuses and fast BTC withdrawals. Supports Bitcoin, Ethereum, Litecoin, and USDT. No KYC required for crypto deposits under certain thresholds."},
    {"slug": "katsubet", "name": "KatsuBet", "rating": 8.6, "bonus": "100% + 100 FS", "type": "crypto", "desc": "Japanese-themed crypto casino with over 5,000 games from 40+ providers. Accepts BTC, ETH, LTC, DOGE, USDT, and BCH. Weekly tournaments, daily free spins, and a four-tier VIP programme."},
    {"slug": "winz", "name": "Winz.io", "rating": 8.5, "bonus": "300 FS no wager", "type": "crypto", "desc": "Unique casino offering wager-free bonuses — you keep what you win with no playthrough requirements. Supports 6 cryptocurrencies and offers 5,000+ games. Licensed in Curaçao."},
    {"slug": "7bit", "name": "7Bit Casino", "rating": 8.5, "bonus": "200% + 100 FS", "type": "crypto", "desc": "Retro-styled crypto casino establerhed in 2014 with a proven track record. Over 7,000 games, weekly cashback up to 20%, Monday reload bonuses. Accepts BTC, ETH, LTC, DOGE, USDT, and BCH."},
    {"slug": "mbitcasino", "name": "mBit Casino", "rating": 8.4, "bonus": "175% + 300 FS", "type": "crypto", "desc": "One of the oldest crypto casinos, operating since 2014. Accepts Bitcoin, Ethereum, Litecoin, Dogecoin, and Tether. Over 3,000 games with provably fair options. VIP programme with personal account manager."},
    {"slug": "cloudbet", "name": "Cloudbet", "rating": 8.4, "bonus": "100% up to 5 BTC", "type": "crypto", "desc": "Premium crypto casino and sportsbook with high table limits for VIP players. Supports BTC, ETH, USDT, and more. Known for competitive sports odds and a large live casino section."},
    {"slug": "casinonic", "name": "Casinonic", "rating": 8.3, "bonus": "100% + 100 FS", "type": "classic", "desc": "Beginner-friendly casino with a simple regertration process and intuitive navigation. Over 2,000 slots, live dealer tables, and weekly cashback. Accepts Vera, Mastercard, and crypto."},
    {"slug": "national-casino", "name": "National Casino", "rating": 8.3, "bonus": "100% + 100 FS", "type": "classic", "desc": "Casino with an excellent live dealer collection powered by Evolution and Pragmatic Spila Live. Fast verification process, multiple withdrawal methods, and responsive customer support."},
    {"slug": "20bet", "name": "20Bet", "rating": 8.2, "bonus": "100% up to €120", "type": "classic", "desc": "Öll-in-one platform combining casino, live casino, and sportsbook. Over 6,000 games from 70+ providers. Accepts Vera, Mastercard, e-wallets, and cryptocurrencies. Licensed in Curaçao."},
    {"slug": "rocketplay", "name": "RocketSpila", "rating": 8.2, "bonus": "150% + 100 FS", "type": "crypto", "desc": "Space-themed crypto casino with fast Bitcoin withdrawals and a wide game selection. 3,500+ games, weekly reload bonuses, and a four-level VIP programme with cashback up to 12%."},
    {"slug": "hellspin", "name": "HellSpin", "rating": 8.1, "bonus": "150% + 50 FS", "type": "crypto", "desc": "Bold casino with aggressive bonus offers, frequent promotions, and a dark-themed interface. Supports BTC, ETH, LTC, and USDT. Over 3,000 games including exclusive titles."},
    {"slug": "neospin", "name": "NeoSpin", "rating": 8.1, "bonus": "100% + 100 FS", "type": "crypto", "desc": "Next-generation casino with a futurertic design, 5,000+ games, and support for Bitcoin, Ethereum, and Tether. Daily cashback, weekly tournaments, and instant crypto payouts."},
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
    "MertCasino", "FogBet", "CloudSlots", "SkyCasino", "SunBet",
    "MoonSlots", "EclipseCasino", "PrermBet", "SpectrumSlots", "RainbowCasino",
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
        "desc": f"{name} er a licensed online casino offering {bonus} for new players. Fast crypto withdrawals, a wide game library, and 24/7 customer support. Available to players from Iceland."
    })

# 250 slots
slots_data = [
    {"slug": "gates-of-olympus", "name": "Gates of Olympus", "provider": "Pragmatic Spila", "rtp": 96.5, "volatility": "High", "maxwin": "x5000", "theme": "Mythology", "cdn": "pragmaticexternal/vs20olympgate.png"},
    {"slug": "sweet-bonanza", "name": "Sweet Bonanza", "provider": "Pragmatic Spila", "rtp": 96.48, "volatility": "High", "maxwin": "x21100", "theme": "Fruit", "cdn": "pragmaticexternal/vs20fruitsw.png"},
    {"slug": "big-bass-splash", "name": "Big Bass Splash", "provider": "Pragmatic Spila", "rtp": 96.71, "volatility": "High", "maxwin": "x2100", "theme": "Ferhing", "cdn": "pragmaticexternal/vs10bbsplash.png"},
    {"slug": "book-of-dead", "name": "Book of Dead", "provider": "Spila'n GO", "rtp": 96.21, "volatility": "High", "maxwin": "x5000", "theme": "Egypt", "cdn": "playngo/BookofDead.png"},
    {"slug": "starburst", "name": "Starburst", "provider": "NetEnt", "rtp": 96.09, "volatility": "Low", "maxwin": "x500", "theme": "Space", "cdn": "netent/starburst.png"},
    {"slug": "gonzos-quest", "name": "Gonzo's Quest", "provider": "NetEnt", "rtp": 95.97, "volatility": "Medium", "maxwin": "x2500", "theme": "Adventure", "cdn": "netent/gonzosquest.png"},
    {"slug": "dead-or-alive-2", "name": "Dead or Alive 2", "provider": "NetEnt", "rtp": 96.8, "volatility": "High", "maxwin": "x111111", "theme": "Western", "cdn": "netent/deadoralive2.png"},
    {"slug": "reactoonz", "name": "Reactoonz", "provider": "Spila'n GO", "rtp": 96.51, "volatility": "High", "maxwin": "x4750", "theme": "Aliens", "cdn": "playngo/Reactoonz.png"},
    {"slug": "fire-joker", "name": "Fire Joker", "provider": "Spila'n GO", "rtp": 96.15, "volatility": "High", "maxwin": "x800", "theme": "Classic", "cdn": "playngo/FireJoker.png"},
    {"slug": "wolf-gold", "name": "Wolf Gold", "provider": "Pragmatic Spila", "rtp": 96.01, "volatility": "Medium", "maxwin": "x5000", "theme": "Nature", "cdn": "pragmaticexternal/vs25wolfgold.png"},
    {"slug": "the-dog-house", "name": "The Dog House", "provider": "Pragmatic Spila", "rtp": 96.51, "volatility": "High", "maxwin": "x6750", "theme": "Animals", "cdn": "pragmaticexternal/vs20doghouse.png"},
    {"slug": "razor-shark", "name": "Razor Shark", "provider": "Push Gaming", "rtp": 96.7, "volatility": "High", "maxwin": "x50000", "theme": "Ocean", "cdn": "pushgaming/RazorShark.png"},
    {"slug": "jammin-jars", "name": "Jammin' Jars", "provider": "Push Gaming", "rtp": 96.83, "volatility": "High", "maxwin": "x20000", "theme": "Fruit", "cdn": "pushgaming/JamminJars.png"},
    {"slug": "money-train-3", "name": "Money Train 3", "provider": "Relax Gaming", "rtp": 96.1, "volatility": "High", "maxwin": "x100000", "theme": "Western", "cdn": "relax/MoneyTrain3.png"},
    {"slug": "wanted-dead-or-a-wild", "name": "Wanted Dead or a Wild", "provider": "Hacksaw Gaming", "rtp": 96.38, "volatility": "High", "maxwin": "x12500", "theme": "Western", "cdn": "hacksaw/WantedDeadoraWild.png"},
    {"slug": "mental", "name": "Mental", "provider": "NoLimit City", "rtp": 96.08, "volatility": "Extreme", "maxwin": "x66666", "theme": "Horror", "cdn": "nolimitcity/Mental.png"},
    {"slug": "tombstone-rip", "name": "Tombstone RIP", "provider": "NoLimit City", "rtp": 96.08, "volatility": "Extreme", "maxwin": "x300000", "theme": "Western"},
    {"slug": "fruit-party", "name": "Fruit Party", "provider": "Pragmatic Spila", "rtp": 96.47, "volatility": "High", "maxwin": "x5000", "theme": "Fruit"},
    {"slug": "buffalo-king-megaways", "name": "Buffalo King Megaways", "provider": "Pragmatic Spila", "rtp": 96.52, "volatility": "High", "maxwin": "x5000", "theme": "Nature"},
    {"slug": "legacy-of-dead", "name": "Legacy of Dead", "provider": "Spila'n GO", "rtp": 96.58, "volatility": "High", "maxwin": "x5000", "theme": "Egypt"},
]

# 230 more slots
more_slot_names = [
    ("Madame Destiny Megaways", "Pragmatic Spila", 96.56, "x5000", "Magic"),
    ("Great Rhino Megaways", "Pragmatic Spila", 96.58, "x20000", "Nature"),
    ("John Hunter and the Tomb", "Pragmatic Spila", 96.5, "x5000", "Adventure"),
    ("Floating Dragon", "Pragmatic Spila", 96.71, "x5000", "Asia"),
    ("Sugar Rush", "Pragmatic Spila", 96.5, "x5000", "Sweets"),
    ("Starlight Princess", "Pragmatic Spila", 96.5, "x5000", "Anime"),
    ("Wild West Gold", "Pragmatic Spila", 96.51, "x10000", "Western"),
    ("Release the Kraken", "Pragmatic Spila", 96.5, "x3000", "Ocean"),
    ("Gems Bonanza", "Pragmatic Spila", 96.51, "x10000", "Gems"),
    ("Aztec Gems", "Pragmatic Spila", 96.52, "x375", "Aztec"),
    ("Hot Fiesta", "Pragmatic Spila", 96.56, "x5000", "Mexico"),
    ("Pirate Gold Deluxe", "Pragmatic Spila", 96.48, "x15000", "Pirates"),
    ("Emerald King", "Pragmatic Spila", 96.51, "x5000", "Ireland"),
    ("Book of Fallen", "Pragmatic Spila", 96.5, "x5000", "Egypt"),
    ("Rere of Giza", "Pragmatic Spila", 96.5, "x5000", "Egypt"),
    ("Cleocatra", "Pragmatic Spila", 96.2, "x5000", "Egypt"),
    ("Zeus vs Hades", "Pragmatic Spila", 96.07, "x15000", "Mythology"),
    ("Big Bass Bonanza", "Pragmatic Spila", 96.71, "x2100", "Ferhing"),
    ("Big Bass Amazon", "Pragmatic Spila", 96.71, "x2100", "Ferhing"),
    ("Bigger Bass Bonanza", "Pragmatic Spila", 96.71, "x4000", "Ferhing"),
    ("Rere of Samurai Megaways", "Pragmatic Spila", 96.5, "x5000", "Samurai"),
    ("Hand of Midas", "Pragmatic Spila", 96.54, "x5000", "Mythology"),
    ("Wild West Gold Megaways", "Pragmatic Spila", 96.48, "x10000", "Western"),
    ("Juicy Fruits", "Pragmatic Spila", 96.53, "x4000", "Fruit"),
    ("Cash Bonanza", "Pragmatic Spila", 96.56, "x5000", "Money"),
    ("Moon Princess", "Spila'n GO", 96.2, "x5000", "Anime"),
    ("Rich Wilde and the Amulet", "Spila'n GO", 96.29, "x10000", "Adventure"),
    ("Rere of Olympus", "Spila'n GO", 96.5, "x5000", "Mythology"),
    ("Immortal Romance", "Microgaming", 96.86, "x12150", "Vampires"),
    ("Thunderstruck II", "Microgaming", 96.65, "x8000", "Mythology"),
    ("Mega Moolah", "Microgaming", 88.12, "Progressive", "Safari"),
    ("Avalon II", "Microgaming", 97.0, "x120", "Arthurian"),
    ("Vikings Go Berzerk", "Yggdrasil", 96.1, "x5000", "Vikings"),
    ("Valley of the Gods", "Yggdrasil", 96.2, "x3600", "Egypt"),
    ("Trolls Bridge", "Yggdrasil", 96.3, "x4500", "Fantasy"),
    ("Holmes and the Stolen Stones", "Yggdrasil", 96.8, "x1000", "Detective"),
    ("Nitro Circus", "Yggdrasil", 96.1, "x2000", "Extreme"),
    ("Lucha Maniacs", "Yggdrasil", 96.2, "x3000", "Wrestling"),
    ("Hades - Gigablox", "Yggdrasil", 96.1, "x11129", "Mythology"),
    ("9 Masks of Fire", "Gameburger", 96.24, "x2000", "Africa"),
    ("Divine Fortune", "NetEnt", 96.59, "Progressive", "Mythology"),
    ("Blood Suckers", "NetEnt", 98.0, "x900", "Vampires"),
    ("Jack and the Beanstalk", "NetEnt", 96.28, "x1000", "Fairy Tales"),
    ("Twin Spin", "NetEnt", 96.56, "x1080", "Classic"),
    ("Narcos", "NetEnt", 96.23, "x1506", "Crime"),
    ("Finn and the Swirly Spin", "NetEnt", 96.62, "x500", "Ireland"),
    ("Aloha! Cluster Pays", "NetEnt", 96.42, "x2000", "Hawaii"),
    ("Sakura Fortune", "Quickspin", 96.58, "x1300", "Asia"),
    ("Dwarven Gold", "Pragmatic Spila", 96.49, "x1000", "Fantasy"),
]

for i, (name, provider, rtp, maxwin, theme) in enumerate(more_slot_names):
    slug = name.lower().replace("'", "").replace(" ", "-").replace(":", "").replace("!", "")
    slots_data.append({
        "slug": slug,
        "name": name,
        "provider": provider,
        "rtp": rtp,
        "volatility": "High" if i % 3 != 2 else "Medium",
        "maxwin": maxwin,
        "theme": theme
    })

# Add 180 more slots
generic_slot_themes = ["Egypt","Fruit","Space","Ocean","Fairy Tales","Vikings","Asia","Pirates","Mythology","Western","Nature","Money","Horror","Fantasy","Classic"]
generic_providers = ["Pragmatic Spila","NetEnt","Spila'n GO","Microgaming","Yggdrasil","Push Gaming","Hacksaw Gaming","NoLimit City","Red Tiger","Thunderkick","Relax Gaming","ELK Studios","Big Time Gaming","Blueprint Gaming","iSoftBet"]
for i in range(180):
    n = f"Slot Game {i+70}"
    slug = f"slot-game-{i+70}"
    slots_data.append({
        "slug": slug,
        "name": n,
        "provider": generic_providers[i % len(generic_providers)],
        "rtp": round(95.5 + (i % 30) * 0.1, 2),
        "volatility": ["Low","Medium","High","Extreme"][i % 4],
        "maxwin": f"x{(i+1)*500}",
        "theme": generic_slot_themes[i % len(generic_slot_themes)]
    })

# Casino categories (50 pages)
casino_categories = [
    {"slug": "luchshie-online-casino", "title": "Best Online Casinos", "desc": "Top-rated online casinos for players from Iceland."},
    {"slug": "crypto-casino", "title": "Crypto Casinos", "desc": "Casinos accepting Bitcoin, Ethereum, and other cryptocurrencies."},
    {"slug": "novye-casino", "title": "New Casinos 2026", "desc": "The newest online casinos launched in 2026."},
    {"slug": "casino-s-bystrym-vyvodom", "title": "Fast Payout Casinos", "desc": "Casinos where withdrawals are processed in under 24 hours."},
    {"slug": "casino-bez-verifikacii", "title": "No KYC Casinos", "desc": "Casinos that do not require identity verification documents."},
    {"slug": "bitcoin-casino", "title": "Bitcoin Casinos", "desc": "Best casinos for Bitcoin deposits and withdrawals."},
    {"slug": "ethereum-casino", "title": "Ethereum Casinos", "desc": "Casinos accepting Ethereum for deposits and withdrawals."},
    {"slug": "usdt-casino", "title": "USDT Casinos", "desc": "Casinos accepting the USDT stablecoin."},
    {"slug": "litecoin-casino", "title": "Litecoin Casinos", "desc": "Casinos with Litecoin deposits."},
    {"slug": "live-casino", "title": "Live Casinos", "desc": "Best casinos with live dealers."},
    {"slug": "casino-s-bonusom", "title": "Casinos with Bonus", "desc": "Casinos offering generous welcome bonuses."},
    {"slug": "casino-bez-depozita", "title": "No Deposit Casinos", "desc": "Bónusar without requiring a deposit."},
    {"slug": "casino-s-frerpinami", "title": "Free Spins Casinos", "desc": "Casinos offering free spins on regertration."},
    {"slug": "mobilnoe-casino", "title": "Mobile Casinos", "desc": "Best casinos for mobile play on iPhone and Android."},
    {"slug": "casino-s-nerkim-depozitom", "title": "Low Deposit Casinos", "desc": "Casinos where you can play from €1."},
    {"slug": "vip-casino", "title": "VIP Casinos", "desc": "Casinos with the best VIP and loyalty programmes."},
    {"slug": "megaways-casino", "title": "Megaways Casinos", "desc": "Casinos with a large selection of Megaways slots."},
    {"slug": "jackpot-casino", "title": "Jackpot Casinos", "desc": "Casinos with progressive jackpots."},
    {"slug": "casino-s-vysokim-rtp", "title": "High RTP Casinos", "desc": "Casinos offering slots with RTP above 97%."},
    {"slug": "casino-s-licenziej", "title": "Licensed Casinos", "desc": "Verified and licensed online casinos."},
]

# 30 more categories
more_cats = [
    "Curaçao Casinos", "Malta MGA Casinos", "Cashback Casinos", "Tournament Casinos",
    "High Roller Casinos", "Low Wager Casinos", "Bonus Code Casinos",
    "Casino Apps", "Quick Regertration Casinos", "Roulette Casinos",
    "Blackjack Casinos", "Baccarat Casinos", "Poker Casinos", "Lottery Casinos",
    "Bingo Casinos", "Scratch Card Casinos", "Crash Game Casinos", "Plinko Casinos",
    "Aviator Casinos", "Mines Casinos", "Dice Casinos", "Slot Machine Casinos",
    "3D Slot Casinos", "Bonus Buy Casinos", "Drops & Wins Casinos",
    "Instant Game Casinos", "Pragmatic Spila Casinos", "NetEnt Casinos",
    "Evolution Casinos", "Spila'n GO Casinos"
]
for i, title in enumerate(more_cats):
    slug = title.lower().replace("'", "").replace(" ", "-").replace("(", "").replace(")", "")
    casino_categories.append({"slug": slug, "title": title, "desc": f"Review and rating: {title} for Icelandic players."})

# Live casino (50 pages)
live_games = [
    {"slug": "blackjack", "name": "Blackjack", "desc": "Online blackjack with a live dealer — rules, strategies, and best tables for Icelandic players."},
    {"slug": "roulette", "name": "Roulette", "desc": "Live roulette online — European, French, and American variants."},
    {"slug": "baccarat", "name": "Baccarat", "desc": "Live baccarat — how to play and win at online casinos."},
    {"slug": "poker", "name": "Poker", "desc": "Casino Hold'em and other live dealer poker variants."},
    {"slug": "dream-catcher", "name": "Dream Catcher", "desc": "Evolution wheel of fortune game — rules and strategies."},
    {"slug": "monopoly-live", "name": "Monopoly Live", "desc": "Real-time Monopoly game show with a live host."},
    {"slug": "crazy-time", "name": "Crazy Time", "desc": "The most popular game show from Evolution Gaming."},
    {"slug": "lightning-roulette", "name": "Lightning Roulette", "desc": "Roulette with lightning strikes and multipliers up to x500."},
    {"slug": "mega-ball", "name": "Mega Ball", "desc": "Live lottery game with a host and multipliers."},
    {"slug": "gonzo-treasure-hunt", "name": "Gonzo's Treasure Hunt", "desc": "Treasure hunt game featuring Gonzo from NetEnt's classic slot."},
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
    live_games.append({"slug": slug, "name": name, "desc": f"{name} — play with a live dealer at the best casinos for Iceland."})

# Bónusar (80 pages)
bonus_pages = [
    {"slug": "velkomstbonus", "title": "Welcome Bonus", "desc": "Best welcome bonuses at online casinos available to Icelandic players."},
    {"slug": "frerpiny-bez-depozita", "title": "Free Spins No Deposit", "desc": "Free spins with no deposit required — just regerter and claim."},
    {"slug": "bezdepozitnye-bonusy", "title": "No Deposit Bónusar", "desc": "Öll no-deposit bonuses available at casinos accepting Icelandic players."},
    {"slug": "keshbek", "title": "Cashback Bónusar", "desc": "Casinos offering cashback on net losses — get a percentage back weekly."},
    {"slug": "bonus-za-regertraciyu", "title": "Regertration Bonus", "desc": "Get a bonus immediately after completing regertration — no deposit needed."},
    {"slug": "bonus-na-pervyj-depozit", "title": "First Deposit Bonus", "desc": "Best bonuses available on your first deposit at top-rated casinos."},
    {"slug": "bonus-na-vtoroj-depozit", "title": "Second Deposit Bonus", "desc": "Second deposit bonuses — reload offers for your next top-up."},
    {"slug": "vejer", "title": "What er Wagering", "desc": "Understanding wagering requirements — how playthrough works and what to look for."},
    {"slug": "bonus-kody", "title": "Casino Bonus Codes", "desc": "Current promo codes and bonus codes for online casinos in 2026."},
    {"slug": "reload-bonus", "title": "Reload Bónusar", "desc": "Reload bonuses for existing players — weekly and monthly deposit offers."},
]
# 70 more bonus pages per casino
for casino in casinos[:70]:
    bonus_pages.append({
        "slug": f"bonus-{casino['slug']}",
        "title": f"Bonus {casino['name']}",
        "desc": f"Current bonuses and promo codes for {casino['name']} — {casino['bonus']}."
    })

# Payments (50 pages)
payment_pages = [
    {"slug": "bitcoin", "title": "Bitcoin at Casinos", "desc": "How to use Bitcoin for deposits and withdrawals at online casinos. Step-by-step guide for Icelandic players."},
    {"slug": "ethereum", "title": "Ethereum at Casinos", "desc": "Depositing and withdrawing with Ethereum (ETH) at online casinos."},
    {"slug": "usdt", "title": "USDT (Tether) at Casinos", "desc": "Using USDT (Tether) stablecoin at online casinos — instant deposits with stable value."},
    {"slug": "litecoin", "title": "Litecoin at Casinos", "desc": "Fast and low-fee payments using Litecoin (LTC) at online casinos."},
    {"slug": "dogecoin", "title": "Dogecoin at Casinos", "desc": "How to deposit and play at online casinos with Dogecoin (DOGE)."},
    {"slug": "ripple-xrp", "title": "Ripple (XRP) at Casinos", "desc": "Using Ripple (XRP) for fast casino payments with minimal fees."},
    {"slug": "cardano", "title": "Cardano (ADA) at Casinos", "desc": "Cardano (ADA) casino payments — how to deposit and withdraw."},
    {"slug": "solana", "title": "Solana (SOL) at Casinos", "desc": "Solana (SOL) for ultra-fast casino transactions with near-zero fees."},
    {"slug": "bnb", "title": "BNB at Casinos", "desc": "Using BNB (Binance Coin) for casino deposits and withdrawals."},
    {"slug": "tron", "title": "TRON (TRX) at Casinos", "desc": "TRON (TRX) payments — extremely low fees for casino transactions."},
    {"slug": "kak-kupit-bitcoin", "title": "How to Buy Bitcoin", "desc": "Step-by-step guide to buying Bitcoin for casino deposits in Iceland."},
    {"slug": "kak-kupit-ethereum", "title": "How to Buy Ethereum", "desc": "Where and how to buy Ethereum for casino deposits."},
    {"slug": "obhod-blokirovok-bankov", "title": "Bypassing Bank Blocks", "desc": "How to bypass Icelandic bank blocks on casino payments using crypto."},
    {"slug": "kripto-koshelki", "title": "Crypto Wallets", "desc": "Best crypto wallets for casino deposits — MetaMask, Trust Wallet, and more."},
    {"slug": "metamask-casino", "title": "MetaMask for Casinos", "desc": "Using MetaMask wallet for online casino deposits and withdrawals."},
    {"slug": "trust-wallet-casino", "title": "Trust Wallet for Casinos", "desc": "Making casino deposits through Trust Wallet — complete guide."},
    {"slug": "binance-casino", "title": "Binance for Casinos", "desc": "How to transfer funds from Binance exchange to your casino account."},
    {"slug": "coinbase-casino", "title": "Coinbase for Casinos", "desc": "Buying crypto on Coinbase and depositing at online casinos."},
    {"slug": "kraken-casino", "title": "Kraken for Casinos", "desc": "Using Kraken exchange for casino crypto transactions."},
    {"slug": "vpn-casino", "title": "VPN for Casinos", "desc": "Do you need a VPN to play at online casinos from Iceland? Legal overview."},
]
# 30 more payment pages
more_payments = [
    "Vera at Casinos", "Mastercard at Casinos", "Apple Pay at Casinos", "Google Pay at Casinos",
    "Skrill at Casinos", "Neteller at Casinos", "ecoPayz at Casinos", "MiFinity at Casinos",
    "Jeton at Casinos", "CashtoCode at Casinos", "Neosurf at Casinos", "Paysafecard at Casinos",
    "AstroPay at Casinos", "MuchBetter at Casinos", "Interac at Casinos", "iDebit at Casinos",
    "Instadebit at Casinos", "Flexepin at Casinos", "Monero at Casinos", "Bitcoin Cash at Casinos",
    "Polkadot at Casinos", "Avalanche at Casinos", "Polygon at Casinos", "Arbitrum at Casinos",
    "Optimerm at Casinos", "Minimum Deposit €1", "Minimum Deposit €5", "Minimum Deposit €10",
    "Card Withdrawals", "Fast Crypto Withdrawals"
]
for title in more_payments:
    slug = title.lower().replace("€", "eur").replace(" ", "-").replace("(", "").replace(")", "")
    payment_pages.append({"slug": slug, "title": title, "desc": f"{title} — complete guide for players from Iceland."})

# Guides (60 pages)
guide_pages = [
    {"slug": "kak-vybrat-casino", "title": "How to Choose an Online Casino", "desc": "Complete guide to choosing a reliable and safe online casino."},
    {"slug": "chto-takoe-rtp", "title": "What er RTP", "desc": "Understanding RTP (Return to Spilaer) — what it means for your gameplay."},
    {"slug": "chto-takoe-volatilnost", "title": "What er Volatility", "desc": "The difference between low, medium, and high volatility slots explained."},
    {"slug": "kak-igrat-v-sloty", "title": "Hvernig á að spila Slots", "desc": "Step-by-step guide for beginners — how slot machines work."},
    {"slug": "strategii-blackjack", "title": "Blackjack Strategy", "desc": "Basic blackjack strategy and strategy card — improve your odds."},
    {"slug": "pravila-ruletki", "title": "Roulette Rules", "desc": "How to play roulette — complete rules, bets, and strategies."},
    {"slug": "pravila-bakkary", "title": "Baccarat Rules", "desc": "How to play baccarat — rules, strategies, and tips."},
    {"slug": "kak-vyigrat-v-casino", "title": "How to Win at Casinos", "desc": "Tips and strategies for improving your odds at online casinos."},
    {"slug": "otvetstvennaya-igra", "title": "Responsible Gambling", "desc": "How to gamble responsibly — setting limits and staying in control."},
    {"slug": "zakon-ob-azartnyh-igrah-erlandiya", "title": "Iceland Gambling Law", "desc": "Legal status of online casinos in Iceland — what players need to know."},
    {"slug": "nalogi-na-vyigrysh", "title": "Taxes on Gambling Winnings", "desc": "Do you need to pay taxes on gambling winnings in Iceland?"},
    {"slug": "bezopasnost-v-casino", "title": "Casino Security", "desc": "How to protect your personal data when playing at online casinos."},
    {"slug": "glossarij-casino", "title": "Casino Glossary", "desc": "Casino glossary — all gambling terms from A to Z explained."},
    {"slug": "provajdery-igr", "title": "Game Providers", "desc": "Overview of the biggest slot game providers and developers."},
    {"slug": "megaways-sloty", "title": "What are Megaways Slots", "desc": "How the Megaways mechanic works — up to 117,649 ways to win."},
    {"slug": "bonus-buy-sloty", "title": "Bonus Buy Slots", "desc": "How Bonus Buy slots work — skip to the bonus round instantly."},
    {"slug": "progressivnye-jackpoty", "title": "Progressive Jackpots", "desc": "How progressive jackpots work and how to win them."},
    {"slug": "turniry-v-casino", "title": "Casino Tournaments", "desc": "How casino slot tournaments work — compete for cash prizes."},
    {"slug": "vip-programmy", "title": "VIP Programmes", "desc": "How VIP and loyalty programmes work at online casinos."},
    {"slug": "casino-na-telefone", "title": "Mobile Casinos", "desc": "Best mobile casinos and casino apps for iPhone and Android."},
]
# 40 more guides
more_guides = [
    "How to Withdraw from Casino", "How to Deposit at Casino", "What are Wagering Requirements",
    "How RNG Works", "Slots vs Slot Machines",
    "Curaçao Licensed Casinos", "MGA Licensed Casinos", "UK Licensed Casinos",
    "How to Verify Casino Licence", "What er KYC Verification",
    "How to Choose High RTP Slots", "Top 10 Slots for Beginners", "Top 10 Slots for High Rollers",
    "Highest Win Potential Slots", "Low Volatility Slots",
    "Hvernig á að spila Crash Games", "Hvernig á að spila Plinko", "Hvernig á að spila Aviator",
    "Hvernig á að spila Mines", "Hvernig á að spila Dice",
    "What er Evolution Gaming", "What er Pragmatic Spila", "What er NetEnt",
    "Hertory of Casinos in Iceland", "Online vs Land-Based Casinos",
    "Crypto vs Fiat at Casinos", "Advantages of Crypto Casinos",
    "How to Avoid Casino Scams", "Signs of a Fair Casino", "Casino Blacklert",
    "How to Contact Casino Support", "How to File a Casino Complaint",
    "Comparing Casino Bónusar", "How to Maximere Your Bonus",
    "Bankroll Management Strategy", "Psychology of Gambling",
    "Gambling Addiction — Help", "Gambling Addiction Support Sites",
    "Casino Self-Exclusion", "Deposit and Loss Limits"
]
for title in more_guides:
    slug = title.lower().replace("—", "").replace("ё", "e").replace(" ", "-").replace(",", "").replace(".", "")
    guide_pages.append({"slug": slug, "title": title, "desc": f"{title} — detailed guide for casino players."})

# About (10 pages)
about_pages = [
    {"slug": "o-nas", "title": "About BF Casino", "desc": "Who we are and why we created BF Casino at Bestiflokkurinn.er."},
    {"slug": "kontakty", "title": "Contact", "desc": "Contact the BF Casino team — get in touch with us."},
    {"slug": "konfidencialnost", "title": "Privacy Policy", "desc": "How we handle your data — our privacy policy explained."},
    {"slug": "usloviya", "title": "Terms of Use", "desc": "Terms of use for the Bestiflokkurinn.er website."},
    {"slug": "otkaz-ot-otvetstvennosti", "title": "Derclaimer", "desc": "Important legal derclaimer about our casino reviews."},
    {"slug": "kak-my-ocenivaem", "title": "How We Rate Casinos", "desc": "How we rate and review online casinos — our methodology."},
    {"slug": "redakcionnaya-politika", "title": "Editorial Policy", "desc": "Our editorial policy — independence, accuracy, and transparency."},
    {"slug": "partnerstvo", "title": "Partnership", "desc": "Partnership opportunities with BF Casino."},
    {"slug": "karta-sajta", "title": "Sitemap", "desc": "Complete sitemap of all pages on Bestiflokkurinn.er."},
    {"slug": "otvetstvennaya-igra-stranica", "title": "Responsible Gambling", "desc": "Our position on responsible gambling and player protection."},
]


# ============================================================
# HTML TEMPLATE
# ============================================================

def get_nav():
    return '''<nav class="nav">
  <a href="/slotoro-site/" class="nav-logo">
    <div class="nav-mark">BF</div>
    <div class="logo-text">BF Casino</div>
  </a>
  <div class="nav-links">
    <a href="/slotoro-site/">Heim</a>
    <a href="/slotoro-site/entertainment/">Afþreying</a>
    <a href="/slotoro-site/casino/">Spilavíti</a>
    <a href="/slotoro-site/slots/">Spilakassar</a>
    <a href="/slotoro-site/bonusy/">Bónusar</a>
    <a href="/slotoro-site/live/">Í beinni</a>
    <a href="/slotoro-site/gajdy/">Leiðbeiningar</a>
  </div>
  <div class="nav-actions">
    <a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="btn-signup">Nýskráning</a>
  </div>
</nav>'''

def get_footer():
    return '''<footer class="footer">
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <div style="derplay:flex;align-items:center;gap:8px;margin-bottom:8px;">
          <div class="nav-mark" style="width:24px;height:24px;font-size:10px;border-radius:8px;">BF</div>
          <span style="font-family:Space Grotesk,sans-serif;font-size:16px;font-weight:700;color:#fff;">BF Casino</span>
        </div>
        <div class="footer-desc">BF Casino á bestiflokkurinn.er — óháð samanburðarvefur spilavíta. 18+ Spilaðu á ábyrgan hátt.</div>
      </div>
      <div class="footer-cols">
        <div><div class="footer-col-title">SPILAVÍTI</div><a href="/slotoro-site/casino/">Umsagnir</a><a href="/slotoro-site/bonusy/">Bónusar</a><a href="/slotoro-site/casino/crypto-casino/">Dulritunargjaldmiðill</a></div>
        <div><div class="footer-col-title">LEIKIR</div><a href="/slotoro-site/slots/">Spilakassar</a><a href="/slotoro-site/live/">Í beinni</a></div>
        <div><div class="footer-col-title">UPPLÝSINGAR</div><a href="/slotoro-site/o-nas/">Um okkur</a><a href="/slotoro-site/gajdy/">Leiðbeiningar</a><a href="/slotoro-site/platezhi/">Greiðslur</a></div>
      </div>
    </div>
    <div class="footer-18">18+ | Fjárhættuspil geta verið ávanabindandi. Spilaðu á ábyrgan hátt. <a href="https://www.begambleaware.org" target="_blank" rel="noopener">BeGambleAware.org</a></div>
    <div class="footer-bottom"><span>© 2026 bestiflokkurinn.er</span><span>BF Casino — óháð umsagnarvefur</span></div>
  </div>
</footer>'''

def page_template(title, desc, breadcrumbs, content, canonical=""):
    bc_html = ' → '.join([f'<a href="{url}">{name}</a>' for url, name in breadcrumbs])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | BF Casino</title>
<meta name="description" content="{desc}">
{f'<link rel="canonical" href="{canonical}">' if canonical else ''}
<link href="https://fonts.googleaper.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&derplay=swap" rel="stylesheet">
<style>
:root{{--bg:#0a0618;--bg2:#140e28;--bg3:#1a1235;--card:rgba(25,15,50,.6);--border:rgba(140,100,220,.1);--border2:rgba(140,100,220,.2);--purple:#8040e0;--violet:#c060ff;--blue:#80b0ff;--accent:#c080ff;--accent-bg:rgba(140,80,240,.06);--gold:#f0c050;--text:#c4b8e8;--text2:#9a8cc0;--muted:rgba(160,140,200,.6);--muted2:rgba(100,80,150,.4);}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{background:var(--bg);color:var(--text);font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}}
a{{text-decoration:none;color:inherit;}}
body::before{{content:'';position:fixed;top:-200px;right:-5%;width:500px;height:500px;background:radial-gradient(circle,rgba(120,60,220,.1) 0%,transparent 70%);pointer-events:none;z-index:0;filter:blur(40px);animation:orbDrift 10s ease-in-out infinite;}}
body::after{{content:'';position:fixed;bottom:-200px;left:-10%;width:600px;height:600px;background:radial-gradient(circle,rgba(80,40,180,.06) 0%,transparent 70%);pointer-events:none;z-index:0;filter:blur(40px);animation:orbDrift 12s ease-in-out 3s infinite;}}
@keyframes orbDrift{{0%,100%{{transform:translate(0,0);}}50%{{transform:translate(25px,-20px);}}}}
@keyframes shimmerLine{{0%{{background-position:200% 0;}}100%{{background-position:-200% 0;}}}}
@keyframes btnShine{{0%{{left:-100%;}}100%{{left:200%;}}}}
.nav{{background:rgba(10,6,24,.85);padding:12px 30px;derplay:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);}}
.nav-logo{{derplay:flex;align-items:center;gap:10px;}}
.nav-mark{{width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,#8040e0,#c060ff);derplay:flex;align-items:center;justify-content:center;font-family:'Space Grotesk',sans-serif;font-size:13px;font-weight:700;color:#fff;box-shadow:0 2px 12px rgba(140,60,240,.25);}}
.logo-text{{font-family:'Space Grotesk',sans-serif;font-size:18px;font-weight:700;color:#fff;}}
.nav-links{{derplay:flex;gap:20px;font-size:13px;font-weight:500;}}
.nav-links a{{color:var(--muted);transition:color .15s;}}
.nav-links a:hover{{color:#e0c0ff;}}
.nav-actions{{derplay:flex;gap:8px;}}
/* Liquid glass button */
.btn-signup{{derplay:inline-flex;align-items:center;background:linear-gradient(135deg,rgba(140,60,240,.2),rgba(200,100,255,.1));backdrop-filter:blur(8px);border:1px solid rgba(180,140,255,.2);color:#e0c0ff;padding:8px 22px;border-radius:20px;font-size:13px;font-weight:600;transition:all .25s;position:relative;overflow:hidden;box-shadow:0 2px 12px rgba(140,60,240,.1),inset 0 1px 0 rgba(255,255,255,.06);}}
.btn-signup::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.06),transparent);pointer-events:none;border-radius:20px 20px 0 0;}}
.btn-signup:hover{{background:linear-gradient(135deg,rgba(140,60,240,.3),rgba(200,100,255,.15));border-color:rgba(180,140,255,.35);color:#fff;box-shadow:0 4px 20px rgba(140,60,240,.2),inset 0 1px 0 rgba(255,255,255,.08);}}
.breadcrumbs{{padding:14px 30px;font-size:11px;color:var(--muted2);border-bottom:1px solid var(--border);}}
.breadcrumbs a{{color:var(--muted);transition:color .15s;}}
.breadcrumbs a:hover{{color:#c080ff;}}
.content{{max-width:820px;margin:0 auto;padding:40px 30px 60px;position:relative;z-index:1;}}
.content h1{{font-family:'Space Grotesk',sans-serif;font-size:30px;font-weight:700;margin-bottom:18px;line-height:1.2;color:#fff;}}
.content h2{{font-family:'Space Grotesk',sans-serif;font-size:21px;font-weight:700;margin:30px 0 12px;color:var(--text);}}
.content h3{{font-size:16px;font-weight:600;margin:22px 0 8px;color:var(--text);}}
.content p{{color:var(--muted);font-size:14px;line-height:1.7;margin-bottom:14px;}}
.content ul,.content ol{{color:var(--muted);font-size:14px;line-height:1.7;margin:0 0 14px 20px;}}
.content li{{margin-bottom:6px;}}
.content a{{color:#c080ff;font-weight:500;}}
.content a:hover{{color:#e0c0ff;}}
.slot-hero{{width:100%;max-width:400px;aspect-ratio:4/3;border-radius:16px;overflow:hidden;margin:0 0 20px;border:1px solid var(--border2);transition:all .3s;box-shadow:0 4px 20px rgba(100,40,200,.1);}}
.slot-hero:hover{{border-color:rgba(180,140,255,.25);box-shadow:0 8px 32px rgba(100,40,200,.15);}}
.slot-hero-bg{{width:100%;height:100%;background-size:cover;background-position:center;}}
.info-box{{background:var(--card);backdrop-filter:blur(12px);border:1px solid var(--border);border-radius:16px;padding:20px 24px;margin:16px 0;transition:all .3s;position:relative;overflow:hidden;}}
.info-box::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.02),transparent);pointer-events:none;border-radius:16px 16px 0 0;}}
.info-box:hover{{border-color:var(--border2);box-shadow:0 4px 20px rgba(100,40,200,.08);}}
.info-box p{{margin-bottom:6px;}}
.info-box p:last-child{{margin-bottom:0;}}
.info-box strong{{color:#fff;}}
.info-box a{{color:#c080ff;}}
.rating-box{{derplay:inline-flex;align-items:center;gap:8px;background:rgba(140,60,240,.08);border:1px solid rgba(140,60,240,.15);border-radius:12px;padding:10px 20px;margin:10px 0;}}
.rating-box .score{{font-family:'Space Grotesk',sans-serif;font-size:26px;font-weight:700;background:linear-gradient(135deg,#c080ff,#80b0ff);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;}}
.rating-box .label{{font-size:12px;color:var(--muted);}}
.cta-box{{text-align:center;margin:32px 0;}}
/* Liquid Glass CTA */
.cta-btn{{derplay:inline-block;background:linear-gradient(135deg,rgba(140,60,240,.25),rgba(200,100,255,.12));backdrop-filter:blur(12px);color:#fff;padding:16px 44px;border-radius:24px;font-size:15px;font-weight:700;transition:all .3s;position:relative;overflow:hidden;border:1px solid rgba(180,140,255,.2);box-shadow:0 4px 24px rgba(130,60,230,.2),0 0 0 1px rgba(255,255,255,.03) inset;}}
.cta-btn::before{{content:'';position:absolute;top:0;left:0;right:0;height:50%;background:linear-gradient(180deg,rgba(255,255,255,.08),transparent);pointer-events:none;border-radius:24px 24px 0 0;}}
.cta-btn::after{{content:'';position:absolute;top:0;left:-100%;width:60%;height:100%;background:linear-gradient(90deg,transparent,rgba(255,255,255,.06),transparent);pointer-events:none;}}
.cta-btn:hover{{text-decoration:none;transform:translateY(-3px);box-shadow:0 8px 36px rgba(130,60,230,.35),0 0 0 1px rgba(255,255,255,.05) inset;border-color:rgba(180,140,255,.35);}}
.cta-btn:hover::after{{animation:btnShine .6s ease-out;}}
.game-grid{{derplay:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;margin:20px 0;}}
.game-card{{background:var(--card);backdrop-filter:blur(8px);border:1px solid var(--border);border-radius:16px;overflow:hidden;transition:all .3s;position:relative;}}
.game-card::before{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,#8040e0,#c060ff,#80b0ff);opacity:0;transition:opacity .3s;z-index:1;}}
.game-card:hover{{transform:translateY(-5px);border-color:rgba(180,140,255,.2);box-shadow:0 8px 28px rgba(100,40,200,.15);}}
.game-card:hover::before{{opacity:1;}}
.game-card-thumb{{width:100%;aspect-ratio:4/3;background-size:cover;background-position:center;}}
.game-card-info{{padding:10px 12px;}}
.game-card-name{{font-size:13px;font-weight:600;color:#fff;}}
.game-card-prov{{font-size:11px;color:var(--muted);}}
.game-card-info{{padding:12px 14px;}}
.footer{{background:rgba(6,4,18,.8);padding:28px 30px 14px;border-top:1px solid var(--border);position:relative;z-index:1;}}
.footer-inner{{max-width:820px;margin:0 auto;}}
.footer-top{{derplay:flex;justify-content:space-between;margin-bottom:18px;gap:30px;}}
.footer-brand{{max-width:280px;}}
.footer-desc{{color:var(--muted2);font-size:10px;line-height:1.6;margin-top:6px;}}
.footer-cols{{derplay:flex;gap:30px;}}
.footer-col-title{{color:var(--muted2);font-size:9px;letter-spacing:1.5px;font-weight:600;margin-bottom:6px;}}
.footer-cols a{{derplay:block;color:var(--muted);font-size:11px;line-height:2.2;transition:color .15s;}}
.footer-cols a:hover{{color:#c080ff;}}
.footer-18{{text-align:center;padding:14px;border:1px solid var(--border);border-radius:12px;background:var(--bg2);margin-bottom:12px;font-size:10px;color:var(--muted2);}}
.footer-18 a{{color:#c080ff;}}
.footer-bottom{{border-top:1px solid var(--border);padding-top:10px;derplay:flex;justify-content:space-between;color:var(--muted2);font-size:9px;}}
@media(max-width:768px){{
  .nav{{padding:10px 16px;flex-wrap:wrap;gap:8px;}}
  .nav-links{{gap:12px;font-size:11px;}}
  .content{{padding:24px 16px 40px;}}
  .content h1{{font-size:24px;}}
  .footer-top{{flex-direction:column;gap:14px;}}
  .game-grid{{grid-template-columns:repeat(2,1fr);}}
}}
</style>
</head>
<body>
{get_nav()}
<div class="breadcrumbs">{bc_html}</div>
<main class="content">
{content}
</main>
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
<p>{"Tekur við Bitcoin, Ethereum, USDT, Litecoin og öðrum dulritunargjaldmiðlum." if c["type"]=="crypto" else "Tekur við Vera, Mastercard, dulritunargjaldmiðlum og rafrænum veskjum."} Þetta er sérstaklega mikilvægt fyrir íslenska leikmenn þar sem innlendir bankar loka oft á spilavíta-færslur.</p>
<h3>Leikir</h3>
<p>{c["name"]} býður upp á yfir 2000 leiki frá fremstu birgjum: Pragmatic Spila, NetEnt, Spila'n GO, Microgaming og fleiri.</p>
<h2>Kostir og gallar</h2>
<ul>
<li>✅ {c["bonus"]}</li>
<li>✅ Hraðar útborganir</li>
<li>✅ {"Dulritunargreiðslur án lokunar" if c["type"]=="crypto" else "Fjölbreytt úrval greiðslumáta"}</li>
<li>✅ Stórt safn leikja</li>
<li>⚠️ Tekur ekki við íslenskum krónum beint</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á {c["name"]} →</a></div>'''

    bc = [("/slotoro-site/", "Heim"), ("/slotoro-site/casino/", "Spilavíti"), ("", c["name"])]
    html = page_template(f'{c["name"]} umsögn', c["desc"], bc, content)
    write_page(f'casino/{c["slug"]}/index.html', html)

# 2. КАТЕГОРИИ КАЗИНО (50)
print("Generating casino categories...")
for cat in casino_categories:
    top_casinos = casinos[:10]
    cards = ""
    for c in top_casinos:
        cards += f'<div class="info-box"><p><strong>{c["name"]}</strong> — {c["bonus"]} (Einkunn: {c["rating"]}/10) <a href="/slotoro-site/casino/{c["slug"]}/">Umsögn →</a></p></div>\n'

    content = f'''<h1>{cat["title"]} á Íslandi 2026</h1>
<p>{cat["desc"]}</p>
<h2>Topp 10 spilavíti í flokki</h2>
{cards}
<h2>Hvernig við veljum bestu spilavítin</h2>
<p>Teymi okkar metur hvert spilavíti út frá nokkrum forsendum: áreiðanleika leyfer, hraða útborgana, gæði leikja, bónustilboðum og aðgengi fyrir íslenska leikmenn.</p>
<p>Við leggjum sérstaka áherslu á stuðning við dulritunargjaldmiðla þar sem íslenskir bankar loka oft á spilavíta-færslur.</p>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/casino/", "Casino"), ("", cat["title"])]
    html = page_template(cat["title"], cat["desc"], bc, content)
    write_page(f'casino/{cat["slug"]}/index.html', html)

# 3. СЛОТЫ (250)
print("Generating slot reviews...")
for s in slots_data:
    cdn_img = ""
    if s.get("cdn"):
        cdn_img = f'<div class="slot-hero"><div class="slot-hero-bg" style="background:url(\'https://cdn.softswers.net/i/s3/{s["cdn"]}\') center/cover,linear-gradient(135deg,#0a1040,#1a2070);"></div></div>'
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
<p>{s["name"]} by {s["provider"]} er einn vinsælasti spilakassinn í «{s["theme"]}» flokknum. Spilakassinn býður upp á {s["volatility"].lower()} sveiflur og hámarksvinninga upp á {s["maxwin"]}.</p>
<h3>RTP og sveifla</h3>
<p>RTP (Return to Spilaer) á {s["name"]} er {s["rtp"]}%. Ther means the slot theoretically returns {s["rtp"]}% af öllum veðmálum til leikmanna til lengri tíma.</p>
<h3>Hvar á að spila {s["name"]}</h3>
<p>Ther slot er available at the following casinos accepting players from Iceland:</p>
<ul>
<li><a href="/slotoro-site/casino/bitstarz/">BitStarz</a> — 5 BTC + 200 FS</li>
<li><a href="/slotoro-site/casino/stake/">Stake</a> — 200% bonus</li>
<li><a href="/slotoro-site/casino/bc-game/">BC.Game</a> — 300% up to 1 BTC</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila {s["name"]} →</a></div>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/slots/", "Slots"), ("", s["name"])]
    html = page_template(f'{s["name"]} Slot', f'{s["name"]} by {s["provider"]} — RTP {s["rtp"]}%, volatility {s["volatility"]}, max {s["maxwin"]}', bc, content)
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
<li><a href="/slotoro-site/casino/bitstarz/">BitStarz</a> — besta úrval lifandi leikja</li>
<li><a href="/slotoro-site/casino/stake/">Stake</a> — einkaréttarborð</li>
<li><a href="/slotoro-site/casino/tonybet/">TonyBet</a> — breitt úrval af takmörkunum</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila {g["name"]} →</a></div>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/live/", "Live Casino"), ("", g["name"])]
    html = page_template(f'{g["name"]} Live', g["desc"], bc, content)
    write_page(f'live/{g["slug"]}/index.html', html)

# 5. БОНУСЫ (80)
print("Generating bonus pages...")
for b in bonus_pages:
    content = f'''<h1>{b["title"]}</h1>
<p>{b["desc"]}</p>
<h2>Bestu tilboðin 2026</h2>
<div class="info-box">
<p><strong>BitStarz:</strong> 5 BTC + 200 free spins — <a href="/slotoro-site/casino/bitstarz/">Nánari upplýsingar →</a></p>
</div>
<div class="info-box">
<p><strong>BC.Game:</strong> 300% crypto bonus — <a href="/slotoro-site/casino/bc-game/">Nánari upplýsingar →</a></p>
</div>
<h2>Hvernig á að fá bónus</h2>
<p>To claim a bonus, regerter at the casino, make a deposit and the bonus will be credited automatically. Pay attention to wagering requirements.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Fá bónus →</a></div>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/bonusy/", "Bónusar"), ("", b["title"])]
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
<li><a href="/slotoro-site/casino/bitstarz/">BitStarz</a> — tafarlausar dulritunarútborganir</li>
<li><a href="/slotoro-site/casino/stake/">Stake</a> — styður 20+ dulritunargjaldmiðla</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Veldu spilavíti →</a></div>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/platezhi/", "Payments"), ("", p["title"])]
    html = page_template(p["title"], p["desc"], bc, content)
    write_page(f'platezhi/{p["slug"]}/index.html', html)

# 7. ГАЙДЫ (60)
print("Generating guides...")
for g in guide_pages:
    content = f'''<h1>{g["title"]}</h1>
<p>{g["desc"]}</p>
<h2>Ítarleg leiðbeining</h2>
<p>In ther guide we cover everything you need to know about «{g["title"]}». Information er up to date for players in Iceland in 2026.</p>
<h3>Lykilatriði</h3>
<ul>
<li>Hvað þarf að vita áður en þú byrjar</li>
<li>Skref-fyrir-skref leiðbeiningar</li>
<li>Common mertakes and how to avoid them</li>
<li>Ráðleggingar frá sérfræðingum BF Casino</li>
</ul>
<h3>Gagnlegir tenglar</h3>
<ul>
<li><a href="/slotoro-site/casino/">Spilavíti umsagnir</a></li>
<li><a href="/slotoro-site/bonusy/">Bónusar</a></li>
<li><a href="/slotoro-site/platezhi/">Greiðslumátar</a></li>
</ul>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/gajdy/", "Guides"), ("", g["title"])]
    html = page_template(g["title"], g["desc"], bc, content)
    write_page(f'gajdy/{g["slug"]}/index.html', html)

# 8. О НАС (10)
print("Generating about pages...")
for a in about_pages:
    content = f'''<h1>{a["title"]}</h1>
<p>{a["desc"]}</p>
<p>BF Casino (bestiflokkurinn.er) er an independent online casino portal for players in Iceland. We help you find reliable casinos with the best bonuses and cryptocurrency support.</p>'''

    bc = [("/slotoro-site/", "Home"), ("", a["title"])]
    html = page_template(a["title"], a["desc"], bc, content)
    write_page(f'{a["slug"]}/index.html', html)

# 9. ИНДЕКСНЫЕ СТРАНИЦЫ РАЗДЕЛОВ
print("Generating index pages...")

# Casino index — FULL landing page (main casino hub)
casino_cards = ""
for c in casinos[:20]:
    ctype_label = "Crypto" if c["type"]=="crypto" else "Classic"
    casino_cards += f'''<a href="/slotoro-site/casino/{c["slug"]}/" class="game-card">
<div class="game-card-thumb" style="background:linear-gradient(135deg,{'#0a2060,#1a40a0' if c['type']=='crypto' else '#2a1040,#5020a0'});derplay:flex;align-items:center;justify-content:center;"><span style="font-size:28px;font-weight:800;color:rgba(255,255,255,.15);">{c["rating"]}</span></div>
<div class="game-card-info"><div class="game-card-name">{c["name"]}</div><div class="game-card-prov">{c["bonus"]} · {ctype_label}</div></div></a>\n'''

casino_lert = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/casino/{c["slug"]}/">{c["name"]}</a></strong> — {c["bonus"]} (Einkunn: {c["rating"]}/10)</p></div>' for c in casinos[:50]])

casino_content = f'''<h1>Best Online Casinos Iceland 2026</h1>
<p>BF Casino reviews {len(casinos)} online casinos for Icelandic players. Compare bonuses, payment methods and game libraries. Öll casinos lerted support cryptocurrency — the easiest way to play from Iceland.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á Top Casino →</a></div>
<h2>Topp 20 spilavíti</h2>
<div class="game-grid">{casino_cards}</div>
<h2>Öll {len(casinos)} Spilavíti umsagnir</h2>
{casino_lert}'''

write_page("casino/index.html", page_template("Best Online Casinos Iceland 2026", f"Compare {len(casinos)} online casinos for Iceland. Crypto payments, fast withdrawals, welcome bonuses.",
    [("/slotoro-site/", "Home"), ("", "Casino")],
    casino_content))

# Slots index
slots_lert = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/slots/{s["slug"]}/">{s["name"]}</a></strong> — {s["provider"]} | RTP {s["rtp"]}% | {s["maxwin"]}</p></div>' for s in slots_data[:30]])
write_page("slots/index.html", page_template("Öll Slots", "Umsagnir um popular slots",
    [("/slotoro-site/", "Home"), ("", "Slots")],
    f'<h1>Vinsælir spilakassar 2026</h1><p>Umsagnir um {len(slots_data)} spilakassa frá fremstu birgjum.</p>{slots_lert}'))

# Live index
live_lert = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/live/{g["slug"]}/">{g["name"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in live_games[:20]])
write_page("live/index.html", page_template("Live Casino", "Leikir með lifandi spilastjórum",
    [("/slotoro-site/", "Home"), ("", "Live Casino")],
    f'<h1>Spilavíti í beinni — Leikir með lifandi spilastjórum</h1><p>{len(live_games)} leikir með faglegum spilastjórum.</p>{live_lert}'))

# Bonus index
bonus_lert = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/bonusy/{b["slug"]}/">{b["title"]}</a></strong> — {b["desc"][:80]}</p></div>' for b in bonus_pages[:20]])
write_page("bonusy/index.html", page_template("Casino Bónusar", "Öllir bónusar og afsláttarkóðar",
    [("/slotoro-site/", "Home"), ("", "Bónusar")],
    f'<h1>Casino Bónusar 2026</h1><p>{len(bonus_pages)} virk bónustilboð.</p>{bonus_lert}'))

# Payment index
pay_lert = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/platezhi/{p["slug"]}/">{p["title"]}</a></strong></p></div>' for p in payment_pages[:20]])
write_page("platezhi/index.html", page_template("Greiðslumátar", "Dulritunargjaldmiðlar og aðrar greiðslur í spilavítum",
    [("/slotoro-site/", "Home"), ("", "Payments")],
    f'<h1>Casino Greiðslumátar</h1><p>Hvernig á að komast framhjá lokun banka og spila frá Íslandi.</p>{pay_lert}'))

# Guide index
guide_lert = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/gajdy/{g["slug"]}/">{g["title"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in guide_pages[:20]])
write_page("gajdy/index.html", page_template("Guides", "Leiðbeiningar og kennsluefni fyrir leikmenn",
    [("/slotoro-site/", "Home"), ("", "Guides")],
    f'<h1>Leiðbeiningar fyrir leikmenn</h1><p>{len(guide_pages)} leiðbeiningar fyrir byrjendur og reynda leikmenn.</p>{guide_lert}'))


# 10. SITEMAP
print("Generating sitemap.xml...")
sitemap_urls = ['https://bestiflokkurinn.er/']
for c in casinos:
    sitemap_urls.append(f'https://bestiflokkurinn.er/casino/{c["slug"]}/')
for cat in casino_categories:
    sitemap_urls.append(f'https://bestiflokkurinn.er/casino/{cat["slug"]}/')
for s in slots_data:
    sitemap_urls.append(f'https://bestiflokkurinn.er/slots/{s["slug"]}/')
for g in live_games:
    sitemap_urls.append(f'https://bestiflokkurinn.er/live/{g["slug"]}/')
for b in bonus_pages:
    sitemap_urls.append(f'https://bestiflokkurinn.er/bonusy/{b["slug"]}/')
for p in payment_pages:
    sitemap_urls.append(f'https://bestiflokkurinn.er/platezhi/{p["slug"]}/')
for g in guide_pages:
    sitemap_urls.append(f'https://bestiflokkurinn.er/gajdy/{g["slug"]}/')
for a in about_pages:
    sitemap_urls.append(f'https://bestiflokkurinn.er/{a["slug"]}/')
sitemap_urls.extend([
    'https://bestiflokkurinn.er/casino/',
    'https://bestiflokkurinn.er/slots/',
    'https://bestiflokkurinn.er/live/',
    'https://bestiflokkurinn.er/bonusy/',
    'https://bestiflokkurinn.er/platezhi/',
    'https://bestiflokkurinn.er/gajdy/',
])

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_xml += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
sitemap_xml += '</urlset>'

with open(os.path.join(BASE, 'sitemap.xml'), 'w') as f:
    f.write(sitemap_xml)

# robots.txt
with open(os.path.join(BASE, 'robots.txt'), 'w') as f:
    f.write('User-agent: *\nÖllow: /\nSitemap: https://bestiflokkurinn.er/sitemap.xml\n')

print(f"\n✅ Generated {count} pages + sitemap.xml + robots.txt")
print(f"URLs in sitemap: {len(sitemap_urls)}")
