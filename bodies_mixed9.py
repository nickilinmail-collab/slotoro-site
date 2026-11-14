# -*- coding: utf-8 -*-
"""Original copy batch 9: game-type categories, VIP/high-roller/tournaments,
low wagering, wallets, bank-block workarounds."""

BODIES = {}

BODIES["spilaviti/ruletta-spilaviti"] = """
<p>Að velja síðu fyrir rúlettu er önnur ákvörðun en að kunna leikinn: reglurnar eru alls staðar eins, en framboð útgáfna, veðmálamörkin og hvort borðin telja í bónusveltu er síðuákvörðun. Þessi síða fjallar um valið; <a href="{URL_BASE}live/roulette/">leikreglurnar og útgáfumunurinn</a> eiga sína eigin umfjöllun.</p>

<h2>Tvær gerðir rúlettu á hverri síðu</h2>
<table>
<tr><th></th><th>RNG-rúletta (tölvugerð)</th><th>Rúlletta í beinni</th></tr>
<tr><td>Niðurstaðan</td><td>Slembitölualgrím, vottað</td><td>Líkamlegt hjól í myndveri</td></tr>
<tr><td>Hraði</td><td>Þinn — enginn borðtími</td><td>Spinn á ~40 sek fresti</td></tr>
<tr><td>Lágmarksveðmál</td><td>Frá ~€0,10</td><td>Frá ~€0,50</td></tr>
<tr><td>Traustupplifun</td><td>Krefst trúar á vottun</td><td>Hjólið sést snúast</td></tr>
</table>
<p>RNG-útgáfan er vanmetin af live-kynslóðinni: sami stærðfræðigrunnur, lægri mörk og enginn biðtími — rétta æfingaumhverfið áður en sest er að alvöru borði.</p>

<h2>Valgrindin fyrir rúllettusíðu</h2>
<ul>
<li><strong>Frönsk borð í boði?</strong> La partage helmingar tap jafnra veðmála á núlli — eini „afsláttur" sem rúlettan gefur. Síða án franskra borða er að halda honum frá þér.</li>
<li><strong>Engin amerísk borð í forgrunni</strong> — síða sem stillir tvöfalda núllinu fremst er að veðja á fáfræði gesta sinna.</li>
<li><strong>Veðmálabilið</strong> — frá €0,10 upp í borðhámörk sem þola kerfisspilara; þröngt bil þrengir að báðum endum.</li>
<li><strong>Bónusvægi borðleikja</strong> — rúlletta telur oft 10% eða 0% í <a href="{URL_BASE}bonusar/vedskilyrdi/">veltukröfur</a>; rúllettuspilari á bónus þarf að vita það fyrirfram.</li>
</ul>

<h2>Niðurstöður prófana okkar</h2>
<p><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> ber bæði RNG-línu og Evolution-borðin með frönskum útgáfum; <a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> er með breiðasta live-úrvalið, <a href="{URL_BASE}live/lightning-roulette/">Lightning-afbrigðið</a> meðtalið. Báðar telja rúlettu í bónusveltu með skertu vægi — skilmálatölurnar standa í <a href="{URL_BASE}spilaviti/">umsögnunum</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Er RNG-rúlettan „stillt gegn mér"?</h3>
<p>Vottuð útgáfa á leyfissíðu keyrir sannprófað slembialgrím með sama 97,3% RTP og evrópskt borð — eftirlitsstofnanirnar prófa einmitt þetta. Óleyfissíða er annað mál; þar er engin vottun og ekkert próf, og það er síðuvalsáhætta, ekki leikjaáhætta.</p>
<h3>Má spila bæði form á sama reikningi?</h3>
<p>Já — og það er besta uppsetningin: RNG til að æfa veðmálagerðir á lágmarki, live þegar upplifunin á að vera alvöru. Innistæðan er ein og söm.</p>
<h3>Hvaða útgáfu á byrjandi að velja fyrst?</h3>
<p>Evrópska eða franska RNG-borðið á lægsta veðmáli: allar veðmálagerðir, enginn tímaþrýstingur, ekkert tap sem svíður meðan reglurnar setjast. Færslan yfir í live er svo bara hraðaspurning.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Rúllettuborðin →</a></div>
"""

