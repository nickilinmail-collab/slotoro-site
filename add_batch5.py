#!/usr/bin/env python3
"""Batch 5: e-wallets, providers, slots, privacy, statistics, game rules."""

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
    "skrill-leidbeining-island",
    "Skrill á Íslandi — leiðbeining fyrir spilavítagreiðslur 2026",
    "Hvernig á að nota Skrill frá Íslandi: opna reikning, leggja inn, gjöld, úttektir og hvers vegna bankinn sér ekki spilavítið.",
    "💼", ("#28140a", "#452414", "#62341e"),
    f'''<p>Skrill er rafrænt veski sem virkar sem <strong>milliliður milli bankans þíns og spilavítisins</strong>. Fyrir íslenska spilara er það ein af fáum leiðum sem virka áreiðanlega án dulritunargjaldmiðla.</p>

<h2>Af hverju Skrill virkar frá Íslandi</h2>
<p>Þegar þú millifærir af íslenskum bankareikningi á Skrill sér bankinn aðeins færslu til <em>Skrill</em> — greiðsluþjónustu sem er fullkomlega lögleg og algeng. Bankinn sér ekki spilavítið.</p>
<p>Þetta er sama ástæða og gerir <a href="{U}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut</a> að góðum valkosti: milliliðurinn brýtur beina tenginguna milli bankans og spilavítisins.</p>

<h2>Skref fyrir skref</h2>
<ol>
<li><strong>Stofnaðu Skrill reikning</strong> — skrill.com, tekur 3–5 mínútur</li>
<li><strong>Staðfestu reikninginn (KYC)</strong> — Skilríki og sönnun á heimilisfangi. Gerðu þetta strax, ekki bíða</li>
<li><strong>Leggðu inn á Skrill</strong> — Bankamillifærsla (SEPA, ódýrast) eða kort (samstundis, hærra gjald)</li>
<li><strong>Veldu Skrill á spilavítinu</strong> — Sláðu inn netfangið þitt á Skrill og staðfestu</li>
<li><strong>Taktu út á sama hátt</strong> — Vinningar fara til baka á Skrill og þaðan á bankann</li>
</ol>

<h2>Gjöld</h2>
<table class="info-table"><thead><tr><th>Aðgerð</th><th>Gjald</th></tr></thead><tbody>
<tr><td>Innlögn með bankamillifærslu</td><td>Yfirleitt ókeypis</td></tr>
<tr><td>Innlögn með korti</td><td>1–2,5%</td></tr>
<tr><td>Greiðsla til spilavítis</td><td>Yfirleitt ókeypis</td></tr>
<tr><td>Úttekt á bankareikning</td><td>Fast gjald (um €5,50)</td></tr>
<tr><td>Gjaldmiðlaskipti</td><td>3,99% álag</td></tr>
<tr><td>Óvirkni (12+ mánuðir)</td><td>€5 á mánuði</td></tr>
</tbody></table>
<div class="info-box"><p><strong>Varúð við gjaldmiðlaskiptum:</strong> 3,99% álag Skrill er hátt. Ef þú heldur jafnvæginu í EUR (í stað þess að skipta fram og til baka úr ISK) sparar þú verulega. Sjá <a href="{U}leidbeiningar/gjaldmidlaskipti-isk-eur-spilaviti/">gjaldmiðlaskipti fyrir spilavíti →</a></p></div>

<h2>Mikilvægt: Skrill og bónusar</h2>
<p>Mörg spilavíti <strong>útiloka Skrill og Neteller frá velkomstbónusum</strong>. Þú leggur inn, færð engan bónus og kemst að því eftir á.</p>
<p>Lestu bónusskilmálana áður en þú leggur inn. Ef Skrill er útilokað og þú vilt bónusinn skaltu nota kort eða dulritunargjaldmiðil í fyrstu innborgun.</p>

<h2>Skrill vs Neteller vs Revolut</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Skrill</th><th>Neteller</th><th>Revolut</th></tr></thead><tbody>
<tr><td>Útbreiðsla á spilavítum</td><td>Mjög góð</td><td>Mjög góð</td><td>Sem kort</td></tr>
<tr><td>Gjaldmiðlaskipti</td><td>3,99%</td><td>3,99%</td><td>0% (virkir dagar)</td></tr>
<tr><td>Úttektargjald</td><td>~€5,50</td><td>~€5,50</td><td>Ókeypis</td></tr>
<tr><td>Útilokaður frá bónus?</td><td>Oft</td><td>Oft</td><td>Sjaldan (telst kort)</td></tr>
<tr><td>Úttekt frá spilavíti</td><td>✅ Já</td><td>✅ Já</td><td>⚠️ Fer eftir spilavíti</td></tr>
</tbody></table>
<p>Skrill og Neteller eru í eigu sama fyrirtækis (Paysafe) og virka nánast eins.</p>

<h2>Hverjum hentar Skrill?</h2>
<ul>
<li>✅ Þeim sem vilja áreiðanlega leið í <strong>báðar áttir</strong> án dulritunargjaldmiðla</li>
<li>✅ Þeim sem spila á mörgum spilavítum — eitt veski fyrir allt</li>
<li>❌ Ekki þeim sem vilja velkomstbónus (oft útilokað)</li>
<li>❌ Ekki þeim sem leggja inn sjaldan (óvirknigjald)</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Er Skrill öruggt?</h3>
<p>Já — Skrill er hluti af Paysafe Group, skráð fyrirtæki með leyfi frá breska fjármálaeftirlitinu (FCA).</p>
<h3>Hversu hratt er úttekt frá spilavíti á Skrill?</h3>
<p>Yfirleitt 0–48 klst eftir að spilavítið samþykkir hana. Mun hraðara en kort (1–5 dagar).</p>
<h3>Get ég notað Skrill án bankareiknings?</h3>
<p>Þú getur lagt inn með korti, en til að taka peninga út í raunheima þarftu bankareikning.</p>''',
    "Sjá greiðsluleiðir →"))

