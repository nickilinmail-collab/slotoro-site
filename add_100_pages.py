#!/usr/bin/env python3
"""Generate content for 100 new SEO pages and insert into generate.py"""

AFF = "https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/"
B = "{URL_BASE}"
CTA = f'<div class="cta-box"><a href="{AFF}" target="_blank" rel="noopener" class="cta-btn">{{text}}</a></div>'

def cta(text="Byrja að spila →"):
    return CTA.replace("{text}", text)

def info(html):
    return f'<div class="info-box"><p>{html}</p></div>'

def casino_link(slug, name):
    return f'<a href="{B}spilaviti/{slug}/">{name}</a>'

def slot_link(slug, name):
    return f'<a href="{B}spilakassar/{slug}/">{name}</a>'

def guide_link(slug, name):
    return f'<a href="{B}leidbeiningar/{slug}/">{name}</a>'

def pay_link(slug, name):
    return f'<a href="{B}greidslur/{slug}/">{name}</a>'

# All 100 pages (minus ones already created)
pages = []

# ==========================================
# CATEGORY 3: "Hvernig" guides (#21-30)
# ==========================================

pages.append({
    "slug": "hvernig-a-ad-opna-reikning-a-spilaviti",
    "title": "Hvernig á að opna reikning á spilavíti — skref fyrir skref 2026",
    "desc": "Skref-fyrir-skref leiðbeiningar um hvernig á að stofna reikning á netspilavíti frá Íslandi. Skráning, staðfesting og fyrsta innborgun.",
    "emoji": "📝",
    "colors": ("#0d1926", "#1a324c", "#274b72"),
    "content": f'''<h1>Hvernig á að opna reikning á spilavíti 2026</h1>
{{hero}}
<p>Ef þú hefur aldrei skráð þig á netspilavíti áður getur ferlið virst flókið. <strong>Í raun tekur það 2-5 mínútur.</strong> Hér er nákvæm skref-fyrir-skref leiðbeining sem virkar á flestum spilavítum.</p>

<h2>Skref 1 — Veldu spilavíti</h2>
<p>Fyrst þarftu að velja hvert spilavíti þú vilt skrá þig á. Athugaðu:</p>
<ul>
<li>Er spilavítið með gilt leyfi? ({guide_link("hvernig-a-ad-stadfesta-spilavitaleyfi", "Hvernig á að staðfesta leyfi →")})</li>
<li>Tekur það við greiðslum frá Íslandi? ({guide_link("spilaviti-sem-tekur-vid-islenskum-kortum", "Greiðsluleiðir á Íslandi →")})</li>
<li>Er viðmótið á íslensku? ({guide_link("spilaviti-med-islensku-vidmoti", "Spilavíti á íslensku →")})</li>
</ul>
{info(f'<strong>Okkar tilmæli fyrir byrjendur:</strong> {casino_link("epicbet", "Epicbet")} — íslensku viðmót, veðlaus bónus, Apple Pay og PIQ greiðslur.')}

<h2>Skref 2 — Skráning</h2>
<p>Á flestum spilavítum þarftu að gefa upp:</p>
<ol>
<li><strong>Netfang</strong> — Notaðu raunverulegt netfang. Þú þarft það til að staðfesta reikninginn og endurstilla lykilorð</li>
<li><strong>Lykilorð</strong> — Veldu sterkt lykilorð (12+ stafir, blöndun af bókstöfum og tölum)</li>
<li><strong>Nafn og fæðingardagur</strong> — Verður að vera rétt — spilavítið ber saman við skilríki seinna</li>
<li><strong>Heimilisfang</strong> — Sumir biðja um þetta strax, aðrir seinna</li>
<li><strong>Gjaldmiðil</strong> — Veldu EUR (evrur) nema spilavítið styðji ISK (mjög sjaldgæft)</li>
</ol>
<p>Á {casino_link("stake", "Stake")} og {casino_link("bc-game", "BC.Game")} þarftu aðeins netfang og lykilorð — allt annað kemur seinna.</p>

<h2>Skref 3 — Staðfestu netfang</h2>
<p>Spilavítið sendir þér tölvupóst með tengli eða kóða. Smelltu á hann til að staðfesta. Athugaðu ruslpósthólfið ef þú sérð hann ekki.</p>

<h2>Skref 4 — Fyrsta innborgun</h2>
<p>Nú geturðu lagt inn peninga. Veldu greiðsluleið:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Besta leiðin á Íslandi. {guide_link("kaupa-bitcoin-island", "Hvernig á að kaupa Bitcoin →")}</li>
<li><strong>Visa/Mastercard</strong> — Virkar stundum. {guide_link("spilaviti-sem-tekur-vid-islenskum-kortum", "Sjá stöðu →")}</li>
<li><strong>PIQ</strong> — {guide_link("piq-greidslur-island", "Sérhannað fyrir Ísland →")}</li>
<li><strong>E-wallets</strong> — {pay_link("skrill-i-spilavitum", "Skrill")} eða {pay_link("neteller-i-spilavitum", "Neteller")}</li>
</ul>
<p>Lágmarksinnborgun er yfirleitt €10. {guide_link("hversu-mikid-kostar-ad-spila", "Hvað kostar að spila? →")}</p>

<h2>Skref 5 — Velkomstbónus</h2>
<p>Flest spilavíti bjóða velkomstbónus á fyrstu innborgun. <strong>Lestu skilmálana áður en þú samþykkir.</strong> Athugaðu {guide_link("hvad-eru-vedskilyrdi", "veðskilyrði")} — þau ráða hvort bónusinn er raunverulega þess virði.</p>
{info(f'<strong>Veðlausir bónusar:</strong> {casino_link("epicbet", "Epicbet")} og {casino_link("respin", "Respin")} bjóða 0x veðskilyrði — vinningar eru þínir strax.')}

<h2>Skref 6 — Byrjaðu að spila</h2>
<p>Tilbúinn! Mæli með að byrja í {guide_link("okeypis-spilaviti-island", "demo-ham")} til að kynnast leikjunum áður en þú veðjar raunverulegum peningum. Settu {guide_link("bankastjornunaradferdir", "takmörk")} á innborgunum strax.</p>

<h2>Algengar spurningar</h2>
<h3>Hversu langan tíma tekur skráning?</h3>
<p>2-5 mínútur á flestum spilavítum. Hraðskráning (aðeins netfang + lykilorð) tekur 30 sekúndur.</p>
<h3>Þarf ég að senda inn skilríki strax?</h3>
<p>Yfirleitt ekki — KYC staðfesting kemur þegar þú tekur út í fyrsta skipti. Sum spilavíti biðja um gögn fyrr ef innborgun fer yfir ákveðið þak.</p>
<h3>Get ég haft reikninga á mörgum spilavítum?</h3>
<p>Já — en aðeins einn reikning á hverju spilavíti. Margir spilarar hafa reikninga á 2-3 spilavítum til að nýta mismunandi bónusa.</p>
<h3>Er öruggt að gefa spilavíti persónuupplýsingar?</h3>
<p>Á spilavíti með gilt leyfi — já. Þau eru skylt að vernda gögnin þín samkvæmt lögum. Athugaðu alltaf leyfið fyrst.</p>
{cta("Opna reikning →")}'''
})

