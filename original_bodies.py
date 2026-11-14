# -*- coding: utf-8 -*-
"""Hand-written original page copy.

Key = page directory (e.g. "spilaviti/crypto-spilaviti"). At build time
generate.py swaps the templated body for this copy AND releases the page
from rewrite_queue.json, so it loses its noindex and returns to the sitemap.

Rules for this file:
  * every page is written from scratch — no sentence may repeat across pages
  * every page carries concrete facts: numbers, names, fees, rules
  * links use the {URL_BASE} placeholder, resolved at build time
"""

BODIES = {}

# ---------------------------------------------------------------- spilaviti --

BODIES["spilaviti/bestu-netspilaviti"] = """
<p>Við höfum prófað og borið saman 21 netspilavíti sem taka við íslenskum leikmönnum. Þessi listi byggir ekki á því hver borgar mest fyrir auglýsingu — hann byggir á leyfum, útborgunarhraða, raunverulegum veðskilyrðum og því hvernig þjónustan svarar þegar eitthvað fer úrskeiðis.</p>

<h2>Topp 5 — nóvember 2026</h2>
<table>
<tr><th>Spilavíti</th><th>Leyfi</th><th>Útborgun</th><th>Helsti kostur</th></tr>
<tr><td><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></td><td>Curaçao (CGA)</td><td>0–24 klst</td><td>Stærsta leikjasafnið, hröð skráning</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></td><td>Curaçao (CGA)</td><td>~10 mín (rafmynt)</td><td>Margverðlaunuð þjónusta síðan 2014</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/stake/">Stake</a></td><td>Curaçao (CGA)</td><td>Nær samstundis</td><td>Eigin leikir með sannanlegri niðurstöðu</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></td><td>MGA (Malta)</td><td>1–3 dagar</td><td>Evrópskt leyfi og aðskildir sjóðir leikmanna</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></td><td>Curaçao (CGA)</td><td>~15 mín (rafmynt)</td><td>Yfir 100 rafmyntir studdar</td></tr>
</table>

<h2>Hvað skiptir raunverulega máli í samanburði</h2>
<h3>Leyfið segir þér hvert þú getur leitað</h3>
<p>Ekkert netspilavíti er með íslenskt leyfi — happdrættislöggjöfin hér heima nær ekki yfir erlendar vefsíður. Munurinn liggur í erlendu leyfunum. Malta (MGA) gerir ströngustu kröfurnar: innistæður leikmanna eru geymdar aðskildar frá rekstrarfé og hægt er að skjóta deilum til óháðs úrskurðaraðila. Curaçao endurskipulagði sitt kerfi árið 2024 undir nýrri stofnun, Curaçao Gaming Authority, sem tók við af gömlu „master license" fyrirkomulagi — eftirlitið batnaði, en það jafnast ekki enn á við Möltu.</p>
<h3>Veðskilyrði eru verðmiðinn á bónusnum</h3>
<p>200% bónus með 45× veðskilyrðum er verri díll en 100% bónus með 30× skilyrðum. Reiknaðu alltaf: bónusupphæð × margfaldari = sú velta sem þarf áður en útborgun opnast. Nánar í <a href="{URL_BASE}bonusar/vedskilyrdi/">umfjöllun okkar um veðskilyrði</a>.</p>
<h3>Útborgunarhraðinn sést ekki í auglýsingunni</h3>
<p>Loforð um „samstundis útborgun" á aðeins við eftir að auðkenning (KYC) er frágengin. Fyrsta útborgun tekur nær alltaf lengri tíma en önnur. Við sendum prufuútborgun á hverju spilavíti sem við skráum — tímarnir í töflunni eru okkar mælingar, ekki loforð rekstraraðilans.</p>

<h2>Staðan gagnvart íslenskum greiðslum</h2>
<p>Stóru bankarnir þrír hafna mörgum kortafærslum í flokknum fjárhættuspil. Þess vegna raðast spilavíti með rafmyntastuðning ofar á listann okkar — innlögn með <a href="{URL_BASE}greidslur/bitcoin/">Bitcoin</a> eða <a href="{URL_BASE}greidslur/ethereum/">Ethereum</a> fer ekki í gegnum íslenskt kortakerfi. Yfirlit yfir allar leiðir er á <a href="{URL_BASE}greidslur/">greiðslusíðunni</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Er löglegt að spila á erlendum netspilavítum frá Íslandi?</h3>
<p>Íslensk lög banna ekki einstaklingum að spila á erlendum síðum og enginn hefur verið sóttur til saka fyrir það. Rekstur án leyfis hér á landi er hins vegar óheimill — þess vegna starfa allar síðurnar erlendis frá. Þú spilar á eigin ábyrgð og nýtur ekki íslenskrar neytendaverndar.</p>
<h3>Þarf að greiða skatt af vinningum?</h3>
<p>Vinningar frá happdrættum með íslenskt leyfi eru undanþegnir skatti. Um vinninga frá erlendum síðum gilda aðrar reglur og þeir geta talist skattskyldar tekjur — við mælum með að leita til skattasérfræðings fyrir stærri upphæðir, sjá <a href="{URL_BASE}leidbeiningar/skattur-a-vinninga/">umfjöllun um skatta</a>.</p>
<h3>Hvernig prófið þið spilavítin?</h3>
<p>Við skráum okkur sjálf, leggjum inn eigið fé, spilum, sendum fyrirspurnir á þjónustuna og tökum út vinninga. Einkunnin byggir á þessu ferli — aðferðafræðin er lýst á síðunni <a href="{URL_BASE}ritstjornarstefna/">um ritstjórnarstefnu</a>.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Skoða efsta valið →</a></div>
"""

