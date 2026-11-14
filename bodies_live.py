# -*- coding: utf-8 -*-
"""Original copy for /live/ pages. Each game gets its own angle: blackjack =
strategy, roulette = variants, baccarat = odds math, crazy time = bet breakdown."""

BODIES = {}

BODIES["live/blackjack"] = """
<p>Blackjack er eini borðleikurinn þar sem ákvarðanir þínar breyta ávöxtuninni verulega. Spilað með grunnstrategíu heldur húsið aðeins um 0,5% forskoti — spilað eftir tilfinningu hækkar það í 2% eða meira. Munurinn er ekki heppni heldur tafla sem hægt er að læra á kvöldstund.</p>

<h2>Reglurnar á mínútu</h2>
<p>Þú og spilastjórinn fáið tvö spil. Nær þinni hendi 21 en hans — án þess að fara yfir — vinnurðu. Mannspil telja tíu, ás telur eitt eða ellefu. „Blackjack" er ás og tía í fyrstu tveimur spilunum og borgar 3:2 á almennilegum borðum. Spilastjórinn fylgir fastri reglu, oftast að taka spil upp að 17 — hann tekur engar ákvarðanir, sem þýðir að öll spilamennskan liggur hjá þér.</p>

<h2>Grunnstrategían sem lækkar forskot hússins</h2>
<table>
<tr><th>Hendin þín</th><th>Spilastjóri sýnir 2–6</th><th>Spilastjóri sýnir 7–ás</th></tr>
<tr><td>8 eða minna</td><td>Taka spil</td><td>Taka spil</td></tr>
<tr><td>9–11</td><td>Tvöfalda þar sem má</td><td>Taka spil (tvöfalda 11)</td></tr>
<tr><td>12–16</td><td>Standa</td><td>Taka spil</td></tr>
<tr><td>17+</td><td>Standa</td><td>Standa</td></tr>
<tr><td>Par af ásum eða áttum</td><td>Skipta alltaf</td><td>Skipta alltaf</td></tr>
</table>
<p>Taflan er einföldun sem nær langstærstum hluta ávinningsins. Rökfræðin á bak við hana: sýni spilastjórinn 2–6 er hendin hans veik og líkleg til að springa — þá tekur þú enga áhættu sjálfur. Sýni hann 7 eða hærra verður þú að sækja.</p>

<h2>Borðin í beinni: hvað skiptir máli við valið</h2>
<ul>
<li><strong>Útborgun á blackjack:</strong> 3:2 er standard. Borð sem borga 6:5 þrefalda forskot hússins — forðastu þau.</li>
<li><strong>Fjöldi stokka:</strong> átta stokkar í skónum er venjan í beinni; færri stokkar bæta stöðu þína örlítið.</li>
<li><strong>Hliðarveðmál:</strong> Perfect Pairs og 21+3 bera 4–8% húsforskot. Þau eru skemmtun, ekki strategía.</li>
<li><strong>„Infinite" borð:</strong> óendanlega mörg sæti af því allir spila sömu hendi — gott fyrir byrjendur því lágmarkið er lægra.</li>
</ul>

<h2>Tryggingin — stysta lexía síðunnar</h2>
<p>Þegar spilastjórinn sýnir ás býðst „insurance". Stærðfræðin er einföld: veðmálið tapar til lengdar nema þú teljir spil, sem streymisborð með sífelldri stokkun gera ómögulegt. Svarið er alltaf nei.</p>

<h2>Hvar er gott að spila blackjack í beinni</h2>
<p><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> er með breitt úrval Evolution-borða frá €1 lágmarki. <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> býður bæði klassísk og Infinite-borð. Yfirlit yfir alla borðleiki er í <a href="{URL_BASE}spilaviti/live-spilaviti/">live-umfjölluninni</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Má nota strategíutöflu á meðan ég spila?</h3>
<p>Já. Taflan er opinber stærðfræði, ekki svindl, og enginn skilmáli bannar hana. Hafðu hana á öðrum skjá fyrstu kvöldin — hún verður ósjálfráð fyrr en þú heldur.</p>
<h3>Virkar spilatalning í beinni?</h3>
<p>Nei. Borðin í beinni stokka ýmist eftir hverja hendi eða skipta um skó löngu áður en talning verður nothæf. Grunnstrategían er raunhæfa hámarkið — og hún dugar til að gera blackjack að hagstæðasta borðleiknum.</p>
<h3>Hvað þýðir það þegar borðið „stendur á mjúkri 17"?</h3>
<p>Mjúk 17 er ás plús sex. Borð þar sem spilastjórinn stendur á mjúkri 17 (S17) er örlítið hagstæðara þér en borð þar sem hann tekur spil (H17) — muninn sérðu í borðreglunum neðst í leikglugganum.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Setjast við borðið →</a></div>
"""

