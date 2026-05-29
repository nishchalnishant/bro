# SRS-SCHEDULE — Spaced Repetition for NEET PG

> **Daily revision vs SRS:** DAILY-REVISION.md is for passive content review (reading facts). This file drives active recall testing at increasing intervals. Use both: read daily, test on SRS schedule.

---

## 1. Interval Logic

When you first study a topic, schedule active recall (close the notes, answer MCQs from memory) at these intervals:

| Review | Interval from last successful review |
|--------|--------------------------------------|
| R1 | +1 day |
| R2 | +3 days |
| R3 | +7 days |
| R4 | +14 days |
| R5 | +30 days |

- Pass all 5 reviews → mark topic **[x] Mastered** in WEAK-TOPICS.md
- Fail any review → reset to R1 (+1 day from today); record the reset date

---

## 2. How to Use With This Repo

1. Study a topic → mark it `[~]` in the subject's `WEAK-TOPICS.md`
2. Note today's date in the "Last Revised" column (add the column if missing)
3. Use the interval table above to compute each review date
4. Log the topic in the **30-Day SRS Master Log** (Section 5 below)
5. On each review date, test yourself without notes — pass/fail
6. On final pass (R5), update WEAK-TOPICS.md from `[~]` to `[x]`

---

## 3. Subject Priority Tiers

Review frequency: Tier 1 subjects get SRS slots every week; Tier 2 every 10 days; Tier 3 every 2 weeks.

### Tier 1 — Highest Yield (review most frequently)
| Subject | Approx. NEET PG Qs |
|---------|-------------------|
| General Medicine | 23 |
| Surgery | 15 |
| OBG | 15 |
| Pathology | 18 |
| Pharmacology | 16 |
| Anatomy | 14 |

### Tier 2 — High Yield
| Subject | Approx. NEET PG Qs |
|---------|-------------------|
| SPM / Community Medicine | 16 |
| Pediatrics | 12 |
| Physiology | 13 |
| Microbiology | 13 |
| Biochemistry | 11 |

### Tier 3 — Standard Yield
| Subject | Approx. NEET PG Qs |
|---------|-------------------|
| ENT | 8 |
| Ophthalmology | 8 |
| Forensic Medicine | 8 |
| Dermatology | 7 |
| Orthopaedics | 7 |
| Psychiatry | 6 |
| Anaesthesia | 5 |
| Radiology | 4 |

---

## 4. Weekly SRS Planner Template

Copy this block each Monday and fill in **Status** (P = pass, F = fail/reset).

| Day | Subject (Tier 1) | Review Type | Topics | Status |
|-----|-----------------|-------------|--------|--------|
| Mon | Medicine | New study | | |
| Mon | Pathology | New study | | |
| Tue | Pharmacology | New study | | |
| Tue | Anatomy | New study | | |
| Wed | Medicine | R1 review (+1d) | | |
| Wed | Pathology | R1 review (+1d) | | |
| Wed | Surgery | New study | | |
| Wed | OBG | New study | | |
| Thu | Pharmacology | R1 review (+1d) | | |
| Thu | Anatomy | R1 review (+1d) | | |
| Thu | Tier 2 subject | New study | | |
| Fri | Surgery | R1 review (+1d) | | |
| Fri | OBG | R1 review (+1d) | | |
| Fri | Medicine | R2 review (+3d from Mon) | | |
| Sat | Pathology | R2 review (+3d from Mon) | | |
| Sat | Tier 2 subject | R1 review (+1d) | | |
| Sun | Pharmacology | R2 review (+3d from Tue) | | |
| Sun | Anatomy | R2 review (+3d from Tue) | | |
| Sun | Weak topic catch-up | Any | | |

---

## 5. 30-Day SRS Master Log Template

Add one row per topic when first studied. Fill dates as you complete each review (YYYY-MM-DD). Mark Mastered? with Y when R5 passes.