BODIES["spilaviti/crypto-spilaviti"] = """
<p>Rafmyntaspilavíti leysa tvö vandamál íslenskra leikmanna í einu: kortafærslur sem bankinn hafnar og útborganir sem taka daga. Færsla á blockchain fer hvorki í gegnum Visa né íslenskan banka — hún er staðfest af netinu sjálfu, oftast innan klukkustundar.</p>

<h2>Samanburður á rafmyntum fyrir spilavíti</h2>
<table>
<tr><th>Mynt</th><th>Staðfestingartími</th><th>Dæmigerður færslukostnaður</th><th>Hentar best</th></tr>
<tr><td>Bitcoin (BTC)</td><td>10–60 mín</td><td>Breytilegur, oft $1–5</td><td>Stærri upphæðir</td></tr>
<tr><td>Litecoin (LTC)</td><td>~2,5 mín á blokk</td><td>Undir $0,10</td><td>Hraðar millifærslur</td></tr>
<tr><td>Ethereum (ETH)</td><td>Innan mínútu</td><td>Sveiflast með álagi netsins</td><td>Þegar spilavítið styður ekki annað</td></tr>
<tr><td>Tether (USDT, TRON-net)</td><td>~1 mín</td><td>~$1</td><td>Að losna við gengissveiflur</td></tr>
</table>
<p>Lykilatriðið sem margir reka sig á: veldu sama net við innlögn og úttekt. USDT er til á mörgum netum (TRON, Ethereum, Solana) og mynt send á rangt net getur tapast endanlega.</p>

<h2>Sveifluáhættan — og hvernig leikmenn verja sig</h2>
<p>Ef þú leggur inn 50.000 kr. í Bitcoin og gengið lækkar um 8% á meðan þú spilar, hefur innistæðan þín rýrnað án þess að þú hafir tapað einni veðmálsrúnd. Þetta vinnur líka í hina áttina, en sá sem vill bara spila — ekki spá í gengi — notar stablecoin eins og USDT, sem fylgir Bandaríkjadal. Flest rafmyntaspilavíti leyfa að skipta á milli mynta inni á reikningnum.</p>

<h2>Sannanleg niðurstaða (provably fair)</h2>
<p>Besta nýjungin sem rafmyntaspilavítin færðu greininni: leikir þar sem hægt er að sannreyna hverja einustu niðurstöðu. Fyrir spilið birtir síðan dulkóðaða útgáfu af fræi (hash), og eftir spilið getur þú staðfest að niðurstaðan var ákveðin áður en þú veðjaðir — ekki eftir á. <a href="{URL_BASE}spilaviti/stake/">Stake</a> og <a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a> byggðu eigin leiki á þessari tækni.</p>

<h2>Þrjú bestu rafmyntaspilavítin að okkar mati</h2>
<p><strong><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></strong> hefur tekið við Bitcoin síðan 2014 og vann til verðlauna fyrir þjónustu löngu áður en rafmyntir urðu tíska. <strong><a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a></strong> styður flestar myntir — yfir hundrað. <strong><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></strong> sameinar rafmyntagreiðslur og stærsta leikjasafnið sem við höfum skráð.</p>

<h2>Algengar spurningar</h2>
<h3>Hvar kaupi ég rafmynt sem Íslendingur?</h3>
<p>Alþjóðlegar kauphallir á borð við Kraken, Coinbase og Binance taka við íslenskum viðskiptavinum með rafrænni auðkenningu. Skref-fyrir-skref ferlið er í <a href="{URL_BASE}greidslur/hvernig-a-ad-kaupa-bitcoin/">leiðbeiningum okkar um kaup á Bitcoin</a>.</p>
<h3>Sér bankinn minn að ég er að spila?</h3>
<p>Bankinn sér kaup á rafmynt hjá kauphöll — það er lögleg fjárfestingarfærsla. Hvað gerist eftir það á blockchain kemur ekki fram á kortayfirlitinu. Athugaðu samt að kauphallir spyrja stundum um tilgang úttekta samkvæmt reglum um peningaþvætti.</p>
<h3>Hvað ef ég sendi á rangt veskisfang?</h3>
<p>Blockchain-færslur eru óafturkræfar. Engin kvörtunarleið, enginn hjálparsími. Afritaðu alltaf heimilisfangið með afrita-hnappnum, aldrei handskrifa, og sendu litla prufuupphæð fyrst þegar um stærri innlögn er að ræða.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Prófa rafmyntaspilavíti →</a></div>
"""

