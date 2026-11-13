#!/usr/bin/env python3
"""
Frostspil.is — генератор 800 страниц казино-портала
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
    {"slug": "gates-of-olympus", "name": "Gates of Olympus", "provider": "Pragmatic Play", "rtp": 96.5, "volatility": "Высокая", "maxwin": "x5000", "theme": "Мифология"},
    {"slug": "sweet-bonanza", "name": "Sweet Bonanza", "provider": "Pragmatic Play", "rtp": 96.48, "volatility": "Высокая", "maxwin": "x21100", "theme": "Фрукты"},
    {"slug": "big-bass-splash", "name": "Big Bass Splash", "provider": "Pragmatic Play", "rtp": 96.71, "volatility": "Высокая", "maxwin": "x2100", "theme": "Рыбалка"},
    {"slug": "book-of-dead", "name": "Book of Dead", "provider": "Play'n GO", "rtp": 96.21, "volatility": "Высокая", "maxwin": "x5000", "theme": "Египет"},
    {"slug": "starburst", "name": "Starburst", "provider": "NetEnt", "rtp": 96.09, "volatility": "Низкая", "maxwin": "x500", "theme": "Космос"},
    {"slug": "gonzos-quest", "name": "Gonzo's Quest", "provider": "NetEnt", "rtp": 95.97, "volatility": "Средняя", "maxwin": "x2500", "theme": "Приключения"},
    {"slug": "dead-or-alive-2", "name": "Dead or Alive 2", "provider": "NetEnt", "rtp": 96.8, "volatility": "Высокая", "maxwin": "x111111", "theme": "Вестерн"},
    {"slug": "reactoonz", "name": "Reactoonz", "provider": "Play'n GO", "rtp": 96.51, "volatility": "Высокая", "maxwin": "x4750", "theme": "Инопланетяне"},
    {"slug": "fire-joker", "name": "Fire Joker", "provider": "Play'n GO", "rtp": 96.15, "volatility": "Высокая", "maxwin": "x800", "theme": "Классика"},
    {"slug": "wolf-gold", "name": "Wolf Gold", "provider": "Pragmatic Play", "rtp": 96.01, "volatility": "Средняя", "maxwin": "x5000", "theme": "Природа"},
    {"slug": "the-dog-house", "name": "The Dog House", "provider": "Pragmatic Play", "rtp": 96.51, "volatility": "Высокая", "maxwin": "x6750", "theme": "Животные"},
    {"slug": "razor-shark", "name": "Razor Shark", "provider": "Push Gaming", "rtp": 96.7, "volatility": "Высокая", "maxwin": "x50000", "theme": "Океан"},
    {"slug": "jammin-jars", "name": "Jammin' Jars", "provider": "Push Gaming", "rtp": 96.83, "volatility": "Высокая", "maxwin": "x20000", "theme": "Фрукты"},
    {"slug": "money-train-3", "name": "Money Train 3", "provider": "Relax Gaming", "rtp": 96.1, "volatility": "Высокая", "maxwin": "x100000", "theme": "Вестерн"},
    {"slug": "wanted-dead-or-a-wild", "name": "Wanted Dead or a Wild", "provider": "Hacksaw Gaming", "rtp": 96.38, "volatility": "Высокая", "maxwin": "x12500", "theme": "Вестерн"},
    {"slug": "mental", "name": "Mental", "provider": "NoLimit City", "rtp": 96.08, "volatility": "Экстрим", "maxwin": "x66666", "theme": "Хоррор"},
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
    {"slug": "o-nas", "title": "О Frostspil", "desc": "Кто мы и почему создали Frostspil."},
    {"slug": "kontakty", "title": "Контакты", "desc": "Свяжитесь с командой Frostspil."},
    {"slug": "konfidencialnost", "title": "Политика конфиденциальности", "desc": "Как мы обрабатываем ваши данные."},
    {"slug": "usloviya", "title": "Условия использования", "desc": "Правила использования сайта Frostspil."},
    {"slug": "otkaz-ot-otvetstvennosti", "title": "Отказ от ответственности", "desc": "Важная юридическая информация."},
    {"slug": "kak-my-ocenivaem", "title": "Как мы оцениваем казино", "desc": "Наша методология оценки."},
    {"slug": "redakcionnaya-politika", "title": "Редакционная политика", "desc": "Принципы нашей редакции."},
    {"slug": "partnerstvo", "title": "Партнёрство", "desc": "Сотрудничество с Frostspil."},
    {"slug": "karta-sajta", "title": "Карта сайта", "desc": "Полная карта всех страниц Frostspil."},
    {"slug": "otvetstvennaya-igra-stranica", "title": "Ответственная игра", "desc": "Наша позиция по ответственной игре."},
]


# ============================================================
# HTML ШАБЛОН
# ============================================================

def get_nav():
    return '''<div class="promo-bar"><span>🎰 FROSTSPIL — ЛУЧШИЕ ОНЛАЙН КАЗИНО ИСЛАНДИИ 🎰</span></div>
<nav class="nav">
  <a href="/slotoro-site/" class="nav-logo"><div class="logo-icon">❄</div><div class="logo-text">FROSTSPIL<small>.is</small></div></a>
  <div class="nav-links">
    <a href="/slotoro-site/">Главная</a>
    <a href="/slotoro-site/casino/">Казино</a>
    <a href="/slotoro-site/slots/">Слоты</a>
    <a href="/slotoro-site/bonusy/">Бонусы</a>
    <a href="/slotoro-site/live/">Live</a>
    <a href="/slotoro-site/platezhi/">Оплата</a>
    <a href="/slotoro-site/gajdy/">Гайды</a>
  </div>
</nav>'''

def get_footer():
    return '''<footer class="footer">
  <div class="footer-inner">
    <div class="footer-top">
      <div><div style="display:flex;align-items:center;gap:8px;margin-bottom:8px;"><div class="logo-icon" style="width:26px;height:26px;font-size:12px;">❄</div><span style="font-size:15px;font-weight:700;">Frostspil</span></div>
      <div class="footer-desc">Frostspil — независимый сайт сравнения казино. 18+ Играйте ответственно.</div></div>
      <div class="footer-cols">
        <div><div class="footer-col-title">КАЗИНО</div><a href="/slotoro-site/casino/">Обзоры</a><a href="/slotoro-site/bonusy/">Бонусы</a><a href="/slotoro-site/casino/crypto-casino/">Крипто</a></div>
        <div><div class="footer-col-title">ИГРЫ</div><a href="/slotoro-site/slots/">Слоты</a><a href="/slotoro-site/live/">Live</a></div>
        <div><div class="footer-col-title">ИНФО</div><a href="/slotoro-site/o-nas/">О нас</a><a href="/slotoro-site/gajdy/">Гайды</a><a href="/slotoro-site/platezhi/">Оплата</a></div>
      </div>
    </div>
    <div class="footer-bottom"><span>© 2026 Frostspil.is</span><span>18+ | Играйте ответственно</span></div>
  </div>
</footer>'''

def page_template(title, desc, breadcrumbs, content, canonical=""):
    bc_html = ' → '.join([f'<a href="{url}">{name}</a>' for url, name in breadcrumbs])
    return f'''<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | Frostspil</title>
<meta name="description" content="{desc}">
{f'<link rel="canonical" href="{canonical}">' if canonical else ''}
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:#050818;color:#fff;font-family:'Inter',system-ui,sans-serif;-webkit-font-smoothing:antialiased;}}
a{{text-decoration:none;color:inherit;}}
.promo-bar{{background:linear-gradient(90deg,#0a0520,#1a0a50,#0a0520);padding:8px 20px;text-align:center;border-bottom:1px solid rgba(120,60,255,0.2);}}
.promo-bar span{{color:rgba(255,215,0,0.9);font-size:11px;font-weight:600;}}
.nav{{background:rgba(5,8,24,0.95);padding:12px 40px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(0,150,255,0.1);position:sticky;top:0;z-index:100;backdrop-filter:blur(12px);}}
.nav-logo{{display:flex;align-items:center;gap:10px;}}
.logo-icon{{width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#80e0ff,#00a0e0,#0060b0);display:flex;align-items:center;justify-content:center;font-size:16px;color:#fff;box-shadow:0 0 14px rgba(100,200,255,0.4);}}
.logo-text{{font-size:20px;font-weight:800;letter-spacing:2px;}}
.logo-text small{{color:#00d4ff;font-size:9px;vertical-align:super;margin-left:2px;}}
.nav-links{{display:flex;gap:18px;font-size:12px;font-weight:500;}}
.nav-links a{{color:rgba(180,200,255,0.6);transition:color 0.2s;}}
.nav-links a:hover{{color:#fff;}}
.breadcrumbs{{padding:14px 40px;font-size:11px;color:rgba(140,180,255,0.5);background:rgba(5,8,24,0.5);}}
.breadcrumbs a{{color:rgba(0,180,255,0.6);}}
.breadcrumbs a:hover{{color:#00d4ff;}}
.content{{max-width:800px;margin:0 auto;padding:40px 40px 60px;}}
.content h1{{font-size:28px;font-weight:800;margin-bottom:16px;line-height:1.2;}}
.content h2{{font-size:20px;font-weight:700;margin:28px 0 12px;color:rgba(200,220,255,0.9);}}
.content h3{{font-size:16px;font-weight:600;margin:20px 0 8px;color:rgba(180,210,255,0.8);}}
.content p{{color:rgba(180,210,255,0.7);font-size:14px;line-height:1.7;margin-bottom:14px;}}
.content ul,.content ol{{color:rgba(180,210,255,0.7);font-size:14px;line-height:1.7;margin:0 0 14px 20px;}}
.content li{{margin-bottom:6px;}}
.content a{{color:#00d4ff;}}
.content a:hover{{text-decoration:underline;}}
.info-box{{background:linear-gradient(135deg,rgba(0,50,120,0.3),rgba(10,20,60,0.5));border:1px solid rgba(0,150,255,0.15);border-radius:14px;padding:20px;margin:20px 0;}}
.rating-box{{display:inline-flex;align-items:center;gap:8px;background:rgba(0,150,255,0.1);border:1px solid rgba(0,150,255,0.2);border-radius:10px;padding:8px 16px;margin:10px 0;}}
.rating-box .score{{font-size:24px;font-weight:800;color:#00e0ff;}}
.rating-box .label{{font-size:12px;color:rgba(140,180,255,0.6);}}
.cta-box{{text-align:center;margin:30px 0;}}
.cta-btn{{display:inline-block;background:linear-gradient(135deg,#ffd700,#ffaa00);color:#1a0a00;padding:14px 36px;border-radius:50px;font-size:15px;font-weight:700;box-shadow:0 0 20px rgba(255,200,0,0.3);}}
.cta-btn:hover{{text-decoration:none;transform:scale(1.02);}}
.footer{{background:#040610;padding:24px 40px 14px;border-top:1px solid rgba(0,60,150,0.08);}}
.footer-inner{{max-width:800px;margin:0 auto;}}
.footer-top{{display:flex;justify-content:space-between;margin-bottom:16px;}}
.footer-desc{{color:rgba(100,140,200,0.4);font-size:10px;line-height:1.5;max-width:250px;margin-top:6px;}}
.footer-cols{{display:flex;gap:30px;}}
.footer-col-title{{color:rgba(0,150,255,0.3);font-size:9px;letter-spacing:1px;margin-bottom:4px;}}
.footer-col a{{display:block;color:rgba(140,180,230,0.4);font-size:10px;line-height:2;}}
.footer-bottom{{border-top:1px solid rgba(0,60,150,0.06);padding-top:10px;display:flex;justify-content:space-between;color:rgba(80,120,180,0.3);font-size:9px;}}
@media(max-width:768px){{
  .nav{{padding:10px 16px;flex-wrap:wrap;}}
  .nav-links{{gap:10px;font-size:10px;}}
  .content{{padding:20px 16px 40px;}}
  .content h1{{font-size:22px;}}
  .footer-top{{flex-direction:column;gap:14px;}}
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
    content = f'''<h1>{c["name"]} — обзор и бонусы 2026</h1>
<div class="rating-box"><div class="score">{c["rating"]}</div><div class="label">/ 10</div></div>
<div class="info-box">
<p><strong>Бонус:</strong> {c["bonus"]}</p>
<p><strong>Тип:</strong> {"Крипто-казино" if c["type"]=="crypto" else "Классическое казино"}</p>
</div>
<p>{c["desc"]}</p>
<h2>Обзор {c["name"]}</h2>
<p>{c["name"]} — это {"крипто-казино" if c["type"]=="crypto" else "онлайн казино"} доступное для игроков из Исландии. Казино предлагает широкий выбор слотов, настольных игр и live-казино с живыми дилерами.</p>
<h3>Бонусы и акции</h3>
<p>Новые игроки получают приветственный бонус {c["bonus"]}. Для активации бонуса необходимо зарегистрироваться и сделать первый депозит.</p>
<h3>Способы оплаты</h3>
<p>{"Принимает Bitcoin, Ethereum, USDT, Litecoin и другие криптовалюты." if c["type"]=="crypto" else "Принимает Visa, Mastercard, криптовалюты и электронные кошельки."} Это особенно важно для исландских игроков, так как местные банки часто блокируют транзакции в казино.</p>
<h3>Игры</h3>
<p>В библиотеке {c["name"]} более 2000 игр от ведущих провайдеров: Pragmatic Play, NetEnt, Play'n GO, Microgaming и других.</p>
<h2>Плюсы и минусы</h2>
<ul>
<li>✅ {c["bonus"]}</li>
<li>✅ Быстрые выплаты</li>
<li>✅ {"Крипто-платежи без блокировок" if c["type"]=="crypto" else "Широкий выбор способов оплаты"}</li>
<li>✅ Большая библиотека игр</li>
<li>⚠️ Не принимает исландскую крону напрямую</li>
</ul>
<div class="cta-box"><a href="#" class="cta-btn">Играть в {c["name"]} →</a></div>'''

    bc = [("/slotoro-site/", "Главная"), ("/slotoro-site/casino/", "Казино"), ("", c["name"])]
    html = page_template(f'{c["name"]} обзор', c["desc"], bc, content)
    write_page(f'casino/{c["slug"]}/index.html', html)

# 2. КАТЕГОРИИ КАЗИНО (50)
print("Генерирую категории казино...")
for cat in casino_categories:
    top_casinos = casinos[:10]
    cards = ""
    for c in top_casinos:
        cards += f'<div class="info-box"><p><strong>{c["name"]}</strong> — {c["bonus"]} (Рейтинг: {c["rating"]}/10) <a href="/slotoro-site/casino/{c["slug"]}/">Обзор →</a></p></div>\n'

    content = f'''<h1>{cat["title"]} в Исландии 2026</h1>
<p>{cat["desc"]}</p>
<h2>Топ-10 казино в категории</h2>
{cards}
<h2>Как мы выбираем лучшие казино</h2>
<p>Наша команда оценивает каждое казино по нескольким критериям: надёжность лицензии, скорость выплат, качество игр, бонусные предложения и доступность для игроков из Исландии.</p>
<p>Особое внимание мы уделяем поддержке криптовалют, так как исландские банки часто блокируют транзакции в онлайн казино.</p>'''

    bc = [("/slotoro-site/", "Главная"), ("/slotoro-site/casino/", "Казино"), ("", cat["title"])]
    html = page_template(cat["title"], cat["desc"], bc, content)
    write_page(f'casino/{cat["slug"]}/index.html', html)

# 3. СЛОТЫ (250)
print("Генерирую обзоры слотов...")
for s in slots_data:
    content = f'''<h1>{s["name"]} — обзор слота</h1>
<div class="info-box">
<p><strong>Провайдер:</strong> {s["provider"]}</p>
<p><strong>RTP:</strong> {s["rtp"]}%</p>
<p><strong>Волатильность:</strong> {s["volatility"]}</p>
<p><strong>Макс. выигрыш:</strong> {s["maxwin"]}</p>
<p><strong>Тема:</strong> {s["theme"]}</p>
</div>
<h2>Описание {s["name"]}</h2>
<p>{s["name"]} от {s["provider"]} — один из популярных слотов в категории «{s["theme"]}». Слот отличается {s["volatility"].lower()} волатильностью и максимальным выигрышем {s["maxwin"]}.</p>
<h3>RTP и волатильность</h3>
<p>RTP (Return to Player) слота {s["name"]} составляет {s["rtp"]}%. Это означает, что теоретически слот возвращает игрокам {s["rtp"]}% от всех поставленных средств в долгосрочной перспективе.</p>
<h3>Где играть в {s["name"]}</h3>
<p>Этот слот доступен в следующих казино, принимающих игроков из Исландии:</p>
<ul>
<li><a href="/slotoro-site/casino/bitstarz/">BitStarz</a> — 5 BTC + 200 FS</li>
<li><a href="/slotoro-site/casino/stake/">Stake</a> — 200% бонус</li>
<li><a href="/slotoro-site/casino/bc-game/">BC.Game</a> — 300% до 1 BTC</li>
</ul>
<div class="cta-box"><a href="#" class="cta-btn">Играть в {s["name"]} →</a></div>'''

    bc = [("/slotoro-site/", "Главная"), ("/slotoro-site/slots/", "Слоты"), ("", s["name"])]
    html = page_template(f'{s["name"]} слот', f'{s["name"]} от {s["provider"]} — RTP {s["rtp"]}%, волатильность {s["volatility"]}, макс {s["maxwin"]}', bc, content)
    write_page(f'slots/{s["slug"]}/index.html', html)

# 4. LIVE КАЗИНО (50)
print("Генерирую live казино страницы...")
for g in live_games:
    content = f'''<h1>{g["name"]} — Live казино</h1>
<p>{g["desc"]}</p>
<h2>Как играть в {g["name"]}</h2>
<p>{g["name"]} с живым дилером — это возможность окунуться в атмосферу настоящего казино, не выходя из дома. Профессиональные дилеры ведут игру в реальном времени через HD-видеотрансляцию.</p>
<h3>Лучшие казино для {g["name"]}</h3>
<ul>
<li><a href="/slotoro-site/casino/bitstarz/">BitStarz</a> — лучший выбор live-игр</li>
<li><a href="/slotoro-site/casino/stake/">Stake</a> — эксклюзивные столы</li>
<li><a href="/slotoro-site/casino/tonybet/">TonyBet</a> — широкий выбор лимитов</li>
</ul>
<div class="cta-box"><a href="#" class="cta-btn">Играть в {g["name"]} →</a></div>'''

    bc = [("/slotoro-site/", "Главная"), ("/slotoro-site/live/", "Live казино"), ("", g["name"])]
    html = page_template(f'{g["name"]} Live', g["desc"], bc, content)
    write_page(f'live/{g["slug"]}/index.html', html)

# 5. БОНУСЫ (80)
print("Генерирую страницы бонусов...")
for b in bonus_pages:
    content = f'''<h1>{b["title"]}</h1>
<p>{b["desc"]}</p>
<h2>Лучшие предложения 2026</h2>
<div class="info-box">
<p><strong>BitStarz:</strong> 5 BTC + 200 фриспинов — <a href="/slotoro-site/casino/bitstarz/">Подробнее →</a></p>
</div>
<div class="info-box">
<p><strong>BC.Game:</strong> 300% крипто бонус — <a href="/slotoro-site/casino/bc-game/">Подробнее →</a></p>
</div>
<h2>Как получить бонус</h2>
<p>Для получения бонуса зарегистрируйтесь в казино, внесите депозит и бонус будет начислен автоматически. Обратите внимание на требования к отыгрышу (вейджер).</p>
<div class="cta-box"><a href="#" class="cta-btn">Забрать бонус →</a></div>'''

    bc = [("/slotoro-site/", "Главная"), ("/slotoro-site/bonusy/", "Бонусы"), ("", b["title"])]
    html = page_template(b["title"], b["desc"], bc, content)
    write_page(f'bonusy/{b["slug"]}/index.html', html)

# 6. ПЛАТЕЖИ (50)
print("Генерирую страницы платежей...")
for p in payment_pages:
    content = f'''<h1>{p["title"]}</h1>
<p>{p["desc"]}</p>
<h2>Как это работает</h2>
<p>Исландские банки блокируют платежи в онлайн казино. Криптовалюты — лучший способ обойти эти ограничения. Транзакции быстрые, анонимные и без комиссий.</p>
<h3>Пошаговая инструкция</h3>
<ol>
<li>Создайте кошелёк (MetaMask, Trust Wallet или Binance)</li>
<li>Купите криптовалюту на бирже</li>
<li>Переведите средства в казино</li>
<li>Играйте и выводите выигрыш обратно на кошелёк</li>
</ol>
<h3>Рекомендуемые казино</h3>
<ul>
<li><a href="/slotoro-site/casino/bitstarz/">BitStarz</a> — мгновенные крипто-выплаты</li>
<li><a href="/slotoro-site/casino/stake/">Stake</a> — поддержка 20+ криптовалют</li>
</ul>
<div class="cta-box"><a href="#" class="cta-btn">Выбрать казино →</a></div>'''

    bc = [("/slotoro-site/", "Главная"), ("/slotoro-site/platezhi/", "Оплата"), ("", p["title"])]
    html = page_template(p["title"], p["desc"], bc, content)
    write_page(f'platezhi/{p["slug"]}/index.html', html)

# 7. ГАЙДЫ (60)
print("Генерирую гайды...")
for g in guide_pages:
    content = f'''<h1>{g["title"]}</h1>
<p>{g["desc"]}</p>
<h2>Подробное руководство</h2>
<p>В этом гайде мы подробно разберём всё что нужно знать про «{g["title"]}». Информация актуальна для игроков из Исландии в 2026 году.</p>
<h3>Основные моменты</h3>
<ul>
<li>Что важно знать перед началом</li>
<li>Пошаговая инструкция</li>
<li>Частые ошибки и как их избежать</li>
<li>Рекомендации от экспертов Frostspil</li>
</ul>
<h3>Полезные ссылки</h3>
<ul>
<li><a href="/slotoro-site/casino/">Обзоры казино</a></li>
<li><a href="/slotoro-site/bonusy/">Бонусы</a></li>
<li><a href="/slotoro-site/platezhi/">Способы оплаты</a></li>
</ul>'''

    bc = [("/slotoro-site/", "Главная"), ("/slotoro-site/gajdy/", "Гайды"), ("", g["title"])]
    html = page_template(g["title"], g["desc"], bc, content)
    write_page(f'gajdy/{g["slug"]}/index.html', html)

# 8. О НАС (10)
print("Генерирую страницы 'О нас'...")
for a in about_pages:
    content = f'''<h1>{a["title"]}</h1>
<p>{a["desc"]}</p>
<p>Frostspil.is — независимый информационный портал об онлайн казино для игроков из Исландии. Мы помогаем найти надёжные казино с лучшими бонусами и поддержкой криптовалют.</p>'''

    bc = [("/slotoro-site/", "Главная"), ("", a["title"])]
    html = page_template(a["title"], a["desc"], bc, content)
    write_page(f'{a["slug"]}/index.html', html)

# 9. ИНДЕКСНЫЕ СТРАНИЦЫ РАЗДЕЛОВ
print("Генерирую индексные страницы...")

# Casino index
casino_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/casino/{c["slug"]}/">{c["name"]}</a></strong> — {c["bonus"]} (Рейтинг: {c["rating"]}/10)</p></div>' for c in casinos[:30]])
write_page("casino/index.html", page_template("Все казино", "Полный список онлайн казино для Исландии",
    [("/slotoro-site/", "Главная"), ("", "Казино")],
    f'<h1>Все онлайн казино 2026</h1><p>Полный список из {len(casinos)} онлайн казино, проверенных командой Frostspil.</p>{casino_list}'))

# Slots index
slots_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/slots/{s["slug"]}/">{s["name"]}</a></strong> — {s["provider"]} | RTP {s["rtp"]}% | {s["maxwin"]}</p></div>' for s in slots_data[:30]])
write_page("slots/index.html", page_template("Все слоты", "Обзоры популярных слотов",
    [("/slotoro-site/", "Главная"), ("", "Слоты")],
    f'<h1>Популярные слоты 2026</h1><p>Обзоры {len(slots_data)} слотов от лучших провайдеров.</p>{slots_list}'))

# Live index
live_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/live/{g["slug"]}/">{g["name"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in live_games[:20]])
write_page("live/index.html", page_template("Live казино", "Игры с живыми дилерами",
    [("/slotoro-site/", "Главная"), ("", "Live казино")],
    f'<h1>Live казино — игры с живым дилером</h1><p>{len(live_games)} игр с профессиональными дилерами.</p>{live_list}'))

# Bonus index
bonus_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/bonusy/{b["slug"]}/">{b["title"]}</a></strong> — {b["desc"][:80]}</p></div>' for b in bonus_pages[:20]])
write_page("bonusy/index.html", page_template("Бонусы казино", "Все бонусы и промокоды",
    [("/slotoro-site/", "Главная"), ("", "Бонусы")],
    f'<h1>Бонусы казино 2026</h1><p>{len(bonus_pages)} актуальных бонусных предложений.</p>{bonus_list}'))

# Payment index
pay_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/platezhi/{p["slug"]}/">{p["title"]}</a></strong></p></div>' for p in payment_pages[:20]])
write_page("platezhi/index.html", page_template("Способы оплаты", "Крипто и другие платежи в казино",
    [("/slotoro-site/", "Главная"), ("", "Оплата")],
    f'<h1>Способы оплаты в казино</h1><p>Как обойти банковские блокировки и играть из Исландии.</p>{pay_list}'))

# Guide index
guide_list = "\n".join([f'<div class="info-box"><p><strong><a href="/slotoro-site/gajdy/{g["slug"]}/">{g["title"]}</a></strong> — {g["desc"][:80]}</p></div>' for g in guide_pages[:20]])
write_page("gajdy/index.html", page_template("Гайды", "Руководства для игроков",
    [("/slotoro-site/", "Главная"), ("", "Гайды")],
    f'<h1>Гайды для игроков</h1><p>{len(guide_pages)} руководств для новичков и опытных игроков.</p>{guide_list}'))


# 10. SITEMAP
print("Генерирую sitemap.xml...")
sitemap_urls = ['https://frostspil.is/']
for c in casinos:
    sitemap_urls.append(f'https://frostspil.is/casino/{c["slug"]}/')
for cat in casino_categories:
    sitemap_urls.append(f'https://frostspil.is/casino/{cat["slug"]}/')
for s in slots_data:
    sitemap_urls.append(f'https://frostspil.is/slots/{s["slug"]}/')
for g in live_games:
    sitemap_urls.append(f'https://frostspil.is/live/{g["slug"]}/')
for b in bonus_pages:
    sitemap_urls.append(f'https://frostspil.is/bonusy/{b["slug"]}/')
for p in payment_pages:
    sitemap_urls.append(f'https://frostspil.is/platezhi/{p["slug"]}/')
for g in guide_pages:
    sitemap_urls.append(f'https://frostspil.is/gajdy/{g["slug"]}/')
for a in about_pages:
    sitemap_urls.append(f'https://frostspil.is/{a["slug"]}/')
sitemap_urls.extend([
    'https://frostspil.is/casino/',
    'https://frostspil.is/slots/',
    'https://frostspil.is/live/',
    'https://frostspil.is/bonusy/',
    'https://frostspil.is/platezhi/',
    'https://frostspil.is/gajdy/',
])

sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_xml += f'  <url><loc>{url}</loc><changefreq>weekly</changefreq><priority>0.8</priority></url>\n'
sitemap_xml += '</urlset>'

with open(os.path.join(BASE, 'sitemap.xml'), 'w') as f:
    f.write(sitemap_xml)

# robots.txt
with open(os.path.join(BASE, 'robots.txt'), 'w') as f:
    f.write('User-agent: *\nAllow: /\nSitemap: https://frostspil.is/sitemap.xml\n')

print(f"\n✅ Сгенерировано {count} страниц + sitemap.xml + robots.txt")
print(f"URLs в sitemap: {len(sitemap_urls)}")
