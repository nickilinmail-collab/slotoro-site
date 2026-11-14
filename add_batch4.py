#!/usr/bin/env python3
"""Batch 4: payments, slot guides, game rules, providers, comparisons."""

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

P.append(page(
    "gjaldmidlaskipti-isk-eur-spilaviti",
    "Gjaldmiðlaskipti ISK í EUR fyrir spilavíti — hvernig á að spara 2026",
    "Hvað kostar að skipta ISK í EUR fyrir spilavítainnlagnir? Samanburður á bönkum, Revolut, Wise og dulritunargjaldmiðlum.",
    "💱", ("#0a1a1f", "#14333a", "#1e4d55"),
    f'''<p>Nánast öll netspilavíti nota EUR eða USD — ekki íslenskar krónur. <strong>Það þýðir að í hvert sinn sem þú leggur inn borgar þú gjaldmiðlaskiptagjald.</strong> Yfir ár getur þetta orðið umtalsvert, og flestir taka aldrei eftir því.</p>

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
<li><strong>USDT veski</strong> — Kauptu USDT einu sinni, sendu inn og út án frekari skipta. <a href="{U}leidbeiningar/hvernig-a-ad-kaupa-usdt-island/">Hvernig á að kaupa USDT →</a></li>
</ul>
<p>Með þessari aðferð borgar þú skiptagjald einu sinni í stað þess að greiða það við hverja innborgun og úttekt.</p>

<h2>Revolut — mikilvæg smáatriði</h2>
<p>Revolut býður gjaldmiðlaskipti á millibankagengi (interbank rate) án álags — en með takmörkunum:</p>
<ul>
<li><strong>Mánaðarþak</strong> á ókeypis skiptum á grunnáskrift. Yfir þakið bætist við lítið gjald</li>
<li><strong>Helgarálag</strong> — Um helgar (þegar gjaldeyrismarkaðir eru lokaðir) bætir Revolut við um 1% álagi</li>
</ul>
<p>Ráð: skiptu ISK í EUR á virkum degi, ekki á laugardagskvöldi.</p>
<p><a href="{U}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut fyrir spilavíti — ítarleg leiðbeining →</a></p>

<h2>Spilavíti sem taka við ISK</h2>
<p>Örfá spilavíti bjóða ISK sem gjaldmiðil. Það hljómar vel en athugaðu: þegar spilavíti býður ISK er það yfirleitt með eigin gengi sem getur verið óhagstæðara en bankinn þinn. Berðu saman áður en þú velur.</p>
<p><a href="{U}leidbeiningar/spilaviti-isk-kronur/">Spilavíti sem taka við íslenskum krónum →</a></p>

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
<p>Ef þú heldur jafnvægi í EUR tekurðu á þig gengisáhættu EUR/ISK. Yfir stutt tímabil er hún lítil, en hafðu hana í huga ef þú geymir stórar upphæðir.</p>''',
    "Finna spilavíti →"))

P.append(page(
    "paysafecard-a-islandi-spilaviti",
    "Paysafecard á Íslandi — fyrirframgreitt kort fyrir spilavíti 2026",
    "Hvernig Paysafecard virkar á Íslandi: hvar á að kaupa, hvernig á að nota og af hverju úttektir virka ekki.",
    "🎟️", ("#0a1428", "#142445", "#1e3462"),
    f'''<p>Paysafecard er fyrirframgreiddur kóði sem þú kaupir með reiðufé eða korti og notar til innborgunar — án þess að gefa upp bankaupplýsingar. <strong>Fyrir íslenska spilara hefur það einn stóran kost og einn stóran galla.</strong></p>

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
<p>Fyrir flesta íslenska spilara eru <a href="{U}leidbeiningar/bestu-crypto-spilavitin-island/">dulritunargjaldmiðlar</a> eða <a href="{U}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut</a> betri kostur — þeir virka í báðar áttir.</p>

<h2>Hverjum hentar Paysafecard?</h2>
<ul>
<li>✅ Þeim sem vilja <strong>hart eyðsluþak</strong> — þú getur ekki eytt meiru en kóðinn inniheldur</li>
<li>✅ Þeim sem vilja alls ekki tengja bankareikning við spilavíti</li>
<li>❌ Ekki þeim sem spila reglulega og taka út oft</li>
</ul>
<p>Eyðsluþakið er raunverulegur kostur frá sjónarhóli <a href="{U}leidbeiningar/hvernig-a-ad-setja-takmork-a-spilaviti/">ábyrgrar spilunar</a> — þú getur ekki „bara lagt inn aðeins meira" í hita leiksins.</p>

<h2>Algengar spurningar</h2>
<h3>Rennur Paysafecard kóði út?</h3>
<p>Kóðar gilda yfirleitt í 12 mánuði. Eftir það getur mánaðarlegt gjald dregist af eftirstöðvum.</p>
<h3>Get ég notað hluta af kóða?</h3>
<p>Já — þú getur notað hluta og geymt eftirstöðvarnar til síðari nota á sama kóða.</p>
<h3>Hvaða spilavíti taka við Paysafecard?</h3>
<p>Mörg evrópsk spilavíti, en ekki öll. Athugaðu greiðslusíðu spilavítisins fyrst. <a href="{U}greidslur/paysafecard-i-spilavitum/">Sjá Paysafecard spilavíti →</a></p>''',
    "Sjá greiðsluleiðir →"))

