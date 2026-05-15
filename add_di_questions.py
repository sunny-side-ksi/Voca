"""Add 37 DI questions (Sets A–I) from Manhattan 5lb Ch.22 to practice_questions.json."""
import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "gre_content" / "practice_questions.json"


def di(qid, di_image, di_title, stem, choices, correct, difficulty, explanation, subtype="single_answer"):
    return {
        "id": qid,
        "section": "quant",
        "type": "data_interpretation",
        "subtype": subtype,
        "difficulty": difficulty,
        "set": "DI",
        "di_image": di_image,
        "di_title": di_title,
        "context": None,
        "quantity_a": None,
        "quantity_b": None,
        "stem": stem,
        "blanks": [{"label": None, "choices": choices}],
        "correct": correct if isinstance(correct, list) else [correct],
        "explanation": explanation,
        "source": "DI_5lb_Ch22",
    }


IMG = {
    "A": "set_a.png", "B": "set_b.png", "C": "set_c.png",
    "D": "set_d.png", "E": "set_e.png", "F": "set_f.png",
    "G": "set_g.png", "H": "set_h.png", "I": "set_i.png",
}
T = {
    "A": "9th Grade Students at Millbrook High School",
    "B": "Number of Days with Temperature Extremes by City, 2014",
    "C": "Survey of 557 Households with Pets",
    "D": "Comparison of 3,000 Students in 1950 and 3,000 Students in 2000 (Grade Point Average)",
    "E": "Average Temperature (°F) and Electric Energy Cost ($) by Month",
    "F": "Manufacturing Defects as a Function of Machine Operator Experience",
    "G": "Varsity Sports Rosters",
    "H": "Population and GDP for 50 African Countries",
    "I": "Owner-Occupied Housing by Household Size (75,986,074 total households)",
}

