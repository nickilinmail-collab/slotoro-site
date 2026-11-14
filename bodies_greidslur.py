# -*- coding: utf-8 -*-
"""Original copy for /greidslur/ pages. Each page has its own structure and
vocabulary — nothing here may be copied between entries."""

BODIES = {}

BODIES["greidslur/bitcoin"] = """
<p>Bitcoin er algengasta innlagnarleiðin á erlend spilavíti frá Íslandi — ekki af hugsjón, heldur af praktík: færslan fer beint á milli veskja og enginn banki fær tækifæri til að hafna henni.</p>

<h2>Leiðin frá krónum að spilareikningi, skref fyrir skref</h2>
<ol>
<li><strong>Stofnaðu aðgang hjá kauphöll.</strong> Kraken og Coinbase taka við íslenskum kennitölum og styðja rafræn skilríki við auðkenningu. Binance er þriðji kosturinn.</li>
<li><strong>Kauptu BTC með korti eða millifærslu.</strong> Kortakaup skila myntinni strax en bera 1,5–4% gjald; SEPA-millifærsla af gjaldeyrisreikningi er ódýrari en tekur 1–2 daga.</li>
<li><strong>Sæktu innlagnarfangið hjá spilavítinu.</strong> Undir „Deposit" → Bitcoin birtist fang (byrjar á bc1, 1 eða 3) og oftast QR-kóði.</li>
<li><strong>Sendu af kauphöllinni á fangið.</strong> Afritaðu með hnappnum — aldrei handrita. Fyrir upphæðir yfir ~50.000 kr. mælum við með lítilli prufusendingu fyrst.</li>
<li><strong>Bíddu staðfestinga.</strong> Flest spilavíti telja innlögnina gilda eftir 1–3 staðfestingar á netinu, sem tekur frá tíu mínútum upp í klukkustund eftir álagi.</li>
</ol>

<h2>Hvað kostar þetta í raun?</h2>
<table>
<tr><th>Liður</th><th>Dæmigerður kostnaður</th><th>Hver tekur gjaldið</th></tr>
<tr><td>Kaup á BTC með korti</td><td>1,5–4%</td><td>Kauphöllin</td></tr>
<tr><td>Úttekt af kauphöll</td><td>Fast gjald, breytilegt</td><td>Kauphöllin</td></tr>
<tr><td>Netgjald (mining fee)</td><td>Oftast $1–5, sveiflast</td><td>Bitcoin-netið</td></tr>
<tr><td>Innlögn hjá spilavíti</td><td>0 kr. hjá öllum sem við skráum</td><td>—</td></tr>
</table>
<p>Samtals er raunkostnaðurinn við að koma 100 evrum inn á spilareikning oftast á bilinu 2–6% — sambærilegur við erlenda kortafærslu, en án höfnunaráhættunnar.</p>

<h2>Tvennt sem brennir byrjendur</h2>
<p><strong>Gengið hreyfist meðan þú spilar.</strong> Innistæðan þín er í BTC; falli gengið um 5% yfir kvöldið hefur bankrúllan þín rýrnað jafn mikið. Sá sem vill festa verðgildið skiptir yfir í <a href="{URL_BASE}greidslur/usdt/">USDT</a> inni á síðunni þar sem það er í boði.</p>
<p><strong>Rangt net við úttekt.</strong> Þegar þú tekur út skaltu velja Bitcoin-netið fyrir BTC-fang. Sumir ruglast á „BTC" og „BTC (Lightning)" eða wrapped-útgáfum á öðrum netum — mynt á röngu neti er töpuð.</p>

<h2>Hvar virkar þetta best</h2>
<p><a href="{URL_BASE}spilaviti/bitstarz/">BitStarz</a> hefur afgreitt Bitcoin-úttektir á ~10 mínútum í okkar prófunum. <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> og <a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a> taka bæði við BTC án innlagnargjalds. Berðu saman í <a href="{URL_BASE}spilaviti/crypto-spilaviti/">yfirliti rafmyntaspilavíta</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Er Lightning-netið studd leið?</h3>
<p>Æ fleiri síður bjóða Lightning fyrir smærri upphæðir — færslan kostar brot úr krónu og skilar sér á sekúndum. Athugaðu innlagnargluggann; ef þar stendur aðeins „Bitcoin" er það hefðbundna netið.</p>
<h3>Hve lítið get ég lagt inn?</h3>
<p>Lágmörk spilavítanna eru oftast 0,0001–0,0005 BTC. Neðan við það borgar netgjaldið sig ekki — fyrir örinnlagnir er <a href="{URL_BASE}greidslur/litecoin/">Litecoin</a> hagkvæmari.</p>
<h3>Hvað geri ég við vinninginn?</h3>
<p>Sama leið til baka: úttekt á kauphallarfangið þitt, sala í evrur eða dollara, millifærsla heim. Mundu að kauphöllin getur óskað skýringa á uppruna fjár samkvæmt peningaþvættisreglum — geymdu skjáskot af úttektarstaðfestingu spilavítisins.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Leggja inn með Bitcoin →</a></div>
"""

