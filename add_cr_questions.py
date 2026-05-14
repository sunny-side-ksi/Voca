"""CR_5lb_Ch6 — Argument-Based Reading Comprehension (Manhattan 5lb Ch.6)
   → gre_content/practice_questions.json 에 critical_reasoning 문제 추가
"""
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "gre_content" / "practice_questions.json"


def cr(qid, passage, stem, a, b, c, d, e, correct, diff="medium"):
    return {
        "id": qid, "section": "verbal", "type": "critical_reasoning",
        "subtype": "cr", "difficulty": diff, "set": None,
        "passage": passage, "stem": stem,
        "blanks": [{"label": "Blank", "choices": {"A": a, "B": b, "C": c, "D": d, "E": e}}],
        "correct": [correct], "explanation": "", "source": "CR_5lb_Ch6",
    }


questions = [

# ── Q1 ──────────────────────────────────────────────────────────────────────
cr("CR5LB_01",
   "The school board has responded to the new school lunch guidelines by replacing fried potatoes "
   "with fruit in a standard meal option that used to consist of a hamburger, fried potatoes, and "
   "milk. However, the guidelines specifically require that vegetables, not fruits, be included in every meal.",
   "The information above most strongly supports which of the following conclusions?",
   "Fruit provides just as much nutritional value as vegetables.",
   "Students are more likely to eat fruit than vegetables.",
   "The school board is not following the new school lunch guidelines.",
   "The school board is responsible for the health of the student population.",
   "The new school lunch guidelines are unnecessarily strict.",
   "C"),

# ── Q2 ──────────────────────────────────────────────────────────────────────
cr("CR5LB_02",
   "While many people think of the lottery as a harmless way to have fun and possibly win some money, "
   "buying lottery tickets is a form of gambling. Therefore, public officials shouldn't buy lottery tickets.",
   "The argument relies upon which of the following assumptions?",
   "Individuals who play the lottery are less likely to win a big payout than they are to be killed in a car crash.",
   "Some public officials are guilty of much more serious offenses than gambling.",
   "Some public officials shouldn't gamble.",
   "Many public officials are already tempted to violate rules governing their positions.",
   "Most lottery winners are not made as happy by their winnings as they expected.",
   "C"),

# ── Q3 ──────────────────────────────────────────────────────────────────────
cr("CR5LB_03",
   "Some say that Saddlebrook College provides the best value in our state. Yet, students of our "
   "state's Tunbridge College pay less, enjoy newer buildings and smaller class sizes, and earn "
   "larger incomes after graduation.",
   "The information above most strongly supports which of the following judgments?",
   "Tunbridge College provides the best value in our state.",
   "Tunbridge College has more stringent entrance requirements than Saddlebrook, and thus attracts students of a higher caliber.",
   "It is not true that Saddlebrook College is the best value in our state.",
   "Students at Tunbridge College report higher rates of satisfaction than students at Saddlebrook.",
   "Earning a high income after graduation is a valid means of judging the value of a college education.",
   "C"),

# ── Q4 ──────────────────────────────────────────────────────────────────────
cr("CR5LB_04",
   "Students have long shown that people who drive red cars receive more speeding tickets from the "
   "police than people who drive cars of other colors. Researchers have thus concluded that the color "
   "of a car influences its driver's behavior.",
   "The researchers' conclusion depends upon which of the following assumptions?",
   "Red cars do not attract more attention from the police than do cars of other colors.",
   "Police officers do not pull over red car drivers more often for reasons unrelated to the drivers' behavior.",
   "The color red does not cause drivers to feel more aggressive while driving.",
   "Red car drivers do not receive more expensive parking tickets on average than drivers of other colors.",
   "Drivers of red cars are not generally more risk-tolerant than drivers of other colors.",
   "B"),

# ── Q7 ──────────────────────────────────────────────────────────────────────
cr("CR5LB_07",
   "The fight against the drug trade in Country X should focus on the time being on tightening the "
   "country's borders and targeting major smugglers. Rather, the United Nations and the government of "
   "Country X should eventually replace the poppy fields with other farming ventures (\"agricultural "
   "infrastructure\"). Country X should eventually replace the poppy fields with other farming ventures.",
   "What function do the two boldface sentences serve in the passage?",
   "The first is a short-term conclusion reached by the speaker; the second is a longer-term conclusion.",
   "The first is a short-term solution to a problem; the second is a longer-term solution to the same problem.",
   "The first presents a problem; the second sentence, rather than providing evidence, presents a solution.",
   "No information was given about the popularity of the solution, so this is incorrect.",
   "The first sentence presents an argument; the second sentence, rather than providing evidence, presents a solution.",
   "B"),

# ── Q8 ──────────────────────────────────────────────────────────────────────
cr("CR5LB_08",
   "In the 18th and 19th centuries, it was believed by many in coastal cities of the United States that "
   "the waterfront was an undesirable location for residential buildings. As a result, developers paid "
   "low prices for homes along the beach. Today, however, urban waterfront properties are generally "
   "seen as prestigious, as evidenced by the large sums paid for homes along the beach from a developer "
   "who wishes to make a large profit would be wise to buy urban waterfront properties.",
   "Which of the following, if true, most strongly supports the chairman's argument?",
   "People today have more money, relatively speaking, to spend on real estate than they did in previous centuries.",
   "Homeowners will be willing to spend large sums of money on residential properties in traditionally industrial or commercial districts.",
   "Many urban waterfront lots are available for purchase.",
   "Many coastal cities are encouraging developers to rehabilitate the waterfront through tax incentives.",
   "Properties in interior residential districts in coastal cities are significantly more expensive than those on the waterfront.",
   "B"),

# ── Q9 ──────────────────────────────────────────────────────────────────────
cr("CR5LB_09",
   "Psychiatric research has shown that receiving high quality outpatient care, rather than being "
   "confined to an institution, produces the best quality of life for people who are mentally ill. "
   "Responding to this research, Congress allowed most of the mentally ill to leave mental institutions. "
   "In 1983, however, researchers discovered that, contrary to what they would have expected, the "
   "mentally ill who had been released were doing worse than those who had stayed. Congress has "
   "therefore proposed that all visitors from Country Y undergo a medical examination before entering Country X.",
   "Which of the following, if true, resolves the paradox in the passage above?",
   "More people were diagnosed with psychiatric disorders in 1983 than in 1963.",
   "In 1983, men who had been released from mental institutions fared worse than their female counterparts.",
   "The discovery of new medications does not explain why the mentally ill were doing worse in 1983.",
   "Congress never supplied the funding that would have been necessary to provide high-quality outpatient care to the newly released patients.",
   "The specific diagnoses of those who fared worst in 1983 cannot be resolved under consideration.",
   "D"),

# ── Q10 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_10",
   "In response to the increasing cost of producing energy through traditional means, such as combustion "
   "and solar power, hoping someday to rely on them completely and thus lower energy costs. The utility "
   "companies claim that, although these sources require significant initial capital investment, they will "
   "provide stable energy supplies at low cost. As a result, these sources will be less risky for certain "
   "utilities than non-renewable sources, such as oil and coal, whose prices can fluctuate dramatically "
   "according to availability.",
   "The claim of the utility companies presupposes which of the following?",
   "The public will embrace the development of wind and solar power.",
   "No new deposits of gas, oil, and coal will be discovered in the near future.",
   "Weather patterns are consistent and predictable, so solar and wind energy supplies will be stable.",
   "The necessary technology for conversion to wind and solar power is not more expensive than the technology required to create energy through combustion.",
   "Obtaining energy from nonrenewable sources, such as gas, oil, and coal, cannot be made less risky.",
   "C"),