P.append(page(
    "book-of-dead-leidarvisir",
    "Book of Dead — leiðarvísir, RTP og aðferðir 2026",
    "Book of Dead frá Play'n GO: RTP 96,21%, há sveifla, stækkandi tákn. Hvernig leikurinn virkar og hvar á að spila á Íslandi.",
    "📖", ("#281a0a", "#453014", "#62461e"),
    f'''<p>Book of Dead kom út árið 2016 og er enn meðal mest spiluðu spilakassa í Evrópu. <strong>Einfaldur vélbúnaður, há sveifla og stækkandi tákn sem geta fyllt alla skjáinn.</strong></p>

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
<li><strong>Prófaðu í demo fyrst</strong> — <a href="{U}spilakassar/book-of-dead/">Spila Book of Dead ókeypis</a></li>
<li><strong>Athugaðu RTP-útgáfuna</strong> — Play'n GO gefur út margar RTP-stillingar. Athugaðu í leikjareglum að þú sért á 96,21%, ekki lægri útgáfu. <a href="{U}leidbeiningar/bestu-spilakassarnir-haesta-rtp/">Meira um RTP-útgáfur →</a></li>
<li><strong>Frísnúningatilboð</strong> — Book of Dead er algengasti leikurinn í <a href="{U}leidbeiningar/okeypis-snuningar-spilaviti/">frísnúningatilboðum</a>. Góð leið til að prófa án eigin fjármuna</li>
</ul>

<h2>Book of Dead vs aðrir „book" leikir</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>Framleiðandi</th><th>RTP</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td><a href="{U}spilakassar/book-of-dead/">Book of Dead</a></td><td>Play'n GO</td><td>96,21%</td><td>5.000x</td></tr>
<tr><td><a href="{U}spilakassar/legacy-of-dead/">Legacy of Dead</a></td><td>Play'n GO</td><td>96,58%</td><td>5.000x</td></tr>
<tr><td><a href="{U}spilakassar/book-of-oz/">Book of Oz</a></td><td>Play'n GO</td><td>96,31%</td><td>5.000x</td></tr>
<tr><td><a href="{U}spilakassar/book-of-fallen/">Book of Fallen</a></td><td>Pragmatic Play</td><td>96,50%</td><td>5.000x</td></tr>
</tbody></table>
<p>Legacy of Dead hefur hæsta RTP af þessum — nánast sami leikur með aðeins betri stærðfræði.</p>

<h2>Hvar á að spila á Íslandi</h2>
<div class="info-box"><p><strong><a href="{U}spilaviti/slotoro/">Slotoro</a></strong> — Play'n GO safnið, demo í boði, €10 lágmarksinnborgun.</p></div>
<div class="info-box"><p><strong><a href="{U}spilaviti/bitstarz/">BitStarz</a></strong> — Book of Dead ásamt öllu Play'n GO safninu.</p></div>

<h2>Algengar spurningar</h2>
<h3>Hvað er hámarksvinningur í Book of Dead?</h3>
<p>5.000x veðmálið. Á €1 snúningi væri það €5.000. Þarf stækkandi Rich Wilde tákn yfir mörg hjól.</p>
<h3>Er hægt að kaupa frísnúninga?</h3>
<p>Nei — Book of Dead býður ekki Bónus Buy. Þú þarft að fá þrjár bækur náttúrulega.</p>
<h3>Af hverju vinn ég ekkert í langan tíma?</h3>
<p>Það er eðli hásveifluleikja. Book of Dead getur farið 200–300 snúninga án umtalsverðs vinnings. Ef það er óþægilegt skaltu skoða <a href="{U}leidbeiningar/lag-sveiflu-spilakassar/">lágsveifluspilakassa</a>.</p>''',
    "Spila Book of Dead →"))

