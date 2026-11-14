#!/usr/bin/env python3
"""Batch 3: payments, licences, providers, game rules, strategies."""

AFF = "https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/"
U = "{URL_BASE}"


def page(slug, title, desc, emoji, colors, body, cta="Byrja að spila →"):
    return f'''    {{
        "slug": "{slug}",
        "title": "{title}",
        "desc": "{desc}",
        "emoji": "{emoji}",
        "colors": {colors},
        "content": f\'\'\'<h1>{title.split(" — ")[0]}</h1>
{{hero}}
{body}
<div class="cta-box"><a href="{AFF}" target="_blank" rel="noopener" class="cta-btn">{cta}</a></div>\'\'\'
    }},'''


P = []

# ---------- PAYMENTS ----------
P.append(page(
    "hvernig-a-ad-kaupa-usdt-island",
    "Hvernig á að kaupa USDT á Íslandi — skref fyrir skref 2026",
    "Leiðbeiningar um kaup á USDT (Tether) frá Íslandi fyrir spilavítainnlagnir. Kauphallir, net, gjöld og hvernig á að senda.",
    "💵", ("#0a1f14", "#143a26", "#1e5538"),
    f'''<p>USDT (Tether) er <strong>besti dulritunargjaldmiðillinn fyrir spilavítainnlagnir</strong> frá Íslandi: verðið er stöðugt (1 USDT ≈ 1 USD), færslugjöldin eru undir dollar og millifærslan tekur mínútur.</p>

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
<p>Bankinn þinn breytir ISK í EUR með 1–2% álagi. Til að spara getur þú notað <a href="{U}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut</a> fyrir gjaldmiðlaskiptin.</p>

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
<div class="info-box"><p><strong><a href="{U}spilaviti/slotoro/">Slotoro</a></strong> — USDT, BTC, ETH og fleira. €10 lágmark.</p></div>
<div class="info-box"><p><strong><a href="{U}spilaviti/stake/">Stake</a></strong> — Styður USDT á mörgum netum.</p></div>
<div class="info-box"><p><strong><a href="{U}spilaviti/bc-game/">BC.Game</a></strong> — 100+ dulritunargjaldmiðlar.</p></div>
<p>Sjá <a href="{U}leidbeiningar/bestu-crypto-spilavitin-island/">topp 10 dulritunarspilavítin á Íslandi →</a></p>

<h2>Algengar spurningar</h2>
<h3>Er löglegt að kaupa USDT á Íslandi?</h3>
<p>Já — kaup og eign dulritunargjaldmiðla er fullkomlega löglegt á Íslandi. Sjá <a href="{U}leidbeiningar/er-ologligt-ad-spila-a-spilaviti-island/">lagalega stöðu →</a></p>
<h3>Hvað kostar að kaupa USDT fyrir €100?</h3>
<p>Á Coinbase með korti: um €2–4 í gjöld. Á Binance með SEPA: undir €0,50. Síðan $0,5–1 í færslugjald þegar þú sendir á spilavítið.</p>
<h3>Get ég tekið út vinninga í USDT?</h3>
<p>Já — og það er hraðasta leiðin. Spilavítið sendir USDT á veskið þitt, þú selur fyrir EUR á kauphöllinni og millifærir á bankann.</p>
<h3>Hvað ef ég sendi á rangt net?</h3>
<p>Fjármunirnir tapast yfirleitt varanlega. Sum spilavíti geta endurheimt þá gegn gjaldi en það er ekki tryggt. Athugaðu alltaf netið áður en þú staðfestir.</p>''',
    "Spila með USDT →"))

P.append(page(
    "bitcoin-vs-usdt-spilaviti",
    "Bitcoin vs USDT á spilavíti — hvort er betra? 2026",
    "Samanburður á Bitcoin og USDT fyrir spilavítainnlagnir: gjöld, hraði, verðsveiflur og hvað hentar íslenskum spilurum.",
    "⚖️", ("#1a1200", "#332400", "#4d3600"),
    f'''<p>Þegar þú spilar á dulritunarspilavíti þarftu að velja gjaldmiðil. <strong>Bitcoin og USDT eru langalgengastir — en þeir henta í gjörólíkum aðstæðum.</strong></p>

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
<p><a href="{U}leidbeiningar/hvernig-a-ad-kaupa-usdt-island/">Hvernig á að kaupa USDT á Íslandi →</a></p>

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
<p>Flest en ekki öll. Bitcoin er studd alls staðar. Athugaðu greiðslusíðu spilavítisins áður en þú kaupir.</p>''',
    "Finna crypto-spilavíti →"))