BODIES["live/roulette"] = """
<p>Rúlettan er einfaldasti borðleikurinn að læra og sá sem flestir misskilja: útgáfan sem þú velur ræður meiru um ávöxtun þína en nokkurt veðmálamynstur. Munurinn á evrópsku og amerísku hjóli er heilt prósentustig af hverju einasta veðmáli.</p>

<h2>Útgáfurnar þrjár — og hvers vegna valið skiptir öllu</h2>
<table>
<tr><th>Útgáfa</th><th>Reitir</th><th>Forskot hússins</th><th>Dómur</th></tr>
<tr><td>Frönsk (með la partage)</td><td>0–36</td><td>1,35% á jöfnu veðmálin</td><td>Besti kosturinn</td></tr>
<tr><td>Evrópsk</td><td>0–36</td><td>2,70%</td><td>Góð</td></tr>
<tr><td>Amerísk</td><td>0, 00, 1–36</td><td>5,26%</td><td>Slepptu henni</td></tr>
</table>
<p>Ameríska hjólið bætir við tvöföldu núlli án þess að hækka útborganir — húsforskotið tvöfaldast fyrir nákvæmlega ekkert í staðinn. Franska reglan „la partage" skilar þér helmingi jafnra veðmála til baka þegar kúlan lendir á núlli. Leitaðu að henni í borðlýsingunni.</p>

<h2>Veðmálin og raunlíkur þeirra</h2>
<p>Á evrópsku hjóli: stakt númer borgar 35:1 en líkurnar eru 1 af 37 — þar liggur húsforskotið. Rautt/svart, slétt/oddatala og hátt/lágt borga 1:1 með 18 vinningsreiti af 37. Tylftir og dálkar borga 2:1. Öll veðmál á sama hjóli bera sama húsforskot; munurinn er aðeins sveiflan. Stök númer gefa sjaldgæfa stóra vinninga, jöfnu veðmálin tíða smáa.</p>

<h2>Um „kerfi" — það sem tölfræðin segir</h2>
<p>Martingale (tvöfaldaðu eftir tap) og skyld kerfi breyta ekki húsforskotinu, þau umraða því aðeins: mörg lítil vinningskvöld gegn einstaka kvöldi sem þurrkar þau öll út. Tíu töp í röð á rauðu/svörtu koma fyrir — og ellefta tvöföldunin rekst á hámark borðsins. Spilaðu rúlettu sem skemmtun með fyrirfram ákveðinni upphæð, ekki sem tekjuáætlun. <a href="{URL_BASE}abyrg-spilun/">Ábyrg spilun</a> er ekki formsatriði í þessum leik.</p>

<h2>Í beinni: hraðinn og sérútgáfurnar</h2>
<p>Hefðbundið borð í beinni spinnur á ~40 sekúndna fresti; Auto- og Speed-útgáfur ná spinnum undir 25 sekúndum. Lightning Roulette frá Evolution dregur 1–5 „elding­arnúmer" með margfaldara upp í 500× — á móti lækkar útborgun á önnur stök númer úr 35:1 í 29:1. Skemmtilegri sveifla, aðeins lakari grunnávöxtun: vitaðu hvað þú ert að kaupa.</p>

<h2>Hvar á að spinna</h2>
<p>Evrópsk og frönsk borð finnurðu hjá <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> og <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> frá €0,50 lágmarki. Fleiri borðleikir í beinni eru teknir fyrir í <a href="{URL_BASE}spilaviti/live-spilaviti/">live-yfirlitinu</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Er hjólið í beinni örugglega tilviljanakennt?</h3>
<p>Það er vélrænt hjól undir myndavélum og eftirliti leyfisveitanda — engin tölvuslembitala. Frávik í hjóli sem þúsundir fylgjast með í beinni kæmi fram í tölfræðinni samstundis.</p>
<h3>Hvaða veðmál hentar byrjanda?</h3>
<p>Jöfnu veðmálin á frönsku eða evrópsku borði: lægsta sveiflan, einfaldasta ákvörðunin og á frönsku borði lægsta húsforskotið sem rúlettan býður.</p>
<h3>Skila „heit númer" einhverju?</h3>
<p>Nei. Hjólið man ekki fyrri spinn — númer sem kom þrisvar síðasta klukkutímann hefur nákvæmlega sömu líkur í næsta spinni og hin 36. Tölfræðiborðarnir í leikglugganum eru skraut, ekki upplýsingar.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Velja borð →</a></div>
"""

