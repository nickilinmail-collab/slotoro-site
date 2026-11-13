#!/usr/bin/env python3
"""
Bestiflokkurinn.is — генератор 800 страниц казино-портала
Сначала на русском, потом переведём на исландский
"""
import os
import json

# ============================================================
# ДАННЫЕ СТРАНИЦ
# ============================================================

# 150 казино обзоров
casinos = [
    {"slug": "bitstarz", "name": "BitStarz", "rating": 9.8, "bonus": "5 BTC + 200 FS", "type": "crypto", "desc": "Лучшее крипто-казино с мгновенными выплатами. Более 3000 игр от топовых провайдеров."},
    {"slug": "stake", "name": "Stake", "rating": 9.6, "bonus": "200% + VIP", "type": "crypto", "desc": "Популярное крипто-казино с VIP программой и эксклюзивными играми."},
    {"slug": "bc-game", "name": "BC.Game", "rating": 9.4, "bonus": "300% до 1 BTC", "type": "crypto", "desc": "Инновационное казино с собственными играми и криптовалютными бонусами."},
    {"slug": "tonybet", "name": "TonyBet", "rating": 9.2, "bonus": "150% + 100 FS", "type": "classic", "desc": "Надёжное казино с широким выбором слотов и live-игр."},
    {"slug": "epicbet", "name": "Epicbet", "rating": 9.0, "bonus": "100% до €500", "type": "classic", "desc": "Современное казино с быстрыми выплатами и отличной поддержкой."},
    {"slug": "respin", "name": "Respin Casino", "rating": 8.9, "bonus": "200% + 50 FS", "type": "classic", "desc": "Казино с огромной библиотекой слотов и щедрыми бонусами."},
    {"slug": "vegazone", "name": "VegaZone", "rating": 8.8, "bonus": "150% до €300", "type": "classic", "desc": "Стильное казино с эксклюзивными турнирами и акциями."},
    {"slug": "wildcoins", "name": "WildCoins", "rating": 8.7, "bonus": "250% + 100 FS", "type": "crypto", "desc": "Крипто-казино с дикими бонусами и быстрым выводом."},
    {"slug": "katsubet", "name": "KatsuBet", "rating": 8.6, "bonus": "100% + 100 FS", "type": "crypto", "desc": "Японская тематика, криптовалюты и тысячи слотов."},
    {"slug": "winz", "name": "Winz.io", "rating": 8.5, "bonus": "300 FS без вейджера", "type": "crypto", "desc": "Уникальные бонусы без требований к отыгрышу."},
    {"slug": "7bit", "name": "7Bit Casino", "rating": 8.5, "bonus": "200% + 100 FS", "type": "crypto", "desc": "Ретро-стиль с современными крипто-функциями."},
    {"slug": "mbitcasino", "name": "mBit Casino", "rating": 8.4, "bonus": "175% + 300 FS", "type": "crypto", "desc": "Одно из старейших крипто-казино с проверенной репутацией."},
    {"slug": "cloudbet", "name": "Cloudbet", "rating": 8.4, "bonus": "100% до 5 BTC", "type": "crypto", "desc": "Премиальное крипто-казино с высокими лимитами."},
    {"slug": "casinonic", "name": "Casinonic", "rating": 8.3, "bonus": "100% + 100 FS", "type": "classic", "desc": "Простое и удобное казино для новичков."},
    {"slug": "national-casino", "name": "National Casino", "rating": 8.3, "bonus": "100% + 100 FS", "type": "classic", "desc": "Казино с отличной коллекцией live-игр."},
    {"slug": "20bet", "name": "20Bet", "rating": 8.2, "bonus": "100% до €120", "type": "classic", "desc": "Универсальная платформа с казино и ставками."},
    {"slug": "rocketplay", "name": "RocketPlay", "rating": 8.2, "bonus": "150% + 100 FS", "type": "crypto", "desc": "Космическая тематика и быстрые крипто-выплаты."},
    {"slug": "hellspin", "name": "HellSpin", "rating": 8.1, "bonus": "150% + 50 FS", "type": "crypto", "desc": "Дерзкое казино с агрессивными бонусами."},
    {"slug": "neospin", "name": "NeoSpin", "rating": 8.1, "bonus": "100% + 100 FS", "type": "crypto", "desc": "Футуристическое казино нового поколения."},
    {"slug": "betpanda", "name": "BetPanda", "rating": 8.0, "bonus": "100% до 1 BTC", "type": "crypto", "desc": "Дружелюбное крипто-казино с низким вейджером."},
]

# Генерируем ещё 130 казино
extra_casino_names = [
    "LuckyStar", "IceBet", "NordicSlots", "FrostBet", "SnowCasino", "AuroraBet",
    "VikingSlots", "ThunderBet", "GlacierCasino", "BorealisBet", "CrystalSlots",
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
    bonus_options = ["100% до €200", "150% + 50 FS", "200% до €500", "50 FS бесплатно", "100% до 0.5 BTC", "125% + 75 FS", "100% до €300"]
    bonus = bonus_options[i % len(bonus_options)]
    casinos.append({
        "slug": slug,
        "name": name,
        "rating": rating,
        "bonus": bonus,
        "type": ctype,
        "desc": f"{name} — онлайн казино с лицензией и быстрыми выплатами. {bonus} для новых игроков."
    })

# 250 слотов
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
    {"slug": "tombstone-rip", "name": "Tombstone RIP", "provider": "NoLimit City", "rtp": 96.08, "volatility": "Экстрим", "maxwin": "x300000", "theme": "Вестерн"},
    {"slug": "fruit-party", "name": "Fruit Party", "provider": "Pragmatic Play", "rtp": 96.47, "volatility": "Высокая", "maxwin": "x5000", "theme": "Фрукты"},
    {"slug": "buffalo-king-megaways", "name": "Buffalo King Megaways", "provider": "Pragmatic Play", "rtp": 96.52, "volatility": "Высокая", "maxwin": "x5000", "theme": "Природа"},
    {"slug": "legacy-of-dead", "name": "Legacy of Dead", "provider": "Play'n GO", "rtp": 96.58, "volatility": "Высокая", "maxwin": "x5000", "theme": "Египет"},
]