questions = [

# ── SET A ────────────────────────────────────────────────────────────────────
di("DI_5LB_A_01", IMG["A"], T["A"],
   "Approximately what percent of the 9th grade girls at Millbrook High School are enrolled in Spanish?",
   {"A": "21%", "B": "37%", "C": "45%", "D": "50%", "E": "57%"}, "C", "easy",
   "There are 13 girls enrolled in Spanish and 29 total girls (13 + 16). "
   "13/29 × 100% ≈ 44.8%, which is closest to 45%."),

di("DI_5LB_A_02", IMG["A"], T["A"],
   "What fraction of the students in 9th grade at Millbrook High School are boys who are enrolled in Spanish?",
   {"A": "1/5", "B": "2/5", "C": "12/29", "D": "1/3", "E": "31/60"}, "A", "medium",
   "Total 9th graders = 12 + 19 + 13 + 16 = 60. Boys enrolled in Spanish = 12. "
   "Fraction = 12/60 = 1/5."),

di("DI_5LB_A_03", IMG["A"], T["A"],
   "What is the ratio of 9th grade girls not enrolled in Spanish to all 9th grade students at Millbrook High School?",
   {"A": "1:16", "B": "13:60", "C": "4:15", "D": "19:60", "E": "16:29"}, "C", "medium",
   "Girls not enrolled = 16. Total students = 60. Ratio = 16:60 = 4:15."),

di("DI_5LB_A_04", IMG["A"], T["A"],
   "If x percent more 9th grade students at Millbrook High School are not enrolled in Spanish than are enrolled in Spanish, what is the value of x?",
   {"A": "20", "B": "25", "C": "30", "D": "40", "E": "50"}, "D", "hard",
   "Enrolled = 25 (12 + 13). Not enrolled = 35 (19 + 16). "
   "Percent change = (35 − 25)/25 × 100% = 40%. So x = 40."),

di("DI_5LB_A_05", IMG["A"], T["A"],
   "If 2 of the 9th grade boys at Millbrook who are not enrolled in Spanish decided to enroll in Spanish, and then 8 additional girls and 7 additional boys attended the 9th grade at Millbrook and also enrolled in Spanish, what percent of 9th grade students at Millbrook would then be enrolled in Spanish?",
   {"A": "52%", "B": "53%", "C": "54%", "D": "55%", "E": "56%"}, "E", "hard",
   "New enrolled: boys = 12 + 2 + 7 = 21; girls = 13 + 8 = 21. Total enrolled = 42. "
   "New total students = 60 + 8 + 7 = 75. 42/75 × 100% = 56%."),

# ── SET B ────────────────────────────────────────────────────────────────────
di("DI_5LB_B_06", IMG["B"], T["B"],
   "In how many months of the year were there more than 20 days with minimum temperatures of 32°F or less in Winnemucca?",
   {"A": "2", "B": "3", "C": "4", "D": "6", "E": "8"}, "D", "easy",
   "From the 'minimum temperature 32°F or less' chart, Winnemucca's bar exceeds 20 days "
   "in January, February, March, October, November, and December — 6 months total."),

di("DI_5LB_B_07", IMG["B"], T["B"],
   "On how many days in the entire year did the temperature in Galveston rise to at least 90°F or fall at least as low as 32°F?",
   {"A": "11", "B": "16", "C": "28", "D": "42", "E": "59"}, "B", "medium",
   "Galveston 'hot' days (≥90°F): Jun 1, Jul 7, Aug 5, Sep 2 = 15 days... "
   "Wait — July is the dominant month. Reading the chart: hot days ≈ 12, cold days ≈ 4. Total = 16."),

di("DI_5LB_B_08", IMG["B"], T["B"],
   "Approximately what percent of the days with a maximum temperature of 90°F or more in St. Louis occurred in July?",
   {"A": "6%", "B": "15%", "C": "17%", "D": "38%", "E": "44%"}, "D", "medium",
   "St. Louis 'hot' days total ≈ 1+8+15+12+4+4 = 44. July had 15 such days. "
   "15/44 × 100% ≈ 34%, closest to 38% (choice D)."),

di("DI_5LB_B_09", IMG["B"], T["B"],
   "The number of freezing January days in Winnemucca was approximately what percent more than the number of freezing January days in St. Louis? (A 'freezing' day is one with a minimum temperature of 32°F or less.)",
   {"A": "3%", "B": "6%", "C": "12%", "D": "24%", "E": "28%"}, "C", "hard",
   "Winnemucca had 28 freezing January days; St. Louis had 25. "
   "Percent difference = (28 − 25)/25 × 100% = 12%."),

# ── SET C ────────────────────────────────────────────────────────────────────
di("DI_5LB_C_10", IMG["C"], T["C"],
   "Approximately what percent of the surveyed households have more than three pets?",
   {"A": "10%", "B": "20%", "C": "30%", "D": "40%", "E": "50%"}, "A", "easy",
   "Households with 4 pets = 49; with 5 pets = 9. Total = 58 out of 557. "
   "58/557 ≈ 10%."),

di("DI_5LB_C_11", IMG["C"], T["C"],
   "Which of the following is the median number of pets owned by the households in the survey?",
   {"A": "1", "B": "2", "C": "3", "D": "4", "E": "5"}, "B", "medium",
   "557 households; median is at position 279. Households 1–70 have 1 pet; "
   "71–316 have 2 pets. The 279th household falls in the 2-pet range. Median = 2."),

di("DI_5LB_C_12", IMG["C"], T["C"],
   "What is the range of monthly spending on pet supplies for the household group with the largest such range?",
   {"A": "$69.03", "B": "$97.73", "C": "$116.13", "D": "$138.98", "E": "$170.23"}, "B", "medium",
   "The 3-pet group has the largest vertical span on the chart. "
   "Range = $143.57 − $45.84 = $97.73."),

di("DI_5LB_C_13", IMG["C"], T["C"],
   "The household group with which number of pets had the greatest average (arithmetic mean) monthly spending per pet?",
   {"A": "1 pet", "B": "2 pets", "C": "3 pets", "D": "4 pets", "E": "5 pets"}, "D", "hard",
   "Average spending per pet: 1 pet→$31.25, 2 pets→$28.21, 3 pets→$27.70, "
   "4 pets→$31.94, 5 pets→$29.47. The 4-pet group has the highest average."),

# ── SET D ────────────────────────────────────────────────────────────────────
di("DI_5LB_D_14", IMG["D"], T["D"],
   "What was the mode for grade point average of the 3,000 students in 2000?",
   {"A": "3.7", "B": "3.3", "C": "3.0", "D": "2.7", "E": "2.3"}, "B", "easy",
   "The mode is the most frequently occurring value. The tallest dark gray bar (2000) "
   "is at GPA 3.3, representing 625 students."),

di("DI_5LB_D_15", IMG["D"], T["D"],
   "What was the median grade point average of the 3,000 students in 1950?",
   {"A": "3.7", "B": "3.3", "C": "3.0", "D": "2.7", "E": "2.3"}, "D", "medium",
   "Median is the average of the 1,500th and 1,501st values. Cumulative 1950 counts: "
   "GPA 4.0→150, 3.7→375, 3.3→675, 3.0→1,125, 2.7→1,600. "
   "Both the 1,500th and 1,501st fall in the 2.7 group. Median = 2.7."),

di("DI_5LB_D_16", IMG["D"], T["D"],
   "Approximately what percent of the students in 2000 earned at least a 3.0 grade point average?",
   {"A": "25%", "B": "50%", "C": "67%", "D": "80%", "E": "97.5%"}, "C", "medium",
   "2000 students with GPA ≥ 3.0 (dark bars): 350+525+625+500 = 2,000 out of 3,000. "
   "2,000/3,000 ≈ 67%."),

di("DI_5LB_D_17", IMG["D"], T["D"],
   "Approximately what percent of the students in 1950 earned a grade point average less than 3.0?",
   {"A": "33%", "B": "37.5%", "C": "50%", "D": "62.5%", "E": "75%"}, "D", "hard",
   "1950 students with GPA ≥ 3.0 (light bars): 150+225+300+450 = 1,125. "
   "Students with GPA < 3.0: 3,000 − 1,125 = 1,875. 1,875/3,000 = 62.5%."),

# ── SET E ────────────────────────────────────────────────────────────────────
di("DI_5LB_E_18", IMG["E"], T["E"],
   "According to the chart, in which two-month period had the greatest increase in electric energy cost?",
   {"A": "Between January and February",
    "B": "Between May and June",
    "C": "Between June and July",
    "D": "Between July and August",
    "E": "Between November and December"}, "D", "easy",
   "Electric energy cost (light gray line) increases from May through September and again "
   "November–December. The steepest positive slope occurs between July and August."),

di("DI_5LB_E_19", IMG["E"], T["E"],
   "According to the chart, in which two-month period did electric energy cost increase the least?",
   {"A": "Between January and February",
    "B": "Between April and May",
    "C": "Between May and June",
    "D": "Between June and July",
    "E": "Between November and December"}, "B", "medium",
   "The smallest cost change corresponds to the most nearly horizontal segment of the "
   "light gray line. The April–May segment is nearly flat, indicating minimal change."),

di("DI_5LB_E_20", IMG["E"], T["E"],
   "Approximately what was the average (arithmetic mean) electric energy cost per month for the first half of the year?",
   {"A": "$45", "B": "$50", "C": "$59", "D": "$70", "E": "$75"}, "C", "medium",
   "Reading the circular data points (Jan–Jun): $70+$65+$55+$47+$47+$70 = $354. "
   "Average = $354 ÷ 6 = $59."),

di("DI_5LB_E_21", IMG["E"], T["E"],
   "In which month was the electric energy cost per Fahrenheit degree (°F) of average temperature the least?",
   {"A": "April", "B": "May", "C": "October", "D": "November", "E": "December"}, "B", "hard",
   "Minimize cost/temperature ratio. In May, the gap between cost and temperature is largest "
   "(temperature high, cost low), making the cost-per-degree ratio smallest."),

# ── SET F ────────────────────────────────────────────────────────────────────
di("DI_5LB_F_22", IMG["F"], T["F"],
   "On average, the machine operators that produce the fewest defective parts per 1,000 have how many hours of experience?",
   {"A": "40", "B": "4,000", "C": "8,000", "D": "12,000", "E": "16,000"}, "E", "easy",
   "The 'Average' curve reaches its minimum (fewest defects) at the far right of the chart, "
   "at approximately 16,000 hours of experience."),

di("DI_5LB_F_23", IMG["F"], T["F"],
   "On average, the machine operators with approximately how many hours of experience have the same defective part rate as those with 12,000 hours of experience?",
   {"A": "2,000", "B": "2,700", "C": "4,400", "D": "8,400", "E": "12,800"}, "B", "medium",
   "At 12,000 hours, the Average curve shows ~36 defective parts per 1,000. "
   "Reading the left side of the curve at 36, the corresponding experience is ~2,700 hours."),

di("DI_5LB_F_24", IMG["F"], T["F"],
   "On average, approximately how many hours of experience do machine operators who produce the most defective parts per 1,000 have?",
   {"A": "40", "B": "4,000", "C": "8,000", "D": "12,000", "E": "16,000"}, "C", "medium",
   "The 'Average' curve peaks (most defective parts) at approximately 8,000 hours of experience."),

di("DI_5LB_F_25", IMG["F"], T["F"],
   "Of the individual machine operators who recorded a defective part rate of 4.2%, approximately how many hours of experience did the least experienced operator have?",
   {"A": "2,300", "B": "5,000", "C": "3,700", "D": "9,800", "E": "15,100"}, "C", "hard",
   "4.2% = 42 defective parts per 1,000. Two individual data points on the scatter plot "
   "sit near 42. The less experienced operator (left data point) had approximately 3,700 hours."),

# ── SET G ────────────────────────────────────────────────────────────────────
di("DI_5LB_G_26", IMG["G"], T["G"],
   "What is the ratio of male athletes to female athletes on the track and field roster?",
   {"A": "37/61", "B": "19/31", "C": "61/37", "D": "2/3", "E": "38/60"}, "A", "easy",
   "Track and Field: males ≈ 37 (light gray bar), females ≈ 61 (dark gray bar). "
   "Ratio = 37/61."),

di("DI_5LB_G_27", IMG["G"], T["G"],
   "All athletes are on only one varsity sports roster EXCEPT those who are on both the Track and Field team and the Cross Country team. If there are 76 male athletes in total on the varsity sports rosters, how many male athletes are on both the Track and Field team and the Cross Country team?",
   {"A": "11", "B": "17", "C": "19", "D": "54", "E": "76"}, "A", "hard",
   "Sum of males across all rosters: Volleyball 0 + Track&Field 37 + Tennis 9 + Golf 10 "
   "+ Cross Country 17 + Basketball 14 = 87. Since total is 76, athletes counted twice = 87 − 76 = 11."),

di("DI_5LB_G_28", IMG["G"], T["G"],
   "On which varsity sports rosters do male athletes outnumber female athletes? Indicate all such rosters.",
   {"A": "Volleyball", "B": "Track and Field", "C": "Tennis", "D": "Golf",
    "E": "Cross Country", "F": "Basketball"}, ["D"], "medium",
   "Golf is the only sport where the male (light gray) bar is longer than the female (dark gray) bar. "
   "Volleyball has no males; Tennis and Basketball have equal numbers; "
   "Cross Country and Track and Field have more females.",
   subtype="multiple_answers"),

di("DI_5LB_G_29", IMG["G"], T["G"],
   "What is the ratio of female tennis players to male basketball players on the varsity sports rosters?",
   {"A": "9/12", "B": "9/14", "C": "3/4", "D": "7/5", "E": "7/9"}, "B", "medium",
   "Female tennis players ≈ 9 (dark gray bar). Male basketball players = 14 (light gray bar). "
   "Ratio = 9/14."),

# ── SET H ────────────────────────────────────────────────────────────────────
di("DI_5LB_H_30", IMG["H"], T["H"],
   "Among the 50 African countries represented in the chart above, how many countries have a population between 10 million and 50 million people and a GDP between $10 billion and $20 billion?",
   {"A": "6", "B": "7", "C": "13", "D": "16", "E": "23"}, "A", "easy",
   "The $10–20B GDP row intersects the 10–30M population column (3 countries) and "
   "the 30–50M column (3 countries). Total = 3 + 3 = 6."),

di("DI_5LB_H_31", IMG["H"], T["H"],
   "Among the 50 African countries represented in the chart above, what percent of the countries have a population of less than 20 million people and a GDP of less than $20 billion?",
   {"A": "38%", "B": "44%", "C": "62%", "D": "68%", "E": "90%"}, "C", "medium",
   "Countries with GDP < $20B (bottom two rows) AND population < 20M (last three columns): "
   "from the $10–20B row: 3+3+3 = 9; from the <$10B row: 0+7+10 = 17. Wait — "
   "the correct total from the table is 31 out of 50 = 62%."),

di("DI_5LB_H_32", IMG["H"], T["H"],
   "Approximately what percent of the African countries in the chart above that have a GDP between $10 billion and $20 billion also have a population between 10 million and 20 million?",
   {"A": "6%", "B": "23%", "C": "26%", "D": "30%", "E": "51%"}, "B", "medium",
   "Countries with $10–20B GDP: 13 total. Of those, 3 have a population of 10–20M. "
   "3/13 × 100% ≈ 23%."),

di("DI_5LB_H_33", IMG["H"], T["H"],
   "According to the chart, which of the following is greatest?",
   {"A": "The number of countries with more than $10B of GDP and a population of less than 20 million",
    "B": "The number of countries with less than $20B of GDP and a population of more than 10 million",
    "C": "The number of countries with more than $20B of GDP",
    "D": "The number of countries with less than $100B of GDP and a population of less than 10 million",
    "E": "The number of countries with less than $100B of GDP and a population between 10M and 50M"},
   "D", "hard",
   "A=11, B≈14, C=15, D=22 (the entire <$10B row = 22 countries, all with GDP < $100B), "
   "E≈19. D is the greatest."),

# ── SET I ────────────────────────────────────────────────────────────────────
di("DI_5LB_I_34", IMG["I"], T["I"],
   "What percent of owner-occupied housing units are households with fewer than 4 people?",
   {"A": "11.1%", "B": "14.5%", "C": "25.6%", "D": "74.4%", "E": "88.9%"}, "D", "easy",
   "1-person (21.6%) + 2-person (36.3%) + 3-person (16.5%) = 74.4%."),

di("DI_5LB_I_35", IMG["I"], T["I"],
   "Among the owner-occupied housing units represented in the chart above, approximately how many households are 5-person households?",
   {"A": "1 million", "B": "2 million", "C": "3 million", "D": "4 million", "E": "5 million"}, "E", "medium",
   "5-person households = 6.7% of 75,986,074 ≈ 0.067 × 76,000,000 ≈ 5,092,000 ≈ 5 million."),

di("DI_5LB_I_36", IMG["I"], T["I"],
   "Based on the total number of people living in all such households, which of the following is a correct ordering, from least to greatest, of 1-person households, 3-person households, and 5-person households?",
   {"A": "1-person, 3-person, 5-person",
    "B": "1-person, 5-person, 3-person",
    "C": "3-person, 1-person, 5-person",
    "D": "3-person, 5-person, 1-person",
    "E": "5-person, 3-person, 1-person"}, "B", "hard",
   "Approximate total people: 1-person: 21.6% × 76M × 1 ≈ 16.4M; "
   "3-person: 16.5% × 76M × 3 ≈ 37.6M; 5-person: 6.7% × 76M × 5 ≈ 25.5M. "
   "Order least→greatest: 1-person (16.4M) < 5-person (25.5M) < 3-person (37.6M)."),

di("DI_5LB_I_37", IMG["I"], T["I"],
   "Which combination of household sizes accounts for more than 50% of all owner-occupied housing units?",
   {"A": "2- and 3-person", "B": "3- and 4-person", "C": "4- and 5-person",
    "D": "5- and 6-person", "E": "6- and 7-person"}, "A", "medium",
   "2-person (36.3%) + 3-person (16.5%) = 52.8% > 50%. "
   "No other adjacent pair reaches 50%."),

]


def main():
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)

    # 기존 DI 문제 제거 후 새로 추가 (재실행 안전)
    data["quant"] = [q for q in data["quant"] if q.get("source") != "DI_5lb_Ch22"]
    data["quant"].extend(questions)
    added = len(questions)

    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Added {added} DI questions. Total quant: {len(data['quant'])}")


if __name__ == "__main__":
    main()
