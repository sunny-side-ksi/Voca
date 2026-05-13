"""TC_0513 (Manhattan 5lb Chapter 3 Text Completions) → practice_questions.json 추가"""
import json
import string
from pathlib import Path

DATA_FILE = Path(__file__).parent / "gre_content" / "practice_questions.json"
L = list(string.ascii_uppercase)


def make_q(qid, stem, blank_defs, answer_words, diff="medium"):
    """blank_defs: [(label, [c1,c2,...]), ...]  answer_words: [correct_word_per_blank]"""
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

# ── Q1 ──────────────────────────────────────────────────────────────────────
make_q("TC0513_01",
    "In Europe, football, otherwise known as soccer, is the most popular sport by several orders of magnitude, whereas in the United States of America, fandom is fairly evenly __________ among a few different sports.",
    [("Blank", ["regarded","inspired","enjoyed","measured","apportioned"])],
    ["apportioned"]),

# ── Q2 ──────────────────────────────────────────────────────────────────────
make_q("TC0513_02",
    "The astrophysicist argues that our books and films about interstellar space travel are a form of mass __________, and that only a miracle on a scale heretofore unseen could allow a human being to voyage to even the closest star in another solar system.",
    [("Blank", ["innovation","delusion","dementia","catastrophe","hysteria"])],
    ["delusion"]),

# ── Q3 ──────────────────────────────────────────────────────────────────────
make_q("TC0513_03",
    "Peculiarly enough, Shakespeare has been often (i) __________ as the best English language playwright, and often (ii) __________ as a man lacking the education to write those plays.",
    [("Blank (i)",  ["crowned","stigmatized","castigated"]),
     ("Blank (ii)", ["demonized","dismissed","deified"])],
    ["crowned","dismissed"]),

# ── Q4 ──────────────────────────────────────────────────────────────────────
make_q("TC0513_04",
    "While far from the bane that some scholars have declared them to be, (i) __________ versions of novels and essays do indeed excise essential elements; students would have to supplement their reading with (ii) __________ sources to fully understand the intent of the original.",
    [("Blank (i)",  ["annotated","abridged","antedated"]),
     ("Blank (ii)", ["complementary","complimentary","compelling"])],
    ["abridged","complementary"]),

# ── Q5 ──────────────────────────────────────────────────────────────────────
make_q("TC0513_05",
    "Even the __________ and alluring charms of Paris were not sufficient to cure the young expatriate of his yearning for the simple and quaint charms of his rural American home.",
    [("Blank", ["lascivious","sophisticated","foreign","alien","alienating"])],
    ["sophisticated"]),

# ── Q6 ──────────────────────────────────────────────────────────────────────
make_q("TC0513_06",
    "The fact that the average life expectancy ten thousand years ago was so much shorter than it is now is often (i) __________ as evidence supporting the notion that the world always improves with time. However, if you (ii) __________ for the fact that most children in that epoch died in childbirth, life expectancy for those who survived birth was nearly the same then as it is now.",
    [("Blank (i)",  ["cited","disregarded","embodied"]),
     ("Blank (ii)", ["prepare","read","correct"])],
    ["cited","correct"]),

# ── Q7 ──────────────────────────────────────────────────────────────────────
make_q("TC0513_07",
    "On an aptitude test in 1986, an argument posited that the possibility of conducting banking transactions from home was as likely as flying cars, an argument that sounds __________ today, when such transactions are commonplace.",
    [("Blank", ["prescient","preternatural","preordained","preposterous","pithy"])],
    ["preposterous"]),

# ── Q8 ──────────────────────────────────────────────────────────────────────
make_q("TC0513_08",
    "The widespread tendency to __________ retired political leaders who were successful stems from an arguably primal human need to venerate both men and gods.",
    [("Blank", ["castigate","remember","lionize","appreciate","indemnify"])],
    ["lionize"]),

# ── Q9 ──────────────────────────────────────────────────────────────────────
make_q("TC0513_09",
    "Academic work can be as taxing as manual labor. The misconception that (i) __________ work strains the mind less than physical work strains the body has been proven wrong by scientific investigation as well as by anecdotal evidence. It is simply not true that the (ii) __________ musings of a mathematician are necessarily easier than the physical labor of, say, a carpenter.",
    [("Blank (i)",  ["cerebral","intense","actuarial"]),
     ("Blank (ii)", ["quotidian","extraordinary","intellectual"])],
    ["cerebral","intellectual"]),