P.append(page(
    "lightning-roulette-adferdir",
    "Lightning Roulette — aðferðir, RTP og hvernig það virkar 2026",
    "Lightning Roulette frá Evolution: margfaldarar allt að 500x, RTP 97,3% og hvernig margfaldararnir hafa áhrif á útborganir.",
    "⚡", ("#1a0a28", "#2d1445", "#401e62"),
    f'''<p>Lightning Roulette frá Evolution er <strong>vinsælasta lifandi rúllettan í heiminum</strong>. Grunnreglurnar eru þær sömu og í evrópskri rúllettu — en 1–5 tölur fá margfaldara í hverri umferð.</p>

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
<li><strong>Forðist Martingale</strong> — Með 29:1 útborgun og einstaka tölur virkar tvöföldunarkerfi enn verr en í venjulegri rúllettu. <a href="{U}leidbeiningar/martingale-adferd-rulletta/">Af hverju Martingale bregst →</a></li>
<li><strong>Settu lotumörk</strong> — Margfaldararnir gera leikinn spennandi, sem gerir það auðveldara að spila lengur en ætlað var</li>
</ul>

<h2>Afbrigði frá Evolution</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>Sérkenni</th><th>Hámarksmargfaldari</th></tr></thead><tbody>
<tr><td><a href="{U}live/lightning-roulette/">Lightning Roulette</a></td><td>Upprunalega útgáfan</td><td>500x</td></tr>
<tr><td><a href="{U}live/xxxtreme-lightning-roulette/">XXXtreme Lightning Roulette</a></td><td>Keðjueldingar, allt að 2.000x</td><td>2.000x</td></tr>
<tr><td><a href="{U}live/lightning-baccarat/">Lightning Baccarat</a></td><td>Sama hugmynd í baccarat</td><td>512x</td></tr>
<tr><td><a href="{U}live/lightning-blackjack/">Lightning Blackjack</a></td><td>Margfaldarar á vinningshendur</td><td>25x</td></tr>
<tr><td><a href="{U}live/lightning-dice/">Lightning Dice</a></td><td>Teningar með margföldurum</td><td>1.000x</td></tr>
</tbody></table>

<h2>Algengar spurningar</h2>
<h3>Er RTP lægra í Lightning Roulette?</h3>
<p>Nei — 97,30%, sama og venjuleg evrópsk rúlletta. Lægri grunnútborgun á beinar tölur er vegin upp af margföldurunum.</p>
<h3>Get ég spáð fyrir um eldingartölur?</h3>
<p>Nei. Þær eru valdar af slembitölugjafa í hverri umferð, óháð fyrri umferðum.</p>
<h3>Er hægt að spila Lightning Roulette ókeypis?</h3>
<p>Nei — lifandi leikir með raunverulegum spilastjóra eru ekki í boði í demo-ham. Þú getur hins vegar æft þig á <a href="{U}leidbeiningar/rullettureglur-a-islensku/">RNG rúllettu</a> ókeypis.</p>''',
    "Spila Lightning Roulette →"))