P.append(page(
    "hvada-leyfi-er-best-spilaviti",
    "MGA, Curaçao eða UKGC — hvaða spilavítileyfi er best? 2026",
    "Samanburður á spilavítaleyfum: Malta (MGA), Curaçao, UKGC og fleiri. Hvað verndar þig best sem íslenskan spilara?",
    "📜", ("#1a1a0a", "#33331a", "#4d4d28"),
    f'''<p>Leyfið segir þér hvaða reglum spilavítið lýtur, hvað gerist ef deilur koma upp og hversu vel peningarnir þínir eru verndaðir. <strong>En ekki eru öll leyfi jöfn.</strong></p>

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
<li>Reglulegar úttektir á slembitölugjafa ({U}leidbeiningar/hvernig-rng-virkar/ — <a href="{U}leidbeiningar/hvernig-rng-virkar/">hvernig RNG virkar</a>)</li>
<li>Skyldubundin verkfæri fyrir <a href="{U}leidbeiningar/spila-af-abyrgd/">ábyrga spilun</a></li>
<li>MGA tekur við kvörtunum frá spilurum beint</li>
</ul>
<p>Ef þú lendir í deilu við MGA-spilavíti geturðu sent kvörtun til MGA sem rannsakar málið. Það er raunveruleg vernd.</p>

<h2>Curaçao — algengasta leyfið</h2>
<p>Flest spilavíti sem taka við íslenskum spilurum eru með Curaçao leyfi — þar á meðal <a href="{U}spilaviti/slotoro/">Slotoro</a>, <a href="{U}spilaviti/bitstarz/">BitStarz</a> og <a href="{U}spilaviti/stake/">Stake</a>.</p>
<p><strong>Kostir:</strong> Opið aðgengi, leyfir dulritunargjaldmiðla, færri takmarkanir á bónusum.</p>
<p><strong>Gallar:</strong> Sögulega hefur eftirlit verið veikt og deilumeðferð takmörkuð.</p>
<p><strong>Breytingar 2023–2026:</strong> Curaçao hefur endurskoðað leyfiskerfi sitt (LOK-löggjöfin) með strangari kröfum og beinni útgáfu frá Curaçao Gaming Authority í stað gömlu undirleyfanna. Nýju leyfin eru töluvert betri en þau gömlu.</p>

<h2>Hvað skiptir meira máli en leyfið?</h2>
<p>Leyfið er grunnurinn — en það segir ekki alla söguna. Athugaðu líka:</p>
<ol>
<li><strong>Greiðslusaga</strong> — Greiðir spilavítið út á réttum tíma? Leitaðu að umsögnum frá raunverulegum spilurum</li>
<li><strong>Gegnsæ skilmálar</strong> — Eru <a href="{U}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrði</a> skýrt sett fram?</li>
<li><strong>Aldur og orðspor</strong> — Spilavíti sem hefur starfað í 5+ ár hefur meira að tapa á slæmri hegðun</li>
<li><strong>Þjónustuver</strong> — Prófaðu að senda fyrirspurn fyrir fyrstu innborgun</li>
</ol>
<p>Sjá: <a href="{U}leidbeiningar/einkenni-sanngjarns-spilavitis/">Einkenni sanngjarns spilavítis →</a></p>

<h2>Hvernig staðfesti ég leyfið?</h2>
<p>Neðst á forsíðu spilavítisins á að vera leyfisnúmer og tengill á leyfisskrá. Smelltu á hann — hann á að leiða á opinbera skrá leyfisveitanda þar sem þú sérð stöðu leyfisins.</p>
<p><a href="{U}leidbeiningar/hvernig-a-ad-stadfesta-spilavitaleyfi/">Ítarleg leiðbeining um staðfestingu leyfis →</a></p>

<h2>Algengar spurningar</h2>
<h3>Er Curaçao leyfi öruggt?</h3>
<p>Það veitir grunnvernd en minni en MGA. Fyrir íslenska spilara er það oft eina raunhæfa valið. Veldu þá rótgróin spilavíti með góða greiðslusögu.</p>
<h3>Af hverju taka MGA-spilavíti stundum ekki við Íslendingum?</h3>
<p>Sum MGA-spilavíti einbeita sér að mörkuðum með eigin leyfiskerfi og loka á lönd þar sem staðan er óljós. Þetta er viðskiptaákvörðun, ekki lagaleg skylda.</p>
<h3>Skiptir leyfið máli ef ég spila með Bitcoin?</h3>
<p>Já — leyfið snýst um sanngirni leikja og hvort þú færð útborgað, ekki bara greiðslumáta.</p>''',
    "Sjá spilavíti með leyfi →"))