BODIES["greidslur/ethereum"] = """
<p>Ethereum er næststærsta rafmyntin og á spilavítum gegnir hún öðru hlutverki en Bitcoin: blokkir myndast á ~12 sekúndna fresti, svo innlögnin þín er komin inn á meðan Bitcoin-notandinn bíður enn fyrstu staðfestingar.</p>

<h2>ETH á móti hinum — hvenær er það rétta valið?</h2>
<p>Veldu Ethereum þegar hraðinn skiptir þig máli og upphæðin er miðlungs eða stærri. Fyrir smáupphæðir étur netgjaldið hlutfallslega mikið — gas-gjaldið fer eftir álagi á netinu og getur sveiflast frá under $1 upp í tugi dollara á háannatíma. Fyrir fastar, fyrirsjáanlegar færslur er <a href="{URL_BASE}greidslur/usdt/">USDT á TRON-netinu</a> ódýrari; fyrir verðtryggingu gagnvart sveiflum sömuleiðis.</p>

<h2>Það sem enginn útskýrir: gas</h2>
<p>Hver færsla á Ethereum greiðir „gas" — þóknun til staðfestingaraðila netsins. Gasverð er uppboðsmarkaður: þegar margir nota netið hækkar það. Praktísk regla fyrir spilara: sendu innlagnir utan bandarísks dagtíma, þá er netið rólegra og gjaldið lægra. Kauphallirnar sýna áætlað gjald áður en þú staðfestir — ef það virðist hátt, bíddu klukkustund og athugaðu aftur.</p>

<h2>Innlögn í fimm línum</h2>
<ol>
<li>Kauptu ETH hjá Kraken, Coinbase eða Binance.</li>
<li>Opnaðu „Deposit" → Ethereum (ERC-20) hjá spilavítinu og afritaðu fangið (byrjar á 0x).</li>
<li>Sendu af kauphöllinni og veldu <strong>Ethereum-netið</strong> — ekki Arbitrum, Optimism eða önnur hliðarnet nema spilavítið taki það skýrt fram.</li>
<li>Færslan er inni eftir ~1–2 mínútur.</li>
<li>Úttekt fer sömu leið til baka, á 0x-fangið þitt.</li>
</ol>

<h2>MetaMask-leiðin fyrir lengra komna</h2>
<p>Eigið veski eins og MetaMask sleppir kauphöllinni úr miðjunni: þú geymir myntina sjálfur og tengist spilavítinu beint. Á móti kemur full ábyrgð — frasarnir tólf eru eina öryggisafritið og enginn hjálparsími endurheimtir þá. Byrjendum ráðleggjum við kauphallarleiðina; hún er einfaldari og mistök eru afturkræfari.</p>

<h2>Síður sem fara vel með ETH</h2>
<p><a href="{URL_BASE}spilaviti/stake/">Stake</a> bókar Ethereum-innlagnir hraðast í okkar mælingum. <a href="{URL_BASE}spilaviti/bc-game/">BC.Game</a> leyfir að skipta ETH í stablecoin inni á reikningnum. <a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> styður ETH bæði inn og út án gjalds af sinni hálfu.</p>

<h2>Algengar spurningar</h2>
<h3>Sendi ég ETH eða get ég notað token?</h3>
<p>Innlagnarfang spilavítis fyrir Ethereum tekur yfirleitt aðeins við ETH sjálfu. USDT, USDC og aðrir tokenar eiga sína eigin innlagnarglugga — token sendur á ETH-glugga getur tapast.</p>
<h3>Af hverju segir kauphöllin „pending" svona lengi?</h3>
<p>Annaðhvort er gasverðið sem þú valdir of lágt fyrir álagið, eða kauphöllin safnar úttektum í hópa. Ethereum-hluti leiðarinnar tekur mínútur; biðin liggur nær alltaf hjá kauphöllinni.</p>
<h3>Er ETH öruggara en BTC?</h3>
<p>Bæði net eru margprófuð og örugg í sjálfu sér. Áhættan þín er sú sama: gengissveiflur og mannleg mistök við föng og net — ekki tæknin.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Spila með Ethereum →</a></div>
"""