P.append(page(
    "hacksaw-gaming-leikir",
    "Hacksaw Gaming — leikir, RTP og sérkenni 2026",
    "Hacksaw Gaming: Wanted Dead or a Wild, Le Bandit, Chaos Crew. Nýi framleiðandinn sem breytti spilakassamarkaðnum.",
    "🪚", ("#1a140a", "#332814", "#4d3c1e"),
    f'''<p>Hacksaw Gaming er sænskur framleiðandi sem stofnaður var 2018 og hefur á örfáum árum orðið einn sá vinsælasti í bransanum. <strong>Þekktur fyrir hráan stíl, hásveifluleiki og „Scratch Cards" sem endurvöktu þann flokk.</strong></p>

<h2>Um Hacksaw Gaming</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2018</td></tr>
<tr><td>Höfuðstöðvar</td><td>Malta / Svíþjóð</td></tr>
<tr><td>Fjöldi leikja</td><td>100+</td></tr>
<tr><td>Þekktustu leikir</td><td>Wanted Dead or a Wild, Le Bandit, Chaos Crew, Hand of Anubis</td></tr>
<tr><td>Sérkenni</td><td>Hásveifla, teiknimyndastíll, Bónus Buy, skraflóð</td></tr>
<tr><td>Dæmigert RTP</td><td>96,0–96,3%</td></tr>
</tbody></table>

<h2>Vinsælustu Hacksaw leikirnir</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>RTP</th><th>Sveifla</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td><a href="{U}spilakassar/wanted-dead-or-a-wild/">Wanted Dead or a Wild</a></td><td>96,38%</td><td>Öfgakennd</td><td>12.500x</td></tr>
<tr><td><a href="{U}spilakassar/le-bandit/">Le Bandit</a></td><td>96,30%</td><td>Mjög há</td><td>10.000x</td></tr>
<tr><td><a href="{U}spilakassar/chaos-crew/">Chaos Crew</a></td><td>96,30%</td><td>Mjög há</td><td>10.000x</td></tr>
<tr><td><a href="{U}spilakassar/chaos-crew-2/">Chaos Crew 2</a></td><td>96,27%</td><td>Öfgakennd</td><td>25.000x</td></tr>
<tr><td><a href="{U}spilakassar/hand-of-anubis/">Hand of Anubis</a></td><td>96,22%</td><td>Mjög há</td><td>10.000x</td></tr>
<tr><td><a href="{U}spilakassar/le-pharaoh/">Le Pharaoh</a></td><td>96,25%</td><td>Há</td><td>5.000x</td></tr>
<tr><td><a href="{U}spilakassar/cash-bonanza/">Cash Bonanza</a></td><td>96,20%</td><td>Há</td><td>7.500x</td></tr>
<tr><td><a href="{U}spilakassar/stack-em/">Stack'em</a></td><td>96,27%</td><td>Mjög há</td><td>25.000x</td></tr>
</tbody></table>

<h2>Wanted Dead or a Wild — flaggskipið</h2>
<p>Þessi leikur gerði Hacksaw frægt. Þrjár ólíkar bónusumferðir:</p>
<ul>
<li><strong>Dead</strong> — Sticky wilds sem safnast upp</li>
<li><strong>Wanted</strong> — Margfaldarar sem leggjast saman</li>
<li><strong>Wild</strong> — Duel-umferð með stigvaxandi margföldurum</li>
</ul>
<p>Hámarksvinningur er 12.500x — en sveiflan er öfgakennd. Það er algengt að fara 400+ snúninga án umtalsverðs vinnings.</p>

<h2>Skraflóð (Scratch Cards)</h2>
<p>Hacksaw endurvakti skraflóðaflokkinn með leikjum eins og Dork Unit og Rocket Blast. Þessir leikir eru einfaldir — þú „skrapar" og sérð strax hvort þú vannst — en hafa sömu háu sveifluna og spilakassarnir þeirra.</p>
<p><a href="{U}spilaviti/skraplod-spilaviti/">Spilavíti með skraflóðum →</a></p>

<h2>Hacksaw vs Nolimit City</h2>
<p>Báðir framleiðendur eru þekktir fyrir öfgakennda sveiflu, en nálgunin er ólík:</p>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Hacksaw</th><th>Nolimit City</th></tr></thead><tbody>
<tr><td>Stíll</td><td>Teiknimynda-, litríkur</td><td>Dökkur, óþægilegur</td></tr>
<tr><td>Vélbúnaður</td><td>Einfaldari, hraðari</td><td>Flókinn (xWays, xNudge)</td></tr>
<tr><td>Hámarksvinningar</td><td>5.000x–25.000x</td><td>Allt að 300.000x</td></tr>
<tr><td>Aðgengi byrjenda</td><td>Betra</td><td>Erfiðara</td></tr>
</tbody></table>
<p><a href="{U}leidbeiningar/nolimit-city-hasveifluleikir/">Nolimit City yfirlit →</a></p>

<h2>Ráð fyrir Hacksaw leiki</h2>
<ul>
<li><strong>Lækkaðu veðmálsstærðina</strong> — Með öfgakenndri sveiflu þarftu 300–500 snúninga til að upplifa leikinn almennilega</li>
<li><strong>Prófaðu í demo fyrst</strong> — Sjáðu hversu langt fjármagnið endist áður en þú veðjar raunverulega</li>
<li><strong>Bónus Buy með varúð</strong> — Flestir Hacksaw leikir bjóða það, en kostnaðurinn er oft 100x+ veðmálið</li>
</ul>
<p>Sjá: <a href="{U}leidbeiningar/hvad-er-sveifla/">hvað er sveifla →</a> · <a href="{U}leidbeiningar/bankastjornunaradferdir/">bankastjórnun →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hvar get ég spilað Hacksaw á Íslandi?</h3>
<p><a href="{U}spilaviti/slotoro/">Slotoro</a> og <a href="{U}spilaviti/bitstarz/">BitStarz</a> bjóða báðir Hacksaw safnið.</p>
<h3>Er Hacksaw með lágt RTP?</h3>
<p>Nei — um 96%, staðlað. Það er sveiflan sem er öfgakennd, ekki RTP.</p>
<h3>Hvaða Hacksaw leikur hentar byrjendum?</h3>
<p>Le Pharaoh eða Cash Bonanza — enn há sveifla en mun vægari en Chaos Crew eða Wanted Dead or a Wild.</p>''',
    "Spila Hacksaw leiki →"))

P.append(page(
    "push-gaming-leikir",
    "Push Gaming — Razor Shark, Jammin' Jars og RTP 2026",
    "Push Gaming leikjaframleiðandi: Razor Shark, Jammin' Jars, Fat Banker. RTP tafla, sérkenni og hvar á að spila.",
    "🔱", ("#0a1a28", "#143045", "#1e4662"),
    f'''<p>Push Gaming er breskur framleiðandi sem gerir <strong>vandaða hásveifluleiki með sterkri grafík</strong>. Razor Shark og Jammin' Jars eru meðal mest spiluðu spilakassa í Evrópu.</p>

<h2>Um Push Gaming</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>2010</td></tr>
<tr><td>Höfuðstöðvar</td><td>London, Bretland</td></tr>
<tr><td>Fjöldi leikja</td><td>60+</td></tr>
<tr><td>Þekktustu leikir</td><td>Razor Shark, Jammin' Jars, Fat Banker, Mystery Museum</td></tr>
<tr><td>Sérkenni</td><td>Há RTP (oft 96,5%+), Cluster Pays, margfaldarar</td></tr>
</tbody></table>

<h2>Bestu Push Gaming leikirnir</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>RTP</th><th>Sveifla</th><th>Hámarksvinningur</th></tr></thead><tbody>
<tr><td><a href="{U}spilakassar/jammin-jars/">Jammin' Jars</a></td><td>96,83%</td><td>Há</td><td>20.000x</td></tr>
<tr><td><a href="{U}spilakassar/razor-shark/">Razor Shark</a></td><td>96,70%</td><td>Mjög há</td><td>50.000x</td></tr>
<tr><td><a href="{U}spilakassar/razor-returns/">Razor Returns</a></td><td>96,98%</td><td>Mjög há</td><td>50.000x</td></tr>
<tr><td><a href="{U}spilakassar/jammin-jars-2/">Jammin' Jars 2</a></td><td>96,40%</td><td>Há</td><td>50.000x</td></tr>
<tr><td><a href="{U}spilakassar/fat-banker/">Fat Banker</a></td><td>96,45%</td><td>Mjög há</td><td>42.000x</td></tr>
<tr><td><a href="{U}spilakassar/fat-rabbit/">Fat Rabbit</a></td><td>96,45%</td><td>Há</td><td>4.000x</td></tr>
<tr><td><a href="{U}spilakassar/fat-santa/">Fat Santa</a></td><td>96,45%</td><td>Há</td><td>5.000x</td></tr>
</tbody></table>
<p>Taktu eftir: Push Gaming leikir hafa yfirleitt <strong>hærra RTP en meðaltalið</strong> (96,4–96,98% á móti 96% meðaltali). Sjá <a href="{U}leidbeiningar/bestu-spilakassarnir-haesta-rtp/">topp 20 spilakassar eftir RTP →</a></p>

<h2>Razor Shark — Mystery Stacks</h2>
<p>Razor Shark er þekktastur fyrir „Nudge and Mystery Stack" vélbúnaðinn: dularfullir staflar opnast og geta innihaldið hvaða tákn sem er. Í frísnúningum safnast margfaldari sem endurstillist ekki — hann getur náð mjög háum gildum.</p>
<p>Hámarksvinningur er 50.000x sem er meðal þess hæsta í bransanum. Sveiflan er samsvarandi.</p>

<h2>Jammin' Jars — Cluster Pays og Rainbow Jars</h2>
<p>Jammin' Jars notar 8×8 grind með Cluster Pays (8+ eins tákn hvar sem er). Wild-krukkur færast um borðið og margfaldarinn þeirra hækkar við hvern vinning.</p>
<p>Með 96,83% RTP er þetta einn af hæstu RTP-leikjum sem almennt eru í boði.</p>

<h2>Push Gaming vs aðrir framleiðendur</h2>
<table class="info-table"><thead><tr><th>Framleiðandi</th><th>Dæmigert RTP</th><th>Sveifla</th><th>Styrkleiki</th></tr></thead><tbody>
<tr><td>Push Gaming</td><td>96,4–97,0%</td><td>Há</td><td>Hátt RTP + vönduð grafík</td></tr>
<tr><td><a href="{U}leidbeiningar/pragmatic-play-allir-leikir/">Pragmatic Play</a></td><td>96,0–96,7%</td><td>Meðal–há</td><td>Magn og Drops &amp; Wins</td></tr>
<tr><td><a href="{U}leidbeiningar/playn-go-bestu-spilakassarnir/">Play'n GO</a></td><td>96,2–96,6%</td><td>Há</td><td>Klassísk hönnun</td></tr>
<tr><td><a href="{U}leidbeiningar/netent-saga-og-bestu-leikir/">NetEnt</a></td><td>96,0–98,0%</td><td>Lág–há</td><td>Gæði og fjölbreytni</td></tr>
<tr><td><a href="{U}leidbeiningar/nolimit-city-hasveifluleikir/">Nolimit City</a></td><td>96,0–96,1%</td><td>Öfgakennd</td><td>Hámarksvinningar</td></tr>
</tbody></table>

<h2>Algengar spurningar</h2>
<h3>Hvaða Push Gaming leikur hefur hæsta RTP?</h3>
<p>Razor Returns með 96,98% — nánast 97%, sem er hátt fyrir hásveifluleik.</p>
<h3>Er Razor Shark of sveiflukenndur fyrir byrjendur?</h3>
<p>Já, frekar. Byrjaðu á Fat Rabbit eða <a href="{U}spilakassar/jammin-jars/">Jammin' Jars</a> sem eru vægari.</p>
<h3>Hvar get ég spilað Push Gaming á Íslandi?</h3>
<p><a href="{U}spilaviti/slotoro/">Slotoro</a> og <a href="{U}spilaviti/bitstarz/">BitStarz</a> bjóða báðir Push Gaming safnið.</p>''',
    "Spila Push Gaming →"))