# ── Q11 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_11",
   "Inorganic pesticides remain active on the surfaces of fruits and vegetables for several days after "
   "spraying, while organic pesticides dissipate within a few hours after leaving the surface of the "
   "sprayed produce. Therefore, one must be careful to wash the produce thoroughly before eating it to "
   "prevent the ingestion of pesticides. Therefore, when purchasing from a farm that uses only organic "
   "pesticides, one need not worry about ingesting pesticides.",
   "The argument above assumes which of the following?",
   "All produce that has been treated with inorganic pesticides must be labeled as such at the point of sale.",
   "No farm that uses only organic pesticides also uses inorganic pesticides from other sources.",
   "The conclusion of the argument is already limited to those farms that use \"only organic pesticides.\"",
   "Organic pesticides are incapable of penetrating the skin of a fruit or vegetable; therefore, the organic pesticide will dissipate from the fruit a few hours after application.",
   "The use of either type of pesticide does not increase the cost of the produce.",
   "D"),

# ── Q12 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_12",
   "Although the exact cause is unknown, Disease X generally occurs when various cell types become "
   "resistant to a naturally occurring hormone and the pancreas is unable to produce that hormone at "
   "a high enough rate to reduce the number of patients suffering complications from Disease X. The "
   "government thinks that the proposed education program will be effective, it should educate the "
   "public about appropriate medication usage.",
   "Which of the following, if true, provides the strongest reasons to believe that the proposed "
   "education program will not be effective?",
   "School health programs already educate middle school students about the threat.",
   "The public already has access to this information through the internet.",
   "The government has not set aside money for such a program.",
   "Drug manufacturers lobby doctors to prescribe their company's brand of medication.",
   "If the proper medications are unaffordable, educating people about those medications will do little to increase their proper use and thus achieve the stated goal.",
   "E"),

# ── Q13 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_13",
   "Every year, many people become ill because of airborne mold spores in their homes. After someone "
   "becomes ill, specialists look in damp areas of the house, since mold is almost always found in "
   "places where there is substantial moisture. If one wishes to avoid mold poisoning, then, one should "
   "make sure to keep all internal plumbing in good condition to prevent leakage and minimize mold growth.",
   "Which of the following is an assumption on which the argument depends?",
   "Mold does not create moisture; therefore, wet areas as a result of mold is not a possibility.",
   "Most homeowners know enough about plumbing to determine whether theirs is in good condition.",
   "Mold cannot grow in dry areas, so the fact that mold is almost always found in wet areas is still valid.",
   "Even if some varieties of mold are harmless, the conclusion that one should keep plumbing in good condition to minimize mold growth could still be valid.",
   "Whether mold spores can be filtered from the air may be relevant to a conclusion about the health effects of mold in the home, but it is not directly relevant to the given conclusion.",
   "A"),

