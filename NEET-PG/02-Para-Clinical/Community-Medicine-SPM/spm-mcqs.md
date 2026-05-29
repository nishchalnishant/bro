# Community Medicine / SPM — High-Yield MCQs

> 30 questions | +4/−1 marking | NEET PG pattern

---

## EPIDEMIOLOGY CONCEPTS (Q1–Q5)

**Q1. A researcher follows 1,000 smokers and 1,000 non-smokers for 10 years to compare the incidence of lung cancer. This study design is:**
- A) Case-control study
- B) Prospective cohort study
- C) Randomized controlled trial
- D) Cross-sectional study

<details>
<summary>Answer</summary>

**Correct: B**

A prospective cohort study follows disease-free individuals with different exposures forward in time to measure incidence; it directly calculates relative risk (RR). Case-control studies start with cases and controls and look backward at exposure (calculates odds ratio). RCTs involve randomization and intervention. Cross-sectional studies measure prevalence at a single point in time; best measure is prevalence ratio.

</details>

---

**Q2. During a food poisoning outbreak at a wedding, 80 of 200 guests who ate chicken developed gastroenteritis. Of 50 guests who did not eat chicken, 5 developed gastroenteritis. The attack rate in those who ate chicken is:**
- A) 5%
- B) 10%
- C) 40%
- D) 80%

<details>
<summary>Answer</summary>

**Correct: C**

Attack rate = (Number of new cases among exposed / Total number exposed) × 100 = (80/200) × 100 = 40%. Attack rate is a form of incidence used in outbreak investigations over a defined exposure period. The attack rate in unexposed = (5/50) × 100 = 10%. Relative risk = 40%/10% = 4. Secondary attack rate measures spread within households after a primary case.

</details>

---

**Q3. Prevalence of diabetes in a community survey is 10%. A new rapid test has 90% sensitivity and 80% specificity. The positive predictive value (PPV) of this test in this population is approximately:**
- A) 33%
- B) 50%
- C) 75%
- D) 90%

<details>
<summary>Answer</summary>

**Correct: A**

PPV = TP/(TP+FP). In 1,000 people: 100 have DM (prevalence 10%), 900 don't. True positives = 100 × 0.90 = 90. False positives = 900 × 0.20 = 180. PPV = 90/(90+180) = 90/270 ≈ 33%. PPV decreases as prevalence decreases — critical concept. Sensitivity = 90% (detects disease). Specificity = 80% (correctly rules out disease). NPV improves with lower prevalence.

</details>

---

**Q4. The best measure of association in a case-control study is:**
- A) Relative risk
- B) Odds ratio
- C) Attributable risk
- D) Population attributable risk

<details>
<summary>Answer</summary>

**Correct: B**

Odds ratio (OR) is the measure of association used in case-control studies because incidence cannot be directly calculated (study starts from outcome, not exposure). OR = (ad)/(bc) in a 2×2 table. When disease is rare, OR approximates relative risk. Relative risk is calculated in cohort studies. Attributable risk (risk difference) is calculated from cohort studies. OR is also used in logistic regression.

</details>

---

**Q5. Secondary attack rate (SAR) is best defined as:**
- A) Number of new cases in the total population during an outbreak
- B) Number of cases among contacts of primary cases within the incubation period
- C) Number of cases per 1,000 population per year
- D) Proportion of exposed individuals who develop disease

<details>
<summary>Answer</summary>

**Correct: B**

Secondary attack rate = (Number of new cases among close contacts of primary case / Total susceptible contacts) × 100, measured within the maximum incubation period. SAR measures communicability/infectivity of a disease within a household or closed group. High SAR indicates highly contagious disease (e.g., measles SAR ~90%). Attack rate measures disease frequency during a defined exposure event.

</details>

---

## BIOSTATISTICS (Q6–Q10)

**Q6. A study compares mean blood pressure in three groups receiving three different antihypertensives. The appropriate statistical test is:**
- A) Student's unpaired t-test
- B) Paired t-test
- C) One-way ANOVA (Analysis of Variance)
- D) Chi-square test

<details>
<summary>Answer</summary>