# ---------- PROVIDERS ----------
P.append(page(
    "playn-go-bestu-spilakassarnir",
    "Play'n GO — bestu spilakassarnir og RTP 2026",
    "Play'n GO leikjaframleiðandi: Book of Dead, Reactoonz, Rise of Olympus. RTP tafla, sveifla og hvar á að spila á Íslandi.",
    "🎲", ("#0a0f28", "#141b45", "#1e2762"),
    f'''<p>Play'n GO er sænskur leikjaframleiðandi sem stendur á bak við <a href="{U}spilakassar/book-of-dead/">Book of Dead</a> — einn vinsælasta spilakassa allra tíma. <strong>Þekkt fyrir háa sveiflu og hreina, hraðvirka leiki.</strong></p>

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
<tr><td>1</td><td><a href="{U}spilakassar/book-of-dead/">Book of Dead</a></td><td>96,21%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>2</td><td><a href="{U}spilakassar/reactoonz/">Reactoonz</a></td><td>96,51%</td><td>Há</td><td>4.570x</td></tr>
<tr><td>3</td><td><a href="{U}spilakassar/fire-joker/">Fire Joker</a></td><td>96,15%</td><td>Meðal</td><td>800x</td></tr>
<tr><td>4</td><td><a href="{U}spilakassar/rise-of-olympus/">Rise of Olympus</a></td><td>96,50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>5</td><td><a href="{U}spilakassar/moon-princess/">Moon Princess</a></td><td>96,50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>6</td><td><a href="{U}spilakassar/legacy-of-dead/">Legacy of Dead</a></td><td>96,58%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>7</td><td><a href="{U}spilakassar/rich-wilde-and-the-amulet/">Rich Wilde and the Amulet</a></td><td>96,50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>8</td><td><a href="{U}spilakassar/book-of-oz/">Book of Oz</a></td><td>96,31%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>9</td><td><a href="{U}spilakassar/rise-of-merlin/">Rise of Merlin</a></td><td>96,52%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>10</td><td><a href="{U}spilakassar/gods-of-rock/">Gods of Rock</a></td><td>96,20%</td><td>Há</td><td>5.000x</td></tr>
</tbody></table>

<h2>Book of Dead — hvers vegna svona vinsælt?</h2>
<p>Book of Dead kom út 2016 og er enn meðal mest spiluðu spilakassa í Evrópu. Ástæðurnar:</p>
<ul>
<li><strong>Einfaldur vélbúnaður</strong> — 10 línur, engar flækjur</li>
<li><strong>Stækkandi tákn</strong> — Í frísnúningum er valið eitt tákn sem stækkar yfir alla hjólið</li>
<li><strong>Há sveifla</strong> — Löng þurrkatímabil en stórir vinningar þegar þeir koma</li>
<li><strong>Frísnúningar oft í bónustilboðum</strong> — Mörg spilavíti nota Book of Dead í <a href="{U}leidbeiningar/okeypis-snuningar-spilaviti/">frísnúningatilboðum</a></li>
</ul>

<h2>Play'n GO vs Pragmatic Play</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Play'n GO</th><th>Pragmatic Play</th></tr></thead><tbody>
<tr><td>Sveifla</td><td>Yfirleitt há</td><td>Meðal til mjög há</td></tr>
<tr><td>Bónus Buy</td><td>Sjaldgæft</td><td>Algengt</td></tr>
<tr><td>Vélbúnaður</td><td>Einfaldur, klassískur</td><td>Tumble, margfaldarar</td></tr>
<tr><td>Hámarksvinningar</td><td>Yfirleitt 5.000x</td><td>Allt að 25.000x</td></tr>
<tr><td>Hentar</td><td>Þeim sem vilja klassíska spilun</td><td>Þeim sem vilja stóra margfaldara</td></tr>
</tbody></table>
<p><a href="{U}leidbeiningar/pragmatic-play-allir-leikir/">Pragmatic Play yfirlit →</a> · <a href="{U}leidbeiningar/netent-saga-og-bestu-leikir/">NetEnt yfirlit →</a></p>

<h2>Hvar á að spila Play'n GO á Íslandi</h2>
<div class="info-box"><p><strong><a href="{U}spilaviti/slotoro/">Slotoro</a></strong> — Play'n GO safnið í boði ásamt 70 öðrum framleiðendum.</p></div>
<div class="info-box"><p><strong><a href="{U}spilaviti/bitstarz/">BitStarz</a></strong> — Allir helstu Play'n GO titlar.</p></div>

<h2>Algengar spurningar</h2>
<h3>Hvaða Play'n GO leikur hefur hæsta RTP?</h3>
<p>Legacy of Dead og Rise of Merlin með um 96,5–96,6%. Munurinn milli leikja er þó lítill — sveiflan skiptir meira máli fyrir upplifunina.</p>
<h3>Er Book of Dead með háa sveiflu?</h3>
<p>Já — mjög háa. Búðu þig undir löng tímabil án vinninga. Veldu veðmálsstærð sem leyfir 300+ snúninga.</p>
<h3>Býður Play'n GO Bónus Buy?</h3>
<p>Aðeins í fáum titlum. Play'n GO hefur haldið sig við klassíska nálgun þar sem frísnúningar koma náttúrulega.</p>''',
    "Spila Play'n GO →"))