P.append(page(
    "big-bass-bonanza-leidarvisir",
    "Big Bass Bonanza — leiðarvísir, RTP og öll afbrigði 2026",
    "Big Bass Bonanza serían frá Pragmatic Play: RTP 96,71%, fiskitákn og margfaldarar. Samanburður á öllum útgáfum.",
    "🎣", ("#0a1a28", "#143045", "#1e4662"),
    f'''<p>Big Bass Bonanza er ein vinsælasta spilakassasería í heimi. <strong>RTP 96,71% — eitt það hæsta hjá Pragmatic Play — og einfaldur vélbúnaður sem allir skilja strax.</strong></p>

<h2>Tæknilegar upplýsingar (upprunalega útgáfan)</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Gildi</th></tr></thead><tbody>
<tr><td>Framleiðandi</td><td>Pragmatic Play / Reel Kingdom</td></tr>
<tr><td>Útgáfuár</td><td>2020</td></tr>
<tr><td>RTP</td><td>96,71%</td></tr>
<tr><td>Sveifla</td><td>Há</td></tr>
<tr><td>Hámarksvinningur</td><td>2.100x veðmál</td></tr>
<tr><td>Hjól / línur</td><td>5 hjól, 3 raðir, 10 línur</td></tr>
<tr><td>Frísnúningar</td><td>10 við 3 scatter</td></tr>
<tr><td>Bónus Buy</td><td>✅ Já (um 100x)</td></tr>
</tbody></table>

<h2>Hvernig leikurinn virkar</h2>
<h3>Fiskimaðurinn og fiskarnir</h3>
<p>Kjarninn er einfaldur: í frísnúningum er fiskimaðurinn wild-tákn. Þegar hann birtist safnar hann öllum fiskatáknum á skjánum og þú færð verðmæti þeirra (allt að 10x veðmálið á hvern fisk).</p>

<h3>Margfaldari sem vex</h3>
<p>Í frísnúningum eykst margfaldarinn eftir því hversu oft fiskimaðurinn birtist:</p>
<ul>
<li>4 fiskimenn → 2x margfaldari + 10 frísnúningar í viðbót</li>
<li>8 fiskimenn → 3x margfaldari + 10 frísnúningar</li>
<li>12 fiskimenn → 10x margfaldari + 10 frísnúningar</li>
</ul>
<p>Að ná 10x margfaldaranum er þar sem stóru vinningarnir gerast.</p>

<h2>Öll afbrigði seríunnar</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>RTP</th><th>Hámarksvinningur</th><th>Sérkenni</th></tr></thead><tbody>
<tr><td><a href="{U}spilakassar/big-bass-bonanza/">Big Bass Bonanza</a></td><td>96,71%</td><td>2.100x</td><td>Upprunalega</td></tr>
<tr><td><a href="{U}spilakassar/bigger-bass-bonanza/">Bigger Bass Bonanza</a></td><td>96,71%</td><td>4.000x</td><td>Stærri grind (4 raðir)</td></tr>
<tr><td><a href="{U}spilakassar/big-bass-splash/">Big Bass Splash</a></td><td>95,67%</td><td>5.000x</td><td>Val um frísnúningaham</td></tr>
<tr><td><a href="{U}spilakassar/big-bass-bonanza-megaways/">Big Bass Bonanza Megaways</a></td><td>95,67%</td><td>5.000x</td><td>Megaways vélbúnaður</td></tr>
<tr><td><a href="{U}spilakassar/big-bass-amazon/">Big Bass Amazon Xtreme</a></td><td>96,71%</td><td>5.000x</td><td>Xtreme margfaldarar</td></tr>
<tr><td><a href="{U}spilakassar/big-bass-keeping-it-reel/">Big Bass Keeping it Reel</a></td><td>96,71%</td><td>5.000x</td><td>Mystery tákn</td></tr>
</tbody></table>
<div class="info-box"><p><strong>Athugið:</strong> Big Bass Splash og Megaways útgáfurnar hafa <strong>lægra RTP (95,67%)</strong> en upprunalega. Ef RTP skiptir þig máli skaltu halda þig við upprunalegu útgáfuna eða Bigger Bass Bonanza.</p></div>

<h2>Af hverju er serían svona vinsæl?</h2>
<ul>
<li><strong>Auðskiljanlegt</strong> — Fiskimaðurinn safnar fiskum. Enginn þarf að lesa reglur</li>
<li><strong>Hátt RTP</strong> — 96,71% er yfir meðaltali. Sjá <a href="{U}leidbeiningar/bestu-spilakassarnir-haesta-rtp/">RTP samanburð →</a></li>
<li><strong>Skýr framvinda</strong> — Þú sérð margfaldarann vaxa, sem heldur spennu uppi</li>
<li><strong>Algengt í bónustilboðum</strong> — Mörg spilavíti nota Big Bass í <a href="{U}leidbeiningar/okeypis-snuningar-spilaviti/">frísnúningatilboðum</a></li>
</ul>

<h2>Ráð</h2>
<ul>
<li><strong>Veldu upprunalegu eða Bigger</strong> — Betra RTP en Splash/Megaways útgáfurnar</li>
<li><strong>Reiknaðu fyrir 200+ snúninga</strong> — Há sveifla, frísnúningar koma að meðaltali á 180–250 snúninga fresti</li>
<li><strong>Bónus Buy</strong> — Um 100x veðmálið. Fer beint í frísnúninga en kostnaðurinn er hár. <a href="{U}leidbeiningar/bonus-buy-spilakassar/">Er Bónus Buy þess virði? →</a></li>
<li><strong>Athugaðu RTP-útgáfuna</strong> — Spilavíti geta keyrt lægri stillingu. Athugaðu í leikjareglum</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Hvaða Big Bass leikur er bestur?</h3>
<p>Upprunalega Big Bass Bonanza fyrir RTP (96,71%), Bigger Bass Bonanza ef þú vilt hærri hámarksvinning með sama RTP.</p>
<h3>Hvað er hámarksvinningur?</h3>
<p>2.100x í upprunalegu útgáfunni, allt að 5.000x í nýrri afbrigðum.</p>
<h3>Er hægt að spila ókeypis?</h3>
<p>Já — <a href="{U}spilakassar/big-bass-bonanza/">prófaðu Big Bass Bonanza í demo</a> án skráningar.</p>''',
    "Spila Big Bass Bonanza →"))