**Correct: C**

One-way ANOVA compares means of three or more independent groups with one independent variable (treatment type). Student's unpaired t-test compares means of exactly two independent groups. Paired t-test compares means before and after in the same group. Chi-square test compares proportions/frequencies of categorical variables. Post-hoc tests (Tukey, Bonferroni) identify which specific groups differ after significant ANOVA.

</details>

---

**Q7. A researcher reports p = 0.03 with 95% confidence interval for risk ratio of 1.4 (CI: 1.05–1.87). The correct interpretation is:**
- A) There is a 3% chance the null hypothesis is true
- B) The probability of obtaining this result by chance alone, assuming no true association, is 3%
- C) The treatment works in 97% of patients
- D) There is 97% probability that the true RR lies between 1.05 and 1.87

<details>
<summary>Answer</summary>

**Correct: B**

p-value is the probability of observing a result at least as extreme as obtained, assuming the null hypothesis (H₀) is true — NOT the probability H₀ is true. p <0.05 → reject H₀ (statistically significant). The 95% CI (1.05–1.87) excludes 1.0 → significant (consistent with p <0.05). The CI means: if the study were repeated 100 times, 95 times the true RR would fall within the calculated interval.

</details>

---

**Q8. A diagnostic test for TB has sensitivity 70% and specificity 95%. In a population where TB prevalence is 1%, the negative predictive value (NPV) is closest to:**
- A) 70%
- B) 88%
- C) 99.7%
- D) 95%

<details>
<summary>Answer</summary>

**Correct: C**

In 10,000 people: 100 have TB, 9,900 don't. True negatives = 9,900 × 0.95 = 9,405. False negatives = 100 × 0.30 = 30. NPV = 9,405/(9,405+30) = 9,405/9,435 ≈ 99.7%. NPV is high when prevalence is low and specificity is high. A high NPV means a negative test reliably rules out disease. This is why screening tests require high sensitivity (to minimize false negatives).

</details>

---

**Q9. In a clinical trial, investigators do not know which patients received the drug or placebo, and patients are also unaware. This is called:**
- A) Single-blind study
- B) Double-blind study
- C) Open-label study
- D) Triple-blind study

<details>
<summary>Answer</summary>

**Correct: B**

Double-blind RCT: both the investigator/assessor and the participant are blinded to treatment allocation, eliminating observer bias and performance bias. Single-blind: only participant is blinded. Triple-blind: participant, investigator, AND data analyst are blinded. Open-label: no blinding. Double-blind RCT is the gold standard study design with highest internal validity. Blinding reduces ascertainment (detection) bias.

</details>

---

**Q10. A researcher reports a study in which participants who were sicker were more likely to use a new medication, making the medication appear harmful. This is an example of:**
- A) Recall bias
- B) Selection bias
- C) Confounding by indication (channeling bias)
- D) Hawthorne effect

<details>
<summary>Answer</summary>

**Correct: C**

Confounding by indication (channeling bias) occurs when a drug is preferentially prescribed to sicker patients, making it appear to cause worse outcomes; the underlying disease severity is the confounder. Recall bias: cases remember exposures better than controls (case-control studies). Selection bias: non-representative sample selection. Hawthorne effect: subjects change behavior when observed. Multivariate analysis, propensity score matching, and RCTs control for confounding.

</details>

---

## SCREENING AND CAUSALITY (Q11–Q15)

**Q11. According to Wilson and Jungner criteria (WHO 1968), a disease suitable for mass screening should have all of the following EXCEPT:**
- A) An accepted, effective, and available treatment
- B) A recognizable latent or early symptomatic stage
- C) A rare disease with high case fatality rate
- D) A suitable, acceptable, and validated screening test

<details>
<summary>Answer</summary>

**Correct: C**

Wilson-Jungner criteria require that the disease be an important health problem (common, serious) — NOT rare. A rare disease, even with high fatality, does not justify mass screening due to poor cost-effectiveness and low PPV. Key criteria: important health problem, known natural history, detectable early stage, effective treatment, acceptable test, agreed policy, cost-effective. Examples of valid screening: cervical Ca (Pap smear), breast Ca (mammography), neonatal hypothyroidism (TSH).