# ── Q14 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_14",
   "To prevent overcrowding, last month the town zoning board limited the number of new buildings that "
   "can be constructed in town to two per year. Critics of the plan argue that this plan will not prevent "
   "overcrowding. The town currently has only a very modest rate of new building construction; the plan "
   "would allow the same rate of new construction to continue unimpeded by the new zoning restrictions.",
   "Which of the following, if true, would most support the claims of the critics of the plan?",
   "Other towns funded under similar zoning plans have had mixed success with similar zoning plans.",
   "Since the construction of the last school in town is irrelevant to this argument.",
   "So how property taxes in this town compare to those in neighboring towns is irrelevant.",
   "The town zoning board states that 'the town zoning board limited the number of new buildings that can be constructed in the town in any given year.' The goal of this plan is to prevent overcrowding.",
   "The nearest garbage dump is several miles away from town.",
   "D"),

# ── Q15 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_15",
   "Because of a new type of fungus that killed off cacao trees in Brazil, there was an unusually meager "
   "harvest of cacao beans this year. The wholesale price of cocoa solids and cocoa butter has increased "
   "significantly and is likely to stay high. Therefore, the retail price of chocolate is certain to "
   "increase within six months.",
   "The answer to which of the following questions would provide information relevant to evaluating the argument above?",
   "Has the price of cocoa solids and cocoa butter remained steady during other periods of poor harvest?",
   "Are consumers willing to spend more for chocolate?",
   "Have the prices of other ingredients in the chocolate decreased recently?",
   "What percentage of cacao trees in Brazil were affected by the fungus?",
   "Can the fungus be eliminated within the next six months?",
   "C"),

# ── Q20 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_20",
   "Smoking is a known cause of serious health problems, including emphysema and lung cancer. Now, "
   "an additional concern can be added to the list of maladies caused by smoking. A recent study "
   "surveyed both smokers and nonsmokers, and found that smokers are significantly more anxious and "
   "nervous than nonsmokers.",
   "Which of the following is an assumption on which the argument rests?",
   "Anxiety and nervousness can lead to serious health problems.",
   "Anxiety and nervousness do not make individuals more likely to start smoking.",
   "Equivalent numbers of smokers and nonsmokers were surveyed for the study.",
   "Smokers who had smoked a cigarette immediately before responding to the survey were more anxious and nervous than those who had not smoked for several hours.",
   "Smokers are aware of the serious health problems attributed to smoking, including lung cancer and emphysema.",
   "B"),

# ── Q21 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_21",
   "The number of cases of tuberculosis diagnosed in Country X increased dramatically this year. The "
   "country's news media have speculated that the sharp increase in new cases is the result of the "
   "tuberculosis outbreak that occurred in neighboring Country Y last year. Health officials in Country "
   "X have therefore proposed that all visitors from Country Y undergo a medical examination before "
   "entering Country X.",
   "Which of the following, if true, most strongly suggests that the proposed medical examinations "
   "will not help curb the spread of tuberculosis in Country X?",
   "Country Z, which also neighbors Country Y, has not experienced an increase in cases of tuberculosis.",
   "Current medical technology is not capable of detecting all carriers of tuberculosis.",
   "Tuberculosis is not spread through human contact.",
   "Visitors from Country Y are not the source of the disease. Thus, testing them would likely do little to curb the spread of the disease.",
   "If the visitors from Country Y are indeed carriers, then their refusal to visit Country X would help curb the spread.",
   "D"),

# ── Q22 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_22",
   "The People of Prohibitionland are considering banning the service of alcoholic beverages in "
   "restaurants to curb unruly behavior and increase their revenues and profits. However, some "
   "restaurant proprietors in those areas claim there was a short-term negative impact on restaurant "
   "visitation in the beginning of last year. In contrast, the sales taxes paid by the restaurants "
   "in those provinces did not increase at a significantly higher rate than in other parts of "
   "Prohibitionland that did not have a ban.",
   "Which of the following, if true, provides the strongest support for the restaurant proprietors' "
   "claim against the ban?",
   "In the provinces that enacted the restrictions on alcoholic beverages last year, there was a short-term negative impact on restaurant visitation.",
   "The relative tax rate on food and beverages as compared to other consumer goods is irrelevant.",
   "A gradual decline in alcohol consumption over the past 20 years would show that, over time, any ban on alcohol would have an increasingly small impact on restaurant visitation.",
   "This answer calls the evidence into question by indicating that any apparent increase in sales taxes and, presumably, revenues for restaurants that have been operating under the restrictions enacted last year is irrelevant.",
   "Overall sales tax revenue did not increase at a higher rate in the provinces that enacted the restrictions on alcoholic beverages, which makes the cited evidence more compelling by ruling out the possibility of different growth rates in the different areas.",
   "D"),

# ── Q23 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_23",
   "Serious individual art collectors are usually discreet when making significant purchases or sales "
   "of major artworks. For instance, these collectors often place anonymous bids for major artworks "
   "at auction, while discreet in purchasing and selling their artwork, were relatively open about "
   "the artworks in their possession. Alternatively, one could weaken this claim using information "
   "that showed that serious art collectors possessed only a small fraction of the world's most "
   "valuable art.",
   "Which of the following, if true, does NOT weaken the conclusion above?",
   "That the value of a piece of art is subjective is irrelevant to the reasoning of the argument. This choice does not present any information that weakens the link between serious art collectors and the discretion they employ when purchasing or selling such artwork.",
   "That serious art collectors publicize their art shortly after purchasing it means that the whereabouts of their valuable art must be widely known.",
   "If museums own the vast majority of the world's valuable artwork, then the practices of serious individual art collectors are essentially irrelevant to the location of most of the world's valuable artwork.",
   "Since the majority of the world's valuable privately held artwork is owned by individuals who are not considered serious collectors, then the practices of serious art collectors are essentially irrelevant.",
   "That the collections of most serious individual art collectors are often displayed in public settings means that the whereabouts of most of the world's most valuable artwork are widely known.",
   "A"),

