#!/usr/bin/env python3
"""
Ingest all 140 unique entries from ARS_PHYTOGLYPHICA_EXPANDED into IG_catalog.json.
Run from repo root: uv run programs/ingest_ars_expanded.py
"""
import json
import sys
from pathlib import Path

# ── Primitive order: Ð Þ Ř Φ ƒ Ç Γ ɢ ⊙ Ħ Σ Ω ──────────────────────────────
PRIMITIVES = ['Ð', 'Þ', 'Ř', 'Φ', 'ƒ', 'Ç', 'Γ', 'ɢ', '⊙', 'Ħ', 'Σ', 'Ω']

TYPE_TUPLES = {
    'I':    ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑤','𐑔','𐑠','⊙','𐑖','𐑳','𐑭'],
    'II':   ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑤','𐑲','𐑠','⊙','𐑖','𐑕','𐑭'],
    'III':  ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑤','𐑔','𐑠','⊙','𐑖','𐑕','𐑭'],
    'IV':   ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑤','𐑔','𐑠','𐑢','𐑖','𐑳','𐑭'],
    'V':    ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑤','𐑔','𐑠','⊙','𐑫','𐑙','𐑭'],
    'VI':   ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑧','𐑔','𐑠','⊙','𐑖','𐑳','𐑭'],
    'VII':  ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑤','𐑲','𐑠','⊙','𐑫','𐑕','𐑴'],
    'VIII': ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑧','𐑔','𐑝','𐑢','𐑒','𐑙','𐑷'],
    'IX':   ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑤','𐑲','𐑠','⊙','𐑫','𐑕','𐑭'],
    'X':    ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑧','𐑔','𐑠','⊙','𐑖','𐑳','𐑭'],
    'XI':   ['𐑦','𐑸','𐑾','𐑬','𐑱','𐑤','𐑲','𐑵','⊙','𐑫','𐑳','𐑴'],
}