</details>

---

**Q12. In an ROC (Receiver Operating Characteristic) curve analysis, the ideal cut-off point for a screening test in a population with high disease prevalence is:**
- A) The point with highest specificity only
- B) The point closest to the upper-left corner (0,1) of the ROC curve
- C) The point where sensitivity = specificity (Youden's index)
- D) The point with highest area under the curve (AUC)

<details>
<summary>Answer</summary>

**Correct: B**

The optimal cut-off on an ROC curve is the point closest to the upper-left corner (0% FPR, 100% sensitivity) — maximizing both sensitivity and specificity simultaneously. Youden's index (sensitivity + specificity − 1, or J = max) mathematically identifies this point. AUC measures overall discriminatory ability (AUC 0.9–1.0 = excellent). Lowering the cut-off increases sensitivity but decreases specificity; raising it does the opposite.

</details>

---

**Q13. Hill's criterion of causality that is considered the most important is:**
- A) Biological plausibility
- B) Consistency of association
- C) Strength of association
- D) Temporality (cause precedes effect)

<details>
<summary>Answer</summary>

**Correct: D**

Temporality is the only essential (sine qua non) criterion in Hill's criteria of causality — the cause MUST precede the effect; without this, causality is impossible. Strength of association (high RR/OR) is the strongest supporting evidence. Biological plausibility supports but is not essential (mechanism may be unknown). Consistency across studies, dose-response gradient, specificity, analogy, coherence, and experimental evidence are other criteria.

</details>

---

**Q14. Likelihood ratio positive (LR+) of a diagnostic test is calculated as:**
- A) Sensitivity / (1 − Specificity)
- B) Specificity / (1 − Sensitivity)
- C) PPV / (1 − NPV)
- D) (1 − Sensitivity) / Specificity

<details>
<summary>Answer</summary>

**Correct: A**

LR+ = Sensitivity / (1 − Specificity) = True positive rate / False positive rate. LR+ >10 strongly increases post-test probability (excellent test). LR− = (1 − Sensitivity) / Specificity; LR− <0.1 strongly decreases post-test probability. LR is not affected by prevalence (unlike PPV/NPV), making it useful for comparing tests across populations. Post-test odds = Pre-test odds × LR.

</details>

---

**Q15. A researcher finds that as cigarette consumption (packs/year) increases, the risk of lung cancer increases in a dose-dependent manner. This is which Hill's criterion?**
- A) Temporality
- B) Specificity
- C) Biological gradient (dose-response relationship)
- D) Coherence

<details>
<summary>Answer</summary>

**Correct: C**

Biological gradient (dose-response relationship): increasing exposure leads to increasing risk, strengthening causal inference (e.g., more pack-years → higher lung cancer risk). Specificity: one cause → one effect (rare, not always applicable). Coherence: finding consistent with known natural history and biology. Temporality: exposure precedes disease. Analogy: similar cause-effect known for related agent.

</details>

---

## NATIONAL HEALTH PROGRAMS — INDIA (Q16–Q20)

**Q16. Under India's Universal Immunization Programme (UIP), which vaccine is given at 9–12 months of age?**
- A) OPV (oral polio vaccine) — only at birth
- B) Measles-Rubella (MR) vaccine — first dose
- C) DPT booster — first booster
- D) Japanese Encephalitis vaccine — second dose

<details>
<summary>Answer</summary>

**Correct: B**

Under UIP India (revised schedule): Measles-Rubella (MR) first dose is given at 9–12 months. Second MR dose at 16–24 months. BCG at birth. OPV at birth + 6, 10, 14 weeks + booster at 16–24 months. DPT primary at 6, 10, 14 weeks; first booster at 16–24 months; second booster at 5–6 years. Hepatitis B: at birth, 6, 10, 14 weeks (as pentavalent). JE vaccine given in endemic states at 9–12 months (with MR).

</details>

---