# ── Q24 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_24",
   "Last January, in an attempt to lower the number of traffic fatalities, the state legislature passed "
   "its new \"Click It or Ticket\" law. Under the new law, motorists can be cited for not wearing their "
   "seat belts, even in the absence of an additional driving infraction. Law enforcement groups and "
   "citizens groups are already protesting the new regulations, claiming that the new regulations will "
   "save countless additional lives by stating that the new regulations will save countless lives.",
   "Which of the following inferences is best supported by the above passage?",
   "Prior to the \"Click It or Ticket\" law, motorists could not be stopped simply for not wearing a seat belt.",
   "Search and seizure laws are never mentioned in the text. This answer choice is outside the scope of the argument.",
   "Laws in other states are never mentioned in the text. This answer choice is outside the scope of the argument.",
   "Though the text states that the new regulation might save countless additional lives, the effectiveness of the previous laws is never mentioned.",
   "The argument does not compare or otherwise evaluate the competency or authority of law enforcement groups and citizens groups.",
   "A"),

# ── Q25 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_25",
   "Calorie restriction, a diet high in nutrients but low in calories, has been shown to prolong the "
   "life of rats and mice by preventing diseases. In a study of moderately overweight humans, each "
   "who reduced their calorie intake by at least 25%, demonstrated decreases in insulin levels and "
   "body temperature. The study found that individuals with the greatest percentage decrease in their "
   "calorie intake demonstrated the greatest decrease in insulin levels and body temperature.",
   "The two boldface portions in the argument above are best described by which of the following?",
   "The first is the conclusion reached by the researchers; the second is a consideration in support of that assertion.",
   "The first is a premise that is challenged by the argument; the second is a situation that the author uses to contradict that premise.",
   "The first provides specific information about the effects of calorie restriction. In rats and mice, this diet is shown to prolong life by preventing diseases.",
   "The first describes the cause of a particular strategy; the second describes a more direct connection between this strategy and longevity.",
   "The first provides specific information about the effects of calorie restriction; the second directly illustrates how weight loss efforts of a certain group failed for exactly that reason.",
   "E"),

# ── Q26 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_26",
   "Recent research has indicated that married people are not only happier than unmarried people, but "
   "also healthier. This study has been widely reported by the media, which commentators have concluded "
   "that being married is good for one's health and attitude. To do so, the media commentators must "
   "reverse the causation: being happy and healthy makes a person more likely to marry.",
   "The conclusion of the media commentators depends on rejecting which of the following assumptions?",
   "The research compared married people to unmarried people. Neither the researchers nor the media commentators made any distinction between newlyweds and those who had been married a long time.",
   "The type of wedding is outside the scope of this argument. The research compared married people to unmarried people, but no distinction was made based upon the type of wedding.",
   "At first, this statement may seem necessary; after all, if the commentators conclude that marriage causes happiness, a lack of depression in married people would certainly support that conclusion.",
   "This statement eliminates the alternative interpretation of the research findings — that being happy and healthy makes a person more likely to marry.",
   "The research compared married people to unmarried people. Neither the researchers nor the media commentators made any distinction between harmonious marriages and combative marriages.",
   "D"),

# ── Q27 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_27",
   "For nearly a century, physiologists erroneously believed that a buildup of lactic acid in muscle "
   "tissue was responsible for the soreness that many people experience after strenuous exercise. The "
   "acid, they claimed, is the waste product produced by metabolic activity in the muscle and reaches "
   "\"threshold\" levels, causing soreness, when the muscle has depleted its oxygen supply. Researchers "
   "have recently discovered, however, that lactic acid is actually the fuel that powers muscular "
   "activity. Therefore, the cause of muscle soreness remains unknown.",
   "In the argument above, the portions in boldface play which of the following roles?",
   "The first is an assertion that the author accepts as true; the second is a consideration in support of that assertion.",
   "The first is an assertion that the author accepts as true; the second describes a situation that the author poses as contrary to that assertion.",
   "The first is a claim that the author argues against; the second is presented as evidence contrary to the first.",
   "The first is a claim that the author believes to be invalid; the second is additional evidence that the author uses to support his main point.",
   "The first is evidence that the author believes is no longer valid; the second is the author's main point.",
   "D"),