# Ещё 230 слотов
more_slot_names = [
    ("Madame Destiny Megaways", "Pragmatic Play", 96.56, "x5000", "Магия"),
    ("Great Rhino Megaways", "Pragmatic Play", 96.58, "x20000", "Природа"),
    ("John Hunter and the Tomb", "Pragmatic Play", 96.5, "x5000", "Приключения"),
    ("Floating Dragon", "Pragmatic Play", 96.71, "x5000", "Азия"),
    ("Sugar Rush", "Pragmatic Play", 96.5, "x5000", "Сладости"),
    ("Starlight Princess", "Pragmatic Play", 96.5, "x5000", "Аниме"),
    ("Wild West Gold", "Pragmatic Play", 96.51, "x10000", "Вестерн"),
    ("Release the Kraken", "Pragmatic Play", 96.5, "x3000", "Океан"),
    ("Gems Bonanza", "Pragmatic Play", 96.51, "x10000", "Камни"),
    ("Aztec Gems", "Pragmatic Play", 96.52, "x375", "Ацтеки"),
    ("Hot Fiesta", "Pragmatic Play", 96.56, "x5000", "Мексика"),
    ("Pirate Gold Deluxe", "Pragmatic Play", 96.48, "x15000", "Пираты"),
    ("Emerald King", "Pragmatic Play", 96.51, "x5000", "Ирландия"),
    ("Book of Fallen", "Pragmatic Play", 96.5, "x5000", "Египет"),
    ("Rise of Giza", "Pragmatic Play", 96.5, "x5000", "Египет"),
    ("Cleocatra", "Pragmatic Play", 96.2, "x5000", "Египет"),
    ("Zeus vs Hades", "Pragmatic Play", 96.07, "x15000", "Мифология"),
    ("Big Bass Bonanza", "Pragmatic Play", 96.71, "x2100", "Рыбалка"),
    ("Big Bass Amazon", "Pragmatic Play", 96.71, "x2100", "Рыбалка"),
    ("Bigger Bass Bonanza", "Pragmatic Play", 96.71, "x4000", "Рыбалка"),
    ("Rise of Samurai Megaways", "Pragmatic Play", 96.5, "x5000", "Самураи"),
    ("Hand of Midas", "Pragmatic Play", 96.54, "x5000", "Мифология"),
    ("Wild West Gold Megaways", "Pragmatic Play", 96.48, "x10000", "Вестерн"),
    ("Juicy Fruits", "Pragmatic Play", 96.53, "x4000", "Фрукты"),
    ("Cash Bonanza", "Pragmatic Play", 96.56, "x5000", "Деньги"),
    ("Moon Princess", "Play'n GO", 96.2, "x5000", "Аниме"),
    ("Rich Wilde and the Amulet", "Play'n GO", 96.29, "x10000", "Приключения"),
    ("Rise of Olympus", "Play'n GO", 96.5, "x5000", "Мифология"),
    ("Immortal Romance", "Microgaming", 96.86, "x12150", "Вампиры"),
    ("Thunderstruck II", "Microgaming", 96.65, "x8000", "Мифология"),
    ("Mega Moolah", "Microgaming", 88.12, "Прогрессив", "Сафари"),
    ("Avalon II", "Microgaming", 97.0, "x120", "Артурианна"),
    ("Vikings Go Berzerk", "Yggdrasil", 96.1, "x5000", "Викинги"),
    ("Valley of the Gods", "Yggdrasil", 96.2, "x3600", "Египет"),
    ("Trolls Bridge", "Yggdrasil", 96.3, "x4500", "Фэнтези"),
    ("Holmes and the Stolen Stones", "Yggdrasil", 96.8, "x1000", "Детектив"),
    ("Nitro Circus", "Yggdrasil", 96.1, "x2000", "Экстрим"),
    ("Lucha Maniacs", "Yggdrasil", 96.2, "x3000", "Борьба"),
    ("Hades - Gigablox", "Yggdrasil", 96.1, "x11129", "Мифология"),
    ("9 Masks of Fire", "Gameburger", 96.24, "x2000", "Африка"),
    ("Divine Fortune", "NetEnt", 96.59, "Прогрессив", "Мифология"),
    ("Blood Suckers", "NetEnt", 98.0, "x900", "Вампиры"),
    ("Jack and the Beanstalk", "NetEnt", 96.28, "x1000", "Сказки"),
    ("Twin Spin", "NetEnt", 96.56, "x1080", "Классика"),
    ("Narcos", "NetEnt", 96.23, "x1506", "Криминал"),
    ("Finn and the Swirly Spin", "NetEnt", 96.62, "x500", "Ирландия"),
    ("Aloha! Cluster Pays", "NetEnt", 96.42, "x2000", "Гаваи"),
    ("Sakura Fortune", "Quickspin", 96.58, "x1300", "Азия"),
    ("Dwarven Gold", "Pragmatic Play", 96.49, "x1000", "Фэнтези"),
]

for i, (name, provider, rtp, maxwin, theme) in enumerate(more_slot_names):
    slug = name.lower().replace("'", "").replace(" ", "-").replace(":", "").replace("!", "")
    slots_data.append({
        "slug": slug,
        "name": name,
        "provider": provider,
        "rtp": rtp,
        "volatility": "Высокая" if i % 3 != 2 else "Средняя",
        "maxwin": maxwin,
        "theme": theme
    })

# Добавим ещё 180 слотов
generic_slot_themes = ["Египет","Фрукты","Космос","Океан","Сказки","Викинги","Азия","Пираты","Мифология","Вестерн","Природа","Деньги","Хоррор","Фэнтези","Классика"]
generic_providers = ["Pragmatic Play","NetEnt","Play'n GO","Microgaming","Yggdrasil","Push Gaming","Hacksaw Gaming","NoLimit City","Red Tiger","Thunderkick","Relax Gaming","ELK Studios","Big Time Gaming","Blueprint Gaming","iSoftBet"]
for i in range(180):
    n = f"Slot Game {i+70}"
    slug = f"slot-game-{i+70}"
    slots_data.append({
        "slug": slug,
        "name": n,
        "provider": generic_providers[i % len(generic_providers)],
        "rtp": round(95.5 + (i % 30) * 0.1, 2),
        "volatility": ["Низкая","Средняя","Высокая","Экстрим"][i % 4],
        "maxwin": f"x{(i+1)*500}",
        "theme": generic_slot_themes[i % len(generic_slot_themes)]
    })

