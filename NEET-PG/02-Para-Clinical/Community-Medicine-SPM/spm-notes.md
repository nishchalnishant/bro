# Community Medicine (SPM/PSM) - NEET PG High-Yield Notes

---

## CONCEPTS OF HEALTH AND DISEASE

### Definition of Health
- **WHO 1948: "Health is a state of complete physical, mental, and social well-being and not merely the absence of disease or infirmity"**
- Spiritual dimension added later (WHO 1984) — not in original definition
- **PYQ HOTSPOT**: WHO definition criticized for being utopian, static, and unmeasurable

### Determinants of Health (Lalonde Model - 1974)
| Determinant | Examples |
|-------------|----------|
| Human biology (genetics) | Age, sex, hereditary factors |
| Environment | Physical, social, psychological |
| Lifestyle | Diet, smoking, exercise |
| Health care organization | Availability, quality |

- **Most important determinant of health = Socioeconomic status**
- Mnemonic: **HELP** - Human biology, Environment, Lifestyle, Provision of healthcare

### Spectrum of Disease
- Susceptibility → Sub-clinical → Clinical → Disability → Death
- **Iceberg phenomenon**: Only tip visible (clinical cases); submerged portion = sub-clinical/undiagnosed cases
  - **PYQ HOTSPOT**: Polio and hypertension are classic examples of iceberg phenomenon
  - TB = large submerged portion (sub-clinical cases >> clinical)

### Natural History of Disease - Leavell & Clark

#### 5 Levels of Prevention
| Level | Stage of Disease | Measures |
|-------|-----------------|----------|
| **1st - Health Promotion** | Pre-pathogenesis | Health education, nutrition, sanitation |
| **2nd - Specific Protection** | Pre-pathogenesis | Immunization, chemoprophylaxis, safety measures |
| **3rd - Early Diagnosis & Treatment** | Pathogenesis (early) | Screening, case finding |
| **4th - Disability Limitation** | Pathogenesis (late) | Treatment to prevent complications |
| **5th - Rehabilitation** | Post-disease | Physical, social, vocational rehab |

- **Primordial prevention** (Strasser 1978): Prevention of risk factors from establishing in a population (e.g., preventing adoption of western diet)
- **PYQ HOTSPOT**: Primordial prevention is NOT part of Leavell & Clark's original model

### Epidemiological Triad (Agent-Host-Environment)
- **Agent**: Biological, chemical, physical, nutritional
- **Host**: Age, sex, genetics, immunity, behavior
- **Environment**: Physical (water, air), biological (vectors), social
- **PYQ HOTSPOT**: Vector = biological environment

### Web of Causation (MacMahon & Pugh)
- Complex interrelationship of factors in chronic disease causation
- **Multiple causation theory**

---

## EPIDEMIOLOGY

### Study Designs

#### Case-Control Study
- **Direction: Backward (retrospective)**
- Starts with disease, looks back at exposure
- **Odds Ratio (OR)** = measure of association
- OR = (ad)/(bc) using 2×2 table:

|  | Disease+ | Disease- |
|--|----------|----------|
| Exposed | a | b |
| Unexposed | c | d |

- **OR = (a×d)/(b×c)**
- **OR > 1 = risk factor; OR < 1 = protective factor**
- Advantages: cheap, fast, good for rare diseases, multiple exposures studied
- Disadvantages: recall bias, cannot calculate incidence, not good for rare exposures

#### Cohort Study
- **Direction: Forward (prospective)**
- Starts with exposure, follows for disease outcome
- **Relative Risk (RR)** = measure of association
- **RR = [a/(a+b)] / [c/(c+d)]**
- **Attributable Risk (AR) = Incidence in exposed - Incidence in unexposed = a/(a+b) - c/(c+d)**
- **Population Attributable Risk % (PAR%) = (Incidence in total population - Incidence in unexposed) / Incidence in total population × 100**
- Advantages: can calculate incidence, RR, temporal relationship, less bias
- Disadvantages: expensive, time-consuming, loss to follow-up

#### Cross-Sectional Study (Prevalence Study)
- Measures exposure AND disease at same point in time
- Measure of association: **Prevalence Ratio**
- Advantages: quick, cheap, hypothesis generating
- Disadvantages: cannot establish causality, prevalence-incidence bias

#### Randomized Controlled Trial (RCT)
- **Gold standard for causality and efficacy**
- Blinding: single blind, double blind (both patient and observer), triple blind (+ data analyst)
- **PYQ HOTSPOT**: RCT has best internal validity; systematic reviews/meta-analysis have best external validity

#### Ecological Study
- Unit of analysis = population (not individual)
- **Ecological fallacy/Ecologic bias**: Cannot apply group-level findings to individuals
- Good for: hypothesis generation, policy research

### Measures of Disease Frequency