pages.append({
    "slug": "hvernig-a-ad-taka-ut-vinninga",
    "title": "Hvernig á að taka út af spilavíti á Íslandi — úttektarleiðarvísir 2026",
    "desc": "Allt sem þú þarft að vita um úttektir: aðferðir, hraði, KYC staðfesting og hvernig á að forðast vandamál.",
    "emoji": "💸",
    "colors": ("#1a0a0a", "#331414", "#4d1e1e"),
    "content": f'''<h1>Hvernig á að taka út af spilavíti á Íslandi 2026</h1>
{{hero}}
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
<p>Spilavíti þarf yfirleitt 24-48 klst til að samþykkja úttekt. Ef það tekur lengur en 72 klst skaltu hafa samband við þjónustuver. Sum spilavíti eru hraðari — {casino_link("bitstarz", "BitStarz")} afgreiðir flestar úttektir á undir 10 mínútum.</p>

<h3>„Bankinn minn hafnaði úttektinni"</h3>
<p>Íslenskir bankar geta hafnað millifærslum frá spilavítum. Lausn: notaðu dulritunargjaldmiðla eða e-wallet þar sem bankinn sér ekki uppruna fjármuna.</p>

<h3>„Mér var neitað um úttekt"</h3>
<p>Algengustu ástæður: 1) KYC ekki lokið, 2) veðskilyrði bónuss ekki uppfyllt, 3) hámarksúttekt á dag náð, 4) annað greiðsluheimilisfang en notað var við innborgun.</p>

<h2>Hraðastu spilavítin í úttektum</h2>
{info(f'<strong>{casino_link("bitstarz", "BitStarz")}</strong> — Flestar BTC úttektir afgreiddar á undir 10 mínútum')}
{info(f'<strong>{casino_link("stake", "Stake")}</strong> — Dulritunarúttektir á 0-2 klst')}
{info(f'<strong>{casino_link("epicbet", "Epicbet")}</strong> — PIQ úttektir á 1-24 klst')}

<h2>Algengar spurningar</h2>
<h3>Hversu mikið get ég tekið út í einu?</h3>
<p>Fer eftir spilavíti. Dæmi: €5.000 á dag, €10.000 á viku, €30.000 á mánuði. Dulritunarspilavíti hafa oft hærri mörk.</p>
<h3>Þarf ég að borga skatt af vinningum?</h3>
<p>Á Íslandi eru spilavinningar yfirleitt ekki skattskyldir. {guide_link("skattar-spilavinningar-island", "Sjá skattaleiðbeiningar →")}</p>
<h3>Get ég tekið út í ISK?</h3>
<p>Flest spilavíti borga í EUR. Bankinn þinn breytir sjálfkrafa í ISK. Til að spara gjaldmiðlaskiptagjöld getur þú notað Revolut eða dulritunargjaldmiðla.</p>
{cta("Finna spilavíti með hröðum úttektum →")}'''
})