P.append(page(
    "mega-moolah-pottavinningur",
    "Mega Moolah — stærsti pottur netheima 2026",
    "Mega Moolah: stigvaxandi pottur sem hefur greitt yfir 20 milljónir evra. Hvernig potturinn virkar, RTP og líkur.",
    "🦁", ("#281a0a", "#453014", "#62461e"),
    f'''<p>Mega Moolah er frægasti stigvaxandi pottur í sögu netspilavíta. <strong>Hann hefur greitt út margar af stærstu vinningum sem skráðir hafa verið á netinu — þar á meðal yfir 18 milljónir evra í einni greiðslu.</strong></p>

<h2>Tæknilegar upplýsingar</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Gildi</th></tr></thead><tbody>
<tr><td>Framleiðandi</td><td>Microgaming / Games Global</td></tr>
<tr><td>Útgáfuár</td><td>2006</td></tr>
<tr><td>RTP</td><td>88,12% (grunnleikur) — 93–96% með potti</td></tr>
<tr><td>Sveifla</td><td>Mjög há</td></tr>
<tr><td>Hjól / línur</td><td>5 hjól, 3 raðir, 25 línur</td></tr>
<tr><td>Lágmarksveðmál</td><td>€0,25</td></tr>
<tr><td>Pottar</td><td>4 (Mini, Minor, Major, Mega)</td></tr>
<tr><td>Lágmarks Mega pottur</td><td>€1.000.000</td></tr>
</tbody></table>

<h2>Potturinn fjórfaldi</h2>
<table class="info-table"><thead><tr><th>Pottur</th><th>Dæmigert verðmæti</th><th>Tíðni</th></tr></thead><tbody>
<tr><td>Mini</td><td>~€10</td><td>Oft</td></tr>
<tr><td>Minor</td><td>~€100</td><td>Reglulega</td></tr>
<tr><td>Major</td><td>~€10.000</td><td>Sjaldan</td></tr>
<tr><td>Mega</td><td>€1.000.000+</td><td>Mjög sjaldan</td></tr>
</tbody></table>
<p>Þegar Mega potturinn er unninn endurstillist hann í €1 milljón og byrjar að vaxa aftur.</p>

<h2>Hvernig potturinn vinnst</h2>
<p>Pottumferðin er <strong>algjörlega handahófskennd</strong> — hún getur kveikt á hvaða snúningi sem er, óháð veðmálsstærð eða því hvort þú vannst í grunnleiknum.</p>
<p>Þegar hún kveikir birtist hjól með 20 reitum skipt milli pottanna fjögurra. Þar sem hjólið stöðvast ræður hvaða pott þú vinnur.</p>
<div class="info-box"><p><strong>Mikilvægt:</strong> Hærra veðmál eykur <em>líkurnar</em> á að pottumferðin kvikni — en tryggir hana ekki. Þú getur unnið Mega pottinn á lágmarksveðmáli, þó líkurnar séu minni.</p></div>

<h2>RTP — lestu þetta áður en þú spilar</h2>
<p>Hér er það sem margir átta sig ekki á: <strong>grunnleikur Mega Moolah hefur aðeins 88,12% RTP.</strong> Það er langt undir meðaltalinu (um 96%).</p>
<p>Ástæðan: hluti af hverju veðmáli fer í pottinn í stað þess að greiðast út í venjulegum vinningum. Heildar-RTP (með pottinum talið) fer í 93–96%, en sá hluti rennur til eins heppins spilara — ekki þín.</p>
<p>Í reynd þýðir þetta: ef þú spilar Mega Moolah og vinnur ekki pottinn tapar þú hraðar en í venjulegum spilakassa.</p>
<p><a href="{U}leidbeiningar/hvad-er-rtp/">Ítarlegt um RTP →</a> · <a href="{U}leidbeiningar/bestu-spilakassarnir-haesta-rtp/">spilakassar með hæsta RTP →</a></p>

<h2>Líkurnar á Mega pottinum</h2>
<p>Áætlaðar líkur eru um <strong>1 á móti 50 milljónum snúninga</strong>. Til samanburðar: líkurnar á að verða fyrir eldingu á ævinni eru um 1 á móti 15.000.</p>
<p>Það þýðir ekki að það sé ómögulegt — einhver vinnur reglulega. En það þýðir að þú átt ekki að spila Mega Moolah með þá væntingu að vinna hann.</p>

<h2>Serían</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>Þema</th><th>Grunn-RTP</th></tr></thead><tbody>
<tr><td><a href="{U}spilakassar/mega-moolah/">Mega Moolah</a></td><td>Afrískt safarí</td><td>88,12%</td></tr>
<tr><td>Mega Moolah Isis</td><td>Egyptaland</td><td>88,12%</td></tr>
<tr><td>Absolootly Mad Mega Moolah</td><td>Lísa í Undralandi</td><td>88,12%</td></tr>
<tr><td>Atlantean Treasures Mega Moolah</td><td>Neðansjávar</td><td>88,12%</td></tr>
<tr><td>Book of Atem WowPot</td><td>Egyptaland (WowPot net)</td><td>93,04%</td></tr>
</tbody></table>

<h2>Aðrir stórir pottar</h2>
<ul>
<li><a href="{U}spilakassar/mega-fortune/">Mega Fortune</a> (NetEnt) — Lúxusþema, hefur greitt yfir €17 milljónir</li>
<li><a href="{U}spilakassar/divine-fortune/">Divine Fortune</a> (NetEnt) — Minni pottar en mun hærra grunn-RTP (96,59%)</li>
<li><a href="{U}spilakassar/wolf-gold/">Wolf Gold</a> (Pragmatic Play) — Fastir pottar, RTP 96,01%</li>
</ul>
<p><a href="{U}leidbeiningar/stighaekkandi-pottar/">Allt um stigvaxandi potta →</a> · <a href="{U}spilaviti/jackpot-spilaviti/">Pottaspilavíti →</a></p>

<h2>Algengar spurningar</h2>
<h3>Hver er stærsti Mega Moolah vinningurinn?</h3>
<p>Rúmlega €18,9 milljónir árið 2018 — skráð sem einn stærsti netspilavítisvinningur sögunnar.</p>
<h3>Þarf ég að veðja hámarki til að vinna pottinn?</h3>
<p>Nei — potturinn getur kveikt á hvaða veðmálsstærð sem er. En hærra veðmál eykur líkurnar hlutfallslega.</p>
<h3>Er Mega Moolah góður leikur?</h3>
<p>Fyrir draumavinning — já. Fyrir jafna spilun — nei, vegna 88% grunn-RTP. Ef þú vilt spila lengur fyrir sömu upphæð skaltu velja leik með 96%+ RTP.</p>''',
    "Spila pottaleiki →"))