# ── Q10 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_10",
    "Known for her humorous but acerbic wit, the fashion doyenne commented, in her usual, simultaneously (i) __________ and (ii) __________ manner, that in Los Angeles, 'the women dressed like men and the men dressed like boys.'",
    [("Blank (i)",  ["slanderous","amusing","serious"]),
     ("Blank (ii)", ["considerate","hysterical","caustic"])],
    ["amusing","caustic"]),

# ── Q11 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_11",
    "Every generation is accused of slacking by the preceding ones, before in turn calling its own progeny lackadaisical; such is the __________ of life.",
    [("Blank", ["vicissitude","irony","circle","serendipity","comedy"])],
    ["circle"]),

# ── Q12 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_12",
    "Although retired, the professor takes pains to remain __________ the latest developments in her field.",
    [("Blank", ["akimbo to","abreast of","obtuse to","subservient to","askance to"])],
    ["abreast of"]),

# ── Q13 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_13",
    "She was not the only (i) __________ of the long-proposed legislation, but she was the (ii) __________ who finally got the bill onto the legislative agenda.",
    [("Blank (i)",  ["apologist","critic","proponent"]),
     ("Blank (ii)", ["catalyst","mercenary","lackey"])],
    ["proponent","catalyst"]),

# ── Q14 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_14",
    "Jeremy was not one to (i) __________ his success, let alone talk much at all, so his family was shocked when they finally discovered that their (ii) __________ son was a Rhodes Scholar.",
    [("Blank (i)",  ["demarcate","whitewash","trumpet"]),
     ("Blank (ii)", ["improvident","taciturn","dissolute"])],
    ["trumpet","taciturn"]),

# ── Q15 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_15",
    "In his youth, Oscar Wilde catapulted to sudden fame both because of and despite his (i) __________ witticisms; however, the cutting remarks that won him renown also led to his financial and physical ruin, and he died (ii) __________ and sickly in a shabby Parisian hotel.",
    [("Blank (i)",  ["innovative","acerbic","inimical"]),
     ("Blank (ii)", ["pallid","aghast","impecunious"])],
    ["acerbic","impecunious"]),

# ── Q16 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_16",
    "Hursthouse, (i) __________ virtue ethicists in general, argues that ethics is properly neither situational nor utilitarian and that one ought to seek out virtue and emulate it rather than base one's judgments on subjective concerns or a (ii) __________ weighing of pain and pleasure likely to result from a given action; critics, of course, tend to (iii) __________ that Hursthouse and other virtue ethicists who seek to define virtue merely seek to enshrine their own prejudices under the guise of theory.",
    [("Blank (i)",   ["enigmatic to","breaking away from","emblematic of"]),
     ("Blank (ii)",  ["pragmatic","quixotic","grandiloquent"]),
     ("Blank (iii)", ["posit","deny","cajole"])],
    ["emblematic of","pragmatic","posit"]),

# ── Q17 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_17",
    "The film was (i) __________ (ii) __________ by critics; rightfully, not a single reviewer had any positive thing to say about it.",
    [("Blank (i)",  ["warily","mendaciously","roundly"]),
     ("Blank (ii)", ["lauded","panned","venerated"])],
    ["roundly","panned"]),

# ── Q18 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_18",
    "The distinction between architecture and the engineering professions that it resembles is that the former must consider __________ as well as functionality, as clients often base their decisions more on the beauty of the project than its practicality.",
    [("Blank", ["insouciance","utility","price","aesthetics","profundity"])],
    ["aesthetics"]),

# ── Q19 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_19",
    "Once considered able to only __________ emulate actions without understanding the action's deeper significance, bearded dragons have recently been observed copying non-instinctive actions of other bearded dragons, prompting scientists to question whether other reptiles might also be capable of genuine imitation.",
    [("Blank", ["attentively","insensibly","listlessly","actively","consciously"])],
    ["insensibly"]),

# ── Q20 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_20",
    "December's earthquake was but a __________ to a terrible year for a small island nation recently wracked by civil strife and devastating tropical storms.",
    [("Blank", ["prologue","catharsis","coda","homily","rampage"])],
    ["coda"]),

# ── Q21 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_21",
    "Although they had never met, the two writers felt they were of one mind, each (i) __________ anticipating the contents of the other's letters; never had two intellectuals been more (ii) __________.",
    [("Blank (i)",  ["ominously","anachronistically","presciently"]),
     ("Blank (ii)", ["providential","shrewd","simpatico"])],
    ["presciently","simpatico"]),