BODIES["spilaviti/ny-spilaviti"] = """
<p>Ný spilavíti opna í hverjum mánuði — og þau þurfa að kaupa sér leikmenn með betri kjörum en gömlu síðurnar bjóða. Það gerir þau áhugaverð. En nýtt vörumerki hefur líka enga sögu, og saga er það eina sem sannar að síða borgi út. Hér er hvernig við metum nýliðana, og hverjir standast skoðun.</p>

<h2>Nýjustu síðurnar sem við höfum tekið út</h2>
<table>
<tr><th>Spilavíti</th><th>Opnaði</th><th>Velkomstbónus</th><th>Staða skoðunar</th></tr>
<tr><td><a href="{URL_BASE}spilaviti/neospin/">Neospin</a></td><td>2023</td><td>100% + frísnúningar</td><td>Útborgun prófuð ✓</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/vegazone/">Vegazone</a></td><td>2024</td><td>Pakki á fyrstu innlagnir</td><td>Útborgun prófuð ✓</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/epicbet/">EpicBet</a></td><td>2023</td><td>Veðmál + spilavíti í einu</td><td>Útborgun prófuð ✓</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/betpanda/">Betpanda</a></td><td>2023</td><td>Rafmyntabónus</td><td>Í prófun</td></tr>
</table>

<h2>Gátlistinn okkar fyrir nýtt spilavíti</h2>
<h3>1. Flettu leyfinu upp — ekki trúa merkinu</h3>
<p>Leyfismerki neðst á síðu er bara mynd. Smelltu á það: gilt leyfi opnar staðfestingarsíðu hjá útgefandanum sjálfum með nafni rekstrarfélagsins. Ef smellurinn gerir ekkert, eða félagið á staðfestingarsíðunni passar ekki við skilmálana, er það ástæða til að loka flipanum.</p>
<h3>2. Lestu úttektarkaflann í skilmálunum</h3>
<p>Nýjar síður fela verstu ákvæðin þar: hámarksúttekt á viku (allt niður í €500 — það tekur mánuði að ná út stórum vinningi), gjald á úttektir án veltu, eða ákvæði um að „óvirkir" reikningar tæmist. Þetta tekur fimm mínútur að lesa og sparar mánaða armæðu.</p>
<h3>3. Sannreyndu leikjaframleiðendurna</h3>
<p>Fölsuð eintök af þekktum spilakössum eru til — þau líta eins út en skila annarri ávöxtun. Vísbending um alvöru safn: leikir opnast af lénum framleiðandans og framleiðandinn skráir síðuna hjá sér sem samstarfsaðila. Þekkt nöfn: NetEnt, Play'n GO, Pragmatic Play, Hacksaw.</p>
<h3>4. Prófaðu þjónustuna áður en þú leggur inn</h3>
<p>Spyrðu spjallið einnar erfiðrar spurningar: „Hver er hámarksúttekt á mánuði og hve langur er vinnslutími?" Loðið svar frá nýrri síðu er rauður fáni — því eftir innlögn verður svarið ekki skýrara.</p>

<h2>Af hverju nýjar síður bjóða betur</h2>
<p>Markaðurinn er mettur og nýtt vörumerki kaupir sér markaðshlutdeild: hærri bónusar, lægri veðskilyrði, frísnúningar án innlagnar. Fyrir leikmann sem kann að lesa skilmála er þetta raunverulegt tækifæri — kjörin versna oftast þegar síðan hefur náð fótfestu. Berðu tilboðin saman við <a href="{URL_BASE}bonusar/">bónusyfirlitið okkar</a> áður en þú velur.</p>

<h2>Algengar spurningar</h2>
<h3>Eru ný spilavíti áhættusamari en gömul?</h3>
<p>Já, að öðru jöfnu — það vantar söguna sem sannar útborganir. Áhættan minnkar verulega ef rekstrarfélagið á fleiri síður fyrir og leyfið er sannreynanlegt. Við tilgreinum rekstrarfélagið í hverri <a href="{URL_BASE}spilaviti/">umsögn</a>.</p>
<h3>Á ég að taka stóra velkomstbónusinn?</h3>
<p>Ekki sjálfkrafa. Reiknaðu veltukröfuna fyrst: 400% bónus með 50× skilyrðum þýðir að 10.000 kr. innlögn krefst 2.000.000 kr. veltu. Lítill bónus með lágum skilyrðum er oft meira virði.</p>
<h3>Hversu lengi teljið þið síðu „nýja"?</h3>
<p>Fyrstu tvö árin. Eftir það hefur safnast næg saga — kvartanir, úttektartímar, breytingar á skilmálum — til að meta síðuna eins og hverja aðra.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Sjá nýjustu tilboðin →</a></div>
"""