P.append(page(
    "gdpr-og-netspilaviti",
    "GDPR og netspilavíti — hvaða gögn safna þau um þig? 2026",
    "Persónuvernd á netspilavítum: hvaða gögn eru söfnuð, hvaða réttindi þú hefur samkvæmt GDPR og hvernig á að beita þeim.",
    "🔒", ("#0a1420", "#14283c", "#1e3c58"),
    f'''<p>Þegar þú skráir þig á netspilavíti afhendir þú umtalsvert magn persónuupplýsinga. <strong>Sem íslenskur ríkisborgari nýtur þú verndar GDPR — en aðeins gagnvart spilavítum sem starfa innan EES.</strong></p>

<h2>Hvaða gögn safna spilavíti?</h2>
<table class="info-table"><thead><tr><th>Flokkur</th><th>Dæmi</th><th>Af hverju</th></tr></thead><tbody>
<tr><td>Auðkenni</td><td>Nafn, fæðingardagur, kennitala/vegabréf</td><td>Aldursstaðfesting, lagaskylda (KYC)</td></tr>
<tr><td>Samskipti</td><td>Netfang, símanúmer, heimilisfang</td><td>Reikningsstjórnun</td></tr>
<tr><td>Fjárhagur</td><td>Kortaupplýsingar, bankareikningur, færslusaga</td><td>Greiðslur, peningaþvættisvarnir</td></tr>
<tr><td>Hegðun</td><td>Hvaða leiki þú spilar, hversu lengi, veðmálsstærðir</td><td>Markaðssetning, ábyrg spilun</td></tr>
<tr><td>Tækni</td><td>IP-tala, tæki, vafri, staðsetning</td><td>Svikavarnir, landfræðileg takmörk</td></tr>
</tbody></table>

<h2>Réttindi þín samkvæmt GDPR</h2>
<h3>1. Réttur til aðgangs</h3>
<p>Þú getur beðið um afrit af öllum gögnum sem spilavítið geymir um þig. Það verður að svara innan <strong>30 daga</strong> og afhenda gögnin ókeypis.</p>

<h3>2. Réttur til leiðréttingar</h3>
<p>Ef upplýsingar eru rangar getur þú krafist leiðréttingar.</p>

<h3>3. Réttur til eyðingar („rétturinn til að gleymast")</h3>
<p>Þú getur beðið um að gögnum verði eytt — <strong>en með mikilvægum undantekningum</strong>. Spilavíti verða að geyma fjárhagsgögn og KYC-gögn í 5–7 ár vegna peningaþvættislöggjafar. Þau geta því ekki eytt öllu.</p>

<h3>4. Réttur til að andmæla markaðssetningu</h3>
<p>Þú getur hvenær sem er afþakkað markpósta, SMS og símtöl. Þetta má ekki vera háð neinum skilyrðum.</p>

<h3>5. Réttur til gagnaflutnings</h3>
<p>Þú getur fengið gögnin þín á véllæsilegu formi til að flytja annað.</p>

<h2>Hvernig á að beita réttindunum</h2>
<ol>
<li>Finndu persónuverndarstefnu spilavítisins (yfirleitt neðst á síðunni)</li>
<li>Leitaðu að netfangi persónuverndarfulltrúa (DPO) — oft privacy@ eða dpo@</li>
<li>Sendu skriflega beiðni. Tilgreindu nákvæmlega hvað þú vilt (aðgang, eyðingu, andmæli)</li>
<li>Þeir hafa 30 daga til að svara</li>
<li>Ef þeir svara ekki eða neita ólögmætt — kvartaðu til Persónuverndar (personuvernd.is)</li>
</ol>

<h2>Gildir GDPR um öll spilavíti?</h2>
<div class="info-box"><p><strong>Nei.</strong> GDPR gildir um fyrirtæki sem starfa innan EES eða beina þjónustu markvisst að einstaklingum innan EES. Spilavíti með <a href="{U}leidbeiningar/hvada-leyfi-er-best-spilaviti/">Malta (MGA) leyfi</a> falla undir GDPR. Spilavíti með Curaçao leyfi gera það oft ekki formlega.</p></div>
<p>Mörg Curaçao-spilavíti fylgja GDPR-líkum reglum af fúsum vilja, en þú hefur ekki sömu lagalegu úrræði ef þau gera það ekki. Þetta er ein ástæða þess að MGA-leyfi er verðmætara frá sjónarhóli neytendaverndar.</p>

<h2>Hagnýtar ráðleggingar</h2>
<ul>
<li><strong>Notaðu sérstakt netfang</strong> — Aðskildu spilavítasamskipti frá persónulegum pósti</li>
<li><strong>Lestu persónuverndarstefnuna</strong> — Sérstaklega kaflann um deilingu með þriðja aðila</li>
<li><strong>Afþakkaðu markaðssetningu strax</strong> — Gerðu það við skráningu, ekki eftir að póstarnir byrja</li>
<li><strong>Varist ótengd „spilavíti"</strong> — Ef síða biður um kennitölu án skýrrar KYC-ástæðu er það viðvörunarmerki</li>
<li><strong>Athugaðu hvort gögn eru seld</strong> — Sum spilavíti deila gögnum með markaðsaðilum. Þetta á að koma fram í stefnunni</li>
</ul>

<h2>Sérstaklega viðkvæmt: hegðunargögn</h2>
<p>Spilavíti vita nákvæmlega hvenær þú spilar, hversu lengi, hvaða leiki og hversu mikið. Þessi gögn eru notuð bæði til <a href="{U}leidbeiningar/spila-af-abyrgd/">ábyrgrar spilunar</a> (að greina áhættuhegðun) og til markaðssetningar (að senda bónus þegar þú hefur ekki spilað í viku).</p>
<p>Ef þú vilt ekki fá bónustilboð byggð á hegðun þinni — afþakkaðu markaðssetningu. Það er réttur þinn.</p>

<h2>Algengar spurningar</h2>
<h3>Get ég látið eyða reikningnum mínum alveg?</h3>
<p>Þú getur lokað reikningnum, en spilavítið verður að geyma KYC- og fjárhagsgögn í 5–7 ár vegna peningaþvættislöggjafar. Markaðsgögnum og hegðunargögnum má eyða.</p>
<h3>Hvað ef spilavítið svarar ekki beiðni minni?</h3>
<p>Ef það fellur undir GDPR getur þú kvartað til Persónuverndar á Íslandi eða til eftirlitsaðila í landi spilavítisins (t.d. maltneska eftirlitsins fyrir MGA-spilavíti).</p>
<h3>Er öruggt að senda mynd af vegabréfinu?</h3>
<p>Til spilavítis með gilt leyfi — já, það er lagaskylda þeirra að vernda gögnin. Sendu aldrei skilríki í gegnum ódulkóðaðan tölvupóst; notaðu upphleðsluform spilavítisins.</p>''',
    "Sjá spilavíti með MGA leyfi →"))

