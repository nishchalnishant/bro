# Pharmacology — Pharmacokinetics Notes

> Part of: [pharmacology-notes index](pharmacology-notes.md) | [MCQs](pharmacology-mcqs.md) | [Lecture](pharmacology-lecture.md)

---

## 1. PHARMACOKINETICS

### Bioavailability
- **Definition**: Fraction of administered drug that reaches systemic circulation unchanged
- **Oral bioavailability affected by**: first-pass metabolism, gut wall metabolism, absorption
- **IV route**: bioavailability = 100% (reference standard)
- **F = (AUC oral / AUC IV) × 100**

### First-Pass Effect (Pre-systemic Metabolism)
- Occurs in gut wall and liver before drug reaches systemic circulation
- **High first-pass drugs**: morphine, nitroglycerin, propranolol, lidocaine, aspirin, testosterone, levodopa
- **Consequence**: oral dose >> IV dose needed for same effect
- **Nitroglycerin**: given sublingually/transdermally to bypass first-pass

> **PYQ HOTSPOT**: Nitroglycerin is given sublingually to avoid first-pass effect

### Volume of Distribution (Vd)
- **Formula**: Vd = Dose / Plasma concentration
- **Vd = 3-5 L**: stays in plasma (large MW, protein bound) — heparin, warfarin
- **Vd = 10-20 L**: distribution into interstitial fluid
- **Vd > 20 L (very high)**: extensive tissue binding — chloroquine, digoxin, amiodarone

| Drug | Vd | Implication |
|------|-----|-------------|
| Heparin | ~0.06 L/kg | Plasma only |
| Warfarin | ~0.14 L/kg | Highly protein bound |
| Chloroquine | ~200-800 L/kg | Extensive tissue binding |
| Digoxin | ~7 L/kg | Stored in muscle/tissue |

> **PYQ HOTSPOT**: High Vd = NOT dialyzable (drug in tissues, not plasma)

### Protein Binding
- **Acidic drugs bind albumin**: warfarin, phenytoin, NSAIDs, furosemide
- **Basic drugs bind alpha-1 acid glycoprotein**: propranolol, lidocaine, quinidine
- **Only free (unbound) drug** is pharmacologically active
- **Displacement interactions**: one drug displaces another → increased free drug → toxicity
- **Warfarin + aspirin**: aspirin displaces warfarin → bleeding risk

### Half-Life (t1/2)
- **t1/2 = 0.693 × Vd / CL**
- Time to reach 50% of initial concentration
- **Steady state reached in 4-5 half-lives**
- **Drug eliminated in ~4-5 half-lives** (>94% eliminated)
- **Short t1/2**: phenytoin, warfarin (NOT true — warfarin t1/2 = 36 hrs)
- **Long t1/2**: amiodarone (40-55 days), digoxin (36-48 hrs)

### Clearance
- **CL = Vd × Ke (elimination rate constant)**
- **CL = Dose / AUC**
- **Hepatic CL**: depends on hepatic blood flow and extraction ratio
- **High extraction ratio drugs**: first-pass effect significant (morphine, propranolol)
- **Low extraction ratio drugs**: changes in protein binding affect clearance

### Zero-Order vs First-Order Kinetics

| Parameter | Zero-Order | First-Order |
|-----------|-----------|-------------|
| Rate | Constant amount/time | Constant fraction/time |
| Enzyme | Saturated | Not saturated |
| t1/2 | Not constant | Constant |
| Examples | **Alcohol, phenytoin (at high doses), aspirin (high doses), heparin** | Most drugs |
| Graph (log conc vs time) | Curved | Straight line |

> **PYQ HOTSPOT**: Phenytoin - zero order kinetics (capacity-limited/saturation kinetics) — small dose increase → disproportionate rise in plasma levels → toxicity

### Loading Dose / Maintenance Dose

- **Loading Dose = (Vd × Target Css) / F**
- **Maintenance Dose = CL × Target Css / F**
- **Loading dose**: used when rapid onset needed (digoxin, amiodarone, phenytoin)
- **Digoxin loading dose**: 0.5–1 mg given in divided doses (digitalizing dose)

### Enzyme Induction

**Mnemonic: "CRAP GPS"** — Carbamazepine, Rifampicin, Alcohol (chronic), Phenytoin, Griseofulvin, Phenobarbitone, Sulphonylureas

| Inducer | Drugs whose levels DECREASE |
|---------|---------------------------|
| **Rifampicin** (most potent inducer) | Warfarin, OCPs, cyclosporine, azoles, protease inhibitors |
| **Phenytoin** | Warfarin, OCPs, doxycycline |
| **Carbamazepine** | Warfarin, OCPs, valproate, thyroid hormones |
| **Phenobarbitone** | Vitamin D metabolism (→ rickets), bilirubin, steroids |

> **PYQ HOTSPOT**: Rifampicin + OCP → contraceptive failure

### Enzyme Inhibition

| Inhibitor | Mechanism | Consequence |
|-----------|-----------|-------------|
| **Ketoconazole** | CYP3A4 inhibition | ↑ warfarin, cyclosporine, statins |
| **Cimetidine** | Multiple CYP inhibition | ↑ warfarin, theophylline, phenytoin |
| **Erythromycin/Clarithromycin** | CYP3A4 | ↑ statins (rhabdomyolysis) |
| **Fluoxetine/Paroxetine** | CYP2D6 | ↑ TCAs, codeine effects |
| **Metronidazole** | CYP2C9 | ↑ warfarin → bleeding |
| **Grapefruit juice** | CYP3A4 in gut | ↑ felodipine, statins |