# ── Q29 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_29",
   "According to a recent study on financial roles, two thirds of all high school seniors say that "
   "they play significant financial responsibilities for their families. At the same time, a second "
   "study found that 80% of high school seniors have never opened a bank account, and of this 80%, "
   "one-third have bounced a check. The number of seniors that has bounced a check (one-third of 80%) "
   "is larger than the number of seniors who claim to contribute to their families financially.",
   "Which of the following conclusions can be properly drawn from the statements above?",
   "Although it might be true that schools would be wise to incorporate finance into their core curricula, this is an opinion that does not have to be based upon the given evidence.",
   "That one-third of high school seniors claim to have \"significant financial responsibilities\" to their families does not necessarily mean that the same students might earn money for their families.",
   "The first study states that one-third of all high school seniors have significant financial responsibilities to their families. The second study states that 80% of high school seniors have opened a bank account, and of this 80%, one-third have bounced a check.",
   "The passage states that certain high school seniors who contribute to the food, shelter, or clothing for themselves or their families \"rate themselves\" as having significant financial responsibilities.",
   "Any high school senior who contributes to the food, shelter, or clothing for themselves or their families has significant financial responsibilities. This does not mean that any high school senior who contributes to these categories has significant financial responsibilities.",
   "C"),

# ── Q30 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_30",
   "Federal law prohibits businesses from reimbursing any employees for the cost of owning and "
   "operating a private aircraft for business purposes. Most of the business activity of the United "
   "States is owned by small-and mid-size businesses. The planes owned by the companies discussed in "
   "the passage are owned by large companies, and flights taken in these planes are used for business "
   "purposes. Most mid-level executives on board are in full compliance with the law and their "
   "business associates on those flights.",
   "Which of the following can be most properly inferred from the statements above?",
   "The federal law in question costs businesses money as no evidence about the relative costs is given.",
   "This choice is an irrelevant comparison as the preferences of the executives are not the concern of the statements.",
   "This choice does not have to follow as there is no information given about the travel arrangements made by large companies.",
   "There is no information given about the travel arrangements of upper level executives and no reason to believe that those with the companies discussed do not comply with their companies' policies.",
   "If, as the statements indicate, the companies are in full compliance with this law, it must be true that those with the guidelines also are.",
   "E"),

# ── Q31 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_31",
   "Experts estimate that insurance companies' tardiness in paying doctors for legitimate medical "
   "claims results from billing errors amounting to 10% in overhead costs for physicians. Since dealing "
   "with these billing errors takes time and money and is clear that insurance companies do not have a "
   "significant economic incentive to delay claim payments to doctors.",
   "Which of the following, if true, most strengthens the conclusion above?",
   "While the fact that some doctors who submit accurate bills to insurance companies still receive tardy payments seems to indicate that there must be something other than doctors causing delayed payments, it fails to prove that the insurance company has an economic motive to deliberately delay payments.",
   "This choice compares the costs insurance companies must absorb due to incorrect bills to the costs physicians must absorb due to tardy payments from insurance companies.",
   "The argument is focused on the payment of legitimate claims; the rising proportion of illegitimate claims does not present a clear economic incentive for insurance companies to delay payments of legitimate claims.",
   "The types of billing errors made by doctors' offices does not establish any economic motive for insurance companies to delay payments to doctors.",
   "If insurance companies delay payments to doctors for legitimate medical claims, this results in a 10% increase in overhead costs for physicians. These costs ultimately result in higher fees that doctors charge to insurance companies. Insurance companies, in turn, raise the premiums that they charge consumers for health coverage. This choice states that the insurance companies increase their fees to consumers far more than the doctors increase their fees to insurance companies.",
   "E"),

# ── Q32 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_32",
   "Farmers in developing countries claim that the global price of wheat is low because American "
   "farmers produce too much of the grain. Because they have no incentive to manage their crops, "
   "since the U.S. government will buy any surplus wheat, American farmers routinely produce more "
   "wheat than the global market can absorb and the global price of wheat plummets. The question "
   "asks which choice weakens the claim that removing the American subsidy would cause the price of "
   "wheat to rise.",
   "Which of the following, if true, most weakens the argument?",
   "The fact that there are uses for wheat that is not eaten is irrelevant. This does not address the farmers' claims.",
   "That buyers of wheat can predict their needs in advance is irrelevant, because the text indicates that American farmers do not pay attention to actual market demand.",
   "The global market for soybeans suggests that other countries would modify their output to counterbalance any reduction on the part of the United States.",
   "The farmers assume that the sole cause of the wheat surplus is the United States. Other countries, such as Canada and Russia, are also likely to produce more wheat if the United States stops subsidizing its wheat, keeping prices constant rather than allowing them to rise.",
   "The price of another crop is largely irrelevant. Moreover, the fact that the price of sorghum, a non-subsidized crop, is lower tends to weaken, rather than strengthen, the claims of the farmers.",
   "D"),

# ── Q33 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_33",
   "Researchers studying the spread of the Black Plague in 16th-century England claim that certain "
   "people named after the plague by carrying a genetic mutation called Delta-32 prevented its "
   "carriers from contracting the plague. They support this claim by noting that a strikingly large "
   "percentage of descendants of plague survivors carry the mutation.",
   "The researchers' hypothesis is based on which of the following assumptions?",
   "The argument is specific to the relationship between Delta-32 and resistance to the plague. Other diseases are irrelevant.",
   "The argument is specific to the relationship between Delta-32 and resistance to the plague. Other diseases are irrelevant.",
   "If Delta-32 existed in its current form before the 16th century, the conclusion would still stand, so this choice is not a necessary assumption.",
   "The argument does not claim that Delta-32 prevents all bacteria-caused disease.",
   "The researchers claim that Delta-32 prevented its carriers from contracting the plague on the basis of its presence in descendants of plague survivors. But it is theoretically possible that these descendants carry the mutation Delta-32 because the plague mutated the genes of their ancestors. In order to claim that the mutation prevented the plague, you must assume that the plague did not cause the mutation Delta-32.",
   "E"),