| Measure | Formula | Notes |
|---------|---------|-------|
| **Incidence Rate** | New cases / Population at risk × 1000 | Per unit time |
| **Prevalence** | All cases / Total population × 1000 | Point or period |
| **P = I × D** | Prevalence = Incidence × Duration | For stable diseases |
| **Attack Rate** | Cases / Population exposed × 100 | For outbreaks |
| **Secondary Attack Rate (SAR)** | New cases among contacts / Susceptible contacts × 100 | Within incubation period |
| **Case Fatality Rate (CFR)** | Deaths / Cases × 100 | Severity of disease |
| **Crude Death Rate (CDR)** | Deaths / Mid-year population × 1000 | |

- **PYQ HOTSPOT**: Prevalence increases with: ↑ incidence, ↑ duration, immigration of cases, emigration of healthy
- Prevalence decreases with: ↑ mortality, ↑ cure rate, immigration of healthy

### Rates vs Ratios vs Proportions
- **Rate**: Change over time; has time component
- **Ratio**: Comparison of two numbers (e.g., sex ratio)
- **Proportion**: Part of whole (no time component)
- **Standardization**: Used to compare rates between populations with different age/sex distributions
  - Direct standardization: uses standard population
  - Indirect standardization: uses SMR (Standardized Mortality Ratio)

### Bias in Epidemiology

| Type | Definition | Control |
|------|-----------|---------|
| **Selection bias** | Systematic error in selecting study participants | Randomization, proper sampling |
| **Information/Observation bias** | Systematic error in measuring exposure/outcome | Blinding, standardization |
| **Recall bias** | Cases remember exposure better than controls | Objective data, medical records |
| **Confounding** | Third variable associated with both exposure and outcome | Restriction, matching, stratification, multivariate analysis |
| **Berkson's bias** | Hospital-based case-control: hospital admission rates differ | Population-based controls |
| **Neyman bias** | Prevalence-incidence bias in cross-sectional studies | — |

### Screening

#### 2×2 Table for Screening
|  | Disease+ | Disease- |
|--|----------|----------|
| **Test+** | **TP (a)** | **FP (b)** |
| **Test-** | **FN (c)** | **TN (d)** |

| Measure | Formula | Meaning |
|---------|---------|---------|
| **Sensitivity** | a/(a+c) | True positive rate; ability to detect disease |
| **Specificity** | d/(b+d) | True negative rate; ability to rule out disease |
| **PPV** | a/(a+b) | Proportion of test+ who truly have disease |
| **NPV** | d/(c+d) | Proportion of test- who truly don't have disease |

- **PYQ HOTSPOT**: 
  - Sensitivity ↑ → FN ↓ → Good for ruling OUT disease (SnNout)
  - Specificity ↑ → FP ↓ → Good for ruling IN disease (SpPin)
  - **PPV depends on prevalence** (higher prevalence → higher PPV)
  - NPV depends on prevalence (lower prevalence → higher NPV)
- **ROC Curve**: plots Sensitivity vs (1-Specificity); **area under curve = accuracy**
- **Lead time bias**: Screening detects disease earlier; survival appears longer without change in outcome
- **Length bias**: Screening detects more slowly progressive (less aggressive) disease

### Wilson-Jungner Criteria for Screening (WHO)
1. Disease must be important health problem
2. Natural history must be understood
3. Recognizable early/latent stage
4. Treatment available
5. Suitable test available
6. Test acceptable to population
7. Adequate facilities for diagnosis/treatment
8. Agreed policy on who to treat
9. Cost-effective
10. Ongoing process, not one-time

### Causality - Hill's Criteria (1965)
Mnemonic: **SCAT BCEP**
1. **S**trength of association (high RR/OR)
2. **C**onsistency (replicated in different studies)
3. **A**nalogyspecificity (one cause → one effect)
4. **T**emporality (**ONLY MANDATORY CRITERION** - cause precedes effect)
5. **B**iological gradient (dose-response relationship)
6. **C**oherence (consistent with known facts)
7. **E**xperiment (RCT confirms association)
8. **P**lausibility (biologically plausible)
9. **Specificity** (one exposure → one disease)

- **PYQ HOTSPOT**: Temporality is the only necessary (mandatory) criterion

---

## BIOSTATISTICS

### Types of Data
| Type | Examples | Tests |
|------|---------|-------|
| **Nominal** (categorical) | Blood group, gender, religion | Chi-square, Fisher's exact |
| **Ordinal** | Cancer staging, pain scale | Mann-Whitney U, Kruskal-Wallis |
| **Interval** | Temperature (°C), IQ | t-test, ANOVA |
| **Ratio** | Height, weight, BP | t-test, ANOVA |

- **PYQ HOTSPOT**: Interval vs Ratio - Ratio has TRUE ZERO (e.g., 0 kg means no weight); Interval has arbitrary zero (0°C ≠ no temperature)

### Normal Distribution
- **Mean = Median = Mode** (symmetrical, bell-shaped)
- **68-95-99.7 Rule**:
  - Mean ± 1 SD = **68.27%** of observations
  - Mean ± 2 SD = **95.45%** of observations
  - Mean ± 3 SD = **99.73%** of observations
- **PYQ HOTSPOT**: 95% reference range = Mean ± 1.96 SD