BODIES["live/baccarat"] = """
<p>Baccarat lítur út fyrir að vera flókinn hástéttaleikur — í raun er hann sá borðleikur sem krefst fæstra ákvarðana. Þú velur eitt af þremur veðmálum, afgangurinn gerist sjálfkrafa eftir föstum reglum. Einmitt þess vegna er hægt að segja nákvæmlega hvaða veðmál borgar sig.</p>

<h2>Gangurinn í leiknum</h2>
<p>Tvær hendur eru gefnar, „Player" og „Banker" — nöfnin eru hefð, hvorug er þín. Markmiðið: nær 9. Spil 2–9 halda gildi sínu, tíur og mannspil telja núll, ás telur einn; fari summa yfir 9 gildir aðeins seinni tölustafurinn (7+8=15 → 5). Þriðja spilið fylgir fastri töflu sem spilastjórinn framkvæmir — þú þarft aldrei að kunna hana.</p>

<h2>Veðmálin þrjú, reiknuð til enda</h2>
<table>
<tr><th>Veðmál</th><th>Útborgun</th><th>Forskot hússins (8 stokkar)</th></tr>
<tr><td>Banker</td><td>1:1 mínus 5% þóknun</td><td>1,06%</td></tr>
<tr><td>Player</td><td>1:1</td><td>1,24%</td></tr>
<tr><td>Jafntefli (Tie)</td><td>8:1</td><td>~14,4%</td></tr>
</table>
<p>Niðurstaðan úr töflunni er öll strategía leiksins: <strong>Banker er stærðfræðilega besta veðmálið</strong>, þrátt fyrir þóknunina — dráttarreglurnar gefa þeirri hendi örlítið betri vinningslíkur. Player er nánast jafngott. Jafnteflið er með margfalt verri ávöxtun og á ekkert erindi í veðmálaplan, sama hve freistandi 8:1 lítur út.</p>

<h2>„No commission" borðin — lestu smáa letrið</h2>
<p>Sum borð auglýsa Banker án 5% þóknunar. Á móti borgar Banker-vinningur með sexu aðeins helming (1:2 eða „push" eftir útgáfu). Nettóáhrifin: húsforskotið á Banker hækkar úr 1,06% í um 1,46%. Þóknunarlausa borðið er sem sagt verra, umbúðirnar bara snyrtilegri.</p>

<h2>Af hverju leikurinn hentar ákveðinni tegund spilara</h2>
<p>Baccarat er fyrir þann sem vill lágt húsforskot án þess að leggja strategíutöflur á minnið eins og í <a href="{URL_BASE}live/blackjack/">blackjack</a>. Hendurnar eru hraðar — undir mínútu í Speed-útgáfum — og sveiflan á Banker/Player er sú lægsta við borðin. Á móti kemur að leikurinn býður enga leið til að hafa áhrif; þeim sem leiðist það finnst baccarat tómlegur.</p>

<h2>Borðin sem við mælum með</h2>
<p>Evolution rekur baccarat-myndver með borðum frá €1 upp í hávaðaupphæðir hjá <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> og <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a>. Samanburður á live-framboði síðanna er í <a href="{URL_BASE}spilaviti/live-spilaviti/">yfirlitinu</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Á ég að fylgja „mynstrunum" á skjánum?</h3>
<p>Skorkortin (Big Road og félagar) sýna liðnar hendur. Skórinn man þær ekki — hver hönd er óháð þeirri síðustu, og „mynstur" í tilviljanakenndum röðum eru sjónhverfing. Þau eru hluti af stemningunni, ekki upplýsingar.</p>
<h3>Hvað eru Player Pair og Banker Pair veðmálin?</h3>
<p>Hliðarveðmál um að fyrstu tvö spil handar myndi par; borga 11:1 með yfir 10% húsforskoti. Sama saga og jafnteflið — skemmtun á yfirverði.</p>
<h3>Hvers vegna draga sumir leikmenn spilin sjálfir í „Squeeze" útgáfum?</h3>
<p>Baccarat Squeeze lætur spilastjórann (eða þig, í Control Squeeze) fletta spilunum hægt í hornið — hrein sviðsetning sem breytir engu um líkur, en gerir hverja hönd að atriði. Vinsælast við stærri veðmál.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Prófa baccarat →</a></div>
"""