# ── Entry manifest: (key, type, description) ─────────────────────────────────
# 140 unique entries from ARS_PHYTOGLYPHICA_EXPANDED (154 total minus 14 SKIPs)
ENTRIES = [
    # ── Europe & Mediterranean (1–48) ─────────────────────────────────────────
    ('wormwood',          'I',   'Artemisia absinthium L. | Asteraceae — Type I Aromatic Baseline. Thujone-dominant volatile oil; bilateral serration encodes ester cleavage.'),
    ('yarrow',            'I',   'Achillea millefolium L. | Asteraceae — Type I Aromatic Baseline. Millefoliate leaf; hundreds of fine serrations encode repeated ROTR for azulene release.'),
    ('rosemary',          'I',   'Salvia rosmarinus Spenn. | Lamiaceae — Type I Aromatic Baseline. Revolute needle leaves protect abaxial trichomes; camphor/1,8-cineole dominant.'),
    ('sage',              'I',   'Salvia officinalis L. | Lamiaceae — Type I Aromatic Baseline. Boundary case; decussate phyllotaxis (Omega=trivial variant); thujone/camphor dominant.'),
    ('mugwort',           'I',   'Artemisia vulgaris L. | Asteraceae — Type I Aromatic Baseline. Dark adaxial/white tomentose abaxial; directional DEREF to trichome field.'),
    ('southernwood',      'I',   'Artemisia abrotanum L. | Asteraceae — Type I Aromatic Baseline. Finely dissected thread-like leaves; minimal extraction effort; lemon-scented chemotype.'),
    ('tarragon',          'I',   'Artemisia dracunculus L. | Asteraceae — Type I Aromatic Baseline. Estragole dominant; linear-lanceolate leaf encodes PUSH not ROTR.'),
    ('oregano',           'I',   'Origanum vulgare L. | Lamiaceae — Type I Aromatic Baseline. Inflorescence bracts concentrate pharmaceutical; carvacrol/thymol XOR gate.'),
    ('thyme',             'I',   'Thymus vulgaris L. | Lamiaceae — Type I Aromatic Baseline. Miniature revolute leaves; protected abaxial trichome chamber; thymol dominant.'),
    ('marjoram',          'I',   'Origanum majorana L. | Lamiaceae — Type I Aromatic Baseline. Symmetric extraction from both surfaces; cis-sabinene hydrate dominant.'),
    ('lavender',          'I',   'Lavandula angustifolia Mill. | Lamiaceae — Type I Aromatic Baseline. Inflorescence calyx trichomes; flower color encodes ester content.'),
    ('hyssop',            'I',   'Hyssopus officinalis L. | Lamiaceae — Type I Aromatic Baseline. Bilateral flower orientation encodes directional harvest; pinocamphone/isopinocamphone.'),
    ('winter_savory',     'I',   'Satureja montana L. | Lamiaceae — Type I Aromatic Baseline. Stiff entire leaves encode crush instruction; high thymol content.'),
    ('lemon_balm',        'I',   'Melissa officinalis L. | Lamiaceae — Type I Aromatic Baseline. Ovate crenate leaves; citronellal/citral/geranial volatile profile.'),
    ('peppermint',        'I',   'Mentha x piperita L. | Lamiaceae — Type I Aromatic Baseline. Broadly serrate leaves; menthol activates TRPM8; XOR gate with menthone.'),
    ('spearmint',         'I',   'Mentha spicata L. | Lamiaceae — Type I Aromatic Baseline. Sharply serrate leaves; R-(-)-carvone dominant; Frobenius chirality.'),
    ('catnip',            'I',   'Nepeta cataria L. | Lamiaceae — Type I Aromatic Baseline. Nepetalactone; cat rolling response IS external pharmaceutical self-report.'),
    ('clary_sage',        'I',   'Salvia sclarea L. | Lamiaceae — Type I Aromatic Baseline. Dense glandular trichomes on bracts; sclareol requires steam distillation.'),
    ('santolina',         'I',   'Santolina chamaecyparissus L. | Asteraceae — Type I Aromatic Baseline. Extreme trichome density; woolly surface encodes DEREF -> PUSH.'),
    ('bog_myrtle',        'I',   'Myrica gale L. | Myricaceae — Type I Aromatic Baseline. Resinous gland leaves; alpha-pinene/1,8-cineole; potency peaks under water stress.'),
    ('sweet_gale',        'I',   'Myrica gale chemotype | Myricaceae — Type I Aromatic Baseline. Aromatic chemotype used in gruit ale; same structural tuple as bog myrtle.'),
    ('juniper',           'I',   'Juniperus communis L. | Cupressaceae — Type I Aromatic Baseline. Pharmaceutical in fleshy female cones; color change (green->black) IS self-report.'),
    ('sweet_flag',        'I',   'Acorus calamus L. | Acoraceae — Type I Aromatic Baseline. Aromatic rhizome is pharmaceutical organ; beta-asarone content varies with ploidy.'),
    ('angelica',          'I',   'Angelica archangelica L. | Apiaceae — Type I Aromatic Baseline. Entire plant aromatic; hollow stem as volatile resonating chamber; multi-organ sequence.'),
    ('lovage',            'I',   'Levisticum officinale W.D.J.Koch | Apiaceae — Type I Aromatic Baseline. Celery-like aroma; ligustilide dominant; simple compound profile.'),
    ('fennel',            'I',   'Foeniculum vulgare Mill. | Apiaceae — Type I Aromatic Baseline. Filiform leaves maximize volatile release; anethole/fenchone XOR gate (seed vs. leaf).'),
    ('dill',              'I',   'Anethum graveolens L. | Apiaceae — Type I Aromatic Baseline. S-(+)-carvone dominant; leaf (volatile) vs. seed (stable) dual-module architecture.'),
    ('caraway',           'I',   'Carum carvi L. | Apiaceae — Type I Aromatic Baseline. S-(+)-carvone dominant seed; biennial life cycle encodes pharmaceutical readiness.'),
    ('coriander',         'I',   'Coriandrum sativum L. | Apiaceae — Type I Aromatic Baseline. Complete compound class switch: leaf (aldehydes) XOR seed (linalool).'),
    ('anise',             'I',   'Pimpinella anisum L. | Apiaceae — Type I Aromatic Baseline. Anethole dominant seed; ridged surface encodes self-report of anethole content.'),
    ('belladonna',        'II',  'Atropa belladonna L. | Solanaceae — Type II Tropane. Hyoscyamine/atropine; glossy black berries and fetid odor encode toxicity self-report.'),
    ('henbane',           'II',  'Hyoscyamus niger L. | Solanaceae — Type II Tropane. Scopolamine:hyoscyamine ~1:2; viscid pubescence encodes danger.'),
    ('datura',            'II',  'Datura stramonium L. | Solanaceae — Type II Tropane. Spiny capsule encodes DEREF -> PUSH; medicine inside capsule.'),
    ('mandrake',          'II',  'Mandragora officinarum L. | Solanaceae — Type II Tropane. Humanoid root; tropane alkaloids; cultural DANGER encoding in bifurcated form.'),
    ('black_henbane_annual', 'II', 'Hyoscyamus niger L. annual form | Solanaceae — Type II Tropane. Annual form; higher scopolamine proportion than biennial; faster-acting.'),
    ('foxglove',          'III', 'Digitalis purpurea L. | Plantaginaceae — Type III Cardiac Glycoside. Leaf-size gradient up stem encodes cardiac glycoside concentration gradient.'),
    ('lily_of_the_valley','III', 'Convallaria majalis L. | Asparagaceae — Type III Cardiac Glycoside. Parallel-veined entire leaves; sweet flower fragrance is NOT pharmaceutical self-report.'),
    ('oleander',          'III', 'Nerium oleander L. | Apocynaceae — Type III Cardiac Glycoside. Narrow leathery whorled leaves; oleandrin present in all tissues; most toxic Type III.'),
    ('christmas_rose',    'III', 'Helleborus niger L. | Ranunculaceae — Type III Cardiac Glycoside. Winter flowering IS self-report of pharmaceutical readiness; hellebrin in root.'),
    ('german_chamomile',  'IV',  'Matricaria chamomilla L. | Asteraceae — Type IV Non-Critical Aromatic. Petal reflex does not encode chamazulene content; structurally opaque.'),
    ('roman_chamomile',   'IV',  'Chamaemelum nobile (L.) All. | Asteraceae — Type IV Non-Critical Aromatic. Apple fragrance does not track pharmaceutical content.'),
    ('comfrey',           'IV',  'Symphytum officinale L. | Boraginaceae — Type IV Non-Critical Aromatic. Hispid leaves; allantoin content not morphologically encoded.'),
    ('coltsfoot',         'IV',  'Tussilago farfara L. | Asteraceae — Type IV Non-Critical Aromatic. Flowers before leaves; hoof-shaped outline; no pharmaceutical self-report.'),
    ('mullein',           'IV',  'Verbascum thapsus L. | Scrophulariaceae — Type IV Non-Critical Aromatic. Dense trichomes serve mechanical not pharmaceutical function.'),
    ('yew',               'V',   'Taxus baccata L. | Taxaceae — Type V Axiom A / Eternal. Taxane diterpenoid; 11 stereocenters; eternal chirality; red aril encodes edible/lethal split.'),
    ('autumn_crocus',     'V',   'Colchicum autumnale L. | Colchicaceae — Type V Axiom A / Eternal. Colchicine via ring-expansion; flowers in autumn, leaves in spring; temporal separation.'),
    ('stinking_hellebore','V',   'Helleborus foetidus L. | Ranunculaceae — Type V Axiom A / Eternal. Protoanemonin/hellebrin; fetid odor IS self-report; winter survival = readiness.'),
    ('monkshood',         'V',   'Aconitum napellus L. | Ranunculaceae — Type V Axiom A / Eternal. Most toxic European plant; 19 enzymatic steps; helmet flower encodes DANGER.'),

    # ── Asia (49–98 minus cross-refs 64, 65, 68, 91) ─────────────────────────
    ('patchouli',         'I',   'Pogostemon cablin (Blanco) Benth. | Lamiaceae — Type I Aromatic Baseline. Sesquiterpenes in trichomes; self-report intensifies post-harvest.'),
    ('holy_basil',        'I',   'Ocimum tenuiflorum L. | Lamiaceae — Type I Aromatic Baseline. Eugenol dominant; anthocyanin coloration tracks eugenol content under stress.'),
    ('camphor_basil',     'I',   'Ocimum kilimandscharicum Guerke | Lamiaceae — Type I Aromatic Baseline. Camphor crystallizes on leaf surface; literal externalized self-report.'),
    ('lemongrass',        'I',   'Cymbopogon citratus (DC.) Stapf | Poaceae — Type I Aromatic Baseline. Citral in leaf sheaths; overlapping sheaths form protected aromatic chamber.'),
    ('citronella',        'I',   'Cymbopogon nardus (L.) Rendle | Poaceae — Type I Aromatic Baseline. Citronellal/geraniol in leaf sheaths; drooping leaf tip encodes directional extraction.'),
    ('galangal',          'I',   'Alpinia galanga (L.) Willd. | Zingiberaceae — Type I Aromatic Baseline. Aromatic rhizome; pungency/aroma IS self-report of 1-acetoxychavicol acetate content.'),
    ('ginger',            'I',   'Zingiber officinale Roscoe | Zingiberaceae — Type I Aromatic Baseline. Gingerol -> shogaol XOR gate on drying; fibrous texture encodes conversion state.'),
    ('asian_ginseng',     'VI',  'Panax ginseng C.A.Mey. | Araliaceae — Type VI Adaptogen. Ginsenosides (Rb1/Rg1/Re); neck-ring count = age = content; decoction 45-60 min.'),
    ('american_ginseng',  'VI',  'Panax quinquefolius L. | Araliaceae — Type VI Adaptogen. Higher Rb1/lower Rg1 than Asian ginseng; five-leaflet palmate phyllotaxis; identical tuple.'),
    ('ashwagandha',       'VI',  'Withania somnifera (L.) Dunal | Solanaceae — Type VI Adaptogen. Withanolides; horse-smell of cut root IS self-report; winter cherry ripeness encodes root maturity.'),
    ('rhodiola',          'VI',  'Rhodiola rosea L. | Crassulaceae — Type VI Adaptogen. Rosavins/salidroside; rose fragrance of cut root IS self-report; alpine stress increases content.'),
    ('schisandra',        'VI',  'Schisandra chinensis (Turcz.) Baill. | Schisandraceae — Type VI Adaptogen. Five simultaneous flavors of berry IS self-report; vine coil count = age = lignan content.'),
    ('eleuthero',         'VI',  'Eleutherococcus senticosus (Rupr. & Maxim.) Maxim. | Araliaceae — Type VI Adaptogen. Eleutherosides; acicular prickles encode DEREF -> scrape bark.'),
    ('astragalus',        'VI',  'Astragalus membranaceus (Fisch.) Bunge | Fabaceae — Type VI Adaptogen. Astragalosides + polysaccharides; root concentric rings encode LOOP count.'),
    ('jiaogulan',         'VI',  'Gynostemma pentaphyllum (Thunb.) Makino | Cucurbitaceae — Type VI Adaptogen. Gypenosides (convergent with ginsenosides); sweet leaf taste IS self-report.'),
    ('he_shou_wu',        'VI',  'Reynoutria multiflora (Thunb.) Moldenke | Polygonaceae — Type VI Adaptogen. Black processed root (stilbene glycosides) vs. raw (anthraquinone laxative).'),
    ('goji',              'VI',  'Lycium barbarum L. | Solanaceae — Type VI Adaptogen. Polysaccharides/zeaxanthin; berry color saturation IS self-report.'),
    ('shatavari',         'VI',  'Asparagus racemosus Willd. | Asparagaceae — Type VI Adaptogen. Steroidal saponins (shatavarins); tuber number/succulence encodes age and content.'),
    ('guduchi',           'VI',  'Tinospora cordifolia (Willd.) Hook.f. & Thomson | Menispermaceae — Type VI Adaptogen. Stem is pharmaceutical organ; bitter taste IS self-report.'),
    ('amla',              'VI',  'Phyllanthus emblica L. | Phyllanthaceae — Type VI Adaptogen. Highest natural vitamin C; sour-astringent taste IS self-report of tannin content.'),
    ('turmeric',          'VI',  'Curcuma longa L. | Zingiberaceae — Type VI Adaptogen. Curcuminoids; orange color intensity of cut rhizome IS direct self-report.'),
    ('ayahuasca_vine',    'VII', 'Banisteriopsis caapi (Spruce ex Griseb.) C.V.Morton | Malpighiaceae — Type VII Beta-Carboline. Harmala alkaloids (MAO inhibitors); spiral grain count = age = content; two-phase winding.'),
    ('syrian_rue',        'VII', 'Peganum harmala L. | Nitrariaceae — Type VII Beta-Carboline. Harmala alkaloids; seed color/reticulation encodes harmaline; two-phase preparation.'),
    ('iboga',             'VII', 'Tabernanthe iboga Baill. | Apocynaceae — Type VII Beta-Carboline. Ibogaine; root bark bitterness IS potency; biphasic pharmacokinetics = binary winding.'),
    ('voacanga',          'VII', 'Voacanga africana Stapf ex Scott-Elliot | Apocynaceae — Type VII Beta-Carboline. Ibogaine-type alkaloids; root bark bitterness = potency; structurally identical to iboga.'),
    ('yohimbe',           'VII', 'Pausinystalia johimbe (K.Schum.) Pierre ex Beille | Rubiaceae — Type VII Beta-Carboline. Yohimbine; bark thickness/redness encodes alkaloid content; two-phase.'),
    ('tea',               'VIII','Camellia sinensis (L.) Kuntze | Theaceae — Type VIII Caffeine-Purine. Caffeine; no morphological self-report; processing is XOR gate (oxidation -> theaflavins vs. catechins).'),
    ('coffee',            'VIII','Coffea arabica L. | Rubiaceae — Type VIII Caffeine-Purine. Caffeine in seed; cherry color = ripeness not caffeine; decussate phyllotaxis forces trivial winding.'),
    ('kola_nut',          'VIII','Cola acuminata (P.Beauv.) Schott & Endl. | Malvaceae — Type VIII Caffeine-Purine. Caffeine in seed; seed color does not encode caffeine.'),
    ('yerba_mate',        'VIII','Ilex paraguariensis A.St.-Hil. | Aquifoliaceae — Type VIII Caffeine-Purine. Caffeine in leaf; multi-fill gourd protocol is cultural not morphological.'),
    ('guayusa',           'VIII','Ilex guayusa Loes. | Aquifoliaceae — Type VIII Caffeine-Purine. Higher caffeine than mate; entire leaf margin; no morphological self-report.'),
    ('guarana',           'VIII','Paullinia cupana Kunth | Sapindaceae — Type VIII Caffeine-Purine. 2-4x coffee caffeine; eyeball aril appearance is cultural DEREF not pharmaceutical.'),
    ('opium_poppy',       'IX',  'Papaver somniferum L. | Papaveraceae — Type IX Opioid Alkaloid. Morphinan skeleton; 5 stereocenters; capsule crown tilt IS self-report of harvest readiness.'),
    ('kratom',            'IX',  'Mitragyna speciosa (Korth.) Havil. | Rubiaceae — Type IX Opioid Alkaloid. Mitragynine/7-OH-mitragynine; vein color IS direct self-report (red=sedating, white=stimulating).'),
    ('wild_lettuce',      'IX',  'Lactuca virosa L. | Asteraceae — Type IX Opioid Alkaloid. Lactucarium latex; milky->brown oxidation = temporal self-report; boundary case.'),
    ('licorice',          'X',   'Glycyrrhiza glabra L. | Fabaceae — Type X Triterpene Saponin. Glycyrrhizin (50x sweeter than sucrose); sweetness IS self-report; steep not decoct.'),
    ('chinese_licorice',  'X',   'Glycyrrhiza uralensis Fisch. ex DC. | Fabaceae — Type X Triterpene Saponin. Structurally identical to G. glabra; different flavonoid composition.'),
    ('bupleurum',         'X',   'Bupleurum chinense DC. | Apiaceae — Type X Triterpene Saponin. Saikosaponins; bitter root taste IS self-report; decoction required.'),
    ('platycodon',        'X',   'Platycodon grandiflorus (Jacq.) A.DC. | Campanulaceae — Type X Triterpene Saponin. Platycodin saponins; mucilaginous root texture encodes saponin content.'),
    ('reishi',            'XI',  'Ganoderma lucidum (Curtis) P.Karst. | Ganodermataceae — Type XI Fungal Interface. Ganoderic acids; lacquered surface intensity = triterpenoid content; two-phase extraction.'),
    ('turkey_tail',       'XI',  'Trametes versicolor (L.) Lloyd | Polyporaceae — Type XI Fungal Interface. PSK/PSP polysaccharides; concentric color zones = species ID; white pore surface = DEREF.'),
    ('lions_mane',        'XI',  'Hericium erinaceus (Bull.) Pers. | Hericiaceae — Type XI Fungal Interface. Erinacines/hericenones (NGF); cascading teeth morphology encodes neurotrophic function.'),
    ('cordyceps',         'XI',  'Ophiocordyceps sinensis (Berk.) G.H.Sung et al. | Ophiocordycipitaceae — Type XI Fungal Interface. Cordycepin/polysaccharides; caterpillar-fungus composite = prerequisite encoding.'),
    ('chaga',             'XI',  'Inonotus obliquus (Ach. ex Pers.) Pilat | Hymenochaetaceae — Type XI Fungal Interface. Betulinic acid/melanin; black cracked exterior = age self-report; birch host IS prerequisite.'),
    ('maitake',           'XI',  'Grifola frondosa (Dicks.) Gray | Meripilaceae — Type XI Fungal Interface. Grifolan beta-glucan (D-fraction); overlapping fan-shaped caps; white pore surface = DEREF.'),
    ('shiitake',          'XI',  'Lentinula edodes (Berk.) Pegler | Omphalotaceae — Type XI Fungal Interface. Lentinan beta-glucan; boundary case; self-modeling weaker than reishi or cordyceps.'),

    # ── Africa (99–122 minus cross-refs 106, 108, 111, 112) ──────────────────
    ('african_wormwood',  'I',   'Artemisia afra Jacq. ex Willd. | Asteraceae — Type I Aromatic Baseline. Thujone/1,8-cineole/camphor; structurally identical to European wormwood.'),
    ('african_sage',      'I',   'Salvia africana L. | Lamiaceae — Type I Aromatic Baseline. Brownish-golden flowers; rugose leaf texture IS self-report of terpenoid richness.'),
    ('buchu',             'I',   'Agathosma betulina (P.J.Bergius) Pillans | Rutaceae — Type I Aromatic Baseline. Peltate glandular trichomes; diosphenol/menthone/limonene; pungent odor IS self-report.'),
    ('african_ginger',    'I',   'Siphonochilus aethiopicus (Schweinf.) B.L.Burtt | Zingiberaceae — Type I Aromatic Baseline. Aromatic rhizome; pink-purple color when fresh is species-specific self-report.'),
    ('rooibos',           'IV',  'Aspalathus linearis (Burm.f.) R.Dahlgren | Fabaceae — Type IV Non-Critical Aromatic. Needle-like leaves; aspalathin/nothofagin content not morphologically encoded.'),
    ('egyptian_henbane',  'II',  'Hyoscyamus muticus L. | Solanaceae — Type II Tropane. Highest scopolamine of any Solanaceae; stickier leaf texture IS self-report of higher alkaloid content.'),
    ('african_thorn_apple','II', 'Datura metel L. | Solanaceae — Type II Tropane. Trumpet-shaped flowers; spiny capsule; fetid odor of crushed leaf IS self-report.'),
    ('iboga_shrub',       'VII', 'Tabernanthe iboga Baill. shrub form | Apocynaceae — Type VII Beta-Carboline. Shrub form (1-2 m); same structural tuple as tree form iboga; lower root bark yield.'),
    ('ancistrocladus',    'VII', 'Ancistrocladus spp. | Ancistrocladaceae — Type VII Beta-Carboline. Naphthylisoquinoline alkaloids; hook-bearing stems encode DEREF upward to alkaloid-rich leaves.'),
    ('african_dream_herb','IX',  'Entada rheedii Spreng. | Fabaceae — Type IX Opioid Alkaloid. Oneirogenic alkaloids in massive sea-bean seeds; frozen-order extraction via hard woody testa.'),
    ('devils_claw',       'VI',  'Harpagophytum procumbens (Burch.) DC. ex Meisn. | Pedaliaceae — Type VI Adaptogen. Harpagoside; hooked fruit encodes DEREF downward to tuber; decoction 20-30 min.'),
    ('hoodia',            'VI',  'Hoodia gordonii (Masson) Sweet ex Decne. | Apocynaceae — Type VI Adaptogen. P57 pregnane glycoside; bitter stem taste IS self-report; boundary case.'),
    ('kanna',             'I',   'Sceletium tortuosum (L.) N.E.Br. | Aizoaceae — Type I Aromatic Baseline. Mesembrine (serotonin reuptake inhibitor); succulent leaves; fermentation = preparation protocol.'),
    ('pelargonium',       'VI',  'Pelargonium sidoides DC. | Geraniaceae — Type VI Adaptogen. Coumarins/proanthocyanidins/stilbenes; dark root color IS self-report; decoction 20-30 min.'),
    ('african_potato',    'VI',  'Hypoxis hemerocallidea Fisch. et al. | Hypoxidaceae — Type VI Adaptogen. Hypoxoside prodrug -> rooperol (via gut microbiome); yellow corm color IS self-report.'),
    ('griffonia',         'VIII','Griffonia simplicifolia (DC.) Baill. | Fabaceae — Type VIII Caffeine-Purine. 5-HTP (serotonin precursor); single compound class; no morphological self-report.'),
    ('khat',              'VIII','Catha edulis (Vahl) Forssk. ex Endl. | Celastraceae — Type VIII Caffeine-Purine. Cathinone; 48-hour degradation window IS temporal self-report; fresh leaf only.'),
    ('myrrh',             'I',   'Commiphora myrrha (Nees) Engl. | Burseraceae — Type I Aromatic Baseline. Oleo-gum-resin; thorny branches encode DEREF to resin; color/fragrance IS self-report.'),
    ('frankincense',      'I',   'Boswellia sacra Flueck. | Burseraceae — Type I Aromatic Baseline. Boswellic acids; resin color gradient encodes compound profile (pale=monoterpenes, dark=boswellic acids).'),
    ('pygeum',            'VI',  'Prunus africana (Hook.f.) Kalkman | Rosaceae — Type VI Adaptogen. Phytosterols/triterpenoids for BPH; red-brown bark and bitter taste IS self-report.'),

    # ── Americas (123–143 minus cross-refs 131, 135, 136, 137, 140, 141) ──────
    ('white_sage',        'I',   'Salvia apiana Jeps. | Lamiaceae — Type I Aromatic Baseline. Extreme white-canescent trichome density; 1,8-cineole/camphor/alpha-pinene; smudge stick IS compiled program.'),
    ('yerba_buena',       'I',   'Clinopodium douglasii (Benth.) Kuntze | Lamiaceae — Type I Aromatic Baseline. Western North American mint; minty-camphoraceous aroma IS self-report.'),
    ('sweetgrass',        'I',   'Hierochloe odorata (L.) P.Beauv. | Poaceae — Type I Aromatic Baseline. Coumarin-rich; fragrance intensifies with drying; braiding IS preparation instruction.'),
    ('echinacea',         'VI',  'Echinacea purpurea (L.) Moench | Asteraceae — Type VI Adaptogen. Alkylamides/caffeic acid/polysaccharides; spiny cone IS DEREF; floret reflex = developmental self-report.'),
    ('goldenseal',        'VI',  'Hydrastis canadensis L. | Ranunculaceae — Type VI Adaptogen. Berberine; vivid gold color of rhizome IS direct self-report.'),
    ('black_cohosh',      'VI',  'Actaea racemosa L. | Ranunculaceae — Type VI Adaptogen. Triterpene glycosides; dark knotty root encodes age; wand-like inflorescence = spatial identity pointer.'),
    ('slippery_elm',      'VI',  'Ulmus rubra Muhl. | Ulmaceae — Type VI Adaptogen. Mucilage polysaccharide; slippery texture when wet IS self-report; boundary case.'),
    ('boneset',           'IV',  'Eupatorium perfoliatum L. | Asteraceae — Type IV Non-Critical Aromatic. Perfoliate leaves encode no pharmaceutical content; sesquiterpene lactones not morphologically encoded.'),
    ('chacruna',          'VII', 'Psychotria viridis Ruiz & Pav. | Rubiaceae — Type VII Beta-Carboline. DMT-containing admixture leaf; stipules mark growing tip with highest DMT concentration.'),
    ('chaliponga',        'VII', 'Diplopterys cabrerana (Cuatrec.) B.Gates | Malpighiaceae — Type VII Beta-Carboline. DMT-containing vine; ovate drip-tip leaves; complementary to ayahuasca vine.'),
    ('yopo',              'VII', 'Anadenanthera peregrina (L.) Speg. | Fabaceae — Type VII Beta-Carboline. Bufotenin (5-HO-DMT); spirally twisted seed pod encodes winding instruction.'),
    ('yaupon_holly',      'VIII','Ilex vomitoria Aiton | Aquifoliaceae — Type VIII Caffeine-Purine. Only North American native caffeine plant; purification ritual use; no morphological self-report.'),
    ('cacao',             'VIII','Theobroma cacao L. | Malvaceae — Type VIII Caffeine-Purine. Theobromine in seed; woody pod encodes DEREF; seed bitterness IS self-report.'),
    ('pacific_yew',       'V',   'Taxus brevifolia Nutt. | Taxaceae — Type V Axiom A / Eternal. Paclitaxel source; 11 stereocenters; bark = pharmaceutical organ; destructive harvest.'),
    ('mayapple',          'V',   'Podophyllum peltatum L. | Berberidaceae — Type V Axiom A / Eternal. Podophyllotoxin; eternal chirality; umbrella leaf; flowering = harvest readiness signal.'),

    # ── Australia & Oceania (144–154) ─────────────────────────────────────────
    ('tea_tree',                    'I',  'Melaleuca alternifolia (Maiden & Betche) Cheel | Myrtaceae — Type I Aromatic Baseline. Terpinen-4-ol dominant; oil glands visible through leaf IS direct DEREF.'),
    ('eucalyptus_blue_gum',         'I',  'Eucalyptus globulus Labill. | Myrtaceae — Type I Aromatic Baseline. 1,8-cineole dominant; juvenile/adult leaf XOR gate; oil glands visible as translucent dots.'),
    ('eucalyptus_narrow_peppermint','I',  'Eucalyptus radiata Sieber ex DC. | Myrtaceae — Type I Aromatic Baseline. Higher alpha-terpineol/limonene; narrower leaves encode lower shear threshold.'),
    ('lemon_myrtle',                'I',  'Backhousia citriodora F.Muell. | Myrtaceae — Type I Aromatic Baseline. 90-98% citral; lemon scent on crushing IS unambiguous self-report; highest citral of any plant.'),
    ('aniseed_myrtle',              'I',  'Syzygium anisatum (Vickery) Craven & Biffin | Myrtaceae — Type I Aromatic Baseline. Anethole-dominant leaf; translucent oil glands; anise fragrance IS self-report.'),
    ('lemon_tea_tree',              'I',  'Leptospermum petersonii F.M.Bailey | Myrtaceae — Type I Aromatic Baseline. Citronellal/neral/geranial profile; narrow linear leaves with entire margins.'),
    ('river_mint',                  'I',  'Mentha australis R.Br. | Lamiaceae — Type I Aromatic Baseline. Native Australian mint; serrate ovate leaves; structurally identical to Northern Hemisphere mints.'),
    ('kakadu_plum',                 'IV', 'Terminalia ferdinandiana Exell | Combretaceae — Type IV Non-Critical Aromatic. Highest natural vitamin C; yellow-green fruit; sourness does not linearly track ascorbic acid.'),
    ('native_ginger',               'I',  'Alpinia caerulea (R.Br.) Benth. | Zingiberaceae — Type I Aromatic Baseline. Blue fruit (species ID only); aromatic rhizome encodes same DEREF -> PUSH as Asian ginger.'),
    ('wattleseed',                  'IV', 'Acacia spp. | Fabaceae — Type IV Non-Critical Aromatic. Roasted seed; Maillard flavor IS processing self-report; boundary food/pharmaceutical.'),
    ('quandong',                    'IV', 'Santalum acuminatum (R.Br.) A.DC. | Santalaceae — Type IV Non-Critical Aromatic. Bright red fruit; high vitamin C; fruit color encodes species identity not content.'),
]


def build_entry(key, type_code, description):
    vals = TYPE_TUPLES[type_code]
    entry = {'name': key, 'description': description}
    for prim, val in zip(PRIMITIVES, vals):
        entry[prim] = val
    return entry


def main():
    repo_root = Path(__file__).parent.parent
    catalog_path = repo_root / 'data' / 'IG_catalog.json'

    if not catalog_path.exists():
        print(f'ERROR: catalog not found at {catalog_path}', file=sys.stderr)
        sys.exit(1)

    with open(catalog_path, encoding='utf-8') as f:
        catalog = json.load(f)

    existing = {e['name'] for e in catalog}
    before = len(catalog)

    added = 0
    skipped = 0
    for key, type_code, description in ENTRIES:
        if key in existing:
            skipped += 1
        else:
            catalog.append(build_entry(key, type_code, description))
            existing.add(key)
            added += 1

    with open(catalog_path, 'w', encoding='utf-8') as f:
        json.dump(catalog, f, indent=2, ensure_ascii=False)

    print(f'Catalog: {before} -> {len(catalog)} entries')
    print(f'Added {added}. Skipped {skipped} (already in catalog).')


if __name__ == '__main__':
    main()