### Skewed Distribution
- **Positive skew (right skew)**: Tail on right; **Mean > Median > Mode**
- **Negative skew (left skew)**: Tail on left; **Mode > Median > Mean**
- Mnemonic: In positive skew, MEAN is pulled toward the tail (higher values)

### Statistical Tests

| Situation | Parametric | Non-Parametric |
|-----------|-----------|----------------|
| Compare 2 groups | **Student's t-test** | Mann-Whitney U / Wilcoxon rank sum |
| Compare >2 groups | **ANOVA (F-test)** | Kruskal-Wallis |
| Paired comparison | **Paired t-test** | Wilcoxon signed rank |
| Categorical data | **Chi-square (χ²)** | Fisher's exact (small samples) |
| Correlation | **Pearson's r** | **Spearman's rho** |

- **Chi-square**: For categorical data, expected cell count ≥ 5 in each cell
- **Fisher's exact test**: When expected cell count < 5 (small samples)
- **McNemar's test**: Paired categorical data
- **PYQ HOTSPOT**: Chi-square cannot be used when expected cell frequency < 5

### P-value, CI, Errors
- **P-value**: Probability of obtaining results by chance if null hypothesis is true
  - **p < 0.05 = statistically significant** (conventional threshold)
- **Confidence Interval (CI)**: Range likely to contain true population value
  - **95% CI = x̄ ± 1.96 × SE**
  - If 95% CI for OR/RR includes 1.0 → NOT significant

| Error Type | Definition | Symbol | Consequence |
|-----------|-----------|--------|-------------|
| **Type I (α)** | Rejecting true null hypothesis (false positive) | α (usually 0.05) | Claiming effect that doesn't exist |
| **Type II (β)** | Accepting false null hypothesis (false negative) | β (usually 0.2) | Missing true effect |
| **Power** | Probability of detecting true effect | 1-β | Usually set at 0.80 (80%) |

- **PYQ HOTSPOT**: Power = 1 - β; increasing sample size increases power and decreases both errors

### Sample Size Determination
- Larger sample needed when:
  - Higher power required (1-β ↑)
  - Smaller α (more stringent)
  - Smaller expected effect size
  - Higher variability in population

---

## NUTRITION

### Protein-Energy Malnutrition (PEM)

| Feature | **Kwashiorkor** | **Marasmus** |
|---------|-----------------|--------------|
| Cause | Protein deficiency (adequate calories) | Total calorie deficiency |
| Age | 1-3 years (post-weaning) | < 1 year |
| Edema | **YES (pitting edema)** | No |
| Serum albumin | **Low (<3.5 g/dL)** | Normal/slightly low |
| Appearance | "Moon face", flaky paint dermatosis | "Old man face", skin & bones |
| Muscle wasting | Masked by edema | Severe |
| Hair changes | Flag sign (brown bands), easily pluckable | Sparse, thin |
| Appetite | **Poor** | **Preserved (ravenous)** |
| Liver | **Fatty liver (hepatomegaly)** | Normal |
| Mortality | Higher | Lower |

- **PYQ HOTSPOT**: Edema in Kwashiorkor due to hypoalbuminemia → ↓ oncotic pressure
- **Marasmus-Kwashiorkor** (Mixed): features of both; worst prognosis
- **Gomez classification** (weight for age): Grade I: 75-90%, Grade II: 60-75%, Grade III: <60%
- **Waterlow classification** (stunting = height for age; wasting = weight for height)
- **Z-score**: <-2 SD = moderate malnutrition; <-3 SD = severe malnutrition

### BMI Classification

| BMI | WHO | Asian (Indian) |
|-----|-----|----------------|
| Underweight | < 18.5 | < 18.5 |
| Normal | 18.5-24.9 | 18.5-22.9 |
| Overweight | 25-29.9 | 23-24.9 |
| Obese Class I | 30-34.9 | 25-29.9 |
| Obese Class II | 35-39.9 | ≥ 30 |
| Obese Class III | ≥ 40 | — |

- **PYQ HOTSPOT**: Asian cutoff for overweight = 23 (not 25)
- **MUAC**: Mid-upper arm circumference; <12.5 cm = severe malnutrition (child 1-5 years); <23 cm = malnutrition in adults

### Micronutrient Deficiencies

#### Vitamin A Deficiency
- **Xerophthalmia grading (WHO)**:
  - XN: Night blindness (**earliest feature**)
  - X1A: Conjunctival xerosis
  - X1B: **Bitot's spots** (triangular, foamy, temporal conjunctiva)
  - X2: Corneal xerosis
  - X3A: Corneal ulceration (<1/3 cornea)
  - X3B: Keratomalacia (**corneal ulceration >1/3 - blindness**)
  - XS: Corneal scar
  - XF: Xerophthalmic fundus
- **PYQ HOTSPOT**: Bitot's spots = X1B; Keratomalacia = X3B (causes blindness)
- **DOSS Program (Vitamin A Supplementation)**:
  - 6 months to 5 years; every 6 months
  - Dose: 1,00,000 IU at 6 months; **2,00,000 IU thereafter**

