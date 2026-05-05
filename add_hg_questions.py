"""HGset verbal questions → practice_questions.json 추가"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "gre_content" / "practice_questions.json"

# ── 헬퍼 ─────────────────────────────────────────────────────────────────────

def tc1(qid, stem, choices5, correct_letter, diff="medium", passage=None):
    """Single-blank TC (5 choices, no labels in PDF → assign A-E)"""
    labels = ["A","B","C","D","E"]
    ch = {labels[i]: choices5[i] for i in range(len(choices5))}
    return {
        "id": qid, "section": "verbal", "type": "text_completion",
        "subtype": "single_blank", "difficulty": diff, "set": None,
        "passage": passage, "stem": stem,
        "blanks": [{"label": "Blank", "choices": ch}],
        "correct": [correct_letter], "explanation": "",
    }


def tc2(qid, stem, b1_choices, b2_choices, correct, diff="medium"):
    """Double-blank TC. b1_choices: 3 items (A/B/C), b2_choices: 3 items (D/E/F)"""
    def _ch(items, start):
        import string
        labels = list(string.ascii_uppercase)
        return {labels[start+i]: items[i] for i in range(len(items))}
    blanks = [
        {"label": "Blank (i)",  "choices": _ch(b1_choices, 0)},
        {"label": "Blank (ii)", "choices": _ch(b2_choices, 3)},
    ]
    return {
        "id": qid, "section": "verbal", "type": "text_completion",
        "subtype": "double_blank", "difficulty": diff, "set": None,
        "passage": None, "stem": stem, "blanks": blanks,
        "correct": correct, "explanation": "",
    }


def tc3(qid, stem, b1, b2, b3, correct, diff="medium"):
    """Triple-blank TC."""
    def _ch(items, start):
        import string
        labels = list(string.ascii_uppercase)
        return {labels[start+i]: items[i] for i in range(len(items))}
    blanks = [
        {"label": "Blank (i)",   "choices": _ch(b1, 0)},
        {"label": "Blank (ii)",  "choices": _ch(b2, 3)},
        {"label": "Blank (iii)", "choices": _ch(b3, 6)},
    ]
    return {
        "id": qid, "section": "verbal", "type": "text_completion",
        "subtype": "triple_blank", "difficulty": diff, "set": None,
        "passage": None, "stem": stem, "blanks": blanks,
        "correct": correct, "explanation": "",
    }


def se(qid, stem, choices6, correct2, diff="medium"):
    """Sentence Equivalence (6 choices A-F, pick 2)"""
    labels = ["A","B","C","D","E","F"]
    ch = {labels[i]: choices6[i] for i in range(len(choices6))}
    return {
        "id": qid, "section": "verbal", "type": "sentence_equivalence",
        "subtype": "sentence_equivalence", "difficulty": diff, "set": None,
        "passage": None, "stem": stem,
        "blanks": [{"label": "Blank", "choices": ch}],
        "correct": sorted(correct2), "explanation": "",
    }


def rc(qid, passage, stem, choices5, correct_letter, diff="medium", subtype="single_answer"):
    labels = ["A","B","C","D","E"]
    ch = {labels[i]: choices5[i] for i in range(len(choices5))}
    return {
        "id": qid, "section": "verbal", "type": "reading_comprehension",
        "subtype": subtype, "difficulty": diff, "set": None,
        "passage": passage, "stem": stem,
        "blanks": [{"label": "Blank", "choices": ch}],
        "correct": [correct_letter] if isinstance(correct_letter, str) else correct_letter,
        "explanation": "",
    }


# ── HGset 문제 데이터 ──────────────────────────────────────────────────────────

questions = []

# ═══════════════════════════════════════════════════════════════════
# HGset #1  (Groups 1-2, Short Passage 1, Critical Reasoning 1)
# ═══════════════════════════════════════════════════════════════════

# Group #1 TC single blank
questions += [
    tc1("HG01_G1_TC_01",
        "In a production process that is complex and often unpredictable, roles that start out discretely defined may become quite __________.",
        ["confused","perfunctory","independent","overt","exacting"], "A"),
    tc1("HG01_G1_TC_02",
        "While the writer was best known for her much-ballyhooed __________, her impact reached far beyond memorable quips.",
        ["pensiveness","drollness","stoicism","fastidiousness","congeniality"], "B"),
]
# Group #1 TC double blank
questions += [
    tc2("HG01_G1_TC_03",
        "While people complain about their hectic lives and demanding schedules, one might be justified in suspecting that they are being somewhat (i) __________: compulsive busyness seems to be, for many, a source of (ii) __________.",
        ["disingenuous","guarded","dilatory"],
        ["pride","despair","irritation"],
        ["A","D"]),
    tc2("HG01_G1_TC_04",
        "The author argues that the field of sociology has been overly (i) __________, partly because, for many scholars, the edges of the social universe are defined by national borders. In this era of increasing globalization, however, sociology is presented with a historically distinct opportunity to transcend its former (ii) __________.",
        ["narrow in scope","susceptible to fads","averse to empiricism"],
        ["utilitarianism","parochialism","historicism"],
        ["A","E"]),
    tc2("HG01_G1_TC_05",
        "Readers may initially be irked by the book's apparent (i) __________ but, once immersed in the author's prose, they may come to regard the work's (ii) __________ as an asset.",
        ["flippancy","aimlessness","tendentiousness"],
        ["subtlety","discursions","exhaustiveness"],
        ["B","E"]),
]
# Group #1 TC triple blank
questions.append(
    tc3("HG01_G1_TC_06",
        "Those who took Clark's old-mannered compliance for obsequiousness (i) __________ him: his apparent (ii) __________ veiled a fervent (iii) __________ of the authority that others exercised over him, one that he occasionally expressed by discreetly sabotaging their most important projects.",
        ["misconstrued","condemned","respected"],
        ["cynicism","acquiescence","intractability"],
        ["veneration","justification","detestation"],
        ["A","E","I"])
)
# Group #1 SE
questions += [
    se("HG01_G1_SE_07",
       "When studying the ancient Greek astronomers Copernicus realized that despite the intrinsic beauty of many of their arguments, the ancients often made claims that __________ logic.",
       ["refuted","questioned","influenced","swayed","defied","disregarded"], ["E","F"]),
    se("HG01_G1_SE_08",
       "For all the __________ the new CEO has received from the press recently, her staff have a decidedly less rosy view of her.",
       ["encomiums","tributes","evaluations","critiques","attention","publicity"], ["A","B"]),
    se("HG01_G1_SE_09",
       "Coagulation factors are useful proteins whose simple names—many are known only by Roman numerals—__________ their importance and the specificity of their roles in the thinning and clotting of blood.",
       ["nullify","obviate","mitigate","belie","mask","accentuate"], ["D","E"]),
    se("HG01_G1_SE_10",
       "Although its director __________ that the movie uses a documentary approach in portraying the famous sit-down strike, in practice its characters are heavily fictionalized and fall into familiar Hollywood types.",
       ["asserts","concedes","guarantees","disputes","grants","maintains"], ["A","F"]),
]

# Group #2 TC single blank
questions += [
    tc1("HG01_G2_TC_01",
        "Though the volume of radioactive waste produced by nuclear power plants is __________, the problem of how to dispose of that waste is not: rather, it is of major importance.",
        ["unmanageable","troubling","significant","small","deceptive"], "D"),
    tc1("HG01_G2_TC_02",
        "We often regard natural phenomena like rainfall as mysterious and unpredictable; although for short time spans and particular places they appear so, in fact on a truly global scale, nature has been a model of __________.",
        ["reliability","diversity","complexity","plasticity","discontinuity"], "A"),
]
# Group #2 TC double blank
questions += [
    tc2("HG01_G2_TC_03",
        "The national bank has been uncommonly powerful in comparison to its counterparts in other nations. It retains this potency partly because its control of the nation's banking system is (i) __________ governmental interference, and thus its actions remain largely (ii) __________.",
        ["unencumbered by","replete with","hindered by"],
        ["compulsory","discretionary","bureaucratic"],
        ["A","E"]),
    tc2("HG01_G2_TC_04",
        "The material covered in this article has been (i) __________ in previous publications, and since currently neglected areas remained unexplored, the article contains no (ii) __________.",
        ["skirted","scrutinized","countered"],
        ["revelations","distortions","conclusions"],
        ["B","D"]),
]
# Group #2 TC triple blank
questions += [
    tc3("HG01_G2_TC_05",
        "Unambiguous texts can allow their readers to (i) __________ them quickly, but ambiguous texts can have the attractive (ii) __________ of multiple possible interpretations, all of which can be considered equally (iii) __________, and none of which is the single true meaning.",
        ["misunderstand","comprehend","complicate"],
        ["stigma","blemish","allure"],
        ["valid","frank","inveterate"],
        ["B","F","G"]),
    tc3("HG01_G2_TC_06",
        "Even the reader acquainted with the outlines of Pushkin's biography will be (i) __________ the (ii) __________ so vividly conveyed in Binyon's biography. Not only was Pushkin's personal correspondence intercepted and his movements (iii) __________, but Tsar Nicholas I's decision to oversee Pushkin's career obliged Pushkin to submit all his manuscripts for inspection.",
        ["attracted to","confused by","struck by"],
        ["suffocating lack of creative freedom","concern for contemporary society","underlying sense of historical change"],
        ["ignored","monitored","commended"],
        ["C","D","H"]),
]
# Group #2 SE
questions += [
    se("HG01_G2_SE_07",
       "The uniquely human activity to rethink and revise our social arrangements is a weird blessing, allowing us to create systems that are as likely to __________ us as to liberate us.",
       ["cheer","shackle","admonish","educate","stifle","enliven"], ["B","E"]),
    se("HG01_G2_SE_08",
       "Although field studies have linked inbreeding to declines among song sparrow populations, some researchers argue that, in nature, inbreeding proves __________ as a factor when compared with crushing blows from weather changes.",
       ["hazardous","momentous","trivial","significant","precarious","inconsequential"], ["C","F"]),
    se("HG01_G2_SE_09",
       "Although the insistence on balancing spending tax revenues has contributed to the economy's stagnation, unfortunately, the government does not seem likely to __________ this rigid policy.",
       ["initiate","persist in","publicize","repudiate","continue","recant"], ["D","F"]),
    se("HG01_G2_SE_10",
       "Since it was committed to the idea of science as an international, politically neutral enterprise, the Royal Society of London refused to __________ members from enemy nations during world wars of the twentieth century.",
       ["betray","expel","endorse","oust","sanction","condemn"], ["B","D"]),
]

# Short Passage 1
_p1 = ("A divide between aesthetic and technical considerations has played a crucial role in mapmaking and cartographic scholarship. "
       "Since nineteenth century cartographers, for instance, understood themselves as technicians who did not care about visual effects, "
       "while others saw themselves as landscape painters. That dichotomy structured the discipline of the history of cartography. "
       "Until the 1980s, in what Blakemore and Harley called 'the Old is Beautiful Paradigm,' scholars largely focused on maps made before 1800, "
       "marveling at their beauty and sometimes regretting the decline of the pre-technical age. Early mapmaking was considered art while modern "
       "cartography was located within the realm of engineering utility. Alpers, however, has argued that this boundary would have puzzled mapmakers "
       "in the seventeenth century, because they considered themselves to be visual engineers.")
questions += [
    rc("HG01_SP1_RC_01", _p1,
       "According to the passage, Alpers would say that the assumptions underlying the 'paradigm' were",
       ["inconsistent with the way some mapmakers prior to 1800 understood their own work",
        "dependent on a seventeenth-century conception of mapmaking visual engineering",
        "unconcerned with the difference between the aesthetic and technical questions of mapmaking",
        "insensitive to divisions among cartographers working in the period after 1800",
        "supported by the demonstrable technical superiority of mapmaking made after 1800"],
       "A"),
    rc("HG01_SP1_RC_02", _p1,
       "It can be inferred from the passage that, beginning in the 1980s, historians of cartography",
       ["placed greater emphasis on the beauty of maps made after 1800",
        "expanded their range of study to include more material created after 1800",
        "grew more sensitive to the way mapmakers prior to 1800 conceived of their work",
        "came to see the visual details of maps as aesthetic objects rather than practical cartographic aids",
        "reduced the attention they paid to the technical aspects of mapmaking"],
       "B"),
]

# Critical Reasoning 1
_cr1 = ("Until very recently, Presorbin and Veltrex, two medications used to block excess stomach acid, were both available only with "
        "a prescription written by a doctor. In an advertisement for Presorbin, its makers argue that Presorbin is superior on the grounds "
        "that doctors have written 200 million prescriptions for Presorbin, as compared to 100 million for Veltrex. It can be argued that "
        "the number of prescriptions written is never a worthwhile criterion for comparing the merits of medicines, but that the advertisement's "
        "argument is absurd is quite adequately revealed by observing that Presorbin was available as a prescription medicine years before Veltrex was.")
questions.append(
    rc("HG01_CR1_RC_01", _cr1,
       "In the columnist's argument, the two highlighted portions play which of the following roles?",
       ["The first is a claim that the columnist's argument seeks to clarify; the second states a conclusion drawn about one possible interpretation of that claim.",
        "The first identifies the conclusion of an argument that the columnist's argument is directed against; the second states the main conclusion of the columnist's argument.",
        "The first states the main conclusion of the columnist's argument; the second states a conclusion that the columnist draws in defending that conclusion against an objection.",
        "The first identifies an assumption made in an argument that the columnist's argument is directed against; the second states the main conclusion of the columnist's argument.",
        "The first is a claim that has been offered as evidence to support a position that the columnist opposes; the second states the main conclusion of the columnist's argument."],
       "B")
)

# ═══════════════════════════════════════════════════════════════════
# HGset #2  (Groups 3-4, Short Passage 2, Critical Reasoning 2)
# ═══════════════════════════════════════════════════════════════════

# Group #3 TC single blank
questions += [
    tc1("HG02_G3_TC_01",
        "Among the Meakambut people of Papua New Guinea, legends are associated with specific caves in the Speik region, and the legends are __________: only cave owners can share its secrets.",
        ["impenetrable","immutable","proprietary","didactic","self-perpetuating"], "C"),
    tc1("HG02_G3_TC_02",
        "It is a paradox of the Victorians that they were both __________ and, throughout the empire, cosmopolitan.",
        ["capricious","insular","mercenary","idealistic","intransigent"], "B"),
]
# Group #3 TC double blank
questions += [
    tc2("HG02_G3_TC_03",
        "Despite the scathing precision with which she satirizes the lies of the social aspirants and moneyed folk, the writer appears to (i) __________ being part of the world she presents as so (ii) __________.",
        ["abhor","relish","evoke"],
        ["unattainable","insufferable","enchanting"],
        ["B","E"]),
    tc2("HG02_G3_TC_04",
        "The contemporary trend whereby fashion designers flout mainstream tradition is unique only in its (i) __________; earlier fashion designers experienced the same (ii) __________ impulse, albeit in a less extreme form.",
        ["subversiveness","intensity","palpability"],
        ["indiscriminate","iconoclastic","temperate"],
        ["B","E"]),
    tc2("HG02_G3_TC_05",
        "Memory-prompt technology such as online birthday reminders does more than enhance our recall abilities; it induces us to (i) __________ ever more behaviors to automated processes. Witness the (ii) __________ a program that allows us to create computer greeting cards for the entire year in one setting.",
        ["delegate","ascribe","liken"],
        ["controversy over","popularity of","sophistication of"],
        ["A","E"]),
]
# Group #3 TC triple blank
questions.append(
    tc3("HG02_G3_TC_06",
        "Biologists have little (i) __________ drawing the link between the success of humanity and human (ii) __________. Indeed, many biologists claim that this attribute, the ability to (iii) __________, or, to put it more sharply, to make individuals subordinate their self-interest to the needs of the group, lies at the root of human achievement.",
        ["consciences regarding","compunction about","justification for"],
        ["reflect","sociability","uniqueness"],
        ["communicate","cooperate","reticence"],
        ["B","E","H"])
)
# Group #3 SE
questions += [
    se("HG02_G3_SE_07",
       "Progressive and reactionary populist movements are not necessarily __________: each may, and usually does, possess the features of the other.",
       ["dichotomous","untenable","unsustainable","contradictory","subversive","efficacious"], ["A","D"]),
    se("HG02_G3_SE_08",
       "Flawed as it may be for it is constructed by subjective scientists, science itself has methods that help us __________ our bias and talk about objective reality with some validity.",
       ["bypass","reduce","exacerbate","magnify","acknowledge","circumvent"], ["A","F"]),
    se("HG02_G3_SE_09",
       "In Japanese aesthetics, especially but not only in Noh, beauty contains the idea of __________: beauty must have an air of evanescence, the intimation of its own demise.",
       ["transience","symmetry","decay","simplicity","balance","deterioration"], ["A","C"]),
    se("HG02_G3_SE_10",
       "Although one can adduce myriad of examples of ecosystem disruption by nonindigenous species, nevertheless most introduced species that survived in fact appear to have quite __________ effects on the ecosystem they have invaded.",
       ["minimal","trifling","marked","conspicuous","intriguing","deleterious"], ["A","B"]),
]

# Group #4 TC single blank
questions += [
    tc1("HG02_G4_TC_01",
        "Apparently, advanced tortoises evolved multiple times: the high-domed shells and columnar, elephantine feet of current forms are specializations for terrestrial life that evolved __________ on each continent.",
        ["independently","interchangeably","paradoxically","simultaneously","symmetrically"], "A"),
    tc1("HG02_G4_TC_02",
        "Instead of demonstrating the __________ of archaeological applications of electronic remote sensing, the pioneering study became, to some skeptics, an illustration of the imprudence of interpreting sites based on virtual archeology.",
        ["ubiquity","redundancy","limitation","complexity","promise"], "E"),
]
# Group #4 TC double blank
questions += [
    tc2("HG02_G4_TC_03",
        "Given the __________ committees and the __________ nature of its investigation, it would be unreasonable to gainsay the committee's conclusions at first glance.",
        ["sterling reputation of","lack of funding for","ad hoc existence of"],
        ["superficial","spontaneous","exhaustive"],
        ["A","F"]),
    tc2("HG02_G4_TC_04",
        "Though many professional book reviewers would agree that criticism should be (i) __________ enterprise, a tendency to write (ii) __________ reviews has risen partly out of the mistaken belief that sharing personal details will help reviewers stand out of the pack.",
        ["an anonymous","an evenhanded","a spirited"],
        ["scathing","confessional","superficial"],
        ["A","E"]),
]
# Group #4 TC triple blank
questions.append(
    tc3("HG02_G4_TC_05",
        "Scientific papers often (i) __________ what actually happened in the course of the investigations they describe. Misunderstandings, blind alleys, and mistakes of various sorts will fail to appear in the final written accounts, because (ii) __________ is a desirable attribute when transmitting results in a science report and would be poorly served by (iii) __________.",
        ["amplify","misrepresent","particularize"],
        ["transparency","efficiency","exhaustiveness"],
        ["a comprehensive historical account","a purely quantitative analysis","an overly superficial discussion"],
        ["B","E","G"])
)
# Group #4 TC triple blank (q6)
questions.append(
    tc3("HG02_G4_TC_06",
        "Analysis of 47.5-million-year-old fossils from Pakistan has yielded fresh insights into the early ancestors of modern whales. Maiacetus inuus was a land animal (i) __________ life in the sea. One fossil encased a fetus positioned for a head-first delivery, typical of land mammals. But it probably spent much of its time (ii) __________: its big teeth were suited for catching fish, while its flipper-like feet must have been (iii) __________ walking.",
        ["resistant to","removed from","adapted to"],
        ["in the water","fleeing from predators","on the ground"],
        ["incompatible with","clumsy for","strengthened by"],
        ["C","G","H"])
)
# Group #4 SE
questions += [
    se("HG02_G4_SE_07",
       "The Chavez Pass archaeological site was initially interpreted as indicative of __________ society, since it was thought to have been at the center of a cluster of smaller, contemporary settlements that it presumably controlled.",
       ["an expansionist","a hierarchical","an urban","a heterogeneous","a diverse","a stratified"], ["B","F"]),
    se("HG02_G4_SE_08",
       "Even if the story now seems a surprisingly innocuous overture to the author's later, more fully developed narrations, it __________ some of the key traits of those bleaker tales.",
       ["avoids","belies","undercuts","anticipates","possesses","prefigures"], ["D","F"]),
    se("HG02_G4_SE_09",
       "In the absence of a surface gradient, the new laws of refraction and reflection are __________ the conventional law, so they represent more of an extension than a complete revolution.",
       ["inferable from","entailed by","antithetical to","coincident with","antecedent to","oppositional to"], ["A","B"]),
    se("HG02_G4_SE_10",
       "While recognizing that recent reports of cyber warfare, phone-hacking scandals, and identity thefts have tended to accent the destructive connotation of the word, Sur Halpern maintains that 'hacking' is such __________ term that its meaning nearly always derives from its context.",
       ["a generic","an inclusive","a positive","a subjective","an affirmative","a technical"], ["A","B"]),
]

# Short Passage 2
_p2 = ("Most mammals reach sexual maturity when their growth rates are in decline, whereas humans experience a growth spurt during adolescence. "
       "Whether apes experience an adolescent growth spurt is still undecided. In the 1950s, data on captive chimpanzees collected by James Gavan "
       "appeared devoid of evidence of an adolescent growth spurt in these apes. In a recent reanalysis of Gavan's data, however, zoologist "
       "Elizabeth Watts has found that as chimpanzees reach sexual maturity, the growth rate of their limbs accelerates. Most biologists, however, "
       "are skeptical that this is a humanlike adolescent growth spurt. While the human adolescent growth spurt is physically obvious and affects "
       "virtually the entire body, the chimpanzee's increased growth rate is detectable only through sophisticated mathematical analysis. Moreover, "
       "according to scientist Holly Smith, the growth rate increase in chimpanzees begins when 86% of full skeletal growth has been attained, "
       "whereas human adolescence generally commences when 77 percent of full skeletal growth has occurred.")
questions += [
    rc("HG02_SP2_RC_01", _p2,
       "Which of the following best describes the main idea of the passage?",
       ["Researchers have long disagreed about whether data collected in the 1950s indicate that chimpanzees and other apes experience an adolescent growth spurt.",
        "Research data collected on chimpanzees living in captivity are inconclusive with respect to chimpanzees living in the wild.",
        "The notion that apes do not experience an adolescent growth spurt has been confirmed by research conducted since.",
        "Although the idea that apes experience an adolescent growth spurt has received some support, most biologists remain unconvinced.",
        "Although researchers agree that chimpanzees do not experience an adolescent growth spurt, they are divided in their opinions of whether this is true of other apes."],
       "D"),
    rc("HG02_SP2_RC_02", _p2,
       "The passage mentions which of the following as one of the reasons why most biologists remain skeptical that chimpanzees experience a humanlike adolescent growth spurt?",
       ["Chimpanzees do not experience a demonstrable increase in growth rate until they are fully sexually mature.",
        "The increase in growth rate that chimpanzees undergo at sexual maturity is less apparent than that of humans.",
        "The increase in growth rate once regarded as a humanlike adolescent growth spurt in chimpanzees is too sporadic to be regarded as significant.",
        "Not all chimpanzees undergo a calculable growth spurt.",
        "Watt's approach to analyzing data is considered to be highly unorthodox."],
       "B"),
    rc("HG02_SP2_RC_03", _p2,
       "The passage suggests which of the following about the adolescent growth spurt that takes place in humans?",
       ["Its primary effects are found in parts of the body other than the limbs.",
        "It is generally completed by the time 77 percent of full skeletal growth is attained.",
        "It is normally detectable without the assistance of sophisticated mathematical analysis.",
        "The rate of growth is much faster at the beginning of puberty than at any other time.",
        "The estimated growth rate varies depending on the methods of measurement that are used."],
       "C"),
]

# Critical Reasoning 2
_cr2 = ("Stylistic evidence and laboratory evidence strongly support the claim that the magnificent painting Garden of Eden is a work of the "
        "Flemish master van Eyck. Nevertheless, the painting must have been the work of someone else, as anyone with a little historical and "
        "zoological knowledge can tell merely by looking at the painting. The animals in the painting are all vivid representations of actual "
        "animals, including armadillos. Yet armadillos are native only to the Americas, and van Eyck died decades before Europeans reached the Americas.")
questions.append(
    rc("HG02_CR2_RC_01", _cr2,
       "In the argument given, the two highlighted portions play which of the following roles?",
       ["The first is a position that the argument seeks to reject; the second is evidence that the argument uses against that position.",
        "The first and the second are each pieces of evidence that have been used to support the position that the argument opposes.",
        "The first presents the main conclusion of the argument; the second provides evidence in support of that conclusion.",
        "The first is a judgment that serves as the basis for the main conclusion of the argument; the second states that main conclusion.",
        "The first is an intermediate conclusion drawn in order to support a further conclusion stated in the argument; the second provides evidence in support of that intermediate conclusion."],
       "C")
)

# ═══════════════════════════════════════════════════════════════════
# HGset #3  (Groups 5-6, Short Passage 3, Critical Reasoning 3)
# ═══════════════════════════════════════════════════════════════════

questions += [
    tc1("HG03_G5_TC_01",
        "A new television documentary focuses on one of the prime minister's defining contradictions, portraying her as a woman who cultivated an image of __________, but who liked to live grandly.",
        ["irascibility","abstemiousness","contentiousness","insouciance","surreptitiousness"], "B"),
    tc1("HG03_G5_TC_02",
        "In proto-scientific times, claims about the physical world were often accepted as true if they were reasonable; experimental verification, if thought necessary at all, was __________.",
        ["utilitarian","perfunctory","egregious","empirical","inductive"], "B"),
    tc2("HG03_G5_TC_03",
        "The economic recovery was somewhat lopsided; (i) __________ in some of the industrial economies while (ii) __________ in others of them.",
        ["unexpected","robust","feeble"],
        ["turbulent","swift","predictable"],
        ["C","D"]),
    tc2("HG03_G5_TC_04",
        "Scholarly works on detective stories often begin with (i) __________, suggesting that there is something vaguely wrong with adults who spend their time reading such fiction and certainly something (ii) __________ those who devote energy to its analysis.",
        ["chronologies","apologies","synopses"],
        ["awry in","astute about","courageous about"],
        ["B","D"]),
    tc2("HG03_G5_TC_05",
        "Due to the extraordinary circumstances, British business owners found themselves in a (i) __________ position during the Second World War, forced to accept regular interference from government and to acquiesce to (ii) __________ role for labor unions in negotiating the terms and conditions of employment.",
        ["defensive","dominant","customary"],
        ["a traditional","an enhanced","a diminished"],
        ["A","E"]),
    tc3("HG03_G5_TC_06",
        "For almost two centuries, the German island of Sylt has offered various therapies for every conceivable (i) __________ from broken bones to liver complaints. The local mud, saltwater, thermal pools, and spas have been deemed (ii) __________ by the German medical system, which (iii) __________ some of these treatments. Consequently, the treatments are widely used.",
        ["malady","indiscretion","prognosis"],
        ["healthful","suspect","innocuous"],
        ["doubts","denies","funds"],
        ["A","D","I"]),
    se("HG03_G5_SE_07",
       "Miller reminded his clients that labor relationship is inherently __________: the interests of business owners are diametrically opposed to those of employees.",
       ["adversarial","exploitative","mercenary","antagonistic","variable","changeable"], ["A","D"]),
    se("HG03_G5_SE_08",
       "Progressive and reactionary populist movements are not necessarily __________; each may, and usually does, possess features of the other.",
       ["dichotomous","untenable","unsustainable","contradictory","subversive","efficacious"], ["A","D"]),
    se("HG03_G5_SE_09",
       "Even the cleverest use of time management techniques is powerless to __________ the sum of minutes in a person's life, so people squeeze as much as they could into each one of them.",
       ["justify","quantify","augment","enrich","measure","extend"], ["C","F"]),
    se("HG03_G5_SE_10",
       "One of the vocalists who auditioned for a leading part in the local production of Sweeney Todd seemed to prefer __________ to any attempts at producing a melody; a more unpleasant voice was hard to imagine.",
       ["warbling","imitating","improvising","shrieking","crooning","caterwauling"], ["D","F"]),
]

questions += [
    tc1("HG03_G6_TC_01",
        "The space travels described in science fiction stories always used to be epic adventures, in comparison to which current journeys in space seem quite __________.",
        ["mundane","exciting","dramatic","risky","heroic"], "A"),
    tc1("HG03_G6_TC_02",
        "Medieval cathedrals still stand as marvels of architecture, but as far as modern science is concerned, medieval physics and chemistry are simply irrelevant, at best a dead end, at worst the very __________ of what science is supposed to be.",
        ["exemplar","glorification","reflection","dilution","antithesis"], "E"),
    tc2("HG03_G6_TC_03",
        "Although trains may use energy more (i) __________ than do automobiles, the latter move only when they contain at least one occupant, whereas railway carriages spend a considerable amount of time running up and down the tracks (ii) __________, or nearly so.",
        ["lavishly","efficiently","routinely"],
        ["vacant","unimpeded","overloaded"],
        ["B","D"]),
    tc2("HG03_G6_TC_04",
        "Historian Barbara Alpern Engel's task in writing a book about women in Russia must have been a (i) __________ one, because the (ii) __________ the Russian empire's peoples meant that Russian women could never be treated as a homogeneous group.",
        ["motivating","boring","daunting"],
        ["unity among","disinterest in","diversity of"],
        ["C","F"]),
    tc3("HG03_G6_TC_05",
        "One sometimes hears that Marco Polo introduced pasta to the Western world, having encountered it in China. This durable myth, which (i) __________ that nothing should have been known to pasta in Italy until 1295, can easily be (ii) __________ by pointing out that there are Italian references to pasta that (iii) __________.",
        ["requires","demonstrates","symbolizes"],
        ["augmented","debunked","traced"],
        ["praise its virtues","can be authenticated","predate that event"],
        ["A","E","I"]),
    tc3("HG03_G6_TC_06",
        "Both very good and very bad books are easy to review. Praise and (i) __________ come easily. But what of books that contain a muddle of virtues and vices? Here the reviewer's task is more (ii) __________: the author's useful and thought-provoking observations need to be (iii) __________ the useless and tedious.",
        ["ambivalence","compliment","censure"],
        ["evident","demanding","manageable"],
        ["supplanted by","sifted from","overshadowed by"],
        ["C","E","H"]),
    se("HG03_G6_SE_07",
       "Even though women in the United States would not gain the right to vote until 1920, throughout the nineteenth century many feminist goals were gradually __________, especially the rights of married women to control their own property.",
       ["realized","abandoned","eroded","modified","revised","achieved"], ["A","F"]),
    se("HG03_G6_SE_08",
       "It is hardly __________ the committee calls for: rudimentary competence would be an improvement on the current chaos.",
       ["accountability","faultlessness","disarray","loyalty","unrichness","perfection"], ["B","F"]),
    se("HG03_G6_SE_09",
       "Edited collections of scholarly essays generally tend to be somewhat uneven: they suffer from the __________ subject matter of the various essays, the lack of an overarching and consistent thesis, and the variable quality of the contributions.",
       ["intriguing","heterogeneous","comprehensive","disparate","mediocre","engaging"], ["B","D"]),
    se("HG03_G6_SE_10",
       "Films that critics have slumbered through rarely generate industry excitement, even though the critics' __________ reception may be less the fault of the movie than of its unfortunate time slot near a fatiguing film festival's conclusion.",
       ["somnolent","impartial","lethargic","laconic","befuddled","evenhanded"], ["A","C"]),
]

_p3 = ("Many cultural anthropologists have come to reject the scientific framework of empiricism that dominated the field until the 1970s "
       "and now regard all scientific knowledge as socially constructed. They argue that information about cultures during the empiricist era "
       "typically came from anthropologists who brought with them a prepackaged set of conscious and unconscious biases. Cultural anthropology, "
       "according to the post-1970s critique, is unavoidably subjective, and the anthropologist should be explicit in acknowledging that fact. "
       "Anthropology should stop striving to build a better database about cultural behavior and should turn to developing a more humanistic "
       "interpretation of cultures. The new framework holds that it may be more enlightening to investigate the biases of earlier texts than to "
       "continue with empirical methodologies.")
questions += [
    rc("HG03_SP3_RC_01", _p3,
       "The author implies which of the following about most cultural anthropologists working prior to the 1970s?",
       ["They argued that scientific knowledge was socially constructed.",
        "They were explicit in acknowledging the biases inherent in scientific investigation.",
        "They regarded scientific knowledge as consisting of empirical truths.",
        "They shared the same conscious and unconscious biases.",
        "They acknowledged the need for a new scientific framework."],
       "C"),
    rc("HG03_SP3_RC_02", _p3,
       "According to the passage, 'many cultural anthropologists' today would agree that anthropologists should",
       ["build a better, less subjective database about cultural behavior",
        "strive to improve the empirical methodologies used until the 1970s",
        "reject the notion that scientific knowledge is socially constructed",
        "turn to examining older anthropological texts for unacknowledged biases",
        "integrate humanistic interpretations with empirical methodologies"],
       "D"),
]

_cr3 = ("New methods developed in genetic research have led taxonomists to revise their views on the evolutionary relationships between many "
        "species. Traditionally the relatedness of species has been ascertained by a close comparison of their anatomy. The new methods infer "
        "the closeness of any two species' relationship to each other directly from similarities between the species' genetic codes.")
questions.append(
    rc("HG03_CR3_RC_01", _cr3,
       "Which of the following conclusions is best supported by the information?",
       ["The apparent degree of relatedness of some species, as determined by anatomical criteria, is not borne out by their degree of genetic similarity.",
        "When they know the differences between two species' genetic codes, taxonomists can infer what the observable anatomical differences between those species must be.",
        "The degree to which individuals of the same species are anatomically similar is determined more by their genetic codes than by such environmental factors as food supply.",
        "The traditional anatomical methods by which taxonomists investigated the relatedness of species are incapable of any further refinement.",
        "Without the use of genetic methods, taxonomists would never be able to obtain any accurate information about species' degrees of relatedness to one another."],
       "A")
)

# ═══════════════════════════════════════════════════════════════════
# HGset #4  (Groups 7-8, Short Passage 4, Critical Reasoning 4)
# ═══════════════════════════════════════════════════════════════════

questions += [
    tc1("HG04_G7_TC_01",
        "The governor might conceivably find a genuine resolution to the budgetary dilemma, but she may be tempted to engage in a deception: a __________ exercise in fiscal prudence.",
        ["rigorous","sparkling","specious","blatant","convincing"], "C"),
    tc1("HG04_G7_TC_02",
        "Without seeming unworldly, William James appeared wholly removed from the __________ of society, the conventionality of academe.",
        ["ethos","idealism","romance","paradoxes","commonplaces"], "E"),
    tc2("HG04_G7_TC_03",
        "The great (i) __________ of most books that examine the American presidency is their ideological bias, but for the most part, this volume on the presidency maintains an impressive degree of (ii) __________.",
        ["contribution","limitation","paradox"],
        ["certainty","fluency","objectivity"],
        ["B","F"]),
    tc2("HG04_G7_TC_04",
        "The reclusive clergyman may have lived and died in melancholy, but this doesn't seem to have (i) __________ his genius in any way. On the contrary, we find ourselves wondering whether his genius wasn't (ii) __________ in some mysterious way by his mood.",
        ["influenced","hampered","triggered"],
        ["served","controlled","identified"],
        ["B","D"]),
    tc2("HG04_G7_TC_05",
        "The author argued that the field of sociology has been overly (i) __________, partly because, for many scholars, the edges of the social universe are defined by national borders. In this era of increasing globalization, however, sociology is presented with a historically distinct opportunity to transcend its former (ii) __________.",
        ["narrow in scope","susceptible to fads","averse to empiricism"],
        ["utilitarianism","parochialism","historicism"],
        ["A","E"]),
    tc3("HG04_G7_TC_06",
        "Applications of the Endangered Species Act have fared best in contexts in which habitat condition is closely linked to species condition and the cause of habitat degradation is easily identified. The achievements of the ESA in those contexts, however, have (i) __________ that other uses of the act can (ii) __________ that record even where such favorable conditions do not (iii) __________.",
        ["quelled the conviction","presaged the uncertainty","fostered the misconception"],
        ["mitigate","duplicate","elucidate"],
        ["vary","pertain","diminish"],
        ["C","E","H"]),
    se("HG04_G7_SE_07",
       "Since some contemporary Western dieticians believe that the only function of food is to provide nourishment, these dieticians view an emphasis on the aesthetic dimension of the culinary arts as __________.",
       ["unprecedented","unwarranted","illuminating","groundless","promising","novel"], ["B","D"]),
    se("HG04_G7_SE_08",
       "Harper Lee's narration in To Kill a Mockingbird is __________, mixing an adult's and a child's perspective according to no logic other than the immediate exigencies of the plot.",
       ["a paradigm","a hodgepodge","a model","an innovation","a patchwork","an embarrassment"], ["B","E"]),
    se("HG04_G7_SE_09",
       "A clever form of diplomacy involves subtly inducing the other party to propose your preference so that your __________ their requests appears as the granting of a concession.",
       ["accession to","inattention to","subversion of","abnegation of","repudiation of","acquiescence to"], ["A","F"]),
    se("HG04_G7_SE_10",
       "The employee had a reputation for fractiousness, but his coworkers found him to be, on the contrary, quite __________.",
       ["insightful","affable","sagacious","capable","easygoing","productive"], ["B","E"]),
]

questions += [
    tc1("HG04_G8_TC_01",
        "The idea of a 'language instinct' may seem __________ to those who think of language as the zenith of the human intellect and of instincts as brute impulses.",
        ["jarring","plausible","gratifying","inevitable","conciliatory"], "A"),
    tc1("HG04_G8_TC_02",
        "In contrast to such sparsely populated terrestrial habitats as desert and tundra, the oceans __________ with a seemingly endless array of creatures.",
        ["teem","flow","evolve","roil","ebb"], "A"),
    tc2("HG04_G8_TC_03",
        "As Ellen Donkin explains, in eighteenth-century England, writing plays (i) __________ women. Even when the (ii) __________ meant that playwriting did not bring personal fame, the work nonetheless enabled them to present their own views to the public and offered the possibility of acquiring capital.",
        ["empowered","overextended","impressed"],
        ["use of a pseudonym","lack of a producer","poor remuneration"],
        ["A","D"]),
    tc2("HG04_G8_TC_04",
        "The national bank has been uncommonly powerful in comparison to its counterparts in other nations. It remains this potency partly because its control of the nation's banking system (i) __________ governmental interference, and thus its actions remain largely (ii) __________.",
        ["unencumbered by","replete with","hindered by"],
        ["compulsory","discretionary","bureaucratic"],
        ["A","E"]),
    tc3("HG04_G8_TC_05",
        "Just because, as a photographer, Friedlander (i) __________ places that most people consider ugly does not mean that he is out to prove they are beautiful. Instead, his work suggests that the photographer simply cannot ignore so much of the built American landscape but is obligated to (ii) __________ what we pass through day in and day out, regardless of (iii) __________.",
        ["tends to avoid","is harshly critical of","is interested in"],
        ["document","emulate","discredit"],
        ["authenticity","truthfulness","aesthetics"],
        ["C","D","I"]),
    tc3("HG04_G8_TC_06",
        "Traditional Vietnamese culture has long promoted the idea of gender equality. Founding myths (i) __________ the equal division of labor in child care for mothers and fathers. As is often the case, however, theoretical commitments are (ii) __________ actual processes. In reality, gender-based (iii) __________ persists.",
        ["obscure","celebrate","countermand"],
        ["incommensurate with","surpassed by","inspired by"],
        ["parity","inclusiveness","stratification"],
        ["B","D","I"]),
    se("HG04_G8_SE_07",
       "Culture, like speech, is primarily a human faculty, although both functions may exist in a more __________ form in lesser primates.",
       ["indispensable","crucial","primitive","intelligible","recognizable","rudimentary"], ["C","F"]),
    se("HG04_G8_SE_08",
       "In mathematics, judgment about the validity of proofs are mediated by peer-reviewed journals; to ensure __________, reviewers are carefully chosen by journal editors, and the identity of scholars whose papers are under consideration are kept secret.",
       ["timelessness","originality","fairness","comprehensiveness","objectivity","novelty"], ["C","E"]),
    se("HG04_G8_SE_09",
       "Jackie Wullschlager's biography of Hans Christian Andersen __________ the insipid sweetness with which Andersen coated his life and reveals a vulnerable gingerbread man with a bitter almond where his heart should be.",
       ["conjure up","imagines","strips away","overlooks","removes","ignores"], ["C","E"]),
    se("HG04_G8_SE_10",
       "While it is always clear that the author's message is heartfelt, it is mostly buried by shortcomings of style, organization, and production, although the book does become more __________ toward the end.",
       ["sincere","intelligible","orthodox","readable","frank","voluble"], ["B","D"]),
]

_p4 = ("Writing about nineteenth-century women's travel writing, Lila Harper notes that the four women she discussed used their own names, "
       "in contrast with the nineteenth-century female novelists who either published anonymously or used male pseudonyms. The novelists "
       "doubtless realized that they were breaking boundaries, whereas three of the four daring, solitary travelers espoused traditional values, "
       "eschewing radicalism and women's movements. Whereas the female novelists criticized their society, the female travelers seemed content "
       "to leave society as it was while accomplishing their own liberation. In other words, they lived a contradiction. For the subjects of "
       "Harper's study, solitude in both the private and public spheres prevailed—a solitude that conferred authority, hitherto a male prerogative, "
       "but that also precluded any collective action or female solidarity.")
questions += [
    rc("HG04_SP4_RC_01", _p4,
       "Which of the following best characterizes the 'contradiction' that the author refers to?",
       ["The subjects of Harper's study enjoyed solitude, and yet as travelers they were often among people.",
        "Nineteenth-century travel writers used their own names, but nineteenth-century novelists used pseudonyms.",
        "Women's movements in the nineteenth-century were not very radical in comparison with those of the twentieth-century.",
        "Nineteenth-century female novelists thought they were breaking boundaries, but it was the nineteenth-century women who traveled alone who were really doing so.",
        "While traveling alone in the nineteenth-century was considered a radical act for a woman, the nineteenth-century solitary female travelers generally held conventional views."],
       "E"),
    rc("HG04_SP4_RC_02", _p4,
       "According to the passage, solitude had which of the following effects for the nineteenth-century female travelers? (Select all that apply.)",
       ["It conferred an authority typically enjoyed only by men.",
        "It prevented formation of alliances with other women.",
        "It relieved peer pressure to conform to traditional values."],
       ["A","B"], subtype="multi_answer"),
]

_cr4 = ("Sportfishers introduced the Zander, a type of perch, to Britain's rivers and canals in the 1970s. Because zander eat large numbers "
        "of smaller fish, they have had a devastating effect on native fish populations. To protect the native fish, a government program removed "
        "a significant proportion of the zander from Britain's waterways last year. Surprisingly, this year the loss of native fish to zander "
        "has been greater than before.")
questions.append(
    rc("HG04_CR4_RC_01", _cr4,
       "Which of the following, if true, would most help to explain the greater effect of zander on the native fish population?",
       ["The climate in Britain is very similar to the climate in regions to which zander are native.",
        "Most of the zander removed were fully grown, and fully grown zander eat large numbers of smaller zander.",
        "Every year a large number of zander are caught by sportfishers in Britain's waterways.",
        "Previous government programs designed to remove nonnative species from Britain's waterways have failed.",
        "Zander are just one of several nonnative fish that prey on the other fish found in Britain's waterways."],
       "B")
)

# ═══════════════════════════════════════════════════════════════════
# HGset #5  (Groups 9-10, Short Passage 5, Critical Reasoning 5)
# ═══════════════════════════════════════════════════════════════════

questions += [
    tc1("HG05_G9_TC_01",
        "The subjects who are engaged in more difficult tasks __________ deterioration in their performance over time, and therefore the need to concentrate apparently enhances long-term efficiency.",
        ["elicited","anticipated","noticed","displayed","evaded"], "E"),
    tc1("HG05_G9_TC_02",
        "The medical professor's thesis—hardly new, but rarely __________ by a faculty member of his distinction—is that patients are more than the sum of their symptoms and systems.",
        ["discounted","ignored","subverted","underestimated","espoused"], "E"),
    tc2("HG05_G9_TC_03",
        "Contrary to those who fear the impact of invasive species on native plants, the biologist contends that the threat posed to biodiversity by nonnative species is often (i) __________. For instance, a study of garlic mustard found that garlic mustard abundance in forest plots was not (ii) __________ the number of other plant species there.",
        ["subtle","uniform","exaggerated"],
        ["consistent with","related to","sustained by"],
        ["C","E"]),
    tc2("HG05_G9_TC_04",
        "Many of the towns that have voted to keep incinerators in the country's solid waste plan have done so not because they necessarily (i) __________ incinerators, but because they are (ii) __________ to narrow their waste-disposal options.",
        ["question","favor","oppose"],
        ["willing","eager","loath"],
        ["B","F"]),
    tc2("HG05_G9_TC_05",
        "Although movie critic Pauline Kael had a distaste for sycophancy, she also had a need for (i) __________, as a consequence of these competing feelings, she sent very (ii) __________ signals to friends and colleagues.",
        ["solitude","obeisance","clarity"],
        ["direct","subtle","mixed"],
        ["B","F"]),
    tc3("HG05_G9_TC_06",
        "A certain amount of theoretical frenzy about comics today is (i) __________. After all, similar frenzies have occurred in other art forms in periods of their rapid development. But such intellectual (ii) __________ rarely precedes creative glory. On the contrary, it commonly indicates that an artistic (iii) __________, having been made and recognized, is over, and that a process of increasingly strained emulation has set in.",
        ["understandable","unprecedented","perplexing"],
        ["torpor","conservatism","arousal"],
        ["pitfall","tradition","breakthrough"],
        ["A","F","I"]),
    se("HG05_G9_SE_07",
       "Scientists reported last month on a sign of relative solar __________: the solar wind, a rush of charged particles continually spewed from the Sun at a million miles an hour, had diminished to its lowest level in 50 years.",
       ["quiescence","turbulence","isolation","calm","remoteness","instability"], ["A","D"]),
    se("HG05_G9_SE_08",
       "Publicity surrounding celebrities' donations to charity is often greeted with cynicism, but a study of celebrity donations shows that they do __________ other donations.",
       ["preclude","elicit","allow","draw","bar","replace"], ["B","D"]),
    se("HG05_G9_SE_09",
       "Aerial viewings of the gigantic stone horse attributed to the Native American Quechuan people fail to __________ the considerable artistry required to create the piece: the horse appears crudely constructed unless carefully examined from the ground.",
       ["reveal","justify","manifest","mitigate","diminish","undercut"], ["A","C"]),
    se("HG05_G9_SE_10",
       "The laboratory maze has grown ever less __________ since it was first invented; instead of hoping to lose a rodent in a labyrinth, today's scientists design mazes to elicit a few simple, easily measured behaviors.",
       ["intricate","extensive","effective","convoluted","useful","prevalent"], ["A","D"]),
]

questions += [
    tc1("HG05_G10_TC_01",
        "The artist is known for making photographs that deal with politically charged subject matter, yet because her art is so evocative and open-ended, it would be wrong to characterize it as __________.",
        ["polemical","edifying","unobservant","innovative","ambiguous"], "A"),
    tc1("HG05_G10_TC_02",
        "Investors are grateful that the attorney general has stepped in to pursue inquiries into misfeasance in the financial markets, given that the regulators officially charged with policing the industry have been __________.",
        ["diffident","meticulous","straightforward","implacable","tenacious"], "A"),
    tc2("HG05_G10_TC_03",
        "The author of this travel guide (i) __________ to show his readers the city as it really is, but his information is not reliable: for example, his geography is (ii) __________, with one walking tour covering areas of the city that are twenty miles apart.",
        ["designs","forbears","purports"],
        ["erratic","erudite","extensive"],
        ["C","D"]),
    tc2("HG05_G10_TC_04",
        "The museum's compelling new architectural exhibition looks at eleven projects around the world that have had major (i) __________ impacts despite modest budgets. It is part of (ii) __________ in the museum's architecture and design department, which in the past has championed architecture's artistic value over its real-world consequences.",
        ["social","aesthetic","critical"],
        ["an emphasis on theory","a shift in philosophy","a rejection of pragmatism"],
        ["A","E"]),
    tc3("HG05_G10_TC_05",
        "Given children's active fantasy lives, one might think of truthfulness as (i) __________ virtue in young children, but it turns out that lying is the more (ii) __________ skill. A child who is going to lie must recognize the truth, intellectually conceive of an alternate reality, and be able to convincingly sell that new reality to someone else. Therefore, lying (iii) __________ cognitive development and social skills in a way that honesty simply does not.",
        ["an instinctive","an acquired","a conscious"],
        ["advanced","practical","mundane"],
        ["undermines","forgoes","demands"],
        ["B","D","I"]),
    tc3("HG05_G10_TC_06",
        "Within the culture as a whole, the natural sciences have been so successful that the word 'scientific' is often used in (i) __________ manner; it is often assumed that to call something 'scientific' is to imply that its reliability has been (ii) __________ by results that cannot reasonably be (iii) __________.",
        ["an ironic","a literal","an honorific"],
        ["maligned","challenged","established"],
        ["exaggerated","anticipated","disputed"],
        ["C","F","I"]),
    se("HG05_G10_SE_07",
       "The researcher noted that microbes, although __________, make up far more of the living protoplasm on Earth than all humans, animals and plants combined.",
       ["invisible","omnipresent","diminutive","ubiquitous","minuscule","ethereal"], ["C","E"]),
    se("HG05_G10_SE_08",
       "In matters of taste, the art patron and collector Peggy Guggenheim was __________: she was for the strangest, most surprising, the most satisfying, the best, the unique.",
       ["neophyte","novice","realist","extremist","pragmatist","zealot"], ["D","F"]),
    se("HG05_G10_SE_09",
       "In Inuit culture, elaborate carving has often been used to enhance __________ objects such as harpoon heads and other tools.",
       ["utilitarian","functional","domestic","decorative","manufactured","ornamental"], ["A","B"]),
    se("HG05_G10_SE_10",
       "Benjamin Franklin's reputation is so much one of pairing scientific investigation with commonsense empiricism that it is somewhat startling to realize how __________ his great experiment's mentoring truly was.",
       ["reasonable","speculative","pragmatic","conjectural","careless","judicious"], ["B","D"]),
]

_p5 = ("Although vastly popular during its time, much nineteenth-century women's fiction in the United States went unread by the "
       "twentieth-century educated elite, who were taught to ignore it as didactic. However, American literature has a tradition of "
       "didacticism going back to its Puritan roots, shifting over time from sermons and poetic transcripts into novels, which proved to be "
       "perfect vehicles for conveying social values. In the nineteenth century, critics reviled Poe for neglecting to conclude his stories "
       "with pithy moral tags, while Longfellow was canonized for his didactic verse. Although rhetorical changes favoring the anti-didactic "
       "can be detected as nineteenth-century America transformed itself into a secular society, it was twentieth-century criticism, which "
       "placed aesthetic value above everything else, that had no place in its doctrine for the didacticism of others.")
questions += [
    rc("HG05_SP5_RC_01", _p5,
       "Which of the following best describes the function of the highlighted sentence?",
       ["It explains why the fiction mentioned in the first sentence was not popular in the twentieth century.",
        "It assists in drawing a contrast between nineteenth-century and twentieth-century critics.",
        "It provides an example of how twentieth-century readers were taught to ignore certain literature.",
        "It questions the usefulness of a particular distinction between Poe and Longfellow made by critics.",
        "It explains why Poe's stories were more popular than Longfellow's verse during the nineteenth century."],
       "B"),
    rc("HG05_SP5_RC_02", _p5,
       "In the context in which it appears, 'conveying' most nearly means",
       ["carrying","transferring","granting","imparting","projecting"],
       "D"),
]

_cr5 = ("There are many structural and thematic similarities between Piers Plowman by Langland (1330-1400) and House of Fame by Chaucer "
        "(1342-1400), two Middle English poems relating dream visions. Some critics have argued that because a number of the shared elements "
        "are uncommon in Middle English poetry, and because Langland's poem probably predates Chaucer's by a few years, Chaucer was most "
        "likely influenced by Piers Plowman when writing House of Fame.")
questions.append(
    rc("HG05_CR5_RC_01", _cr5,
       "Which of the following, if true, most seriously weakens the critics' argument?",
       ["Piers Plowman is one of Langland's major works, whereas House of Fame is a minor work of Chaucer's.",
        "House of Fame survives in only three manuscript copies, substantially fewer than the number of manuscript copies that exist of Piers Plowman.",
        "Because Piers Plowman became a well-known work in its day, it is likely that the similarities were detected by many people who read House of Fame soon after Chaucer wrote it.",
        "Many of the themes and structures of Piers Plowman are also found in Latin, Italian, and French works with which Chaucer could well have been familiar.",
        "There is no evidence that Chaucer and Langland ever met or that they corresponded with each other about literary topics."],
       "D")
)

# ═══════════════════════════════════════════════════════════════════
# HGset #6  (Groups 11-12, Short Passage 6, Critical Reasoning 6)
# ═══════════════════════════════════════════════════════════════════

questions += [
    tc1("HG06_G11_TC_01",
        "For the urban researcher, the long lives of ancient cities can provide ample chronological data, making up for the paucity stemming from relative __________ of most present-day cities.",
        ["complexity","formlessness","transparency","diversity","youthfulness"], "E"),
    tc1("HG06_G11_TC_02",
        "Even if he wants to serve again—and given his obvious love for the job, the assumption among insiders is that he is more likely to stay than go—there is at least __________ his serving another term.",
        ["impediment to","incentive for","precedent for","benefit in","rationale for"], "A"),
    tc2("HG06_G11_TC_03",
        "Nordhaus predicts that in the future we will increasingly be (i) __________ ecological problems like global warming rather than (ii) __________ them. We may make some headway in limiting emissions, but much of our work will be in adapting to ecological problems and alleviating their effects.",
        ["managing","analyzing","transcending"],
        ["solving","addressing","mitigating"],
        ["A","D"]),
    tc2("HG06_G11_TC_04",
        "What they see in Tanaka is the one candidate capable of (i) __________ leadership, in direct contrast to Williamson, whose term in office has been marred by (ii) __________.",
        ["compassionate","decisive","nepotistic"],
        ["grandstanding","partisanship","vacillation"],
        ["B","F"]),
    tc2("HG06_G11_TC_05",
        "Partly because of Lee's skill at synthesizing (i) __________ trends drawn from many fields of study, her theories appeared to present, with uncanny aptness, ideas already (ii) __________ in the minds of her contemporaries.",
        ["superseded","irrelevant","emergent"],
        ["discredited","well-established","half-formulated"],
        ["C","F"]),
    tc3("HG06_G11_TC_06",
        "Unlike most other serious journals, which drain money from their owners, the Reviews has long been (i) __________. But the formula is not without its imperfections. The publication has always been erudite and (ii) __________ but not always lively and readable. (iii) __________, accompanied by a certain aversion to risk taking, has pervaded its pages for a long time.",
        ["lucrative","realistic","unesteemed"],
        ["authoritative","animated","trendy"],
        ["An originality","An impulsiveness","A staleness"],
        ["A","D","I"]),
    se("HG06_G11_SE_07",
       "Far from __________ innovations, as the patent system was designed to do, the patenting of concepts such as gene sequences gives individuals and corporations a legal chokehold over ideas that should be useful to all.",
       ["spurring","recognizing","codifying","acknowledging","fostering","cataloging"], ["A","E"]),
    se("HG06_G11_SE_08",
       "During the Renaissance, the use of optical lenses, which were capable of projecting images onto blank canvasses, greatly aided artists by allowing them to accurately observe and depict the external world; in other words, these lenses were instrumental in conveying __________.",
       ["idealism","optimism","ambition","realism","sanguinity","verisimilitude"], ["D","F"]),
    se("HG06_G11_SE_09",
       "The professor's habitual air of __________ was a misleading front, concealing amazing reserves of patience and a deep commitment to his students' learning.",
       ["cordiality","irascibility","disorganization","conviviality","diffidence","exasperation"], ["B","F"]),
    se("HG06_G11_SE_10",
       "Advocates for workers' rights have adopted a new strategy, one that will require considerable ingenuity but that if successful, could __________ a movement aimed at making labor rights an unassailable feature of American democracy.",
       ["frustrate","galvanize","presume","affect","animate","thwart"], ["B","E"]),
]

questions += [
    tc1("HG06_G12_TC_01",
        "Barring the discovery of new letters, hidden diaries, or the like, fresh information about eminent people is hard to find because their lives have been so intensely __________.",
        ["ridiculed","scrutinized","admired","embellished","underrated"], "B"),
    tc2("HG06_G12_TC_02",
        "Despite having only recently learned to walk, toddlers make the most (i) __________ dance students. Their joy and movement is so pure, so complete, and so (ii) __________.",
        ["skilled","inattentive","delightful"],
        ["futile","irrelevant","contagious"],
        ["C","F"]),
    tc2("HG06_G12_TC_03",
        "Tagore had a sharply defined sense of the (i) __________ of scientific inquiry. The fact that science dealt in statistics and numbers, that its logic was probabilistic, meant that the domain of moral questions (ii) __________ it: moral questions, for Tagore, required certainties, not probabilities.",
        ["irrationality","limits","futility"],
        ["guarded over","lay outside","was subject to"],
        ["B","E"]),
    tc3("HG06_G12_TC_04",
        "The modern iron suspension bridge dates from the early nineteenth century, but it did not have (i) __________ debut; many early suspension bridges were damaged, if not outright destroyed, by the wind. There were few (ii) __________, however, so the form (iii) __________.",
        ["a propitious","a conspicuous","an equivocal"],
        ["obvious parallels","practical alternatives","unnoticed instances"],
        ["declined","inspired","persisted"],
        ["A","E","I"]),
    tc3("HG06_G12_TC_05",
        "The experimental theater company's members know that their performances (i) __________ an audience, that they were dense and unpredictable and not always easy to digest. But none of the techniques used would be (ii) __________ anyone with an interest in music or films. The actors therefore felt that theater critics' derisive commentary showed only that the critics (iii) __________ the company's work.",
        ["made demands on","had to command","were sure to please"],
        ["contemplated by","alien to","intuitive for"],
        ["lambasted","exploited","misunderstood"],
        ["A","E","I"]),
    tc3("HG06_G12_TC_06",
        "The characters in this comic strip fret about the (i) __________ of their 'little counterculture lives,' especially when terrible things are happening in the world, but the cartoonist makes their lives (ii) __________ in ways that do not seem (iii) __________ at all. Real things happen here—births, deaths, adoptions, affairs, breakups—and they matter.",
        ["unpredictability","arduousness","triviality"],
        ["stagnate","resonate","compete"],
        ["outlandish","inconsequential","intangible"],
        ["C","E","H"]),
    se("HG06_G12_SE_07",
       "One __________ is that so far, Web services have turned out to be much harder to deliver than their champions had hoped.",
       ["hope","snag","prospect","hitch","upshot","reason"], ["B","D"]),
    se("HG06_G12_SE_08",
       "Asserting a need to preserve the __________ that became the hallmark of her predecessors' tenure, the new director of federal monetary policy refused to subscribe to rigid or mechanistic rules in policy making.",
       ["firmness","adaptability","unpredictability","autonomy","strictness","flexibility"], ["B","F"]),
    se("HG06_G12_SE_09",
       "Wilson is wont to emphasize the __________ of ants, how ants with full stomachs will regurgitate liquid food for those without, or how the old will fight so the young can survive.",
       ["beneficence","altruism","unpredictability","intelligence","fecundity","fertility"], ["A","B"]),
    se("HG06_G12_SE_10",
       "At first, most of the famous fairy tales seem so implausible and so irrelevant to contemporary life that their __________ is hard to understand.",
       ["universality","persistence","appeal","ephemerality","survival","transience"], ["B","E"]),
]

_p6 = ("During the Pleistocene epoch, several species of elephants isolated on islands underwent rapid dwarfing. This phenomenon was not "
       "necessarily confined to the Pleistocene, but may have occurred much earlier in the Southeastern Asian islands, although evidence is "
       "fragmentary. Several explanations are possible for this dwarfing. For example, islands often have not been colonized by large predators "
       "or are too small to hold viable predator populations. Once free from predation pressure, large body size is of little advantage to "
       "herbivores. Additionally, island habitats have limited food resources; a smaller body size and a need for fewer resources would thus be "
       "favored. Interestingly, the island rule is reversed for small mammals such as rodents, for which gigantism is favored under insular conditions.")
questions += [
    rc("HG06_SP6_RC_01", _p6,
       "The primary purpose of the passage is to",
       ["question the plausibility of one explanation sometimes offered for the dwarfing of certain species living on islands",
        "argue that dwarfing of certain species living on islands occurred prior to the Pleistocene",
        "cite evidence suggesting that dwarfing may have adverse consequences for some species living on islands",
        "present some possible explanations for the dwarfing of certain species living on islands",
        "contrast the effects of insular conditions on species with large body size and species with small body size"],
       "D"),
    rc("HG06_SP6_RC_02", _p6,
       "According to the passage, which of the following statements about body size in mammals is true?",
       ["A large body is unfavorable to mammalian species' survival under most conditions.",
        "A large body tends to benefit small mammals living on islands.",
        "For most herbivorous mammals, a large body size is easier to sustain in the absence of large predators.",
        "Under most conditions, a small body is less beneficial to herbivorous mammals than to nonherbivorous mammals.",
        "Among nonherbivorous mammals, a small body is more beneficial on an island than on a mainland."],
       "B"),
]

_cr6 = ("The Great Sphinx is a huge statue in Egypt that has a lion's body with a man's head. The face of the Sphinx has long been claimed "
        "to be that of pharaoh Khafre, who lived around 2600 B.C., but it cannot be: erosion patterns recently discovered on the lion's legs "
        "can only have been caused by heavy rains, and the Sahara has not had heavy rains in over 10,000 years.")
questions.append(
    rc("HG06_CR6_RC_01", _cr6,
       "Which of the following, if true, most seriously weakens the argument?",
       ["The face of the Sphinx bears a resemblance to the faces on certain stylized statues dating from both before and after the reign of Khafre.",
        "Other erosion patterns that appear on the body of the Sphinx are of a sort that could be caused by wind and sand alone.",
        "Other than the Sphinx, there are no surviving sculptures that have been claimed to portray the face of Khafre.",
        "In the last 10,000 years the climate of Egypt has been so dry that even rains that are not heavy have been extremely infrequent.",
        "The face of the Sphinx is small relative to the rest of the head, indicating that the face may have been recarved long after the Sphinx was built."],
       "E")
)

# ═══════════════════════════════════════════════════════════════════
# HGset #7  (Groups 13-14, Short Passage 7, Critical Reasoning 7)
# ═══════════════════════════════════════════════════════════════════

questions += [
    tc1("HG07_G13_TC_01",
        "My grandma has a strong belief in all things __________: she insists, for example, that the house in which she lived as a child was haunted.",
        ["clamorous","invidious","numinous","empirical","sonorous"], "C"),
    tc1("HG07_G13_TC_02",
        "Consolidating a memory is not instantaneous or even __________: every memory must be encoded and moved from short-term to long-term storage, and some of these memories are, for whatever reason, more vividly imprinted than others.",
        ["salutary","deliberate","sequential","momentary","inevitable"], "E"),
    tc2("HG07_G13_TC_03",
        "Many of the unusual behaviors attributed to crows—such as drinking coffee or presenting gifts to people who feed them—are based on (i) __________ and therefore fall into the category of (ii) __________ rather than science.",
        ["long-term observation","controlled experiments","secondhand testimony"],
        ["anecdote","speculation","hypothesis"],
        ["C","D"]),
    tc3("HG07_G13_TC_04",
        "The notion of film producers as the ogres of the movie business has proved an (i) __________ one, but according to The Producers by Tim Adler, it is not always warranted in reality. Attacking what he calls the 'auteur myth'—the idea of the director as the purveyor of art in an industry otherwise peopled with (ii) __________—he places at the heart of his book an image of the producer as the primary (iii) __________ force in the movie.",
        ["accurate","hypocritical","enduring"],
        ["visionaries","profit-mongers","innocents"],
        ["financial","inertial","creative"],
        ["C","E","I"]),
    tc3("HG07_G13_TC_05",
        "The (i) __________ nature of the candidate's comments is calculated. As a long-standing target of critics who regard him as a radical, he understands that he needs to be as (ii) __________ as possible if he is to overcome those critiques and appear as a (iii) __________ leader.",
        ["opprobrious","platitudinous","pugnacious"],
        ["innocuous","truculent","supercilious"],
        ["polarizing","cautious","conciliatory"],
        ["B","D","I"]),
    tc3("HG07_G13_TC_06",
        "Most psychologists have claimed that aesthetic emotions are genuine, but different in kind from non-aesthetic emotions. This, however, is (i) __________ rather than an empirical observation. On the other hand, Gombrich argues that emotional responses to art are (ii) __________; art triggers remembrances of previously experienced emotions. These debates have prompted Radford to argue that people experience real melancholy or joy in responding to art, but that these are (iii) __________ responses precisely because people know they are reacting to illusory stimuli.",
        ["a descriptive distinction","a body of profound knowledge","a valid evidence"],
        ["vivacious","synonymous","ersatz"],
        ["zealous","lugubrious","irrational"],
        ["A","F","I"]),
    se("HG07_G13_SE_07",
       "Members of the union's negotiating team insisted on several changes to the company's proposal before they would support it, making it clear that they would __________ no compromise.",
       ["disclose","reject","brook","tolerate","repudiate","weigh"], ["C","D"]),
    se("HG07_G13_SE_08",
       "Excessive focus on what might have been can cause in us feelings of restlessness and regret but some scientists are beginning to think that fancying an alternative reality might have __________ effects as well.",
       ["subtle","adverse","restorative","pleasurable","unfavorable","tonic"], ["C","F"]),
    se("HG07_G13_SE_09",
       "Apparent flaws in the sculptor's work have not __________ its respectful reception by most modern critics.",
       ["determined","controlled","undermined","prevented","overshadowed","precluded"], ["D","F"]),
    se("HG07_G13_SE_10",
       "Williamson had a fierce commitment to achieving an accord, spending enormous amounts of time trying to forge a consensus out of an often __________ assembly.",
       ["apathetic","fractious","restive","cynical","compliant","tractable"], ["B","C"]),
]

questions += [
    tc1("HG07_G14_TC_01",
        "In the solar system, collisions involving cosmic objects are among the most __________ processes shaping surfaces: images of many solar objects show a proliferation of impact craters formed throughout the past 4.5 billion years.",
        ["cataclysmic","pervasive","misleading","uncontrollable","random"], "B"),
    tc1("HG07_G14_TC_02",
        "Many creative photographers were delighted to find in instant photography a mode that encouraged them to stop viewing photography as __________ and start viewing it as something they could handle with spontaneity, even derision.",
        ["sacrosanct","ephemeral","malleable","egalitarian","autonomous"], "A"),
    tc2("HG07_G14_TC_03",
        "Recent scholarship has questioned the (i) __________ of tropical forests around the world; archaeologists have shown that the largest contiguous tract of what was thought to be virgin rain forest had been transformed into a cultural parkland, and many of the forest islands in West Africa are (ii) __________ as well.",
        ["diversity","naturalness","sustainability"],
        ["isolated","endangered","anthropogenic"],
        ["B","F"]),
    tc2("HG07_G14_TC_04",
        "The research found that in assessing others, many people hold an unconscious view that competence and warmth are (i) __________: when they perceive a person to be highly capable, they infer that he or she must have a tendency to be (ii) __________.",
        ["equally important","mutually reinforcing","inversely related"],
        ["ambitious","unfeeling","disingenuous"],
        ["C","E"]),
    tc2("HG07_G14_TC_05",
        "Mr. Stevens found that home schooling, far from representing (i) __________ philosophy, (ii) __________ some of the most widely accepted education ideas: that children should be treated as individuals, taught in small numbers, and given a measure of discretion over their own learning.",
        ["a benign","an orthodox","an anomalous"],
        ["overcomes","embodies","anticipates"],
        ["C","E"]),
    tc3("HG07_G14_TC_06",
        "Most capuchin monkey conflict involves such a (i) __________ repertoire of gestural and vocal signals that it is difficult for researchers to tease apart the meanings of the individual signals. This (ii) __________ is (iii) __________ by the fact that many signals seem to shift in meaning according to the context in which they are produced and the developmental stage of the individuals producing them.",
        ["precise","rich","straightforward"],
        ["problem","opportunity","oversight"],
        ["augmented","ameliorated","anticipated"],
        ["B","D","G"]),
    se("HG07_G14_SE_07",
       "Architects may be more extroverted and therefore the more __________ members of a bridge design team, but they are not always the most essential.",
       ["indispensable","conscientious","reliable","visible","valuable","salient"], ["D","F"]),
    se("HG07_G14_SE_08",
       "Although scientific progress leads to constant revision of ideas, one observation that has remained __________ over the years is that there are a lot of insects in the world: some 950,000 species have been identified.",
       ["robust","significant","strong","perplexing","confounding","obscure"], ["A","C"]),
    se("HG07_G14_SE_09",
       "Anne Carson's book Nox is, very deliberately, __________ literary object—the opposite of an e-reader, which is designed to vanish in your palm as you read on a train.",
       ["an evanescent","a cumbersome","an immutable","an unwieldy","an ephemeral","a flexible"], ["B","D"]),
    se("HG07_G14_SE_10",
       "One of the peculiarities of humans is that we irrationally gravitate to the predictable and avoid risk; whatever the reason for this __________, it is hardly a sound basis for dealing with complex, long-term problems.",
       ["eccentricity","predilection","vacillation","proclivity","wavering","cowardice"], ["B","D"]),
]

_p7 = ("In the early twentieth century, small magazines and the innovative graphics used on them created the face of the avant-garde. "
       "It was a look that signaled progressive ideas and unconventionality because it dispensed with the cardinal rule of graphic design: "
       "to take an idea and make it visually clear, concise, and instantly understood. Instead, graphics produced by avant-garde artists "
       "exclusively for the avant-garde were usually difficult to decipher, ambiguous, or nonsensical. This overturning of convention, "
       "this assailing of standard graphic and typographic formats, was part of a search for intellectual freedom. The impulse toward "
       "liberation enabled avant-guardists to see with fresh eyes untried possibilities for arranging and relating words and images on paper.")
questions += [
    rc("HG07_SP7_RC_01", _p7,
       "According to the passage, the primary purpose of conventional graphic design is to",
       ["render unpopular ideas palatable to a wider audience",
        "capture readers' attention with bold fonts",
        "communicate nonsensical notions to a wide public",
        "communicate ideas as efficiently and unambiguously as possible",
        "introduce previously unknown ideas to the general public"],
       "D"),
    rc("HG07_SP7_RC_02", _p7,
       "According to the passage, avant-garde artists of the early twentieth century created ambiguous or nonsensical graphics as part of an attempt to (select all that apply)",
       ["expand the potential for expression through visual art",
        "compete with advertisements for readers' attention",
        "encourage the expansion of small magazines"],
       ["A"], subtype="multi_answer"),
]

_cr7 = ("Cotton grass, which grows only in arctic regions, has been the only summertime source of protein available to caribou. Caribou "
        "that do not get adequate amounts of protein in the summer are unable to reproduce the following year. Rising average temperatures "
        "in arctic regions, however, are causing cotton grass to disappear. Therefore, if the warming trend continues, caribou are likely "
        "to become extinct.")
questions.append(
    rc("HG07_CR7_RC_01", _cr7,
       "Which of the following is an assumption on which the argument depends?",
       ["Cotton grass is the only one of the caribou's food sources that is becoming scarce as temperatures rise in arctic regions.",
        "Caribou that do not eat enough protein to reproduce do not live as long as caribou that do.",
        "The warming trend in arctic regions will not enable other plants capable of providing protein to caribou to grow there.",
        "The caribou is the only animal that depends on cotton grass as a major source of food.",
        "If the warming trend continues and cotton grass disappears from arctic regions, then cotton grass will be extinct."],
       "C")
)

# ═══════════════════════════════════════════════════════════════════
# HGset #8  (Groups 15-16, Short Passage 8, Critical Reasoning 8)
# ═══════════════════════════════════════════════════════════════════

questions += [
    tc1("HG08_G15_TC_01",
        "Some ethicists worry that a deeper understanding of the brain may be tantamount to __________: if we discover that free will is an illusion of neural circuitry, how will we hold people responsible for their actions?",
        ["vindication","proscription","ministration","valediction","exculpation"], "E"),
    tc1("HG08_G15_TC_02",
        "The stories in Yiyun Li's recent collection are distinctive particularly for the strong contrast between their emotional intensity and their consistently __________ tone.",
        ["affable","ebullient","measured","irascible","overwrought"], "C"),
    tc2("HG08_G15_TC_03",
        "Scholarly works on detective stories often begin with (i) __________, suggesting that there is something vaguely wrong with adults who spend their time reading such fiction and certainly something (ii) __________ those who devote energy to its analysis.",
        ["chronologies","apologies","synopses"],
        ["awry in","astute about","courageous about"],
        ["B","D"]),
    tc2("HG08_G15_TC_04",
        "So, perhaps the lesson is that rather than wanting their monarchy to (i) __________ its modernized Scandinavian counterparts, the British public cherishes it most when it is most (ii) __________.",
        ["commend","discount","emulate"],
        ["egalitarian","anachronistic","regal"],
        ["C","E"]),
    tc2("HG08_G15_TC_05",
        "He was never (i) __________; he was nothing if not (ii) __________, so he forbore for the present to declare his passion.",
        ["chivalrous","impetuous","thoughtful"],
        ["boorish","circumspect","spontaneous"],
        ["B","E"]),
    tc3("HG08_G15_TC_06",
        "Although political events in different countries were not (i) __________ in the nineteenth century, their interrelationship was (ii) __________ compared with the present, when interdependence has become far greater. (iii) __________ has ceased to be an option.",
        ["unconnected","trivial","simultaneous"],
        ["conditional","superficial","transparent"],
        ["Isolationism","Resilience","Idealism"],
        ["A","E","G"]),
    se("HG08_G15_SE_07",
       "Well organized and researched and including all significant discoveries and medical scientists, this history of Western medicine has justly been called __________.",
       ["encyclopedic","long-winded","exhaustive","rambling","overbearing","undiscriminating"], ["A","C"]),
    se("HG08_G15_SE_08",
       "Science is arguably a very high-minded pursuit, but that is not to say that all of its practitioners are __________, as numerous articles alleging overly generous pharmaceutical industry payments to medical researchers have tried to show.",
       ["conventional","clever","unimpeachable","ingenious","blameless","predictable"], ["C","E"]),
    se("HG08_G15_SE_09",
       "In a field of egotists, Bloomfield is __________, often praising her competitors and punctuating her correspondence with self-deprecating remarks.",
       ["unassuming","complimentary","acerbic","ingenuous","cutting","modest"], ["A","F"]),
    se("HG08_G15_SE_10",
       "Because its previously __________ beliefs had become core tenets of mainstream politics, the activist group disbanded; with no more skeptics to persuade, its purpose had evaporated.",
       ["arcane","seditious","quixotic","idealistic","popular","conventional"], ["C","D"]),
]

questions += [
    tc1("HG08_G16_TC_01",
        "Politicians who invoke the founders of the United States in support of their views seem to imply that the founders consistently concurred when in reality they were a highly __________ group of thinkers.",
        ["erudite","innovative","predictable","contentious","methodical"], "D"),
    tc1("HG08_G16_TC_02",
        "Of all her works, this play is the most dependent on the dramatic conventions of the author's day; it was both the least __________ of her plays and the most commercially successful.",
        ["experimental","popular","formulaic","lucrative","contemporary"], "A"),
    tc2("HG08_G16_TC_03",
        "One way to predict the effects of global climate change on an ecosystem is to extrapolate current trends into the future. A (i) __________ of this method is that its predictions (ii) __________ actual observation, but the method also makes the questionable assumption that the future will resemble the present.",
        ["virtue","drawback","peculiarity"],
        ["dispense with","derive from","improve upon"],
        ["A","E"]),
    tc3("HG08_G16_TC_04",
        "Just because, as a photographer, Friedlander (i) __________ places that most people consider ugly does not mean that he is out to prove they are beautiful. Instead, his work suggests that the photographer is obligated to (ii) __________ what we pass through day in and day out, regardless of (iii) __________.",
        ["tends to avoid","is harshly critical of","is interested in"],
        ["document","emulate","discredit"],
        ["authenticity","truthfulness","aesthetics"],
        ["C","D","I"]),
    tc3("HG08_G16_TC_05",
        "China's rapidly growing population is the main threat facing large carnivores in the People's Republic. Increasingly, policies aimed at limiting population growth have been (i) __________; nevertheless, the country's vast size means that human populations in areas where large carnivores still occur (ii) __________. This human pressure has (iii) __________ the south China tiger.",
        ["modified","deemphasized","implemented"],
        ["could start to decline","can grow unchecked","have stabilized"],
        ["celebrated","doomed","bypassed"],
        ["C","E","H"]),
    tc3("HG08_G16_TC_06",
        "Behavioral economists have come to believe that a (i) __________ of choices can be paralyzing. Studies of retirement plans show that the more investment choices a plan offers, the less likely people are to participate in it. It may follow, then, that a lack of flexibility in certain plans may actually be a (ii) __________. People reasonably (iii) __________ some advantages in exchange for peace of mind.",
        ["surfeit","reduction","stabilization"],
        ["virtue","conundrum","revelation"],
        ["foresee","forestall","forgo"],
        ["A","D","I"]),
    se("HG08_G16_SE_07",
       "It is hardly __________ the committee calls for: rudimentary competence would be an improvement on the current chaos.",
       ["accountability","faultlessness","disarray","loyalty","unrichness","perfection"], ["B","F"]),
    se("HG08_G16_SE_08",
       "Explorers could not build each other's knowledge if they could not trust the records of previous explorers; thus, exploration depended on the __________ of those who had gone before.",
       ["collegiality","endurance","exactitude","meticulousness","eminence","tenacity"], ["C","D"]),
    se("HG08_G16_SE_09",
       "Although its director __________ that the movie uses a documentary approach in portraying the famous sit-down strike, in practice its characters are heavily fictionalized and fall into familiar Hollywood types.",
       ["asserts","concedes","guarantees","disputes","grants","maintains"], ["A","F"]),
    se("HG08_G16_SE_10",
       "Joshua Gisemba Bagaka found that the pedagogical results of group projects and other engaged learning activities in Kenyan mathematics classrooms were __________; such activities, then, may not be the best way of improving mathematics education.",
       ["overstated","counterintuitive","mixed","discouraging","inconsistent","inexplicable"], ["C","E"]),
]

_p8 = ("According to Hill and Spicer, the term 'nation-state' is a misnomer, since the ideal model of a monolingual, culturally homogeneous "
       "state has never existed, not even among Europeans, who invented the nation-state concept and introduced it to the rest of the world. "
       "Modern European states, they argue, emerged after the Renaissance through the rise of nations (i.e., specific ethnic groups) to positions "
       "of political and economic dominance over a number of other ethnic groups within bounded political territories. The term 'nation-state', "
       "Hill and Spicer argue, obscures the internal cultural and linguistic diversity of states that could more accurately be called 'conquest states.' "
       "The resurgence of multiple ethnic groups within a single state, Hill says, is not 'potentially threatening to the sovereign jurisdiction of the "
       "state,' as Urban and Sherzer suggest; rather, the assertion of cultural differences threatens to reveal ethnocentric beliefs and practices "
       "upon which conquest states were historically founded.")
questions += [
    rc("HG08_SP8_RC_01", _p8,
       "The primary purpose of the passage is to",
       ["discuss issues relating to a form of political organization by raising doubts about the terminology used to refer to it",
        "trace changes in a form of political organization by examining the evolution of the terminology used to refer to it",
        "justify the continued use of an established term for an evolving form of political organization",
        "question the accuracy of a new term for a form of political organization",
        "compare two terms for a form of political organization"],
       "A"),
    rc("HG08_SP8_RC_02", _p8,
       "The author of the passage quotes Urban and Sherzer most probably in order to",
       ["introduce a discussion of the legal ramifications of expanding the nation-state concept",
        "summarize a claim about one possible effect of asserting cultural differences within a state",
        "shift the focus of discussion from internal threats that states face to external threats that they face",
        "point out similarities between the threats to states seen by Urban and Sherzer and those seen by Hill",
        "describe one way an ethnocentric practice has affected attempts to assert cultural differences within a state"],
       "B"),
    rc("HG08_SP8_RC_03", _p8,
       "According to the passage, Hill and Spicer define nations as which of the following?",
       ["coalitions of distinct ethnic groups with similar concerns",
        "Distinct ethnic groups",
        "Culturally homogeneous states",
        "Linguistically diverse states",
        "Territorially bounded states"],
       "B"),
]

_cr8 = ("In mountainous regions, the timberline is the highest altitude at which trees grow. In the Rocky Mountains, the current timberline "
        "is at the altitude above which growing season temperatures remain cooler than 10 degrees centigrade. Fossilized remains of trees that "
        "grew 10,000 years ago have been found 100 meters above the current Rocky Mountain timberline. Clearly, therefore, the climate of "
        "the Rocky Mountains is cooler now than it was 10,000 years ago.")
questions.append(
    rc("HG08_CR8_RC_01", _cr8,
       "Which of the following is an assumption on which the argument relies?",
       ["In the past 10,000 years, the only trees to have grown above today's timberline are the trees whose fossilized remains have been found.",
        "No trees grew 10,000 years ago at altitudes higher than the ones at which fossilized tree remains have been found.",
        "The fossils are not of species of trees that were able to tolerate cooler growing temperatures than the species that currently grow near the timberline.",
        "The Rocky Mountains have not eroded significantly over the past 10,000 years.",
        "The climate of the Rocky Mountains has never been significantly warmer than during the lifetime of the trees whose fossilized remains have been found."],
       "C")
)

# ── 기존 JSON에 추가 ──────────────────────────────────────────────────────────

data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
existing_ids = {q["id"] for q in data["verbal"]}
new_questions = [q for q in questions if q["id"] not in existing_ids]

data["verbal"].extend(new_questions)
DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"추가된 문제: {len(new_questions)}개")
print(f"전체 Verbal 문제: {len(data['verbal'])}개")

type_count = {}
for q in data["verbal"]:
    type_count[q["type"]] = type_count.get(q["type"], 0) + 1
for t, c in sorted(type_count.items()):
    print(f"  {t}: {c}")