**Q17. Under India's NTEP (National TB Elimination Programme), the target for TB elimination is defined as:**
- A) Zero TB cases by 2025
- B) Less than 1 TB case per million population by 2025
- C) Less than 10 TB cases per 100,000 population by 2025 (End TB goal by 2035, advanced to 2025 in India)
- D) Reduction in TB incidence by 50% from 2015 baseline by 2025

<details>
<summary>Answer</summary>

**Correct: C**

India's NTEP (formerly RNTCP) targets TB elimination — defined as <10 cases per 100,000 population per year — by 2025 (10 years ahead of WHO End TB Strategy target of 2035). The Nikshay Poshan Yojana provides ₹500/month nutritional support to TB patients. DSTB treatment: 2HRZE/4HR (6 months). MDR-TB treated with bedaquiline-based regimens (18–20 months under new shorter regimen).

</details>

---

**Q18. The population norm for a Primary Health Centre (PHC) in a hilly/tribal/difficult area under Indian health infrastructure is:**
- A) 30,000 population
- B) 20,000 population
- C) 10,000 population
- D) 5,000 population

<details>
<summary>Answer</summary>

**Correct: B**

Population norms in India: Sub-centre — 5,000 (plains), 3,000 (hilly/tribal). PHC — 30,000 (plains), 20,000 (hilly/tribal/difficult). CHC (Community Health Centre) — 1,20,000 (plains), 80,000 (hilly/tribal). PHC is the first contact point with qualified medical officer (MO). Sub-centre is staffed by ANM (Auxiliary Nurse Midwife) and Male Health Worker. CHC has 30 beds and specialist care (surgeon, physician, OBG, pediatrician).

</details>

---

**Q19. Under NVBDCP (National Vector Borne Disease Control Programme), the drug used for mass drug administration (MDA) for lymphatic filariasis elimination in India is:**
- A) Diethylcarbamazine (DEC) alone
- B) DEC + Albendazole (DA) — in non-endemic for onchocerciasis
- C) Ivermectin + DEC + Albendazole (IDA)
- D) Ivermectin alone

<details>
<summary>Answer</summary>

**Correct: C**

India switched from DA (DEC + Albendazole) to IDA (Ivermectin + DEC + Albendazole) triple drug therapy for MDA in lymphatic filariasis-endemic districts from 2018 onwards, as IDA achieves more rapid reduction in microfilaremia. India is the largest contributor to global filariasis burden. Vector is Culex mosquito. Target: elimination by 2027 (WHO goal 2030). Night blood smear (microfilariae nocturnal periodicity) is standard diagnosis.

</details>

---

**Q20. Under the Reproductive Child Health (RCH) program, the 3-dose tetanus toxoid (TT) schedule for a primigravida starts at:**
- A) First antenatal visit regardless of gestational age, minimum 4-week gap
- B) 16 weeks gestation for first dose, 20 weeks for second dose, 24 weeks for third
- C) As early as possible in pregnancy; 2nd dose 4 weeks after 1st; 3rd dose 6 months later
- D) 28, 32, and 36 weeks of gestation

<details>
<summary>Answer</summary>

**Correct: C**

For primigravida: TT1 — as early as possible in pregnancy; TT2 — 4 weeks after TT1 (provides protection for this pregnancy); TT3/Booster — 6 months after TT2 or in next pregnancy (provides lifetime protection). Under RCH/Mission Indradhanush, pregnant women receive TT immunization. Td (Tetanus-diphtheria) has replaced TT in some states. Each TT dose provides protection for 5 years; 3 doses = lifetime immunity.

</details>

---

## NUTRITION (Q21–Q25)

**Q21. A 2-year-old child is brought with oedema of feet and legs, depigmented reddish hair, moon-face, and a "flaky paint" rash. Serum albumin is very low. Weight-for-height is 85% of median. The diagnosis is:**
- A) Marasmus
- B) Kwashiorkor
- C) Marasmic-kwashiorkor
- D) Nutritional oedema without PEM

<details>
<summary>Answer</summary>

**Correct: B**