#### Iodine Deficiency
- **Endemic goiter**: Goiter prevalence >5% in community
- **Cretinism** (congenital): Most severe consequence; **most common cause of preventable mental retardation**
- **NIN Classification of goiter**:
  - Grade 0: No goiter
  - Grade 1: Visible on swallowing
  - Grade 2: Visible at rest
- **PYQ HOTSPOT**: Iodized salt = 15-30 ppm iodine; neonatal hypothyroidism screened by TSH

#### Iron Deficiency Anemia (IDA)
- **Most common nutritional deficiency worldwide**
- Stages: Depleted stores → Functional deficit → Frank anemia
- Lab: **Low Hb, Low serum ferritin (earliest), ↑TIBC, ↓MCV (microcytic hypochromic)**
- National Programs: WIFS (Weekly Iron and Folic Acid Supplementation), IFA supplementation in pregnancy

#### Vitamin D Deficiency
- **Rickets** (children): Craniotabes, Harrison's sulcus, rachitic rosary, bow legs
- **Osteomalacia** (adults): Bone pain, pseudo-fractures (Looser zones), muscle weakness
- Source: Sunlight (UVB) = main source in India

#### Folate/Folic Acid
- **Neural Tube Defect (NTD) prevention**: **400 mcg/day periconceptionally** (1 month before to 3 months after conception)
- **PYQ HOTSPOT**: Folic acid reduces NTD risk by 70%

### Government Nutrition Programs

| Program | Target Group | Key Features |
|---------|-------------|--------------|
| **ICDS (1975)** | Children <6 yr, pregnant/lactating women | 6 services: supplementary nutrition, immunization, health checkup, referral, pre-school education, nutrition/health education |
| **Mid-Day Meal (1995)** | School children 1-8 (6-14 years) | 300 kcal, 8-12g protein (primary); 700 kcal (upper primary) |
| **PDS** | BPL/APL families | Subsidized food grains through ration shops |
| **POSHAN Abhiyaan (2018)** | Children, pregnant women | Target: ↓ stunting, undernutrition, anemia, LBW |
| **SNP (Supplementary Nutrition Programme)** | Children <3 yr, pregnant women | Under ICDS |

- **PYQ HOTSPOT**: ICDS started in 1975; Mid-Day Meal Act 1982

### Food Safety
- **FSSAI Act 2006**: Food Safety and Standards Authority of India
- **PFA Act 1954**: Prevention of Food Adulteration Act (replaced by FSSAI)
- **Common adulterants**: Metanil yellow in turmeric, starch in spices, chalk in flour

---

## NATIONAL HEALTH PROGRAMS

### RNTCP / National TB Elimination Programme (NTEP)

#### TB in India
- **India has highest TB burden globally** (26% of global burden)
- **Target**: Eliminate TB by **2025** (SDG goal 2030)
- **Nikshay Poshan Yojana**: Rs 500/month nutritional support to TB patients

#### DOTS (Directly Observed Treatment, Short-course)
| Category | Patients | Regimen |
|----------|---------|---------|
| **Cat I** | New smear+, New severe extrapulmonary, New smear- with extensive parenchymal involvement | 2HRZE + 4HR |
| **Cat II** | Previously treated: retreatment, relapse, treatment after failure/default | 2HRZES + 1HRZE + 5HRE |

- **H = Isoniazid, R = Rifampicin, Z = Pyrazinamide, E = Ethambutol, S = Streptomycin**
- **PYQ HOTSPOT**: DOTS = cornerstone of RNTCP; category decided by smear status and treatment history
- **MDR-TB**: Resistance to at least Isoniazid AND Rifampicin
- **XDR-TB**: MDR + resistance to any fluoroquinolone + any injectable drug
- **Newer regimens**: BPaL (Bedaquiline + Pretomanid + Linezolid) for XDR-TB

### NVBDCP (National Vector Borne Disease Control Programme)

#### Malaria
- **API (Annual Parasite Incidence)** = (Confirmed malaria cases in year / Population under surveillance) × 1000
- **SPR (Slide Positivity Rate)** = (Positive slides / Total slides examined) × 100
- **ABER (Annual Blood Examination Rate)** = (Blood slides examined / Population) × 100 (minimum 10%)
- **PYQ HOTSPOT**: High-risk area = API ≥ 2; Very high risk = API ≥ 5
- **Plasmodium falciparum**: Malignant tertian; highest mortality; no hypnozoites
- **Plasmodium vivax**: Benign tertian; hypnozoites (relapse); treat with Primaquine (8-aminoquinoline)
- **Drug of choice**: Chloroquine (for vivax); **ACT (Artemisinin Combination Therapy)** for falciparum

#### Dengue
- **Aedes aegypti**: Vector; daytime biting; breeds in clean stored water
- **Warning signs**: Abdominal pain, persistent vomiting, rapid breathing, bleeding gums
- **NS1 antigen**: Positive in first 5 days
- **Tourniquet test (Rumpel-Leede)**: ≥20 petechiae in 1 inch² = positive

#### Filariasis
- **MDA (Mass Drug Administration)**: **DEC (Diethylcarbamazine) + Albendazole** annually
- Vector: **Culex quinquefasciatus**
- Elimination target: microfilaria rate < 1%