BODIES["live/crazy-time"] = """
<p>Crazy Time er ekki borðleikur heldur sjónvarpsþáttur sem tekur við veðmálum: risastórt lukkuhjól, kynnir í beinni og fjórir bónusleikir með margfaldara sem hafa farið yfir 10.000×. Leikurinn er stærsta smíð Evolution og vinsælasti „game show" titill netspilavíta.</p>

<h2>Hjólið og reitirnir</h2>
<p>Hjólið hefur 54 reiti: talnareitirnir 1, 2, 5 og 10 og fjórir bónusreitir — Coin Flip, Cash Hunt, Pachinko og Crazy Time. Þú veðjar á hvar hjólið stoppar; lendi það á bónusreit sem þú veðjaðir á ferðu inn í bónusleikinn.</p>
<table>
<tr><th>Reitur</th><th>Fjöldi á hjóli</th><th>Grunnútborgun</th><th>RTP</th></tr>
<tr><td>1</td><td>21</td><td>1:1</td><td>96,08%</td></tr>
<tr><td>2</td><td>13</td><td>2:1</td><td>95,95%</td></tr>
<tr><td>5</td><td>7</td><td>5:1</td><td>95,78%</td></tr>
<tr><td>10</td><td>4</td><td>10:1</td><td>95,73%</td></tr>
<tr><td>Coin Flip</td><td>4</td><td>Margfaldari</td><td>95,70%</td></tr>
<tr><td>Cash Hunt</td><td>2</td><td>Margfaldari</td><td>95,27%</td></tr>
<tr><td>Pachinko</td><td>2</td><td>Margfaldari</td><td>94,33%</td></tr>
<tr><td>Crazy Time</td><td>1</td><td>Margfaldari</td><td>94,41%</td></tr>
</table>
<p>Takið eftir mynstri sem gildir um allan leikinn: því meira aðdráttarafl, því lægri ávöxtun. Veðmálið á töluna 1 heldur mestu til baka; glamúrreitirnir Pachinko og Crazy Time minnstu.</p>

<h2>Top Slot — margfaldarinn fyrir hvern snúning</h2>
<p>Fyrir hvern snúning dregur „Top Slot" einn reit og einn margfaldara (allt að 50×). Smelli hvort tveggja saman margfaldast útborgun reitsins — þannig verður 10-reiturinn skyndilega 500:1. Þetta er vélin á bak við stóru tölurnar í auglýsingunum, og ástæðan fyrir því að RTP-bilið er svona breitt.</p>

<h2>Bónusleikirnir fjórir í einni línu hver</h2>
<p><strong>Coin Flip:</strong> rauð eða blá hlið, margfaldari á hvorri — einfaldasti og tíðasti bónusinn. <strong>Cash Hunt:</strong> 108 skotmörk á skjá, þú velur eitt; allir fá eitthvað, enginn veit hvað hinir fengu. <strong>Pachinko:</strong> kúla fellur gegnum pinnavegg, „Double" reitir geta tvöfaldað upp í 10.000× hámarkið. <strong>Crazy Time:</strong> sjaldgæfasti og stærsti — risahjól bak við rauðar dyr, þrír litir af flipp, margfaldarar sem byrja í tugum.</p>

<h2>Hvernig á að hugsa um veðmálaplanið</h2>
<p>Algengasta nálgunin er að dekka talnareitina (sveifluminna, tíðir smávinningar) eða alla bónusreitina (hver bónus hittir að meðaltali á ~9 snúninga fresti samanlagt). Hvorugt breytir ávöxtuninni — taflan að ofan gildir — en sveiflan er gjörólík. Spilaðu með upphæð sem má hverfa og settu tímamörk fyrirfram; þátturinn er hannaður til að halda þér, sjá <a href="{URL_BASE}abyrg-spilun/">ábyrga spilun</a>.</p>

<h2>Hvar er hægt að horfa og spila</h2>
<p>Crazy Time er hjá flestum síðum með Evolution-samning — þar á meðal <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> og <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> frá €0,10 lágmarksveðmáli. Aðrir þættir sömu gerðar (Monopoly Live, Funky Time) eru í <a href="{URL_BASE}live/">live-safninu</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Hvenær borgar sig að veðja á Crazy Time reitinn sjálfan?</h3>
<p>Aldrei út frá ávöxtun — reiturinn er einn af 54 og RTP hans er næstlægst í leiknum. Fólk veðjar á hann af því að bónusinn er viðburður; það er gild skemmtiástæða, ekki stærðfræðileg.</p>
<h3>Hvað þýðir „Rescue" þegar kúlan í Pachinko lendir neðst?</h3>
<p>Ekkert slíkt er til — lendi kúlan á „Double" tvöfaldast allir margfaldarar og kúlunni er sleppt aftur. Hámarkið í öllum bónusum er 10.000× veðmálið þitt; nái margfaldarar hærra er útborgunin þökuð við það.</p>
<h3>Get ég horft án þess að veðja?</h3>
<p>Já — borðið er opið áhorfendum og spjallið líka. Að horfa á tuttugu snúninga áður en þú leggur fyrsta veðmálið er reyndar ódýrasta kennslustundin sem leikurinn býður.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Opna Crazy Time →</a></div>
"""