# CATEGORY 4: Legal (#31-32)
pages.append({
    "slug": "er-ologligt-ad-spila-a-spilaviti-island",
    "title": "Er ólöglegt að spila á spilavíti á Íslandi? Lagaleg staða 2026",
    "desc": "Er ólöglegt fyrir íslendinga að spila á netspilavítum? Lög, reglur og hvað segja bankarnir. Uppfært 2026.",
    "emoji": "⚖️",
    "colors": ("#1a1a0a", "#33331a", "#4d4d28"),
    "content": f'''<h1>Er ólöglegt að spila á spilavíti á Íslandi? 2026</h1>
{{hero}}
<p>Þetta er algengasta spurningin sem íslenskir spilarar spyrja — og svarið er <strong>flóknara en einfalt já eða nei</strong>.</p>

<h2>Stutt svar</h2>
{info('<strong>Nei — það er ekki ólöglegt fyrir einstaklinga að spila á erlendum netspilavítum frá Íslandi.</strong> Engin lög banna íslenskum ríkisborgurum að spila. Hins vegar er rekstur spilavíta á Íslandi bannaður.')}

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
<p>Þó að lög banni ekki spilurum að spila hafa <a href="{B}leidbeiningar/islenskir-bankar-spilaviti/">íslenskir bankar</a> tekið eigin ákvarðanir:</p>
<ul>
<li>Arion banki, Landsbankinn og Íslandsbanki geta hafnað kortagreiðslum til spilavíta</li>
<li>Þetta er <strong>innri stefna bankanna</strong> — ekki lagaskylda</li>
<li>Dulritunargjaldmiðlar og rafræn veski fara framhjá þessu</li>
</ul>
<p>{guide_link("spilaviti-sem-tekur-vid-islenskum-kortum", "Hvaða spilavíti tekur við íslenskum kortum? →")}</p>

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
<p>Já — kaup og notkun dulritunargjaldmiðla er fullkomlega löglegt á Íslandi. {guide_link("kaupa-bitcoin-island", "Hvernig á að kaupa Bitcoin →")}</p>
<h3>Breytist staðan ef Ísland fær leyfiskerfi?</h3>
<p>Ef Ísland innleiðir leyfiskerfi (líkt og Danmörk) munu sum spilavíti sækja um leyfi og verða "opinberlega" löguð. Spilavíti án íslensks leyfis gætu þá verið lokað á — en þetta er enn aðeins umræða.</p>
{cta("Finna leyfileg spilavíti →")}'''
})