### NLEP (National Leprosy Eradication Programme)

#### MDT Regimens

| Type | Duration | Drugs |
|------|---------|-------|
| **Paucibacillary (PB)** | 6 months | Dapsone 100mg daily + Rifampicin 600mg monthly (supervised) |
| **Multibacillary (MB)** | 12 months | Dapsone 100mg daily + Clofazimine 50mg daily + Rifampicin 600mg + Clofazimine 300mg monthly |

- **PB**: 1-5 lesions, smear negative
- **MB**: >5 lesions or smear positive
- **Elimination**: Prevalence < **1 per 10,000** population
- **PYQ HOTSPOT**: India achieved national elimination in 2005; some states still endemic
- **Lepromin test (Mitsuda reaction)**: Not diagnostic; tests cell-mediated immunity

### Universal Immunization Programme (UIP)

#### National Immunization Schedule (NIS)

| Age | Vaccine | Route | Dose |
|-----|---------|-------|------|
| Birth | BCG, OPV-0, Hep B-0 | ID (BCG), Oral, IM | 0.1 mL, 2 drops, 0.5 mL |
| 6 weeks | DTwP/IPV/Hib-1, OPV-1, PCV-1, Rota-1 | IM/Oral | — |
| 10 weeks | DTwP/IPV/Hib-2, OPV-2, PCV-2, Rota-2 | IM/Oral | — |
| 14 weeks | DTwP/IPV/Hib-3, OPV-3, PCV-3, Rota-3 | IM/Oral | — |
| 9-12 months | MR (Measles-Rubella), JE-1 (endemic areas) | SC | 0.5 mL |
| 16-24 months | DPT booster-1, OPV booster, MR-2, JE-2 | IM/Oral/SC | — |
| 5-6 years | DPT booster-2 | IM | — |
| 10 years | Td (Tetanus-diphtheria reduced) | IM | — |
| 16 years | Td | IM | — |
| Pregnant | TT/Td × 2 doses, IFA, Calcium | IM | — |

- **PYQ HOTSPOT**:
  - **BCG**: ID in left deltoid; 0.05 mL (neonate), 0.1 mL (older child)
  - **BCG contraindication**: HIV+, immunocompromised (NOT premature/LBW baby)
  - **OPV contraindication**: Immunocompromised household contacts (use IPV)
  - **Cold chain**: -15 to -25°C for OPV; +2 to +8°C for most other vaccines
  - **Open vial policy**: BCG, OPV, measles = discard after session; DPT, TT, Hep B = keep up to 4 weeks
- **Herd immunity thresholds**: Measles 92-95%, Polio 80-85%, Smallpox 80-85%

### NACP (National AIDS Control Programme)
- **Phases**: NACP I (1992), II (1999), III (2007), IV (2012-2017), now NACP V
- **PPTCT (Prevention of Parent-to-Child Transmission)**: All HIV+ pregnant women get lifelong ART (Option B+)
- **ICTC**: Integrated Counselling and Testing Centres (voluntary)
- **VCTC**: Voluntary Counselling and Testing Centres
- **TI (Targeted Interventions)**: For high-risk groups (CSW, MSM, IDU)
- **PYQ HOTSPOT**: NACO = National AIDS Control Organization

### RMNCH+A Strategy

#### Janani Suraksha Yojana (JSY)
- **BPL pregnant women** for institutional delivery
- Cash incentive: **Rs 1400 (rural)**, Rs 1000 (urban) to mother + Rs 600 to ASHA
- PYQ HOTSPOT: JSY launched 2005; modified CSSM

#### Janani Shishu Suraksha Karyakram (JSSK)
- **Free services** to pregnant women and sick newborns in government facilities
- Free drugs, diagnostics, blood, transport, diet

#### PMSMA (Pradhan Mantri Suraksha Matritva Abhiyan)
- **9th of every month**: Free ANC checkup for all pregnant women in 2nd and 3rd trimester