P.append(page(
    "keno-reglur-a-islensku",
    "Keno reglur á íslensku — hvernig á að spila 2026",
    "Keno reglur á íslensku: hvernig á að velja tölur, útborganir, RTP og hvort það borgar sig að spila.",
    "🔢", ("#0a1a24", "#143340", "#1e4d5c"),
    f'''<p>Keno er lottó-líkur leikur sem á rætur að rekja til Kína fyrir yfir 2.000 árum. <strong>Þú velur tölur, vélin dregur tölur, og þú færð greitt eftir því hversu margar passa.</strong> Einfalt — en húsforskotið er hátt.</p>

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
<div class="info-box"><p><strong>Keno hefur eitt hæsta húsforskot í spilavítum:</strong> yfirleitt 20–35% hjá hefðbundnu keno og 5–12% hjá netútgáfum. Til samanburðar: <a href="{U}leidbeiningar/baccarat-reglur-a-islensku/">baccarat</a> 1,06%, <a href="{U}leidbeiningar/rullettureglur-a-islensku/">evrópsk rúlletta</a> 2,7%, <a href="{U}spilakassar/">spilakassar</a> um 4%.</p></div>
<p>Það þýðir að peningarnir þínir endast mun skemur í keno en í flestum öðrum leikjum. Spilaðu það fyrir skemmtunina, ekki sem fjárhagslega skynsamlegt val.</p>

<h2>Aðferðir — hvað virkar og hvað ekki</h2>
<h3>Virkar ekki</h3>
<ul>
<li><strong>„Heitar" og „kaldar" tölur</strong> — Hvert dráttur er óháður. Tala sem kom oft í gær er ekki líklegri í dag</li>
<li><strong>Mynstur á borðinu</strong> — Að velja tölur í röð eða í formi gefur enga tölfræðilega yfirburði</li>
<li><strong>Veðmálakerfi</strong> — <a href="{U}leidbeiningar/martingale-adferd-rulletta/">Martingale</a> og sambærileg kerfi breyta ekki húsforskotinu</li>
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
<p>Á spilavítum með gilt leyfi, já — tölurnar eru dregnar með vottuðum <a href="{U}leidbeiningar/hvernig-rng-virkar/">slembitölugjafa</a>.</p>
<h3>Hvað er besti fjöldi talna?</h3>
<p>Stærðfræðilega skiptir það ekki máli fyrir vænt gildi. 4–6 tölur gefa oftast jafnasta upplifun milli vinningstíðni og stærðar.</p>''',
    "Spila keno →"))

P.append(page(
    "video-poker-reglur-a-islensku",
    "Video poker reglur á íslensku — besti leikurinn í spilavítinu? 2026",
    "Video poker reglur á íslensku: Jacks or Better, útborgunartöflur, RTP allt að 99,5% og grunnstrategy.",
    "🖥️", ("#0a1a1a", "#143333", "#1e4d4d"),
    f'''<p>Video poker er <strong>einn af fáum spilavítisleikjum þar sem kunnátta skiptir raunverulegu máli</strong> — og með réttri strategíu getur RTP farið yfir 99%. Það er betra en nánast allt annað í spilavítinu.</p>

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
<p>Video poker hefur betra RTP en nánast allir <a href="{U}spilakassar/">spilakassar</a> (um 96%), <a href="{U}leidbeiningar/rullettureglur-a-islensku/">rúlletta</a> (97,3%) og jafnvel flest <a href="{U}leidbeiningar/blackjack-adferdir/">blackjack</a> borð.</p>
<p>Gallinn: það krefst athygli og þekkingar á strategíu. Mörgum finnst það minna skemmtilegt en spilakassar þar sem maður ýtir bara á hnapp.</p>

<h2>Algengar spurningar</h2>
<h3>Er video poker betra en spilakassar?</h3>
<p>Stærðfræðilega — mun betra. 99,5% RTP á móti 96%. En það krefst þess að þú lærir strategíu og spilir rétta útgáfu.</p>
<h3>Hvernig athuga ég hvort borðið er 9/6?</h3>
<p>Skoðaðu útborgunartöfluna í leiknum. Full House á að borga 9 og Flush 6 fyrir eitt mynt. Ef þær tölur eru lægri er RTP lægra.</p>
<h3>Þarf ég að muna alla strategíuna?</h3>
<p>Nei — listinn hér að ofan nær yfir langflestar aðstæður. Fullkomin strategía bætir aðeins um 0,1–0,2% við.</p>''',
    "Spila video poker →"))