# CATEGORY 5: Payments (#41-42)
pages.append({
    "slug": "revolut-spilaviti-island-leidbeining",
    "title": "Revolut á spilavíti á Íslandi — ítarleg leiðbeining 2026",
    "desc": "Hvernig á að nota Revolut til innborgunar á netspilavíti frá Íslandi. Skref-fyrir-skref og hvort bankinn sér viðskiptin.",
    "emoji": "🟣",
    "colors": ("#1a0a28", "#2d1445", "#401e62"),
    "content": f'''<h1>Revolut á spilavíti á Íslandi 2026</h1>
{{hero}}
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
{info(f'<strong>{casino_link("epicbet", "Epicbet")}</strong> — Visa/Mastercard (Revolut virkar). Einnig Apple Pay.')}
{info(f'<strong>{casino_link("slotoro", "Slotoro")}</strong> — Visa/Mastercard studdir.')}
{info(f'<strong>{casino_link("tonybet", "TonyBet")}</strong> — Visa/Mastercard. Evrópulegt leyfi.')}
{info(f'<strong>{casino_link("20bet", "20Bet")}</strong> — Tekur við öllum kortum.')}
<p>Í raun styðja öll spilavíti sem taka við Visa/Mastercard einnig Revolut-kort.</p>

<h2>Algengar spurningar</h2>
<h3>Er Revolut ókeypis?</h3>
<p>Já — grunnáskriftin er ókeypis. Sýndarkort er frítt. Líkamlegt kort kostar einu sinni (um €5). Gjaldmiðlaskipti eru frítt upp að ákveðnu mánaðarlegu þaki.</p>
<h3>Hversu hratt er innborgun með Revolut?</h3>
<p>Samstundis — eins og venjulegt debetkort. Eina töfin er millifærsla frá íslenska bankanum á Revolut (venjulega nokkrar klukkustundir til 1 dagur).</p>
<h3>Get ég tekið út á Revolut?</h3>
<p>Já — ef þú lagðir inn með Revolut-korti geturðu venjulega tekið út á sama kort. Sumir spilarar velja þó að taka út í dulritunargjaldmiðlum og skipta síðan í EUR á Revolut.</p>
{cta("Finna spilavíti →")}'''
})