#### Other Programs
- **MAA (Mothers' Absolute Affection)**: Breastfeeding promotion
- **HBNC (Home Based Newborn Care)**: ASHA visits 6 times in first month
- **RBSK (Rashtriya Bal Swasthya Karyakram)**: Child health screening

### Other National Programs

| Program | Key Points |
|---------|-----------|
| **NMHP** (National Mental Health Programme, 1982) | District Mental Health Programme (DMHP) |
| **NCCP** (National Cancer Control Programme, 1975) | 3 Regional Cancer Centers, palliative care |
| **NPCDCS** (2010) | Integrated NCD program: Cancer, Diabetes, CVD, Stroke |
| **NPCB** (National Programme for Control of Blindness) | Cataract surgeries, VISION 2020 |
| **NVBDCP** | Malaria, Dengue, Filariasis, Kala-azar, JE, Chikungunya |
| **IDDCP** (Iodine Deficiency Disorders) | Universal Salt Iodization |

### Ayushman Bharat (PM-JAY)
- **Pradhan Mantri Jan Arogya Yojana**
- Health coverage: **Rs 5 lakh per family per year**
- Covers **50 crore beneficiaries** (bottom 40% of population)
- Launched **2018**
- Cashless and paperless at empaneled hospitals
- **PYQ HOTSPOT**: Does NOT cover OPD; only hospitalization

---

## VITAL STATISTICS AND HEALTH INDICATORS

### Demographic Measures

| Indicator | Formula | Normal/India |
|-----------|---------|-------------|
| **CBR (Crude Birth Rate)** | Live births/Mid-year pop × 1000 | ~20 (India 2020) |
| **CDR (Crude Death Rate)** | Deaths/Mid-year pop × 1000 | ~6 (India 2020) |
| **Natural Growth Rate** | CBR - CDR | ~14/1000 |
| **TFR (Total Fertility Rate)** | Average children per woman (15-49 yr) | ~2.0 (India 2020); replacement = 2.1 |
| **GRR** | TFR × proportion of female births | <1 = declining population |
| **NRR** | GRR × probability of surviving to mean age of childbearing | NRR=1 means stable population |

### Mortality Measures

| Indicator | Formula | India Value |
|-----------|---------|------------|
| **IMR** | Infant deaths (0-365 days)/1000 live births | ~28 (SRS 2020) |
| **NMR** | Neonatal deaths (0-28 days)/1000 live births | ~20 |
| **PNMR** | Post-neonatal deaths (29 days-1 yr)/1000 LB | IMR - NMR |
| **U5MR** | Deaths under 5 years/1000 live births | ~32 |
| **Stillbirth rate** | Stillbirths/1000 total births | — |
| **MMR** | Maternal deaths/100,000 live births | **97 (India 2018-20)** |
| **Perinatal mortality rate** | Stillbirths+deaths in 1st week/1000 total births | — |

- **PYQ HOTSPOT**:
  - **IMR = single most sensitive indicator of health status of a community**
  - MMR India target: <70 by 2030 (SDG); current = 97
  - **Three Delays Model** (Thaddeus & Maine):
    - Delay 1: Deciding to seek care
    - Delay 2: Reaching facility
    - Delay 3: Receiving adequate care

### Causes of Maternal Mortality in India
- Leading cause: **Hemorrhage** (PPH most common)
- Others: Hypertensive disorders, Sepsis, Obstructed labor, Abortion complications
- Mnemonic: **HHSOA** - Hemorrhage, Hypertension, Sepsis, Obstructed labor, Abortion

### Life Expectancy
- India life expectancy at birth: **~70 years** (males ~68.2, females ~70.7)
- **PYQ HOTSPOT**: Life expectancy at birth = best overall measure of health of a community

### Registration of Births and Deaths
- **RBD Act 1969**: Compulsory registration of births and deaths
- **SRS (Sample Registration System)**: Best source for IMR, CDR, CBR in India
- **Census**: Every 10 years; last census 2011 (2021 postponed)
- **Civil Registration System (CRS)**: For vital events

---

## ENVIRONMENTAL HEALTH

### Water Supply and Purification

#### Water Quality Standards (WHO/BIS)
| Parameter | Permissible Level |
|-----------|-----------------|
| **Turbidity** | <1 NTU (acceptable), <5 NTU (maximum) |
| **pH** | **6.5-8.5** |
| **Residual chlorine** | **0.5 mg/L** at consumer end |
| **Coliform count** | **Zero coliforms** in 100 mL |
| **Fluoride** | 0.5-1.5 mg/L (1 ppm optimal for dental) |
| **Nitrates** | <45 mg/L |
| **Arsenic** | <0.05 mg/L |

#### Water-Borne Diseases
- **Classical water-borne**: Cholera, typhoid, hepatitis A, polio (fecal-oral)
- **Water-washed**: Trachoma, scabies, skin infections (lack of water for hygiene)
- **Water-based**: Guinea worm (Dracunculiasis), schistosomiasis
- **Water-related**: Malaria, filariasis (vector breeds in water)

#### Purification Methods

| Method | Removal |
|--------|---------|
| **Sedimentation** | Suspended particles |
| **Coagulation (Alum)** | Colloidal matter; alum dose = 20-40 mg/L |
| **Slow Sand Filtration** | 0.1-0.4 m/hr; **biological layer (Schmutzdecke)** removes bacteria; **most effective** for purification |
| **Rapid Sand Filtration** | 3-6 m/hr; needs pre-coagulation; removes turbidity only |
| **Chlorination** | Disinfection; **Breakpoint chlorination**: adding enough Cl₂ to oxidize all organic matter before free residual chlorine appears |

- **Breakpoint chlorination**: Point where residual chlorine sharply rises after complete oxidation of organic matter
- **Horrock's test**: Field test for residual chlorine
- **Ortho-toluidine test**: Colorimetric test for residual chlorine (yellow = positive)

### Sanitation

#### Types of Latrines
| Type | Key Feature |
|------|------------|
| **Bore hole latrine** | 30-40 cm diameter; 3-4.5 m deep |
| **VIP latrine (Ventilated Improved Pit)** | Fly trap design |
| **Water seal latrine** | **Most commonly recommended in India**; prevents fly/odor |
| **Septic tank** | Anaerobic digestion; for individual homes |

- **Sewage treatment**:
  - **Primary**: Physical (screening, grit removal, sedimentation)
  - **Secondary**: Biological (activated sludge, trickling filter) - **removes 90% BOD**
  - **Tertiary**: Chemical/physical (removes remaining BOD, nutrients, pathogens)
- **BOD (Biochemical Oxygen Demand)**: Oxygen needed to oxidize organic matter; **BOD of clean water <5 ppm**; sewage 200-300 ppm
- **Septic tank effluent**: BOD reduced by ~70%

### Air Pollution
- **PM2.5**: Most harmful; reaches alveoli; WHO limit = 25 μg/m³ (24-hr)
- **PM10**: Can reach bronchioles
- **CO (Carbon Monoxide)**: 240× greater affinity for Hb than O₂; produced by combustion
- **Indoor air pollution**: **5th leading cause of death in developing countries**; biomass fuels (wood, dung, crop residues)
- **Sick Building Syndrome**: Building-related illness; poor ventilation, VOCs, fungi; >20% occupants affected

### Biomedical Waste (BMW Rules 2016)

| Category | Color | Treatment |
|----------|-------|----------|
| Human anatomical waste | **Yellow** | Incineration |
| Contaminated/solid waste | **Yellow** | Autoclaving/incineration |
| Sharps | **Red** | Autoclaving/microwave |
| Glassware | **White (translucent)** | Autoclave/chemical treatment |
| Cytotoxic/chemical | **Black** | Secured landfill |

- **PYQ HOTSPOT**: Red container for sharps; Yellow for anatomical waste

### Occupational Health

#### Pneumoconioses
| Disease | Cause | Key Feature |
|---------|-------|------------|
| **Silicosis** | Crystalline silica (quartz) | Eggshell calcification of hilar nodes; **most fibrogenic dust** |
| **Asbestosis** | Asbestos | **Mesothelioma** (pleural cancer); ferruginous bodies; **asbestosis → lung cancer RR = 50 if smoker** |
| **Coal worker's pneumoconiosis** | Coal dust | Progressive massive fibrosis; Caplan syndrome (with RA) |
| **Byssinosis** | Cotton dust | "Monday fever"; chest tightness on return to work |
| **Bagassosis** | Sugarcane dust (bagasse) | Hypersensitivity pneumonitis |

- **PYQ HOTSPOT**: Silicosis + TB = **Silicotuberculosis** (common association)
- **Factories Act 1948**: Governs occupational health in organized sector
- **Schedule of occupational diseases** (Factories Act): 29 notifiable occupational diseases

---

## FAMILY PLANNING

### Contraceptive Methods

| Method | Mechanism | Failure Rate (Pearl Index) |
|--------|-----------|--------------------------|
| **Cu-T 380A** | Spermicidal (Cu ions), prevents fertilization/implantation | <1% |
| **OCP (Combined)** | Inhibits ovulation, thickens cervical mucus | <1% |
| **Condom** | Barrier | 2-15% |
| **Vasectomy (NSVC)** | Ligation of vas deferens | <0.1% |
| **Tubectomy (TL)** | Ligation of fallopian tubes | <0.5% |
| **DMPA (Depot MPA)** | Injectable progestin; every 3 months | <1% |

#### OCP Mechanism and Contraindications
- **Combined OCP**: Estrogen (inhibits FSH → no follicle) + Progestin (inhibits LH → no ovulation)
- **Benefits**: Reduced dysmenorrhea, PID protection, ovarian/endometrial cancer protection, regulation of cycle
- **Absolute contraindications**: Active liver disease, history of DVT/PE, migraine with aura, smoker >35 years, undiagnosed vaginal bleeding, breast cancer, active cardiovascular disease

#### IUCD
- **Cu-T 380A**: Copper surface area 380 mm²; effective for **10 years**; most commonly used IUCD in India
- **LNG-IUS (Mirena)**: Levonorgestrel-releasing; effective for 5 years; reduces menstrual blood loss
- **PYQ HOTSPOT**: IUCD of choice post-partum = **Cu-T 380A** (can be inserted immediately post-delivery)

### NSVC (No-Scalpel Vasectomy with Cauterization)
- **Safer vasectomy technique**; outpatient procedure; smaller incision/puncture
- **PYQ HOTSPOT**: Vasectomy = terminal method; requires counseling; failure requires partner evaluation (not always vasectomy failure)

### MTP Act 1971 (Amended 2021)
| Gestation | Requirements |
|-----------|-------------|
| Up to **20 weeks** | Opinion of **1 registered medical practitioner (RMP)** |
| **20-24 weeks** | Opinion of **2 RMPs** (for specified categories: rape survivors, minors, mentally ill, fetal abnormality) |
| Beyond 24 weeks | **Medical Board at state level** for substantial fetal abnormality only |

- **PYQ HOTSPOT**: Amendment 2021 extended upper limit from 20 to 24 weeks for special categories
- **Women who can access MTP up to 24 weeks**: Rape survivors, minors, change of marital status (widowed/divorced), women with disabilities, fetal malformations
- MTP can only be performed in **government hospitals or certified private hospitals**

### POCSO Act 2012 (Protection of Children from Sexual Offences)
- **Child = person under 18 years**
- All sexual offenses against children under 18
- **Mandatory reporting**: All persons must report to police
- **PYQ HOTSPOT**: Doctor must report POCSO; cannot maintain patient confidentiality

---

## HEALTH ADMINISTRATION

### Primary Health Care Structure

| Level | Population served | Key Features |
|-------|------------------|-------------|
| **Sub-Center** | **3000-5000** (plains), 1000-3000 (hilly) | 1 ANM + 1 MPW (M); basic health services |
| **PHC** | **20,000-30,000** (plains), 3000-20000 (hilly) | 1 doctor; 6 beds; 24×7 for delivery |
| **CHC (Community Health Centre)** | **80,000-1,20,000** | 30 beds; 4 specialists (surgeon, physician, OBG, pediatrician) |
| **District Hospital** | District (~2 million) | Full specialty services |

- **PYQ HOTSPOT**: PHC serves 20,000-30,000 (plains); has 6 beds
- **Sub-center**: **First contact point** with government health system
- **CHC = First Referral Unit (FRU)**: Must provide EmOC (Emergency Obstetric Care)

### ASHA (Accredited Social Health Activist)
- **1 per 1000 population** in rural areas
- Link worker between community and health system
- Not employee but voluntary worker with incentives
- **Key activities**: JSY facilitation, immunization promotion, HBNC, RBSK

### ANM (Auxiliary Nurse Midwife)
- Works at sub-center level
- **Multipurpose worker (female)**: immunization, antenatal care, FP, health education

### MPW (Multi-Purpose Worker)
- MPW (Male) = Health Worker Male = Malaria surveillance worker
- Population: 3000-5000 per MPW (sub-center level)

### National Health Policy 2017
- **Vision**: Highest attainable standard of health for all
- **Key targets by 2025**:
  - IMR: **28/1000 LB**
  - U5MR: **23/1000 LB**
  - MMR: **100/1,00,000 LB**
  - CBR: **16/1000**
  - NMR: **16/1000 LB**
- **Health expenditure**: Government to spend **2.5% of GDP** on health
- **Comprehensive primary health care**: HWC (Health and Wellness Centres)

### Health and Wellness Centres (HWC)
- Upgraded Sub-Centers and PHCs
- Provide **CPHC (Comprehensive Primary Health Care)**
- 12 service packages including mental health, geriatric care, NCD screening

---

## QUICK REFERENCE: HIGH-YIELD NUMBERS

| Parameter | Value |
|-----------|-------|
| WHO definition year | 1948 |
| Sub-center population | 3000-5000 (plains) |
| PHC population | 20,000-30,000 (plains) |
| CHC population | 80,000-1,20,000 |
| ASHA ratio | 1:1000 |
| BCG route | Intradermal, left deltoid |
| Residual chlorine | 0.5 mg/L |
| Optimal fluoride | 1 ppm (0.5-1.5 mg/L) |
| BMI overweight (Asian) | ≥23 |
| Vitamin A dose (>6 months) | 2,00,000 IU |
| MTP Act 2021 - 1 doctor | Up to 20 weeks |
| MTP Act 2021 - 2 doctors | 20-24 weeks |
| Cu-T 380A duration | 10 years |
| PM-JAY coverage | Rs 5 lakh/family/year |
| India MMR 2018-20 | 97/1,00,000 LB |
| India IMR (SRS 2020) | ~28/1000 LB |
| India TFR | ~2.0 |
| MDR-TB definition | Resistance to H + R |
| Leprosy elimination | <1/10,000 population |
| NLEP - MB MDT duration | 12 months |
| NLEP - PB MDT duration | 6 months |

---

## KEY MNEMONICS

### Epidemiology
- **SCAT BCEP** = Hill's criteria (Strength, Consistency, Analogy, Temporality, Biological gradient, Coherence, Experiment, Plausibility + Specificity)
- **SnNout** = High Sensitivity rules OUT disease
- **SpPin** = High Specificity rules IN disease

### Biostatistics
- **NOIR** = Nominal, Ordinal, Interval, Ratio (data types)
- **Type I = α = false alarm** (cry wolf)
- **Type II = β = miss** (missing true effect)

### Nutrition
- **DAMN IT** = causes of Kwashiorkor (Deficient Amino acids, Maize diet, No meat in diet, Insufficient diet, Toxins, inadequate weaning)

### Health Programs
- **DOTS**: Directly Observed Treatment Short-course
- **NSVC**: No Scalpel Vasectomy with Cauterization

### Vitamins
- **Xerophthalmia grades**: XN → X1A → X1B (Bitot's) → X2 → X3A → X3B (Keratomalacia) → XS → XF

---

*Notes compiled for NEET PG preparation. Focus on PYQ HOTSPOT sections for maximum marks.*