BODIES["live/monopoly-live"] = """
<p>Monopoly Live tók borðspilið sem allir þekkja og breytti því í veðmálahjól með þrívíddarbónus: þegar hjólið stoppar á „2 ROLLS" eða „4 ROLLS" stígur sjálfur Hr. Monopoly fram og gengur um teiknað borð þar sem hver reitur ber vinning. Útkoman er einn vinsælasti live-leikur Evolution — og sá sem flestir spila vitlaust.</p>

<h2>Uppbygging hjólsins</h2>
<table>
<tr><th>Reitur</th><th>Fjöldi (af 54)</th><th>Útborgun</th></tr>
<tr><td>1</td><td>22</td><td>1:1</td></tr>
<tr><td>2</td><td>15</td><td>2:1</td></tr>
<tr><td>5</td><td>7</td><td>5:1</td></tr>
<tr><td>10</td><td>4</td><td>10:1</td></tr>
<tr><td>Chance</td><td>2</td><td>Peningagjöf eða margfaldari</td></tr>
<tr><td>2 Rolls</td><td>3</td><td>Bónusborðið</td></tr>
<tr><td>4 Rolls</td><td>1</td><td>Bónusborðið, tveir teningar auka</td></tr>
</table>
<p>RTP er hæst á 1-reitnum (96,23%) og lægst á tíunni (~96,0%) — óvenju jafnt fyrir leik af þessari gerð. Chance-spjaldið gefur ýmist beinharðan vinning eða margfaldara á næsta snúning.</p>

<h2>Bónusinn — og reglan sem byrjendur reka sig á</h2>
<p><strong>Þú ferð aðeins inn í bónusinn ef þú veðjaðir á Rolls-reitinn sem hjólið stoppaði á.</strong> Áhorfandinn sem „geymdi sér" bónusveðmálið horfir á aðra ganga um borðið. Í bónusnum kastar teningapar sér sjálfkrafa, Hr. Monopoly gengur reitina og safnar: húsum og hótelum fylgja margfaldarar sem leggjast ofan á, tvennur gefa aukaköst. Stóru tölurnar úr auglýsingum leiksins — hundruð- og þúsundfaldarar — gerast þegar hótel hafa hlaðist á borðið áður en göngunni lýkur.</p>

<h2>Hvernig reyndir spilarar leggja upp</h2>
<p>Algengasta uppleggið er að hafa alltaf eitthvað á báðum Rolls-reitunum — þeir eru 4 af 54 reitum samanlagt og án þeirra ertu aðeins að spila talnahjól. Talnaveðmálin virka þá sem „brú" sem heldur innistæðunni gangandi milli bónusa. Það breytir ekki ávöxtuninni (taflan ræður), en tryggir að stóra augnablik leiksins gerist með þig innanborðs.</p>

<h2>Hvar er spilað</h2>
<p>Monopoly Live er eitt borð á heimsvísu, rekið af Evolution allan sólarhringinn, og aðgengilegt m.a. hjá <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> og <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> frá €0,10. Skyldir þættir — <a href="{URL_BASE}live/crazy-time/">Crazy Time</a> og <a href="{URL_BASE}live/dream-catcher/">Dream Catcher</a> — nota sama hjólagrunn með öðrum bónusum.</p>

<h2>Algengar spurningar</h2>
<h3>Hvað gerir „Chance" nákvæmlega?</h3>
<p>Hr. Monopoly dregur spjald: ýmist beingreiðslu á öll virk veðmál eða margfaldara sem festist á næsta snúning hjólsins. Margfaldaraspjaldið er ástæða þess að stundum sérðu „10 × 8" borga 80:1 á venjulegum talnareit.</p>
<h3>Er bónusútkoman fyrirfram ákveðin?</h3>
<p>Teningarnir í bónusnum eru líkamlegir og kastað í vél fyrir framan myndavélina; borðuppsetningin (hús/hótel) er slembin fyrir hvern bónus. Eftirlit leyfisveitenda Evolution nær yfir hvort tveggja.</p>
<h3>Monopoly Live eða Crazy Time — hvor er „betri"?</h3>
<p>Ávöxtunarlega eru þeir áþekkir á talnareitunum. Crazy Time er sveiflumeiri með fjóra ólíka bónusa og hærri hámörk; Monopoly rólegri með einn bónus sem kemur oftar. Spurningin er hvora skemmtun þú kaupir — stærðfræðin sker ekki úr.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Setjast að borðinu →</a></div>
"""