# Категории казино (50 страниц)
casino_categories = [
    {"slug": "luchshie-online-casino", "title": "Лучшие онлайн казино", "desc": "Рейтинг лучших онлайн казино для игроков из Исландии."},
    {"slug": "crypto-casino", "title": "Крипто казино", "desc": "Казино принимающие Bitcoin, Ethereum и другие криптовалюты."},
    {"slug": "novye-casino", "title": "Новые казино 2026", "desc": "Самые новые онлайн казино открытые в 2026 году."},
    {"slug": "casino-s-bystrym-vyvodom", "title": "Казино с быстрым выводом", "desc": "Казино где вывод средств занимает менее 24 часов."},
    {"slug": "casino-bez-verifikacii", "title": "Казино без верификации", "desc": "Казино не требующие верификации документов."},
    {"slug": "bitcoin-casino", "title": "Bitcoin казино", "desc": "Лучшие казино для депозитов и выводов в Bitcoin."},
    {"slug": "ethereum-casino", "title": "Ethereum казино", "desc": "Казино принимающие Ethereum для депозитов."},
    {"slug": "usdt-casino", "title": "USDT казино", "desc": "Казино принимающие стейблкоин USDT."},
    {"slug": "litecoin-casino", "title": "Litecoin казино", "desc": "Казино с депозитами в Litecoin."},
    {"slug": "live-casino", "title": "Live казино", "desc": "Лучшие казино с живыми дилерами."},
    {"slug": "casino-s-bonusom", "title": "Казино с бонусом", "desc": "Казино предлагающие щедрые приветственные бонусы."},
    {"slug": "casino-bez-depozita", "title": "Казино без депозита", "desc": "Бонусы без необходимости вносить депозит."},
    {"slug": "casino-s-frispinami", "title": "Казино с фриспинами", "desc": "Казино дающие бесплатные вращения при регистрации."},
    {"slug": "mobilnoe-casino", "title": "Мобильное казино", "desc": "Лучшие казино для игры на телефоне."},
    {"slug": "casino-s-niskim-depozitom", "title": "Казино с низким депозитом", "desc": "Казино где можно играть от 1€."},
    {"slug": "vip-casino", "title": "VIP казино", "desc": "Казино с лучшими VIP и лоялти программами."},
    {"slug": "megaways-casino", "title": "Megaways казино", "desc": "Казино с большим выбором Megaways слотов."},
    {"slug": "jackpot-casino", "title": "Джекпот казино", "desc": "Казино с прогрессивными джекпотами."},
    {"slug": "casino-s-vysokim-rtp", "title": "Казино с высоким RTP", "desc": "Казино предлагающие слоты с RTP выше 97%."},
    {"slug": "casino-s-licenziej", "title": "Казино с лицензией", "desc": "Проверенные лицензированные казино."},
]

# Ещё 30 категорий
more_cats = [
    "Казино Curacao", "Казино Malta (MGA)", "Казино с кешбэком", "Казино с турнирами",
    "Казино для хайроллеров", "Казино с минимальным вейджером", "Казино с бонус-кодами",
    "Казино с приложением", "Казино с быстрой регистрацией", "Казино с рулеткой",
    "Казино с блэкджеком", "Казино с баккарой", "Казино с покером", "Казино с лотереей",
    "Казино с бинго", "Казино со скретч-картами", "Казино с краш-играми", "Казино с Plinko",
    "Казино с Aviator", "Казино с Mines", "Казино с Dice", "Казино с автоматами",
    "Казино с 3D слотами", "Казино с Bonus Buy", "Казино с Drops & Wins",
    "Казино с быстрыми играми", "Казино с провайдером Pragmatic", "Казино с провайдером NetEnt",
    "Казино с провайдером Evolution", "Казино с провайдером Play'n GO"
]
for i, title in enumerate(more_cats):
    slug = title.lower().replace("'", "").replace(" ", "-").replace("(", "").replace(")", "")
    casino_categories.append({"slug": slug, "title": title, "desc": f"Обзор и рейтинг: {title} в Исландии."})

# Live казино (50 страниц)
live_games = [
    {"slug": "blackjack", "name": "Блэкджек", "desc": "Онлайн блэкджек с живым дилером — правила, стратегии и лучшие столы."},
    {"slug": "roulette", "name": "Рулетка", "desc": "Живая рулетка онлайн — европейская, французская и американская."},
    {"slug": "baccarat", "name": "Баккара", "desc": "Баккара с живым дилером — как играть и выигрывать."},
    {"slug": "poker", "name": "Покер", "desc": "Casino Hold'em и другие виды покера с живым дилером."},
    {"slug": "dream-catcher", "name": "Dream Catcher", "desc": "Колесо фортуны от Evolution — правила и стратегии."},
    {"slug": "monopoly-live", "name": "Monopoly Live", "desc": "Монополия в реальном времени с живым ведущим."},
    {"slug": "crazy-time", "name": "Crazy Time", "desc": "Самое популярное шоу от Evolution Gaming."},
    {"slug": "lightning-roulette", "name": "Lightning Roulette", "desc": "Рулетка с молниями и множителями до x500."},
    {"slug": "mega-ball", "name": "Mega Ball", "desc": "Лотерея с живым ведущим и множителями."},
    {"slug": "gonzo-treasure-hunt", "name": "Gonzo's Treasure Hunt", "desc": "Охота за сокровищами с Гонзо."},
]
# Ещё 40 live игр
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
    live_games.append({"slug": slug, "name": name, "desc": f"{name} — играйте с живым дилером в лучших казино Исландии."})

# Бонусы (80 страниц)
bonus_pages = [
    {"slug": "velkomstbonus", "title": "Приветственный бонус", "desc": "Лучшие приветственные бонусы в онлайн казино Исландии."},
    {"slug": "frispiny-bez-depozita", "title": "Фриспины без депозита", "desc": "Бесплатные вращения без необходимости вносить депозит."},
    {"slug": "bezdepozitnye-bonusy", "title": "Бездепозитные бонусы", "desc": "Все бонусы без депозита в казино Исландии."},
    {"slug": "keshbek", "title": "Кешбэк бонусы", "desc": "Казино с возвратом проигранных средств."},
    {"slug": "bonus-za-registraciyu", "title": "Бонус за регистрацию", "desc": "Получите бонус сразу после регистрации."},
    {"slug": "bonus-na-pervyj-depozit", "title": "Бонус на первый депозит", "desc": "Лучшие бонусы на первое пополнение счёта."},
    {"slug": "bonus-na-vtoroj-depozit", "title": "Бонус на второй депозит", "desc": "Бонусы на второе пополнение."},
    {"slug": "vejer", "title": "Что такое вейджер", "desc": "Объяснение требований к отыгрышу бонусов."},
    {"slug": "bonus-kody", "title": "Бонус-коды казино", "desc": "Актуальные промокоды для онлайн казино."},
    {"slug": "reload-bonus", "title": "Релоад бонусы", "desc": "Бонусы на повторные депозиты."},
]
# Ещё 70 бонус-страниц по казино
for casino in casinos[:70]:
    bonus_pages.append({
        "slug": f"bonus-{casino['slug']}",
        "title": f"Бонус {casino['name']}",
        "desc": f"Актуальные бонусы и промокоды {casino['name']} — {casino['bonus']}."
    })