# ── Q22 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_22",
    "After many years of war and bloodshed, some became __________ suffering, casting a blind eye to scenes of misery around them.",
    [("Blank", ["inured to","exempted from","dominant over","effusive towards","maudlin over"])],
    ["inured to"]),

# ── Q23 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_23",
    "After a brief initial struggle over power, the group elected a leader and __________ into a surprisingly harmonious team.",
    [("Blank", ["fractured","syncopated","coalesced","agglomerated","amortized"])],
    ["coalesced"]),

# ── Q24 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_24",
    "The highly anticipated finale of the TV series was divisive: newcomers to the show found the fast-paced action enjoyable, while long-time fans __________ the storyline unfinished.",
    [("Blank", ["appreciated","generated","examined","considered","secured"])],
    ["considered"]),

# ── Q25 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_25",
    "The author was far from (i) __________ the novel. While most of the book was already written, he knew that it would take innumerable hours to review and edit. This was going to be (ii) __________, not only because of the book's length, but also because of the convoluted plot.",
    [("Blank (i)",  ["finishing","inscribing","rejecting"]),
     ("Blank (ii)", ["hardy","trying","redundant"])],
    ["finishing","trying"]),

# ── Q26 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_26",
    "During his sales pitch, the car salesman attempted to __________ the young couple into purchasing the luxury automobile, despite the pair's obvious indifference to his flattery.",
    [("Blank", ["support","inveigle","deliberate","marginalize","hector"])],
    ["inveigle"]),

# ── Q27 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_27",
    "Just as reminiscences of a childhood spent in rural Mexico color the poet's work, so too does the experience of war __________ her poetry.",
    [("Blank", ["inform","mimic","invalidate","defer","presage"])],
    ["inform"]),

# ── Q28 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_28",
    "The peanut is often (i) __________ referred to as a nut; (ii) __________ to such people, it is actually a legume.",
    [("Blank (i)",  ["archaically","erroneously","deftly"]),
     ("Blank (ii)", ["unbeknownst","abhorrent","consanguineous"])],
    ["erroneously","unbeknownst"]),

# ── Q29 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_29",
    "The (i) __________ child approached the diving board; (ii) __________ water in the first place, he found the prospect of jumping into it from some height even more frightening.",
    [("Blank (i)",  ["tremulous","coltish","cumbersome"]),
     ("Blank (ii)", ["beguiled by","chary of","repulsed by"])],
    ["tremulous","chary of"]),

# ── Q30 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_30",
    "Soldier ants are wingless, sterile females that guard the colony and supply it with food, thus acting as both (i) __________ and laborers as the (ii) __________ queen produces enough (iii) __________ to continually populate the colony.",
    [("Blank (i)",   ["sentries","sages","sycophants"]),
     ("Blank (ii)",  ["fecund","efficacious","imperious"]),
     ("Blank (iii)", ["forebears","progeny","harbingers"])],
    ["sentries","fecund","progeny"]),

# ── Q31 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_31",
    "The Paris Commune was a government that ruled France for about two months in 1871; despite its (i) __________ reign, it was at the time (ii) __________ as a sign of the emergence of a powerful working class.",
    [("Blank (i)",  ["equivocal","ephemeral","omnipotent"]),
     ("Blank (ii)", ["discounted","recanted","heralded"])],
    ["ephemeral","heralded"]),

# ── Q32 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_32",
    "While taller wind turbines would allow more areas of the country to provide cost-effective alternative energy, there are several (i) __________ that engineers are currently facing while trying to build such turbines. Taller towers necessitate (ii) __________ bases, requiring the current width to be nearly doubled. This leads to (iii) __________ issue: these wider sections would be too large to travel on modern highways, meaning that the taller turbines would need to be constructed at the location where they are to eventually stand.",
    [("Blank (i)",   ["flaws","supplements","complications"]),
     ("Blank (ii)",  ["equitable","unobtrusive","stouter"]),
     ("Blank (iii)", ["a concomitant","a theoretical","an objective"])],
    ["complications","stouter","a concomitant"]),

# ── Q33 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_33",
    "During the prolonged and elaborate farewell tour, no one thought the plaudits heaped upon him were __________, since his heroics were well documented and admired by all.",
    [("Blank", ["obsequious","derivative","deserved","vestigial","antiquated"])],
    ["obsequious"]),