BODIES["spilaviti/blackjack-spilaviti"] = """
<p>Blackjack-spilari velur síðu eftir öðrum mælikvörðum en spilakassafólk: hann veit að leikurinn sjálfur gefur ~99,5% með réttri spilun, svo spurningin færist á það sem síðan stýrir — borðareglur, mörk og hvort bónuskerfið hleypir borðleikjum að. Þessi síða er valgrindin; <a href="{URL_BASE}live/blackjack/">strategían sjálf</a> er sér.</p>

<h2>Borðareglurnar sem síðan velur fyrir þig</h2>
<table>
<tr><th>Regla</th><th>Góð útgáfa</th><th>Slæm útgáfa</th><th>Áhrif á forskot hússins</th></tr>
<tr><td>Útborgun á blackjack</td><td>3:2</td><td>6:5</td><td>6:5 bætir ~1,4 prósentustigum við</td></tr>
<tr><td>Mjúk 17</td><td>Spilastjóri stendur (S17)</td><td>Tekur spil (H17)</td><td>~0,2 stig</td></tr>
<tr><td>Tvöföldun</td><td>Á hvaða tvö spil sem er</td><td>Aðeins 9–11</td><td>~0,1–0,2 stig</td></tr>
<tr><td>Uppgjöf (surrender)</td><td>Í boði</td><td>Ekki</td><td>~0,1 stig þér í hag þegar hún er til</td></tr>
</table>
<p>Summan af „smáreglunum" er munurinn á 99,5% og ~98% leik — <strong>borðavalið innan síðunnar skiptir meira máli en síðuvalið sjálft</strong>, og góð síða er sú sem býður borðin með vinstri dálkinum.</p>

<h2>RNG eða beinni — blackjack-útgáfan af spurningunni</h2>
<p>Tölvublackjack stokkar fyrir hverja hönd — spilatalning dauð, en grunnstrategían gildir óskert og hraðinn er þinn. Live-borðin gefa skóinn, spilastjórann og félagsskapinn. Ávöxtunarlega er jafntefli; æfingalega vinnur RNG (engin bið, lágmörk frá €0,10), upplifunarlega beinni. Sama tvöfalda uppsetning og í <a href="{URL_BASE}spilaviti/ruletta-spilaviti/">rúllettuvalinu</a>: æfa ódýrt, spila alvöru.</p>

<h2>Bónusgildran sem blackjack-fólk þekkir</h2>
<p>Borðleikir telja 0–10% í <a href="{URL_BASE}bonusar/vedskilyrdi/">veltukröfur</a> nær alls staðar — velkomstbónus sem á að veltast gegnum blackjack er stærðfræðileg blindgata. Blackjack-spilarinn tekur annaðhvort bónuslausan reikning (úttektir frjálsar frá fyrstu hendi) eða veltir bónusinn í kössum og sest svo að borðinu. Að hefja veltuna óvart við borðið er algengasta sjálfsmark flokksins.</p>

<h2>Hvar borðin standast grindina</h2>
<p><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> ber breiðasta úrval 3:2-borða með S17 í Evolution-línunni; <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> býður Infinite-borð með lágmarki fyrir byrjendur. Borðareglur hverrar síðu eru skráðar í <a href="{URL_BASE}spilaviti/">umsögnunum</a> — leitaðu að 6:5-viðvöruninni.</p>

<h2>Algengar spurningar</h2>
<h3>Af hverju eru 6:5-borð yfirhöfuð til?</h3>
<p>Því þau líta eins út og borga síðunni þriðjungi meira af hverjum blackjack. Þau lifa á spilurum sem lesa ekki útborgunarlínuna — fimm sekúndna athugun efst í borðreglunum ver þig.</p>
<h3>Er spilatalning bönnuð á netinu?</h3>
<p>Hún er ekki „bönnuð" — hún er gagnslaus: RNG stokkar hverja hönd, live-skór skiptast löngu fyrir nothæfa talningu. Grunnstrategían er löglega, opinberlega og endanlega hámarkið, sjá <a href="{URL_BASE}live/blackjack/">töfluna</a>.</p>
<h3>Hvað með „blackjack-mót"?</h3>
<p>Til á stærri síðunum: fast innlagnargjald, stigakeppni, verðlaunapottur — skemmtilegt format þar sem andstæðingurinn er stigataflan, ekki húsið. <a href="{URL_BASE}spilaviti/motaspilaviti/">Mótaumfjöllunin</a> tekur formið fyrir.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">3:2-borðin →</a></div>
"""