# Платежи (50 страниц)
payment_pages = [
    {"slug": "bitcoin", "title": "Bitcoin в казино", "desc": "Как использовать Bitcoin для депозитов и выводов в онлайн казино."},
    {"slug": "ethereum", "title": "Ethereum в казино", "desc": "Депозиты и выводы через Ethereum."},
    {"slug": "usdt", "title": "USDT (Tether) в казино", "desc": "Использование стейблкоина USDT в онлайн казино."},
    {"slug": "litecoin", "title": "Litecoin в казино", "desc": "Быстрые платежи через Litecoin."},
    {"slug": "dogecoin", "title": "Dogecoin в казино", "desc": "Как играть в казино с Dogecoin."},
    {"slug": "ripple-xrp", "title": "Ripple (XRP) в казино", "desc": "Платежи через XRP в онлайн казино."},
    {"slug": "cardano", "title": "Cardano (ADA) в казино", "desc": "Использование ADA для игры в казино."},
    {"slug": "solana", "title": "Solana (SOL) в казино", "desc": "Быстрые SOL-транзакции в казино."},
    {"slug": "bnb", "title": "BNB в казино", "desc": "Binance Coin для депозитов в казино."},
    {"slug": "tron", "title": "TRON (TRX) в казино", "desc": "Низкие комиссии с TRON."},
    {"slug": "kak-kupit-bitcoin", "title": "Как купить Bitcoin", "desc": "Пошаговый гайд по покупке Bitcoin для казино."},
    {"slug": "kak-kupit-ethereum", "title": "Как купить Ethereum", "desc": "Где и как купить ETH."},
    {"slug": "obhod-blokirovok-bankov", "title": "Обход банковских блокировок", "desc": "Как обойти блокировки исландских банков на казино-транзакции."},
    {"slug": "kripto-koshelki", "title": "Крипто-кошельки", "desc": "Лучшие кошельки для хранения криптовалют."},
    {"slug": "metamask-casino", "title": "MetaMask для казино", "desc": "Как использовать MetaMask для казино."},
    {"slug": "trust-wallet-casino", "title": "Trust Wallet для казино", "desc": "Депозиты через Trust Wallet."},
    {"slug": "binance-casino", "title": "Binance для казино", "desc": "Как переводить средства с Binance в казино."},
    {"slug": "coinbase-casino", "title": "Coinbase для казино", "desc": "Покупка крипто через Coinbase для казино."},
    {"slug": "kraken-casino", "title": "Kraken для казино", "desc": "Использование биржи Kraken."},
    {"slug": "vpn-casino", "title": "VPN для казино", "desc": "Нужен ли VPN для игры в казино из Исландии."},
]
# Ещё 30 платежных страниц
more_payments = [
    "Visa в казино", "Mastercard в казино", "Apple Pay в казино", "Google Pay в казино",
    "Skrill в казино", "Neteller в казино", "ecoPayz в казино", "MiFinity в казино",
    "Jeton в казино", "CashtoCode в казино", "Neosurf в казино", "Paysafecard в казино",
    "AstroPay в казино", "MuchBetter в казино", "Interac в казино", "iDebit в казино",
    "Instadebit в казино", "Flexepin в казино", "Monero в казино", "Bitcoin Cash в казино",
    "Polkadot в казино", "Avalanche в казино", "Polygon в казино", "Arbitrum в казино",
    "Optimism в казино", "Минимальный депозит 1€", "Минимальный депозит 5€", "Минимальный депозит 10€",
    "Вывод на карту", "Быстрый вывод крипто"
]
for title in more_payments:
    slug = title.lower().replace("€", "eur").replace(" ", "-").replace("(", "").replace(")", "")
    payment_pages.append({"slug": slug, "title": title, "desc": f"{title} — полный гайд для игроков из Исландии."})

# Гайды (60 страниц)
guide_pages = [
    {"slug": "kak-vybrat-casino", "title": "Как выбрать онлайн казино", "desc": "Полное руководство по выбору надёжного казино."},
    {"slug": "chto-takoe-rtp", "title": "Что такое RTP", "desc": "Объяснение Return to Player — процента возврата."},
    {"slug": "chto-takoe-volatilnost", "title": "Что такое волатильность", "desc": "Разница между низкой, средней и высокой волатильностью."},
    {"slug": "kak-igrat-v-sloty", "title": "Как играть в слоты", "desc": "Пошаговое руководство для начинающих."},
    {"slug": "strategii-blackjack", "title": "Стратегии блэкджека", "desc": "Базовая стратегия и карточка для блэкджека."},
    {"slug": "pravila-ruletki", "title": "Правила рулетки", "desc": "Как играть в рулетку — полное руководство."},
    {"slug": "pravila-bakkary", "title": "Правила баккары", "desc": "Как играть в баккару."},
    {"slug": "kak-vyigrat-v-casino", "title": "Как выиграть в казино", "desc": "Советы и стратегии для увеличения шансов."},
    {"slug": "otvetstvennaya-igra", "title": "Ответственная игра", "desc": "Как играть ответственно и контролировать расходы."},
    {"slug": "zakon-ob-azartnyh-igrah-islandiya", "title": "Закон об азартных играх Исландии", "desc": "Правовой статус онлайн казино в Исландии."},
    {"slug": "nalogi-na-vyigrysh", "title": "Налоги на выигрыш", "desc": "Нужно ли платить налоги с выигрыша в Исландии."},
    {"slug": "bezopasnost-v-casino", "title": "Безопасность в казино", "desc": "Как защитить свои данные при игре онлайн."},
    {"slug": "glossarij-casino", "title": "Глоссарий казино", "desc": "Все термины казино от А до Я."},
    {"slug": "provajdery-igr", "title": "Провайдеры игр", "desc": "Обзор крупнейших разработчиков слотов."},
    {"slug": "megaways-sloty", "title": "Что такое Megaways", "desc": "Как работает механика Megaways."},
    {"slug": "bonus-buy-sloty", "title": "Слоты с Bonus Buy", "desc": "Как работает покупка бонуса."},
    {"slug": "progressivnye-jackpoty", "title": "Прогрессивные джекпоты", "desc": "Как выиграть прогрессивный джекпот."},
    {"slug": "turniry-v-casino", "title": "Турниры в казино", "desc": "Как участвовать в слот-турнирах."},
    {"slug": "vip-programmy", "title": "VIP программы", "desc": "Как работают VIP и лоялти программы."},
    {"slug": "casino-na-telefone", "title": "Казино на телефоне", "desc": "Лучшие мобильные казино и приложения."},
]
# Ещё 40 гайдов
more_guides = [
    "Как вывести деньги из казино", "Как пополнить счёт в казино", "Что такое вагерные требования",
    "Как работает генератор случайных чисел", "Разница между слотами и автоматами",
    "Казино с лицензией Curacao", "Казино с лицензией MGA", "Казино с лицензией UK",
    "Как проверить лицензию казино", "Что такое KYC верификация",
    "Как выбрать слот с высоким RTP", "Топ-10 слотов для новичков", "Топ-10 слотов для хайроллеров",
    "Слоты с максимальным выигрышем", "Слоты с низкой волатильностью",
    "Как играть в краш-игры", "Как играть в Plinko", "Как играть в Aviator",
    "Как играть в Mines", "Как играть в Dice",
    "Что такое провайдер Evolution", "Что такое провайдер Pragmatic Play", "Что такое провайдер NetEnt",
    "История казино в Исландии", "Онлайн казино vs наземные казино",
    "Криптовалюты vs фиат в казино", "Преимущества крипто-казино",
    "Как избежать мошенничества", "Признаки честного казино", "Чёрный список казино",
    "Как связаться с поддержкой казино", "Как подать жалобу на казино",
    "Сравнение бонусов разных казино", "Как использовать бонус максимально эффективно",
    "Стратегия управления банкроллом", "Психология азартных игр",
    "Зависимость от азартных игр — помощь", "Сайты помощи при игровой зависимости",
    "Самоисключение из казино", "Лимиты депозитов и проигрыша"
]
for title in more_guides:
    slug = title.lower().replace("—", "").replace("ё", "е").replace(" ", "-").replace(",", "").replace(".", "")
    guide_pages.append({"slug": slug, "title": title, "desc": f"{title} — подробное руководство."})