BODIES["greidslur/visa-i-spilavitum"] = """
<p>Visa-kortið í veskinu þínu virkar á erlendum spilavítum — stundum. Þessi síða útskýrir af hverju „stundum", hvað ræður niðurstöðunni og hvað þú gerir þegar færslunni er hafnað.</p>

<h2>Af hverju íslensk kort klikka á spilavítum</h2>
<p>Hver kortafærsla ber flokkunarkóða söluaðila (MCC). Fjárhættuspil er kóði 7995, og kortaútgefandinn — bankinn þinn — ákveður hvort hann hleypir þeim flokki í gegn. Íslensku bankarnir þrír beita þarna mismunandi og breytilegum reglum, og niðurstaðan getur verið ólík milli debet- og kreditkorta frá sama banka. Sama kort getur því virkað á einni síðu og ekki annarri, eftir því hvernig söluaðilinn er skráður.</p>

<h2>Ef þú ætlar samt að nota kortið</h2>
<ul>
<li><strong>Kreditkort fremur en debet</strong> — höfnunartíðnin er lægri í okkar reynslu.</li>
<li><strong>3-D Secure þarf að vera virkt</strong> — erlend spilavíti keyra nær öll sannvottun í appi bankans.</li>
<li><strong>Byrjaðu smátt.</strong> Fyrsta færsla upp á 2–3 þúsund krónur segir þér strax hvort leiðin er opin, án þess að stærri upphæð frjósi í biðstöðu.</li>
<li><strong>Gerðu ráð fyrir gjaldeyrisálagi.</strong> Færslan er í evrum eða dollurum; ofan á gengið leggst erlent færslugjald kortsins.</li>
</ul>

<h2>Vandamálið sem kemur á óvart: úttektin</h2>
<p>Jafnvel þegar innlögn með Visa heppnast er ekki sjálfgefið að úttekt skili sér sömu leið. Endurgreiðsla á kort (OCT-færsla) er ekki studd hjá mörgum erlendum síðum, og þá býður spilavítið bankamillifærslu eða rafmynt í staðinn. Þú gætir sem sagt lagt inn með korti en þurft aðra leið út — skipulegðu það áður en þú vinnur, ekki eftir á.</p>

<h2>Raunhæfu valkostirnir</h2>
<table>
<tr><th>Leið</th><th>Höfnunaráhætta</th><th>Hraði út</th></tr>
<tr><td>Visa/Mastercard</td><td>Veruleg hjá íslenskum kortum</td><td>1–5 virkir dagar, ef í boði</td></tr>
<tr><td><a href="{URL_BASE}greidslur/bitcoin/">Bitcoin</a></td><td>Engin</td><td>Mínútur–klst</td></tr>
<tr><td><a href="{URL_BASE}greidslur/usdt/">USDT</a></td><td>Engin</td><td>Mínútur</td></tr>
<tr><td><a href="{URL_BASE}greidslur/apple-pay-i-spilavitum/">Apple Pay</a></td><td>Sama og kortið undir því</td><td>Á ekki við út</td></tr>
</table>

<h2>Algengar spurningar</h2>
<h3>Færslunni var hafnað — er kortið mitt í lagi?</h3>
<p>Já. Höfnun á 7995-flokki segir ekkert um kortið þitt annars staðar og skráist ekki sem vanskil. Hún þýðir einfaldlega að útgefandinn hleypir þessum söluaðilaflokki ekki í gegn.</p>
<h3>Get ég beðið bankann um að opna fyrir spilavítafærslur?</h3>
<p>Þú getur spurt, og sum kortafyrirtæki bjóða stillingar á netbanka fyrir einstaka söluaðilaflokka. Svörin eru misjöfn — en það kostar ekkert að athuga stillingarnar áður en þú leitar annarra leiða.</p>
<h3>Er öruggara að slá kortanúmerið inn á spilavíti en í aðra netverslun?</h3>
<p>Sama öryggislag gildir: dulkóðuð tenging og 3-D Secure sannvottun. Veldu síður með sannreynanlegt leyfi — <a href="{URL_BASE}spilaviti/">yfirlitið okkar</a> birtir rekstrarfélag hverrar síðu — og notaðu aldrei kort annarra; það brýtur skilmála og frystir reikninginn.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Sjá greiðsluleiðir Slotoro →</a></div>
"""