BODIES["live/lightning-roulette"] = """
<p>Lightning Roulette er venjuleg evrópsk rúletta með einni breytingu sem umturnar upplifuninni: fyrir hvern snúning slær „elding" á 1–5 tilviljanakennd númer og hleður þau margfaldara frá 50× upp í 500×. Verðið fyrir þessa möguleika er falið annars staðar í útborgunartöflunni — og það er einmitt það sem þessi síða reiknar upp á borðið.</p>

<h2>Hvað breyttist frá venjulegu rúlettunni</h2>
<table>
<tr><th></th><th>Evrópsk rúletta</th><th>Lightning Roulette</th></tr>
<tr><td>Stakt númer, venjulegt</td><td>35:1</td><td><strong>29:1</strong></td></tr>
<tr><td>Stakt númer með eldingu</td><td>—</td><td>50× til 500×</td></tr>
<tr><td>Jöfn veðmál (rautt/svart o.fl.)</td><td>1:1</td><td>1:1 (óbreytt)</td></tr>
<tr><td>RTP á stökum númerum</td><td>97,30%</td><td>97,10%</td></tr>
<tr><td>RTP á jöfnum veðmálum</td><td>97,30%</td><td>97,30%</td></tr>
</table>
<p>Lesningin úr töflunni: <strong>eldingarnar eru fjármagnaðar með lækkun stakra númera úr 35:1 í 29:1.</strong> Jöfnu veðmálin eru ósnert — rautt/svart á þessu borði er nákvæmlega sama veðmál og á venjulegu evrópsku borði, bara með flottari sviðsmynd.</p>

<h2>Hvað þýðir það fyrir veðmálavalið?</h2>
<p>Tvær samkvæmar leiðir eru til að spila þetta borð. Sú fyrri: eingöngu jöfn veðmál — þá ertu í venjulegri rúlettu með ljósasýningu í kaupbæti. Sú seinni: stök númer, meðvitaður um að þú hefur skipt hluta af jöfnu ávöxtuninni fyrir sjaldgæfa 50–500× smelli; sveiflan er margföld á við venjulegt borð. Ósamkvæma leiðin er að spila stök númer og vænta 35:1-taktsins — útborganirnar 29:1 naga innistæðuna hraðar en tilfinningin segir.</p>

<h2>Hvernig eldingin velur</h2>
<p>Margfaldaranúmerin og stærðir þeirra eru dregin af slembikerfi fyrir hvern snúning, óháð veðmálum borðsins — kerfið sér ekki hvar spilararnir liggja. Hjólið sjálft er líkamlegt og kúlan alvöru; aðeins verðlaunalagið er stafrænt. Leikurinn vann „Game of the Year" EGR-verðlaunin 2018 og gat af sér heila fjölskyldu: Lightning Blackjack, Lightning Baccarat og XXXtreme-útgáfuna með margfaldara upp í 2.000×.</p>

<h2>Hvar og fyrir hve mikið</h2>
<p>Borðið er hjá öllum Evolution-síðum, þar á meðal <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> og <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a>, frá €0,20 á númer. Grunnreglur og útgáfusamanburður rúlettunnar eru í <a href="{URL_BASE}live/roulette/">rúlettu-umfjölluninni</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Fæ ég margfaldarann á split- eða corner-veðmál?</h3>
<p>Nei — eldingarmargfaldarinn greiðist aðeins á bein (straight-up) veðmál á númerið. Split, corner og línur borga sínar venjulegu, lækkuðu tölur. Þetta stendur í borðreglunum en kemur mörgum á óvart við fyrsta stóra smell.</p>
<h3>Koma 500× eldingarnar í alvöru?</h3>
<p>Já, en sjaldan — stærstu margfaldararnir eru settir á fá númer og flestar eldingar eru 50–100×. Að veðja á öll fimm eldingarnúmerin eftir á er ekki hægt: eldingin slær eftir að veðmálaglugginn lokast.</p>
<h3>Er XXXtreme-útgáfan betri því hámarkið er hærra?</h3>
<p>Hún gengur lengra í sömu skiptum: enn fleiri eldingar og allt að 2.000×, gegn því að venjuleg stök númer lækka í 24:1 og RTP niður fyrir venjulegu útgáfuna. Meiri rússíbani, lakari grunnur — valið er smekksatriði, ekki stærðfræði.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Prófa eldingarnar →</a></div>
"""