P.append(page(
    "nolimit-city-hasveifluleikir",
    "Nolimit City — hásveifluleikir og hámarksvinningar 2026",
    "Nolimit City: Mental, San Quentin, Fire in the Hole. Hæstu sveiflur í bransanum, xWays vélbúnaður og RTP tafla.",
    "💀", ("#1a0a0a", "#331414", "#4d1e1e"),
    f'''<p>Nolimit City er sænskur framleiðandi sem gerir <strong>erfiðustu og sveiflukenndustu spilakassa á markaðnum</strong>. Leikir eins og <a href="{U}spilakassar/mental/">Mental</a> og <a href="{U}spilakassar/san-quentin/">San Quentin</a> hafa orðspor fyrir að vera miskunnarlausir — en hámarksvinningar fara yfir 50.000x.</p>

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
<tr><td><a href="{U}spilakassar/mental/">Mental</a></td><td>96,08%</td><td>Öfgakennd</td><td>66.666x</td></tr>
<tr><td><a href="{U}spilakassar/san-quentin/">San Quentin xWays</a></td><td>96,03%</td><td>Öfgakennd</td><td>150.000x</td></tr>
<tr><td><a href="{U}spilakassar/fire-in-the-hole-xbomb/">Fire in the Hole xBomb</a></td><td>96,06%</td><td>Öfgakennd</td><td>60.000x</td></tr>
<tr><td><a href="{U}spilakassar/tombstone-rip/">Tombstone R.I.P.</a></td><td>96,08%</td><td>Öfgakennd</td><td>300.000x</td></tr>
<tr><td><a href="{U}spilakassar/deadwood/">Deadwood</a></td><td>96,03%</td><td>Há</td><td>13.950x</td></tr>
<tr><td><a href="{U}spilakassar/punk-toilet/">Punk Toilet</a></td><td>96,05%</td><td>Öfgakennd</td><td>44.400x</td></tr>
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
<p>Sjá: <a href="{U}leidbeiningar/hvad-er-sveifla/">Hvað er sveifla og hvers vegna skiptir hún máli →</a> og <a href="{U}leidbeiningar/bankastjornunaradferdir/">bankastjórnunaraðferðir →</a></p>

<h2>Fyrir hverja hentar Nolimit City?</h2>
<ul>
<li>✅ Spilara sem vilja möguleika á risavinningi og sætta sig við löng þurrkatímabil</li>
<li>✅ Þá sem kunna að meta frumlega leikjahönnun og óhefðbundin þemu</li>
<li>❌ <strong>Ekki</strong> byrjendur — byrjaðu frekar á <a href="{U}spilakassar/starburst/">Starburst</a> eða öðrum lágsveifluleikjum</li>
<li>❌ <strong>Ekki</strong> þá sem spila með lítið fjármagn</li>
</ul>
<p>Byrjendur: <a href="{U}leidbeiningar/topp-10-spilakassar-fyrir-byrjendur/">topp 10 spilakassar fyrir byrjendur →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hvaða Nolimit City leikur hefur hæsta hámarksvinning?</h3>
<p>Tombstone R.I.P. með 300.000x veðmálið. Á €0,20 snúningi væri það €60.000 — en líkurnar eru hverfandi.</p>
<h3>Er RTP lágt hjá Nolimit City?</h3>
<p>Nei — um 96% sem er staðlað. Það er sveiflan sem er öfgakennd, ekki RTP.</p>
<h3>Hvar get ég spilað Nolimit City á Íslandi?</h3>
<p><a href="{U}spilaviti/slotoro/">Slotoro</a> og <a href="{U}spilaviti/bitstarz/">BitStarz</a> bjóða báðir Nolimit City safnið.</p>''',
    "Spila Nolimit City →"))