BODIES["spilaviti/vip-spilaviti"] = """
<p>VIP-kerfi spilavíta eru tryggðarprógrömm með alvöru peningavirði — og með innbyggðum hvata sem vinnur gegn þér. Bæði er satt samtímis, og sá sem skilur hvernig kerfin reiknast getur tekið virðið án þess að láta stigann spila sér. Þessi síða sundurliðar vélina.</p>

<h2>Hvernig stigarnir virka</h2>
<p>Grunnformúlan er alls staðar eins: <strong>velta → stig → þrep</strong>. Hver veðjuð evra safnar stigum (kassar oftast 100%, borðleikir skert), þrepin opna fríðindi, og efstu þrepin — oft með persónulegum stjóra — nást á veltu sem mælist í tugþúsundum evra. Tvö kerfisatriði skipta útreikninginn máli: hvort stig <em>fyrnast</em> (mánaðar-/ársfjórðungskerfi núllstilla stöðuna og búa til veltuþrýsting) og hvort þrep <em>haldast</em> þegar veltan dettur niður.</p>

<h2>Fríðindin raðað eftir raunvirði</h2>
<table>
<tr><th>Fríðindi</th><th>Raunvirði</th><th>Athugasemd</th></tr>
<tr><td>Hækkandi <a href="{URL_BASE}bonusar/endurgreidsla/">endurgreiðsla</a> / rakeback</td><td><strong>Hæst</strong></td><td>Prósenta af veltu/tapi, oft veltufrí — eina fríðindin sem skalast</td></tr>
<tr><td>Hraðari úttektir og hærri mörk</td><td>Hátt</td><td>Raunveruleg þjónustubót, sjá <a href="{URL_BASE}spilaviti/spilaviti-med-hradri-utborgun/">úttektarhraða</a></td></tr>
<tr><td>Veltufríir bónusar</td><td>Miðlungs–hátt</td><td>Sjaldgæfir neðan efstu þrepa</td></tr>
<tr><td>Afmælisgjafir, varningur, ferðir</td><td>Lágt–miðlungs</td><td>Sýnilegast, skalast verst</td></tr>
<tr><td>„Persónulegur stjóri"</td><td>Breytilegt</td><td>Þjónusta — og um leið söluaðili síðunnar</td></tr>
</table>

<h2>Hvatinn sem vinnur gegn þér</h2>
<p>Kerfið verðlaunar veltu — ekki árangur, ekki skynsemi, veltu. Fyrningarreglur og „200 stig í næsta þrep"-borðar eru hönnuð til að framkalla spilun sem þú ætlaðir ekki; persónulegi stjórinn hringir þegar þú hættir að spila, ekki þegar þú tapar. Varnarreglan er ein: <strong>VIP-staða er aukaafurð spilunar sem þú hefðir stundað hvort eð er — aldrei markmið.</strong> Um leið og þrep réttlætir innlögn hefur kerfið snúið þér; <a href="{URL_BASE}abyrg-spilun/">mörkin þín</a> eiga að standa óháð stigatöflu.</p>

<h2>Hvar kerfin eru skást hönnuð</h2>
<p><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> rekur þrepakerfi með endurgreiðslu sem vex með stigum; <a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a> er með rakeback-línu sem telur frá fyrstu veltu. Kerfislýsingar og fyrningarreglur hverrar síðu eru í <a href="{URL_BASE}spilaviti/">umsögnunum</a> — og <a href="{URL_BASE}spilaviti/harollu-spilaviti/">hárúlluumfjöllunin</a> dekkar efsta lagið sérstaklega.</p>

<h2>Algengar spurningar</h2>
<h3>Get ég samið um VIP-kjör?</h3>
<p>Á efri þrepum, já — kjörin þar eru verðskrá með svigrúmi, og kurteist „hvað getið þið boðið mér?" við þjónustuverið kostar ekkert. Veltusaga þín er samningsstaðan; spurningin er eðlileg og síðurnar vanar henni.</p>
<h3>Flyst VIP-staða milli síðna?</h3>
<p>Formlega nei, praktískt stundum: sumar síður bjóða „VIP-match" — sýndu skjáskot af þrepi annars staðar og fáðu sambærilegt. Spyrja borgar sig áður en veltusagan byrjar á núlli.</p>
<h3>Eru VIP-boð í tölvupósti alvöru?</h3>
<p>Boð frá síðu sem þú átt reikning hjá: oftast já, en virkjaðu tilboðið inni á síðunni, aldrei gegnum hlekk í pósti sem þú getur ekki sannreynt. „VIP-boð" frá ókunnum síðum er veiðipóstur, punktur.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Vildarkerfin →</a></div>
"""