BODIES["greidslur/mastercard-i-spilavitum"] = """
<p>Mastercard og Visa eru oft nefnd í sömu andrá, en á spilavítum hegða kerfin sér ekki eins. Mastercard hefur í gegnum tíðina verið strangara gagnvart netspilun — og fyrir íslenska leikmenn bætist sá munur ofan á afstöðu bankans sem gaf kortið út.</p>

<h2>Munurinn á Mastercard og Visa í þessum geira</h2>
<p>Bæði kerfi merkja fjárhættuspilafærslur með sama MCC-kóða, 7995. Munurinn liggur í tvennu. Annars vegar hafnar Mastercard-kerfið sjálft netspilunarfærslum frá sumum löndum án tillits til bankans. Hins vegar er endurgreiðsla vinninga inn á kort — sem Visa styður víða gegnum OCT-færslur — þrengri hjá Mastercard, svo úttekt á Mastercard er sjaldgæfari í boði hjá erlendum síðum. Niðurstaðan fyrir íslenskan leikmann: Mastercard er fyrst og fremst innlagnarleið, og ekki alltaf sú.</p>

<h2>Prófun í réttri röð</h2>
<ol>
<li>Athugaðu í netbanka hvort kortið þitt leyfi erlenda netverslun og hvort hægt sé að stilla söluaðilaflokka.</li>
<li>Veldu spilavíti sem sýnir Mastercard-merkið í innlagnarglugga — ekki bara á forsíðu.</li>
<li>Prófaðu lága upphæð fyrst og hafðu símann við höndina fyrir sannvottun bankans.</li>
<li>Gangi innlögnin: spurðu þjónustuna strax hvort úttekt á sama kort sé möguleg. Ef ekki, settu upp úttektarleið — rafmynt eða millifærslu — áður en þú spilar.</li>
</ol>

<h2>Debetkort: aukaatriði sem skiptir máli</h2>
<p>Íslensk debetkort eru flest Mastercard eða Maestro. Debetfærsla tekur peninginn beint af reikningnum, og þegar spilavítafærsla festist í biðstöðu — sem gerist við hafnanir — getur upphæðin verið frátekin dögum saman þó færslan gangi aldrei í gegn. Kreditkort einangrar þig frá þessu; biðstaða á kreditheimild snertir ekki launareikninginn þinn.</p>

<h2>Þegar kortaleiðin lokast</h2>
<p>Sama lausn og við <a href="{URL_BASE}greidslur/visa-i-spilavitum/">Visa-hindrunum</a>: færslur sem fara ekki gegnum kortakerfið. <a href="{URL_BASE}greidslur/bitcoin/">Bitcoin</a> og <a href="{URL_BASE}greidslur/ethereum/">Ethereum</a> eru opin öllum; kaup á rafmynt hjá kauphöll er venjuleg fjárfestingarfærsla sem bankar hafna ekki. Yfirlit allra leiða er á <a href="{URL_BASE}greidslur/">greiðslusíðunni</a>.</p>

<h2>Algengar spurningar</h2>
<h3>Virkar fyrirframgreitt Mastercard-gjafakort?</h3>
<p>Nær aldrei. Fyrirframgreidd kort án nafns standast ekki auðkenniskröfur spilavítanna og eru að auki oft lokuð fyrir erlendum færslum. Spilavítið þarf að geta tengt greiðsluleið við skráðan eiganda reikningsins.</p>
<h3>Af hverju sé ég „pending" færslu sem spilavítið segist ekki hafa fengið?</h3>
<p>Höfnunarferlið gengur í tveimur skrefum: heimildin var tekin frá en uppgjörið gekk til baka. Fráteknar upphæðir losna sjálfkrafa, oftast innan 5–10 virkra daga. Spilavítið fékk aldrei peninginn — biðstaðan er milli kortakerfisins og bankans þíns.</p>
<h3>Telur kortainnlögn öðruvísi í bónusveltu en rafmynt?</h3>
<p>Hjá flestum síðum nei, en sumir bónusar eru bundnir við tilteknar greiðsluleiðir — rafræn veski eru stundum undanskilin velkomstbónus. Skilmálar hvers bónuss gilda; sjá <a href="{URL_BASE}bonusar/">bónusyfirlitið</a>.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Innlagnarleiðir Slotoro →</a></div>
"""