Kwashiorkor is caused by severe protein deficiency with adequate caloric intake; characterized by oedema (hypoalbuminaemia), "flaky paint" or "crazy pavement" dermatosis, depigmented flag sign in hair, moon face, hepatomegaly (fatty infiltration), preserved subcutaneous fat. Marasmus = severe calorie + protein deficiency → severe wasting, "wizened old man" appearance, no oedema. Marasmic-kwashiorkor = wasting + oedema. WHO F-75/F-100 formulas used for treatment.

</details>

---

**Q22. Bitot's spots (triangular, foamy, grey deposits on bulbar conjunctiva) indicate deficiency of which vitamin, and what is the standard high-dose supplementation given to children 1–5 years in India?**
- A) Vitamin D — 60,000 IU monthly
- B) Vitamin A — 2,00,000 IU every 6 months
- C) Vitamin A — 1,00,000 IU every 3 months
- D) Vitamin E — 400 mg daily

<details>
<summary>Answer</summary>

**Correct: B**

Bitot's spots are an early manifestation of Vitamin A deficiency (xerophthalmia classification XN, X1A, X1B, X2, X3A/B). Under India's National Vitamin A Supplementation Programme (NVASP): children 6–11 months → 1,00,000 IU once; children 1–5 years → 2,00,000 IU every 6 months. Night blindness (XN) is the earliest symptom. Vitamin A also reduces measles mortality. Vitamin A palmitate is given to mothers within 6 weeks of delivery (1,80,000 IU).

</details>

---

**Q23. The ICDS (Integrated Child Development Services) scheme in India provides supplementary nutrition to all of the following EXCEPT:**
- A) Children 0–6 years
- B) Pregnant and lactating women
- C) Adolescent girls (11–18 years) in select states
- D) School-going children 6–14 years in rural areas

<details>
<summary>Answer</summary>

**Correct: D**

ICDS targets: children 0–6 years, pregnant women, lactating mothers, and adolescent girls (11–18 years, under Kishori Shakti Yojana/SABLA in select states). School-going children 6–14 years are covered under the PM Poshan Shakti Nirman (formerly Mid-Day Meal Scheme) — a separate program under Ministry of Education. ICDS is delivered through Anganwadi centres (one per 1,000 population), providing 6 services: supplementary nutrition, immunization, health check-up, referral services, pre-school education, nutrition and health education.

</details>

---

**Q24. A child with IQ 45, short stature, coarse facies, macroglossia, and umbilical hernia is diagnosed with cretinism. The most common cause in India is:**
- A) Autoimmune thyroiditis (Hashimoto's)
- B) Iodine deficiency during pregnancy
- C) Congenital absence of thyroid gland
- D) TSH receptor gene mutation

<details>
<summary>Answer</summary>

**Correct: B**

Iodine deficiency during pregnancy is the most preventable cause of intellectual disability worldwide and the most common cause of cretinism in India (endemic in Himalayan belt, sub-Himalayan regions). Universal iodization of salt (≥15 ppm at consumption level) is mandated under Prevention of Food Adulteration Act. Neonatal TSH screening (Guthrie card) detects congenital hypothyroidism. Endemic goitre prevalence >30% = IDD-endemic area.

</details>

---

**Q25. The Recommended Dietary Allowance (RDA) for iron in a pregnant woman as per ICMR 2020 guidelines is:**
- A) 21 mg/day
- B) 27 mg/day
- C) 35 mg/day
- D) 17 mg/day

<details>
<summary>Answer</summary>

**Correct: C**

ICMR 2020 RDA for iron: Pregnant women — 35 mg/day (increased from earlier 27 mg/day). Non-pregnant women of reproductive age — 21 mg/day. Children 1–3 years — 9 mg/day. Adolescent girls — 32 mg/day. Under POSHAN 2.0 and Anemia Mukt Bharat (AMB), pregnant women receive IFA (Iron + Folic Acid) 100 mg elemental iron + 500 mcg folic acid daily for 180 days. Anemia prevalence in pregnant women in India is ~50% (NFHS-5).

</details>

---

## VITAL STATISTICS AND ENVIRONMENT (Q26–Q30)

**Q26. According to NFHS-5 (2019–21) data, the Infant Mortality Rate (IMR) of India is approximately:**
- A) 20 per 1,000 live births
- B) 35 per 1,000 live births
- C) 44 per 1,000 live births
- D) 15 per 1,000 live births