# CATEGORY 9: Comparisons (#81, #84)
pages.append({
    "slug": "bestu-crypto-spilavitin-island",
    "title": "Bestu crypto spilavítin á Íslandi 2026 — Bitcoin, Ethereum og USDT",
    "desc": "Topp 10 dulritunarspilavíti sem taka við íslenskum spilurum. Bitcoin, USDT, Ethereum. Hraðar úttektir, engir bankar.",
    "emoji": "₿",
    "colors": ("#1a0f00", "#332200", "#4d3300"),
    "content": f'''<h1>Bestu crypto spilavítin á Íslandi 2026</h1>
{{hero}}
<p>Dulritunargjaldmiðlar eru orðnir <strong>vinsælasta greiðsluleiðin</strong> hjá íslenskum spilavítaspilurum — og af góðum ástæðum. Bankarnir geta ekki lokað á greiðslur, úttektir eru hraðar og gjöldin lág.</p>

<h2>Topp 10 dulritunarspilavíti á Íslandi</h2>
<table class="info-table"><thead><tr><th>#</th><th>Spilavíti</th><th>Bónus</th><th>Dulritun</th><th>Úttektarhraði</th><th>Einkunn</th></tr></thead><tbody>
<tr><td>1</td><td>{casino_link("bitstarz", "BitStarz")}</td><td>5 BTC + 200 FS</td><td>BTC, ETH, LTC, DOGE, BCH</td><td>Undir 10 mín</td><td>9.8/10</td></tr>
<tr><td>2</td><td>{casino_link("stake", "Stake")}</td><td>200% + VIP</td><td>BTC, ETH, LTC, DOGE, XRP, TRX, USDT, USDC</td><td>0-2 klst</td><td>9.6/10</td></tr>
<tr><td>3</td><td>{casino_link("bc-game", "BC.Game")}</td><td>300% allt að 1 BTC</td><td>100+ gjaldmiðlar</td><td>0-1 klst</td><td>9.4/10</td></tr>
<tr><td>4</td><td>{casino_link("cloudbet", "Cloudbet")}</td><td>100% allt að 5 BTC</td><td>BTC, ETH, USDT, BCH, DOGE, LTC</td><td>0-24 klst</td><td>8.4/10</td></tr>
<tr><td>5</td><td>{casino_link("katsubet", "KatsuBet")}</td><td>100% + 100 FS</td><td>BTC, ETH, LTC, DOGE, USDT, BCH</td><td>0-24 klst</td><td>8.6/10</td></tr>
<tr><td>6</td><td>{casino_link("winz", "Winz.io")}</td><td>300 FS (engin veðskilyrði)</td><td>BTC, ETH, LTC, DOGE, USDT, TRX</td><td>0-24 klst</td><td>8.5/10</td></tr>
<tr><td>7</td><td>{casino_link("7bit", "7Bit Casino")}</td><td>200% + 100 FS</td><td>BTC, ETH, LTC, DOGE, BCH</td><td>0-24 klst</td><td>8.5/10</td></tr>
<tr><td>8</td><td>{casino_link("mbitcasino", "mBit Casino")}</td><td>175% + 300 FS</td><td>BTC, ETH, LTC, DOGE, USDT</td><td>0-24 klst</td><td>8.4/10</td></tr>
<tr><td>9</td><td>{casino_link("wildcoins", "WildCoins")}</td><td>250% + 100 FS</td><td>BTC, ETH, LTC, USDT</td><td>0-24 klst</td><td>8.7/10</td></tr>
<tr><td>10</td><td>{casino_link("hellspin", "HellSpin")}</td><td>150% + 50 FS</td><td>BTC, ETH, LTC, USDT</td><td>0-24 klst</td><td>8.1/10</td></tr>
</tbody></table>

<h2>Af hverju dulritunargjaldmiðlar á Íslandi?</h2>
<ul>
<li><strong>Engir bankar í leiðinni</strong> — {guide_link("islenskir-bankar-spilaviti", "Íslenskir bankar")} loka stundum á kortagreiðslur til spilavíta. Dulritunargreiðslur fara beint á blokkkeðjunni</li>
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
<p><strong>Okkar ráð:</strong> Notaðu USDT (TRC-20) fyrir innlagnir — hraðara, ódýrara og ekkert verðáhætta meðan þú spilar. {guide_link("kaupa-bitcoin-island", "Hvernig á að kaupa dulritunargjaldmiðla →")}</p>

<h2>Hvernig á að byrja?</h2>
<ol>
<li>Opnaðu reikning á kauphöll (Coinbase, Binance eða Kraken)</li>
<li>Keyptu BTC eða USDT</li>
<li>Skráðu þig á spilavíti af listanum hér að ofan</li>
<li>Leggðu inn — afritaðu wallet-heimilisfang spilavítisins og sendu</li>
<li>Byrjaðu að spila!</li>
</ol>
<p>{guide_link("kaupa-bitcoin-island", "Ítarleg leiðbeining um kaup á dulritunargjaldmiðlum →")}</p>

<h2>Algengar spurningar</h2>
<h3>Er löglegt að nota Bitcoin á spilavíti?</h3>
<p>Já — {guide_link("er-ologligt-ad-spila-a-spilaviti-island", "engin lög á Íslandi banna")} kaup á dulritunargjaldmiðlum eða notkun þeirra á spilavítum.</p>
<h3>Hvaða dulritunargjaldmiðill er bestur fyrir spilavíti?</h3>
<p>USDT (TRC-20) — stöðugt verð, lág gjöld, hraðar millifærslur. Bitcoin ef þú vilt halda BTC til langs tíma.</p>
<h3>Get ég keypt Bitcoin beint á spilavítinu?</h3>
<p>Sum spilavíti (t.d. {casino_link("stake", "Stake")}) bjóða innbyggð kaup á dulritunargjaldmiðlum. Hins vegar eru gjöldin yfirleitt hærri en á kauphöll.</p>
{cta("Spila með Bitcoin →")}'''
})