P.append(page(
    "spilafikn-a-islandi-tolfraedi",
    "Spilafikn á Íslandi — tölfræði og staðreyndir 2026",
    "Hversu algeng er spilafikn á Íslandi? Rannsóknir, áhættuhópar, einkenni og hvar hjálp er að fá. Hjálparsími 1717.",
    "📈", ("#141414", "#282828", "#3c3c3c"),
    f'''<p>Fjárhættuspil eru útbreidd á Íslandi — spilakassar, lottó, getraunir og netspilavíti. <strong>Fyrir langflesta er þetta skaðlaus afþreying. Fyrir lítinn en raunverulegan hóp verður það vandamál.</strong></p>

<h2>Hvað segja rannsóknir?</h2>
<p>Rannsóknir á spilahegðun Íslendinga hafa verið gerðar með reglulegu millibili, meðal annars á vegum stjórnvalda og háskólasamfélagsins. Meginniðurstöður sem ítrekað koma fram:</p>
<ul>
<li>Meirihluti fullorðinna Íslendinga tekur einhvern þátt í fjárhættuspilum árlega — oftast lottó eða getraunum</li>
<li>Hlutfall þeirra sem sýna merki um <strong>vandamálaspilun</strong> er lítið brot af heildinni, í takt við það sem sést á öðrum Norðurlöndum</li>
<li>Spilakassar og hraðir netleikir tengjast hærri tíðni vandamála en lottó eða getraunir</li>
<li>Ungir karlmenn eru stærsti áhættuhópurinn</li>
</ul>
<div class="info-box"><p><strong>Athugasemd um tölur:</strong> Við birtum ekki nákvæmar prósentur hér því niðurstöður eru mismunandi eftir rannsóknaraðferð, ártali og skilgreiningu á „vandamálaspilun". Ef þú þarft nákvæmar tölur mælum við með að leita beint til Embættis landlæknis eða birtra rannsókna á vegum háskólanna.</p></div>

<h2>Af hverju eru hraðir leikir áhættusamari?</h2>
<p>Tíðni og hraði skipta meira máli en upphæðin:</p>
<table class="info-table"><thead><tr><th>Leikjaform</th><th>Tími milli veðmála</th><th>Áhættustig</th></tr></thead><tbody>
<tr><td>Lottó</td><td>Dagar</td><td>Lágt</td></tr>
<tr><td>Getraunir / íþróttaveðmál</td><td>Klukkustundir</td><td>Miðlungs</td></tr>
<tr><td>Spilakassar (staðbundnir)</td><td>Sekúndur</td><td>Hátt</td></tr>
<tr><td>Netspilakassar</td><td>Sekúndur, alltaf í boði</td><td>Hátt</td></tr>
<tr><td>Lifandi spilavíti</td><td>Sekúndur til mínútur</td><td>Hátt</td></tr>
</tbody></table>
<p>Netspilavíti sameina hraða og aðgengi — þau eru opin allan sólarhringinn og í vasanum. Það er bæði þægindi og áhætta.</p>

<h2>Hverjir eru í mestri áhættu?</h2>
<ul>
<li><strong>Ungir karlmenn (18–35 ára)</strong> — Hæsta tíðni í flestum rannsóknum</li>
<li><strong>Þeir sem byrjuðu ungir</strong> — Því fyrr sem spilun hefst, þeim mun meiri áhætta síðar</li>
<li><strong>Fólk með aðrar fíknir</strong> — Áfengi, vímuefni og spilun fara oft saman</li>
<li><strong>Þeir sem glíma við kvíða eða þunglyndi</strong> — Spilun getur orðið flóttaleið</li>
<li><strong>Fólk í fjárhagsvanda</strong> — Von um skyndilausn eykur áhættuhegðun</li>
</ul>

<h2>Hvernig þróast vandamálið?</h2>
<p>Spilafikn þróast yfirleitt í stigum:</p>
<ol>
<li><strong>Vinningsstig</strong> — Snemmbúnir vinningar skapa óraunhæfar væntingar</li>
<li><strong>Tapstig</strong> — Tap eykst, spilarinn byrjar að elta tapið og leyna því</li>
<li><strong>Örvæntingarstig</strong> — Lán, skuldir, sambandsslit, hugsanlega lögbrot</li>
<li><strong>Uppgjöf eða bati</strong> — Annaðhvort dýpkar vandinn eða viðkomandi leitar hjálpar</li>
</ol>
<p>Því fyrr sem gripið er inn í, þeim mun betri eru horfurnar.</p>

<h2>Einkenni — stutt yfirlit</h2>
<ul>
<li>Spilar meira en ætlað var, ítrekað</li>
<li>Eltir tap með stærri veðmálum</li>
<li>Leynir umfangi spilunar fyrir öðrum</li>
<li>Hefur reynt að hætta án árangurs</li>
<li>Notar peninga sem þarf í annað</li>
<li>Pirringur eða eirðarleysi þegar ekki er hægt að spila</li>
</ul>
<p><a href="{U}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">Ítarlegri listi yfir viðvörunarmerki →</a></p>

<h2>Hvar er hjálp að fá á Íslandi?</h2>
<div class="info-box"><p><strong>Hjálparsíminn 1717</strong> — Opinn allan sólarhringinn, alla daga ársins. Ókeypis, nafnlaust ef þú vilt. Einnig fyrir aðstandendur.</p></div>
<div class="info-box"><p><strong>SÁÁ</strong> — Veitir meðferð og ráðgjöf, einnig vegna spilafiknar. saa.is</p></div>
<div class="info-box"><p><strong>Heilsugæslan</strong> — Fyrsti viðkomustaður fyrir tilvísun í sálfræðiþjónustu.</p></div>
<div class="info-box"><p><strong>GA (Gamblers Anonymous)</strong> — Sjálfshjálparhópar, einnig fundir á netinu.</p></div>
<p><a href="{U}leidbeiningar/studningssidur-vid-spilafikn/">Öll stuðningsúrræði →</a> · <a href="{U}leidbeiningar/radleggingar-til-adstandenda-spilafikla/">Ráð til aðstandenda →</a></p>

<h2>Forvarnir — það sem virkar</h2>
<ol>
<li><a href="{U}leidbeiningar/hvernig-a-ad-setja-takmork-a-spilaviti/">Innborgunartakmörk</a> — sett fyrirfram, áður en spilun hefst</li>
<li><a href="{U}leidbeiningar/sjalfsutilokun-spilavita/">Sjálfsútilokun</a> — ef takmörk duga ekki</li>
<li>BetBlocker — ókeypis hugbúnaður sem lokar á spilavítasíður á öllum tækjum</li>
<li>Bankalokun — sumir bankar geta lokað á fjárhættuspilafærslur</li>
<li>Opin umræða — leynd er einkenni vandamálsins, ekki lausn</li>
</ol>

<h2>Algengar spurningar</h2>
<h3>Er spilafikn viðurkennd sem sjúkdómur?</h3>
<p>Já — Alþjóðaheilbrigðismálastofnunin (WHO) flokkar spilaröskun (gambling disorder) sem geðröskun í ICD-11, á sama hátt og vímuefnafíkn.</p>
<h3>Er hægt að ná bata?</h3>
<p>Já. Meðferð, sjálfshjálparhópar og hugræn atferlismeðferð hafa sýnt árangur. Bakslag er algengt í ferlinu og þýðir ekki að meðferð sé árangurslaus.</p>
<h3>Hvað ef ég er ekki viss hvort ég eigi í vanda?</h3>
<p>Hringdu í 1717 og ræddu það. Það kostar ekkert og þú þarft ekki að greina sjálfan þig fyrirfram.</p>''',
    "Sjá ábyrga spilun →"))

P.append(page(
    "sic-bo-reglur-a-islensku",
    "Sic Bo reglur á íslensku — teningaleikurinn útskýrður 2026",
    "Sic Bo reglur á íslensku: veðmálategundir, útborganir, húsforskot og hvaða veðmál borga sig best.",
    "🎲", ("#1a0a14", "#331428", "#4d1e3c"),
    f'''<p>Sic Bo er kínverskur teningaleikur sem hefur verið spilaður í yfir 2.000 ár. <strong>Þrír teningar, eitt kast, tugir veðmálamöguleika.</strong> Hann er einfaldur að spila en húsforskotið er mjög breytilegt eftir því hvað þú veðjar á.</p>

<h2>Grunnreglur</h2>
<ol>
<li>Þrír teningar eru hristir í lokuðum bikar</li>
<li>Þú leggur veðmál á borðið áður en þeir eru opnaðir</li>
<li>Teningarnir eru sýndir</li>
<li>Öll veðmál sem passa eru greidd út</li>
</ol>
<p>Það er allt. Engar ákvarðanir eftir kastið, engin strategía í sjálfum leiknum — aðeins val á veðmálum.</p>

<h2>Veðmálategundir og húsforskot</h2>
<table class="info-table"><thead><tr><th>Veðmál</th><th>Lýsing</th><th>Útborgun</th><th>Húsforskot</th></tr></thead><tbody>
<tr><td><strong>Small</strong></td><td>Samtala 4–10</td><td>1:1</td><td><strong>2,78%</strong></td></tr>
<tr><td><strong>Big</strong></td><td>Samtala 11–17</td><td>1:1</td><td><strong>2,78%</strong></td></tr>
<tr><td>Slétt / Oddatala</td><td>Samtala slétt eða oddatala</td><td>1:1</td><td>2,78%</td></tr>
<tr><td>Ein tala</td><td>Tiltekin tala birtist</td><td>1:1 til 3:1</td><td>7,87%</td></tr>
<tr><td>Tvær tölur</td><td>Tvær tilteknar tölur</td><td>5:1</td><td>16,67%</td></tr>
<tr><td>Samtala (t.d. 10)</td><td>Nákvæm samtala</td><td>6:1 til 60:1</td><td>9,7–15,3%</td></tr>
<tr><td>Þrennt (tiltekið)</td><td>Þrír eins, tiltekin tala</td><td>180:1</td><td>16,2%</td></tr>
<tr><td>Hvaða þrennt sem er</td><td>Þrír eins, hvaða tala</td><td>30:1</td><td>30,1%</td></tr>
</tbody></table>

<h2>Besta veðmálið: Small eða Big</h2>
<div class="info-box"><p><strong>Veðjaðu á Small eða Big.</strong> Þau hafa 2,78% húsforskot — sambærilegt við <a href="{U}leidbeiningar/rullettureglur-a-islensku/">evrópska rúllettu</a> (2,7%). Öll önnur veðmál í Sic Bo hafa verulega hærra húsforskot.</p></div>
<p>„Hvaða þrennt sem er" lítur freistandi út með 30:1 útborgun — en húsforskotið er 30,1%. Það er eitt versta veðmál sem til er í nokkru spilavíti.</p>

<h2>Af hverju Small/Big greiða ekki fyrir þrennt</h2>
<p>Ef þrír eins koma upp (t.d. 3-3-3) tapa bæði Small og Big. Þetta er þar sem húsið fær forskot sitt — annars væru þessi veðmál fullkomlega jöfn 50/50.</p>
<p>Líkurnar á þrennu eru 6/216 = 2,78% — nákvæmlega húsforskotið.</p>

<h2>Sic Bo vs önnur teningaspil</h2>
<table class="info-table"><thead><tr><th>Leikur</th><th>Besta húsforskot</th><th>Flækjustig</th><th>Ákvarðanir eftir kast</th></tr></thead><tbody>
<tr><td>Sic Bo</td><td>2,78%</td><td>Lágt</td><td>Nei</td></tr>
<tr><td>Craps</td><td>1,36% (Don't Pass)</td><td>Hátt</td><td>Já (odds veðmál)</td></tr>
<tr><td><a href="{U}live/lightning-dice/">Lightning Dice</a></td><td>~3,5%</td><td>Mjög lágt</td><td>Nei</td></tr>
</tbody></table>
<p>Craps hefur lægra húsforskot en krefst mun meiri þekkingar. Sic Bo er aðgengilegra fyrir byrjendur.</p>

<h2>Hvar á að spila Sic Bo á Íslandi</h2>
<div class="info-box"><p><strong><a href="{U}live/sic-bo/">Lifandi Sic Bo</a></strong> — Evolution býður lifandi útgáfu með raunverulegum spilastjóra</p></div>
<div class="info-box"><p><strong><a href="{U}live/super-sic-bo/">Super Sic Bo</a></strong> — Útgáfa með handahófskenndum margföldurum allt að 1.000x</p></div>
<div class="info-box"><p><strong><a href="{U}spilaviti/teningaleikja-spilaviti/">Teningaleikjaspilavíti</a></strong> — Yfirlit yfir spilavíti með teningaleikjum</p></div>

<h2>Super Sic Bo — athugaðu útborgunina</h2>
<p>Eins og í <a href="{U}leidbeiningar/lightning-roulette-adferdir/">Lightning Roulette</a> bætir Super Sic Bo við margföldurum — en lækkar grunnútborganir á móti. Heildar-RTP er svipað. Margfaldararnir gilda aðeins um tiltekin veðmál, ekki Small/Big.</p>

<h2>Algengar spurningar</h2>
<h3>Er einhver strategía í Sic Bo?</h3>
<p>Aðeins ein: veðjaðu á Small eða Big og forðist allt annað. Það er engin leið til að hafa áhrif á teningana.</p>
<h3>Hvaða veðmál á ég alls ekki að taka?</h3>
<p>„Hvaða þrennt sem er" (30,1% húsforskot) og „Tvær tölur" (16,67%). Útborgunin lítur vel út en stærðfræðin er hræðileg.</p>
<h3>Er Sic Bo í boði í demo?</h3>
<p>RNG-útgáfur já. Lifandi útgáfur með raunverulegum spilastjóra eru ekki í boði ókeypis.</p>''',
    "Spila Sic Bo →"))