BODIES["spilaviti/harollu-spilaviti"] = """
<p>Hárúlluspilarinn — sá sem veðjar hundruðum evra á hendi eða þúsundum á kvöldi — hefur þarfir sem venjuleg síðuhönnun afgreiðir illa: borðhámörk, úttektarþök og þjónustuhraði verða aðalatriði, bónusprósentur aukaatriði. Þessi síða er valgrind fyrir það lag markaðarins, skrifuð án glamúrsins sem fylgir orðinu „high roller".</p>

<h2>Flöskuhálsarnir sem stór veltuspilari rekst á</h2>
<table>
<tr><th>Flöskuháls</th><th>Dæmigerð mörk markaðarins</th><th>Hvað þarf að sannreyna</th></tr>
<tr><td>Borðhámark</td><td>€500–5.000 á hendi í beinni</td><td>VIP-borð (Salon Privé gerðin) með hærri mörkum — aðgangskrafa oft lágmarksinnistæða</td></tr>
<tr><td>Vikuleg úttektarþök</td><td>€5.000–20.000</td><td>Stór vinningur á þaki skilar sér í mánaðaskömmtum — þakið er mikilvægasta talan í skilmálunum</td></tr>
<tr><td>Innlagnarhámörk greiðsluleiða</td><td>Kort oft €1.000–5.000</td><td><a href="{URL_BASE}greidslur/bitcoin/">Rafmynt</a> er í praxís eina ótakmarkaða leiðin</td></tr>
<tr><td>KYC á stórar hreyfingar</td><td>Uppruni fjár við háar upphæðir</td><td>Skjölin tilbúin fyrirfram — launaseðlar, söluyfirlit; sjá <a href="{URL_BASE}spilaviti/spilaviti-med-hradri-utborgun/">úttektarferlið</a></td></tr>
</table>

<h2>Bónusstærðfræðin snýst við á þessu stigi</h2>
<p>Velkomstbónus með €200-þaki er suð fyrir €5.000-innlögn — en <a href="{URL_BASE}bonusar/endurgreidsla/">endurgreiðsla og rakeback</a> skalast línulega með veltu og verða stærsta einstaka kjarabreytan: 10% vikulegt cashback á stórri veltu er meira fé á ári en nokkur velkomstpakki markaðarins. Hárúlluspilarinn ber því saman <a href="{URL_BASE}spilaviti/vip-spilaviti/">VIP-kerfin</a>, ekki forsíðutilboðin — og semur; á þessu veltustigi eru kjörin viðræðugrundvöllur, ekki verðskrá.</p>

<h2>Áhættudreifing sem stórspilarar vanrækja</h2>
<p>Stór innistæða á einni síðu er mótaðilaáhætta, sama hve traust síðan virðist: <a href="{URL_BASE}spilaviti/malta-mga-spilaviti/">MGA-sjóðaaðskilnaður</a> er eina kerfislega vörnin, og hann fylgir fáum síðunum í rafmyntalaginu. Praktíska reglan: spilarúllan inni, afgangurinn úti — stórar upphæðir ferðast inn fyrir lotu og út eftir hana, ekki búa á síðunni. Rafmyntaleiðin gerir þetta ókeypis og hratt; það er raunverulegi hárúllukostur hennar.</p>

<h2>Hvar efra lagið er afgreitt almennilega</h2>
<p><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> hefur afgreitt stærstu úttektirnar í okkar prófunum án þakleikfimi; <a href="{URL_BASE}spilaviti/stake/">Stake</a> rekur þekktasta stórveltulag rafmyntaheimsins með samningskjörum. Þakatölur beggja eru skráðar í <a href="{URL_BASE}spilaviti/">umsögnunum</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Hvað telst „hárúlla" í netspilun?</h3>
<p>Engin opinber lína — markaðurinn hólfar við ~€100+ meðalveðmál eða €10.000+ mánaðarveltu; VIP-kerfin draga sínar línur í stigum. Línan sem skiptir þig máli er önnur: upphæðin þar sem borðhámörk og úttektarþök byrja að þvælast fyrir þér. Þar byrjar þessi flokkur.</p>
<h3>Fæ ég betri RTP sem stórspilari?</h3>
<p>Nei — leikirnir borga öllum eins, sjá <a href="{URL_BASE}leidbeiningar/hvad-er-rtp/">RTP-leiðarvísinn</a>. Það sem batnar er allt í kringum leikinn: kjör, mörk, þjónusta. Síða sem lofar „betri leikjum fyrir VIP" lofar einhverju sem kerfið býður ekki.</p>
<h3>Er Salon Privé þess virði?</h3>
<p>Fyrir þann sem spilar hvort eð er á þeim mörkum: já — einkaborð, eigin spilastjóri, stundum reglustillingar. Aðgangsþröskuldurinn er innistæða/velta, ekki gjald; þetta er þjónustulag, ekki áskrift.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Stórveltukjörin →</a></div>
"""