BODIES["live/dream-catcher"] = """
<p>Dream Catcher er einfaldasti live-leikur sem til er: eitt stórt hjól, sex mögulegar tölur, kynnir sem spinnur. Ekkert borð, engar hendur, engin strategía að læra. Þetta var fyrsti „game show" leikur Evolution (2017) og opnaði flokkinn sem <a href="{URL_BASE}live/crazy-time/">Crazy Time</a> fullkomnaði síðar — en einfaldleikinn heldur honum enn á dagskrá.</p>

<h2>Hjólið í tölum</h2>
<table>
<tr><th>Reitur</th><th>Fjöldi (af 54)</th><th>Útborgun</th><th>RTP</th></tr>
<tr><td>1</td><td>23</td><td>1:1</td><td>96,58%</td></tr>
<tr><td>2</td><td>15</td><td>2:1</td><td>95,96%</td></tr>
<tr><td>5</td><td>7</td><td>5:1</td><td>95,91%</td></tr>
<tr><td>10</td><td>4</td><td>10:1</td><td>96,15%</td></tr>
<tr><td>20</td><td>2</td><td>20:1</td><td>95,47%</td></tr>
<tr><td>40</td><td>1</td><td>40:1</td><td>94,87%</td></tr>
<tr><td>2× / 7× margfaldarar</td><td>2</td><td>Endurspinn með margfaldara</td><td>—</td></tr>
</table>

<h2>Margfaldarareitirnir — eina flækjan</h2>
<p>Stoppi hjólið á 2× eða 7× vinnst ekkert strax: öll veðmál standa, hjólið spinnur aftur og næsta niðurstaða margfaldast. Lendi margfaldari aftur, margfaldast margfaldararnir saman — 7× ofan á 7× ofan á 40 gefur 1.960:1, og það hefur gerst í beinni. Þetta er allur „galdur" leiksins: langur hali af litlum líkum á stórum tölum, hengdur á annars einfalt hjól.</p>

<h2>Fyrir hvern er þetta hjól?</h2>
<p>Dream Catcher er innganga í live-heiminn: engin spilareglubók, veðmálið er bara „á hvaða tölu stoppar hjólið". Hann hentar þeim sem finnst <a href="{URL_BASE}live/blackjack/">blackjack</a> krefjast of mikillar athygli og <a href="{URL_BASE}live/crazy-time/">Crazy Time</a> of hávaðasamur. Reyndari spilarar nota hann gjarnan sem léttmeti milli borða — og það er heiðarlegasta lýsingin á honum: popcorn-leikur með 95–96% skilum.</p>

<h2>Veðmálaupplegg án sjálfsblekkingar</h2>
<p>Töflulesturinn segir það sem segja þarf: 1-reiturinn ber hæstu ávöxtunina og lægstu sveifluna, 40-reiturinn öfugt. Að dekka margar tölur samtímis lækkar bara ávöxtunina í átt að vegnu meðaltali — hjólið er hannað þannig að engin samsetning „vinnur á" það. Veldu sveiflustigið sem skemmtir þér, settu <a href="{URL_BASE}abyrg-spilun/">mörk fyrirfram</a> og njóttu sýningarinnar.</p>

<h2>Hvar hjólið snýst</h2>
<p>Allar Evolution-síður bera Dream Catcher; hjá <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> og <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> er lágmarkið €0,10. Yfirlit allra þátta af þessari gerð er í <a href="{URL_BASE}live/">live-safninu</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Hver er munurinn á Dream Catcher og Money Wheel annarra framleiðanda?</h3>
<p>Grunnhugmyndin er sú sama (Big Six hjól úr spilavítum Vegas); útfærslur annarra framleiðenda hafa aðrar talnadreifingar og oft lakara RTP. Tölurnar á þessari síðu gilda um Evolution-útgáfuna sérstaklega.</p>
<h3>Telur leikurinn í bónusveltu?</h3>
<p>Game show leikir lenda misjafnlega í bónusskilmálum — sumar síður telja þá 100%, aðrar 10% eða núll eins og borðleiki. <a href="{URL_BASE}bonusar/vedskilyrdi/">Veðskilyrðaumfjöllunin</a> útskýrir hvar þetta stendur í skilmálunum.</p>
<h3>Hvers vegna sé ég stundum tvo kynna á vakt?</h3>
<p>Borðið gengur allan sólarhringinn og kynnarnir skiptast á um hálftíma-klukkutíma fresti — sami leikur, nýtt andlit. Spjallið flyst óbreytt á milli.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Snúa hjólinu →</a></div>
"""