# ---------- STRATEGY / GAME RULES ----------
P.append(page(
    "martingale-adferd-rulletta",
    "Martingale aðferðin í rúllettu — virkar hún? 2026",
    "Martingale veðmálakerfið útskýrt á íslensku: hvernig það virkar, stærðfræðin á bak við það og hvers vegna það bregst.",
    "📉", ("#280a0a", "#451414", "#621e1e"),
    f'''<p>Martingale er frægasta veðmálakerfið í sögu spilavíta: <strong>tvöfaldaðu veðmálið eftir hvert tap, og þegar þú vinnur færðu allt til baka plús einn vinning.</strong> Hljómar óbrigðult. Það er það ekki.</p>

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
<li><strong>Veldu leiki með lágt húsforskot</strong> — <a href="{U}leidbeiningar/baccarat-reglur-a-islensku/">Baccarat (Banker)</a> 1,06%, <a href="{U}leidbeiningar/blackjack-adferdir/">blackjack með grunnstrategíu</a> 0,5%</li>
<li><strong>Spilaðu evrópska rúllettu</strong> — 2,7% á móti 5,26% á amerískri</li>
<li><strong>Settu tap- og vinningsmörk</strong> — Ákveddu fyrirfram hvenær þú hættir</li>
<li><strong>Fast veðmál</strong> — Sama upphæð í hverri umferð. Leiðinlegra en mun öruggara</li>
</ul>
<p><a href="{U}leidbeiningar/bankastjornunaradferdir/">Bankastjórnunaraðferðir →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hefur einhver grætt á Martingale?</h3>
<p>Til skamms tíma — já, margir. Kerfið gefur tíða litla vinninga. Vandamálið er að eitt langt taptímabil þurrkar út allan ágóðann og meira til.</p>
<h3>Virkar Martingale í blackjack?</h3>
<p>Sömu vandamál: borðtakmörk og endanlegt fjármagn. Í blackjack er betra að einbeita sér að <a href="{U}leidbeiningar/blackjack-adferdir/">grunnstrategíu</a> sem raunverulega lækkar húsforskotið.</p>
<h3>Banna spilavíti Martingale?</h3>
<p>Nei — spilavíti hafa ekkert á móti því. Borðtakmörkin sjá til þess að kerfið virki ekki til lengdar.</p>''',
    "Spila rúllettu →"))

P.append(page(
    "texas-holdem-reglur-a-islensku",
    "Texas Hold'em reglur á íslensku — hvernig á að spila póker 2026",
    "Texas Hold'em reglur á íslensku: handaröð, veðmálaumferðir, position og grunnstrategy fyrir byrjendur.",
    "♠️", ("#0a1a0f", "#14331e", "#1e4d2d"),
    f'''<p>Texas Hold'em er vinsælasta pókerafbrigðið í heiminum. <strong>Reglurnar eru einfaldar — en leikurinn tekur ævi að ná tökum á.</strong> Hér eru grunnreglurnar á íslensku.</p>

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
<div class="info-box"><p><strong><a href="{U}live/poker/">Lifandi póker á Svipan</a></strong> — Yfirlit yfir lifandi pókerleiki</p></div>
<div class="info-box"><p><strong><a href="{U}live/texas-holdem-bonus/">Texas Hold'em Bonus</a></strong> — Spilavítisútgáfa gegn dílara (ekki gegn öðrum spilurum)</p></div>
<div class="info-box"><p><strong><a href="{U}spilaviti/poker-spilaviti/">Pókerspilavíti</a></strong> — Spilavíti með pókerhluta</p></div>

<h2>Algengar spurningar</h2>
<h3>Hver er munurinn á póker og spilavítispóker?</h3>
<p>Í hefðbundnum póker spilar þú gegn öðrum spilurum og spilavítið tekur þóknun af pottinum. Í spilavítispóker (t.d. Texas Hold'em Bonus) spilar þú gegn húsinu með föstum reglum og húsforskoti.</p>
<h3>Er póker heppni eða kunnátta?</h3>
<p>Hvort tveggja. Til skamms tíma ræður heppnin miklu, en til langs tíma skilar kunnátta sér. Það er ástæðan fyrir því að sömu nöfn birtast ítrekað á úrslitaborðum stórmóta.</p>
<h3>Hvað er „bluff"?</h3>
<p>Að veðja árásargjarnt með veika hönd til að fá andstæðinginn til að kasta betri hönd. Mikilvægur hluti leiksins en ofnotaður hjá byrjendum.</p>''',
    "Spila póker →"))