P.append(page(
    "spilaviti-vs-vedmalasidur",
    "Spilavíti vs íþróttaveðmál — hvort hentar þér betur? 2026",
    "Samanburður á netspilavítum og íþróttaveðmálum: húsforskot, kunnátta, sveifla og hvað hentar íslenskum spilurum.",
    "⚔️", ("#14140a", "#28281a", "#3c3c28"),
    f'''<p>Margir íslenskir spilarar velta fyrir sér hvort þeir eigi að spila á spilavíti eða veðja á íþróttir. <strong>Leikirnir eru gjörólíkir — og henta ólíkum týpum.</strong></p>

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
<p>Lægsta húsforskotið í spilavíti: <a href="{U}leidbeiningar/video-poker-reglur-a-islensku/">video poker</a> (0,5%), <a href="{U}leidbeiningar/blackjack-adferdir/">blackjack</a> (0,5%), <a href="{U}leidbeiningar/baccarat-reglur-a-islensku/">baccarat</a> (1,06%).</p>

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
<div class="info-box"><p><strong>Hvort tveggja:</strong> Mörg spilavíti bjóða bæði — <a href="{U}spilaviti/slotoro/">Slotoro</a>, <a href="{U}spilaviti/epicbet/">Epicbet</a>, <a href="{U}spilaviti/tonybet/">TonyBet</a> og <a href="{U}spilaviti/20bet/">20Bet</a>.</p></div>

<h2>Sameiginleg áhætta</h2>
<p>Bæði form geta orðið vandamál. Íþróttaveðmál eru stundum talin „öruggari" af því að kunnátta kemur við sögu — en sú tilfinning að vera „góður í þessu" getur gert það auðveldara að réttlæta stærri veðmál.</p>
<p>Sömu varnir gilda fyrir hvort tveggja: <a href="{U}leidbeiningar/hvernig-a-ad-setja-takmork-a-spilaviti/">innborgunartakmörk</a>, föst fjárhagsáætlun og meðvitund um <a href="{U}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">viðvörunarmerki</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Er hægt að vinna stöðugt á íþróttaveðmálum?</h3>
<p>Örfáir ná því — það krefst tölfræðilíkana, aðgangs að bestu líkunum og strangrar fjármálastjórnunar. Langflestir tapa til lengdar, rétt eins og í spilavíti.</p>
<h3>Hvort er hraðara að tapa peningum í?</h3>
<p>Spilavíti, vegna hraðans. Spilakassi getur klárað 600 snúninga á klukkustund. Íþróttaveðmál tekur klukkustundir að afgreiðast — sem gefur tíma til umhugsunar.</p>
<h3>Get ég notað velkomstbónus á bæði?</h3>
<p>Yfirleitt eru aðskildir bónusar fyrir spilavíti og íþróttir, með ólíkum <a href="{U}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrðum</a>. Lestu skilmálana — íþróttabónusar krefjast oft lágmarkslíkinda.</p>''',
    "Sjá spilavíti og veðmál →"))

P.append(page(
    "aldurstakmork-a-spilavitum-island",
    "Aldurstakmörk á spilavítum á Íslandi — 18 eða 21 ár? 2026",
    "Hver er lögleg aldur til að spila á netspilavíti frá Íslandi? Aldurstakmörk, KYC staðfesting og hvernig spilavíti athuga aldur.",
    "🔞", ("#1a0a0a", "#331414", "#4d1e1e"),
    f'''<p>Aldurstakmörk í fjárhættuspilum eru ekki samræmd á heimsvísu og geta verið ruglingsleg. <strong>Hér er staðan fyrir íslenska spilara.</strong></p>

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
<p><a href="{U}leidbeiningar/hvad-er-kyc-stadfesting/">Hvað er KYC staðfesting? →</a></p>

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
<p>Sjá: <a href="{U}leidbeiningar/radleggingar-til-adstandenda-spilafikla/">ráðleggingar til aðstandenda →</a></p>

<h2>Af hverju eru aldurstakmörk til?</h2>
<p>Rannsóknir benda til að því fyrr sem einstaklingur byrjar að spila fjárhættuspil, þeim mun meiri líkur séu á vandamálum síðar. Heili unglinga er enn í þroska hvað varðar áhættumat og hvatastjórnun, sem gerir þennan hóp viðkvæmari.</p>
<p>Þess vegna eru aldurstakmörk — ásamt <a href="{U}leidbeiningar/sjalfsutilokun-spilavita/">sjálfsútilokun</a> og <a href="{U}leidbeiningar/hvernig-a-ad-setja-takmork-a-spilaviti/">takmörkum</a> — kjarninn í regluverki um ábyrga spilun.</p>

<h2>Algengar spurningar</h2>
<h3>Get ég spilað 17 ára ef spilavítið er erlent?</h3>
<p>Nei. Aldurstakmarkið er sett af spilavítinu og leyfisveitanda þess, ekki af staðsetningu þinni. Allar leyfðar síður krefjast 18 ára aldurs hið minnsta.</p>
<h3>Þarf ég að senda skilríki strax?</h3>
<p>Yfirleitt ekki við skráningu — en alltaf áður en fyrsta úttekt er afgreidd.</p>
<h3>Hvað ef ég nota reikning foreldris?</h3>
<p>Það brýtur skilmála spilavítisins. Reikningnum verður lokað og vinningar gerðir upptækir þegar KYC leiðir í ljós að notandi og reikningshafi eru ekki sá sami.</p>''',
    "Sjá ábyrga spilun →"))

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