# ── Q34 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_34",
    "He has such a pleasingly (i) __________ personality that it's hard to be bothered by the (ii) __________ in his past.",
    [("Blank (i)",  ["sanguine","high-handed","evanescent"]),
     ("Blank (ii)", ["peccadilloes","incendiaries","achievements"])],
    ["sanguine","peccadilloes"]),

# ── Q35 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_35",
    "The Tasmanian devil is not considered (i) __________, since only a few of its confrontations with humans have been (ii) __________.",
    [("Blank (i)",  ["adverse","menacing","unpredictable"]),
     ("Blank (ii)", ["premature","quixotic","unprovoked"])],
    ["menacing","unprovoked"]),

# ── Q36 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_36",
    "The (i) __________ young employee was soon (ii) __________ for making a serious mistake that cost the company thousands of dollars.",
    [("Blank (i)",  ["banal","sagacious","verdant"]),
     ("Blank (ii)", ["enamored","castigated","deposed"])],
    ["verdant","castigated"]),

# ── Q37 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_37",
    "The beauty pageant contestant told the judges she wanted world peace, but her suggestion to bring about world peace was __________—apparently, she naively thinks everyone could just be told to 'love one another' and all the world's disagreements would fade away.",
    [("Blank", ["convoluted","facile","impeccable","amicable","dulcet"])],
    ["facile"]),

# ── Q38 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_38",
    "In front of her parents, adults euphemistically referred to the overly talkative young girl as precocious, though they privately found her to be __________.",
    [("Blank", ["garrulous","skittish","solicitous","endearing","naive"])],
    ["garrulous"]),

# ── Q39 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_39",
    "While the author's first collection of short stories presented a (i) __________ hodgepodge of voices, the second collection presents a remarkably (ii) __________ set of tales presented by a (iii) __________ narrator.",
    [("Blank (i)",   ["motley","variable","homogeneous"]),
     ("Blank (ii)",  ["insightful","even","facetious"]),
     ("Blank (iii)", ["lonely","disingenuous","sole"])],
    ["motley","even","sole"]),

# ── Q40 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_40",
    "In contrast to environmental economics, an older field that concerns itself with the monetary valuation of natural resources, the emergent field of ecological economics positions the human economy as a subsystem of natural ecologies, thus __________ environmental economists' subordination of the natural world.",
    [("Blank", ["circumscribing","corroborating","refuting","ameliorating","reversing"])],
    ["reversing"]),

# ── Q41 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_41",
    "Today's highly partisan political environment is far from __________; not so long ago, ideological opponents were still able to set aside differences and work across party lines, as is typically necessary to pass productive legislation.",
    [("Blank", ["civil","immutable","polemical","efficacious","enjoyable"])],
    ["efficacious"]),

# ── Q42 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_42",
    "The virtual (i) __________ of John F. Kennedy focuses on his presidential achievements, legend, and assassination; similarly, during his candidacy, verbal and written (ii) __________ were laid at the altar of his wartime exploits.",
    [("Blank (i)",  ["deification","excoriation","praise"]),
     ("Blank (ii)", ["calumnies","garlands","obloquies"])],
    ["deification","garlands"]),

# ── Q43 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_43",
    "For centuries, commercial portrait painters have employed a bifurcated aesthetic: like other artists, they strive to represent the truth that gives their works life, but commerce dictates that they simultaneously employ subtle __________ that make the likeness more attractive than the sitter.",
    [("Blank", ["palettes","aesthetics","artifacts","artifices","sentiments"])],
    ["artifices"]),

# ── Q44 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_44",
    "Dogmatic professors often alienate their classes because they fail to realize that their __________ enervates rather than inspires students.",
    [("Blank", ["wisdom","pedantry","parsimony","pulchritude","wit"])],
    ["pedantry"]),

# ── Q45 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_45",
    "General McClellan focused so intently on the petty, logistical details of the upcoming campaign that Lincoln felt that said attention to __________, however necessary, had superseded more lofty goals.",
    [("Blank", ["irrelevancies","tactics","minutiae","strategy","peccadilloes"])],
    ["minutiae"]),

# ── Q46 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_46",
    "Jimmy Stewart, the actor, spoke with an (i) __________ that (ii) __________ audiences; through hesitancy and understatement, he was at least as captivating as his flamboyant peers.",
    [("Blank (i)",  ["awkward lisp","overwhelming passion","appealing shyness"]),
     ("Blank (ii)", ["enthralled","repelled","amused"])],
    ["appealing shyness","enthralled"]),