P.append(page(
    "bingo-a-netinu-island",
    "Bingó á netinu á Íslandi — reglur og spilavíti 2026",
    "Bingó á netinu: 90-bolta og 75-bolta reglur, mynstur, RTP og hvaða spilavíti bjóða bingó fyrir íslenska spilara.",
    "🎱", ("#0a1a1a", "#143333", "#1e4d4d"),
    f'''<p>Bingó er félagslegasti leikurinn í netspilavítum — flest bingóherbergi hafa spjall þar sem spilarar tala saman meðan umferðin gengur. <strong>Lágur hraði, lágt veðmál og meira um skemmtun en stóra vinninga.</strong></p>

<h2>Tvö helstu afbrigði</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>90-bolta (evrópskt)</th><th>75-bolta (amerískt)</th></tr></thead><tbody>
<tr><td>Boltar</td><td>1–90</td><td>1–75</td></tr>
<tr><td>Spjald</td><td>9×3, 15 tölur</td><td>5×5, 24 tölur + frír reitur</td></tr>
<tr><td>Vinningar</td><td>1 lína, 2 línur, fullt hús</td><td>Mynstur (form, bókstafir)</td></tr>
<tr><td>Umferðarlengd</td><td>Lengri</td><td>Styttri</td></tr>
<tr><td>Vinsælt í</td><td>Evrópu, Bretlandi</td><td>Norður-Ameríku</td></tr>
</tbody></table>

<h2>90-bolta bingó — reglurnar</h2>
<p>Spjaldið er 9 dálkar × 3 raðir. Hver röð hefur 5 tölur og 4 auða reiti — samtals 15 tölur á spjaldi.</p>
<p>Þrír vinningar í hverri umferð:</p>
<ol>
<li><strong>Ein lína</strong> — Allar 5 tölur í einni röð</li>
<li><strong>Tvær línur</strong> — Allar tölur í tveimur röðum</li>
<li><strong>Fullt hús</strong> — Allar 15 tölur. Stærsti vinningurinn</li>
</ol>

<h2>75-bolta bingó — mynstur</h2>
<p>Spjaldið er 5×5 með fríum reit í miðju. Vinningsmynstur eru tilkynnt fyrir hverja umferð:</p>
<ul>
<li><strong>Lína</strong> — Lárétt, lóðrétt eða á ská</li>
<li><strong>Form</strong> — Kross, demantur, bókstafir</li>
<li><strong>Coverall / Blackout</strong> — Allt spjaldið. Stærsti vinningurinn</li>
</ul>

<h2>Auto-daub — þú missir ekki af neinu</h2>
<p>Á netinu merkir kerfið tölurnar sjálfkrafa („auto-daub"). Þú getur ekki klikkað á tölu. Það þýðir líka að:</p>
<ul>
<li>Þú getur spilað mörg spjöld samtímis án vandræða</li>
<li>Kunnátta skiptir engu máli — niðurstaðan er fyrirfram ákveðin af tölunum sem dregnar eru</li>
<li>Þú getur spjallað á meðan án þess að tapa</li>
</ul>

<h2>Hvernig vinningar skiptast</h2>
<p>Bingó er <strong>pottleikur</strong>: allir þátttakendur greiða fyrir spjöld, potturinn myndast og vinningshafar skipta honum. Spilavítið tekur þóknun (oft 10–25%).</p>
<p>Það þýðir tvennt:</p>
<ul>
<li>Því fleiri sem spila, þeim mun stærri er potturinn — en þeim mun minni líkur á að þú vinnir</li>
<li>Því færri sem spila, þeim mun minni pottur — en betri líkur</li>
</ul>
<p>Sumir reyndir bingóspilarar velja viljandi herbergi með fáum spilurum í stað stærstu pottanna.</p>

<h2>Bingó vs aðrir leikir</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Bingó</th><th>Spilakassar</th><th>Keno</th></tr></thead><tbody>
<tr><td>Húsforskot</td><td>10–25%</td><td>~4%</td><td>5–35%</td></tr>
<tr><td>Hraði</td><td>5–15 mín/umferð</td><td>Sekúndur</td><td>Sekúndur</td></tr>
<tr><td>Félagslegt</td><td>✅ Spjall</td><td>❌</td><td>❌</td></tr>
<tr><td>Kostnaður á umferð</td><td>Lágur (€0,10–1)</td><td>Breytilegur</td><td>Lágur</td></tr>
</tbody></table>
<p>Húsforskotið í bingó er hátt — en hraðinn er lágur. Að spila bingó í klukkustund kostar yfirleitt mun minna en að spila <a href="{U}spilakassar/">spilakassa</a> í klukkustund, einfaldlega vegna þess að þú gerir færri veðmál.</p>

<h2>Hvar á að spila bingó á Íslandi</h2>
<div class="info-box"><p><strong><a href="{U}spilaviti/bingo-spilaviti/">Bingóspilavíti</a></strong> — Yfirlit yfir spilavíti með bingóherbergjum</p></div>
<div class="info-box"><p><strong><a href="{U}live/bingo-live/">Lifandi bingó</a></strong> — Bingó með raunverulegum kynni frá Evolution og Pragmatic Play</p></div>
<p>Athugaðu að bingó er ekki í boði á öllum spilavítum — það er sérhæfður flokkur.</p>

<h2>Ráð fyrir byrjendur</h2>
<ul>
<li><strong>Byrjaðu á fáum spjöldum</strong> — Þó auto-daub geri það tæknilega mögulegt að spila 50 spjöld, byrjaðu á 2–4 til að skilja flæðið</li>
<li><strong>Athugaðu þóknunina</strong> — Hún er sjaldan auglýst. Spurðu þjónustuver ef hún kemur ekki fram</li>
<li><strong>Prófaðu rólegri herbergi</strong> — Betri vinningslíkur þótt potturinn sé minni</li>
<li><strong>Nýttu spjallið</strong> — Mörg herbergi hafa spjallleiki með aukaverðlaunum</li>
</ul>

<h2>Algengar spurningar</h2>
<h3>Er hægt að auka líkurnar í bingó?</h3>
<p>Aðeins með því að kaupa fleiri spjöld (hlutfallslega betri líkur) eða spila í herbergjum með færri þátttakendum. Engin önnur aðferð virkar.</p>
<h3>Er netbingó sanngjarnt?</h3>
<p>Á spilavítum með gilt leyfi — já. Tölurnar eru dregnar með vottuðum <a href="{U}leidbeiningar/hvernig-rng-virkar/">slembitölugjafa</a>.</p>
<h3>Hvað kostar að spila?</h3>
<p>Spjöld kosta yfirleitt €0,05–1. Þú getur spilað í klukkustund fyrir nokkrar evrur, sem gerir bingó að einum ódýrasta leiknum í tíma talið.</p>''',
    "Spila bingó →"))