# ---------- COMPARISONS ----------
P.append(page(
    "bestu-spilakassarnir-haesta-rtp",
    "Spilakassar með hæsta RTP 2026 — topp 20 listi",
    "Listi yfir spilakassa með hæsta RTP (allt að 99%). Hvað RTP þýðir raunverulega og hvernig á að finna rétta stillingu.",
    "📊", ("#0a1a1a", "#143333", "#1e4d4d"),
    f'''<p>RTP (Return to Player) segir hversu hátt hlutfall af veðjuðum peningum spilakassi greiðir til baka <strong>yfir milljónir snúninga</strong>. Hærra RTP þýðir lægra húsforskot — en það tryggir ekki vinning í þinni lotu.</p>

<h2>Topp 20 spilakassar eftir RTP</h2>
<table class="info-table"><thead><tr><th>#</th><th>Spilakassi</th><th>Framleiðandi</th><th>RTP</th><th>Sveifla</th></tr></thead><tbody>
<tr><td>1</td><td><a href="{U}spilakassar/blood-suckers/">Blood Suckers</a></td><td>NetEnt</td><td>98,00%</td><td>Lág</td></tr>
<tr><td>2</td><td><a href="{U}spilakassar/starmania/">Starmania</a>*</td><td>NextGen</td><td>97,87%</td><td>Lág</td></tr>
<tr><td>3</td><td><a href="{U}spilakassar/dead-or-alive/">Dead or Alive</a></td><td>NetEnt</td><td>96,82%</td><td>Há</td></tr>
<tr><td>4</td><td><a href="{U}spilakassar/big-bass-bonanza/">Big Bass Bonanza</a></td><td>Pragmatic Play</td><td>96,71%</td><td>Há</td></tr>
<tr><td>5</td><td><a href="{U}spilakassar/finn-and-the-swirly-spin/">Finn and the Swirly Spin</a></td><td>NetEnt</td><td>96,62%</td><td>Meðal</td></tr>
<tr><td>6</td><td><a href="{U}spilakassar/divine-fortune/">Divine Fortune</a></td><td>NetEnt</td><td>96,59%</td><td>Meðal</td></tr>
<tr><td>7</td><td><a href="{U}spilakassar/legacy-of-dead/">Legacy of Dead</a></td><td>Play'n GO</td><td>96,58%</td><td>Há</td></tr>
<tr><td>8</td><td><a href="{U}spilakassar/twin-spin/">Twin Spin</a></td><td>NetEnt</td><td>96,55%</td><td>Meðal</td></tr>
<tr><td>9</td><td><a href="{U}spilakassar/rise-of-merlin/">Rise of Merlin</a></td><td>Play'n GO</td><td>96,52%</td><td>Há</td></tr>
<tr><td>10</td><td><a href="{U}spilakassar/reactoonz/">Reactoonz</a></td><td>Play'n GO</td><td>96,51%</td><td>Há</td></tr>
<tr><td>11</td><td><a href="{U}spilakassar/gates-of-olympus/">Gates of Olympus</a></td><td>Pragmatic Play</td><td>96,50%</td><td>Há</td></tr>
<tr><td>12</td><td><a href="{U}spilakassar/rise-of-olympus/">Rise of Olympus</a></td><td>Play'n GO</td><td>96,50%</td><td>Há</td></tr>
<tr><td>13</td><td><a href="{U}spilakassar/moon-princess/">Moon Princess</a></td><td>Play'n GO</td><td>96,50%</td><td>Há</td></tr>
<tr><td>14</td><td><a href="{U}spilakassar/sugar-rush/">Sugar Rush</a></td><td>Pragmatic Play</td><td>96,50%</td><td>Há</td></tr>
<tr><td>15</td><td><a href="{U}spilakassar/sweet-bonanza/">Sweet Bonanza</a></td><td>Pragmatic Play</td><td>96,48%</td><td>Meðal-há</td></tr>
<tr><td>16</td><td><a href="{U}spilakassar/fruit-party/">Fruit Party</a></td><td>Pragmatic Play</td><td>96,47%</td><td>Há</td></tr>
<tr><td>17</td><td><a href="{U}spilakassar/razor-shark/">Razor Shark</a></td><td>Push Gaming</td><td>96,70%</td><td>Há</td></tr>
<tr><td>18</td><td><a href="{U}spilakassar/jammin-jars/">Jammin' Jars</a></td><td>Push Gaming</td><td>96,83%</td><td>Há</td></tr>
<tr><td>19</td><td><a href="{U}spilakassar/dead-or-alive-2/">Dead or Alive 2</a></td><td>NetEnt</td><td>96,29%</td><td>Mjög há</td></tr>
<tr><td>20</td><td><a href="{U}spilakassar/book-of-dead/">Book of Dead</a></td><td>Play'n GO</td><td>96,21%</td><td>Há</td></tr>
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
<li><strong>Lág sveifla</strong> (t.d. <a href="{U}spilakassar/starburst/">Starburst</a>) — Tíðir litlir vinningar, jafnari spilun, fjármagnið endist lengur</li>
<li><strong>Há sveifla</strong> (t.d. <a href="{U}spilakassar/book-of-dead/">Book of Dead</a>) — Löng þurrkatímabil, en stærri vinningar þegar þeir koma</li>
</ul>
<p><a href="{U}leidbeiningar/hvad-er-sveifla/">Hvað er sveifla? →</a> · <a href="{U}leidbeiningar/lag-sveiflu-spilakassar/">Lágsveifluspilakassar →</a></p>

<h2>Hvað þýðir 96% RTP í raun?</h2>
<p>Af hverjum €100 sem veðjaðir eru í leiknum — samanlagt af öllum spilurum yfir milljónir snúninga — skilar hann €96 til baka. Það þýðir <strong>ekki</strong> að þú fáir €96 til baka af þínum €100.</p>
<p>Í þinni lotu geturðu fengið €0 eða €5.000. RTP lýsir langtímameðaltali, ekki einstökum lotum.</p>
<p><a href="{U}leidbeiningar/hvad-er-rtp/">Ítarleg RTP útskýring →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hvaða spilakassi hefur hæsta RTP?</h3>
<p>Blood Suckers frá NetEnt með 98%. Það er einnig lágsveifluleikur sem þýðir að fjármagnið endist lengi.</p>
<h3>Ætti ég alltaf að velja hæsta RTP?</h3>
<p>Ekki endilega. Ef þú vilt möguleika á stórum vinningi skiptir hámarksvinningur og sveifla meira máli. Ef þú vilt löng spilalota með litlu tapi — veldu hátt RTP og lága sveiflu.</p>
<h3>Hafa spilavíti áhrif á RTP?</h3>
<p>Þau geta valið milli RTP-útgáfa sem framleiðandinn býður. Þau geta ekki breytt niðurstöðum í rauntíma — <a href="{U}leidbeiningar/hvernig-rng-virkar/">RNG-inn</a> er vottaður af óháðum prófunaraðilum.</p>''',
    "Spila hátt RTP spilakassa →"))