# ── Q34 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_34",
   "The argument claims that wide dissemination of wireless access would be a practical way to meet "
   "urban needs, based on the evidence of its successful use in rural areas. The author must then "
   "assume that urban areas provide no additional problems for wireless use.",
   "Which of the following, if true, most strengthens the conclusion above?",
   "This choice confirms an assumption of the argument and thus strengthens the conclusion.",
   "This choice weakens the argument because it damages the assumption that urban areas pose no extra problems for wireless use.",
   "This choice is an irrelevant distinction. The argument concerned all three groups needing this service.",
   "This choice is irrelevant because no information is specifically about one group needing the service more than others.",
   "The suggestion that one group needs it more than the others is irrelevant to the conclusion.",
   "A"),

# ── Q35 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_35",
   "Studies have shown that people who keep daily diet records are far more successful at losing weight "
   "than people who don't keep track of what they eat. Researchers believe that many weight-loss "
   "efforts fail because people eat more calories than they intend to consume. One study followed a "
   "group of patients who reported that they could not lose weight when consuming only 1,200 calories a "
   "day. The study found that, on average, the dieters actually consumed 47% more than claimed.",
   "The two boldface portions in the argument above are best described by which of the following?",
   "The first boldface is not the conclusion; it is an observed fact. The second boldface is evidence that the researchers' conclusion is correct, but it is not evidence that the first boldface is correct.",
   "The first boldface is a fact that supports the researchers' theory, but it does not explain why the theory is correct — the other premises do so.",
   "The first boldface is a fact that supports the researchers' theory, but it does not illustrate the truth of that theory — the second boldface does.",
   "The first boldface (diet record = diet success) is a basis for the researchers' conclusion that many weight loss efforts fail because people eat more calories than they intended. The second boldface directly illustrates how weight loss efforts of a certain group failed for exactly that reason.",
   "The first boldface is a factual statement, not a theory. Furthermore, the first boldface supports the theory of the researchers; it is not something that they have disproved.",
   "D"),

# ── Q36 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_36",
   "The anticipated retirement of tens of thousands of baby boomers will create an unprecedented "
   "opportunity to provide jobs for unemployed young people. The argument's premise is that the "
   "retirement of the baby boomers will create shortages. The argument assumes the efficacy of its "
   "conclusion — in other words, that the conference will be effective in creating job opportunities.",
   "The argument above depends on which of the following assumptions?",
   "If anything, this choice strengthens the argument. If immigration does not provide a labor pool, it is more likely that a shortage will ensue.",
   "The argument assumes that it is feasible to affect employment patterns by government encouragement and/or action. If that assumption is denied, the weakness is weakened, as the conference would be pointless.",
   "This choice makes an irrelevant distinction. It does not matter if the best positions require skills, as long as the majority are available to the unskilled unemployed in question.",
   "Knowing that a significant proportion of baby boomers will not retire on schedule does not significantly weaken the argument. The argument relies on general estimates, not on exact numbers.",
   "If anything, this choice strengthens the argument. If these people are unaware of these opportunities, it would be positive to convene to plan how to reach them.",
   "B"),

# ── Q37 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_37",
   "The \"Doppler effect\" refers to the universal perceived change in the apparent pitch of a sound when "
   "the listener and the source of the sound are moving relative to one another. Specifically, whenever "
   "the distance between the listener and the source is increasing, the sound will be perceived by the "
   "listener as lower than its true pitch; whenever that distance is decreasing, the sound will be "
   "perceived as higher. If the above principles hold, which of the following should be observed as "
   "a westbound train is approached by an eastbound train blowing its horn?",
   "Which of the following should be observed as a westbound train is approached by an eastbound train blowing its horn?",
   "Passengers in the eastbound train do not hear the true pitch of the horn; passengers in the westbound train do.",
   "It is true that the westbound passengers hear the true pitch; the eastbound passengers, however, hear a sound that is higher than the true pitch.",
   "Passengers in the eastbound train do not hear the true pitch of the horn of the horn; passengers in the westbound train do.",
   "Westbound passengers do hear the true pitch of the sound. Eastbound passengers do hear a sound that is higher in pitch than the true sound.",
   "It is true that eastbound passengers hear a sound that is higher than the true pitch; the westbound passengers, however, hear the true pitch.",
   "D"),

# ── Q38 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_38",
   "The popular notion that a tree's age can be determined by counting the number of internal rings in "
   "a trunk is fact. In the 18th and 19th centuries, it was believed by many in coastal cities of the "
   "United States that the outermost layers of wood of the Brazilian jatoba tree often peel away when "
   "the temperature exceeds 95 degrees Fahrenheit, leaving the tree with fewer rings than it would "
   "otherwise have. If only the temperature factor is known, the rings will be a reliable measure only "
   "if the temperature never exceeds 95 degrees Fahrenheit.",
   "Which of the following conclusions can be made on the basis of the information in the passage?",
   "The argument says nothing about precipitation. This answer choice is out of scope since it would require a number of other assumptions to make it relevant to the argument's conclusion.",
   "Whether other trees share this feature is irrelevant; the argument focuses only on the Brazilian ash.",
   "If it is the case that once above 95 degrees leads to one ring lost, then it might still be possible to predict the tree's age, as long as it is known on how many days the temperature exceeded 95 degrees.",
   "The thickness of the rings is irrelevant.",
   "The conclusion is that the rings will be a reliable measure only if the temperature never exceeds 95 degrees. This is only true if there is no way to predict how many rings would be lost when the temperature does exceed 95 degrees.",
   "E"),