# CATEGORY 10: Responsible gambling (#91)
pages.append({
    "slug": "merki-thess-ad-thu-sert-ordinn-hadur-spilavitum",
    "title": "Merki þess að þú sért orðinn háður spilavítum — og hvað er hægt að gera",
    "desc": "10 algeng merki spilafiknar, hvernig á að fá hjálp og stuðningsúrræði á Íslandi. Hjálparsími 1717 er opinn 24/7.",
    "emoji": "🛡️",
    "colors": ("#1a1a1a", "#333333", "#4d4d4d"),
    "content": f'''<h1>Merki þess að þú sért orðinn háður spilavítum</h1>
{{hero}}
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
<li><strong>Sjálfsútilokun</strong> — Þú getur lokað á reikninginn þinn tímabundið eða varanlega. {guide_link("sjalfsutilokun-spilavita", "Hvernig sjálfsútilokun virkar →")}</li>
</ul>

<h3>Hjálp á Íslandi</h3>
{info('<strong>Hjálparsími 1717</strong> — Opinn allan sólarhringinn, alla daga. Ókeypis og trúnaðarmál. Hægt að hringja nafnlaust.')}
{info('<strong>SÁÁ</strong> — Samtök áfengis- og vímuvarnastarfs. Veita einnig stuðning við spilafikn. <em>saa.is</em>')}
{info('<strong>Ráðgjafar- og greiningarstöð — RGS</strong> — Sérfræðiþjónusta í Reykjavík.')}

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
{cta("Setja takmörk →")}'''
})

# CATEGORY 6: Game types (#51-55)
pages.append({
    "slug": "blackjack-reglur-a-islensku",
    "title": "Blackjack reglur á íslensku — fullkominn leiðarvísir 2026",
    "desc": "Blackjack reglur útskýrðar á íslensku. Hvernig á að spila, kortavirði, split, double down og hvenær á að standa.",
    "emoji": "🃏",
    "colors": ("#0a1a0d", "#14331a", "#1e4d27"),
    "content": f'''<h1>Blackjack reglur á íslensku 2026</h1>
{{hero}}
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
<p>{guide_link("blackjack-adferdir", "Ítarleg blackjack strategy → ")}</p>

<h2>Sérstök atriði</h2>
<h3>Blackjack (náttúrulegur 21)</h3>
<p>Ef þú færð 21 á fyrstu tveimur kortunum (ás + 10/gosi/drottning/kóngur) er þetta „Blackjack" og þú vinnur 3:2 (eða 6:5 á sumum borðum). Þetta er besta hönd sem hægt er að fá.</p>

<h3>Bust</h3>
<p>Ef samtala kortanna fer yfir 21 hefurðu tapað strax — sama hvað díllerinn er með.</p>

<h2>Hvar á að spila blackjack á Íslandi</h2>
{info(f'<strong>{casino_link("tonybet", "TonyBet")}</strong> — Sterkur lifandi blackjack hluti frá Evolution')}
{info(f'<strong>{casino_link("slotoro", "Slotoro")}</strong> — RNG blackjack og lifandi borð')}
{info(f'<strong><a href="{B}live/blackjack/">Lifandi blackjack á Svipan</a></strong> — Sjá alla lifandi blackjack leiki')}

<h2>Algengar spurningar</h2>
<h3>Er hægt að vinna stöðugt í blackjack?</h3>
<p>Til lengri tíma hefur spilavítið forskot (0.5% með réttri strategy). En rétt strategy minnkar tapið verulega og gefur þér bestu mögulegu líkurnar.</p>
<h3>Er kortatelling ólögleg?</h3>
<p>Nei — kortatelling er ekki ólögleg. Hins vegar er hún ómöguleg á netspilavítum vegna þess að stokkurinn er stokkaður á ný í hverri umferð (RNG).</p>
<h3>Hvað er munurinn á RNG blackjack og lifandi blackjack?</h3>
<p>RNG blackjack notar tölvu sem dílara — hraðara, hægt að spila í demo. Lifandi blackjack streymir raunverulegum dílara í beinni — hægara en raunverulegri upplifun.</p>
{cta("Spila blackjack →")}'''
})

