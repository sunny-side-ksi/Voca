"""TC_0513 Q67-Q128 (Manhattan 5lb Chapter 3) -> practice_questions.json"""
import json
import string
from pathlib import Path

DATA_FILE = Path(__file__).parent / "gre_content" / "practice_questions.json"
L = list(string.ascii_uppercase)


def make_q(qid, stem, blank_defs, answer_words, diff="medium"):
    blanks, correct = [], []
    idx = 0
    for (label, choices), ans in zip(blank_defs, answer_words):
        ch = {L[idx + j]: choices[j] for j in range(len(choices))}
        blanks.append({"label": label, "choices": ch})
        for j, c in enumerate(choices):
            if c.lower().strip() == ans.lower().strip():
                correct.append(L[idx + j]); break
        idx += len(choices)
    n = len(blank_defs)
    subtype = ["single_blank", "double_blank", "triple_blank"][n - 1]
    return {"id": qid, "section": "verbal", "type": "text_completion",
            "subtype": subtype, "difficulty": diff, "set": None, "passage": None,
            "stem": stem, "blanks": blanks, "correct": correct,
            "explanation": "", "source": "TC_0513"}


questions = [

# Q67
make_q("TC0513_67",
    "Although this historical figure had been (i)__________ politician and a brilliant inventor, the professor found herself unable to (ii)__________ the interest of her students in the career of a man with such outdated views.",
    [("Blank (i)",  ["an insipid", "an adept", "an effete"]),
     ("Blank (ii)", ["whet", "accrue", "tout"])],
    ["an effete", "whet"]),

# Q68
make_q("TC0513_68",
    "The comedian's __________ wit has long been the cause of the polarized sentiments she evokes in her audience; some adore her caustic sense of humor, while others abhor it.",
    [("Blank", ["ample", "acerbic", "anachronistic", "abstruse", "astounding"])],
    ["acerbic"]),

# Q69
make_q("TC0513_69",
    "Contrary to the assumptions that many Westerners hold about mindfulness practices, meditation is often anything but __________; while using various methods to calm the mind, meditators frequently experience intense periods of restlessness and doubt.",
    [("Blank", ["beneficial", "mystical", "orthodox", "benign", "halcyon"])],
    ["halcyon"]),

# Q70
make_q("TC0513_70",
    "Faced with __________ population attempting to compete for the few available jobs.",
    [("Blank", ["a myopic", "an anemic", "a botched", "a booming", "an educated"])],
    ["an educated"]),

# Q71
make_q("TC0513_71",
    "Despite his longtime advocacy for campaign finance reform, the career politician was, in fact, far more (i)__________ corporate interests than his rival, whose relatively recent entry into the political arena meant that he had far fewer (ii)__________ to make good on.",
    [("Blank (i)",  ["leery of", "beholden to", "apathetic about"]),
     ("Blank (ii)", ["affiliations", "dilemmas", "obligations"])],
    ["beholden to", "obligations"]),

# Q72
make_q("TC0513_72",
    "Far too (i)__________ to consider a career in the political limelight, the unassuming aide contented herself with a career behind the scenes, (ii)__________ supporting the political heavyweights of her day.",
    [("Blank (i)",  ["diffident", "apathetic", "ideological"]),
     ("Blank (ii)", ["implicitly", "quietly", "skeptically"])],
    ["diffident", "quietly"]),

# Q73
make_q("TC0513_73",
    "There are many good reasons to construct urban traffic lanes for cyclists: city infrastructure is already __________ under the strain of excess auto traffic, and the safety advantages of limiting road-sharing between cyclists and vehicles are all too clear.",
    [("Blank", ["seething", "waiting", "groaning", "baying", "intensifying"])],
    ["groaning"]),

# Q74
make_q("TC0513_74",
    "Though the professor had made her (i)__________ tendencies clear to the hiring committee, the extent and consistency of her (ii)__________ was still a surprise to many who had voted to approve her hiring: she openly challenged the accepted norms of her field and of the university as a whole, going so far as to advocate for the (iii)__________ of inherently elitist institutions of higher education in the name of democratizing education.",
    [("Blank (i)",   ["intellectual", "illiberal", "heterodox"]),
     ("Blank (ii)",  ["iconoclasm", "theories", "intelligence"]),
     ("Blank (iii)", ["abolition", "enshrinement", "mitigation"])],
    ["heterodox", "iconoclasm", "abolition"]),

# Q75
make_q("TC0513_75",
    "The apparent simplicity of a cup of coffee __________ the dizzying number of hours of toil required to produce it, from months of cultivation of the bean tree to painstaking refinement in highly sophisticated machinery.",
    [("Blank", ["redresses", "confirms", "belies", "furnishes", "fosters"])],
    ["belies"]),

# Q76
make_q("TC0513_76",
    "Notwithstanding the mishmash of worn tools littering every surface of the artist's studio, the place exuded a certain sense of order manifest through the clutter; the decor was, if (i)__________, (ii)__________.",
    [("Blank (i)",  ["unkempt", "dire", "arduous"]),
     ("Blank (ii)", ["largely unsophisticated", "positively callous", "surprisingly deliberate"])],
    ["unkempt", "surprisingly deliberate"]),

# Q77
make_q("TC0513_77",
    "Two years after the legislature's (i)__________ approval of the community arts center, construction came to an equally public standstill, largely due to the unforeseen hemorrhaging of the (ii)__________ funds at the hands of spendthrift leaders.",
    [("Blank (i)",  ["scorned", "heralded", "ratified"]),
     ("Blank (ii)", ["stolen", "exacerbated", "appropriated"])],
    ["heralded", "appropriated"]),

# Q78
make_q("TC0513_78",
    "Incensed, and perhaps spooked, by the implications of the bureau's purportedly (i)__________ inquisitions, the Hollywood film director shuttered his studios, suspended production of numerous projects, and (ii)__________ with his wife to Europe.",
    [("Blank (i)",  ["benign", "risque", "amicable"]),
     ("Blank (ii)", ["immigrated", "decamped", "pandered"])],
    ["risque", "decamped"]),

# Q79
make_q("TC0513_79",
    "The relationship between the two leaders has gone from positively (i)__________ to chilly at best, not least because the recent arms scandal threatens to (ii)__________ the mutual trust that has been held on both sides for years.",
    [("Blank (i)",  ["peaceful", "reverent", "congenial"]),
     ("Blank (ii)", ["bolster", "erode", "fester"])],
    ["congenial", "erode"]),

# Q80
make_q("TC0513_80",
    "In an age of near-instantaneous fact checking, political candidates must be careful of making spontaneous statements intended to appease a crowd, as any fictitious claim will inevitably be found to be __________.",
    [("Blank", ["bogus", "genuine", "unnecessary", "unfamiliar", "specious"])],
    ["bogus"]),

# Q81
make_q("TC0513_81",
    "His grandmother's house was always a bedlam of porcelain figurines, collector's spoons, and other (i)__________ doodads. But it hardly would have been (ii)__________ to tell her that he thought her choice of decor was vulgar; in fact, he had to think (iii)__________ because the avaricious youth was gunning for a big birthday present from her.",
    [("Blank (i)",   ["tacky", "vitreous", "grizzled"]),
     ("Blank (ii)",  ["discerning", "rancorous", "doting"]),
     ("Blank (iii)", ["amicably", "tactically", "duplicitously"])],
    ["tacky", "discerning", "tactically"]),

# Q82
make_q("TC0513_82",
    "The captain (i)__________ for as long as he could, but eventually the crew became frustrated with the small portions of mead and the dearth of plunder, and decided to take matters into their own hands.",
    [("Blank (i)",  ["dissuaded", "warded off", "depreciated"]),
     ("Blank (ii)", ["sea change", "mutiny", "helmsmanship"])],
    ["warded off", "mutiny"]),

# Q83
make_q("TC0513_83",
    "Of course, we would all like to believe that our every success is of our own manufacture, but to believe that is to neglect the (i)__________ element present in all lives, beginning with a birth lottery that assigns to some such gifts as intelligence and to others such (ii)__________ as wealth.",
    [("Blank (i)",  ["common", "inchoate", "serendipitous"]),
     ("Blank (ii)", ["encumbrances", "dispensations", "piques"])],
    ["serendipitous", "dispensations"]),

# Q84
make_q("TC0513_84",
    "The eyes of the mantis shrimp have more types of photoreceptors, or color-detecting cells, than those of any other animal on the planet. While one would think that this would allow the mantis shrimp to better (i)__________ colors, researchers have found this to be (ii)__________.",
    [("Blank (i)",  ["improve", "discriminate", "illiberal"]),
     ("Blank (ii)", ["baseless", "obvious", "apparent"])],
    ["discriminate", "baseless"]),

# Q85
make_q("TC0513_85",
    "Jackson's supporters praised his earthy speech as evidence of his common touch, while his (i)__________ condemned it as (ii)__________.",
    [("Blank (i)",  ["interlocutors", "detractors", "contemporaries"]),
     ("Blank (ii)", ["vulgar", "obtuse", "genteel"])],
    ["detractors", "vulgar"]),

# Q86
make_q("TC0513_86",
    "Economists have developed such sophisticated and (i)__________ mathematical tools for modeling human behavior that other social scientists often employ those tools to model and help (ii)__________ even decisions that have no obvious economic consequences.",
    [("Blank (i)",  ["eclectic", "populist", "versatile"]),
     ("Blank (ii)", ["interpolate", "extrapolate", "explicate"])],
    ["versatile", "extrapolate"]),

# Q87
make_q("TC0513_87",
    "Patients who stop taking antibiotics when symptoms subside contribute to the evolution of drug-resistant strains, because an incomplete course of treatment spares the most __________ bacteria.",
    [("Blank", ["widespread", "immature", "robust", "benign", "notorious"])],
    ["robust"]),

# Q88
make_q("TC0513_88",
    "Children who are recognized as preternaturally intelligent often go on to fulfill their early promise, contrary to the stereotype of maladjusted __________ wasting their gifts.",
    [("Blank", ["prodigies", "teenagers", "cranks", "theorizers", "pragmatists"])],
    ["prodigies"]),

# Q89
make_q("TC0513_89",
    "Freud's structural model of the psyche should be understood as (i)__________ device, useful for inciting and guiding discovery, rather than as an attempt to (ii)__________ physical relationships among parts of the human brain.",
    [("Blank (i)",  ["a heuristic", "a literary", "an allegorical"]),
     ("Blank (ii)", ["dictate", "ameliorate", "represent"])],
    ["a heuristic", "represent"]),

# Q90
make_q("TC0513_90",
    "The silent-film pioneer Harold Lloyd made a virtue of the (i)__________ limits of his day, playing men so (ii)__________ it was easy to imagine it was the character rather than the medium who lacked a voice.",
    [("Blank (i)",  ["artistic", "commercial", "technical"]),
     ("Blank (ii)", ["avant-garde", "diffident", "reluctant"])],
    ["technical", "diffident"]),

# Q91
make_q("TC0513_91",
    "When first introduced by senior management, the new boss was viewed as a figurehead at best, but after months of watching him shake up the office hierarchy and double productivity, even the most __________ of his employees was astonished at what he was able to accomplish.",
    [("Blank", ["scrutinized", "clueless", "skeptical", "senior", "resolute"])],
    ["skeptical"]),

# Q92
make_q("TC0513_92",
    "Critics of media consolidation say that it has resulted in both a (i)__________ of unique viewpoints and a lack of local news coverage, with news conglomerates that often discuss the same issues across all platforms, while (ii)__________ regional coverage, cannot afford to (iii)__________ enough full-time reporters.",
    [("Blank (i)",   ["banality", "deviation", "scarcity"]),
     ("Blank (ii)",  ["elaborate", "domestic", "regional"]),
     ("Blank (iii)", ["staff", "imply", "broadcast"])],
    ["scarcity", "regional", "staff"]),

# Q93
make_q("TC0513_93",
    "The writer's efforts at mainstream novels (i)__________ his ability to represent the more (ii)__________ world.",
    [("Blank (i)",  ["attest to", "belie", "gainsay"]),
     ("Blank (ii)", ["ebullient", "quotidian", "fantastical"])],
    ["belie", "quotidian"]),

# Q94
make_q("TC0513_94",
    "The independent audit showed that the company was not __________, let alone flourishing, as its initial report to its stockholders tried to aver.",
    [("Blank", ["copious", "evasive", "thriving", "unprecedented", "solvent"])],
    ["solvent"]),

# Q95
make_q("TC0513_95",
    "A business that, when it receives a requisite amount of regulatory pressure, (i)__________ its own non-compliance with industry safety standards with yet another series of suspect omissions is of the most highly (ii)__________ variety.",
    [("Blank (i)",  ["imbues", "verifies", "supplants"]),
     ("Blank (ii)", ["laudable", "contrived", "contemptible"])],
    ["supplants", "contemptible"]),

# Q96
make_q("TC0513_96",
    "The new employee's relaxed demeanor during the job interview belied a vastly more __________ style on the job, a fact that he learned to his chagrin within the first few days of employment.",
    [("Blank", ["draconian", "friendly", "fatuous", "illicit", "nonplussed"])],
    ["draconian"]),

# Q97
make_q("TC0513_97",
    "(i)__________ comprehension of the character of Italian wine is impeded not only by labyrinthine complexities of vineyards and varietals, but also by fluctuations in environmental conditions from year to year, which render even the most reliable vintages subject to (ii)__________.",
    [("Blank (i)",  ["An exhaustive", "A futile", "An irredeemable"]),
     ("Blank (ii)", ["efficient taxonomy", "remarkable variance", "mitigating circumstances"])],
    ["An exhaustive", "remarkable variance"]),

# Q98
make_q("TC0513_98",
    "Added to the (i)__________ with which the clerk seems to treat his clients is what appears to be a more general lack of respect for his office; he seems to treat the whole thing as if it were some grand (ii)__________.",
    [("Blank (i)",  ["casual nonchalance", "profound meticulousness", "idle envy"]),
     ("Blank (ii)", ["gesture", "farce", "tirade"])],
    ["casual nonchalance", "farce"]),

# Q99
make_q("TC0513_99",
    "According to critics, the novelist's latest effort, with its dry pedantry and humorless presentation, managed to make a seemingly (i)__________ subject matter into (ii)__________ collection of poorly constructed sentences.",
    [("Blank (i)",  ["engaging", "affectless", "dogmatic"]),
     ("Blank (ii)", ["a worthy", "a tired", "an instructive"])],
    ["engaging", "a tired"]),

# Q100
make_q("TC0513_100",
    "The more deeply one delves into the relevant literature, the more apparent it becomes that psychoanalysis is a practice (i)__________. Even tenets that some might deem (ii)__________ to the general philosophy, such as the notion that the human psyche is primarily governed by conflicting desires and is formed in large part by early childhood experiences, are by no means accepted as gospel, even by some of its most (iii)__________.",
    [("Blank (i)",   ["teeming with ridicule", "devoid of substance", "rife with contention"]),
     ("Blank (ii)",  ["critical", "immaterial", "anathema"]),
     ("Blank (iii)", ["esteemed beneficiaries", "quarrelsome factions", "seasoned practitioners"])],
    ["rife with contention", "critical", "seasoned practitioners"]),

# Q101
make_q("TC0513_101",
    "The pair's apparent antagonism could easily be written off as (i)__________ pure and simple, but further scrutiny should render (ii)__________ the fact that the rivalry also confers a fair amount of (iii)__________, as it provides each with an opportunity to derive motivation and inspiration from the other.",
    [("Blank (i)",   ["hypocrisy", "antipathy", "flagrancy"]),
     ("Blank (ii)",  ["useless", "patent", "spurious"]),
     ("Blank (iii)", ["worthless pride", "mutual benefit", "tacit disagreement"])],
    ["antipathy", "patent", "mutual benefit"]),

# Q102
make_q("TC0513_102",
    "In this day and age, side show barkers, competing with the unfathomable number of spectacular oddities daily displayed on the internet for free, must increasingly lard their pitches with flights of fancy and soaring __________, arching far beyond reality, to fill the seats in their arcades.",
    [("Blank", ["tit for tat", "parables", "conundrums", "innuendos", "hyperboles"])],
    ["hyperboles"]),

# Q103
make_q("TC0513_103",
    "(i)__________, the law had little impact, but it was (ii)__________ by subsequent legislation providing funding and enforcement.",
    [("Blank (i)",  ["Justifiably", "Unbelievably", "Initially"]),
     ("Blank (ii)", ["rendered moot", "given teeth", "kept at bay"])],
    ["Initially", "given teeth"]),

# Q104
make_q("TC0513_104",
    "Evoking both horror and joy in its audience in equal measure, the opera became an instant classic of __________ technique.",
    [("Blank", ["macabre", "figurative", "articulate", "counterpoint", "contrived"])],
    ["counterpoint"]),

# Q105
make_q("TC0513_105",
    "The famous Notre Dame cathedral in Paris took almost 200 years to complete; this immense architectural effort included the first notable use of a flying __________, but this renowned feature was not part of the original design and was only employed when the walls forming the nave began to crumble and needed additional support.",
    [("Blank", ["partition", "albatross", "hallmark", "buttress", "trademark"])],
    ["buttress"]),

# Q106
make_q("TC0513_106",
    "While no single empirical investigation can ever conclusively prove the (i)__________ of a theory, the fact that the data are (ii)__________ findings from over a dozen independent labs worldwide bodes well for the framework's resilience.",
    [("Blank (i)",  ["rationality", "veracity", "candor"]),
     ("Blank (ii)", ["consistent with", "founded on", "antithetical to"])],
    ["veracity", "consistent with"]),

# Q107
make_q("TC0513_107",
    "A full account of the complexities of sleep, sought after by scientists, philosophers and mystics for millennia, continues to elude us. That we are still so ignorant about a topic so (i)__________ to our daily lives is at once fascinating and (ii)__________.",
    [("Blank (i)",  ["mysterious", "obscure", "pertinent"]),
     ("Blank (ii)", ["deeply humbling", "fully impenetrable", "totally blatant"])],
    ["pertinent", "deeply humbling"]),

# Q108
make_q("TC0513_108",
    "Mozart's brief life exemplified a discrepancy between fame and means: as his musical stardom (i)__________ beyond measure, his income (ii)__________.",
    [("Blank (i)",  ["abated", "grew exponentially", "waxed"]),
     ("Blank (ii)", ["remained exorbitant", "dwindled", "barely stirred"])],
    ["waxed", "dwindled"]),

# Q109
make_q("TC0513_109",
    "Finally, after refusing for a decade, the family patriarch, weakened by age and infirmity, surrendered to the impassioned pleas of his avaricious nieces, and gave his __________ to the risky investment stratagem.",
    [("Blank", ["assent", "ascent", "dissent", "descent", "assertion"])],
    ["assent"]),

# Q110
make_q("TC0513_110",
    "Even thrill-seeking visitors to amusement parks will avoid those attractions with a reputation for real (i)__________, like those at the now-shuttered Action Park. These patrons want not danger but its (ii)__________, a ride that (iii)__________ but is in fact perfectly safe.",
    [("Blank (i)",   ["peril", "titillation", "lavishness"]),
     ("Blank (ii)",  ["complement", "simulacrum", "abettor"]),
     ("Blank (iii)", ["satisfies", "mollifies", "terrifies"])],
    ["peril", "simulacrum", "terrifies"]),

# Q111
make_q("TC0513_111",
    "Desktop publishing allows (i)__________ to do for themselves the work once reserved for professionals whose (ii)__________ or other training developed design skills along with narrow technical mastery.",
    [("Blank (i)",  ["dilettantes", "artisans", "ideologues"]),
     ("Blank (ii)", ["sensibility", "acumen", "apprenticeship"])],
    ["dilettantes", "apprenticeship"]),

# Q112
make_q("TC0513_112",
    "The opening act's stage presence was far less (i)__________ as those of the singer who followed, whose stage presence was far more (ii)__________.",
    [("Blank (i)",  ["unremarkable", "hackneyed", "arresting"]),
     ("Blank (ii)", ["charismatic", "pedestrian", "experienced"])],
    ["arresting", "charismatic"]),

# Q113
make_q("TC0513_113",
    "The contradictions in the philosopher's life were more (i)__________ because he was celebrated for his prodigal intellectual (ii)__________ that led to his profound insights.",
    [("Blank (i)",  ["insightful", "confounding", "unpremeditated"]),
     ("Blank (ii)", ["acumen", "vacuity", "veracity"])],
    ["confounding", "acumen"]),

# Q114
make_q("TC0513_114",
    "If impact on one's contemporaries is the test of (i)__________, Flann O'Brien's The Third Policeman cannot be said to be among the most significant postmodern novels, as it went unpublished and unread for 27 years. The literary theorist Keith Hopper, though, appeals to standards other than peer (ii)__________ when he argues persuasively that The Third Policeman is among the most important of early postmodern works, not least because of its deep subversion of both enlightenment and modern traditions in literature.",
    [("Blank (i)",  ["eminence", "modishness", "conversance"]),
     ("Blank (ii)", ["currency", "influence", "relevance"])],
    ["eminence", "influence"]),

# Q115
make_q("TC0513_115",
    "One liberal activist asserts that politicians' tendency to (i)__________ talk of class warfare stems largely from a communal state of denial, a refusal to accept that we already occupy a highly (ii)__________ society.",
    [("Blank (i)",  ["denigrate", "besmirch", "encourage"]),
     ("Blank (ii)", ["socialized", "balkanized", "politicized"])],
    ["denigrate", "balkanized"]),

# Q116
make_q("TC0513_116",
    "In the course of a transatlantic voyage following the First World War, he magically acquired an honorific title of Count as well as a 'von' in his name, a development due to his aquiline nose and social (i)__________ rather than his (ii)__________ genetics, which lacked any distinction, and he (iii)__________ successfully enough in New York City to parlay this charade into a small fortune.",
    [("Blank (i)",   ["arrogance", "deftness", "maladroitness"]),
     ("Blank (ii)",  ["peasant", "patrician", "perturbing"]),
     ("Blank (iii)", ["coalesced", "dissembled", "disseminated"])],
    ["deftness", "peasant", "dissembled"]),

# Q117
make_q("TC0513_117",
    "There is little agreement among specialists about whether the Second Amendment to the United States Constitution provides __________ guarantee of a right to bear arms for private citizens, or whether it was instead meant to allow the populace to protect itself in lieu of a military.",
    [("Blank", ["an earnest", "an amended", "a questionable", "a defeasible", "an ironclad"])],
    ["an ironclad"]),

# Q118
make_q("TC0513_118",
    "The writer Lillian Hellman honestly called her disingenuous argumentative strategy 'the nobility racket': a __________ that involved taking the moral high ground no matter how removed from the subject at hand.",
    [("Blank", ["philosophy", "sophistry", "sinecure", "volubility", "serendipity"])],
    ["sophistry"]),

# Q119
make_q("TC0513_119",
    "The fitness guru __________ his integrity by consuming vast quantities of sugar and chemical-riddled junk food behind closed doors.",
    [("Blank", ["ridiculed", "restored", "undermined", "redacted", "insinuated"])],
    ["undermined"]),

# Q120
make_q("TC0513_120",
    "The presence of unexploded World War II munitions scattered throughout various European cities is very (i)__________, since one can easily imagine becoming a (ii)__________ of a war that ended decades ago.",
    [("Blank (i)",  ["exhilarating", "disquieting", "demeaning"]),
     ("Blank (ii)", ["hero", "martyr", "casualty"])],
    ["disquieting", "casualty"]),

# Q121
make_q("TC0513_121",
    "It may be surprising that even perennially (i)__________ reporters have had misgivings about entering the war zone; their (ii)__________ at the prospect can only be a reflection of the heightened (iii)__________ that pervades the region.",
    [("Blank (i)",   ["professional", "dauntless", "foreign"]),
     ("Blank (ii)",  ["trepidation", "excitement", "skepticism"]),
     ("Blank (iii)", ["rhetoric", "peril", "awareness"])],
    ["dauntless", "trepidation", "peril"]),

# Q122
make_q("TC0513_122",
    "One does not generally associate teenagers with (i)__________. Jean, however, exercises a self-discipline that verges on (ii)__________. It is unclear whether this is a testament to a particularly strong will or a reaction against an excessively (iii)__________ upbringing.",
    [("Blank (i)",   ["silent obedience", "polished urbanity", "practiced restraint"]),
     ("Blank (ii)",  ["asperity", "punishment", "asceticism"]),
     ("Blank (iii)", ["illiberal", "permissive", "meddlesome"])],
    ["practiced restraint", "asceticism", "permissive"]),

# Q123
make_q("TC0513_123",
    "Unexpectedly, the actor's (i)__________ behavior did little to (ii)__________ his reputation as a family man, a reputation (iii)__________ by his exceptionally skilled team of publicists.",
    [("Blank (i)",   ["dissolute", "impudent", "paternal"]),
     ("Blank (ii)",  ["assuage", "damage", "temper"]),
     ("Blank (iii)", ["cleverly subverted", "easily refuted", "carefully cultivated"])],
    ["dissolute", "damage", "carefully cultivated"]),

# Q124
make_q("TC0513_124",
    "Now that fresh produce has become (i)__________ — markets and stands in cities throughout the world — the (ii)__________ that were once the inevitable result of nutritional deficiencies are now entirely (iii)__________.",
    [("Blank (i)",   ["salubrious", "organic", "ubiquitous"]),
     ("Blank (ii)",  ["maladies", "reactions", "dietetic"]),
     ("Blank (iii)", ["comestible", "cultivars", "preventable"])],
    ["ubiquitous", "maladies", "preventable"]),

# Q125
make_q("TC0513_125",
    "Despite her (i)__________ position on tax reform, the senator was not (ii)__________ to strike a concessionary tone when she debated the issue with her opponents.",
    [("Blank (i)",  ["conservative", "fiduciary", "hardline"]),
     ("Blank (ii)", ["loath", "permitted", "qualified"])],
    ["hardline", "loath"]),

# Q126
make_q("TC0513_126",
    "There seems to be (i)__________ the practice of medicine in the United States: while it is the duty of medical professionals to maintain the health of their patients, the same professionals stand to profit more from their patients' (ii)__________.",
    [("Blank (i)",  ["a protest against", "an aversion to", "a paradox in"]),
     ("Blank (ii)", ["infirmity", "inattentiveness", "uncertainty"])],
    ["a paradox in", "infirmity"]),

# Q127
make_q("TC0513_127",
    "Whereas early work in the field of spectroscopy (i)__________ the dispersal of visible light by a prism, the concept was later (ii)__________ to (iii)__________ any and all interactions with radiative energy, including electromagnetic radiation, pressure waves, and the kinetic energy of particles.",
    [("Blank (i)",   ["contrasted with", "arose from", "focused on"]),
     ("Blank (ii)",  ["expanded", "transformed", "amended"]),
     ("Blank (iii)", ["affirm", "endure", "include"])],
    ["focused on", "expanded", "include"]),

# Q128
make_q("TC0513_128",
    "While Abdul's __________ with his children made him well loved, he worried what too much laxity might cost him in their teenage years.",
    [("Blank", ["complacence", "sternness", "satisfaction", "equanimity", "permissiveness"])],
    ["permissiveness"]),

]


def main():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    existing_ids = {q["id"] for q in data["verbal"]}
    new_qs = [q for q in questions if q["id"] not in existing_ids]
    skipped = len(questions) - len(new_qs)

    failed = [q for q in new_qs if len(q["correct"]) != len(q["blanks"])]
    valid = [q for q in new_qs if len(q["correct"]) == len(q["blanks"])]

    data["verbal"].extend(valid)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Added: {len(valid)}  |  Skipped(dup): {skipped}  |  Failed: {len(failed)}")
    print(f"Total verbal: {len(data['verbal'])}")

    blanks_count = {"single_blank": 0, "double_blank": 0, "triple_blank": 0}
    for q in valid:
        blanks_count[q["subtype"]] += 1
    print(f"  single: {blanks_count['single_blank']}, double: {blanks_count['double_blank']}, triple: {blanks_count['triple_blank']}")

    if failed:
        print(f"WARNING - answer mapping failed for: {[q['id'] for q in failed]}")
        for q in failed:
            print(f"  {q['id']}: blanks={len(q['blanks'])}, correct={q['correct']}")
    else:
        print("All answer mappings verified OK")


if __name__ == "__main__":
    main()