# О нас (10 страниц)
about_pages = [
    {"slug": "o-nas", "title": "О Bestiflokkurinn", "desc": "Кто мы и почему создали Bestiflokkurinn."},
    {"slug": "kontakty", "title": "Контакты", "desc": "Свяжитесь с командой Bestiflokkurinn."},
    {"slug": "konfidencialnost", "title": "Политика конфиденциальности", "desc": "Как мы обрабатываем ваши данные."},
    {"slug": "usloviya", "title": "Условия использования", "desc": "Правила использования сайта Bestiflokkurinn."},
    {"slug": "otkaz-ot-otvetstvennosti", "title": "Отказ от ответственности", "desc": "Важная юридическая информация."},
    {"slug": "kak-my-ocenivaem", "title": "Как мы оцениваем казино", "desc": "Наша методология оценки."},
    {"slug": "redakcionnaya-politika", "title": "Редакционная политика", "desc": "Принципы нашей редакции."},
    {"slug": "partnerstvo", "title": "Партнёрство", "desc": "Сотрудничество с Bestiflokkurinn."},
    {"slug": "karta-sajta", "title": "Карта сайта", "desc": "Полная карта всех страниц Bestiflokkurinn."},
    {"slug": "otvetstvennaya-igra-stranica", "title": "Ответственная игра", "desc": "Наша позиция по ответственной игре."},
]


# ============================================================
# HTML ШАБЛОН
# ============================================================

def get_nav():
    return '''<nav class="nav">
  <a href="/slotoro-site/" class="nav-logo">
    <svg width="32" height="32" viewBox="0 0 46 46" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="lg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#4da8ff"/><stop offset="50%" stop-color="#4dd9ff"/><stop offset="100%" stop-color="#e84050"/></linearGradient></defs><rect width="46" height="46" rx="12" fill="url(#lg)"/><text x="23" y="30" text-anchor="middle" font-family="Space Grotesk,sans-serif" font-size="20" font-weight="700" fill="#fff">BF</text></svg>
    <div class="logo-text">BF Casino</div>
  </a>
  <div class="nav-links">
    <a href="/slotoro-site/">Home</a>
    <a href="/slotoro-site/casino/">Casino</a>
    <a href="/slotoro-site/slots/">Slots</a>
    <a href="/slotoro-site/bonusy/">Bonuses</a>
    <a href="/slotoro-site/live/">Live</a>
    <a href="/slotoro-site/platezhi/">Payments</a>
    <a href="/slotoro-site/gajdy/">Guides</a>
  </div>
  <div class="nav-actions">
    <a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="btn-signup">Sign Up</a>
  </div>
</nav>'''