# ── Q39 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_39",
   "Celiac disease results from an inability of the digestive tract, specifically the small intestine, "
   "to tolerate gluten, a protein found in wheat, barley, and rye. The body's immune system attacks "
   "the intestinal lining, causing serious damage to the intestine. People who suffer from celiac "
   "disease must eliminate gluten from their diets. The symptoms of the disease include cramps, "
   "bloating, and anemia.",
   "If the statements above are true, which of the following can be made on the basis of the statements above?",
   "Anyone who has celiac disease will experience anemia.",
   "People experiencing abdominal cramps, bloating, and anemia have celiac disease.",
   "Eliminating gluten from one's diet will cure celiac disease.",
   "Celiac disease can be found only in grains.",
   "It is not known whether gluten is found only in grains. It may exist in other foods as well.",
   "E"),

# ── Q40 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_40",
   "All languages that have only three basic color terms describe the same six colors using those "
   "three terms: black, white, red, green, and blue. In addition, all languages that have only three "
   "color terms describe the same six colors. Among colored objects, the mind recognizes differences "
   "among colored objects, and therefore culture does not influence color perception.",
   "Which of the following, if true, most strongly weakens the argument above?",
   "While language may affect how the mind distinguishes colored objects, it may have no effect on the conclusion.",
   "Irrelevant. In fact, this statement may slightly strengthen the argument: if every language permits speakers to see 6 color variations, then it might be argued that human color perception is independent of language.",
   "Irrelevant. The term red may encompass both red and yellow, but that doesn't mean that speakers of the language cannot see the difference between red and yellow.",
   "If speakers of languages with a blue-green distinction refer to the sky or tree leaves to clarify their meaning, then they obviously see a difference between the sky and tree leaves.",
   "If Tarahumara speakers are less able to identify differences between blue and green objects than Spanish speakers, then it can be argued that the blue-green distinction in the Tarahumara language influences how Tarahumara speakers actually perceive colors.",
   "E"),

# ── Q43 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_43",
   "If it exists elsewhere in the solar system, scientists suspect it would most likely be on Europa, "
   "an icy moon of Jupiter. However, NASA recently scrapped an unmanned science mission to Europa and "
   "reassigned most of the employees who had been working on the project to a different project; it "
   "concerns landing an astronaut on Mars. Polls show that Americans are far more fascinated by space "
   "travel than by scientific research. In response, NASA's critics argue that the decision to scrap "
   "the mission was purely a public relations move designed to appeal to the public's fascination with "
   "space travel.",
   "Which of the following, if true, most strongly weakens the argument that the critics are that NASA's decision was a public relations move?",
   "The conclusion is based on the critics' assumption of causation, and this choice fails to address the issue of the motivations underlying NASA's decision-making process.",
   "Weakens. If NASA consistently manages its budget, it is necessary to keep public interest high.",
   "Irrelevant. This statement differentiates between the opinions of some scientists and the opinions of others, but sheds no light on the motivations behind NASA's decisions.",
   "The Tokyo telescope will provide the information that NASA would have obtained from the mission, making the mission unnecessary.",
   "Irrelevant. The conclusion concerns NASA's motivations; this statement is about the motivations of American citizens.",
   "D"),

# ── Q48 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_48",
   "In a recent poll, 71% of respondents reported that they cast votes in the most recent national "
   "election. Voting records show, however, that only 60% of eligible voters actually voted in that "
   "election. An explanation of a GRE discrepancy explains why the apparent conflict does not apply.",
   "Which of the following, if true, most helps to explain the discrepancy between the poll results "
   "and the actual voting percentages?",
   "If the margin of error is ± 5%, then the 71% figure could be as low as 66% (or as high as 76%). This accounts for less than half of the discrepancy between 71% and 60%.",
   "This choice does not address the stated discrepancy between the percentage of voters who said that they voted and the percentage of voters who actually did vote.",
   "One explanation for the discrepancy between these two results is the possibility that people who do vote will respond to surveys at a higher rate than people who do not vote; in other words, people who do vote are overrepresented in the survey's results.",
   "While this may be true, the poll did not ask people if they intended to vote; rather, it asked people if they had already voted in a past election.",
   "While this may account for some percentage of the discrepancy, the numerical data is not sufficient to explain the entire discrepancy.",
   "C"),