BODIES["greidslur/apple-pay-i-spilavitum"] = """
<p>Apple Pay á spilavíti er ekki sjálfstæð greiðsluleið heldur umbúðir: undir liggur alltaf kortið sem þú skráðir í Wallet. Það breytir samt þrennu sem skiptir spilara máli — öryggi, hraða og því hvaða upplýsingar síðan fær um þig.</p>

<h2>Hvað gerist þegar þú borgar með Apple Pay</h2>
<p>iPhone sendir ekki kortanúmerið þitt. Í staðinn fer einnota tókn (token) til söluaðilans ásamt staðfestingu úr Face ID eða Touch ID. Spilavítið sér aldrei sextán stafa númerið og getur því hvorki geymt það né lekið því. Þetta er raunverulegur öryggisávinningur umfram að slá kortið inn í greiðsluglugga.</p>

<h2>En kemst færslan í gegn?</h2>
<p>Hér er gildran: tóknið vísar á kortið þitt, og færslan ber áfram fjárhættuspilakóðann 7995. Ákvörðunin um höfnun liggur hjá kortaútgefandanum — sama hvort færslan kom um Apple Pay eða beint. Apple Pay leysir sem sagt öryggið og þægindin, <strong>ekki</strong> höfnunarvandann sem lýst er í <a href="{URL_BASE}greidslur/visa-i-spilavitum/">Visa-umfjölluninni</a>. Íslensku bankarnir styðja allir Apple Pay, en afstaða þeirra til 7995-færslna fylgir kortinu, ekki símanum.</p>

<h2>Hvar finnurðu Apple Pay í boði</h2>
<p>Stuðningurinn er enn ójafn. Síður með evrópsk leyfi og hefðbundnar kortagreiðslur bjóða hann helst; hreinar rafmyntasíður sleppa honum oft alveg. Í innlagnarglugganum birtist Apple Pay aðeins þegar þú opnar síðuna í Safari á Apple-tæki — athugaðu því í símanum áður en þú ályktar að síða styðji hann ekki.</p>

<h2>Styrkleikar og takmarkanir í stuttu máli</h2>
<table>
<tr><th></th><th>Apple Pay</th></tr>
<tr><td>Innlögn</td><td>Já, þar sem boðið — á sekúndum</td></tr>
<tr><td>Úttekt</td><td>Nei — veldu aðra leið út fyrirfram</td></tr>
<tr><td>Kortanúmer deilt með síðunni</td><td>Aldrei</td></tr>
<tr><td>Höfnunaráhætta íslenskra korta</td><td>Óbreytt frá kortinu sjálfu</td></tr>
<tr><td>Gjöld frá Apple</td><td>Engin</td></tr>
</table>

<h2>Algengar spurningar</h2>
<h3>Af hverju sést Apple Pay ekki í innlagnarglugganum mínum?</h3>
<p>Þrjár algengustu skýringarnar: þú ert ekki í Safari á Apple-tæki, ekkert kort er virkt í Wallet, eða síðan býður leiðina aðeins í sumum löndum. Prófaðu í símanum með virkt kort áður en þú afskrifar síðuna.</p>
<h3>Tekur spilavítið Apple Pay út?</h3>
<p>Nei. Apple Pay er hannað fyrir greiðslur inn, ekki endurgreiðslur út. Vinningar fara aðrar leiðir — millifærsla, rafræn veski eða <a href="{URL_BASE}greidslur/bitcoin/">rafmynt</a>. Settu úttektarleiðina upp strax við skráningu.</p>
<h3>Er Google Pay það sama?</h3>
<p>Sama grundvallartækni — tóknun í stað kortanúmers — og sama niðurstaða gagnvart bankahöfnunum. Android-notendur fá sambærilegt öryggi með Google Pay þar sem síður bjóða það.</p>
<div class="cta-box"><a href="https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/" target="_blank" rel="sponsored noopener" class="cta-btn">Opna Slotoro í símanum →</a></div>
"""
