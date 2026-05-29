# Biochemistry - NEET PG High-Yield Notes

> 📊 [PYQ Analysis for this subject](../../04-PYQ-Analysis/Subject-Wise/subject-wise-pyq.md#biochemistry) | 🗂️ [Master Index](../../00-Master-Index/master-index.md) | 📝 [MCQs](biochemistry-mcqs.md)

## 📊 PYQ Snapshot (NEET PG 2019–2024)

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | Avg |
|------|------|------|------|------|------|------|-----|
| Questions | 12 | 11 | 11 | 10 | 10 | 10 | **11** |

**Trend:** Slight decline — focus on core metabolic pathways and vitamins.

### Top 10 High-Yield Topics
1. Enzyme kinetics (Km, Vmax, inhibition types)
2. Glycolysis, TCA cycle — key enzymes and energy yield
3. Amino acid metabolism (PKU, alkaptonuria, homocystinuria)
4. Vitamins — deficiency diseases, coenzyme roles
5. Lipid metabolism and ketogenesis
6. DNA replication and repair mechanisms
7. Glycogen metabolism and storage diseases
8. Hemoglobin structure and variants
9. Cholesterol metabolism and bile salt synthesis
10. PCR and molecular biology techniques

> **Strategy:** Vitamins (topic 4) and enzyme kinetics (topic 1) are the most reliable mark-scorers. Molecular biology questions are increasing in recent years.

---

---

## Carbohydrate Metabolism

### Glycolysis

> **PYQ HOTSPOT**: Rate-limiting enzyme, ATP yield, irreversible steps

**Location**: Cytoplasm (cytosol)

**Net ATP yield**: 2 ATP (net), 8 ATP total via substrate-level + NADH

| Step | Substrate | Enzyme | Notes |
|------|-----------|--------|-------|
| 1 | Glucose → G6P | **Hexokinase** (tissues) / **Glucokinase** (liver, beta cells) | ATP consuming; irreversible |
| 3 | F6P → F1,6-BP | **Phosphofructokinase-1 (PFK-1)** | **Rate-limiting step**; irreversible |
| 10 | PEP → Pyruvate | **Pyruvate kinase** | Irreversible; last step |

**Hexokinase vs Glucokinase**:
| Feature | Hexokinase | Glucokinase |
|---------|-----------|-------------|
| Km | Low (high affinity) | High (low affinity) |
| Inhibited by G6P | Yes | No |
| Location | All tissues | Liver, pancreatic beta cells |
| Saturation | Easily saturated | Not easily saturated |

**PFK-1 Regulators**:
- Activated by: AMP, ADP, F2,6-BP (**most potent activator**), fructose 6-phosphate
- Inhibited by: ATP, citrate, H+

**Irreversible steps mnemonic**: **"Hungry People Prefer"** = Hexokinase, PFK-1, Pyruvate kinase

**Total ATP from 1 glucose (aerobic)**:
- Glycolysis: 2 ATP + 2 NADH (= 5 ATP)
- Pyruvate dehydrogenase: 2 NADH (= 5 ATP)
- TCA cycle: 6 NADH + 2 FADH2 + 2 GTP per glucose
- **Total: ~30-32 ATP**

---

### TCA Cycle (Krebs Cycle)

> **PYQ HOTSPOT**: Products per turn, rate-limiting enzyme, energy yield

**Location**: Mitochondrial matrix

**Rate-limiting enzyme**: **Isocitrate dehydrogenase**

**Per turn of TCA cycle (1 acetyl-CoA)**:
- 3 NADH → 7.5 ATP
- 1 FADH2 → 1.5 ATP
- 1 GTP → 1 ATP
- **Total: 10 ATP per acetyl-CoA**

| Step | Enzyme | Key Points |
|------|--------|------------|
| Isocitrate → α-ketoglutarate | **Isocitrate dehydrogenase** | Rate-limiting; CO2 released |
| α-ketoglutarate → Succinyl-CoA | **α-ketoglutarate dehydrogenase** | Requires B1, B2, B3, lipoic acid, CoA |
| Succinyl-CoA → Succinate | Succinyl-CoA synthetase | **Substrate-level phosphorylation** (GTP) |
| Succinate → Fumarate | **Succinate dehydrogenase** | Only membrane-bound TCA enzyme; Complex II of ETC |

**Mnemonic for TCA cycle**: **"Citrate Is Krebs' Starting Substrate For Making Oxaloacetate"**
Citrate → Isocitrate → α-Ketoglutarate → Succinyl-CoA → Succinate → Fumarate → Malate → Oxaloacetate

---

### Glycogen Metabolism

> **PYQ HOTSPOT**: Glycogen storage diseases, key enzymes, branching/debranching

**Glycogen Synthesis**:
- **Rate-limiting enzyme**: **Glycogen synthase**
- UDP-glucose is the activated form
- **Branching enzyme**: α-1,4 to α-1,6 glucosidase transferase (creates branch points)
- Primer protein: **Glycogenin**

**Glycogen Breakdown**:
- **Rate-limiting enzyme**: **Glycogen phosphorylase** (requires pyridoxal phosphate = B6)
- Removes glucose-1-phosphate from α-1,4 bonds
- **Debranching enzyme**: has 2 activities - transferase + α-1,6 glucosidase

**Regulation**:
| Condition | Phosphorylase | Glycogen Synthase |
|-----------|--------------|------------------|
| Glucagon/Epinephrine | Activated (phosphorylated) | Inhibited |
| Insulin | Inhibited | Activated |
| AMP | Activates phosphorylase (allosteric) | - |

---

### Gluconeogenesis

> **PYQ HOTSPOT**: Unique enzymes (bypasses), substrates, location

**Location**: Mainly liver (90%), kidney cortex (10%)

**Substrates (gluconeogenic)**: Lactate, Amino acids (glucogenic), Glycerol, Propionate

**Bypasses** (irreversible steps of glycolysis bypassed):

| Glycolysis Step | Gluconeogenesis Bypass Enzyme |
|----------------|-------------------------------|
| Pyruvate → PEP | **Pyruvate carboxylase** (PC) → OAA, then **PEPCK** |
| F1,6-BP → F6P | **Fructose-1,6-bisphosphatase (FBPase)** |
| G6P → Glucose | **Glucose-6-phosphatase (G6Pase)** (**liver/kidney only**) |

**Pyruvate Carboxylase**: Activated by acetyl-CoA; requires biotin; mitochondria
**PEPCK**: Requires GTP; cytoplasm and mitochondria

**Key point**: **Gluconeogenesis is inhibited by alcohol** (NADH↑ → pyruvate → lactate, not gluconeogenesis)

---

### Pentose Phosphate Pathway (PPP/HMP Shunt)

> **PYQ HOTSPOT**: G6PD deficiency, NADPH production

**Location**: Cytoplasm
**Key products**: NADPH, Ribose-5-phosphate, CO2

**Rate-limiting enzyme**: **Glucose-6-phosphate dehydrogenase (G6PD)**

**Phases**:
1. **Oxidative phase**: Glucose-6-P → Ribulose-5-P; produces 2 NADPH + 1 CO2
2. **Non-oxidative phase**: Interconversion of sugars

**NADPH uses**: 
- Glutathione reductase (RBC protection)
- Fatty acid synthesis
- Cytochrome P450
- Phagocytic burst (NADPH oxidase)

**G6PD Deficiency**:
- X-linked recessive
- **Hemolysis triggered by**: primaquine, dapsone, sulfonamides, fava beans, infections
- **Heinz bodies** (denatured Hb) in peripheral smear
- **Bite cells** on peripheral smear
- **Common in**: Mediterranean, Africa, Middle East populations

---

### Glycogen Storage Diseases (GSD)

> **PYQ HOTSPOT**: Enzyme defect + organ + key features - HIGH YIELD TABLE

| Disease | Enzyme Defect | Stored Material | Organ | Key Features |
|---------|--------------|-----------------|-------|-------------|
| **Type I - Von Gierke** | **Glucose-6-phosphatase** | Glycogen + fat | Liver, kidney | Severe hypoglycemia, hepatomegaly, **no rise in glucose after glucagon**, lactic acidosis, hyperuricemia, hyperlipidemia |
| **Type II - Pompe** | **Lysosomal α-1,4 glucosidase (acid maltase)** | Glycogen in lysosomes | **All organs** (heart, muscle, liver) | **Cardiomegaly** (massive), hypotonia, death in infancy; **only GSD with lysosomal enzyme** |
| **Type III - Cori** | **Debranching enzyme** | Limit dextrin | Liver, muscle | Milder than Von Gierke; **normal lactate** |
| **Type IV - Andersen** | **Branching enzyme** | Amylopectin-like | Liver | Cirrhosis; death in childhood |
| **Type V - McArdle** | **Muscle phosphorylase** | Glycogen | **Muscle only** | Exercise intolerance, muscle cramps, **myoglobinuria**, **no rise in lactate with exercise** |
| **Type VI - Hers** | **Liver phosphorylase** | Glycogen | Liver | Mild, benign |
| **Type VII - Tarui** | **Phosphofructokinase (PFK)** | Glycogen | Muscle, RBC | Similar to McArdle + hemolytic anemia |

**Mnemonic for GSD**: **"Very Poor Carbohydrate Metabolism Always Has Very Terrible Prognosis"**
I-Von gierke, II-Pompe, III-Cori, IV-Anderson, V-McArdle, VI-Hers, VII-Tarui

---

### Galactosemia

> **PYQ HOTSPOT**: Enzyme defect, features, cataracts

**Classic Galactosemia**: Deficiency of **Galactose-1-phosphate uridyltransferase (GALT)**
- Accumulation of: Galactose-1-phosphate (toxic)
- Features: **Jaundice, hepatomegaly, cataracts, mental retardation, E. coli sepsis in neonates**
- Treatment: **Galactose-free diet**

| Disorder | Enzyme Defect | Accumulated Substance |
|---------|--------------|----------------------|
| Classic Galactosemia | GALT | Gal-1-P |
| Galactokinase deficiency | Galactokinase | Galactose, Galactitol | 
| UDP-galactose-4-epimerase def. | Epimerase | Gal-1-P + UDP-galactose |

**Galactitol** → **cataracts** (via aldose reductase pathway)

---

### Hereditary Fructose Intolerance

> **PYQ HOTSPOT**: Enzyme defect vs. Essential fructosuria

| Disorder | Enzyme Defect | Features |
|---------|--------------|---------|
| **Essential fructosuria** | **Fructokinase** | Benign; fructose in urine |
| **Hereditary Fructose Intolerance** | **Aldolase B** | Severe: hypoglycemia, vomiting, hepatic failure; **avoid fructose + sucrose** |
| Fructose-1,6-bisphosphatase def. | FBPase | Gluconeogenesis defect; hypoglycemia with fasting |

---

## Lipid Metabolism

### Fatty Acid Synthesis

> **PYQ HOTSPOT**: Rate-limiting enzyme, location, requirements

**Location**: **Cytoplasm** (CYTOSOL)
**Rate-limiting enzyme**: **Acetyl-CoA carboxylase (ACC)**
- Activated by: citrate, insulin
- Inhibited by: palmitoyl-CoA, glucagon, epinephrine
- Requires: **Biotin** as cofactor

**Fatty Acid Synthase (FAS)**: Uses NADPH (from PPP)
- Product: **Palmitate (C16)** — the primary product

**Transport**: Acetyl-CoA from mitochondria → cytoplasm via **citrate shuttle** (as citrate)

**Malonyl-CoA**: First committed step product; also **inhibits carnitine acyltransferase I (CPT-I)** → prevents FA entry into mitochondria when synthesis is active

---

### Beta-Oxidation of Fatty Acids

> **PYQ HOTSPOT**: ATP yield per palmitate, location, entry mechanism

**Location**: **Mitochondrial matrix**
**Entry**: Via **carnitine shuttle** (CPT-I rate-limiting; inhibited by malonyl-CoA)

**Steps per cycle**: Oxidation → Hydration → Oxidation → Thiolysis
**Products per cycle**: 1 FADH2, 1 NADH, 1 Acetyl-CoA

**ATP yield from Palmitate (C16)**:
- 7 cycles of beta-oxidation → 7 FADH2 + 7 NADH + 8 Acetyl-CoA
- 7 FADH2 × 1.5 = 10.5 ATP
- 7 NADH × 2.5 = 17.5 ATP
- 8 Acetyl-CoA × 10 = 80 ATP
- Activation cost: -2 ATP
- **Net: ~106 ATP**

**Odd-chain FA**: Produces propionyl-CoA → succinyl-CoA (via B12-dependent methylmalonyl-CoA mutase)

**Unsaturated FA**: Requires additional enzymes; **fewer ATP** produced

---

### Ketogenesis

> **PYQ HOTSPOT**: Rate-limiting enzyme, conditions, ketone bodies

**Location**: **Liver mitochondria** (only liver makes ketones; other tissues USE them)
**Rate-limiting enzyme**: **HMG-CoA synthase** (mitochondrial)

**Steps**:
Acetyl-CoA → Acetoacetyl-CoA → **HMG-CoA** → Acetoacetate → β-Hydroxybutyrate / Acetone

**Key enzyme**: **HMG-CoA lyase** (liver) cleaves HMG-CoA → acetoacetate

**Utilization**: Other tissues use ketones (brain during starvation)
- Requires: **Succinyl-CoA:acetoacetate CoA transferase (thiophorase)** — ABSENT IN LIVER
- This is why liver cannot use its own ketones

**Conditions promoting ketogenesis**: Starvation, uncontrolled DM, prolonged exercise, low carb diet

---

### Cholesterol Synthesis

> **PYQ HOTSPOT**: Rate-limiting enzyme, statin mechanism, feedback

**Location**: Primarily liver; also adrenal cortex, gonads

**Rate-limiting enzyme**: **HMG-CoA reductase**
- Inhibited by: statins, cholesterol (feedback), glucagon
- Activated by: insulin

**Pathway**: Acetyl-CoA → HMG-CoA → **Mevalonate** (rate-limiting step) → ... → Cholesterol

**Statins Mechanism**: 
- Competitive inhibitors of HMG-CoA reductase
- ↓ Cholesterol synthesis → ↑ LDL receptor expression → ↑ LDL uptake from blood
- Side effects: **myopathy/rhabdomyolysis** (monitor CK), hepatotoxicity

**Cholesterol → Bile acids**: Requires 7α-hydroxylase (rate-limiting for bile acid synthesis)

---

### Lipoproteins

> **PYQ HOTSPOT**: Structure, function, receptors, deficiencies - HIGH YIELD TABLE

| Lipoprotein | Origin | Major Lipid | Apolipoproteins | Function | Receptor |
|-------------|--------|-------------|-----------------|----------|---------|
| **Chylomicron** | Intestine | Dietary TG (90%) | **ApoB-48**, ApoC-II, ApoE | Transport dietary fat | ApoE receptor (remnant) |
| **VLDL** | Liver | Endogenous TG (55%) | **ApoB-100**, ApoC-II, ApoE | Transport endogenous TG | ApoE receptor → IDL |
| **IDL** | VLDL remnant | TG + Cholesterol | ApoB-100, ApoE | Intermediate | LDL receptor (ApoB-100/E) |
| **LDL** | IDL | Cholesterol (45%) | **ApoB-100** | Transport cholesterol to tissues | **LDL receptor (ApoB-100/E)** |
| **HDL** | Liver + Intestine | Protein (45%) | **ApoA-I** | Reverse cholesterol transport | SR-B1 |

**ApoC-II**: Activates **lipoprotein lipase (LPL)** — deficiency → hypertriglyceridemia
**ApoE**: Mediates remnant clearance
**ApoB-48**: Intestinal form (chylomicrons)
**ApoB-100**: Liver form (VLDL, IDL, LDL)

**Lipoprotein Lipase (LPL)**:
- Location: Capillary endothelium of adipose tissue and muscle
- Function: Hydrolyzes TG from chylomicrons and VLDL
- Activated by: ApoC-II, insulin
- Deficiency → **Familial LPL deficiency (Type I hyperlipoproteinemia)** → massive hypertriglyceridemia, pancreatitis, eruptive xanthomas

**Familial Hypercholesterolemia**: 
- LDL receptor mutation (most common: 19p13)
- **Heterozygous**: TC ~350-550 mg/dL; tendon xanthomas, early CAD
- **Homozygous**: TC > 700 mg/dL; death in childhood from MI

---

## Protein Metabolism

### Essential Amino Acids

> **PYQ HOTSPOT**: Mnemonic, conditionally essential

**Mnemonic**: **"PVT TIM HaLL"**
- **P** - Phenylalanine
- **V** - Valine
- **T** - Threonine
- **T** - Tryptophan
- **I** - Isoleucine
- **M** - Methionine
- **H** - Histidine (semi-essential)
- **a** - (and)
- **L** - Leucine
- **L** - Lysine

**Conditionally essential**: Arginine, Glutamine, Tyrosine (from phenylalanine), Cysteine (from methionine)

**Branched-chain amino acids (BCAA)**: Valine, Leucine, Isoleucine — metabolized in muscle (not liver)

---

### Urea Cycle

> **PYQ HOTSPOT**: Enzymes, location, CPS-1 deficiency, rate-limiting step

**Location**: Liver (both mitochondria and cytoplasm)

**Rate-limiting enzyme**: **Carbamoyl phosphate synthetase I (CPS-I)** — mitochondrial

| Step | Enzyme | Location | Notes |
|------|--------|----------|-------|
| NH3 + CO2 → Carbamoyl-P | **CPS-I** | Mitochondria | Requires N-acetylglutamate (activator), 2 ATP |
| Carbamoyl-P + Ornithine → Citrulline | OTC (Ornithine transcarbamylase) | Mitochondria | **Most common urea cycle defect** |
| Citrulline + Aspartate → Argininosuccinate | Argininosuccinate synthetase | Cytoplasm | 2nd N from aspartate |
| Argininosuccinate → Arginine + Fumarate | Argininosuccinate lyase | Cytoplasm | |
| Arginine → Ornithine + Urea | **Arginase** | Cytoplasm | Final step |

**CPS-I Deficiency**: ↑ NH3, ↑ glutamine, ↓ BUN, ↓ citrulline
**OTC Deficiency**: X-linked; most common; ↑ orotic acid (distinguishes from CPS-I deficiency)

**N-acetylglutamate (NAG)**: Essential activator of CPS-I; made by NAG synthase (activated by arginine)

---

### Amino Acid Disorders

> **PYQ HOTSPOT**: Enzyme defect, metabolite, features - CRITICAL TABLE

| Disorder | Enzyme Defect | Accumulated Metabolite | Features |
|---------|--------------|----------------------|---------|
| **PKU** | **Phenylalanine hydroxylase** (or BH4 cofactor) | Phenylalanine, phenylketones | **Intellectual disability, musty/mousy odor, fair skin/blue eyes/blonde hair, eczema; phenylketones in urine** |
| **Alkaptonuria** | **Homogentisate oxidase** | Homogentisic acid | **Ochronosis** (dark urine/cartilage/connective tissue), **arthritis**; benign mostly |
| **Homocystinuria** | **Cystathionine beta-synthase** (most common) | Homocysteine | **Marfanoid habitus, ectopia lentis (downward), DVT/PE, intellectual disability, premature atherosclerosis**; treat with B6/B12/folate/betaine |
| **MSUD (Maple Syrup Urine Disease)** | **Branched-chain α-keto acid dehydrogenase** | Leucine, Isoleucine, Valine + keto acids | **Sweet maple syrup odor, encephalopathy, death if untreated**; requires B1 (thiamine) |
| **Tyrosinemia Type I** | **Fumarylacetoacetase** | Succinylacetone | Liver failure, renal disease, risk of HCC |
| **Tyrosinemia Type II** | **Tyrosine aminotransferase** | Tyrosine | Corneal erosions, palmar/plantar keratosis |
| **Albinism** | **Tyrosinase** | Tyrosine (cannot make melanin) | ↓ melanin; photosensitivity, nystagmus |
| **Cystinuria** | **SLC3A1** transporter | Cystine, ornithine, lysine, arginine (COLA) | Cystine kidney stones; sodium cyanide-nitroprusside test |

**PKU treatment**: Phenylalanine-restricted diet; avoid aspartame (contains phenylalanine)
**Maternal PKU**: Even controlled PKU mothers → baby at risk for brain damage during gestation

---

### Transamination and Deamination

**Transamination**: Transfer of amino group from amino acid to α-keto acid
- **Enzymes**: Aminotransferases (ALT, AST) — require **pyridoxal phosphate (B6)**
- **ALT**: Alanine + α-KG → Pyruvate + Glutamate (liver specific)
- **AST**: Aspartate + α-KG → OAA + Glutamate

**Oxidative Deamination**: Glutamate → α-KG + NH3
- Enzyme: **Glutamate dehydrogenase** (liver mitochondria)
- Activated by: ADP, NAD+; Inhibited by: GTP, NADH

---

## Molecular Biology

### DNA Structure

> **PYQ HOTSPOT**: B-DNA vs Z-DNA, base pairing, Watson-Crick

| Feature | A-DNA | B-DNA | Z-DNA |
|---------|-------|-------|-------|
| Helix | Right-handed | **Right-handed** | **Left-handed** |
| Base pairs/turn | 11 | **10** | 12 |
| Form found in | Dehydrated conditions | **Normal physiological** | GC-rich regions |
| Groove | Wide major, narrow minor | Wide major, narrow minor | Narrow minor only |

**Base pairing** (Watson-Crick):
- **A = T** (2 hydrogen bonds)
- **G ≡ C** (3 hydrogen bonds) — **stronger; higher melting point with more G-C**

**Chargaff's rules**: A=T, G=C; A+G = T+C (pyrimidines = purines)

**Purines**: Adenine, Guanine (2 rings — "**PURe As Gold**")
**Pyrimidines**: Cytosine, Thymine, Uracil (1 ring — "**CUT the PY**")

---

### DNA Replication

> **PYQ HOTSPOT**: DNA polymerase functions, Okazaki fragments, enzymes

**Key Principle**: Semiconservative, bidirectional, 5'→3' synthesis

| Enzyme | Function |
|--------|----------|
| **Helicase** | Unwinds double helix at replication fork |
| **Primase** | Synthesizes RNA primer (required to start synthesis) |
| **DNA Pol I** | **Removes RNA primers, fills gaps; also 5'→3' exonuclease** |
| **DNA Pol II** | DNA repair |
| **DNA Pol III** | **Main replicative polymerase** in prokaryotes; 3'→5' proofreading exonuclease |
| **DNA Pol α** | **Primase activity** in eukaryotes |
| **DNA Pol δ** | **Main replicative polymerase** in eukaryotes (lagging strand) |
| **DNA Pol ε** | Leading strand in eukaryotes |
| **Ligase** | Joins Okazaki fragments (seals nicks) |
| **Topoisomerase I/II** | Relieves supercoiling; **target of quinolones and camptothecin** |
| **Telomerase** | Extends telomeres; uses its own RNA template; active in germ cells/cancer |

**Okazaki fragments**: Discontinuous synthesis on lagging strand; ~1000-2000 bp in prokaryotes

---

### Transcription

> **PYQ HOTSPOT**: RNA polymerases, promoter elements, alpha-amanitin sensitivity

**RNA Polymerases** (eukaryotic):
| Polymerase | Product | Inhibited By |
|-----------|---------|-------------|
| **RNA Pol I** | rRNA (28S, 18S, 5.8S) — largest rRNA | Not α-amanitin |
| **RNA Pol II** | **mRNA** (also snRNA) | **Low dose α-amanitin** |
| **RNA Pol III** | tRNA, 5S rRNA, snRNA | **High dose α-amanitin** |

**Mnemonic**: "1, 2, 3 = rRNA, mRNA, tRNA"

**Promoter elements**:
- **TATA box** (-25): Core promoter (RNA Pol II)
- **CAAT box** (-75): Increases transcription efficiency
- **GC box** (-90): Binding for Sp1 factor

**Post-transcriptional modifications** (eukaryotic mRNA):
1. **5' cap (7-methylguanosine)**: Added first; required for ribosome binding, protection
2. **3' poly-A tail**: Added after cleavage; stability, export
3. **Splicing**: Introns removed; **spliceosome (snRNPs)**; 5'-GU...AG-3' rule

---

### Translation

> **PYQ HOTSPOT**: Ribosome subunits, codons, antibiotic targets

**Ribosomes**:
| Ribosome | Prokaryote | Eukaryote |
|---------|-----------|----------|
| Whole | **70S** | **80S** |
| Large subunit | 50S (23S + 5S rRNA) | 60S (28S + 5.8S + 5S rRNA) |
| Small subunit | **30S** (16S rRNA) | **40S** (18S rRNA) |

**Genetic Code**:
- **AUG**: Start codon (Met in eukaryotes, fMet in prokaryotes)
- **UAA, UAG, UGA**: Stop codons (nonsense codons)
- **Degenerate**: Multiple codons for 1 amino acid; only **Met and Trp** have single codon
- **Wobble**: 3rd base of codon has flexibility in base pairing with anticodon

**Translation Steps**:
1. **Initiation**: AUG recognized; Met-tRNA in P site
2. **Elongation**: EF-Tu (aa-tRNA to A site), peptide bond (peptidyl transferase), translocation
3. **Termination**: Stop codon → Release factors → ribosome dissociation

**Antibiotic targets** (mnemonic: **"Buy AT 30, CCELL at 50"**):
- 30S: **Aminoglycosides** (irreversible), **Tetracyclines** (reversible)
- 50S: **Chloramphenicol** (peptidyl transferase), **Clindamycin**, **Erythromycin** (macrolides — translocation), **Linezolid**, **Lincomycin**

---

### Mutations

> **PYQ HOTSPOT**: Types, examples, repair mechanisms

| Mutation Type | Definition | Example |
|--------------|-----------|---------|
| **Transition** | Purine→Purine or Pyrimidine→Pyrimidine | A→G, C→T |
| **Transversion** | Purine→Pyrimidine or vice versa | A→T, G→C |
| **Missense** | AA change | Sickle cell (Glu→Val at codon 6) |
| **Nonsense** | Amino acid → Stop codon | |
| **Silent (synonymous)** | No AA change (wobble) | |
| **Frameshift** | Insertion/deletion → reading frame shift | |

**DNA Repair Mechanisms**:
| Repair | Defect Disease |
|--------|--------------|
| Nucleotide excision repair (NER) | **Xeroderma pigmentosum** (UV damage) |
| Base excision repair | Alkylated bases |
| Mismatch repair | **HNPCC/Lynch syndrome** (MLH1, MSH2) |
| Double-strand break repair (NHEJ/HR) | **BRCA1/2** (HR) |

---

### Molecular Techniques

> **PYQ HOTSPOT**: Blotting techniques, PCR, RFLP

| Technique | Detects | Probe/Primer | Mnemonic |
|-----------|---------|-------------|---------|
| **Southern blot** | **DNA** | DNA probe | **S**outhern = **D**NA |
| **Northern blot** | **RNA/mRNA** | DNA/RNA probe | **N**orthern = R**N**A |
| **Western blot** | **Protein** | Antibody | **W**estern = Protein |
| **Eastern blot** | Post-translationally modified proteins | - | |
| **ELISA** | Antigen/Antibody detection | Antibody | |

**PCR (Polymerase Chain Reaction)**:
- Steps: Denaturation (94°C) → Annealing (55-65°C) → Extension (72°C)
- Enzyme: **Taq polymerase** (thermostable, from Thermus aquaticus)
- **RT-PCR**: RNA → cDNA first (reverse transcriptase) → amplify

**RFLP (Restriction Fragment Length Polymorphism)**:
- Uses restriction enzymes to cut DNA at specific sequences
- Differences in fragment lengths → used for genetic mapping, paternity, diagnosis

**CRISPR-Cas9**:
- Guide RNA (gRNA) directs Cas9 endonuclease to specific DNA sequence
- Creates double-strand break → precise genome editing
- Applications: Gene therapy, genetic screening

---

## Vitamins

### Fat-Soluble Vitamins (A, D, E, K)

> **PYQ HOTSPOT**: Deficiency diseases, toxicity (stored in fat = toxic in excess)

| Vitamin | Function | Deficiency | Toxicity | Key Biochemistry |
|---------|----------|-----------|---------|-----------------|
| **A (Retinol)** | Vision (rhodopsin), epithelial differentiation, immune function | **Night blindness** (1st sign), xerophthalmia, Bitot spots, **follicular hyperkeratosis**, increased infections | Teratogenic, headache, hepatotoxicity, pseudotumor cerebri | 11-cis retinal + opsin = rhodopsin |
| **D (Calciferol)** | Ca2+ and PO4 absorption, bone mineralization | **Rickets** (children - bowed legs), **Osteomalacia** (adults), tetany | Hypercalcemia, nephrolithiasis, metastatic calcification | D3 (skin) → 25-OH D3 (liver) → **1,25-(OH)2 D3 = Calcitriol** (kidney, active form); **PTH activates 1α-hydroxylase** |
| **E (Tocopherol)** | Antioxidant (free radical scavenger), stabilizes cell membranes | Hemolytic anemia, **spinocerebellar ataxia**, neuropathy | Inhibits platelet aggregation, anticoagulant | Protects PUFA in membranes |
| **K (Phylloquinone)** | Cofactor for **γ-carboxylation of Glu** → Gla proteins | Bleeding (↑PT, ↑PTT), **hemorrhagic disease of newborn** | - | Activates: Factors **II, VII, IX, X**, Protein C, Protein S, Osteocalcin |

**Vitamin K and warfarin**: Warfarin inhibits **VKOR (Vitamin K epoxide reductase)** → prevents recycling of active Vitamin K

---

### Water-Soluble Vitamins

> **PYQ HOTSPOT**: Cofactor roles, deficiency syndromes

| Vitamin | Coenzyme | Function | Deficiency | Notes |
|---------|---------|----------|-----------|-------|
| **B1 (Thiamine)** | **TPP (Thiamine pyrophosphate)** | Oxidative decarboxylation | **Beriberi** (wet=cardiac, dry=neuro), **Wernicke-Korsakoff** (alcoholics) | Enzymes: **PDH, α-KG DH, Transketolase (PPP), BCAA DH** |
| **B2 (Riboflavin)** | **FAD, FMN** | Redox reactions | Angular stomatitis, cheilosis, corneal vascularization | Required for B6 activation |
| **B3 (Niacin)** | **NAD+, NADP+** | Redox reactions | **Pellagra**: Dermatitis, Diarrhea, Dementia (**3 D's**) + Death | Made from tryptophan (requires B6, B2); used to treat **dyslipidemia** (↑ HDL most) |
| **B5 (Pantothenic acid)** | **CoA, ACP** | Acyl transfer | Dermatitis, alopecia, adrenal insufficiency ("burning feet") | Part of CoA structure |
| **B6 (Pyridoxine)** | **PLP (Pyridoxal phosphate)** | Transamination, decarboxylation, glycogenolysis | **Sideroblastic anemia**, peripheral neuropathy, **isoniazid/OCP-induced deficiency** | Required for: aminotransferases, glycogen phosphorylase, heme synthesis (ALA synthase) |
| **B7 (Biotin)** | Biotin | Carboxylation reactions | Dermatitis, alopecia, glossitis | Avidin (egg white) binds biotin; Enzymes: **ACC, PC, MCC, PCC** |
| **B9 (Folate)** | **THF (Tetrahydrofolate)** | 1-carbon transfers (nucleotide synthesis) | **Megaloblastic anemia** (no neurological symptoms), **Neural tube defects** | Deficiency in **pregnancy** → NTDs; **MTX, TMP inhibit DHFR** |
| **B12 (Cobalamin)** | Methylcobalamin, Adenosylcobalamin | Myelin synthesis, DNA synthesis | **Megaloblastic anemia + SUBACUTE COMBINED DEGENERATION (dorsal + lateral columns)** | **Only animal sources**; requires **intrinsic factor** (parietal cells); stored in liver (years) |
| **C (Ascorbic acid)** | Electron donor | Collagen hydroxylation, iron absorption, antioxidant | **Scurvy**: perifollicular hemorrhage, gingival bleeding, poor wound healing, hemarthrosis | Required for **Prolyl/Lysyl hydroxylase** (collagen); enhances non-heme iron absorption |

**B12 vs Folate Deficiency**:
| Feature | B12 Deficiency | Folate Deficiency |
|--------|---------------|------------------|
| Megaloblastic anemia | Yes | Yes |
| Neurological symptoms | **Yes (SCD)** | **No** |
| Serum B12 | Low | Normal |
| Serum folate | High (trap) | Low |
| Methylmalonic acid | **High** | Normal |
| Homocysteine | High | High |
| Cause | IF deficiency, strict vegan, ileal disease | **Poor diet, alcoholism, pregnancy, MTX** |

---

## Enzymes

### Michaelis-Menten Kinetics

> **PYQ HOTSPOT**: Km meaning, Vmax, enzyme inhibition graphs

**Michaelis-Menten equation**: v = Vmax[S] / (Km + [S])

**Key terms**:
- **Km**: [S] at which v = Vmax/2; measures **affinity** (↓Km = ↑affinity)
- **Vmax**: Maximum velocity; proportional to total enzyme concentration
- **Kcat** (turnover number): reactions per enzyme per second
- **Catalytic efficiency** = Kcat/Km

**Lineweaver-Burk Plot** (double reciprocal: 1/v vs 1/[S]):
- Y-intercept = 1/Vmax
- X-intercept = -1/Km
- Slope = Km/Vmax

| Inhibitor Type | Km | Vmax | Lineweaver-Burk |
|---------------|----|----|----------------|
| **Competitive** | **↑** | **Unchanged** | Same Y-intercept, different slope (converge on Y-axis) |
| **Non-competitive** | **Unchanged** | **↓** | Same X-intercept, different slope (converge on X-axis) |
| **Uncompetitive** | **↓** | **↓** | **Parallel lines** (both change proportionally) |
| Mixed | ↑ or ↓ | ↓ | - |

**Competitive inhibition**: Overcome by excess substrate; binds active site
**Non-competitive**: Cannot be overcome; binds allosteric site; decreases Vmax

---

### Allosteric Enzymes

- **Sigmoidal (S-shaped)** kinetics (not hyperbolic)
- **Homotropic**: Same molecule as substrate is activator
- **Heterotropic**: Different molecule than substrate is modulator
- Examples: Hemoglobin (O2 binding), PFK-1 (AMP activator), pyruvate kinase

---

### Isoenzymes

> **PYQ HOTSPOT**: LDH in MI, CK in MI/muscle disease, ALP in liver vs bone

**LDH (Lactate Dehydrogenase) Isoenzymes**:
| Isoenzyme | Location | Elevated In |
|----------|---------|------------|
| **LDH-1** (HHHH) | **Heart, RBC** | **MI** (LDH1 > LDH2 = "flipped") |
| LDH-2 (HHHM) | Heart, RBC | Normal serum |
| LDH-3 | Lung, lymph nodes | |
| LDH-4 | Liver, kidney | |
| **LDH-5** (MMMM) | **Liver, skeletal muscle** | Liver disease |

**CK (Creatine Kinase) Isoenzymes**:
| Isoenzyme | Location | Elevated In |
|----------|---------|------------|
| **CK-MB** | **Heart** | **MI** (rises 4-6h, peaks 24h) |
| CK-MM | Skeletal muscle | Muscle disease, exercise |
| CK-BB | Brain | |

**ALP (Alkaline Phosphatase)**:
- Bone isoenzyme: Paget's disease, healing fractures, hyperparathyroidism
- Liver isoenzyme: Cholestasis, hepatic infiltration
- Placental isoenzyme: Pregnancy

**Troponin I and T**: Most specific markers for myocardial injury; rise 3-4h, peak 12-24h, remain elevated 7-10 days

---

## Collagen

### Types and Distribution

> **PYQ HOTSPOT**: Type I in OI, Type II in cartilage, Type IV in basement membrane

| Type | Composition | Location | Features |
|------|------------|---------|---------|
| **Type I** | 2α1, 1α2 | **Bone, tendon, skin, dentin, fascia** | Most abundant; **strongest**; "I have **1** bone" |
| **Type II** | 3α1 | **Cartilage, vitreous humor** | Hyaline cartilage |
| **Type III** | 3α1 | **Reticulin** (fetal skin, blood vessels, uterus) | **Ehlers-Danlos** type IV |
| **Type IV** | Non-fibrillar | **Basement membranes** | **Alport syndrome** (COL4A3/4/5 mutation); Goodpasture target antigen |
| **Type V** | - | Placenta, hair | |

---

### Collagen Synthesis Steps

> **PYQ HOTSPOT**: Scurvy = hydroxylation defect; requires Vitamin C

1. Procollagen α-chains synthesized on **rough ER** ribosomes
2. **Hydroxylation** of proline and lysine residues → **requires Vitamin C** and O2 (prolyl/lysyl hydroxylase); also Fe2+
3. **Glycosylation** (hydroxylysine residues)
4. Self-assembly into triple helix (procollagen)
5. Secretion from cell
6. **Cleavage** of propeptides → tropocollagen (procollagen peptidase)
7. **Crosslinking**: Lysyl oxidase (requires Cu2+) → covalent bonds

**Defect at each step**:
- Hydroxylation defect → **Scurvy** (Vit C deficiency)
- Crosslinking defect → **Menkes disease** (Cu2+ deficiency) or **Lathyrism** (beta-aminopropionitrile from sweet peas)

---

### Collagen Disorders

| Disorder | Defect | Type | Features |
|---------|--------|------|---------|
| **Osteogenesis Imperfecta** | Collagen **Type I** mutation (Gly substitution) | AD/AR | **Blue sclerae, multiple fractures, hearing loss, dental abnormalities**; most common: Gly → Ala substitution |
| **Ehlers-Danlos Syndrome** | Various (EDS Classic: Col5A; EDS Vascular: Col3A) | Multiple | **Hyperextensible skin, hypermobile joints, easy bruising**; Vascular type: arterial rupture, most severe |
| **Scurvy** | Defective hydroxylation (Vit C deficiency) | - | Perifollicular hemorrhage, corkscrew hairs, gingival bleeding, hemarthrosis, poor wound healing |
| **Alport Syndrome** | **Type IV collagen** (COL4A3/4/5) | X-linked/AR | Progressive nephritis + **sensorineural deafness** + ocular abnormalities; **"lamellated/split" GBM** on EM |

---

## Tumor Markers

> **PYQ HOTSPOT**: Specific associations, monitoring vs diagnosis

| Tumor Marker | Associated Tumors | Notes |
|-------------|------------------|-------|
| **AFP (Alpha-fetoprotein)** | **HCC, Yolk sac tumor (endodermal sinus)**, hepatoblastoma | Elevated in pregnancy (NTDs); normally produced by yolk sac, liver, GI tract |
| **CEA (Carcinoembryonic antigen)** | **Colorectal cancer** (most specific), also gastric, pancreatic, lung, breast | Not specific; used for **monitoring recurrence**, not screening |
| **CA-125** | **Ovarian cancer** (epithelial) | Also elevated in endometriosis, PID; monitoring treatment |
| **CA 19-9** | **Pancreatic cancer**, also cholangiocarcinoma, gastric | Lewis antigen negative individuals don't express CA 19-9 |
| **PSA (Prostate-specific antigen)** | **Prostate cancer** | Also elevated in BPH, prostatitis; serine protease; monitoring |
| **TRAP (Tartrate-resistant acid phosphatase)** | **Hairy cell leukemia** | CD11c, CD25, CD103 positive |
| **hCG (Human chorionic gonadotropin)** | **Gestational trophoblastic disease** (choriocarcinoma), testicular germ cell tumors | Normal in pregnancy; very high in choriocarcinoma |
| **LDH** | **Lymphomas, leukemias**, testicular germ cell tumors, Ewing sarcoma | Non-specific; indicates tumor burden |
| **Beta-2 microglobulin** | **Multiple myeloma**, lymphomas | Prognosis |
| **Calcitonin** | **Medullary thyroid carcinoma** | C cells of thyroid; part of MEN2A/2B |
| **Thyroglobulin** | **Differentiated thyroid cancer** (papillary/follicular) | Monitoring after thyroidectomy |
| **Chromogranin A** | Neuroendocrine tumors, carcinoid | |
| **5-HIAA** | **Carcinoid tumor** (serotonin metabolite) | 24-hour urine collection |

---

## High-Yield Quick Review

### Energy Metabolism Summary
- **Glycolysis**: 2 ATP net (anaerobic); cytoplasm
- **TCA cycle**: 10 ATP/acetyl-CoA; mitochondria
- **Oxidative phosphorylation**: ~26 ATP/glucose; inner mitochondrial membrane
- **Beta-oxidation**: Mitochondrial matrix; palmitate → 106 ATP

### Rate-Limiting Enzymes Summary
| Pathway | Rate-Limiting Enzyme | Activator | Inhibitor |
|---------|---------------------|-----------|----------|
| Glycolysis | PFK-1 | AMP, F2,6-BP | ATP, citrate |
| Gluconeogenesis | FBPase | ATP, citrate | AMP, F2,6-BP |
| Glycogen synthesis | Glycogen synthase | Glucose, insulin | Glucagon, epinephrine |
| Glycogen breakdown | Glycogen phosphorylase | AMP, glucagon | ATP, G6P, insulin |
| FA synthesis | ACC | Citrate, insulin | Palmitoyl-CoA, glucagon |
| FA oxidation | CPT-I | - | Malonyl-CoA |
| Ketogenesis | HMG-CoA synthase | Fasting | Insulin |
| Cholesterol synthesis | HMG-CoA reductase | Insulin | Statins, cholesterol |
| PPP | G6PD | NADP+ | NADPH |
| Urea cycle | CPS-I | NAG | - |

### Biotin-Dependent Enzymes (mnemonic: "PPAM CC")
- **P**yruvate carboxylase (pyruvate → OAA)
- **P**ropionyl-CoA carboxylase (propionyl-CoA → methylmalonyl-CoA)
- **A**cetyl-CoA carboxylase (acetyl-CoA → malonyl-CoA)
- **M**ethylcrotonyl-CoA carboxylase (leucine catabolism)

### Pyridoxal Phosphate (B6)-Dependent Enzymes
- All **aminotransferases** (ALT, AST)
- **ALA synthase** (heme synthesis - 1st and rate-limiting step)
- **Glycogen phosphorylase**
- **Cystathionine beta-synthase** (homocysteine → cystathionine)
- **Decarboxylases** (DOPA decarboxylase, histidine decarboxylase)

---

*Last updated: 2026 | NEET PG Biochemistry High-Yield Notes*