P.append(page(
    "spilaviti-med-besta-vip-kerfinu",
    "Spilavíti með besta VIP-kerfinu 2026 — samanburður",
    "Hvaða netspilavíti bjóða bestu VIP-kerfin? Endurgreiðsla, persónulegur stjórnandi, hraðari úttektir og hvað er raunverulega þess virði.",
    "👑", ("#1a1400", "#332800", "#4d3c00"),
    f'''<p>Nánast öll spilavíti auglýsa VIP-kerfi. <strong>Fæst þeirra eru raunverulega þess virði.</strong> Hér förum við yfir hvað skiptir máli og hvað er markaðssetning.</p>

<h2>Hvað VIP-kerfi bjóða yfirleitt</h2>
<table class="info-table"><thead><tr><th>Fríðindi</th><th>Raunverulegt virði</th><th>Athugasemd</th></tr></thead><tbody>
<tr><td>Endurgreiðsla (cashback)</td><td>⭐⭐⭐⭐⭐ Hátt</td><td>Beinn peningur til baka. Mikilvægasta atriðið</td></tr>
<tr><td>Hærri úttektarmörk</td><td>⭐⭐⭐⭐ Gott</td><td>Skiptir máli ef þú vinnur stórt</td></tr>
<tr><td>Hraðari úttektir</td><td>⭐⭐⭐⭐ Gott</td><td>Forgangsafgreiðsla</td></tr>
<tr><td>Persónulegur stjórnandi</td><td>⭐⭐⭐ Miðlungs</td><td>Gagnlegt ef vandamál koma upp</td></tr>
<tr><td>Afmælisbónus</td><td>⭐⭐ Lágt</td><td>Oft með háum veðskilyrðum</td></tr>
<tr><td>Sérstakir bónusar</td><td>⭐⭐ Lágt</td><td>Lestu veðskilyrðin — oft 40x+</td></tr>
<tr><td>Lúxusgjafir / ferðir</td><td>⭐ Mjög lágt</td><td>Krefst gríðarlegrar veltu</td></tr>
</tbody></table>

<h2>Endurgreiðsla er það eina sem skiptir raunverulega máli</h2>
<div class="info-box"><p><strong>Reiknaðu þetta:</strong> Ef spilavíti býður 10% vikulega endurgreiðslu á nettótap lækkar það í raun húsforskotið. Á spilakassa með 4% húsforskot og 10% endurgreiðslu er raunverulegt forskot um 3,6%. Það munar.</p></div>
<p>En lestu skilmálana:</p>
<ul>
<li><strong>Er endurgreiðslan í reiðufé eða bónus?</strong> Reiðufé er margfalt betra — bónus kemur með veðskilyrðum</li>
<li><strong>Er hámark?</strong> „10% endurgreiðsla allt að €50" er allt annað en „10% endurgreiðsla"</li>
<li><strong>Nettó eða brúttó tap?</strong> Nettótap (tap mínus vinningar) er staðlað</li>
</ul>

<h2>Spilavíti með sterk VIP-kerfi</h2>
<div class="info-box"><p><strong><a href="{U}spilaviti/stake/">Stake</a></strong> — Eitt þekktasta VIP-kerfið í bransanum. Stigvaxandi þrep með endurgreiðslu, vikulegum og mánaðarlegum bónusum og persónulegum stjórnanda á hærri þrepum. Gegnsætt þrepakerfi.</p></div>
<div class="info-box"><p><strong><a href="{U}spilaviti/slotoro/">Slotoro</a></strong> — Velkomstpakki á þrjár innborganir og áframhaldandi tilboð. Samstarfsaðili Svipan.</p></div>
<div class="info-box"><p><strong><a href="{U}spilaviti/katsubet/">KatsuBet</a></strong> — Fjögurra þrepa VIP-kerfi með vikulegum mótum.</p></div>
<div class="info-box"><p><strong><a href="{U}spilaviti/respin/">Respin</a></strong> — Vikuleg endurgreiðsla og veðlaus tilboð — endurgreiðsla án veðskilyrða er sjaldgæf og verðmæt.</p></div>
<p>Sjá einnig: <a href="{U}spilaviti/vip-spilaviti/">VIP-spilavíti</a> · <a href="{U}leidbeiningar/vip-kerfi/">hvernig VIP-kerfi virka</a> · <a href="{U}leidbeiningar/spilaviti-endurgreidsla/">endurgreiðsla útskýrð</a></p>

<h2>Varúð: VIP-kerfi og ábyrg spilun</h2>
<div class="info-box"><p><strong>Þetta þarf að segjast skýrt.</strong> VIP-kerfi eru hönnuð til að auka veltu. Þau verðlauna þig fyrir að spila meira — sem er beinlínis í andstöðu við <a href="{U}leidbeiningar/spila-af-abyrgd/">ábyrga spilun</a>.</p></div>
<p>Ef persónulegur stjórnandi hringir í þig og býður bónus eftir að þú hefur tapað stórt er það ekki vinsemd — það er viðskiptamódel.</p>
<p>Eftirlitsaðilar í Bretlandi og Svíþjóð hafa sektað spilavíti fyrir að ýta VIP-tilboðum að spilurum sem sýndu merki um vandamálaspilun. Vertu meðvitaður um hvatana.</p>
<p>Ef þú finnur að VIP-staða hefur áhrif á hversu mikið þú spilar: <a href="{U}leidbeiningar/hvernig-a-ad-setja-takmork-a-spilaviti/">settu takmörk</a> eða <a href="{U}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">lestu um viðvörunarmerki</a>.</p>

<h2>Hvernig á að meta VIP-kerfi</h2>
<ol>
<li><strong>Finndu endurgreiðsluhlutfallið</strong> — Allt undir 5% er lítils virði</li>
<li><strong>Athugaðu hvort hún er í reiðufé</strong> — Bónus með 40x veðskilyrðum er nánast verðlaus</li>
<li><strong>Lestu þrepakröfurnar</strong> — Hversu mikla veltu þarf fyrir næsta þrep? Er það raunhæft fyrir þig?</li>
<li><strong>Athugaðu úttektarmörk á hverju þrepi</strong></li>
<li><strong>Hunsaðu gjafir og ferðir</strong> — Þær krefjast veltu sem þú vilt ekki ná</li>
</ol>

<h2>Algengar spurningar</h2>
<h3>Er hægt að komast í VIP án þess að spila mikið?</h3>
<p>Yfirleitt ekki — þrep byggja á veltu. Sum spilavíti bjóða boð byggð á virkni frekar en upphæð, en það er sjaldgæft.</p>
<h3>Er VIP-staða flytjanleg milli spilavíta?</h3>
<p>Nei. Sum spilavíti bjóða þó „VIP status match" þar sem þú sýnir fram á stöðu annars staðar og færð sambærilega.</p>
<h3>Er endurgreiðsla betri en velkomstbónus?</h3>
<p>Fyrir þá sem spila reglulega — já, oftast. Velkomstbónus fæst einu sinni; endurgreiðsla heldur áfram. Og endurgreiðsla í reiðufé hefur engin <a href="{U}leidbeiningar/hvad-eru-vedskilyrdi/">veðskilyrði</a>.</p>''',
    "Sjá VIP-spilavíti →"))

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