| # | Topic | Subject | Date Studied | +1d (R1) | +3d (R2) | +7d (R3) | +14d (R4) | +30d (R5) | Mastered? |
|---|-------|---------|-------------|----------|----------|----------|-----------|-----------|-----------|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |
| 5 | | | | | | | | | |
| 6 | | | | | | | | | |
| 7 | | | | | | | | | |
| 8 | | | | | | | | | |
| 9 | | | | | | | | | |
| 10 | | | | | | | | | |
| 11 | | | | | | | | | |
| 12 | | | | | | | | | |
| 13 | | | | | | | | | |
| 14 | | | | | | | | | |
| 15 | | | | | | | | | |
| 16 | | | | | | | | | |
| 17 | | | | | | | | | |
| 18 | | | | | | | | | |
| 19 | | | | | | | | | |
| 20 | | | | | | | | | |
| 21 | | | | | | | | | |
| 22 | | | | | | | | | |
| 23 | | | | | | | | | |
| 24 | | | | | | | | | |
| 25 | | | | | | | | | |
| 26 | | | | | | | | | |
| 27 | | | | | | | | | |
| 28 | | | | | | | | | |
| 29 | | | | | | | | | |
| 30 | | | | | | | | | |

---

## 6. High-Frequency Reset Topics

These topics are classically failed at SRS reviews — aspirants repeatedly reset them. Prioritise these in Tier 1/2 SRS slots.

| # | Topic | Subject | Why it's hard |
|---|-------|---------|---------------|
| 1 | Brachial plexus (roots, trunks, divisions, cords, branches) | Anatomy | Complex spatial relationships; multiple named injuries |
| 2 | Cardiac action potential phases (0–4) and ion channels | Physiology | Phase confusion; CCB/antiarrhythmic drug targets overlap |
| 3 | Enzyme deficiencies in metabolic/storage disorders | Biochemistry | Large table; similar names (Gaucher/Niemann/Fabry/Krabbe) |
| 4 | Hypersensitivity type I–IV mechanisms + examples | Pathology / Microbiology | Mechanism vs example matching errors |
| 5 | Drug mechanisms and receptor subtypes | Pharmacology | Adrenergic/cholinergic/opioid subtypes all look alike under pressure |
| 6 | Obstetric emergencies — doses, criteria, management | OBG | Doses change; eclampsia vs pre-eclampsia criteria confusion |
| 7 | Vaccine schedule (UIP + IAP) | Pediatrics | Frequent schedule updates; age/route/dose details |
| 8 | CSF interpretation (meningitis types) | Medicine | Overlapping values across bacterial/viral/TB/fungal |
| 9 | ECG reading — axis, blocks, STEMI patterns | Medicine | Lead groupings and territory correlations require practice |
| 10 | Scoring systems (APGAR, CURB-65, Child-Pugh, Bishop, Glasgow, SOFA) | Multiple | Many systems; threshold numbers get mixed up |
| 11 | Cranial nerve nuclei and lesion localisation | Anatomy | Midbrain/pons/medulla localisation errors common |
| 12 | Coagulation cascade (intrinsic/extrinsic/common) + tests | Pathology | PT vs aPTT vs TT associations; factor number confusion |
| 13 | Antibiotics — spectrum, mechanism, resistance | Pharmacology | Aminoglycoside/beta-lactam/macrolide details overlap |
| 14 | Tumour markers and associated malignancies | Pathology | AFP/CEA/CA-125/PSA/Beta-hCG associations get confused |
| 15 | Renal tubular transport and diuretic sites of action | Physiology | Segment-drug mapping under exam stress |
| 16 | Dermatomes and myotomes (C5–S1) | Anatomy | Reflex-root associations (biceps C5, triceps C7, knee L4) |
| 17 | Congenital heart diseases — cyanotic vs acyanotic + shunts | Pediatrics / Medicine | Eisenmenger physiology; when shunt reverses |
| 18 | Sterilisation methods — sporicidal/bactericidal temps and times | Microbiology / SPM | Hot air vs autoclave parameters; glutaraldehyde levels |
| 19 | Statistical tests — parametric vs non-parametric, use cases | SPM | Which test for which data type and sample size |
| 20 | Ophthalmology — glaucoma types, tonometry, angle anatomy | Ophthalmology | Open vs closed angle; drug mechanisms (miotics, beta-blockers) |