# ── Q47 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_47",
    "Given the (i) __________ of the book, the critical reception was surprisingly (ii) __________; reviewers who usually pounce on the slightest orthodoxy met the text with unabashed approbation.",
    [("Blank (i)",  ["ingenuity","tortuousness","conventionality"]),
     ("Blank (ii)", ["tepid","laudatory","deprecating"])],
    ["conventionality","laudatory"]),

# ── Q48 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_48",
    "Ironically, the commentator who so roundly condemned personal (i) __________ was (ii) __________ to the point of bankruptcy—he himself was a reflection of an aspect of the ills that, in other areas, he railed against.",
    [("Blank (i)",  ["indolence","probity","dissipation"]),
     ("Blank (ii)", ["profligate","antediluvian","ascetic"])],
    ["dissipation","profligate"]),

# ── Q49 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_49",
    "For all the student's meticulous preparation, he received __________ grade on his final exam.",
    [("Blank", ["a passable","a deplorable","an exacting","a surprising","an outstanding"])],
    ["a deplorable"]),

# ── Q50 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_50",
    "Just as ancient Greek culture in some ways provided the Romans with a model, the remnants of Roman culture __________ the development of medieval European mores.",
    [("Blank", ["duplicated","curbed","foresaw","informed","hindered"])],
    ["informed"]),

# ── Q51 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_51",
    "As an evolutionary adaptation, cats have developed a mechanism whereby their heads are measuring devices, as their bodies can fit through any space that their heads can, and this physiology is a safeguard that __________ their success as a species.",
    [("Blank", ["reproduces","ensures","enhances","mitigates","inundates"])],
    ["enhances"]),

# ── Q52 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_52",
    "Far from the (i) __________ novice that he made himself out to be, the new teacher was in fact quite (ii) __________: within a week of arrival, he understood the school's byzantine power structures and was using the dysfunctional administration to his advantage.",
    [("Blank (i)",  ["cunning","guileless","capricious"]),
     ("Blank (ii)", ["canny","unseemly","desultory"])],
    ["guileless","canny"]),

# ── Q53 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_53",
    "Since there are significant (i) __________ in the flawed methodologies of the studies upon which it is based, the meta-analysis is anything but (ii) __________.",
    [("Blank (i)",  ["irregularities","subtleties","consistencies"]),
     ("Blank (ii)", ["unreliable","intelligible","credible"])],
    ["irregularities","credible"]),

# ── Q54 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_54",
    "Crane Brinton argued that the middle phases of revolutions are especially (i) __________ because the unleashed force of social momentum transfers power inexorably from more stable (if oppressive) forces to less temperate ones. Yet, he then goes on to say that the excesses (ii) __________ and a more peaceful period ensues.",
    [("Blank (i)",  ["brusque","berserk","pacific"]),
     ("Blank (ii)", ["metastasize","grow","recede"])],
    ["berserk","recede"]),

# ── Q55 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_55",
    "The Donner party made a __________ choice to try to cross the Sierra Nevada too late in the season, and they paid dearly for that dangerous decision.",
    [("Blank", ["prudent","parlous","suicidal","semiotic","providential"])],
    ["parlous"]),

# ── Q56 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_56",
    "The engineer is not interested in developing products to meet market needs; her work is known for its technical brilliance much more than for its __________ potential.",
    [("Blank", ["scientific","ergonomic","commercial","academic","revolutionary"])],
    ["commercial"]),

# ── Q57 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_57",
    "Frederick the Great of Prussia was known for his (i) __________ under fire during his military victories; however, when confronting issues of domestic policy, this equilibrium sometimes failed him. He was often (ii) __________ with his ministers, who never knew when they might be subjected to one of his tirades.",
    [("Blank (i)",  ["intrepidity","cruelty","sangfroid"]),
     ("Blank (ii)", ["fascist","mercurial","vainglorious"])],
    ["sangfroid","mercurial"]),

# ── Q58 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_58",
    "In her opening remarks, the school's director empathized with the apparent (i) __________ of taking disciplinary action in the classroom; on the one hand, teachers can ill afford to (ii) __________ indisputably disruptive behaviors, while on the other, overly strict administration can actually foster such behaviors.",
    [("Blank (i)",  ["necessity","entreaty","paradox"]),
     ("Blank (ii)", ["fabricate","brook","mitigate"])],
    ["paradox","brook"]),

