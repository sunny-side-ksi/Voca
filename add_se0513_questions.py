"""SE_0513 (Manhattan 5lb Chapter 4 Sentence Equivalence) -> practice_questions.json"""
import json
import string
from pathlib import Path

DATA_FILE = Path(__file__).parent / "gre_content" / "practice_questions.json"
L = list(string.ascii_uppercase)


def se(qid, stem, choices6, correct2, diff="medium"):
    ch = {L[i]: choices6[i] for i in range(len(choices6))}
    correct = sorted([L[choices6.index(c)] for c in correct2])
    return {"id": qid, "section": "verbal", "type": "sentence_equivalence",
            "subtype": "sentence_equivalence", "difficulty": diff, "set": None,
            "passage": None, "stem": stem,
            "blanks": [{"label": "Blank", "choices": ch}],
            "correct": correct, "explanation": "", "source": "SE_0513"}


questions = [

# ── Q1 ──
se("SE0513_01",
   "While the colonists would eventually push westward, first, they were in for a long difficult winter, and the main challenge was to __________ their existing resources.",
   ["sell", "peddle", "steward", "upend", "husband", "procure"],
   ["steward", "husband"]),

# ── Q2 ──
se("SE0513_02",
   "James Joyce, the author of many novels, including Finnegans Wake, saw deeply into the hearts of his characters, but, in a life irony as subtle yet piercing as those endured by his characters, he himself could barely __________ text well enough to proof his own galleys.",
   ["see", "feel", "walk", "move", "distinguish", "interpret"],
   ["see", "distinguish"]),

# ── Q3 ──
se("SE0513_03",
   "At work, she is far less __________ than she is around her friends, but from time to time her staff sees her in a volatile state.",
   ["pretentious", "capricious", "informal", "fickle", "direct", "explicit"],
   ["capricious", "fickle"]),

# ── Q4 ──
se("SE0513_04",
   "Forty years ago, anthropologists firmly believed that Neanderthals and modern homo sapiens could not have interbred; this is a perfect example of the __________ nature of science.",
   ["fallacious", "evolving", "counterfactual", "advancing", "vacillating", "indeterminable"],
   ["evolving", "advancing"]),

# ── Q5 ──
se("SE0513_05",
   "The music of the late '70s is often described as __________, despite the notable exception of a few innovators in the budding punk and hip-hop scenes.",
   ["derivative", "trite", "inspired", "visionary", "enigmatic", "cerebral"],
   ["derivative", "trite"]),

# ── Q6 ──
se("SE0513_06",
   "A field trip was arranged so that this troupe of __________ dancers could observe the real masters of their art.",
   ["seasoned", "fledgling", "expert", "novice", "lithe", "torpid"],
   ["fledgling", "novice"]),

# ── Q7 ──
se("SE0513_07",
   "The exhibit is not so much a retrospective as a __________; the artist's weaker, early work is glossed over, and any evidence of his ultimate dissolution is absent entirely.",
   ["paean", "polemic", "tirade", "panacea", "tribute", "critique"],
   ["paean", "tribute"]),

# ── Q8 ──
se("SE0513_08",
   "After the players had practiced for hours in terrible weather, naturally they would be visibly __________.",
   ["flagging", "hale", "lissome", "loathsome", "vigorous", "enervated"],
   ["flagging", "enervated"]),

# ── Q9 ──
se("SE0513_09",
   "Nothing evoked memories of her grandmother's house like the __________ of scents associated with the variety of dishes at the holiday feast.",
   ["paucity", "anomaly", "medley", "melange", "dearth", "rarity"],
   ["medley", "melange"]),

# ── Q10 ──
se("SE0513_10",
   "Unlike the politician's earlier evasions and equivocations, this latest statement is __________ lie.",
   ["a bald", "a tacit", "an overt", "a didactic", "a rhetorical", "an implicit"],
   ["a bald", "an overt"]),

# ── Q11 ──
se("SE0513_11",
   "Possessed of a lighthearted approach to life, Winnie thought that those who were __________ with regards to values and mores missed out on a certain liveliness and spontaneity.",
   ["lax", "equable", "priggish", "auspicious", "impious", "punctilious"],
   ["priggish", "punctilious"]),

# ── Q12 ──
se("SE0513_12",
   "Where gay and lesbian individuals and couples were once ignored, at best, by mainstream media and marketing companies, they are now being __________ as the new frontier in consumer spending.",
   ["touted", "subverted", "revered", "scrutinized", "promoted", "predicted"],
   ["touted", "promoted"]),

# ── Q13 ──
se("SE0513_13",
   "For most of the 20th century, American political contentions reflected pragmatic rather than ideological differences; candidate debates centered around whether programs were __________.",
   ["partisan", "voluble", "feasible", "innocuous", "prejudiced", "viable"],
   ["feasible", "viable"]),

# ── Q14 ──
se("SE0513_14",
   "Though considered a somewhat somber drama at the time of its release in 1975, the film Shampoo, about a philandering hairdresser, now seems more the __________ comedy.",
   ["puckish", "inhibited", "prurient", "wry", "dated", "puritanical"],
   ["puckish", "wry"]),

# ── Q15 ──
se("SE0513_15",
   "With almost 40 titles to her name, the popular novelist has __________ imagination and is never at a loss for new ideas, though the quality of her works is far from consistent.",
   ["a prolix", "a prolific", "an exemplary", "a fecund", "an ingenious", "a profligate"],
   ["a prolific", "a fecund"]),

# ── Q16 ──
se("SE0513_16",
   "The monarchs of the late medieval period made decisions without regard for precedents.",
   ["capricious", "considered", "malicious", "pessimistic", "insidious", "erratic"],
   ["capricious", "erratic"]),

# ── Q17 ──
se("SE0513_17",
   "Because the Lewis and Clark expedition through the West was conceived primarily as a mapping project, government officials were __________ by the wealth of information on a myriad of topics that the explorers gathered.",
   ["aggravated", "flabbergasted", "crushed", "bedazzled", "bored", "disappointed"],
   ["flabbergasted", "bedazzled"]),

# ── Q18 ──
se("SE0513_18",
   "Many people erroneously believe that humans are naturally __________ to distrust or even fear those outside of their social or cultural group; anthropologists and social scientists, however, have consistently shown that xenophobia is a learned behavior.",
   ["indoctrinated", "proven", "prone", "disposed", "taught", "compelled"],
   ["prone", "disposed"]),

# ── Q19 ──
se("SE0513_19",
   "Geneticists find Iceland a living laboratory for the study of __________ because virtually all of its current 300,000 citizens descend from less than a thousand Icelanders who survived the medieval Black Death.",
   ["diversity", "revivification", "therapy", "history", "mutation", "rejuvenation"],
   ["diversity", "mutation"]),

# ── Q20 ──
se("SE0513_20",
   "The only way that a person can function given an influx of information is __________ to metaphorically separate the wheat from the chaff.",
   ["delete", "triage", "prioritize", "respond", "requite", "eliminate"],
   ["triage", "prioritize"]),

# ── Q21 ──
se("SE0513_21",
   "Although accommodating in person, George Orwell __________ defended his political positions in print.",
   ["tenaciously", "obsequiously", "inadvertently", "doggedly", "sycophantically", "idiosyncratically"],
   ["tenaciously", "doggedly"]),

# ── Q22 ──
se("SE0513_22",
   "Although historically, paints were often tinted with toxic elements such as lead, cadmium, and mercury, __________ number of painters lived to be seventy, eighty, and even ninety.",
   ["an incomprehensible", "a flabbergasting", "an impossible", "a confounding", "a dismaying", "an enlightening"],
   ["a flabbergasting", "a confounding"]),

# ── Q23 ──
se("SE0513_23",
   "The phrase 'gilding the lily' is a late 19th-century expression that was first coined to describe the ostentatious gestures of some of the newly rich; it still serves as a shorthand for any __________ and showy behavior.",
   ["gauche", "eccentric", "idiosyncratic", "prosperous", "affluent", "uncouth"],
   ["gauche", "uncouth"]),

# ── Q24 ──
se("SE0513_24",
   "While she still advocated for the wholesale restructuring of society based on principles of equity and sustainability, the radical blogger-turned-essayist had to __________ the expression of her views in order to appeal to the more middle-of-the-road sensibilities of the publishing market.",
   ["abridge", "moderate", "amalgamate", "undermine", "galvanize", "temper"],
   ["moderate", "temper"]),

# ── Q25 ──
se("SE0513_25",
   "A 'Mycenaean waist' refers to the taut, impossibly small waists characteristic of people depicted in certain ancient drawings found on Crete, and it certainly does not __________ any characteristic of most people in modern, overweight Western societies.",
   ["deify", "depict", "denigrate", "mirror", "defame", "distort"],
   ["depict", "mirror"]),

# ── Q26 ──
se("SE0513_26",
   "The commentator's analysis of the recent conflict was anything but __________; he parroted his ideological compatriots, adding nothing new or insightful to the discussion.",
   ["novel", "derivative", "tendentious", "fresh", "evenhanded", "hackneyed"],
   ["novel", "fresh"]),

# ── Q27 ──
se("SE0513_27",
   "In uncertain times, __________ theories often gain greater and faster adherence among the populace than proven ones do.",
   ["corroborated", "putative", "conjectural", "incorrect", "irrefutable", "irreconcilable"],
   ["putative", "conjectural"]),

# ── Q28 ──
se("SE0513_28",
   "Each civil engineer in the firm acted as __________ the others: no one submitted a construction project proposal if another expressed concerns about either the feasibility of the project or the cost estimates.",
   ["a go-between for", "a reviewer for", "an estimator for", "a negotiator for", "a hindrance to", "an overseer to"],
   ["a reviewer for", "an overseer to"]),

# ── Q29 ──
se("SE0513_29",
   "Arthur Conan Doyle's upstanding hero Sherlock Holmes engages in just as much clever deception as his nemesis, Professor Moriarty, proving that __________ is not inherently evil.",
   ["immorality", "brilliance", "cunning", "subterfuge", "wrongdoing", "judgment"],
   ["cunning", "subterfuge"]),

# ── Q30 ──
se("SE0513_30",
   "The etymologies of the words alpha and omega couldn't be more different; the former is obscure — the original symbol for alpha was an ox's head, and an ox is 'alp' in Phoenician — while the latter is __________, as omega simply means 'big O.'",
   ["transparent", "complicated", "overt", "erudite", "abstruse", "scholarly"],
   ["transparent", "overt"]),

# ── Q31 ──
se("SE0513_31",
   "While the muted colors do suggest a certain sobriety, the overall effect is undeniably __________.",
   ["vivacious", "poignant", "limpid", "lackluster", "mirthful", "benign"],
   ["vivacious", "mirthful"]),

# ── Q32 ──
se("SE0513_32",
   "Although the system's __________ at the local level has come under threat, the allegations of preferential treatment have so far not spread to criticisms at the national level.",
   ["unfairness", "solemnity", "probity", "equity", "partiality", "solicitousness"],
   ["probity", "equity"]),

# ── Q33 ──
se("SE0513_33",
   "Response to the provocative proposal was predictably __________: little care was given to the concealment of dislike for its aims or scorn for its authors.",
   ["inscrutable", "polemical", "iconoclastic", "scathing", "fictitious", "impenetrable"],
   ["polemical", "scathing"]),

# ── Q34 ──
se("SE0513_34",
   "The prime minister affected empathy for the impoverished citizenry, but most economic historians believe that her austerity measures, which were unduly __________, further injured them.",
   ["arduous", "commercial", "mercantilist", "onerous", "strict", "venal"],
   ["arduous", "onerous"]),

# ── Q35 ──
se("SE0513_35",
   "While traveling to the spa's remote location could be hectic, visitors more than made up for the stress by unwinding in a supremely __________ environment.",
   ["effusive", "pacific", "elegant", "luxurious", "placid", "blithe"],
   ["pacific", "placid"]),

# ── Q36 ──
se("SE0513_36",
   "The man looked much older than his 70 years, his __________ frame looking as though it had endured the harsh weather of many decades; to play the physically robust Moses, the actor was, in the end, perfect for the role.",
   ["fetid", "vigorous", "desiccated", "wizened", "arid", "hale"],
   ["desiccated", "wizened"]),

# ── Q37 ──
se("SE0513_37",
   "The children's attempt at a Mother's Day brunch was __________; soggy French toast, lukewarm coffee, and a syrup fight in the kitchen that would inevitably end up being cleaned up by the very recipient of the brunch.",
   ["convivial", "amiable", "comical", "satirical", "farcical", "labile"],
   ["comical", "farcical"]),

# ── Q38 ──
se("SE0513_38",
   "Many major websites today have __________ privacy policy: written by lawyers to protect the website that hired them, the language in the document is so abstruse that most consumers could not read it even if they tried to.",
   ["an inscrutable", "a decipherable", "a repetitive", "a lucid", "a sanctioned", "an unreadable"],
   ["an inscrutable", "an unreadable"]),

# ── Q39 ──
se("SE0513_39",
   "Though chronicling the heroism and sacrifice of the common soldier, Erich Remarque's classic novel All Quiet on the Western Front, is profoundly __________ and thus was banned by the Nazis since it implicitly opposed their vision of armed conquest.",
   ["inspirational", "pacific", "prescient", "conciliatory", "prophetic", "clairvoyant"],
   ["pacific", "conciliatory"]),

# ── Q40 ──
se("SE0513_40",
   "Just months from retirement, the disgraced executive was forced to make __________ exit from the company.",
   ["a glorious", "a triumphant", "a boorish", "an ignominious", "a defiled", "an unseemly"],
   ["an ignominious", "an unseemly"]),

# ── Q41 ──
se("SE0513_41",
   "__________ in scandal, the company could regain favor with customers only through mass firings of guilty executives.",
   ["Wallowing", "Stoic", "Bogged down", "Brave", "Mired", "Besotted"],
   ["Bogged down", "Mired"]),

# ── Q42 ──
se("SE0513_42",
   "By framing the new law as a question of urgent safety rather than of privacy, the government obviated the need to pass through the standard channels of legislation, effectively __________ formal dissent and relegating any would-be naysayer from a position of engaged activist to that of powerless bystander.",
   ["curtailing", "undermining", "targeting", "lobbying", "instigating", "facilitating"],
   ["curtailing", "undermining"]),

# ── Q43 ──
se("SE0513_43",
   "What is known, however, is that it took but a slight mutation in the pathogen's genetic constitution to render it lethal to __________ of related species.",
   ["a contraband", "a surplus", "an aurora", "a myriad", "a pantheon", "a plethora"],
   ["a myriad", "a plethora"]),

# ── Q44 ──
se("SE0513_44",
   "Although known for bon mots such as, 'If you don't have anything nice to say about anybody, come sit next to me,' Alice Roosevelt Longworth was said to be very kind; her circulated __________ did not reflect vindictiveness.",
   ["vituperations", "rants", "witticisms", "zeal", "quips", "taciturnity"],
   ["witticisms", "quips"]),

# ── Q45 ──
se("SE0513_45",
   "Always on the lookout for a shady deal or quick con, she became known and scorned as an __________ opportunist.",
   ["unqualified", "unprincipled", "alluring", "unprecedented", "attractive", "unscrupulous"],
   ["unprincipled", "unscrupulous"]),

# ── Q46 ──
se("SE0513_46",
   "After many hours of debate, things seemed to have reached __________, as neither side was willing to give so much as an inch, and no one had anything new to offer.",
   ["an impasse", "a pause", "a timeout", "a confrontation", "an engagement", "a stalemate"],
   ["an impasse", "a stalemate"]),

# ── Q47 ──
se("SE0513_47",
   "While kidney stones are known to produce a truly __________ sensation, often compared to the agony of childbirth, they are almost never fatal.",
   ["anodyne", "inoffensive", "painstaking", "tortuous", "excruciating", "torturous"],
   ["excruciating", "torturous"]),

# ── Q48 ──
se("SE0513_48",
   "Given the breadth and speed of social media, the only way celebrities can hope to conceal their foibles is by employing practices as __________ as those of a spy ring.",
   ["draconian", "arduous", "duplicitous", "fanciful", "cloaked", "conspicuous"],
   ["duplicitous", "cloaked"]),

# ── Q49 ──
se("SE0513_49",
   "The director of the musical admitted that while he was very good with characterization, scenery, lighting, and music, choreography was not at all his __________.",
   ["strong suit", "weakness", "forte", "hobby", "deficiency", "pastime"],
   ["strong suit", "forte"]),

# ── Q50 ──
se("SE0513_50",
   "Though most technology used in the manufacture of bicycles is either decades old or adapted from other industries, the advent of carbon fiber frames brought with it genuine __________.",
   ["innovation", "novelty", "flexibility", "venerability", "transformation", "seriousness"],
   ["innovation", "transformation"]),

# ── Q51 ──
se("SE0513_51",
   "Through __________ antics that flouted the conventions of the establishment, the Yippies of the late 1960s impressed themselves into the public consciousness; their behavior culminated in the instigation of riots in Chicago during the Democratic convention in 1968.",
   ["socialist", "brazen", "anarchist", "communist", "insolent", "fastidious"],
   ["brazen", "insolent"]),

# ── Q52 ──
se("SE0513_52",
   "Sometimes __________ comes at a price; research suggests that among first-generation Chinese Americans, those who embrace the traditional Confucian values of their homeland are more likely to succeed academically than are those who do not.",
   ["acculturation", "assimilation", "investiture", "alienation", "indebtedness", "estrangement"],
   ["acculturation", "assimilation"]),

# ── Q53 ──
se("SE0513_53",
   "Many Enlightenment philosophers viewed Machiavelli's book as a satire meant to expose and caricature the __________ claims to power of the very figures Machiavelli pretended to endorse.",
   ["sarcastic", "specious", "spurious", "squalid", "stolid", "stoic"],
   ["specious", "spurious"]),

# ── Q54 ──
se("SE0513_54",
   "The defendant impressed the jurors as __________; they did not believe that a woman of her education and experience could possibly be as naive as she acted.",
   ["disingenuous", "guileless", "innocent", "accomplished", "artful", "culpable"],
   ["disingenuous", "artful"]),

# ── Q55 ──
se("SE0513_55",
   "Crucial to fostering a realistic understanding of the potential boons — and perils — of the new drug will be a concerted effort to __________ the specific contexts and symptoms that render its use appropriate.",
   ["furnish", "delineate", "outlaw", "transmute", "stipulate", "proscribe"],
   ["delineate", "stipulate"]),

# ── Q56 ──
se("SE0513_56",
   "Millions of dollars over budget and months late, the planned software was finally ready for release, much to the chagrin of its original investors; although it actually had all of the capabilities that the original specification __________, the delay meant that it had already been surpassed by competitors' products.",
   ["possessed", "boasted of", "predicted", "updated", "enhanced", "promised"],
   ["boasted of", "promised"]),

# ── Q57 ──
se("SE0513_57",
   "Robert Gottlieb, who otherwise found much to admire in John Steinbeck, argued that Steinbeck was politically __________, offering an adolescent disaffection in place of settled judgment.",
   ["naive", "perspicacious", "contemptible", "keen", "callow", "disinterested"],
   ["naive", "callow"]),

# ── Q58 ──
se("SE0513_58",
   "The mayor's __________ speech turned the bipartisan issue — traffic reduction — into a three-month-long fight between former allies.",
   ["alienating", "honest", "refreshing", "plodding", "divisive", "conventional"],
   ["alienating", "divisive"]),

# ── Q59 ──
se("SE0513_59",
   "In his writings after visiting New York, Albert Camus expressed more of an inkling rather than a __________ understanding of what he found lacking in American culture.",
   ["elementary", "shrewd", "penetrating", "inchoate", "sinuous", "dialectical"],
   ["shrewd", "penetrating"]),

# ── Q60 ──
se("SE0513_60",
   "Technological advances in communication — such as computers and texting — have caused the teaching of cursive writing in school to become so exceptional that, if the trend continues, original source texts, minutes from historic meetings, diaries, and even letters from ancestors will become __________ to future generations.",
   ["unintelligible", "intellectual", "meaningless", "humdrum", "quotidian", "indecipherable"],
   ["unintelligible", "indecipherable"]),

# ── Q61 ──
se("SE0513_61",
   "It is in the best interest of criminal defendants to appear __________ in front of the judge, showing that not all moral sympathy is lost on them.",
   ["callous", "vindicated", "contrite", "penitential", "messianic", "pious"],
   ["contrite", "penitential"]),

# ── Q62 ──
se("SE0513_62",
   "A surgeon who could best be described as __________ would evenly address the paramedics, evaluate the situation, and methodically work through his normal routine.",
   ["qualified", "premeditated", "phlegmatic", "unflappable", "enraptured", "enthusiastic"],
   ["phlegmatic", "unflappable"]),

# ── Q63 ──
se("SE0513_63",
   "Despite the blandishments of the real estate con artist, the intended mark remained __________ about the value of the plot for sale, as, on the map, it seemed to border a swamp.",
   ["optimistic", "enthused", "irascible", "skeptical", "jaundiced", "leery"],
   ["skeptical", "leery"]),

# ── Q64 ──
se("SE0513_64",
   "In response to a recent editorial slamming the agency's newest advertising campaign, the agency spokesman denounced the piece as __________ adversarial motives, due to the editorialist's position on the board of the agency's primary competitor.",
   ["stemming from", "producing", "typifying", "epitomized by", "engendered by", "creating"],
   ["stemming from", "engendered by"]),

# ── Q65 ──
se("SE0513_65",
   "In the week that followed the climber's disappearance, internet rumor mongers blogged a myriad of __________ reports of her demise, only to be embarrassed by the release of a dramatic video that showed her celebrating on the summit.",
   ["apocryphal", "sentimental", "spurious", "saccharine", "scandalous", "credible"],
   ["apocryphal", "spurious"]),

# ── Q66 ──
se("SE0513_66",
   "The savvy investor had already identified clear indications that the company would soon be __________.",
   ["profitable", "bankrupt", "subsidized", "insolvent", "acquired", "thriving"],
   ["profitable", "thriving"]),

# ── Q67 ──
se("SE0513_67",
   "The tragedy — and the resultant horrific loss of life and damage to property — occurred because of his __________ approach to his duties, evinced by his slouching posture and cavalier attitude.",
   ["murderous", "petty", "lax", "aristocratic", "barbarous", "slack"],
   ["lax", "slack"]),

# ── Q68 ──
se("SE0513_68",
   "The __________ that marks the composer's more recent work represents a major departure from the experiments in dissonance represented by her early compositions.",
   ["disparity", "stridency", "creativity", "harmony", "harshness", "euphony"],
   ["harmony", "euphony"]),

# ── Q69 ──
se("SE0513_69",
   "Although they were already late for the formal reception, the couple continued to __________ because they preferred to lounge about and bask in each other's company.",
   ["lurk", "dally", "tarry", "skulk", "embrace", "equivocate"],
   ["dally", "tarry"]),

# ── Q70 ──
se("SE0513_70",
   "The player's exploits both on the field and in the finest night clubs around the world earned him many __________ from his legions of staunch admirers — so many, in fact, that his given name was all but forgotten.",
   ["similes", "appellations", "sobriquets", "misnomers", "accolades", "kudos"],
   ["appellations", "sobriquets"]),

# ── Q71 ──
se("SE0513_71",
   "To the casual observer, the desert appears __________ place; those who look deeper, however, discover that it supports a vibrant ecosystem teeming with life.",
   ["a verdant", "an arid", "a desolate", "a desiccated", "an inhospitable", "a lush"],
   ["a desolate", "an inhospitable"]),

# ── Q72 ──
se("SE0513_72",
   "The presidential candidate, known not only for the deeply reasoned content of his prepared speeches but also for the fiery brilliance of his delivery, badly miscalculated his ability to perform equally successfully when delivering __________ answers to unexpected queries from the media.",
   ["extemporaneous", "capricious", "lubricious", "disingenuous", "impromptu", "premeditated"],
   ["extemporaneous", "impromptu"]),

# ── Q73 ──
se("SE0513_73",
   "While her friends agree that she projects an air of affability, they are of two minds about whether this friendliness is in fact __________.",
   ["amiable", "unaffected", "genial", "sincere", "vexing", "contrived"],
   ["unaffected", "sincere"]),

# ── Q74 ──
se("SE0513_74",
   "The executive was hit with a penalty not only for the millions in fines and restitution that she must pay, as well as another legal memorandum in which she __________ her role and financial interest in the hedge fund she had founded.",
   ["abjured", "jeopardized", "reneged", "deposed", "censured", "forwent"],
   ["abjured", "forwent"]),

# ── Q75 ──
se("SE0513_75",
   "Some religious adherents follow the letter of their particular tradition while simultaneously __________ its most basic ethical tenets, a fact that may explain why so much violence is perpetrated in the name of love of and obedience to a faith.",
   ["breaching", "obeying", "surpassing", "heeding", "contravening", "contracting"],
   ["breaching", "contravening"]),

# ── Q76 ──
se("SE0513_76",
   "It is perplexing that the number of PhD applicants in linguistics, so obviously a __________ field, has either grown or held steady in each of the past 15 years.",
   ["moribund", "waxing", "burgeoning", "waning", "dissolute", "debased"],
   ["moribund", "waning"]),

# ── Q77 ──
se("SE0513_77",
   "Writers, particularly those of the contemplative persuasion, have always found the __________ nature of the mind — with its passing thoughts and inconstant moods — difficult to convey in language.",
   ["inchoate", "essential", "vestigial", "ephemeral", "evasive", "fleeting"],
   ["ephemeral", "fleeting"]),

# ── Q78 ──
se("SE0513_78",
   "Though the majority of rules in sports are enumerated in rulebooks, there is __________ code of conduct that relates to sportsmanship.",
   ["a tacit", "an evanescent", "an incorrigible", "an unambiguous", "a blatant", "an implicit"],
   ["a tacit", "an implicit"]),

# ── Q79 ──
se("SE0513_79",
   "Many people think that antibiotics are a cure-all, but these medications can actually __________ the problem; taken inconsistently, antibiotics can in fact strengthen bacterial strains.",
   ["exacerbate", "ameliorate", "differentiate", "distort", "pathologize", "magnify"],
   ["exacerbate", "magnify"]),

# ── Q80 ──
se("SE0513_80",
   "Sandra was entirely __________ by the crossword puzzle that, unlike the simple fill-in-the-blanks published on weekdays, was one of the more difficult cryptic crosswords only published on weekends.",
   ["confounded", "flummoxed", "enraged", "smitten", "incensed", "impressed"],
   ["confounded", "flummoxed"]),

# ── Q81 ──
se("SE0513_81",
   "Teachers say they are keen on the idea of participatory pedagogy, but observations show that they are actually __________ to change; even when they think they are doing otherwise, observations show that teachers perpetuate the teacher-centered classroom practices to which they have been habituated.",
   ["amenable", "impervious", "inimical", "prone", "reconciled", "resigned"],
   ["impervious", "inimical"]),

# ── Q82 ──
se("SE0513_82",
   "The subject of the documentary was not bothered that the filmmaker received such __________ from the critics, but that none of the acclaim filtered down to him.",
   ["opprobrium", "wealth", "fulmination", "plaudits", "capital", "approbation"],
   ["plaudits", "approbation"]),

# ── Q83 ──
se("SE0513_83",
   "The Thin Blue Line, a documentary by Errol Morris, is one of very few movies that has had a tangible effect on the real world; the film managed to __________ its subject, who had been on death row for a crime that Morris demonstrated that the man did not commit.",
   ["exculpate", "incarcerate", "inter", "excuse", "manumit", "vindicate"],
   ["exculpate", "vindicate"]),

# ── Q84 ──
se("SE0513_84",
   "Most people expect to see straightforward and direct cause-and-effect relationships between actions and reactions; this contributes to making __________ one of the most difficult concepts to really understand.",
   ["causality", "randomness", "intentionality", "happenstance", "mathematics", "science"],
   ["randomness", "happenstance"]),

# ── Q85 ──
se("SE0513_85",
   "The professor's belief that all of the students admitted to the university were well-qualified academically led her to assume some degree of __________ in every student who was doing poorly in her class.",
   ["moral turpitude", "ineptness", "amorality", "laziness", "incompetence", "sloth"],
   ["laziness", "sloth"]),

# ── Q86 ──
se("SE0513_86",
   "In a way, the environmental movement can still be said to be __________ movement, for while it has been around for decades, it has only recently become a serious political force.",
   ["an incipient", "a disorganized", "a nascent", "a nebulous", "an inconsequential", "an immaterial"],
   ["an incipient", "a nascent"]),

# ── Q87 ──
se("SE0513_87",
   "Einstein's theory of quantum mechanics remained purely experiential until it was theoretically __________ by the work of physicists such as Louis de Broglie and Werner Heisenberg.",
   ["bolstered", "undermined", "condoned", "pardoned", "sabotaged", "buttressed"],
   ["bolstered", "buttressed"]),

# ── Q88 ──
se("SE0513_88",
   "The plan, according to law enforcement and judicial officials, was to keep the prisoner __________ during his court appearances, but the defense attorney argued that restraints would prejudice the jury.",
   ["manacled", "malleable", "nettled", "fettered", "incensed", "incomparable"],
   ["manacled", "fettered"]),

# ── Q89 ──
se("SE0513_89",
   "The painter was just as famous for his personality as for his work; unlike the many pretentious and egotistical men in his field, he was known to be entirely __________.",
   ["artless", "shrewd", "ingenuous", "selfless", "arrogant", "modest"],
   ["artless", "ingenuous"]),

# ── Q90 ──
se("SE0513_90",
   "The newest romantic comedy wasn't exactly bad, but simply __________; it had laughs, but they were all jokes most audience members had heard before.",
   ["atrocious", "amusing", "trite", "hackneyed", "witty", "egregious"],
   ["trite", "hackneyed"]),

# ── Q91 ──
se("SE0513_91",
   "An obsession with aesthetics __________ all of the work of the computer company; even their unsuccessful products manage to look like winsome pieces of modernist sculpture.",
   ["underpins", "irradiates", "underserves", "overwhelms", "undergirds", "saturates"],
   ["underpins", "undergirds"]),

# ── Q92 ──
se("SE0513_92",
   "Oftentimes, when administrators force teachers to cleave too closely to a federal curriculum, those teachers feel __________, because the mandatory curriculum curbs their sense of being creative and dynamic educators.",
   ["crushed", "confounded", "thwarted", "undermined", "tormented", "walloped"],
   ["thwarted", "undermined"]),

# ── Q93 ──
se("SE0513_93",
   "The federal government knows that a certain level of financial stability can be attained by lowering interest rates, yet if it overuses this power, it risks losing its most reliable means of __________ crisis.",
   ["interring", "exacerbating", "annihilating", "palliating", "compounding", "assuaging"],
   ["palliating", "assuaging"]),

# ── Q94 ──
se("SE0513_94",
   "Even though Mariposa loved taking on roles that involved a lot of lines, she was excited to be playing a more __________ character, requiring her to focus more on gesture and expression.",
   ["laconic", "dramatic", "dejected", "mute", "melancholy", "curt"],
   ["laconic", "curt"]),

# ── Q95 ──
se("SE0513_95",
   "Because the United States has become a mature, established nation, the __________ nature of Thomas Paine's political diatribes is now downplayed by government officials who would denounce a contemporary version as seditious.",
   ["pallid", "incendiary", "antithetical", "anemic", "demagogic", "deferential"],
   ["incendiary", "demagogic"]),

# ── Q96 ──
se("SE0513_96",
   "A professional spy, he always affected a __________ demeanor, but those who disliked him often characterized it as taciturn or brusque.",
   ["phlegmatic", "histrionic", "hirsute", "melodramatic", "melancholic", "dispassionate"],
   ["phlegmatic", "dispassionate"]),

# ── Q97 ──
se("SE0513_97",
   "Though Hamlet is famous for being __________, he still manages to go on something of a killing spree.",
   ["indecisive", "melancholy", "monological", "morose", "violent", "barbaric"],
   ["melancholy", "morose"]),

# ── Q98 ──
se("SE0513_98",
   "It's worth wondering whether the increase in diagnoses of psychological disorders has caused us to see certain behaviors that were once considered normal as __________.",
   ["importunate", "mythical", "unfortunate", "anomalous", "aberrant", "fabulous"],
   ["anomalous", "aberrant"]),

# ── Q99 ──
se("SE0513_99",
   "Proust proved that the __________ can be the domain of the novel every bit as much as the fantastical can be.",
   ["mundane", "literary", "bombastic", "cosmopolitan", "belletristic", "quotidian"],
   ["mundane", "quotidian"]),

# ── Q100 ──
se("SE0513_100",
   "The magazine's editor was known to be a very busy woman, so it was important when speaking with her to get right to the __________ of the issue.",
   ["pith", "conclusion", "gist", "apex", "genesis", "culmination"],
   ["pith", "gist"]),

# ── Q101 ──
se("SE0513_101",
   "The reclusive boy was thought to be less than clever, but at sixteen he wrote a complex and beautiful symphony that at long last revealed him to be __________.",
   ["gifted", "musical", "monastic", "exceptional", "hermetic", "precocious"],
   ["exceptional", "precocious"]),

# ── Q102 ──
se("SE0513_102",
   "Many poets __________ the primacy of meter over words: Stephen Fry, in his book, The Ode Less Traveled, argues that rhythm is essential in poetry, whereas deeper meaning is less important.",
   ["stress", "acknowledge", "allow", "immolate", "underscore", "decry"],
   ["stress", "underscore"]),

# ── Q103 ──
se("SE0513_103",
   "Rock and roll music, once the choice of the young, __________ joined the culture of the old as previous generations have aged; as had every preceding style of music before it, rock and roll was stripped of its edge as time passed.",
   ["inevitably", "accidentally", "deliberately", "unavoidably", "resolutely", "painfully"],
   ["inevitably", "unavoidably"]),

# ── Q104 ──
se("SE0513_104",
   "Isherwood's socialism was not merely a mark of his opposition to fascism, but also a mark of his fellow feeling for the laboring classes and his __________ to engage as an equal with working people.",
   ["disinclination", "hankering", "proclivity", "implacability", "unwillingness", "joviality"],
   ["hankering", "proclivity"]),

# ── Q105 ──
se("SE0513_105",
   "Academic freedom does not protect a professor's classroom remarks on matters irrelevant to his subject, though it guarantees the professor considerable liberty of speech about matters __________ to his or her academic work.",
   ["germane", "indifferent", "mimetic", "disinterested", "congruent", "pertinent"],
   ["germane", "pertinent"]),

# ── Q106 ──
se("SE0513_106",
   "Unchecked passion of any kind tends to end in __________ and sorrow.",
   ["disdain", "pity", "rue", "affinity", "remorse", "contempt"],
   ["rue", "remorse"]),

# ── Q107 ──
se("SE0513_107",
   "A tremendous wealth of specimens — billion-year-old blue-green bacteria from the Adirondacks, fossilized tree stumps and spiders from Schoharie County, trilobites from Oneida County, and armored fish from throughout the state — represents only a tiny fraction of the New York State Museum's __________ collection of over one million specimens.",
   ["piecemeal", "voluble", "exhaustive", "evergreen", "sweeping", "commanding"],
   ["exhaustive", "sweeping"]),

# ── Q108 ──
se("SE0513_108",
   "The judge's keen eye for sussing out the pretension of the lawyers in her courtroom was surpassed only by the __________ wit with which she castigated them for it.",
   ["sardonic", "mordant", "obtuse", "jurisprudent", "trenchant", "assiduous"],
   ["mordant", "trenchant"]),

# ── Q109 ──
se("SE0513_109",
   "The amount of self-abasement with which the inmate __________ the probation panel to be set free verged on the humiliating; nevertheless, the judges remained unmoved and he was ultimately sent back to his cell to serve another three years.",
   ["beseeched", "chided", "snubbed", "conceded", "received", "supplicated"],
   ["beseeched", "supplicated"]),

# ── Q110 ──
se("SE0513_110",
   "The cult members treated their leader with __________ loyalty that verged on the obsessive and made them willing, should the need ever arise, to do so much as lay down their lives for him.",
   ["a fanatical", "an arbitrary", "a fickle", "a zealous", "an indeterminate", "a devoted"],
   ["a fanatical", "a zealous"]),

# ── Q111 ──
se("SE0513_111",
   "Jefferson regarded sumptuous living as among the most __________ evils to threaten the young republic, more pernicious even than loyalty to the deposed empire.",
   ["reactionary", "venerable", "epicurean", "grievous", "baneful", "fastidious"],
   ["grievous", "baneful"]),

# ── Q112 ──
se("SE0513_112",
   "Theology was once regarded as the 'Queen of the Sciences,' because every subject eventually had to meet its demands, but 200 years ago that honor and title fell to mathematics, which enjoys __________ over not only physical science but social science as well.",
   ["mayhem", "credence", "hegemony", "autonomy", "dominance", "independence"],
   ["hegemony", "dominance"]),

# ── Q113 ──
se("SE0513_113",
   "The new particles produced by CERN's Large Hadron Collider are __________, lasting a millionth of a billionth of a billionth of a second before disintegrating into photons, quarks, or other particles.",
   ["ephemeral", "infinitesimal", "myriad", "poignant", "fleeting", "countless"],
   ["ephemeral", "fleeting"]),

# ── Q114 ──
se("SE0513_114",
   "While the professor first achieved renown for the theory he devised single-handedly during the early days of his career, his later contributions were achieved in a more __________ manner.",
   ["solitary", "collaborative", "synergetic", "exegetic", "unilateral", "collusive"],
   ["collaborative", "synergetic"]),

# ── Q115 ──
se("SE0513_115",
   "Although the media's coverage of the event was lackluster, the organizers still felt it was __________; what mattered, they said, was not the piddling number of talking heads who turned out to comment, but rather the mass of everyday people who came to register their disapproval of the proposed oil pipeline.",
   ["a blemish", "an exception", "a coup", "a debacle", "a miracle", "an achievement"],
   ["a coup", "an achievement"]),

# ── Q116 ──
se("SE0513_116",
   "Lady Astor once commented to Winston Churchill, 'If I were married to you, I'd put poison in your coffee.' Churchill's famous __________: 'Nancy, if you were my wife, I'd drink it.'",
   ["anecdote", "aphorism", "retort", "recrimination", "rejoinder", "maxim"],
   ["retort", "rejoinder"]),

# ── Q117 ──
se("SE0513_117",
   "The teacher was well-loved by students, but he never __________ the work of teaching; in fact, planning lessons and facilitating group process only exacerbated his deep-seated anxieties about preparation and public speaking.",
   ["appreciated", "fancied", "abhorred", "relished", "detested", "ascertained"],
   ["fancied", "relished"]),

# ── Q118 ──
se("SE0513_118",
   "The teacher was no __________, although she felt she had to maintain the appearance of an authority figure; in truth, she couldn't care less whether students ate food in her class or doodled during lectures.",
   ["stickler", "educator", "delinquent", "scholar", "luminary", "disciplinarian"],
   ["stickler", "disciplinarian"]),

# ── Q119 ──
se("SE0513_119",
   "The actress was young but not __________; she knew manipulation when she saw it, and she resisted being swayed by her crafty handlers.",
   ["guileless", "disingenuous", "naive", "cunning", "talented", "sophisticated"],
   ["guileless", "naive"]),

# ── Q120 ──
se("SE0513_120",
   "The __________ of recent national political discourse, which such hateful rhetoric is impotent to address, has only deepened divisions.",
   ["virulence", "acrimony", "shortsightedness", "partisanship", "miscalculation", "intransigence"],
   ["virulence", "acrimony"]),

# ── Q121 ──
se("SE0513_121",
   "Martin Luther King, Jr. was more __________ than is commonly thought today; it was only in the posthumous process of canonization that his more palatable, less far-reaching political and social visions became prominent.",
   ["ineffective", "radical", "politic", "immoderate", "incongruous", "raucous"],
   ["radical", "immoderate"]),

# ── Q122 ──
se("SE0513_122",
   "While it would help to offset a portion of the expenses of the renovation project, which had been far more __________ than initially anticipated, the proposed tourism fee was never enacted by the city council, who thought that a more complete solution was necessary.",
   ["fortuitous", "unexpected", "costly", "subtle", "timely", "dear"],
   ["costly", "dear"]),

# ── Q123 ──
se("SE0513_123",
   "Aviation authorities at one time issued __________ guidelines for hobbyists flying model airplanes, but in the absence of definitive laws, some individuals have chosen to ignore the recommendations.",
   ["regular", "discretionary", "voluntary", "firm", "insufficient", "unvarying"],
   ["discretionary", "voluntary"]),

# ── Q124 ──
se("SE0513_124",
   "The so-called 'reality' television show claimed to display the __________ side of the starlet's life.",
   ["unusual", "predictable", "quotidian", "exotic", "mundane", "plastic"],
   ["quotidian", "mundane"]),

# ── Q125 ──
se("SE0513_125",
   "The problem with listening to prognosticators — especially in an age when no one seeks to hold them accountable — is that for every accurate prediction made, there are several others that turn out to be __________.",
   ["mistaken", "unforeseen", "hasty", "misleading", "untrue", "surprising"],
   ["mistaken", "untrue"]),

# ── Q126 ──
se("SE0513_126",
   "If the allegations turn out to be true and the school's administrators are found to be __________, they might never be able to be employed in higher education again.",
   ["repentant", "culpable", "synoptic", "contrite", "complicit", "unsound"],
   ["culpable", "complicit"]),

# ── Q127 ──
se("SE0513_127",
   "His characterization of the situation was so __________ as to be impossible for even his adherents to take seriously.",
   ["temperate", "immoderate", "impressive", "lax", "splendid", "extreme"],
   ["immoderate", "extreme"]),

# ── Q128 ──
se("SE0513_128",
   "The author ignored the sensibilities of the general public rather than __________ them.",
   ["recoiling from", "catering to", "coping with", "commiserating with", "pandering to", "cowering to"],
   ["catering to", "pandering to"]),

# ── Q129 ──
se("SE0513_129",
   "Many, if not most, sociologists subscribe to the idea that humans are __________, but a certain event leads to the conclusion that human nature is largely immutable.",
   ["homogenous", "heterogeneous", "malleable", "monolithic", "pliant", "variegated"],
   ["malleable", "pliant"]),

# ── Q130 ──
se("SE0513_130",
   "In romance novels, a strapping hero often __________ a rapier in the service of an ennobled yet submissive woman; this display of force carries the day but, despite the popularity of such books, some pundits bemoan the passive portrayal of women.",
   ["sheathes", "brandishes", "wields", "promulgates", "disseminates", "cauterizes"],
   ["brandishes", "wields"]),

# ── Q131 ──
se("SE0513_131",
   "Mr. Gupta announced that his centrist party would pursue prudent policies, courses that were progressive, while remaining __________ about imposing drastic social changes.",
   ["passionate", "fervent", "cautious", "concerned", "congealed", "conservative"],
   ["cautious", "conservative"]),

# ── Q132 ──
se("SE0513_132",
   "A problem in modern industrial nations — a designation that now encompasses more than the United States and Europe — is that when the wages of the middle class are stagnant, the economy expands at a __________ pace.",
   ["plodding", "normal", "lucrative", "pedestrian", "profitable", "exponential"],
   ["plodding", "pedestrian"]),

# ── Q133 ──
se("SE0513_133",
   "The adaptive abilities of microorganisms are more __________ than is commonly thought: from self-induced rapid mutations that allow them to utilize novel nutrient sources, to the appropriation of other microbe communities, their innovative capabilities know no end.",
   ["ineffectual", "profuse", "advantageous", "prolific", "beneficial", "accommodating"],
   ["profuse", "prolific"]),

# ── Q134 ──
se("SE0513_134",
   "The chess grandmaster Judit Polgar is famous for her __________ gambits.",
   ["atypical", "treacherous", "abstruse", "anomalous", "studious", "impractical"],
   ["atypical", "anomalous"]),

# ── Q135 ──
se("SE0513_135",
   "The incumbent politician was deep in denial if she thought that the pandering advertisements would do anything but __________ her campaign.",
   ["bolster", "aggrieve", "encourage", "hobble", "hamstring", "restore"],
   ["hobble", "hamstring"]),

# ── Q136 ──
se("SE0513_136",
   "Though often equivocal in making decisions, he was __________ in his resolve upon reaching a verdict.",
   ["steadfast", "vacillating", "vague", "unwavering", "apprehensive", "critical"],
   ["steadfast", "unwavering"]),

# ── Q137 ──
se("SE0513_137",
   "The expansion proposal, which the school board affirms will maximize efficiency while maintaining __________ class sizes, has nevertheless been resoundingly opposed by parent groups and the teachers' union.",
   ["remedial", "manageable", "flexible", "deficient", "reasonable", "unwieldy"],
   ["manageable", "reasonable"]),

# ── Q138 ──
se("SE0513_138",
   "The bridge player's frequent errors, although frustrating for his partner, were __________ his defeat, since none of the competing players could determine, from the cards he played, what cards he had.",
   ["an insurance against", "the reason for", "an indication of", "an obstacle to", "a hurdle for", "the guarantee of"],
   ["an insurance against", "an obstacle to"]),

# ── Q139 ──
se("SE0513_139",
   "The medical study contains a glaring deficiency: it assumes that the results are __________, however, the experimental participants were exclusively men between the ages of 30 and 60 with no significant co-morbidities.",
   ["positive", "generalizable", "promising", "singular", "exceptional", "universal"],
   ["generalizable", "universal"]),

]


def main():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    existing_ids = {q["id"] for q in data["verbal"]}
    new_qs = [q for q in questions if q["id"] not in existing_ids]
    skipped = len(questions) - len(new_qs)

    failed = [q for q in new_qs if len(q["correct"]) != 2]
    valid = [q for q in new_qs if len(q["correct"]) == 2]

    data["verbal"].extend(valid)
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Added: {len(valid)}  |  Skipped(dup): {skipped}  |  Failed: {len(failed)}")
    print(f"Total verbal: {len(data['verbal'])}")
    if failed:
        print(f"WARNING - answer mapping failed for: {[q['id'] for q in failed]}")
    else:
        print("All answer mappings verified OK")


if __name__ == "__main__":
    main()