pages.append({
    "slug": "rullettureglur-a-islensku",
    "title": "Rúllettureglur á íslensku — hvernig á að spila rúllettu 2026",
    "desc": "Rúllettureglur á íslensku: veðmálaflötur, tegundir veðmála, líkur og strategy. Evrópsk vs amerísk rúlletta.",
    "emoji": "🎡",
    "colors": ("#1a0a00", "#331400", "#4d1e00"),
    "content": f'''<h1>Rúllettureglur á íslensku 2026</h1>
{{hero}}
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
{info(f'<strong><a href="{B}live/lightning-roulette/">Lightning Roulette</a></strong> — Vinsælasta lifandi rúllettan. Hægt að vinna allt að 500x')}
{info(f'<strong><a href="{B}live/roulette/">Lifandi rúlletta á Svipan</a></strong> — Allir lifandi rúllettuleikir')}
{info(f'<strong>{casino_link("tonybet", "TonyBet")}</strong> — Sterkur lifandi rúllettuhluti')}

<h2>Algengar spurningar</h2>
<h3>Er einhver leið til að tryggja vinning í rúllettu?</h3>
<p>Nei — rúlletta er 100% happadrættisleikur. Engin strategy getur sigrað húsforskotið til lengri tíma. Spilaðu til gamans, ekki sem tekjuleið.</p>
<h3>Hvað er Lightning Roulette?</h3>
<p>Lifandi rúlletta frá Evolution þar sem 1-5 tölur fá „lightning" margfaldara (50x-500x) í hverri umferð. Vinsælasta útgáfan á netinu.</p>
<h3>Er betra að veðja á lit eða tölu?</h3>
<p>Litaveðmál (rautt/svart) vinnur oftar (48.6%) en borgar einungis 1:1. Töluvéðmál (straight up) vinnur sjaldnar (2.7%) en borgar 35:1. Valið fer eftir áhættuvilja þínum.</p>
{cta("Spila rúllettu →")}'''
})

# CATEGORY 8: Providers (#71-72)
pages.append({
    "slug": "pragmatic-play-allir-leikir",
    "title": "Pragmatic Play — allir leikir, RTP og umsagnir 2026",
    "desc": "Allir Pragmatic Play spilakassar á Íslandi: Gates of Olympus, Sweet Bonanza, Big Bass og fleiri. RTP, sveifla og bestu spilavítin.",
    "emoji": "🎰",
    "colors": ("#0a0a1a", "#141433", "#1e1e4d"),
    "content": f'''<h1>Pragmatic Play — allir leikir og RTP 2026</h1>
{{hero}}
<p>Pragmatic Play er <strong>stærsti og vinsælasti leikjaframleiðandinn</strong> á netspilavítum á Íslandi. Ef þú hefur einhvern tíma spilað {slot_link("gates-of-olympus", "Gates of Olympus")}, {slot_link("sweet-bonanza", "Sweet Bonanza")} eða {slot_link("big-bass-bonanza", "Big Bass Bonanza")} — þú hefur spilað Pragmatic Play.</p>

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
<tr><td>1</td><td>{slot_link("gates-of-olympus", "Gates of Olympus")}</td><td>96.50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>2</td><td>{slot_link("sweet-bonanza", "Sweet Bonanza")}</td><td>96.48%</td><td>Meðal-há</td><td>21.175x</td></tr>
<tr><td>3</td><td>{slot_link("big-bass-bonanza", "Big Bass Bonanza")}</td><td>96.71%</td><td>Há</td><td>2.100x</td></tr>
<tr><td>4</td><td>{slot_link("starlight-princess", "Starlight Princess")}</td><td>96.50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>5</td><td>{slot_link("gates-of-olympus-1000", "Gates of Olympus 1000")}</td><td>96.50%</td><td>Mjög há</td><td>15.000x</td></tr>
<tr><td>6</td><td>{slot_link("sugar-rush", "Sugar Rush")}</td><td>96.50%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>7</td><td>{slot_link("wolf-gold", "Wolf Gold")}</td><td>96.01%</td><td>Meðal</td><td>Pottur</td></tr>
<tr><td>8</td><td>{slot_link("big-bass-splash", "Big Bass Splash")}</td><td>95.67%</td><td>Há</td><td>5.000x</td></tr>
<tr><td>9</td><td>{slot_link("sweet-bonanza-1000", "Sweet Bonanza 1000")}</td><td>96.48%</td><td>Mjög há</td><td>25.000x</td></tr>
<tr><td>10</td><td>{slot_link("fruit-party", "Fruit Party")}</td><td>96.47%</td><td>Há</td><td>5.000x</td></tr>
</tbody></table>
<p><a href="{B}spilakassar/">Sjá alla 98 spilakassaumsagnir →</a></p>

<h2>Drops & Wins — hvað er það?</h2>
<p>Drops & Wins er mánaðarlegt mótakerfi frá Pragmatic Play þar sem spilarar geta unnið viðbótarvinning ofan á venjulega spilun. Daglegir og vikulegir vinningssjóðir eru greiddir út af handahófi til spilara sem spila Pragmatic Play leiki á þátttökuspilavítum.</p>
<p>Spilavíti á Íslandi sem styðja Drops & Wins: {casino_link("epicbet", "Epicbet")}, {casino_link("respin", "Respin")}, {casino_link("slotoro", "Slotoro")}.</p>

<h2>Bestu spilavítin fyrir Pragmatic Play á Íslandi</h2>
{info(f'<strong>{casino_link("slotoro", "Slotoro")}</strong> — 8.000+ leikir, stórt Pragmatic Play safn og Drops & Wins')}
{info(f'<strong>{casino_link("epicbet", "Epicbet")}</strong> — Íslenskt viðmót, Pragmatic Play spilakassar og lifandi leikir')}
{info(f'<strong>{casino_link("bitstarz", "BitStarz")}</strong> — Allt Pragmatic Play safnið í boði')}

<h2>Algengar spurningar</h2>
<h3>Er Pragmatic Play öruggt?</h3>
<p>Já — Pragmatic Play hefur leyfi frá Malta Gaming Authority (MGA), UK Gambling Commission og fleiri. Leikirnir eru prófaðir af óháðum prófunarstofum.</p>
<h3>Hvaða Pragmatic Play leikur hefur hæsta RTP?</h3>
<p>{slot_link("big-bass-bonanza", "Big Bass Bonanza")} með 96.71% RTP. Athugaðu þó að sum spilavíti nota lægri RTP stillingar — athugaðu alltaf í leikjareglum.</p>
<h3>Er hægt að spila Pragmatic Play leiki ókeypis?</h3>
<p>Já — flestir Pragmatic Play spilakassar eru í boði í {guide_link("okeypis-spilaviti-island", "demo-ham")}. Engrar skráningar krafist.</p>
{cta("Spila Pragmatic Play →")}'''
})