def get_footer():
    return '''<footer class="footer">
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;">
          <svg width="24" height="24" viewBox="0 0 46 46" xmlns="http://www.w3.org/2000/svg"><defs><linearGradient id="flg" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="#4da8ff"/><stop offset="50%" stop-color="#4dd9ff"/><stop offset="100%" stop-color="#e84050"/></linearGradient></defs><rect width="46" height="46" rx="12" fill="url(#flg)"/><text x="23" y="30" text-anchor="middle" font-family="Space Grotesk,sans-serif" font-size="20" font-weight="700" fill="#fff">BF</text></svg>
          <span style="font-family:Space Grotesk,sans-serif;font-size:16px;font-weight:700;color:#fff;">BF Casino</span>
        </div>
        <div class="footer-desc">BF Casino at bestiflokkurinn.is — independent casino comparison site. We may earn a commission through our links. 18+ Play responsibly.</div>
      </div>
      <div class="footer-cols">
        <div><div class="footer-col-title">CASINO</div><a href="/slotoro-site/casino/">Reviews</a><a href="/slotoro-site/bonusy/">Bonuses</a><a href="/slotoro-site/casino/crypto-casino/">Crypto</a></div>
        <div><div class="footer-col-title">GAMES</div><a href="/slotoro-site/slots/">Slots</a><a href="/slotoro-site/live/">Live Casino</a></div>
        <div><div class="footer-col-title">INFO</div><a href="/slotoro-site/o-nas/">About</a><a href="/slotoro-site/gajdy/">Guides</a><a href="/slotoro-site/platezhi/">Payments</a></div>
      </div>
    </div>
    <div class="footer-18">18+ | Gambling can be addictive. Play responsibly. <a href="https://www.begambleaware.org" target="_blank" rel="noopener">BeGambleAware.org</a></div>
    <div class="footer-bottom"><span>© 2026 bestiflokkurinn.is</span><span>BF Casino — independent review site</span></div>
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
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@500;600;700&display=swap" rel="stylesheet">
<style>
:root{{--bg:#060a1e;--bg2:#0a1030;--bg3:#0e1540;--card:#0b1235;--border:rgba(70,100,180,.15);--border2:rgba(70,100,180,.25);--blue:#4da8ff;--ice:#4dd9ff;--red:#e84050;--red2:#ff5060;--accent:#4dd9ff;--accent-bg:rgba(77,217,255,.06);--gold:#f0c050;--text:#c8d8f0;--text2:#9ab0d0;--muted:#5570a0;--muted2:#354070;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
html{{scroll-behavior:smooth;}}
body{{background:var(--bg);color:var(--text);font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}}
a{{text-decoration:none;color:inherit;}}
body::before{{content:'';position:fixed;top:-200px;right:-100px;width:600px;height:600px;background:radial-gradient(circle,rgba(232,64,80,.05) 0%,transparent 70%);pointer-events:none;z-index:0;animation:ambientRed 8s ease-in-out infinite;}}
body::after{{content:'';position:fixed;bottom:-200px;left:-100px;width:700px;height:700px;background:radial-gradient(circle,rgba(77,168,255,.04) 0%,transparent 70%);pointer-events:none;z-index:0;animation:ambientBlue 10s ease-in-out infinite;}}
@keyframes ambientRed{{0%{{transform:translate(0,0);opacity:.05;}}50%{{transform:translate(-30px,20px);opacity:.08;}}100%{{transform:translate(0,0);opacity:.05;}}}}
@keyframes ambientBlue{{0%{{transform:translate(0,0);opacity:.04;}}50%{{transform:translate(20px,-30px);opacity:.07;}}100%{{transform:translate(0,0);opacity:.04;}}}}
@keyframes shimmerLine{{0%{{background-position:200% 0;}}100%{{background-position:-200% 0;}}}}
.nav{{background:rgba(6,10,30,.9);padding:12px 30px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border);position:sticky;top:0;z-index:100;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);}}
.nav-logo{{display:flex;align-items:center;gap:10px;}}
.logo-text{{font-family:'Space Grotesk',sans-serif;font-size:18px;font-weight:700;color:#fff;}}
.nav-links{{display:flex;gap:20px;font-size:13px;font-weight:500;}}
.nav-links a{{color:var(--muted);transition:color .15s;}}
.nav-links a:hover{{color:var(--ice);}}
.nav-actions{{display:flex;gap:8px;}}
.btn-signup{{display:inline-flex;align-items:center;background:linear-gradient(135deg,var(--red),var(--red2));color:#fff;padding:8px 22px;border-radius:8px;font-size:13px;font-weight:700;transition:all .15s;box-shadow:0 2px 12px rgba(232,64,80,.25);position:relative;overflow:hidden;}}
.btn-signup:hover{{transform:translateY(-1px);box-shadow:0 4px 20px rgba(232,64,80,.35);}}
.breadcrumbs{{padding:14px 30px;font-size:11px;color:var(--muted2);border-bottom:1px solid var(--border);}}
.breadcrumbs a{{color:var(--muted);transition:color .15s;}}
.breadcrumbs a:hover{{color:var(--ice);}}
.content{{max-width:820px;margin:0 auto;padding:40px 30px 60px;position:relative;z-index:1;}}
.content h1{{font-family:'Space Grotesk',sans-serif;font-size:30px;font-weight:700;margin-bottom:18px;line-height:1.2;color:#fff;}}
.content h2{{font-family:'Space Grotesk',sans-serif;font-size:21px;font-weight:700;margin:30px 0 12px;color:var(--text);}}
.content h3{{font-size:16px;font-weight:600;margin:22px 0 8px;color:var(--text);}}
.content p{{color:var(--muted);font-size:14px;line-height:1.7;margin-bottom:14px;}}
.content ul,.content ol{{color:var(--muted);font-size:14px;line-height:1.7;margin:0 0 14px 20px;}}
.content li{{margin-bottom:6px;}}
.content a{{color:var(--ice);font-weight:500;}}
.content a:hover{{text-decoration:underline;}}
.slot-hero{{width:100%;max-width:400px;aspect-ratio:4/3;border-radius:12px;overflow:hidden;margin:0 0 20px;border:1px solid var(--border2);transition:border-color .3s;}}
.slot-hero:hover{{border-color:rgba(77,217,255,.2);}}
.slot-hero-bg{{width:100%;height:100%;background-size:cover;background-position:center;}}
.info-box{{background:var(--card);border:1px solid var(--border);border-radius:12px;padding:18px 22px;margin:16px 0;transition:border-color .2s;}}
.info-box:hover{{border-color:var(--border2);}}
.info-box p{{margin-bottom:6px;}}
.info-box p:last-child{{margin-bottom:0;}}
.info-box strong{{color:#fff;}}
.info-box a{{color:var(--ice);}}
.rating-box{{display:inline-flex;align-items:center;gap:8px;background:rgba(77,217,255,.06);border:1px solid rgba(77,217,255,.12);border-radius:10px;padding:8px 18px;margin:10px 0;}}
.rating-box .score{{font-family:'Space Grotesk',sans-serif;font-size:26px;font-weight:700;color:var(--ice);}}
.rating-box .label{{font-size:12px;color:var(--muted);}}
.cta-box{{text-align:center;margin:32px 0;}}
.cta-btn{{display:inline-block;background:linear-gradient(135deg,var(--red),var(--red2));color:#fff;padding:14px 40px;border-radius:12px;font-size:15px;font-weight:700;box-shadow:0 4px 20px rgba(232,64,80,.25);transition:all .2s;position:relative;overflow:hidden;}}
.cta-btn::before{{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--blue),var(--red),var(--gold),var(--blue));background-size:300% 100%;animation:shimmerLine 3s linear infinite;}}
.cta-btn:hover{{text-decoration:none;transform:translateY(-2px);box-shadow:0 8px 28px rgba(232,64,80,.4);}}
.game-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:14px;margin:20px 0;}}
.game-card{{background:var(--card);border:1px solid var(--border);border-radius:12px;overflow:hidden;transition:all .25s;}}
.game-card:hover{{transform:translateY(-5px);border-color:rgba(77,217,255,.15);box-shadow:0 8px 24px rgba(0,0,0,.3);}}
.game-card-thumb{{width:100%;aspect-ratio:4/3;background-size:cover;background-position:center;}}
.game-card-info{{padding:10px 12px;}}
.game-card-name{{font-size:13px;font-weight:600;color:#fff;}}
.game-card-prov{{font-size:11px;color:var(--muted);}}
.footer{{background:#040818;padding:28px 30px 14px;border-top:1px solid var(--border);position:relative;z-index:1;}}
.footer-inner{{max-width:820px;margin:0 auto;}}
.footer-top{{display:flex;justify-content:space-between;margin-bottom:18px;gap:30px;}}
.footer-brand{{max-width:280px;}}
.footer-desc{{color:var(--muted2);font-size:10px;line-height:1.6;margin-top:6px;}}
.footer-cols{{display:flex;gap:30px;}}
.footer-col-title{{color:var(--muted2);font-size:9px;letter-spacing:1.5px;font-weight:600;margin-bottom:6px;}}
.footer-cols a{{display:block;color:var(--muted);font-size:11px;line-height:2.2;transition:color .15s;}}
.footer-cols a:hover{{color:var(--ice);}}
.footer-18{{text-align:center;padding:14px;border:1px solid var(--border);border-radius:12px;background:var(--bg2);margin-bottom:12px;font-size:10px;color:var(--muted2);}}
.footer-18 a{{color:var(--ice);}}
.footer-bottom{{border-top:1px solid var(--border);padding-top:10px;display:flex;justify-content:space-between;color:var(--muted2);font-size:9px;}}
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
# ГЕНЕРАЦИЯ СТРАНИЦ
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
print("Генерирую обзоры казино...")
for c in casinos:
    content = f'''<h1>{c["name"]} — Review & Bonuses 2026</h1>