# ---------- RESPONSIBLE ----------
P.append(page(
    "hvernig-a-ad-setja-takmork-a-spilaviti",
    "Hvernig á að setja takmörk á spilavíti — verkfæri sem virka 2026",
    "Innborgunartakmörk, tapmörk, tímamörk og sjálfsútilokun. Hvernig á að stilla þau og hvers vegna það skiptir máli.",
    "🎚️", ("#0f1a0a", "#1e3314", "#2d4d1e"),
    f'''<p>Takmörk eru öflugasta verkfærið sem þú hefur til að halda spilun innan heilbrigðra marka. <strong>Þau virka vegna þess að þú tekur ákvörðunina þegar þú ert rólegur — ekki í miðri lotu.</strong></p>

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
<p><a href="{U}leidbeiningar/sjalfsutilokun-spilavita/">Ítarlegt um sjálfsútilokun →</a></p>

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
<p>Sjá einnig: <a href="{U}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">merki spilafiknar →</a> og <a href="{U}leidbeiningar/studningssidur-vid-spilafikn/">stuðningsúrræði á Íslandi →</a></p>

<h2>Algengar spurningar</h2>
<h3>Get ég afturkallað takmörk?</h3>
<p>Að lækka takmörk gerist strax. Að hækka þau tekur 24–72 klst í gildi hjá flestum spilavítum með gilt leyfi.</p>
<h3>Virka takmörk á öllum spilavítum?</h3>
<p>Nei — takmörk gilda aðeins á því spilavíti þar sem þú stillir þau. Ef þú spilar á mörgum stöðum þarftu að stilla þau alls staðar, eða nota BetBlocker sem lokar á allt.</p>
<h3>Hvað ef spilavítið býður ekki takmörk?</h3>
<p>Þá er það ekki spilavíti sem þú átt að nota. Öll spilavíti með gilt leyfi eru skyldug til að bjóða þessi verkfæri.</p>''',
    "Sjá ábyrga spilun →"))

