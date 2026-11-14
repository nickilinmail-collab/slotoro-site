#!/usr/bin/env python3
"""Add brand review pages for cross-brand traffic capture."""

AFF = "https://gameslnk.cc/go/2e7c17f7302f426b36e7e5242aaa9b3e365b64d1eb0a0b0b/"

# (slug, title, desc, emoji, colors, brand, founded, owner, licence, games, bonus, mindep, isl_ui, crypto, pros, cons, extra_sections, faqs)
BRANDS = [
    dict(
        slug="verde-casino-umsogn",
        title="Verde Casino umsögn á íslensku — bónus og greiðslur 2026",
        desc="Verde Casino umsögn fyrir íslenska spilara: velkomstbónus, leikjaúrval, greiðsluleiðir og hvort spilavítið tekur við frá Íslandi.",
        emoji="🌿", colors=("#0a1a0f", "#14331e", "#1e4d2d"),
        brand="Verde Casino", founded="2022", owner="Brivio Limited (V.Partners)",
        licence="Curaçao", games="4.000+", bonus="Allt að €1.500 + 220 FS", mindep="€10",
        isl_ui="❌ Nei (enska, pólska, þýska o.fl.)", crypto="✅ BTC, ETH, LTC, USDT",
        pros=["Stór velkomstpakki yfir fjórar innborganir", "Gott leikjaúrval (4.000+)",
              "Lág lágmarksinnborgun (€10)", "Hluti af V.Partners — sömu eigendur og Slotoro"],
        cons=["Ekkert íslenskt viðmót", "40x veðskilyrði", "Þjónustuver aðeins á ensku",
              "Bónus rennur út á 5 dögum"],
        extra="""<h2>Velkomstpakki Verde Casino</h2>
<p>Verde dreifir velkomstbónusnum yfir fjórar innborganir — svipað og systursíðurnar:</p>
<ol>
<li>1. innborgun: 100% allt að €400 + 100 FS</li>
<li>2. innborgun: 50% allt að €400 + 50 FS</li>
<li>3. innborgun: 75% allt að €400 + 35 FS</li>
<li>4. innborgun: 100% allt að €300 + 35 FS</li>
</ol>
<p>Veðskilyrði eru 40x bónusupphæð — það þýðir að €100 bónus krefst €4.000 í veltu áður en hægt er að taka út.
Berðu þetta saman við <a href="{URL_BASE}leidbeiningar/spilaviti-an-vedskilyrda/">veðlaus spilavíti</a> þar sem vinningurinn er þinn strax.</p>

<h2>Verde Casino vs Slotoro</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Verde Casino</th><th>Slotoro</th></tr></thead><tbody>
<tr><td>Leikir</td><td>4.000+</td><td>8.000+</td></tr>
<tr><td>Framleiðendur</td><td>50+</td><td>71</td></tr>
<tr><td>Lágmarksinnborgun</td><td>€10</td><td>€10</td></tr>
<tr><td>Veðskilyrði</td><td>40x</td><td>40x</td></tr>
<tr><td>Íþróttaveðmál</td><td>❌ Nei</td><td>✅ Já</td></tr>
</tbody></table>""",
        faqs=[("Tekur Verde Casino við íslenskum spilurum?",
               "Já — Verde Casino lokar ekki á Ísland. Viðmótið er þó ekki á íslensku, svo þú þarft að lesa bónusskilmála á ensku."),
              ("Er Verde Casino öruggt?",
               "Verde er með Curaçao leyfi og er rekið af Brivio Limited, sama fyrirtæki og stendur að baki Vulkan Vegas og Ice Casino. Rótgróinn rekstraraðili í bransanum."),
              ("Hvaða greiðsluleið virkar best frá Íslandi?",
               "Dulritunargjaldmiðlar eða Revolut. Íslensk bankakort geta verið hafnað — sjá leiðbeiningar okkar um greiðslur.")],
    ),
    dict(
        slug="hitnspin-umsogn-a-islensku",
        title="Hit'N'Spin umsögn á íslensku — bónus og leikir 2026",
        desc="Hit'N'Spin umsögn fyrir íslenska spilara. Einkaréttarbrand V.Partners: bónus, leikjaúrval og greiðsluleiðir.",
        emoji="🎯", colors=("#28100a", "#451c14", "#62291e"),
        brand="Hit'N'Spin", founded="2023", owner="V.Partners (einkaréttarbrand)",
        licence="Curaçao", games="3.000+", bonus="Allt að €1.000 + 100 FS", mindep="€20",
        isl_ui="❌ Nei", crypto="✅ BTC, ETH, LTC, USDT",
        pros=["Einkaréttarbrand — fáanlegt aðeins í gegnum V.Partners",
              "Nýtt spilavíti með nútímalegu viðmóti", "Gott úrval af lifandi leikjum",
              "Dulritunargjaldmiðlar studdir"],
        cons=["Ekkert íslenskt viðmót", "€20 lágmarksinnborgun (hærra en flest)",
              "Nýtt — minni reynslusaga en eldri spilavíti", "40x veðskilyrði"],
        extra="""<h2>Hvað þýðir „einkaréttarbrand"?</h2>
<p>Hit'N'Spin er eitt af þeim spilavítum sem eingöngu eru í boði í gegnum V.Partners samstarfsnetið — ásamt
<a href="{URL_BASE}spilaviti/slotoro/">Slotoro</a> og Vulkan Spiele. Það þýðir að þú finnur það ekki á hverri
samanburðarsíðu og samkeppnin um bónusa er minni.</p>

<h2>Leikjaúrval</h2>
<p>Hit'N'Spin býður yfir 3.000 leiki frá helstu framleiðendum: Pragmatic Play, Evolution, Play'n GO, NetEnt,
Hacksaw Gaming og Nolimit City. Lifandi spilavítishlutinn er sterkur — Evolution borð eru í boði allan sólarhringinn.</p>""",
        faqs=[("Er Hit'N'Spin nýtt spilavíti?",
               "Já — Hit'N'Spin opnaði 2023 og er því tiltölulega nýtt. Það er rekið af V.Partners sem hefur starfað síðan 2016."),
              ("Get ég spilað Hit'N'Spin frá Íslandi?",
               "Já. Notaðu dulritunargjaldmiðla eða Revolut til innborgunar þar sem íslensk bankakort geta verið hafnað."),
              ("Hvernig ber Hit'N'Spin sig saman við Slotoro?",
               "Slotoro hefur fleiri leiki (8.000+ á móti 3.000+) og lægri lágmarksinnborgun (€10 á móti €20). Bæði eru V.Partners brand.")],
    ),
    dict(
        slug="betsson-a-islandi",
        title="Betsson á Íslandi — umsögn, bónus og staða 2026",
        desc="Betsson umsögn fyrir íslenska spilara. Norrænt spilavíti síðan 1963: leyfi, leikir, greiðslur og hvort það tekur við frá Íslandi.",
        emoji="🟠", colors=("#28140a", "#452414", "#62341e"),
        brand="Betsson", founded="1963 (á netinu síðan 2001)", owner="Betsson AB (skráð á Nasdaq Stokkhólmi)",
        licence="Malta (MGA) + fleiri", games="2.000+", bonus="Fer eftir markaði", mindep="€10",
        isl_ui="❌ Nei", crypto="❌ Nei",
        pros=["Eitt elsta og virtasta spilavíti Norðurlanda", "Skráð á hlutabréfamarkaði — mikið gegnsæi",
              "MGA leyfi (hæsta traust)", "Sterkur íþróttaveðmálahluti"],
        cons=["Tekur ekki alltaf við íslenskum spilurum — fer eftir markaðsstillingum",
              "Engir dulritunargjaldmiðlar", "Ekkert íslenskt viðmót", "Strangar KYC kröfur"],
        extra="""<h2>Tekur Betsson við íslenskum spilurum?</h2>
<p>Betsson rekur sérstakar síður fyrir hvern markað og fylgir leyfisskilyrðum hvers lands. Vegna þess að Ísland hefur
ekkert leyfiskerfi fyrir netspilavíti er aðgengi óstöðugt — stundum er hægt að skrá sig, stundum ekki, og þetta getur
breyst án fyrirvara.</p>
<p>Ef þú vilt spilavíti sem tekur örugglega við íslenskum spilurum skaltu skoða
<a href="{URL_BASE}leidbeiningar/spilaviti-med-islensku-vidmoti/">spilavíti á íslensku</a> eða
<a href="{URL_BASE}leidbeiningar/bestu-crypto-spilavitin-island/">dulritunarspilavíti</a>.</p>

<h2>Af hverju er Betsson svona þekkt?</h2>
<p>Betsson AB er skráð á Nasdaq Stokkhólmi og rekur yfir 20 vörumerki. Fyrirtækið hefur starfað síðan 1963 (upphaflega
sem spilakassafyrirtæki) og fór á netið 2001. Þetta er eitt af fáum spilavítafyrirtækjum þar sem ársreikningar eru
opinberir — mikið gegnsæi samanborið við Curaçao-rekin spilavíti.</p>""",
        faqs=[("Get ég skráð mig á Betsson frá Íslandi?",
               "Það fer eftir því hvaða markaðsútgáfu Betsson býður upp á hverju sinni. Aðgengi frá Íslandi er ekki tryggt og getur breyst."),
              ("Er Betsson öruggt?",
               "Já — Betsson er með MGA leyfi og er skráð á hlutabréfamarkaði. Þetta er meðal áreiðanlegustu rekstraraðila í bransanum."),
              ("Tekur Betsson við Bitcoin?",
               "Nei — Betsson styður ekki dulritunargjaldmiðla. Ef þú vilt spila með Bitcoin skaltu skoða lista okkar yfir dulritunarspilavíti.")],
    ),
    dict(
        slug="unibet-a-islandi",
        title="Unibet á Íslandi — umsögn og staða 2026",
        desc="Unibet umsögn fyrir íslenska spilara: leyfi, leikjaúrval, íþróttaveðmál og hvort síðan tekur við frá Íslandi.",
        emoji="🟢", colors=("#0a1f14", "#143a26", "#1e5538"),
        brand="Unibet", founded="1997", owner="Kindred Group (áður Unibet Group)",
        licence="Malta (MGA), UKGC, fleiri", games="1.500+", bonus="Fer eftir markaði", mindep="€10",
        isl_ui="❌ Nei", crypto="❌ Nei",
        pros=["Rótgróið síðan 1997", "MGA og UKGC leyfi", "Mjög sterkur íþróttaveðmálahluti",
              "Hluti af Kindred Group — skráð fyrirtæki"],
        cons=["Aðgengi frá Íslandi ekki tryggt", "Engir dulritunargjaldmiðlar",
              "Ekkert íslenskt viðmót", "Minna leikjaúrval en crypto-spilavíti"],
        extra="""<h2>Unibet og Kindred Group</h2>
<p>Unibet er flaggskipsvörumerki Kindred Group, sem rekur einnig Maria Casino, 32Red og Otto Kasino.
Kindred er skráð á Nasdaq Stokkhólmi og birtir meðal annars hlutfall tekna sem kemur frá spilurum
með áhættusama spilahegðun — óvenjulegt gegnsæi í bransanum.</p>

<h2>Styrkleiki: íþróttaveðmál</h2>
<p>Unibet er fyrst og fremst þekkt fyrir íþróttaveðmál frekar en spilavítishlutann. Fótbolti, handbolti
og körfubolti eru vel þjónustuð — sem á vel við íslenskan markað þar sem handbolti og fótbolti eru vinsælastir.</p>""",
        faqs=[("Tekur Unibet við íslenskum spilurum?",
               "Aðgengi er ekki tryggt og fer eftir markaðsstillingum Kindred Group hverju sinni."),
              ("Er Unibet betra fyrir íþróttir eða spilavíti?",
               "Íþróttir. Unibet byggði orðspor sitt á veðmálum og spilavítishlutinn er minni en hjá sérhæfðum spilavítum."),
              ("Hvaða valkostir eru fyrir íslenska spilara?",
               "Spilavíti með íslensku viðmóti eða dulritunarspilavíti sem taka örugglega við frá Íslandi — sjá samanburðarlista okkar.")],
    ),
    dict(
        slug="leovegas-a-islandi",
        title="LeoVegas á Íslandi — umsögn og farsímaupplifun 2026",
        desc="LeoVegas umsögn: farsímaspilavítið sem vann til verðlauna. Leyfi, leikir, greiðslur og staða gagnvart Íslandi.",
        emoji="🦁", colors=("#28200a", "#453814", "#62501e"),
        brand="LeoVegas", founded="2011", owner="MGM Resorts International (síðan 2022)",
        licence="Malta (MGA), UKGC, fleiri", games="2.000+", bonus="Fer eftir markaði", mindep="€10",
        isl_ui="❌ Nei", crypto="❌ Nei",
        pros=["Besta farsímaupplifun í bransanum — margverðlaunað",
              "Í eigu MGM Resorts (Las Vegas risinn)", "MGA og UKGC leyfi",
              "Stór lifandi spilavítishluti"],
        cons=["Aðgengi frá Íslandi ekki tryggt", "Engir dulritunargjaldmiðlar",
              "Ekkert íslenskt viðmót", "Bónusskilmálar misjafnir eftir mörkuðum"],
        extra="""<h2>„Konungur farsímaspilavíta"</h2>
<p>LeoVegas byggði allt sitt viðmót fyrir farsíma fyrst — áður en það varð staðall í bransanum. Fyrirtækið hefur
unnið fjölda verðlauna fyrir farsímaupplifun. Ef þú spilar aðallega í símanum er þetta viðmiðunarpunkturinn sem
önnur spilavíti eru borin saman við.</p>
<p>Sjá einnig: <a href="{URL_BASE}leidbeiningar/spilaviti-fyrir-farsima-island/">bestu farsímaspilavítin á Íslandi</a>.</p>

<h2>MGM eignarhald</h2>
<p>MGM Resorts International keypti LeoVegas árið 2022 fyrir um 600 milljónir evra. Það þýðir að bandaríski
spilavítarisinn stendur að baki rekstrinum — sem eykur fjárhagslegan stöðugleika verulega.</p>""",
        faqs=[("Er LeoVegas best fyrir farsíma?",
               "LeoVegas er almennt talið meðal þeirra bestu í farsímaupplifun. Þó hafa önnur spilavíti náð því á síðustu árum."),
              ("Tekur LeoVegas við frá Íslandi?",
               "Aðgengi er ekki tryggt. LeoVegas einbeitir sér að mörkuðum með leyfiskerfi eins og Svíþjóð, Danmörku og Bretlandi."),
              ("Hver á LeoVegas?",
               "MGM Resorts International, bandaríski spilavíta- og hótelrisinn, keypti LeoVegas árið 2022.")],
    ),
    dict(
        slug="mr-green-a-islandi",
        title="Mr Green á Íslandi — umsögn og ábyrg spilun 2026",
        desc="Mr Green umsögn: sænskt spilavíti þekkt fyrir verkfæri í ábyrgri spilun. Leyfi, leikir og staða gagnvart Íslandi.",
        emoji="🎩", colors=("#0a2814", "#144524", "#1e6234"),
        brand="Mr Green", founded="2008", owner="William Hill / evoke plc",
        licence="Malta (MGA), UKGC, fleiri", games="1.800+", bonus="Fer eftir markaði", mindep="€10",
        isl_ui="❌ Nei", crypto="❌ Nei",
        pros=["Leiðandi í verkfærum fyrir ábyrga spilun (Green Gaming)",
              "MGA og UKGC leyfi", "Vandað viðmót og notendaupplifun",
              "Hluti af evoke plc (áður William Hill)"],
        cons=["Aðgengi frá Íslandi ekki tryggt", "Engir dulritunargjaldmiðlar",
              "Ekkert íslenskt viðmót", "Minna leikjaúrval en crypto-spilavíti"],
        extra="""<h2>Green Gaming — verkfæri gegn spilafikn</h2>
<p>Mr Green þróaði „Green Gaming" kerfi sem greinir spilahegðun og varar spilara við ef mynstrið bendir til
áhættusamrar hegðunar. Spilarar fá persónulegt áhættumat og tillögur um takmörk.</p>
<p>Þetta er meðal þróaðustu verkfæra í bransanum. Ef þú vilt lesa meira um merki áhættusamrar spilunar,
sjá <a href="{URL_BASE}leidbeiningar/merki-thess-ad-thu-sert-ordinn-hadur-spilavitum/">leiðbeiningar okkar</a>
og <a href="{URL_BASE}leidbeiningar/sjalfsutilokun-spilavita/">sjálfsútilokun</a>.</p>""",
        faqs=[("Hvað er Green Gaming?",
               "Verkfæri Mr Green sem greinir spilahegðun og gefur spilurum persónulegt áhættumat ásamt tillögum um takmörk."),
              ("Tekur Mr Green við íslenskum spilurum?",
               "Aðgengi er ekki tryggt og fer eftir markaðsstillingum. Mr Green einbeitir sér að mörkuðum með leyfiskerfi."),
              ("Hver á Mr Green?",
               "Mr Green var keypt af William Hill árið 2019 og tilheyrir nú evoke plc samsteypunni.")],
    ),
    dict(
        slug="casumo-a-islandi",
        title="Casumo á Íslandi — umsögn og staða 2026",
        desc="Casumo umsögn: spilavítið með ævintýraþema og Reel Races. Leyfi, leikjaúrval og hvort það tekur við frá Íslandi.",
        emoji="🟣", colors=("#1a0a28", "#2d1445", "#401e62"),
        brand="Casumo", founded="2012", owner="Casumo Services Limited",
        licence="Malta (MGA), UKGC, fleiri", games="2.500+", bonus="Fer eftir markaði", mindep="€10",
        isl_ui="❌ Nei", crypto="❌ Nei",
        pros=["Einstakt ævintýraþema með stigum og verðlaunum",
              "Reel Races — spilakassamót allan daginn", "MGA og UKGC leyfi",
              "Hröð skráning og einfalt viðmót"],
        cons=["Aðgengi frá Íslandi ekki tryggt", "Engir dulritunargjaldmiðlar",
              "Ekkert íslenskt viðmót", "Bónustilboð misjöfn eftir mörkuðum"],
        extra="""<h2>Reel Races — spilakassamót</h2>
<p>Casumo er þekktast fyrir „Reel Races" — stuttar keppnir (oft 20-60 mínútur) þar sem spilarar keppa um
verðlaunasjóð með því að safna stigum í spilakössum. Þetta gerir venjulega spilun samkeppnishæfari.</p>
<p>Sambærileg mót eru í boði á <a href="{URL_BASE}spilaviti/motaspilaviti/">mótaspilavítum</a> sem taka við íslenskum spilurum.</p>

<h2>Ævintýraþemað</h2>
<p>Í stað hefðbundins VIP-kerfis notar Casumo stigakerfi þar sem þú „ferðast" í gegnum ævintýri og vinnur
verðlaun eftir því sem þú spilar. Þetta er gamification-nálgun sem mörg nýrri spilavíti hafa hermt eftir.</p>""",
        faqs=[("Hvað eru Reel Races?",
               "Stuttar spilakassakeppnir hjá Casumo þar sem spilarar keppa um verðlaunasjóð með því að safna stigum."),
              ("Tekur Casumo við frá Íslandi?",
               "Aðgengi er ekki tryggt. Casumo einbeitir sér að mörkuðum með leyfiskerfi eins og Bretlandi og Svíþjóð."),
              ("Er Casumo með VIP kerfi?",
               "Casumo notar ævintýra- og stigakerfi í stað hefðbundins VIP-kerfis.")],
    ),
]