# Write output
print(f"Generated {len(pages)} new page definitions")

# Now we need to insert these into generate.py
import re

with open("generate.py", "r", encoding="utf-8") as f:
    code = f.read()

# Build the insertion string
insert_parts = []
for p in pages:
    # Escape for Python string
    entry = "    {\n"
    entry += f'        "slug": "{p["slug"]}",\n'
    entry += f'        "title": "{p["title"]}",\n'
    entry += f'        "desc": "{p["desc"]}",\n'
    entry += f'        "emoji": "{p["emoji"]}",\n'
    entry += f'        "colors": {p["colors"]},\n'
    entry += f'        "content": f\'\'\'{p["content"]}\'\'\'\n'
    entry += "    }"
    insert_parts.append(entry)

# Find the last ] of seo_pages and insert before it
# We'll insert after the last },\n] pattern
insertion = ",\n" + ",\n".join(insert_parts) + ",\n"

# Find position - look for the closing ] after spilaviti-fyrir-farsima-island content
marker = '''<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="noopener" class="cta-btn">Spila á farsíma →</a></div>\'\'\'\n    },\n]'''

if marker in code:
    code = code.replace(marker, marker.rstrip("]") + "\n" + ",\n".join(insert_parts) + ",\n]")
    with open("generate.py", "w", encoding="utf-8") as f:
        f.write(code)
    print("✅ Inserted into generate.py")
else:
    print("❌ Marker not found - will try alternative approach")
    # Alternative: find the exact line
    lines = code.split("\n")
    for i, line in enumerate(lines):
        if line.strip() == "]" and i > 2700:
            # This should be the end of seo_pages
            indent = "    "
            new_entries = ""
            for p in pages:
                new_entries += f'{indent}{{\n'
                new_entries += f'{indent}    "slug": "{p["slug"]}",\n'
                new_entries += f'{indent}    "title": "{p["title"]}",\n'
                new_entries += f'{indent}    "desc": "{p["desc"]}",\n'
                new_entries += f'{indent}    "emoji": "{p["emoji"]}",\n'
                new_entries += f'{indent}    "colors": {p["colors"]},\n'
                new_entries += f'{indent}    "content": f\'\'\'{p["content"]}\'\'\'\n'
                new_entries += f'{indent}}},\n'
            lines[i] = new_entries + "]"
            code = "\n".join(lines)
            with open("generate.py", "w", encoding="utf-8") as f:
                f.write(code)
            print(f"✅ Inserted {len(pages)} pages at line {i}")
            break