P.append(page(
    "radleggingar-til-adstandenda-spilafikla",
    "Ráðleggingar til aðstandenda spilafíkla — hvernig á að hjálpa 2026",
    "Hvernig á að tala við ástvin sem glímir við spilafikn, hvað á að forðast og hvaða hjálp er í boði á Íslandi.",
    "🤝", ("#1a1413", "#332826", "#4d3c39"),
    f'''<p>Spilafikn snertir ekki bara þann sem spilar. <strong>Maki, börn, foreldrar og vinir verða líka fyrir áhrifum</strong> — fjárhagslega og tilfinningalega. Hér eru hagnýt ráð ef einhver nálægt þér glímir við þetta.</p>

<h2>Merki sem þú gætir tekið eftir</h2>
<ul>
<li>Peningar hverfa án skýringa, eða lán eru tekin ítrekað</li>
<li>Leynd um fjármál — reikningar faldir, símtöl tekin í einrúmi</li>
<li>Skapsveiflur sem fylgja vinningum og töpum</li>
<li>Minni þátttaka í fjölskyldulífi eða áhugamálum</li>
<li>Loforð um að hætta sem ekki eru efnd</li>
<li>Svefnvandamál, kvíði eða þunglyndi</li>
</ul>
<p>Sjá ítarlegri lista: <a href="{U}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">10 merki spilafiknar →</a></p>

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
<li><strong>Hjálpaðu við hagnýt skref</strong> — <a href="{U}leidbeiningar/sjalfsutilokun-spilavita/">Sjálfsútilokun</a>, lokun á bankagreiðslur, uppsetning BetBlocker</li>
<li><strong>Fagnaðu litlum sigrum</strong> — Vika án spilunar er árangur</li>
<li><strong>Gerðu ráð fyrir bakslagi</strong> — Það er algengt og þýðir ekki að allt sé tapað</li>
</ul>

<h2>Ekki gleyma sjálfum þér</h2>
<p>Aðstandendur brenna oft út. Þú átt líka rétt á stuðningi:</p>
<div class="info-box"><p><strong>Hjálparsíminn 1717</strong> — Opinn allan sólarhringinn. Þú getur hringt fyrir þig sjálfan, ekki bara fyrir þann sem spilar.</p></div>
<div class="info-box"><p><strong>Gam-Anon</strong> — Alþjóðlegir stuðningshópar sérstaklega fyrir aðstandendur spilafíkla.</p></div>
<div class="info-box"><p><strong>SÁÁ</strong> — Veitir ráðgjöf til aðstandenda, ekki bara þeirra sem glíma við fíknina.</p></div>
<p><a href="{U}leidbeiningar/studningssidur-vid-spilafikn/">Öll stuðningsúrræði á Íslandi →</a></p>

<h2>Algengar spurningar</h2>
<h3>Á ég að borga skuldirnar til að „hreinsa borðið"?</h3>
<p>Ráðgjafar mæla almennt gegn því. Þegar afleiðingarnar hverfa minnkar hvatinn til að breyta hegðun. Betra er að styðja viðkomandi í að takast á við skuldirnar sjálfur, með faglegri aðstoð.</p>
<h3>Hvað ef viðkomandi neitar að það sé vandamál?</h3>
<p>Afneitun er algeng. Þú getur ekki þvingað fram bata — en þú getur sett eigin mörk, verndað þig fjárhagslega og haldið dyrunum opnum. Margir leita hjálpar síðar.</p>
<h3>Hvernig tala ég við börn um þetta?</h3>
<p>Aldurssvarandi hreinskilni virkar best. Börn skynja spennu hvort sem er og kenna sér oft um. Útskýrðu að þetta sé veikindi fullorðins, ekki þeim að kenna, og að verið sé að leita hjálpar.</p>''',
    "Sjá stuðningsúrræði →"))

# ---------- WRITE ----------
blocks = "\n".join(P)
with open("generate.py", "r", encoding="utf-8") as f:
    code = f.read()
marker = "    },\n]"
idx = code.rfind(marker)
if idx == -1:
    raise SystemExit("marker not found")
pos = idx + len("    },\n")
code = code[:pos] + blocks + "\n" + code[pos:]
with open("generate.py", "w", encoding="utf-8") as f:
    f.write(code)
print(f"inserted {len(P)} pages")
