#!/usr/bin/env python3
"""Batch 2: Add more pages to seo_pages in generate.py"""
import re

AFF = "https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/"
B = "{URL_BASE}"

pages_code = '''    {
        "slug": "ice-casino-a-islandi",
        "title": "Ice Casino á Íslandi — umsögn, bónus og greiðslur 2026",
        "desc": "Ice Casino umsögn fyrir íslenska spilara. Velkomstbónus, leikjaúrval, greiðsluleiðir og hvort þetta spilavíti tekur við frá Íslandi.",
        "emoji": "🧊",
        "colors": ("#0a1a2e", "#143050", "#1e4672"),
        "content": f\'\'\'<h1>Ice Casino á Íslandi — umsögn 2026</h1>
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
<p>Veðskilyrði: 40x bónus. {guide_link("hvad-eru-vedskilyrdi", "Hvað þýðir 40x veðskilyrði? →")}</p>

<h2>Leikjaúrval</h2>
<p>Ice Casino er með yfir 3.500 leiki frá 50+ framleiðendum: Pragmatic Play, NetEnt, Play\'n GO, Evolution, Microgaming og fleiri. Gott úrval af spilakössum, lifandi spilavíti og borðleikjum.</p>

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
<div class="cta-box"><a href="''' + AFF + '''" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>\'\'\'
    },
    {
        "slug": "vulkan-vegas-a-islandi",
        "title": "Vulkan Vegas á Íslandi — umsögn og greiðsluleiðir 2026",
        "desc": "Vulkan Vegas umsögn: bónus allt að €1.000, 5.000+ leikir. Er þetta spilavíti gott fyrir íslenska spilara?",
        "emoji": "🌋",
        "colors": ("#1a0a00", "#331400", "#4d1e00"),
        "content": f\'\'\'<h1>Vulkan Vegas á Íslandi — umsögn 2026</h1>
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
<div class="cta-box"><a href="''' + AFF + '''" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>\'\'\'
    },
    {
        "slug": "gates-of-olympus-leidarvísir",
        "title": "Gates of Olympus — leiðarvísir, RTP og aðferðir 2026",
        "desc": "Gates of Olympus spilakassi: RTP 96.5%, há sveifla, allt að 5.000x vinningur. Hvernig virkar leikurinn og hvar á að spila.",
        "emoji": "⚡",
        "colors": ("#1a0a28", "#2d1445", "#401e62"),
        "content": f\'\'\'<h1>Gates of Olympus — leiðarvísir 2026</h1>
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
<p>Þú getur keypt þig beint í frísnúninga fyrir 100x veðmálið þitt. Dæmi: ef þú spilar á €0.20 kostar Bónus Buy €20. Þetta er áhættusamt en skemmtilegt. {guide_link("bonus-buy-spilakassar", "Er Bónus Buy þess virði? →")}</p>

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
<div class="cta-box"><a href="''' + AFF + '''" target="_blank" rel="noopener" class="cta-btn">Spila Gates of Olympus →</a></div>\'\'\'
    },
    {
        "slug": "sweet-bonanza-leidarvísir",
        "title": "Sweet Bonanza — leiðarvísir, RTP og bónuseiginleikar 2026",
        "desc": "Sweet Bonanza spilakassi: RTP 96.48%, há sveifla, Tumble og margfaldarar. Hvernig á að spila og hvar á Íslandi.",
        "emoji": "🍬",
        "colors": ("#2e0a1a", "#501430", "#721e46"),
        "content": f\'\'\'<h1>Sweet Bonanza — leiðarvísir 2026</h1>
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
<div class="cta-box"><a href="''' + AFF + '''" target="_blank" rel="noopener" class="cta-btn">Spila Sweet Bonanza →</a></div>\'\'\'
    },
    {
        "slug": "netent-saga-og-bestu-leikir",
        "title": "NetEnt — saga, bestu leikir og RTP 2026",
        "desc": "NetEnt leikjaframleiðandi: Starburst, Gonzo\'s Quest, Dead or Alive og fleiri. RTP tafla, saga og bestu spilavítin á Íslandi.",
        "emoji": "🎮",
        "colors": ("#0a1a0a", "#143314", "#1e4d1e"),
        "content": f\'\'\'<h1>NetEnt — saga og bestu leikir 2026</h1>
{hero}
<p>NetEnt (Net Entertainment) er <strong>einn elsti og virtusti leikjaframleiðandinn</strong> í iGaming bransanum. Ef þú hefur spilað <a href="{URL_BASE}spilakassar/starburst/">Starburst</a>, <a href="{URL_BASE}spilakassar/gonzos-quest/">Gonzo\'s Quest</a> eða <a href="{URL_BASE}spilakassar/dead-or-alive/">Dead or Alive</a> — þú hefur spilað NetEnt.</p>

<h2>Um NetEnt</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>1996 (einn af fyrstu framleiðendum)</td></tr>
<tr><td>Höfuðstöðvar</td><td>Stokkhólmur, Svíþjóð</td></tr>
<tr><td>Eigandi</td><td>Evolution Gaming Group (síðan 2020)</td></tr>
<tr><td>Fjöldi leikja</td><td>200+ spilakassar</td></tr>
<tr><td>Þekktustu leikir</td><td>Starburst, Gonzo\'s Quest, Dead or Alive, Divine Fortune</td></tr>
<tr><td>Sérkenni</td><td>Há gæði, lág-meðal sveifla, nýsköpun</td></tr>
</tbody></table>

<h2>Topp 10 NetEnt leikir á Íslandi</h2>
<table class="info-table"><thead><tr><th>#</th><th>Leikur</th><th>RTP</th><th>Sveifla</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td>1</td><td><a href="{URL_BASE}spilakassar/starburst/">Starburst</a></td><td>96.09%</td><td>Lág</td><td>500x</td></tr>
<tr><td>2</td><td><a href="{URL_BASE}spilakassar/gonzos-quest/">Gonzo\'s Quest</a></td><td>95.97%</td><td>Meðal</td><td>2.500x</td></tr>
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
<div class="cta-box"><a href="''' + AFF + '''" target="_blank" rel="noopener" class="cta-btn">Spila NetEnt leiki →</a></div>\'\'\'
    },
    {
        "slug": "spilaviti-an-vedskilyrda",
        "title": "Spilavíti án veðskilyrða á Íslandi — bónusar sem þú heldur 2026",
        "desc": "Netspilavíti án veðskilyrða: vinningar frá bónus eru þínir strax. Listi yfir bestu veðlausu spilavítin á Íslandi.",
        "emoji": "🎁",
        "colors": ("#280a1a", "#451430", "#621e46"),
        "content": f\'\'\'<h1>Spilavíti án veðskilyrða á Íslandi 2026</h1>
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
<div class="cta-box"><a href="''' + AFF + '''" target="_blank" rel="noopener" class="cta-btn">Fá veðlausan bónus →</a></div>\'\'\'
    },
    {
        "slug": "baccarat-reglur-a-islensku",
        "title": "Baccarat reglur á íslensku — hvernig á að spila 2026",
        "desc": "Baccarat reglur útskýrðar á íslensku: Player, Banker, Tie. Veðmálamöguleikar, húsforskot og hvar á að spila á Íslandi.",
        "emoji": "🎴",
        "colors": ("#1a0a1a", "#331433", "#4d1e4d"),
        "content": f\'\'\'<h1>Baccarat reglur á íslensku 2026</h1>
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
<div class="cta-box"><a href="''' + AFF + '''" target="_blank" rel="noopener" class="cta-btn">Spila baccarat →</a></div>\'\'\'
    },'''

# Read generate.py
with open("generate.py", "r", encoding="utf-8") as f:
    code = f.read()

# Find the end of seo_pages list
# Look for the closing bracket on its own line after the last page
marker = "    },\n]"
# Find the LAST occurrence
idx = code.rfind(marker)
if idx == -1:
    print("❌ Could not find end of seo_pages")
else:
    # Insert before the ]
    insert_pos = idx + len("    },\n")
    code = code[:insert_pos] + pages_code + "\n" + code[insert_pos:]
    with open("generate.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("✅ Inserted 7 new pages into generate.py")