# ── Q49 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_49",
   "Scientists recently documented that influenza spreads around the world more efficiently in the "
   "modern era due to commercial air travel. Flu symptoms are severe enough that it would likely "
   "cancel or reschedule air travel if an infected person is on a plane. If the disease spreads "
   "before symptoms appear, then an infected person could travel across the globe before the "
   "first symptoms appear. Health officials in Country X have therefore proposed that all air "
   "travelers be required to receive flu vaccinations before boarding planes.",
   "Which of the following, if true, best supports the proposed preventive measure of mandatory "
   "flu vaccinations before air travel?",
   "The passage states that the infection can be spread by coughing. The flu virus, therefore, can reach the other passengers in the 'closely packed environment' before it enters any filters that might kill the virus.",
   "Vaccines provide significant protection against developing the flu virus (not 100% protection, but the question concerns minimizing the impact of air travel, not eliminating it entirely). If all passengers are vaccinated against the flu, many of those who otherwise would have developed the disease will not, and therefore, will not spread it to others.",
   "You can contract the virus and subsequently spread it; the mentioned populations are 'especially vulnerable' to it.",
   "The passage states that the infection can be spread by coughing; while it may be true that the virus can also spread via direct contact, this information is not stated in the passage.",
   "The passage states that people who develop symptoms before travel begins would likely not make the trip; banning those with visible symptoms would not address the larger danger, since there are not that many people in this category.",
   "B"),

# ── Q52 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_52",
   "Network executives have alleged that television viewership is decreasing due to the availability "
   "of alternative media, such as the internet and mobile devices. However, the cable industry argues "
   "that networks can actually increase their revenue through higher advertising rates, due to the fact "
   "that a larger audience has been lured to television by alternative media devices lead their users "
   "to watch more television.",
   "The two boldface portions in the argument above are best described by which of the following?",
   "The first boldface portion does weigh against the argument, but it is a prediction, rather than 'an inevitable trend'; the second boldface supports the argument but is not the conclusion itself.",
   "The argument about potential increased network revenue is contrary to the first boldface's prediction of shrinking audiences and falling revenue; the argument indeed depends upon the second bold-face assertion that users of alternative devices will actually watch more hours of television.",
   "The first boldface portion clarifies the argument, rather than the second; the second boldface would suggest that the argument is sound, rather than clarifying it.",
   "The technology executives do not accept the prediction of the network executives; the second boldface contradicts that prediction and is not a consequence of it.",
   "The first boldface portion does not use an analogy; the second is in agreement with, not opposition to, the argument.",
   "B"),

# ── Q55 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_55",
   "Most cable television companies currently require customers to subscribe to packages of channels, "
   "rather than allowing à la carte pricing. Consumer groups claim that à la carte pricing will reduce "
   "consumer costs, while the cable television industry claims that the current package pricing structure "
   "is most cost effective for consumers. If the goal is to reduce costs for cable television consumers, "
   "it is critical to determine whether à la carte pricing is likely to save consumers money.",
   "Which of the following would be most important to determine before deciding whether to require "
   "à la carte pricing?",
   "According to the argument, the decision revolves around the costs to consumers, not the number of channels available to them. If there were some pricing consequences as a result of this loss of diversity, the point might be relevant, but no such information is given.",
   "According to the argument, the decision is based only on the costs to consumers, not the advertising profits of the cable television companies.",
   "If consumers would not choose to order all of the channels they currently watch and enjoy as part of a package subscription, then the cable television industry's claim that à la carte pricing would be more expensive is suspect. If many consumers only watch and pay for a few of their favorite channels, à la carte pricing is likely to save consumers money.",
   "According to the argument, the decision concerns only the costs to consumers, not the number of consumers who subscribe to cable. If there were some pricing consequences as a result of a loss of subscribers, the point might be relevant, but no such information is given.",
   "Irrelevant. According to the argument, the decision is based only on the basis of technical specifications for whether cable set-top boxes can handle à la carte pricing.",
   "C"),

# ── Q56 ─────────────────────────────────────────────────────────────────────
cr("CR5LB_56",
   "A certain pharmaceutical firm recently developed a new medicine, Dendazine, that provides highly "
   "effective treatment of severe stomach disorders that were previously thought untreatable. However, "
   "the company spent nearly $5 billion in research and to develop the new drug, then the company can "
   "also agree to sell Dendazine at a price that is at least five times greater than its variable costs "
   "to break even. Yet company management claims that Dendazine will soon become the most profitable "
   "drug in the firm's history.",
   "Which of the following best reconciles the company management's evidence about the expenditures "
   "associated with the development of Dendazine?",
   "The pharmaceutical firm expects patent protection for Dendazine drugs under patent protection. The company can also agree to sell products that are approximately 10 times their variable costs.",
   "While this choice supports the idea that Dendazine will sell well, it does not specifically support the contention that the drug will be profitable in the face of unusually high costs.",
   "Although this choice supports the idea that Dendazine will sell well, it does not specifically support the contention that the drug will be profitable in the face of unusually high costs.",
   "Although this choice supports the idea that Dendazine will be the primary, if not only, treatment for this market niche, it does not support the contention that the drug will be profitable in the face of unusually high costs.",
   "Although this choice supports the idea that the market for Dendazine is very large and will generate great revenues, it does not specifically support the contention that the drug will be profitable in the face of unusually high costs.",
   "A"),

]


def main():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    if "verbal" not in data:
        data["verbal"] = []

    existing_ids = {q["id"] for q in data["verbal"]}
    new_qs = [q for q in questions if q["id"] not in existing_ids]
    skipped = len(questions) - len(new_qs)

    data["verbal"].extend(new_qs)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Added: {len(new_qs)}  |  Skipped(dup): {skipped}")
    print(f"Total verbal: {len(data['verbal'])}")
    cr_count = sum(1 for q in data["verbal"] if q["type"] == "critical_reasoning")
    print(f"CR questions: {cr_count}")


if __name__ == "__main__":
    main()