def build(b):
    pros = "\n".join(f"<tr><td>✅ {p}</td><td>❌ {c}</td></tr>"
                     for p, c in zip(b["pros"], b["cons"]))
    faqs = "\n".join(f"<h3>{q}</h3>\n<p>{a}</p>" for q, a in b["faqs"])
    return f'''    {{
        "slug": "{b['slug']}",
        "title": "{b['title']}",
        "desc": "{b['desc']}",
        "emoji": "{b['emoji']}",
        "colors": {b['colors']},
        "content": f\'\'\'<h1>{b['title'].split(" — ")[0]} 2026</h1>
{{hero}}
<p>{b['brand']} er eitt af þeim spilavítum sem íslenskir spilarar leita reglulega að. <strong>Hér förum við yfir hvað það býður, hvernig það ber sig saman við valkosti sem taka örugglega við frá Íslandi, og hvað þú þarft að varast.</strong></p>

<h2>{b['brand']} í hnotskurn</h2>
<table class="info-table"><thead><tr><th>Þáttur</th><th>Upplýsingar</th></tr></thead><tbody>
<tr><td>Stofnár</td><td>{b['founded']}</td></tr>
<tr><td>Eigandi</td><td>{b['owner']}</td></tr>
<tr><td>Leyfi</td><td>{b['licence']}</td></tr>
<tr><td>Fjöldi leikja</td><td>{b['games']}</td></tr>
<tr><td>Velkomstbónus</td><td>{b['bonus']}</td></tr>
<tr><td>Lágmarksinnborgun</td><td>{b['mindep']}</td></tr>
<tr><td>Íslenskt viðmót</td><td>{b['isl_ui']}</td></tr>
<tr><td>Dulritunargjaldmiðlar</td><td>{b['crypto']}</td></tr>
</tbody></table>

<h2>Kostir og gallar</h2>
<table class="info-table"><thead><tr><th>Kostir</th><th>Gallar</th></tr></thead><tbody>
{pros}
</tbody></table>

{b['extra']}

<h2>Greiðsluleiðir frá Íslandi</h2>
<p>Stærsta hindrunin fyrir íslenska spilara eru <a href="{{URL_BASE}}leidbeiningar/islenskir-bankar-spilaviti/">bankatakmarkanir</a>.
Arion, Landsbankinn og Íslandsbanki geta hafnað kortagreiðslum til spilavíta. Lausnir:</p>
<ul>
<li><strong>Dulritunargjaldmiðlar</strong> — Bankinn kemur hvergi nærri. <a href="{{URL_BASE}}leidbeiningar/kaupa-bitcoin-island/">Hvernig á að kaupa Bitcoin á Íslandi →</a></li>
<li><strong>Revolut</strong> — Fer ekki gegnum íslenskt bankakerfi. <a href="{{URL_BASE}}leidbeiningar/revolut-spilaviti-island-leidbeining/">Revolut leiðbeining →</a></li>
<li><strong>Rafræn veski</strong> — <a href="{{URL_BASE}}greidslur/skrill-i-spilavitum/">Skrill</a> og <a href="{{URL_BASE}}greidslur/neteller-i-spilavitum/">Neteller</a></li>
</ul>

<h2>Valkostir sem taka örugglega við frá Íslandi</h2>
<div class="info-box"><p><strong><a href="{{URL_BASE}}spilaviti/slotoro/">Slotoro</a></strong> — 8.000+ leikir frá 71 framleiðendum, €10 lágmarksinnborgun, dulritunargjaldmiðlar studdir. Samstarfsaðili Svipan.</p></div>
<div class="info-box"><p><strong><a href="{{URL_BASE}}spilaviti/epicbet/">Epicbet</a></strong> — Fullkomið íslenskt viðmót, veðlausir bónusar og Apple Pay.</p></div>
<div class="info-box"><p><strong><a href="{{URL_BASE}}spilaviti/bitstarz/">BitStarz</a></strong> — Dulritunarspilavíti með úttektum undir 10 mínútum.</p></div>
<p>Sjá allan <a href="{{URL_BASE}}spilaviti/">samanburð á spilavítum →</a></p>

<h2>Algengar spurningar</h2>
{faqs}
<div class="cta-box"><a href="{AFF}" target="_blank" rel="noopener" class="cta-btn">Prófa Slotoro →</a></div>\'\'\'
    }},'''


blocks = "\n".join(build(b) for b in BRANDS)

with open("generate.py", "r", encoding="utf-8") as f:
    code = f.read()

marker = "    },\n]"
idx = code.rfind(marker)
if idx == -1:
    raise SystemExit("could not find end of seo_pages")
pos = idx + len("    },\n")
code = code[:pos] + blocks + "\n" + code[pos:]

with open("generate.py", "w", encoding="utf-8") as f:
    f.write(code)
print(f"inserted {len(BRANDS)} brand pages")