BODIES["spilaviti/motaspilaviti"] = """
<p>Spilavítamót snúa einleikjaforminu í keppni: sama leik spila allir, stigataflan raðar, potturinn skiptist eftir sætum. Fyrir spilarann breytir formið grundvallaratriði — andstæðingurinn er ekki lengur húsforskotið heldur hinir á töflunni — og sú breyting opnar eina af fáum raunverulegum „edge"-holum netspilunar. Hún er útskýrð neðst.</p>

<h2>Mótaformin þrjú</h2>
<table>
<tr><th>Form</th><th>Hvernig stig safnast</th><th>Hvað ræður úrslitum</th></tr>
<tr><td>Spilakassamót</td><td>Stærsti vinningur í hlutfalli við veðmál (×-margfaldari), eða heildarvinningar á föstum snúningafjölda</td><td>Sveifluval og heppni</td></tr>
<tr><td>Veltumót / stigahlaup</td><td>Hver veðjuð evra telur — <a href="{URL_BASE}spilaviti/pragmatic-play-spilaviti/">Drops & Wins</a> gerðin</td><td>Veltumagn; varúðar þörf</td></tr>
<tr><td>Borðamót (blackjack/póker)</td><td>Staða eftir fastar hendur/umferðir</td><td>Spilamennska skiptir raunverulegu máli</td></tr>
</table>
<p>Formin tvö fyrstu eru skemmtun með verðlaunamöguleika; veltumótin eru beinlínis hættuleg þeim sem eltir töfluna — þau verðlauna spilun umfram plan, sama vélin og <a href="{URL_BASE}spilaviti/vip-spilaviti/">VIP-stigarnir</a>. Fast þátttökubudget fyrirfram eða ekki taka þátt.</p>

<h2>Edge-holan: margfaldaramótin</h2>
<p>Mót sem raðar eftir hæsta stakmargfaldara (t.d. „besti vinningur ×veðmál á 100 snúningum") hefur rétta strategíu, og hún er gagnstæð venjulegri spilun: <strong>lágmarksveðmál + hásveifluleikur</strong>. Veðmálsupphæðin skiptir töfluna engu (margfaldarinn er hlutfall), svo ódýrustu snúningarnir kaupa jafn marga „lottómiða" í töfluna og dýrir — og hásveiflukassi framleiðir stóru margfaldarana. Fríroll-mót (ókeypis þátttaka) með þessu formi eru fáu tilvikin þar sem vænt gildi spilarans er hreinlega jákvætt. Þau eru líka vinsælasta byrjendagildra símasíðna — í hina áttina: gjaldmót með lélegum potti borga sig sjaldan.</p>

<h2>Hvernig þú metur mót á 30 sekúndum</h2>
<ol>
<li><strong>Þátttökukostnaður</strong> — fríroll, veðmálakrafa eða gjald?</li>
<li><strong>Pottur ÷ áætlaður þátttakendafjöldi</strong> — stigataflan sýnir fjöldann; €2.000 pottur á 5.000 manns er suð.</li>
<li><strong>Dreifing verðlauna</strong> — topp-þung tafla (50% á fyrsta sæti) er happdrætti, flöt tafla borgar breidd.</li>
<li><strong>Stigaformið</strong> — margfaldaraform = lágveðmálsstrategían að ofan; veltuform = budget-reglan.</li>
</ol>

<h2>Hvar mótin ganga</h2>
<p><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> rekur fastar borða- og kassakeppnir með flatri verðlaunadreifingu; <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> keyrir Drops & Wins línuna og eigin helgarmót. Mótadagatöl standa í <a href="{URL_BASE}spilaviti/">umsögnunum</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Telur mótaspilun í bónusveltu og VIP-stig?</h3>
<p>Veðmálin sjálf oftast já — mótaverðlaunin koma svo ýmist sem reiðufé eða bónusfé með eigin <a href="{URL_BASE}bonusar/vedskilyrdi/">veltukröfu</a>. Verðlaunaformið stendur í mótareglunum; það er munurinn á alvöru potti og markaðspotti.</p>
<h3>Má skipta um leik í miðju kassamóti?</h3>
<p>Fer eftir reglum: sum mót binda einn leik, önnur leikjalista. Margfaldarastrategían virkar best þar sem listinn leyfir hásveifluval — lestu leikjalistann áður en þú „eyðir" snúningunum þínum.</p>
<h3>Eru stigatöflurnar sviknar af botnum?</h3>
<p>Á leyfissíðum eru þátttakendur raunreikningar undir sömu KYC-reglum og allir aðrir; „ómögulegar" tölur efst eru nær alltaf stórveltuspilarar í veltuformi. Enn ein ástæða til að kjósa margfaldaraformið — þar keppa allir á sama miða.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Mót í gangi →</a></div>
"""