<div class="rating-box"><div class="score">{c["rating"]}</div><div class="label">/ 10</div></div>
<div class="info-box">
<p><strong>Bonus:</strong> {c["bonus"]}</p>
<p><strong>Type:</strong> {"Crypto Casino" if c["type"]=="crypto" else "Classic Casino"}</p>
</div>
<p>{c["desc"]}</p>
<h2>{c["name"]} Review</h2>
<p>{c["name"]} is a {"crypto casino" if c["type"]=="crypto" else "online casino"} available to players from Iceland. The casino offers a wide selection of slots, table games, and live casino with real dealers.</p>
<h3>Bonuses & Promotions</h3>
<p>New players receive a welcome bonus of {c["bonus"]}. To activate the bonus, register and make your first deposit.</p>
<h3>Payment Methods</h3>
<p>{"Accepts Bitcoin, Ethereum, USDT, Litecoin and other cryptocurrencies." if c["type"]=="crypto" else "Accepts Visa, Mastercard, cryptocurrencies and e-wallets."} This is especially important for Icelandic players as local banks often block casino transactions.</p>
<h3>Games</h3>
<p>{c["name"]} offers over 2000 games from top providers: Pragmatic Play, NetEnt, Play'n GO, Microgaming and more.</p>
<h2>Pros & Cons</h2>
<ul>
<li>✅ {c["bonus"]}</li>
<li>✅ Fast payouts</li>
<li>✅ {"Crypto payments without blocks" if c["type"]=="crypto" else "Wide range of payment methods"}</li>
<li>✅ Large game library</li>
<li>⚠️ Does not accept Icelandic króna directly</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Play at {c["name"]} →</a></div>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/casino/", "Casino"), ("", c["name"])]
    html = page_template(f'{c["name"]} Review', c["desc"], bc, content)
    write_page(f'casino/{c["slug"]}/index.html', html)

# 2. КАТЕГОРИИ КАЗИНО (50)
print("Генерирую категории казино...")
for cat in casino_categories:
    top_casinos = casinos[:10]
    cards = ""
    for c in top_casinos:
        cards += f'<div class="info-box"><p><strong>{c["name"]}</strong> — {c["bonus"]} (Рейтинг: {c["rating"]}/10) <a href="/slotoro-site/casino/{c["slug"]}/">Обзор →</a></p></div>\n'

    content = f'''<h1>{cat["title"]} in Iceland 2026</h1>
<p>{cat["desc"]}</p>
<h2>Top 10 Casinos in Category</h2>
{cards}
<h2>How We Choose the Best Casinos</h2>
<p>Our team evaluates each casino based on several criteria: licence reliability, payout speed, game quality, bonus offers and accessibility for players in Iceland.</p>
<p>We pay special attention to cryptocurrency support as Icelandic banks often block online casino transactions.</p>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/casino/", "Casino"), ("", cat["title"])]
    html = page_template(cat["title"], cat["desc"], bc, content)
    write_page(f'casino/{cat["slug"]}/index.html', html)

# 3. СЛОТЫ (250)
print("Генерирую обзоры слотов...")
for s in slots_data:
    cdn_img = ""
    if s.get("cdn"):
        cdn_img = f'<div class="slot-hero"><div class="slot-hero-bg" style="background:url(\'https://cdn.softswiss.net/i/s3/{s["cdn"]}\') center/cover,linear-gradient(135deg,#0a1040,#1a2070);"></div></div>'
    content = f'''<h1>{s["name"]} — Slot Review</h1>
{cdn_img}
<div class="info-box">
<p><strong>Provider:</strong> {s["provider"]}</p>
<p><strong>RTP:</strong> {s["rtp"]}%</p>
<p><strong>Volatility:</strong> {s["volatility"]}</p>
<p><strong>Max Win:</strong> {s["maxwin"]}</p>
<p><strong>Theme:</strong> {s["theme"]}</p>
</div>
<h2>About {s["name"]}</h2>
<p>{s["name"]} by {s["provider"]} is one of the most popular slots in the «{s["theme"]}» category. The slot features {s["volatility"].lower()} volatility and a maximum win of {s["maxwin"]}.</p>
<h3>RTP & Volatility</h3>
<p>The RTP (Return to Player) of {s["name"]} is {s["rtp"]}%. This means the slot theoretically returns {s["rtp"]}% of all wagers to players over the long term.</p>
<h3>Where to Play {s["name"]}</h3>
<p>This slot is available at the following casinos accepting players from Iceland:</p>
<ul>
<li><a href="/slotoro-site/casino/bitstarz/">BitStarz</a> — 5 BTC + 200 FS</li>
<li><a href="/slotoro-site/casino/stake/">Stake</a> — 200% bonus</li>
<li><a href="/slotoro-site/casino/bc-game/">BC.Game</a> — 300% up to 1 BTC</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Play {s["name"]} →</a></div>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/slots/", "Slots"), ("", s["name"])]
    html = page_template(f'{s["name"]} Slot', f'{s["name"]} by {s["provider"]} — RTP {s["rtp"]}%, volatility {s["volatility"]}, max {s["maxwin"]}', bc, content)
    write_page(f'slots/{s["slug"]}/index.html', html)

# 4. LIVE КАЗИНО (50)
print("Генерирую live казино страницы...")
for g in live_games:
    content = f'''<h1>{g["name"]} — Live Casino</h1>
<p>{g["desc"]}</p>
<h2>How to Play {g["name"]}</h2>
<p>{g["name"]} with a live dealer gives you the experience of a real casino from home. Professional dealers run the game in real time via HD video broadcast.</p>
<h3>Best Casinos for {g["name"]}</h3>
<ul>
<li><a href="/slotoro-site/casino/bitstarz/">BitStarz</a> — best live game selection</li>
<li><a href="/slotoro-site/casino/stake/">Stake</a> — exclusive tables</li>
<li><a href="/slotoro-site/casino/tonybet/">TonyBet</a> — wide range of limits</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Play {g["name"]} →</a></div>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/live/", "Live Casino"), ("", g["name"])]
    html = page_template(f'{g["name"]} Live', g["desc"], bc, content)
    write_page(f'live/{g["slug"]}/index.html', html)

# 5. БОНУСЫ (80)
print("Генерирую страницы бонусов...")
for b in bonus_pages:
    content = f'''<h1>{b["title"]}</h1>
<p>{b["desc"]}</p>
<h2>Best Offers 2026</h2>
<div class="info-box">
<p><strong>BitStarz:</strong> 5 BTC + 200 free spins — <a href="/slotoro-site/casino/bitstarz/">Details →</a></p>
</div>
<div class="info-box">
<p><strong>BC.Game:</strong> 300% crypto bonus — <a href="/slotoro-site/casino/bc-game/">Details →</a></p>
</div>
<h2>How to Get a Bonus</h2>
<p>To claim a bonus, register at the casino, make a deposit and the bonus will be credited automatically. Pay attention to wagering requirements.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Claim Bonus →</a></div>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/bonusy/", "Bonuses"), ("", b["title"])]
    html = page_template(b["title"], b["desc"], bc, content)
    write_page(f'bonusy/{b["slug"]}/index.html', html)