<details>
<summary>Answer</summary>

**Correct: B**

NFHS-5 (2019–21) reported India's IMR at 35.2 per 1,000 live births (SRS 2020: 28 per 1,000). IMR = deaths in first year of life per 1,000 live births; best indicator of socioeconomic development and healthcare quality. MMR (Maternal Mortality Ratio) per SRS 2018–20: 97 per 1,00,000 live births. NMR (Neonatal Mortality Rate): 20 per 1,000 live births. CBR (Crude Birth Rate) India: ~19.5 per 1,000 population. TFR: 2.0 (NFHS-5).

</details>

---

**Q27. As per WHO and BIS standards, the permissible limit of nitrates in drinking water is:**
- A) 10 mg/L
- B) 25 mg/L
- C) 45 mg/L
- D) 100 mg/L

<details>
<summary>Answer</summary>

**Correct: C**

WHO guideline and BIS (IS:10500) permissible limit for nitrates in drinking water is 45 mg/L (as NO₃). Excess nitrates cause methemoglobinemia (blue baby syndrome) in infants <6 months as their fetal hemoglobin is more susceptible to oxidation. BIS desirable limit: 45 mg/L; no relaxation permitted. Fluoride permissible limit: 1.5 mg/L (BIS); optimal for dental health: 0.5–0.8 mg/L. Turbidity: 1 NTU (desirable), 5 NTU (permissible).

</details>

---

**Q28. Epidemic is defined as occurrence of cases of a disease in excess of what would normally be expected. An epidemic limited to a single exposure event (one-time common source) produces which characteristic epidemic curve?**
- A) Propagated (person-to-person) curve — gradual rise, multiple peaks
- B) Point source epidemic curve — sharp rise, single peak, rapid decline within one incubation period
- C) Continuous common source — plateau lasting several incubation periods
- D) Mixed epidemic — initial sharp peak followed by secondary cases

<details>
<summary>Answer</summary>

**Correct: B**

Point source epidemic (e.g., food poisoning at a wedding): all cases exposed at same time → sharp rise, single peak, and rapid fall within one maximum incubation period. Propagated epidemic (e.g., measles) shows gradual rise with successive waves (each peak ~1 incubation period apart). Continuous common source (e.g., contaminated water supply) shows a prolonged plateau. Mixed epidemic starts as point source then propagates person-to-person.

</details>

---

**Q29. The cold chain for vaccines in India is maintained at which temperature at the PHC level?**
- A) −20°C to −15°C
- B) 2°C to 8°C
- C) −60°C to −50°C
- D) 0°C to 4°C

<details>
<summary>Answer</summary>

**Correct: B**

At PHC level, vaccines are stored at 2°C to 8°C (refrigerator temperature) in Ice-Lined Refrigerators (ILR). At district level: −15°C to −25°C (deep freezer). At regional/state level: −15°C to −25°C. OPV and varicella require −15°C to −25°C for long-term storage. The Vaccine Vial Monitor (VVM) tracks heat exposure. Freeze-sensitive vaccines (DPT, Hep B, TT) must NOT be frozen. Cold chain equipment: ILR, deep freezers, cold boxes, vaccine carriers, ice packs.

</details>

---

**Q30. Maternal Mortality Ratio (MMR) is expressed as:**
- A) Maternal deaths per 1,000 live births
- B) Maternal deaths per 1,00,000 live births
- C) Maternal deaths per 1,000 women of reproductive age per year
- D) Maternal deaths per 1,00,000 total births (live + still)

<details>
<summary>Answer</summary>

**Correct: B**

MMR = (Number of maternal deaths / Number of live births) × 1,00,000. Maternal death = death of a woman during pregnancy or within 42 days of termination of pregnancy from causes related to or aggravated by pregnancy or its management. India's MMR: 97/1,00,000 live births (SRS 2018–20). SDG target: <70 by 2030. India's target: <100 by 2020 (achieved). Leading causes of MMR in India: haemorrhage, sepsis, hypertensive disorders. Obstetric death rate uses total births (denominator).

</details>

---