BODIES["spilaviti/lag-vedskilyrdi-spilaviti"] = """
<p>Lág veðskilyrði eru eina bónuseinkennið sem réttlætir síðuval eitt og sér: 20× bónus sem klárast er meira virði en 200% tilboð sem rennur út í veltunni miðri. Þessi flokkur raðar markaðnum eftir tölunni sem raunverulega ræður — margfaldaranum — og endar á tilboðsgerðinni sem slær hann alveg út.</p>

<h2>Hvað telst „lágt"? Kvörðun markaðarins</h2>
<table>
<tr><th>Margfaldari (af bónus)</th><th>Flokkun</th><th>€100 bónus kostar í veltu</th></tr>
<tr><td>0× (veltufrítt)</td><td>Gull — sjaldgæft</td><td>€0</td></tr>
<tr><td>15–25×</td><td>Lágt — raunhæft markmið</td><td>€1.500–2.500</td></tr>
<tr><td>30–40×</td><td>Markaðsmeðaltal</td><td>€3.000–4.000</td></tr>
<tr><td>45×+</td><td>Hátt — bónusinn er skraut</td><td>€4.500+</td></tr>
</table>
<p>Grunngildran óbreytt frá <a href="{URL_BASE}bonusar/vedskilyrdi/">veðskilyrðaumfjölluninni</a>: „af bónus og innlögn" tvöfaldar dæmið þegjandi, og leikjavægi (borðleikir 0–10%) getur gert lága tölu háa í framkvæmd. Lágt skilyrði á pappír er aðeins lágt fyrir kassaspilara.</p>

<h2>Hvers vegna sumar síður verðleggja lágt</h2>
<p>Veltukröfur eru áhættustýring gegn bónusveiði — há tala ver síðuna, lág tala treystir leikjavali og hámarksveðmálsreglum fyrir vörnina. Síður sem bjóða lág skilyrði eru því yfirleitt annaðhvort að kaupa markaðshlutdeild (nýjar, sjá <a href="{URL_BASE}spilaviti/ny-spilaviti/">nýsíðuflokkinn</a>) eða með viðskiptamódel sem hvílir minna á bónusþvingun — rafmyntasíður með <a href="{URL_BASE}bonusar/endurgreidsla/">rakeback-kjarna</a> eru algengasta dæmið. Hvort tveggja er gild ástæða; það sem lág tala er aldrei: tilviljun.</p>

<h2>Veltufríi flokkurinn — þegar margfaldarinn hverfur</h2>
<p>„No wagering" tilboð borga vinninga sem reiðufé: engin velta, ekkert þak á úttekt oftast, bara minni upphafstölur. Fyrir spilarann sem reiknar er valið milli 200 veltusnúninga og 20 veltufríra ekki val — frísnúningavinningar á 40× skilyrðum enda tölfræðilega nálægt núlli, veltufríir eru krónur í hendi. Þar sem þessi tilboð sjást á markaðnum merkjum við þau efst í <a href="{URL_BASE}bonusar/">bónusyfirlitinu</a>.</p>

<h2>Staðan í safninu okkar</h2>
<p><a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> liggur undir markaðsmeðaltali á velkomstlínunni og telur af bónus eingöngu; <a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a> leysir dæmið frá hinni hliðinni — rakeback frá fyrstu veltu í stað þungra bónusa. Tölur hverrar síðu eru í <a href="{URL_BASE}spilaviti/">umsögnunum</a>, alltaf með grunninum (bónus vs bónus+innlögn) tilgreindum.</p>

<h2>Algengar spurningar</h2>
<h3>Er lágt skilyrði með lágu bónusþaki betra en hátt með háu?</h3>
<p>Reiknaðu veltuna á móti því sem þú hefðir hvort eð er spilað: ætlir þú að velta €2.000 í mánuðinum er 20× á €100 bónus (€2.000) ókeypis peningur; 45× á €300 (€13.500) er skuldbinding sem breytir hegðun þinni. Bónusinn á að passa við spilunina, ekki öfugt.</p>
<h3>Get ég beðið síðu um lægri skilyrði?</h3>
<p>Á venjuleg tilboð sjaldan — en <a href="{URL_BASE}spilaviti/vip-spilaviti/">VIP-lagið</a> semur, og „bónuslaus + hærra cashback" er samningsstaða sem þjónustuver þekkja. Spyrja kostar ekkert.</p>
<h3>Hvað gerist ef ég næ ekki veltunni í tíma?</h3>
<p>Bónusfé og bónusvinningar falla niður; innlögnin þín stendur. Þess vegna er tímaramminn (7–30 dagar) þriðja talan sem þarf að lesa — lág velta á stuttum fresti getur verið þyngri en meðalvelta á löngum.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Lægstu skilyrðin →</a></div>
"""