# 6. ПЛАТЕЖИ (50)
print("Генерирую страницы платежей...")
for p in payment_pages:
    content = f'''<h1>{p["title"]}</h1>
<p>{p["desc"]}</p>
<h2>How It Works</h2>
<p>Icelandic banks block payments to online casinos. Cryptocurrencies are the best way to bypass these restrictions. Transactions are fast, anonymous and fee-free.</p>
<h3>Step-by-Step Guide</h3>
<ol>
<li>Create a wallet (MetaMask, Trust Wallet or Binance)</li>
<li>Buy cryptocurrency on an exchange</li>
<li>Transfer funds to the casino</li>
<li>Play and withdraw winnings back to your wallet</li>
</ol>
<h3>Recommended Casinos</h3>
<ul>
<li><a href="/slotoro-site/casino/bitstarz/">BitStarz</a> — instant crypto payouts</li>
<li><a href="/slotoro-site/casino/stake/">Stake</a> — supports 20+ cryptocurrencies</li>
</ul>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Choose Casino →</a></div>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/platezhi/", "Payments"), ("", p["title"])]
    html = page_template(p["title"], p["desc"], bc, content)
    write_page(f'platezhi/{p["slug"]}/index.html', html)

# 7. ГАЙДЫ (60)
print("Генерирую гайды...")
for g in guide_pages:
    content = f'''<h1>{g["title"]}</h1>
<p>{g["desc"]}</p>
<h2>Detailed Guide</h2>
<p>In this guide we cover everything you need to know about «{g["title"]}». Information is up to date for players in Iceland in 2026.</p>
<h3>Key Points</h3>
<ul>
<li>What to know before you start</li>
<li>Step-by-step instructions</li>
<li>Common mistakes and how to avoid them</li>
<li>Recommendations from BF Casino experts</li>
</ul>
<h3>Useful Links</h3>
<ul>
<li><a href="/slotoro-site/casino/">Casino Reviews</a></li>
<li><a href="/slotoro-site/bonusy/">Bonuses</a></li>
<li><a href="/slotoro-site/platezhi/">Payment Methods</a></li>
</ul>'''

    bc = [("/slotoro-site/", "Home"), ("/slotoro-site/gajdy/", "Guides"), ("", g["title"])]
    html = page_template(g["title"], g["desc"], bc, content)
    write_page(f'gajdy/{g["slug"]}/index.html', html)

# 8. О НАС (10)
print("Генерирую страницы 'О нас'...")
for a in about_pages:
    content = f'''<h1>{a["title"]}</h1>
<p>{a["desc"]}</p>
<p>BF Casino (bestiflokkurinn.is) is an independent online casino portal for players in Iceland. We help you find reliable casinos with the best bonuses and cryptocurrency support.</p>'''

    bc = [("/slotoro-site/", "Home"), ("", a["title"])]
    html = page_template(a["title"], a["desc"], bc, content)
    write_page(f'{a["slug"]}/index.html', html)

# 9. ИНДЕКСНЫЕ СТРАНИЦЫ РАЗДЕЛОВ
print("Генерирую индексные страницы...")

# Casino index — FULL landing page (main casino hub)
casino_cards = ""
for c in casinos[:20]:
    ctype_label = "Crypto" if c["type"]=="crypto" else "Classic"
    casino_cards += f'''<a href="/slotoro-site/casino/{c["slug"]}/" class="game-card">
<div class="game-card-thumb" style="background:linear-gradient(135deg,{'#0a2060,#1a40a0' if c['type']=='crypto' else '#2a1040,#5020a0'});display:flex;align-items:center;justify-content:center;"><span style="font-size:28px;font-weight:800;color:rgba(255,255,255,.15);">{c["rating"]}</span></div>
<div class="game-card-info"><div class="game-card-name">{c["name"]}</div><div class="game-card-prov">{c["bonus"]} · {ctype_label}</div></div></a>\n'''

casino_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/casino/{c["slug"]}/">{c["name"]}</a></strong> — {c["bonus"]} (Rating: {c["rating"]}/10)</p></div>' for c in casinos[:50]])

casino_content = f'''<h1>Best Online Casinos Iceland 2026</h1>
<p>BF Casino reviews {len(casinos)} online casinos for Icelandic players. Compare bonuses, payment methods and game libraries. All casinos listed support cryptocurrency — the easiest way to play from Iceland.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Play at Top Casino →</a></div>
<h2>Top 20 Casinos</h2>
<div class="game-grid">{casino_cards}</div>
<h2>All {len(casinos)} Casino Reviews</h2>
{casino_list}'''

write_page("casino/index.html", page_template("Best Online Casinos Iceland 2026", f"Compare {len(casinos)} online casinos for Iceland. Crypto payments, fast withdrawals, welcome bonuses.",
    [("/slotoro-site/", "Home"), ("", "Casino")],
    casino_content))

# Slots index
slots_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/slots/{s["slug"]}/">{s["name"]}</a></strong> — {s["provider"]} | RTP {s["rtp"]}% | {s["maxwin"]}</p></div>' for s in slots_data[:30]])
write_page("slots/index.html", page_template("All Slots", "Reviews of popular slots",
    [("/slotoro-site/", "Home"), ("", "Slots")],
    f'<h1>Popular Slots 2026</h1><p>Reviews of {len(slots_data)} slots from top providers.</p>{slots_list}'))

# Live index
live_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/live/{g["slug"]}/">{g["name"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in live_games[:20]])
write_page("live/index.html", page_template("Live Casino", "Games with live dealers",
    [("/slotoro-site/", "Home"), ("", "Live Casino")],
    f'<h1>Live Casino — Games with Live Dealers</h1><p>{len(live_games)} games with professional dealers.</p>{live_list}'))

# Bonus index
bonus_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/bonusy/{b["slug"]}/">{b["title"]}</a></strong> — {b["desc"][:80]}</p></div>' for b in bonus_pages[:20]])
write_page("bonusy/index.html", page_template("Casino Bonuses", "All bonuses and promo codes",
    [("/slotoro-site/", "Home"), ("", "Bonuses")],
    f'<h1>Casino Bonuses 2026</h1><p>{len(bonus_pages)} active bonus offers.</p>{bonus_list}'))

# Payment index
pay_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/platezhi/{p["slug"]}/">{p["title"]}</a></strong></p></div>' for p in payment_pages[:20]])
write_page("platezhi/index.html", page_template("Payment Methods", "Crypto and other payments at casinos",
    [("/slotoro-site/", "Home"), ("", "Payments")],
    f'<h1>Casino Payment Methods</h1><p>How to bypass bank blocks and play from Iceland.</p>{pay_list}'))

# Guide index
guide_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/gajdy/{g["slug"]}/">{g["title"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in guide_pages[:20]])
write_page("gajdy/index.html", page_template("Guides", "Player guides and tutorials",
    [("/slotoro-site/", "Home"), ("", "Guides")],
    f'<h1>Player Guides</h1><p>{len(guide_pages)} guides for beginners and experienced players.</p>{guide_list}'))


# 10. SITEMAP
print("Генерирую sitemap.xml...")
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

print(f"\n✅ Сгенерировано {count} страниц + sitemap.xml + robots.txt")
print(f"URLs в sitemap: {len(sitemap_urls)}")