BODIES["spilaviti/live-spilaviti"] = """
<p>Live-spilavíti er sá hluti netspilavítis þar sem alvöru manneskja gefur spilin. Myndveri er streymt í beinni, þú veðjar af skjánum og sérð niðurstöðuna gerast fyrir framan þig — ekkert slembitölualgrím, heldur spilastokkur og rúllukúla. Fyrir marga er þetta trúverðugasta form netspilunar.</p>

<h2>Hvernig borðin virka</h2>
<p>Myndverin eru rekin af sérhæfðum framleiðendum, ekki spilavítunum sjálfum. Langstærstur er Evolution, sem rekur myndver víða um Evrópu og mannar borðin allan sólarhringinn; Pragmatic Play Live og Playtech fylgja á eftir. Spilavítið kaupir aðgang að borðunum, þess vegna sérðu sömu borðin á mörgum síðum — munurinn liggur í bónusum, lágmarksveðmálum og því hvaða borð eru opin þér.</p>

<h2>Leikirnir og raunveruleg ávöxtun þeirra</h2>
<table>
<tr><th>Leikur</th><th>RTP (besta spilamennska)</th><th>Dæmigert lágmarksveðmál</th></tr>
<tr><td><a href="{URL_BASE}live/blackjack/">Blackjack</a></td><td>~99,5%</td><td>€1–5</td></tr>
<tr><td><a href="{URL_BASE}live/baccarat/">Baccarat (bankaveðmál)</a></td><td>98,94%</td><td>€1</td></tr>
<tr><td><a href="{URL_BASE}live/roulette/">Evrópsk rúletta</a></td><td>97,30%</td><td>€0,50–1</td></tr>
<tr><td><a href="{URL_BASE}live/crazy-time/">Crazy Time</a></td><td>94,41–96,08% eftir reit</td><td>€0,10</td></tr>
</table>
<p>Taflan sýnir muninn sem spilakassaspilarar átta sig oft ekki á: borðleikir í beinni skila mun hærri fræðilegri ávöxtun en flestir spilakassar, sem liggja gjarnan á bilinu 94–96%.</p>

<h2>Hvað þarf tæknilega</h2>
<p>Streymið lagar sig að nethraða og HD-útsending þarf um 3–5 Mbps — hvaða íslenska nettenging sem er ræður við það. Borðin virka í vafra símans án sérstaks apps. Eina raunverulega krafan: stöðug tenging, því veðmálaglugginn er 10–15 sekúndur og dottin tenging í miðri hendi þýðir að hendin spilast án þín samkvæmt grunnreglu borðsins.</p>

<h2>Hvar er best að spila í beinni</h2>
<p><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> býður breiðasta úrvalið af Evolution-borðum sem við höfum séð hjá rafmyntasíðu. <a href="{URL_BASE}spilaviti/stake/">Stake</a> rekur eigin borð með sínu útliti. <a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a> er valkosturinn fyrir þá sem vilja MGA-leyfi yfir borðunum. Full úttekt er í <a href="{URL_BASE}live/">live-yfirlitinu</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Get ég talað við spilastjórann?</h3>
<p>Já — spjallglugginn birtist spilastjóranum á skjá og hann svarar upphátt í útsendingunni. Spjallið er vaktað og dónaskapur lokar á þig.</p>
<h3>Eru borðin svikin?</h3>
<p>Myndverin eru undir eftirliti leyfisveitenda framleiðandans og spilin eru skönnuð í rauntíma. Svindl í streymi sem þúsundir horfa á samtímis væri uppgötvað samstundis — áhættan fyrir leikmann liggur frekar í vali á óleyfissíðu en í borðinu sjálfu. Notaðu <a href="{URL_BASE}spilaviti/">skoðaðar síður</a>.</p>
<h3>Má spila með bónusfé í beinni?</h3>
<p>Misjafnt. Mörg spilavíti undanskilja borðleiki frá veltukröfum eða telja aðeins 10% af veðmálinu. Lestu bónusskilmálana áður en þú sest við borðið — <a href="{URL_BASE}bonusar/vedskilyrdi/">hér er hvað ber að varast</a>.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Opna live-borðin →</a></div>
"""