BODIES["greidslur/dulritunarveski"] = """
<p>Veskið er eina rafmyntaákvörðunin sem þú tekur áður en fyrsta myntin er keypt — og sú sem flestir taka óvart, með því að taka hana ekki: mynt skilin eftir á kauphöll er líka „veskisval", bara ómeðvitað. Þessi síða raðar valkostunum eftir því sem spilara varðar: aðgangshraða, áhættu og ábyrgð.</p>

<h2>Þrjú lög af vörslu</h2>
<table>
<tr><th>Lag</th><th>Hver geymir lyklana</th><th>Hentar fyrir</th><th>Aðaláhættan</th></tr>
<tr><td>Kauphallarreikningur</td><td>Kauphöllin</td><td>Virka spilarúllu, tíð kaup/sölu</td><td>Mótaðili: frysting, gjaldþrot, reikningslokun</td></tr>
<tr><td>Hugbúnaðarveski (MetaMask, Trust Wallet…)</td><td>Þú — lyklar í síma/vafra</td><td>Milligeymslu, beinar greiðslur</td><td>Tækjaþjófnaður, phishing, frasaleki</td></tr>
<tr><td>Vélbúnaðarveski (kaldgeymsla)</td><td>Þú — lyklar í sértæki</td><td>Upphæðir sem svíður að missa</td><td>Þín eigin skipulagning: frasarnir tapaðir = allt tapað</td></tr>
</table>

<h2>Uppsetningin sem hentar spilara</h2>
<p>Spilarúlla þarf hraða, sparnaður þarf öryggi — blanda laganna leysir hvort tveggja: <strong>kauphöllin sem gátt</strong> (kaup, sala, úttektir til spilavíta — ferlið úr <a href="{URL_BASE}greidslur/hvernig-a-ad-kaupa-bitcoin/">kaupleiðbeiningunum</a>), <strong>eigið veski sem heimahöfn</strong> fyrir það sem á að standa kyrrt. Vinningar fara kauphöll→sala→banki eða kauphöll→eigið veski eftir því hvort þeir eru eyðsla eða eign. Það sem aldrei gerist í góðri uppsetningu: stórar upphæðir sofa á spilasíðu eða kauphöll mánuðum saman.</p>

<h2>Frasarnir tólf — eina reglan sem fyrirgefur ekki</h2>
<p>Eigið veski afhendir þér endurheimtufrasa: 12–24 orð sem ERU veskið. Sá sem hefur þá á allt; enginn hjálparsími endurheimtir þá týnda. Reglurnar þrjár: skrifaðir á pappír (ekki skjáskot, ekki skýjamappa — stafræn afrit eru það sem þjófavélar leita að), geymdir á tveimur stöðum, og <strong>aldrei slegnir inn á vefsíðu</strong>. „Validate your wallet"-síður og stuðningsfulltrúar sem biðja um frasa eru svindl í 100% tilvika — ekki 99: hundrað.</p>

<h2>Spilavítasértæku atriðin</h2>
<p>Úttektarfangið þitt hjá spilavíti á að vera fang sem þú stjórnar eða kauphallarfangið þitt — aldrei fang þriðja aðila („vinur ætlar að selja fyrir mig" er bæði skilmálabrot og svindlmynstur). Og netavalið fylgir veskinu: veski sem sýnir margar keðjur (Trust Wallet gerðin) minnkar hættuna á <a href="{URL_BASE}greidslur/usdt/">rangs-nets-mistökunum</a>, en athugaðu samt netmerkinguna við hverja úttekt — vaninn, ekki veskið, er vörnin.</p>

<h2>Algengar spurningar</h2>
<h3>Þarf spilari yfirhöfuð eigið veski?</h3>
<p>Fyrir hreina spilanotkun dugar kauphallarleiðin — einfaldari endurheimt, kunnuglegt viðmót. Eigið veski verður svarið þegar upphæðir vaxa (mótaðilaáhættan), þegar þú vilt greiða síðum beint, eða þegar kauphöllin þín spyr of margra spurninga um spilavítafærslur.</p>
<h3>Er MetaMask eða Trust Wallet „öruggara"?</h3>
<p>Bæði eru margprófuð; munurinn er vistkerfi (MetaMask = Ethereum-heimurinn, Trust = fjölkeðju) fremur en öryggisstig. Öryggið ræðst af hegðun: frasameðferð, phishing-árvekni, uppfærslur. Veikasti hlekkurinn hefur alltaf sama nafn og eigandinn.</p>
<h3>Hvað ef ég dey eða missi minnið — er myntin farin?</h3>
<p>Án skipulags, já: frasalaus erfingi erfir ekkert. Lausnin er lágstemmd — innsiglað umslag með frösum á stað sem erfðaskráin þín nær til. Óþægileg hugsun, fimm mínútna verk, og eini munurinn á eign og engu fyrir þá sem eftir standa.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Greiða úr eigin veski →</a></div>
"""