# ── Q59 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_59",
    "The library wing was first conceived merely as (i) __________ to address the problem of book overstock until a more permanent solution could be found. Ironically, it was the flimsy nature of the wing itself that attracted such architectural interest and ultimately led to its canonization as a (ii) __________ of its kind. Now a statute exists to protect this originally transient structure in (iii) __________.",
    [("Blank (i)",   ["a stopgap","an ornament","a modicum"]),
     ("Blank (ii)",  ["paragon","nadir","catalyst"]),
     ("Blank (iii)", ["consecration","chronology","perpetuity"])],
    ["a stopgap","paragon","perpetuity"]),

# ── Q60 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_60",
    "Though the negotiation was initially expected to proceed smoothly, it soon became apparent that any semblance of (i) __________ between the parties was disingenuous or, at best, a superficial adherence to certain (ii) __________.",
    [("Blank (i)",  ["duplicity","amity","solace"]),
     ("Blank (ii)", ["mores","truisms","plaudits"])],
    ["amity","mores"]),

# ── Q61 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_61",
    "Unable to eschew her well-known tendency toward (i) __________, the speaker effectively turned a five-minute policy brief into an hour-long (ii) __________ on the history of the region.",
    [("Blank (i)",  ["terseness","precision","elaboration"]),
     ("Blank (ii)", ["distension","expatiation","repertory"])],
    ["elaboration","expatiation"]),

# ── Q62 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_62",
    "The senator's __________ upbringing seemingly had no effect on his policy: he vociferously championed economic, political, and even cultural isolationism.",
    [("Blank", ["cosmopolitan","bucolic","liberal","tendentious","opulent"])],
    ["cosmopolitan"]),

# ── Q63 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_63",
    "The plan, if it can be called that, has been more of (i) __________ vision than a concrete proposal; like many similarly (ii) __________ ideas, it is unlikely to ever come to fruition.",
    [("Blank (i)",  ["an oppositional","a protean","a martial"]),
     ("Blank (ii)", ["quixotic","pragmatic","unorthodox"])],
    ["a protean","quixotic"]),

# ── Q64 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_64",
    "It was a fact that the region was both quiet and rural, but what the typically impoverished residents considered (i) __________ refuge was considered by the well-heeled visitors to be an intolerable (ii) __________, and its residents' lifestyles unpleasantly (iii) __________.",
    [("Blank (i)",   ["a parochial","an arcadian","a squalid"]),
     ("Blank (ii)",  ["asylum","utopia","hinterland"]),
     ("Blank (iii)", ["tony","spartan","rational"])],
    ["an arcadian","hinterland","spartan"]),

# ── Q65 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_65",
    "Though many readers assumed that the (i) __________ depicted in her stories reflected the author's own lifestyle, in reality she was more prudish than (ii) __________.",
    [("Blank (i)",  ["dissent","propriety","debauchery"]),
     ("Blank (ii)", ["licentious","moralizing","perspicacious"])],
    ["debauchery","licentious"]),

# ── Q66 ─────────────────────────────────────────────────────────────────────
make_q("TC0513_66",
    "The club had been all male up until 1963, when it began to admit women, who now make up more of the membership: hence, the female club president was both annoyed and amused at an elderly male member's (i) __________ suggestion that women be shuffled off to (ii) __________ organization where they could play bridge and drink tea without having to worry about serious issues.",
    [("Blank (i)",  ["regressive","rustic","prudish"]),
     ("Blank (ii)", ["an incendiary","an auxiliary","a hierarchical"])],
    ["regressive","an auxiliary"]),

]

# ── Write to JSON ─────────────────────────────────────────────────────────────
with open(DATA_FILE, encoding="utf-8") as f:
    data = json.load(f)

existing_ids = {q["id"] for q in data["verbal"]}
added = [q for q in questions if q["id"] not in existing_ids]
skipped = [q for q in questions if q["id"] in existing_ids]

# 정답 매핑 실패한 문제 체크
failed = [q for q in added if len(q["correct"]) != len(q["blanks"])]
if failed:
    print(f"WARNING: answer mapping failed ({len(failed)}):")
    for q in failed:
        print(f"   {q['id']}: blanks={len(q['blanks'])}, correct={q['correct']}")

valid = [q for q in added if len(q["correct"]) == len(q["blanks"])]
data["verbal"].extend(valid)

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added: {len(valid)}  |  Skipped(dup): {len(skipped)}  |  Failed: {len(failed)}")
print(f"Total verbal: {len(data['verbal'])}")