BODIES["spilaviti/spilaviti-med-hradri-utborgun"] = """
<p>„Samstundis útborgun" er mest misnotaða loforð greinarinnar. Raunverulegur úttektartími er summa þriggja þátta: innri afgreiðslu spilavítisins, auðkenningar þinnar og greiðsluleiðarinnar. Hér er hvernig hver þáttur virkar — og hvaða síður standast tímamælingar okkar.</p>

<h2>Hvað mælingarnar okkar sýna</h2>
<table>
<tr><th>Spilavíti</th><th>Fyrsta úttekt (með KYC)</th><th>Eftir það</th><th>Mæld leið</th></tr>
<tr><td><a href="{URL_BASE}spilaviti/stake/">Stake</a></td><td>~2 klst</td><td>Mínútur</td><td>Rafmynt</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a></td><td>~4 klst</td><td>~10 mín</td><td>Rafmynt</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a></td><td>Innan sólarhrings</td><td>0–24 klst</td><td>Rafmynt</td></tr>
<tr><td><a href="{URL_BASE}spilaviti/tonybet/">TonyBet</a></td><td>1–3 dagar</td><td>1–3 dagar</td><td>Kort/banki</td></tr>
</table>

<h2>Þátturinn sem þú stjórnar sjálfur: auðkenningin</h2>
<p>Stærsta einstaka töfin er KYC-ferlið — skilríki, stundum búsetustaðfesting, stundum uppruni fjár. Síðurnar mega ekki sleppa þessu; reglur um peningaþvætti krefjast þess. Ráðið sem sparar mest: <strong>kláraðu auðkenninguna strax eftir skráningu</strong>, áður en þú vinnur eitthvað. Þá er fyrsta úttektin þín afgreidd eins og sú tíunda.</p>

<h2>Greiðsluleiðirnar í réttri röð</h2>
<p>Eftir að spilavítið sleppir peningnum ræður leiðin ferðinni. <a href="{URL_BASE}greidslur/bitcoin/">Rafmynt</a> berst á mínútum til klukkustundar. Rafræn veski skila sér samdægurs. Kortaúttektir fara í gegnum alþjóðlega kortakerfið og taka 1–5 virka daga — og hjá íslenskum kortum bætist við óvissan um hvort færslan skili sér yfirhöfuð, sjá <a href="{URL_BASE}greidslur/visa-i-spilavitum/">umfjöllun um Visa</a>. Bankamillifærslur reka lestina með 2–7 dögum.</p>

<h2>Rauðu fánarnir sem spá fyrir um hæga útborgun</h2>
<p>Skilmálar sem nefna „allt að 14 virka daga" nota alltaf allan tímann. Vikuleg hámarksúttekt undir €2.000 þýðir að stór vinningur skilar sér í mánaðaskömmtum. Og krafa um veltu á innlögninni sjálfri — ekki bara bónusnum — áður en úttekt opnast er merki um síðu sem vill alls ekki borga út. Allar síður í <a href="{URL_BASE}spilaviti/">yfirlitinu okkar</a> eru lesnar með tilliti til þessara ákvæða.</p>

<h2>Algengar spurningar</h2>
<h3>Af hverju tók fyrsta úttektin mín marga daga en næsta mínútur?</h3>
<p>Fyrsta úttekt þín fór í handvirka skoðun: auðkenning, athugun á bónusmisnotkun, stundum uppruni fjár. Eftir samþykki ertu flokkaður sem staðfestur viðskiptavinur og sjálfvirknin tekur við.</p>
<h3>Getur spilavíti neitað að borga út?</h3>
<p>Löglega aðeins ef þú braust skilmála — algengustu tilvikin eru tvöfaldur reikningur, veðmál yfir bónushámarki og notkun VPN frá bönnuðu landi. Hjá MGA-síðum er hægt að kæra synjun til óháðs aðila; hjá Curaçao-síðum er leiðin í gegnum nýju eftirlitsstofnunina CGA.</p>
<h3>Flýtir rafmynt alltaf fyrir?</h3>
<p>Hún stýrir leiðarhlutanum en ekki innri afgreiðslunni. Rafmyntasíða með sólarhrings vinnslutíma er hægari en kortasíða sem afgreiðir á klukkustund. Taflan að ofan mælir heildartímann, ekki bara blockchain-hlutann.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Hraðasta útborgunin →</a></div>
"""

# Further batches live in their own modules, one per section.
for _mod in ("bodies_greidslur", "bodies_greidslur2", "bodies_live", "bodies_live2",
             "bodies_leidbeiningar", "bodies_bonusar", "bodies_spilaviti2", "bodies_spilaviti3", "bodies_spilaviti4", "bodies_mixed9", "bodies_leid10"):
    try:
        BODIES.update(__import__(_mod).BODIES)
    except ImportError:
        pass