BODIES["greidslur/framhja-bankalokunum"] = """
<p>Kortinu hafnað með „færsla ekki heimil" — og engin skýring. Þetta er algengasta fyrsta snerting Íslendinga við spilavítagreiðslur, og þessi síða útskýrir hvað gerðist, hvað er löglegt og hverjar raunverulegu leiðirnar framhjá eru. Allar þrjár staðreyndir fyrst: lokunin er bankaregla en ekki lög, þú braust ekkert af þér, og löglegar leiðir eru til.</p>

<h2>Hvað lokar — og hvað ekki</h2>
<p>Hver kortafærsla ber söluaðilaflokk; fjárhættuspil er 7995, og kortaútgefandinn ákveður hvort flokkurinn fer í gegn — áhættu- og regluvörslumat hvers banka, ekki landslög. Þess vegna er myndin ósamkvæm: sami banki getur hleypt færslu í gegn á einni síðu og hafnað annarri (skráning söluaðilans ræður), debet og kredit hegða sér ólíkt, og reglurnar breytast án tilkynningar. Smáatriðin eru í <a href="{URL_BASE}greidslur/visa-i-spilavitum/">Visa-</a> og <a href="{URL_BASE}greidslur/mastercard-i-spilavitum/">Mastercard-umfjöllununum</a>.</p>

<h2>Leiðirnar framhjá, raðaðar eftir notagildi</h2>
<table>
<tr><th>Leið</th><th>Hvernig hún sneiðir hjá 7995</th><th>Fyrirvari</th></tr>
<tr><td><a href="{URL_BASE}greidslur/bitcoin/">Rafmynt</a></td><td>Kaup á kauphöll eru fjárfestingarfærsla; blockchain-hlutinn snertir ekki kortakerfið</td><td>Kaupin sjálf: kauphallarskráning + gjöld</td></tr>
<tr><td><a href="{URL_BASE}greidslur/skrill-i-spilavitum/">Rafveski (Skrill/Neteller)</a></td><td>Hleðsla veskis flokkast sem veskisfærsla; veski→síða er innan veskiskerfis</td><td>Gjaldskrá veskjanna, bónusútilokanir</td></tr>
<tr><td>Fyrirframgreiddir kóðar</td><td>Keyptir sem vara, sjá <a href="{URL_BASE}greidslur/paysafecard-i-spilavitum/">paysafecard</a></td><td>Stopult framboð á Íslandi, engin úttektarleið</td></tr>
</table>
<p>Rafmyntaleiðin er sú sem markaðurinn hefur í raun valið: hún leysir lokunina varanlega, í báðar áttir, og er hraðasta úttektarleiðin í leiðinni. <a href="{URL_BASE}spilaviti/crypto-spilaviti/">Rafmyntasíðuyfirlitið</a> er framhaldslesningin.</p>

<h2>Það sem við mælum EKKI með</h2>
<p>Heiðarleg umfjöllun um „framhjá" þarf líka bannlistann: <strong>rangur söluaðilaflokkur</strong> (síður sem bóka spilafærslur sem „ráðgjöf" eða netverslun) er sviksamleg skráning — merki um síðu sem svindlar líka annars staðar, og færslurnar þínar geta fryst í uppgjörsdeilum. <strong>Kort þriðja aðila</strong> brýtur skilmála og endar í frystum vinningum við fyrstu KYC-skoðun. <strong>VPN til að þykjast annað land</strong> leysir ekkert greiðslutengt en bætir skilmálabroti ofan á. Leiðirnar í töflunni eru löglegar og skilmálahreinar; þessar þrjár eru það ekki, og gallinn lendir alltaf á spilaranum.</p>

<h2>Algengar spurningar</h2>
<h3>Má bankinn minn yfirhöfuð loka á þetta?</h3>
<p>Já — færsluheimildir eru þjónustuskilmálar kortsins, og áhætturöksemdir bankans (svikatíðni, endurkröfur í flokknum) eru málefnalegar þó niðurstaðan sé óþægileg. Sum kortafyrirtæki bjóða flokkastillingar í netbanka; athugun þar er fyrsta skrefið áður en þú byggir hjáleið.</p>
<h3>Er það peningaþvætti að fara rafmyntaleiðina?</h3>
<p>Nei — kaup á skráðri kauphöll með eigin auðkenndum reikningi, millifærsla á spilasíðu og úttekt sömu leið er gagnsæ keðja með skjalfestan uppruna. Þvættisreglurnar snúast um uppruna fjár, ekki um hvað þú kaupir fyrir þitt eigið; geymdu færslusöguna og <a href="{URL_BASE}leidbeiningar/skattur-a-vinninga/">skattaumfjöllunin</a> dekkar framtalshliðina.</p>
<h3>Af hverju gengur innlögn en úttekt á sama kort ekki?</h3>
<p>Úttektir á kort fara aðra kerfisleið (OCT-færslur) sem færri útgefendur styðja fyrir 7995 — algeng og óþægileg ósamhverfa. Reglan úr kortaumfjöllununum gildir: úttektarleiðin skipulögð áður en vinningurinn verður til.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Greiðsluleiðir sem virka →</a></div>
"""
