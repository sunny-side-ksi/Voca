"""TCSE v30 volume2 verbal questions → practice_questions.json 추가"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "gre_content" / "practice_questions.json"

def tc1(qid, stem, choices, correct_letter, diff="medium"):
    labels = ["A","B","C","D","E"]
    ch = {labels[i]: choices[i] for i in range(len(choices))}
    return {"id": qid, "section": "verbal", "type": "text_completion",
            "subtype": "single_blank", "difficulty": diff, "set": None,
            "passage": None, "stem": stem,
            "blanks": [{"label": "Blank", "choices": ch}],
            "correct": [correct_letter], "explanation": "", "source": "TCSE_v30_v2"}

def tc2(qid, stem, b1, b2, correct, diff="medium"):
    import string; L = list(string.ascii_uppercase)
    blanks = [{"label": "Blank (i)",  "choices": {L[i]: b1[i] for i in range(len(b1))}},
              {"label": "Blank (ii)", "choices": {L[3+i]: b2[i] for i in range(len(b2))}}]
    return {"id": qid, "section": "verbal", "type": "text_completion",
            "subtype": "double_blank", "difficulty": diff, "set": None,
            "passage": None, "stem": stem, "blanks": blanks,
            "correct": correct, "explanation": "", "source": "TCSE_v30_v2"}

def tc3(qid, stem, b1, b2, b3, correct, diff="medium"):
    import string; L = list(string.ascii_uppercase)
    blanks = [{"label": "Blank (i)",   "choices": {L[i]: b1[i] for i in range(len(b1))}},
              {"label": "Blank (ii)",  "choices": {L[3+i]: b2[i] for i in range(len(b2))}},
              {"label": "Blank (iii)", "choices": {L[6+i]: b3[i] for i in range(len(b3))}}]
    return {"id": qid, "section": "verbal", "type": "text_completion",
            "subtype": "triple_blank", "difficulty": diff, "set": None,
            "passage": None, "stem": stem, "blanks": blanks,
            "correct": correct, "explanation": "", "source": "TCSE_v30_v2"}

def se(qid, stem, choices6, correct2, diff="medium"):
    labels = ["A","B","C","D","E","F"]
    ch = {labels[i]: choices6[i] for i in range(len(choices6))}
    return {"id": qid, "section": "verbal", "type": "sentence_equivalence",
            "subtype": "sentence_equivalence", "difficulty": diff, "set": None,
            "passage": None, "stem": stem,
            "blanks": [{"label": "Blank", "choices": ch}],
            "correct": sorted(correct2), "explanation": "", "source": "TCSE_v30_v2"}

questions = []

# ═══════════════════════════════════════════════════════════
# Part I  Group 81 (TCSE 853–863)
# ═══════════════════════════════════════════════════════════
questions.append(tc2("TCSE853",
    "If all stars are fiery gas balls like our own sun, and if the principle that the situation of our own solar system is not (i)__________ is (ii)__________, then one might think that many other stars should be surrounded by a retinue of planets and moons.",
    ["obvious","permanent","special"],
    ["true","redundant","tested"],
    ["C","D"]))

questions.append(se("TCSE854",
    "As market forces penetrate firms and bid up the value of attributes of labor that are more measurable than is the knowledge born of experience, it can be expected that trends in wages will not __________ those whose main value lies in such experiential knowledge.",
    ["favor","aid","affect","forsake","betray","differentiate"],
    ["A","B"]))

questions.append(tc3("TCSE855",
    "The fall of the monarchical order in 1918 produced a score of fragile successor states in Eastern Europe that (i)__________ ethnic discontent and revanchism. This (ii)__________, when fused with their inherent feebleness, make for power voids and political (iii)__________.",
    ["kept down","overshadowed","simmered with"],
    ["cosmopolitanism","hierarchy","volatility"],
    ["cures","fluidities","redundancies"],
    ["C","F","H"]))

questions.append(se("TCSE856",
    "Fedigan argues that, in actuality, ethologists who claim to __________ anthropomorphism often end up simply substituting one set of anthropomorphic terms for another.",
    ["eschew","defend","support","appreciate","denounce","avoid"],
    ["A","F"]))

questions.append(tc2("TCSE857",
    "Except in times of (i)__________, we would scarcely allow public officials to declare states of emergency that replace some normal rules with those more (ii)__________ to extraordinary circumstances.",
    ["serenity","calamity","debate"],
    ["germane","indifferent","inimical"],
    ["B","D"]))

questions.append(se("TCSE858",
    "If animal parents were judged by human standards, the cuckoo would be one of nature's more __________ creatures, blithely laying its eggs in the nests of other birds, and leaving the incubating and nurturing to them.",
    ["ineffective","mettlesome","irresponsible","lackluster","industrious","feckless"],
    ["C","F"]))

questions.append(tc2("TCSE859",
    "Politicians and pollsters alike warn that the outcome of a presidential race remains (i)__________ until Election Day itself, and many races depend on factors that run from bad weather (ii)__________ voter turnout to last-minute scandals.",
    ["unlikely","fluid","predetermined"],
    ["decreasing","affecting","consolidating"],
    ["B","E"]))

questions.append(tc2("TCSE860",
    "Though the play crackles with humor, the dialogue is less (i)__________ when it comes to the drama's emotional core. There the players tend to spell out their emotions in (ii)__________ aphorisms, and repeat them as necessary.",
    ["adroit","ambiguous","transparent"],
    ["shrewd","jejune","riotous"],
    ["A","E"]))

questions.append(se("TCSE861",
    "Although it initially seemed that the ideological gap between them was insurmountable—he believed in __________ while she believed in accumulating wealth, he in sensitivity towards others while she in self-interest—the marriage ultimately lasted 52 years until his death.",
    ["largess","avarice","empathy","parsimony","cupidity","philanthropy"],
    ["A","F"]))

questions.append(tc2("TCSE862",
    "The insecticide proved (i)__________; by killing the weak adults of a species, it assured that the strong ones would mate among themselves and produce offspring still more (ii)__________ to its effects.",
    ["cruel","feasible","counterproductive"],
    ["resistant","susceptible","vulnerable"],
    ["C","D"]))

questions.append(se("TCSE863",
    "If Wilson's article style changed overtime, it was in the wrong retrograde direction, __________ experimentation and inclining toward works that seemed hobbled by a fear of risk.",
    ["shunning","overemphasizing","aggrandizing","eschewing","mocking","belaboring"],
    ["A","D"]))

# ═══════════════════════════════════════════════════════════
# Group 82 (TCSE 864–874)
# ═══════════════════════════════════════════════════════════
questions.append(se("TCSE864",
    "Films that critics have slumbered through rarely generate industry excitement, even though the critics' _________ reception may be less the fault of the movie than of its unfortunate time slot near a fatiguing film festival's conclusion.",
    ["somnolent","impartial","lethargic","laconic","befuddled","evenhanded"],
    ["A","C"]))

questions.append(tc3("TCSE865",
    "The research on otters' environmental requirements is surprisingly (i)________. One reason for this has to do with the estimation of how much they use different areas. Doing so may be (ii)________ in some kinds of terrain, such as Shetland where the Eurasian otters are active in daytime and have clear individual markings. There it is possible to identify the individuals over stretches of coast of a few kilometers and to see what kinds of coast they use. However, the field conditions are (iii)________.",
    ["straight-forward","controversial","deceptive"],
    ["quite problematic","relatively simple","difficult"],
    ["routine","exceptional","largely unnecessary"],
    ["A","E","H"]))

questions.append(se("TCSE866",
    "The physics graveyard is strewn with the skeletons of failed theories, unexplained effects, and anomalous particles that briefly ________ the research spotlight, then rapidly fade from view.",
    ["douse","intensify","perpetuate","capture","extinguish","secure"],
    ["D","F"]))

questions.append(tc2("TCSE867",
    "Even though the idea that medical research should be rigorously objective is (i)________ one in the medical community, the editors of medical journals often display a disquieting (ii)________  when it comes to articles submitted by researchers who accept money from the makers of the products they evaluate in their research; editors rarely ask whether that research is truly disinterested.",
    ["a neglected","an uncontroversial","an unproductive"],
    ["capriciousness","credulity","stringency"],
    ["B","E"]))

questions.append(tc1("TCSE868",
    "My grandma has a strong belief in all things ________: she insists, for example, that the house in which she lived as a child was haunted.",
    ["clamorous","invidious","numinous","empirical","sonorous"],
    "C"))

questions.append(se("TCSE869",
    "What makes the precisely oriented flight of a honeybee swarm to its new home so ________ is that only a small percentage of its members know the swarm travel route and final destination.",
    ["exact","unpredictable","amazing","erratic","reliable","wondrous"],
    ["C","F"]))

questions.append(tc1("TCSE870",
    "Although New York exhilarated him, even at first Leger's reaction to it was not ________: he was initially bothered by its stunning verticality.",
    ["unspontaneous","unintentional","unqualified","unhopeful","uninterested"],
    "C"))

questions.append(se("TCSE871",
    "In establishing that the dust she had observed constitutes two percent of the mass in the quadrant, the astronomer showed that the dust's extreme visual prominence ________ its relatively minor contribution to the total mass of the region.",
    ["belies","masks","highlights","nullifies","disproves","accentuates"],
    ["A","B"]))

questions.append(se("TCSE872",
    "When Kim Dae Jung was elected South Korea's president in December 1997, he was thought to be of a(an) ________, but nevertheless the right man for the time and the job. Mr Kim had campaigned unremittingly for democracy, even though his efforts had earned him a spell in jail and an attempt on his life by his own government.",
    ["authority","expert","maverick","unknown","nonconformist","dilettante"],
    ["C","E"]))

questions.append(tc1("TCSE873",
    "Some ethicists worry that a deeper understanding of the brain may be tantamount to _______: if we discover that free will is an illusion of neural circuitry, how will we hold people responsible for their action?",
    ["vindication","proscription","ministration","valediction","exculpation"],
    "E"))

questions.append(se("TCSE874",
    "It remains to be shown how large the differences are between humans and other animals. Although Wynne claims to recognize that __________ data are available to make definitive statements, he offers them, nonetheless, arriving at some sweeping generalizations.",
    ["meager","appropriate","suitable","insufficient","biased","impartial"],
    ["A","D"]))

# ═══════════════════════════════════════════════════════════
# Group 83 (TCSE 875–885)
# ═══════════════════════════════════════════════════════════
questions.append(tc2("TCSE875",
    "The genius of the scientific method is that it (i)__________ the dictum of Aristotle that the goal of science is knowledge of the ultimate cause of things. True science, we now know, advances human knowledge by (ii)__________ ultimate causes and focusing instead on the testing of empirical hypotheses.",
    ["qualifies","jettisons","affirms"],
    ["ignoring","predicting","confirming"],
    ["B","D"]))

questions.append(se("TCSE876",
    "At first, most of the famous fairy tales seem so implausible and so irrelevant to contemporary life that their __________ is hard to understand.",
    ["universality","persistence","appeal","ephemerality","survival","transience"],
    ["B","E"]))

questions.append(tc1("TCSE877",
    "The stories in Yiyun Li's recent collection are distinctive particularly for the strong contrast between their emotional intensity and their consistently __________ tone.",
    ["affable","ebullient","measured","irascible","overwrought"],
    "C"))

questions.append(tc2("TCSE878",
    "So, perhaps the lesson is that rather than wanting their monarchy to (i)__________ its modernized Scandinavian counterparts, the British public cherishes it most when it is most (ii)__________.",
    ["commend","discount","emulate"],
    ["egalitarian","anachronistic","regal"],
    ["C","E"]))

questions.append(se("TCSE879",
    "Few ideas are more __________ than the notion that cultures evolve in Darwinian fashion; many academics have begun writing about cultural evolution, but few treat the underlying Darwinian logic with the care it deserves.",
    ["abused","archaic","misused","outdated","divisive","derivative"],
    ["A","C"]))

questions.append(tc3("TCSE880",
    "Although political events in different countries were not (i)__________ in the nineteenth century, their interrelationship was (ii)__________ compared with the present, when interdependence has become far greater. (iii)__________ has ceased to be an option.",
    ["unconnected","trivial","simultaneous"],
    ["conditional","superficial","transparent"],
    ["Isolationism","Resilience","Idealism"],
    ["A","E","G"]))

questions.append(se("TCSE881",
    "Because its previously __________ beliefs had become core tenets of mainstream politics, the activist group disbanded; with no more skeptics to persuade, its purpose had evaporated.",
    ["arcane","seditious","quixotic","idealistic","popular","conventional"],
    ["C","D"]))

questions.append(tc1("TCSE882",
    "Common and easily accessible resources—prey for predators or hosts for parasites—should be, all other things being equal, used frequently. Still, some apparently accessible and suitable resources remain __________.",
    ["vulnerable","unobtainable","sustainable","depleted","unexploited"],
    "E"))

questions.append(se("TCSE883",
    "In a field of egotists, Bloomfield is __________, often praising her competitors and punctuating her correspondence with self-deprecating remarks.",
    ["unassuming","complimentary","acerbic","ingenuous","cutting","modest"],
    ["A","F"]))

questions.append(tc3("TCSE884",
    "The limitations of human attention cause us to miss much of what goes on around us. The real problem here is that we are often (i)__________ these limitations: we think that we see the world as it really is, but our ostensibly reliable visual experience (ii)__________ striking mental (iii)__________.",
    ["impatient with","unaware of","distracted by"],
    ["belies","unifies","dispels"],
    ["feats","images","lapses"],
    ["B","D","I"]))

questions.append(tc2("TCSE885",
    "Knowing how (i)__________ she was at work, her colleagues were surprised at her (ii)__________ throughout the dinner.",
    ["dependable","diffident","diligent"],
    ["timidity","assertiveness","punctiliousness"],
    ["B","E"]))

# ═══════════════════════════════════════════════════════════
# Part II  Group 162 (TCSE 1771–1779)
# ═══════════════════════════════════════════════════════════
questions.append(tc2("TCSE1771",
    "(i) __________ the cumbersome phraseology of contemporary critical theory, her treatise is, stylistically at least, in sharp contrast with the (ii) __________ of the prose she is analyzing—prose reflective of a culture that values extreme linguistic compression.",
    ["Dismissive of","Replete with","Indifferent to"],
    ["floridness","Intricacy","brevity"],
    ["B","F"]))

questions.append(tc2("TCSE1772",
    "In the early 1990s, the discovery of a new microbe in wastewater led microbiologists to (i)__________ ammonia's conversion to nitrogen compounds. Called anammox (for anaerobic ammonia oxidation), the microbe was converting into nitrogen gas in the absence of oxygen, a reaction previously assumed to be (ii) __________.",
    ["question existing dogma about","abandon efforts to facilitate","raise health concerns regarding"],
    ["hazardous","irreversible","impossible"],
    ["A","F"]))

questions.append(tc1("TCSE1773",
    "Many parents who attended the school board meeting ____________ the fact that emerging social problems in some way affected nearly every pupil at the school; nonetheless, these parents often acted with a view to helping only their own children.",
    ["disregarded","bemoaned","ignored","disputed","embellished"],
    "B"))

questions.append(tc3("TCSE1774",
    "Japan's first university was more (i)_______________ than its Chinese counterparts in the same era, since the Chinese Tang system was highly (ii)_____________. However, this changed over time. As Japanese court offices became increasingly hereditary, the examination system, by which students from a wide range of social classes were admitted into the universities, (iii)____________.",
    ["prestigious","egalitarian","profitable"],
    ["aristocratic","reputable","unsystematic"],
    ["became widely utilized","advantaged the proletariat","atrophied into insignificance"],
    ["B","D","I"]))

questions.append(tc2("TCSE1775",
    "Translators are becoming less rather than more (i)____________. Few readers are (ii)____________ the person who translates their favorite foreign novelist, even though that person will have a huge influence on the tone and feel of every page.",
    ["contentious","insignificant","visible"],
    ["affected by","content with","aware of"],
    ["C","F"]))

questions.append(se("TCSE1776",
    "In this otherwise ____________ study, the internal tensions resulting from the increasing integration of the United States with the world economy are simply mentioned rather than analyzed.",
    ["tedious","thorough","biased","exhaustive","superficial","shallow"],
    ["B","D"]))

questions.append(tc3("TCSE1777",
    "One of the most widespread traits among animals is (i)____________. It runs from (ii)____________, such as yawning when others yawn, to emotional (iii)____________, in which the self resonates with fear or joy when it picks up fear or joy in others.",
    ["selfishness","wariness","empathy"],
    ["mimicry","lethargy","dissimulation"],
    ["antagonism","indifference","contagion"],
    ["C","D","I"]))

questions.append(se("TCSE1778",
    "Neuroscientists are discovering that our sensory systems are much more interconnected than previously thought: even in ordinary circumstances, our senses can ____________ one another in extraordinary ways.",
    ["overrule","bypass","abet","improve","circumvent","support"],
    ["C","F"]))

questions.append(tc3("TCSE1779",
    "Precipitate interest in Jennifer Francis's theory that anomalously rapid warming of the Arctic disrupts weather patterns in temperate latitudes has (i)____________ the normal life cycle of a scientific controversy. Usually data are compiled, hypothesis is tested, and conclusions might then become news if deemed solid. Because Francis's idea links climate change to severe weather, it resonated immediately with the media and the public, and Francis has been forced to (ii)____________ before the scientific process has been (iii)____________.",
    ["extended","inverted","subsumed"],
    ["defend her findings","challenge her colleagues","withdraw her supposition"],
    ["evaluated","qualified","concluded"],
    ["B","D","G"]))

# ═══════════════════════════════════════════════════════════
# Group 164 (TCSE 1780–1790)
# ═══════════════════════════════════════════════════════════
questions.append(tc3("TCSE1780",
    "In general, observational studies tend to (i)____________ the effect of diet on overall health because a healthy diet is often (ii)____________ a healthy lifestyle. People who watch what they eat probably exercise more, avoid smoking, and follow other behaviors (iii)____________ good health. Any of those behaviors might also help explain why these people have lower disease rates.",
    ["overstate","clarify","discount"],
    ["irrelevant to","a marker for","a substitute for"],
    ["caused by","unrelated to","linked to"],
    ["A","E","I"]))

questions.append(tc1("TCSE1781",
    "Though her works demonstrate a remarkable dexterity and command of technique with oil paint, as an artist Mangala Bai Thampuratty (1866–1953) was not ____________, having produced only a few paintings.",
    ["influential","prolific","innovative","eclectic","proficient"],
    "B"))

questions.append(tc2("TCSE1782",
    "The (i)____________ of Polish immigration to Brazil are easy to (ii)____________, since at the time of the first Polish arrivals, in the nineteenth century, Poland was partitioned, which resulted in many ethnic Poles carrying German, Russian, or Prussian passports.",
    ["historical contexts","cultural ramifications","cumulative volumes"],
    ["misjudge","justify","predict"],
    ["C","D"]))

questions.append(se("TCSE1783",
    "The convergence of two disparate sciences allows the imagining of new questions that cannot be addressed by knowledge and techniques ____________ either field.",
    ["pioneered by","sequestered within","unsuitable for","unique to","crucial for","important to"],
    ["B","D"]))

questions.append(se("TCSE1784",
    "Though ____________ in his musical expression, the American jazz bassist and composer Charles Mingus eventually developed a personal voice that proved to be much more than a simple mixture of jazz styles.",
    ["eclectic","idiosyncratic","uncompromising","virtuosic","wide-ranging","relentless"],
    ["A","E"]))

questions.append(se("TCSE1785",
    "Despite growing evidence of a positive association between consumption of whole grains and long-term health, a research gap exists between observational studies and the elucidation of the mechanism involved, mechanisms that in some cases are still quite____________.",
    ["ineffective","speculative","unproductive","obscure","unsubstantiated","controversial"],
    ["B","D"]))

questions.append(tc3("TCSE1786",
    "Despite the (i)____________ nature of contemporary science, the (ii)____________ of many individuals (iii)____________: the work of women and minority scientists has too often been exploited or deemed rudimentary and unworthy of inclusion into science history books.",
    ["collaborative","controversial","sophisticated"],
    ["motivations","contributions","idiosyncrasies"],
    ["manifest themselves","point to a solution","remain overlooked"],
    ["A","E","I"]))

questions.append(tc3("TCSE1787",
    "The message in Kaku's new book might be encouraging, but it is a shame that it is delivered in a rather (i)____________ manner: the book is never (ii)____________, but there is (iii)____________ that quickly becomes wearying. Every innovation or gadget has to be likened to something in film, as if we were incapable of understanding these things without endless prodding.",
    ["speculative","joking","pedestrian"],
    ["clear in its aims","far from insipidity","less than readable"],
    ["an obscurity","a repetitiveness","a tendentiousness"],
    ["C","F","H"]))

questions.append(se("TCSE1788",
    "Though Edmurd certainly had a dignified bearing and made a great first impression, those who became acquainted with him soon realized he had an essentially ____________ nature.",
    ["pugnacious","deliberate","punctilious","courteous","complacent","truculent"],
    ["A","F"]))

questions.append(tc1("TCSE1789",
    "The author argues that the coinage was ____________ by the medieval practice of 'clipping' of coins, or shaving off the edges to save the silver.",
    ["debased","ameliorated","exaggerated","promulgated","forged"],
    "A"))

questions.append(tc2("TCSE1790",
    "The geographer held a (i)____________ view of the succession of theoretical trends (environmental determinism, spatial determinism, and various types of critical theory) in her field, maintaining that theory can (ii)____________ what is transpiring in a complex environment by focusing excessively on the favored schemes and variables of the moment.",
    ["self-contradictory","sanguine","deprecatory"],
    ["exacerbate","obfuscate","magnify"],
    ["C","E"]))

# ═══════════════════════════════════════════════════════════
# Group 166 (TCSE 1791–1800)
# ═══════════════════════════════════════════════════════════
questions.append(tc3("TCSE1791",
    "Although Sapir and Whorf's notion that different languages may impart different cognitive skills met with (i)____________ early on, they had little evidence to support their claim. By the 1970s many scientists had become (ii)____________ their hypothesis, and it was largely (iii)____________ as a new set of theories claiming that language and thought are universal came to dominate the field.",
    ["skepticism","excitement","controversy"],
    ["convinced of","disenchanted with","inured to"],
    ["revived","corroborated","abandoned"],
    ["B","E","I"]))

questions.append(se("TCSE1792",
    "Myth and orality are ____________ in Africa: the former is ubiquitous in the African oral literary tradition, while the latter is almost always based on the former.",
    ["interdependent","didactic","sententious","paramount","symbiotic","ancient"],
    ["A","E"]))

questions.append(se("TCSE1793",
    "By 1600, France's sense of itself as a nation bound by a shared destiny was ____________, but over the course of the seventeenth century French culture regained the strength it had had in the Middle Ages.",
    ["absent","innocuous","benign","unique","precarious","uncertain"],
    ["E","F"]))

questions.append(tc3("TCSE1794",
    "Why is the idea that self-deception contributes to happiness so (i)____________? The (ii)____________ of self-deception leads people to assume that it must have some function, that it is, in fact, adaptive in the sense that it helps us survive and thrive. But one could (iii)____________ by arguing that the capacity for self-deception is actually only a by-product of other features of the human mind that are beneficial for reasons other than their being implicated in producing self-deception.",
    ["irrational","repugnant","attractive"],
    ["triviality","prevalence","hazardousness"],
    ["counter this logic","dodge this question","revitalize this theory"],
    ["C","E","G"]))

questions.append(se("TCSE1795",
    "The author illustrates her book about mid-nineteenth-century Paris with photographs revealing the ____________ conditions that prevailed in the city: sewage can be seen draining onto streets lined with crumbling buildings.",
    ["dreary","ambiguous","obscure","noxious","ramshackle","insalubrious"],
    ["D","F"]))

questions.append(tc2("TCSE1796",
    "We won't know what the voters do until they do it, and this is a good time to recall that the accuracy of polls and prognostications depends on who votes. But defying expectations, the electorate seems poised to (i)____________ a number of political tenets so (ii)____________ that they are paraded as fact.",
    ["propound","reject","uphold"],
    ["entrenched","intricate","tenable"],
    ["B","D"]))

questions.append(tc2("TCSE1797",
    "Technocrats and managers cloak contestable value judgements in the garb of 'science': thus the (i)____________ mathematical models that reframe (ii)____________ conclusions (such as the worth of a worker, service, article, or product) as the inevitable dictate of salient, measurable data.",
    ["insatiable demand for","manifest cynicism toward","ambivalent faith in"],
    ["trivial","subjective","foregone"],
    ["A","E"]))

questions.append(tc3("TCSE1798",
    "Whatever the level of the museum's past (i)____________ American art, it pales beside its current (ii) ____________. Since opening its renovated and expanded building, the museum has relegated American paintings to hard-to-find corners of the museum. It is as if American art is (iii) ____________ the overwhelmingly European narrative that dominates the permanent collection galleries.",
    ["enthusiasm for","advocacy of","neglect of"],
    ["craze","disdain","support"],
    ["fundamental to","excluded from","privileged over"],
    ["A","E","H"]))

questions.append(se("TCSE1799",
    "At first glance, the new CEO stands in stark contrast to his predecessor: while Simpkins came across as a scolding headmaster, his successor appears ____________.",
    ["blithe","judicious","scrupulous","winsome","bland","modest"],
    ["A","D"]))

questions.append(tc3("TCSE1800",
    "The essays in this collection, which explore the adaptation of literary texts to film, all (i)____________ the view that the fidelity of film adaptations to their literary precursors is (ii)____________. In fact, the authors of these essays broadly concur that an emphasis on fidelity in film adaptations can be traced to an outmoded academic ideology that insistently prizes the literary in a way that (iii)____________ the value of the cinematic.",
    ["contest","reinforce","sidestep"],
    ["impossible to achieve","a measure of success","difficult to recognize"],
    ["echoes","enhances","subordinates"],
    ["A","E","I"]))

# ═══════════════════════════════════════════════════════════
# Group 168 (TCSE 1801–1812)
# ═══════════════════════════════════════════════════════════
questions.append(tc2("TCSE1801",
    "Some researchers and educators have (i)____________ the argument for hands-on learning, (ii)____________ that a more straightforward approach—known as direct instruction—has potential to help students learn more effectively.",
    ["challenged","evaluated","refined"],
    ["conceding","maintaining","pretending"],
    ["A","E"]))

questions.append(tc2("TCSE1802",
    "Confidence in the nation's finances, barely nailed together by international financial institutions a few weeks ago, is still such a (i)____________ structure that the slightest disturbance could set it (ii)____________.",
    ["ramshackle","labyrinthine","rigid"],
    ["quivering","ablaze","right"],
    ["A","D"]))

questions.append(se("TCSE1803",
    "The negotiations would feature J.P. Morgan in his most famously ____________ mode: knocking heads together, barking out prices for properties, and forcing titans to truckle to his will.",
    ["quixotic","eccentric","histrionic","theatrical","chivalrous","gallant"],
    ["C","D"]))

questions.append(tc2("TCSE1804",
    "Once Plowright's research is complete, she will be prepared to talk about it (i)____________, but for now, because she is discussing theories rather than facts and does not want to commit herself to an unsubstantiated claim, she prefers to make only the most (ii)____________ comments.",
    ["authoritatively","tentatively","extemporaneously"],
    ["provisional","prescient","germane"],
    ["A","D"]))

questions.append(se("TCSE1805",
    "Dogs' intake of olfactory information is less ____________ than that of humans because dogs exhale through the side slits of their nostrils, keeping a continuous flow of inhaled air in their snouts for smelling.",
    ["strenuous","mediated","punctuated","indirect","deliberate","Intermittent"],
    ["C","F"]))

questions.append(tc2("TCSE1806",
    "In a nation that has been reeling from one weather or climate disaster to another, with record tornado outbreaks, landfalling tropical storms and superstorms, record winter snowfalls, and severe droughts, persistent droughts appear almost (i)____________. They (ii)____________ of floods and storms, appearing instead slow-moving disasters whose beginnings and ends are even often hard to identify.",
    ["incessant","prosaic","baneful"],
    ["eclipse the devastating force","lack the violent destructiveness","underscore the benignity"],
    ["B","E"]))

questions.append(tc3("TCSE1807",
    "Surrealism sought to (i)____________ precisely the impulses that traditional or generally accepted thinking had (ii)____________. It was after instinctive, irrational awarenesses, which might come from dreams, or from accepting results derived by chance—or from a receptivity to what is taboo—that could (iii)____________ our sense of everyday reality.",
    ["augment","conceal","affirm"],
    ["marginalized","assimilated","propagated"],
    ["reflect","unsettle","undergird"],
    ["A","D","H"]))

questions.append(tc3("TCSE1808",
    "Here is a basic point: reading itself a fundamentally (i)____________ act. Anyone who has ever taught a child to read will remember the difficulty involved in distinguishing, for instance, between lowercase b, d and p. After all, if you move them around or flip them over, they (ii)____________. We have to be taught to see them only as they appear, flat unnatural, upon the printed page. And we have to be taught also to (iii)____________ not just a few of these odd marks but the thousands that go into telling even the simplest children's story.",
    ["substantial","expanding","unnatural"],
    ["are the same","become inexplicable","are easily distinguishable"],
    ["reverse","combine","comprehend"],
    ["C","G","I"]))

questions.append(tc3("TCSE1809",
    "History is about recognizing continuities and therefore the historian must (i)____________ stories that rope together the disparate worlds of past and present. But it is also true that honest history arises from a sense of (ii)____________. It is the experience of discontinuity that alerts us to the (iii)____________ of the past and sets us looking for narratives to capture that unfamiliar entity.",
    ["weave","shun","untangle"],
    ["interruptedness","powerlessness","imperiousness"],
    ["inexorableness","strangeness","lucidity"],
    ["A","D","H"]))

questions.append(se("TCSE1810",
    "By eating tiny organisms and incorporating their prey's nutrients into their own bodies, large insects become 'nutrient packages' for larger insectivores for whom the pursuit of tiny organisms would be ____________.",
    ["unwieldy","insalubrious","unremunerative","unnecessary","inopportune","unprofitable"],
    ["C","F"]))

questions.append(tc3("TCSE1811",
    "During the 1950s and 1960s, theory-minded neoclassical economists came to (i)____________ the field of labor economics, pushing their more fact-oriented colleagues to the margins. In more recent years, the theorists have become interested in just the sort of (ii)____________ issues they once associated with other economists and whose study they once (iii)____________.",
    ["dominate","popularize","respect"],
    ["notional","quotidian","unexamined"],
    ["disdained","monopolized","promulgated"],
    ["A","E","G"]))

questions.append(tc1("TCSE1812",
    "Contrary to what might be expected, having numerous relationships is not necessarily a ____________ loneliness since loneliness is determined by the way people experience relationships subjectively.",
    ["measure of","bulwark against","catalyst for","consequence of","substitute for"],
    "B"))

# ═══════════════════════════════════════════════════════════
# Group 170 (TCSE 1813–1822)
# ═══════════════════════════════════════════════════════════
questions.append(tc3("TCSE1813",
    "George Eliot's biographer can be highly inventive, but, at the same time, somewhat (i)____________ in her approach to Eliot. She will hoist an alluring psychological flag concerning Eliot and then scrupulously take it down again, because the evidence will not serve to (ii)____________ it. But she takes it down only after it has taken an entirely (iii)____________ flutter in the breeze.",
    ["sentimental","irresponsible","reproachful"],
    ["embroider","discount","support"],
    ["unwarranted","accidental","justified"],
    ["B","F","G"]))

questions.append(se("TCSE1814",
    "In the ancient world, preferences concerning perfumery were ____________: the Roman author Pliny noted that the popular iris perfume of Corinth was eventually supplanted by a succession of other fragrances.",
    ["idiosyncratic","anomalous","ephemeral","eccentric","transitory","arbitrary"],
    ["C","E"]))

questions.append(tc1("TCSE1815",
    "Baron's book implores scientists to present their work in ways that are accessible to the general public in order to save the world at large from scientific illiteracy, ______________ that is echoed in other recent publications.",
    ["a query","an analysis","an exhortation","an allurement","an implication"],
    "C"))

questions.append(se("TCSE1816",
    "The fact that no single Cantonese dictionary is seen as ____________ is one of the main reasons why most Hong Kong authors do not depend on formal reference tools when writing in Cantonese.",
    ["dependable","authoritative","meticulous","definitive","topical","comprehensive"],
    ["B","D"]))

questions.append(tc1("TCSE1817",
    "Research indicates that the habitat ____________ commonly observed for meadow voles and prairie voles living in a single ecosystem results primarily from species differences in habitat tolerance, with interspecific competition playing a lesser role.",
    ["degradation","alteration","saturation","complexity","segregation"],
    "E"))

questions.append(se("TCSE1818",
    "Although workers are eager to believe rumors that the manufacturer plans to invest in modernizing the local plant, the troubled auto company has made no public commitment that would ____________ the plant's future.",
    ["illuminate","endanger","jeopardize","affect","clarify","secure"],
    ["A","E"]))

questions.append(tc1("TCSE1819",
    "The phrase 'right to privacy' is used to refer to a variety of conflicting interests that are not easily subsumed under one definition—with the result that the meaning of the phrase itself has become quite ____________.",
    ["archaic","nebulous","incendiary","platitudinous","plenitudinous"],
    "B"))

questions.append(tc3("TCSE1820",
    "Herbivorous vertebrates often influence the relative (i)____________ of plants with differing palatability within an ecosystem, even though their impact on system-level plant biomass is generally (ii)____________: predators control herbivore numbers, ensuring that the surviving herbivores have (iii)____________ marginally edible plants.",
    ["abundance","hardiness","notoriousness"],
    ["uncertain","irreversible","negligible"],
    ["some ability to detect","few reasons to avoid","no need to consume"],
    ["A","F","I"]))

questions.append(se("TCSE1821",
    "Orbiting Jupiter just beyond Europa, the giant moon Ganymede—bigger than the planet Mercury—appears rather ____________ on the outside, but it may be warm and active within.",
    ["desiccated","forbidding","weathered","inert","adamant","dormant"],
    ["D","F"]))

questions.append(se("TCSE1822",
    "Producers are concerned about Broadway theater's economic straits, which, even setting aside current woe, could ____________ difficulty raising money for future productions.",
    ["presage","foretell","preclude","exacerbate","belie","prevent"],
    ["A","B"]))

# ═══════════════════════════════════════════════════════════
# Group 172 (TCSE 1824–1840; note 1823 absent in PDF)
# ═══════════════════════════════════════════════════════════
questions.append(tc3("TCSE1837a",  # pine stumps (printed as 1837 in PDF p.22)
    "Pine stumps have been found in discrete layers in peat deposits throughout western Europe and thus represent brief but distinct episodes of bog colonization by pine. Their occurrence implies conditions on the bog surface suitable for colonization, followed by inhospitable conditions for trees that nevertheless facilitated preservation of stumps. Thus, the (i)____________ of pine stumps can (ii)____________ climate change, by (iii)____________ the inference that bog surfaces had dried sufficiently to allow colonization and then became too wet to support the trees.",
    ["loss","resilience","presence"],
    ["proceed undetected by","vary independently of","function as a proxy for"],
    ["supporting","repudiating","articulating"],
    ["C","F","I"]))

questions.append(tc3("TCSE1824",
    "Conservationists have proposed various strategies for tropical forest management, but after examining the ecology and economies of mahogany logging in Bolivia, a team of researchers recently concluded that most well-meaning efforts have slim chances for success and could even (i)____________. Not only is sustainable forestry management financially (ii)____________, they say, but adopting such methods could (iii)____________ forest damage.",
    ["commence","backfire","flourish"],
    ["compelling","unattractive","pragmatic"],
    ["mitigate","nullify","increase"],
    ["B","E","I"]))

questions.append(se("TCSE1825",
    "Stacy Schiff, in Cleopatra: A Life, strips away the accretions of myth that have built up around the legendary figure and plucks off the imaginative embroiderings of Shakespeare, Shaw and Elizabeth Taylor.",
    ["denigrates","elucidates","embellishes","aggrandizes","demystifies","manipulates"],
    ["B","E"]))

questions.append(se("TCSE1826",
    "Whereas ground-based interferometers detect astrophysical events briefly and infrequently, space-based ones should hear a ____________ of signals as soon as they turn on, including a constant chorus from binary white dwarfs in our galaxy.",
    ["smattering","plethora","profusion","trickle","range","hum"],
    ["B","C"]))

questions.append(tc2("TCSE1827",
    "Those who knew the senator well were convinced that in spite of his (i)____________ in larger political matters, there was no (ii)____________ in his expressions of feeling for his constituents.",
    ["candor","duplicity","cooperation"],
    ["dissemblance","compassion","fervency"],
    ["B","D"]))

questions.append(tc2("TCSE1828",
    "Although its (i)____________ is (ii)____________, the musical style known as 'ragtime' has most often been described as an amalgamation of African American music with European forms.",
    ["artistic diversity","commercial appeal","precise definition"],
    ["exogenous","settled","elusive"],
    ["C","F"]))

questions.append(tc2("TCSE1829",
    "Scientists have (i)____________ evidence to suggest a cause for the failure of the horse to become the predominant herbivore in central Alberta following glacial recession. A loss of optimal food resources was been cited as a possible cause of the decline of horse populations elsewhere, but the Albertan vegetation data for the period are (ii)____________.",
    ["extensive","little direct","familiar"],
    ["circumstantial","misleading","conflicting"],
    ["B","F"]))

questions.append(tc3("TCSE1830",
    "Direct imaging cannot yet be done for a terrestrial exoplanet because of the daunting optics challenges. For one thing, the glow of a terrestrial exoplanet could be much more (i)____________ than that of its host star. If this is the case, scientists would have to (ii)____________ much of the host star's light to (iii)____________ the exoplanet.",
    ["intense","uniform","faint"],
    ["detect","occult","measure"],
    ["shroud","analyze","reveal"],
    ["C","E","I"]))

questions.append(tc1("TCSE1831",
    "In early twentieth-century India, the claim that films from the West screened by 'first-class theaters' were exclusively 'high-class features' was ____________, since a film's being screened by such theaters was interpreted as a confirmation of quality.",
    ["controversial","paradoxical","anachronistic","tautological","prescient"],
    "D"))

questions.append(tc2("TCSE1832",
    "Dr. Oransky and Mr. Marcus are partisans who editorialize sharply against poor oversight and vague retraction notices, yet their focus on evidence over accusations (i)____________ watchdog forerunners who sometimes seemed (ii)____________ personal animus.",
    ["aligns them with","exposes them to","distinguishes them from"],
    ["indifferent to","motivated by","appalled at"],
    ["C","E"]))

questions.append(tc3("TCSE1833",
    "Ultimately, the young idealists (i)____________ the society they so fervently desired to reform: in their frustration, they reacted to the immediate situation by removing themselves from the postwar social and political arena, where the future of their country was being decided. In doing so, they (ii)____________ the salutary effects their rebellion should have (iii)____________.",
    ["were able to captivate","paid excessive tribute to","did a great disservice to"],
    ["publicized","nullified","eschewed"],
    ["subverted","begotten","superseded"],
    ["C","E","H"]))

questions.append(se("TCSE1834",
    "For wily political press officers, the art of spin is not quite supplanting truth with lies, but instead it aspires to replace awkward complexity with catchy ____________; successful spin creates the impression of unavoidable common sense.",
    ["novelties","slogans","falsehoods","duplicity","simplicity","intelligibility"],
    ["E","F"]))

questions.append(tc3("TCSE1835",
    "Castillo's apparently inexhaustible posthumous career is about to have a significant second act: the large number of books written by Castillo already available is soon to double. While this prospect is bound to thrill many readers, we might (i)____________ our excitement with the recognition that when it comes to publishing the dead, the best is not often saved for last. Given the remarkable (ii)____________ of Castillo's publications to date, it seems unlikely that any of the looming titles could (iii)____________ the masterpieces we already know.",
    ["convey","temper","amplify"],
    ["abstruseness","vacuity","virtuosity"],
    ["equal","outsell","undermine"],
    ["B","F","G"]))

questions.append(se("TCSE1836",
    "Although the use of cameras to study animal behavior was certainly not ____________, cameras were nevertheless not used to study individual frogs in their natural habitat until 2009.",
    ["ideal","unprecedented","laborious","impractical","novel","perfect"],
    ["B","E"]))

questions.append(tc2("TCSE1837b",  # Elizabeth/laconic (also printed as 1837 in PDF p.25)
    "In light of Elizabeth's habitually (i)____________ nature, her friends were quite surprised by her (ii)____________ at the convention.",
    ["ingenuous","laconic","intractable"],
    ["garrulity","ostentatiousness","tenacity"],
    ["B","D"]))

questions.append(tc2("TCSE1838",
    "The (i)____________ of preserved plant remains found by archaeologists at late Pleistocene Paleoindian sites led them to hypothesize a Paleoindian lifestyle in which hunting (ii)____________ gathering, but it now appears that excavation techniques skewed the findings, leading to an underestimation of the use of plant foods.",
    ["paucity","ubiquity","diversity"],
    ["was succeeded by","took precedence over","merely supplemented"],
    ["A","E"]))

questions.append(tc1("TCSE1839",
    "Modern monetary systems are built on nothing more than governments' support of and people's faith in them; money is, in other words, a complete ____________.",
    ["encumbrance","necessity","abstraction","anachronism","misnomer"],
    "C"))

questions.append(tc3("TCSE1840",
    "When there is less natural dust blowing into eastern China, the air quality for millions of people there (i)____________: natural dust plays an important role in determining air temperatures and thereby promotes winds to (ii)____________ human-made pollution. Less natural dust, therefore, means the air becomes (iii)____________, with pollution becoming more concentrated and sticking around longer.",
    ["worsens","fluctuates","Improves"],
    ["accumulate","exacerbate","disperse"],
    ["more unsettled","increasingly stagnant","less stable"],
    ["A","F","H"]))

# ═══════════════════════════════════════════════════════════
# Write to JSON
# ═══════════════════════════════════════════════════════════
with open(DATA_FILE, encoding="utf-8") as f:
    data = json.load(f)

existing_ids = {q["id"] for q in data["verbal"]}
added = [q for q in questions if q["id"] not in existing_ids]
data["verbal"].extend(added)

with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Added {len(added)} TCSE questions (skipped {len(questions)-len(added)} duplicates)")
print(f"Total verbal: {len(data['verbal'])}")
