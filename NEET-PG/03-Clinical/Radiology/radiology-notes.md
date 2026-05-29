# Radiology - NEET PG High-Yield Notes

> 📊 [PYQ Analysis for this subject](../../04-PYQ-Analysis/Subject-Wise/subject-wise-pyq.md#radiology) | 🗂️ [Master Index](../../00-Master-Index/master-index.md) | 📝 [MCQs](radiology-mcqs.md)

## 📊 PYQ Snapshot (NEET PG 2019–2024)

| Year | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | Avg |
|------|------|------|------|------|------|------|-----|
| Questions | 4 | 4 | 4 | 4 | 4 | 4 | **4** |

**Trend:** Stable — exactly 4 questions every year.

### Top High-Yield Topics
1. Chest X-ray patterns — bat-wing, honeycomb, ground glass, consolidation
2. CXR cardiac silhouette — cardiomegaly, specific chamber enlargement
3. CT findings — intracranial bleeds (hyperdense vs hypodense)
4. Contrast agents — types, reactions, contraindications
5. Radiation safety — units (Gy, Sv), ALARA principle
6. Interventional radiology — ERCP, PTBD, angioplasty indications
7. MRI — T1 vs T2 signal characteristics
8. Nuclear medicine — HIDA scan, bone scan, MIBG indications

> **Strategy:** CXR interpretation (topics 1–2) accounts for 2 of the 4 questions almost every year. These overlap with Medicine — master them once, score twice.

---

## RADIATION PHYSICS

### Types of Radiation

| Type | Nature | Penetration | Medical Use |
|------|--------|------------|------------|
| **X-rays** | Electromagnetic; photons | High | Diagnostic imaging, fluoroscopy |
| **Gamma rays** | Electromagnetic; photons (from nucleus) | High | Nuclear medicine |
| **Alpha (α)** | Helium nucleus (2p+2n) | Very low (skin) | Radiolabeled therapy (Ra-223) |
| **Beta (β)** | Electrons | Low (few mm tissue) | Radioiodine (I-131), TACE |
| **Neutrons** | Neutral particles | High | Neutron capture therapy |

- **Ionizing radiation**: X-rays, gamma rays, alpha, beta, neutrons (have enough energy to ionize atoms)
- **Non-ionizing**: UV, infrared, microwaves, radio waves, sound (ultrasound), MRI (magnetic field)

### X-ray Production (PYQ HOTSPOT)

| Mechanism | Description | Properties |
|----------|------------|-----------|
| **Bremsstrahlung (braking radiation)** | Electrons decelerated by nuclear field → X-ray emitted; variable energy | **Continuous spectrum** of X-ray energies; forms majority of beam |
| **Characteristic radiation** | Electron ejects inner shell electron (e.g., K-shell) → higher shell electron fills vacancy → X-ray emitted at specific energy | **Discrete energy**; tube-specific; only above threshold kVp |

### kVp vs mA Effects

| Parameter | Effect on Image Quality |
|----------|----------------------|
| **kVp (tube voltage)** | **Penetrating power of X-rays**; ↑kVp = more penetrating beam, less contrast (more grey tones), less dose |
| **mA (tube current)** | **Number/quantity of X-rays**; ↑mA = more X-rays = brighter image, more dose |
| **mAs (mA × time)** | Total radiation exposure to patient; determines image density/darkness |
| **Focal spot size** | ↓Focal spot = sharper image but more heat; ↑focal spot = blurrier but can handle more power |

---

## RADIATION SAFETY

### ALARA Principle
**A**s **L**ow **A**s **R**easonably **A**chievable - balance between benefit of imaging and radiation risk

### Radiation Dose Units (PYQ HOTSPOT)

| Unit | Definition | SI Unit | Old Unit | Conversion |
|------|-----------|---------|---------|-----------|
| **Gray (Gy)** | Absorbed dose = energy deposited per unit mass | 1 Gy = 1 J/kg | Rad | 1 Gy = 100 Rad |
| **Sievert (Sv)** | Effective dose = Gy × radiation weighting factor (W_R) | Sv | Rem | 1 Sv = 100 Rem |
| **Roentgen (R)** | Ionization in air | C/kg | R | 1 R ≈ 0.01 Gy (in air) |
| **Becquerel (Bq)** | Radioactivity = 1 disintegration/sec | Bq | Curie (Ci) | 1 Ci = 3.7 × 10^10 Bq |

**Radiation Weighting Factors (W_R):**
- X-rays, gamma rays, electrons: **W_R = 1**
- Protons: W_R = 5
- **Alpha particles: W_R = 20** (most damaging per gray)
- Neutrons: W_R = 5-20 (energy dependent)

### Dose Limits (PYQ HOTSPOT)

| Category | Annual Dose Limit |
|---------|-----------------|
| **Occupational workers** | **20 mSv/year** (averaged over 5 years; not >50 mSv in any single year) |
| **General public** | **1 mSv/year** |
| **Pregnant radiation worker** | **1 mSv for gestation** (fetal dose) |
| **Students <18 years** | 1 mSv/year |
| **Lens of eye** | 20 mSv/year |
| **Skin/hands/feet** | 500 mSv/year |

**Typical Effective Doses:**
- CXR: 0.02 mSv
- Chest CT: 7 mSv
- Abdominal CT: 8-10 mSv
- PET-CT: 15-25 mSv
- Background radiation (annual): 2.4 mSv

### Radiation Protection (PYQ HOTSPOT)

**Three pillars: Distance, Shielding, Time**

- **Inverse Square Law**: Dose ∝ 1/distance²; double the distance = **¼ the dose**
- **Lead apron**: Equivalent to **0.25 mm Pb** (reduces dose by >90% for diagnostic X-rays)
- **Thyroid shield**: Protects thyroid (high radiosensitivity)
- **Gonadal shield**: For reproductive organs; mandatory for patients of reproductive age unless it would obscure area of interest

**Radiosensitivity (order - most to least sensitive):**
Lymphocytes > Gonads > Bone marrow > Intestinal epithelium > Skin > Liver > Kidney > Muscle > Brain/Nerve (mature)

**High-dose effects:**
- >1 Gy: Acute radiation syndrome
- **>6 Gy**: Bone marrow failure; LD50 without treatment ~3-4 Gy
- **Teratogenesis**: Greatest risk **8-15 weeks** (organogenesis + CNS development); threshold ~100 mGy fetal dose

---

## PLAIN X-RAY INTERPRETATION

### Systematic Approach to CXR
**ABCDE approach**: Airways/Bones/Cardiac/Diaphragm/Everything else (lung fields, soft tissue)

### Mediastinal Widening (PYQ HOTSPOT)

| Compartment | Contents | Pathology |
|------------|---------|---------|
| **Superior mediastinum** | Great vessels, trachea, thymus | **Aortic dissection/aneurysm, vascular lesions** |
| **Anterior mediastinum** | Thymus, lymph nodes, fat | **4 T's: Thymoma, Teratoma, Thyroid (retrosternal), Terrible lymphoma** |
| **Middle mediastinum** | Heart, pericardium, great vessels, trachea | Pericardial effusion, enlarged hilar nodes, bronchogenic cyst |
| **Posterior mediastinum** | Esophagus, descending aorta, spinal canal, sympathetic chain | Neurogenic tumor (most common - neurofibroma/schwannoma), esophageal lesions |

**Aortic dissection on CXR**: Widened mediastinum (>8 cm), left pleural effusion, calcium sign (>6mm from intimal edge), loss of aortic knuckle

### Pleural Effusion (PYQ HOTSPOT)
- **Amount visible**: >200 mL on PA CXR; >50 mL on lateral (blunting costophrenic angle)
- **Meniscus sign**: Curved upper border of fluid (free-flowing effusion)
- **Massive effusion**: White-out with mediastinal shift to **contralateral** side
- **Loculated effusion**: D-shaped opacity; no meniscus; fixed on decubitus view
- **Subpulmonary effusion**: Elevated "pseudodiaphragm"; peak lateral on right
- **Exudate vs Transudate**: Light's criteria (protein, LDH)

### Pneumothorax
- **Absent lung markings** peripheral
- **Visceral pleural line**: White line with no vessels beyond
- **Tension pneumothorax**: Mediastinal shift to **contralateral** side + depressed ipsilateral diaphragm; **clinical emergency - don't wait for X-ray**
- **Deep sulcus sign**: On supine CXR (ICU patients) - lucency in costophrenic angle

### Pulmonary Patterns

| Pattern | X-ray Appearance | Key Causes |
|---------|-----------------|-----------|
| **Consolidation** | Airspace opacity; air bronchograms | Pneumonia, pulmonary edema |
| **Atelectasis** | Volume loss + white-out; displacement of fissures/mediastinum toward lesion | Mucus plug, endobronchial lesion |
| **Cavitation** | Opacity with central lucency + air-fluid level | TB, abscess, fungal, squamous cell Ca, Wegener's |
| **Miliary** | Innumerable tiny (1-3mm) diffuse nodules | TB (miliary), fungal, sarcoid, silicosis |
| **Nodular** | Discrete rounded opacity <3cm | Metastases, granuloma, primary lung Ca |
| **Ground glass** | Haziness; vessels still visible through it | Interstitial edema, PCP, AIP, NSIP |
| **Honeycombing** | Cystic spaces (5-10mm) in clusters; subpleural | UIP/IPF (end-stage fibrosis) |

### Cardiac Silhouette
- **CTR (Cardiothoracic Ratio)**: >0.5 on PA CXR = cardiomegaly (>0.55 on AP CXR)
- **Right heart border**: SVC (upper), right atrium (lower)
- **Left heart border**: Aortic knuckle (top), pulmonary trunk, left atrial appendage, left ventricle
- **Pericardial effusion**: Globular "water bottle" heart; rapid size change on serial films; no pulmonary edema (differentiates from CCF)

---

## CT SCAN

### Hounsfield Units (HU) (PYQ HOTSPOT)

| Tissue | HU |
|--------|-----|
| Air | **-1000** |
| Fat | **-100 to -80** |
| Water | **0** |
| Soft tissue/muscle | **+20 to +80** |
| Blood (acute) | **+40 to +70** |
| Calcification/bone cortex | **+400 to +1000** |
| Metal | **+3000** |

**Key:** HU is linear; water = reference 0

### CT Windows (PYQ HOTSPOT)

| Window | Width (WW) | Level (WL) | Use |
|--------|-----------|-----------|-----|
| **Lung window** | 1500 | -600 | Lung parenchyma, airways |
| **Bone window** | 2000 | 500 | Cortical bone, fractures |
| **Soft tissue window** | 400 | 40 | Abdominal organs, liver, muscle |
| **Brain window** | 80 | 35 | Intracranial pathology |
| **Subdural window** | 300 | 50 | Subdural hematoma detection |

**Principle:** WW controls contrast; WL determines center; narrow window = better contrast; wide window = more structures visible simultaneously

### CT Applications

**CT Pulmonary Angiography (CTPA):**
- **Gold standard for PE diagnosis**
- Filling defects in pulmonary arteries
- Saddle embolus: Straddles main pulmonary artery bifurcation
- Hampton's hump: Wedge-shaped pleural-based opacity (infarction)

**HRCT for ILD (PYQ HOTSPOT):**

| HRCT Pattern | Disease | Appearance |
|-------------|---------|-----------|
| **Honeycombing** | **UIP/IPF** | Clustered cysts 3-10mm; subpleural; lower lobe |
| **Ground glass** | NSIP, AIP, PCP | Hazy opacity; vessels visible |
| **Reticulation** | Any fibrosis | Network of lines |
| **Tree-in-bud** | Endobronchial TB, bronchiectasis | Centrilobular nodules + branching lines |
| **Crazy paving** | **PAP, AIP, lipoid pneumonia** | Ground glass + superimposed septal lines |
| **Mosaic attenuation** | Constrictive obliterative bronchiolitis, hypersensitivity | Patchy lucency (air trapping) |

**Head CT (PYQ HOTSPOT):**
- **Hyperdense (white)**: Acute blood (SAH, acute SDH, EDH, hypertensive hemorrhage), calcification
- **Hypodense (dark)**: Edema, infarction (becomes visible 6-12 hours), chronic blood, CSF
- **Isodense**: Subacute SDH (2-3 weeks old); easy to miss
- **Hyperdense MCA**: Acute MCA thrombus on plain CT (early sign of MCA territory infarct)

---

## MRI

### Basic Principles

**T1 Relaxation (Spin-Lattice):**
- Energy transfer from proton spin to surrounding lattice
- **T1-weighted images**: FAT appears bright; fluid appears dark
- Short TR, Short TE → T1 weighting

**T2 Relaxation (Spin-Spin):**
- Energy transfer between protons
- **T2-weighted images**: FLUID appears bright; fat intermediate
- Long TR, Long TE → T2 weighting

**Mnemonic: "FAT T1; FLUID T2"** (PYQ HOTSPOT)

### Signal Intensities (PYQ HOTSPOT)

| Structure | T1 | T2 | Notes |
|---------|-----|-----|------|
| **Fat** | **Bright** | Intermediate/bright | STIR suppresses fat |
| **Free water/CSF** | **Dark** | **Bright** | |
| **Muscle** | Intermediate | Intermediate | |
| **Cortical bone** | **Dark** | **Dark** | No mobile protons |
| **Air** | Dark | Dark | No protons |
| **Acute blood (deoxyhemoglobin)** | Dark | **Dark** | Paramagnetic |
| **Subacute blood (methemoglobin)** | **Bright** | Bright (intracellular) | |
| **Chronic blood (hemosiderin)** | **Dark** | **Dark** | Magnetic susceptibility |
| **Gadolinium contrast** | **Bright** | - | T1 shortening |
| **Protein-rich fluid** | Intermediate-bright | Bright | |

### MRI Sequences (PYQ HOTSPOT)

| Sequence | Full Name | Use | Key Feature |
|---------|-----------|-----|------------|
| **T1** | - | Anatomy, fat, blood products, post-contrast | FAT bright |
| **T2** | - | Fluid, edema, most pathology "lights up" | FLUID bright |
| **FLAIR** | Fluid Attenuated Inversion Recovery | **Suppress CSF**; periventricular lesions, MS plaques | CSF dark; lesions bright |
| **DWI** | Diffusion Weighted Imaging | **Acute stroke** (bright DWI + dark ADC = restricted diffusion) | Ischemia within minutes |
| **ADC** | Apparent Diffusion Coefficient | Confirms DWI restriction | Dark in ischemia (true restriction) |
| **GRE/SWI** | Gradient Echo/Susceptibility | Blood products, calcification, cavernoma | **Blooming effect** - exaggerates blood |
| **STIR** | Short Tau Inversion Recovery | **Suppress fat**; bone marrow edema; soft tissue | Fat dark; edema bright |
| **MRS** | MR Spectroscopy | Metabolite peaks; tumor vs necrosis | NAA, Cho, Cr peaks |
| **MRA** | MR Angiography | Vascular imaging; no contrast (TOF) or contrast | Vessel anatomy |

### MRI Contraindications (PYQ HOTSPOT)
**Absolute:**
- **Cardiac pacemakers** (most traditional - check manufacturer; newer are MR conditional)
- **Cochlear implants** (most)
- Ferromagnetic intraocular foreign body
- Ferromagnetic intracranial aneurysm clips (older types)
- Magnetically activated implants

**Relative:**
- **Gadolinium in CKD (GFR <30)**: Risk of **Nephrogenic Systemic Fibrosis (NSF)**
- Pregnancy (especially first trimester) - gadolinium contraindicated
- Severe claustrophobia
- Metallic joint replacements (artifacts; usually safe)
- Tattoos (iron-containing ink)

---

## ULTRASOUND

### Principles (PYQ HOTSPOT)
- Uses **sound waves** (non-ionizing, no radiation)
- **Frequency-Resolution-Penetration tradeoff**: Higher frequency = better resolution but less penetration
  - High frequency (7-15 MHz): Superficial structures (thyroid, breast, testis, small parts)
  - Low frequency (2-5 MHz): Deep structures (abdomen, pelvis, cardiac)

### Echogenicity
- **Hyperechoic**: Brighter than reference; appears white (bone, calculi, fat, gas - with posterior shadowing for calculi)
- **Isoechoic**: Same as reference
- **Hypoechoic**: Darker than reference; soft tissue solid lesion
- **Anechoic**: No echoes; appears black (simple fluid - cyst, urine, bile, blood vessels)

**Posterior enhancement**: Behind anechoic structures (fluid transmits well) - differentiates cyst from solid
**Posterior acoustic shadowing**: Behind highly reflective surfaces (calculi, bone, gas)

### Doppler Ultrasound (PYQ HOTSPOT)

**Color Doppler Convention:**
- **BART mnemonic**: **B**lue **A**way, **R**ed **T**owards (probe)
- Blood flowing **toward** probe = **Red**
- Blood flowing **away** from probe = **Blue**
- **High-velocity/turbulent flow**: Color aliasing (wraparound of colors)

**Types of Doppler:**
- **Duplex**: B-mode + pulsed Doppler; DVT diagnosis (loss of compressibility + absence of flow)
- **Color flow**: Real-time color-coded flow direction
- **Power Doppler**: Sensitive to slow flow; no directional info; not angle-dependent

### FAST Examination (PYQ HOTSPOT)
**Focused Assessment with Sonography for Trauma**

| View | Location Assessed |
|------|-----------------|
| **Hepatorenal (Morrison's pouch)** | Right upper quadrant; most dependent; free fluid collects here first |
| **Splenorenal** | Left upper quadrant |
| **Pericardial** | Subxiphoid/subcostal; pericardial effusion |
| **Pelvic (Pouch of Douglas)** | Most dependent pelvic position |
| **eFAST** (extended) | + Bilateral lung bases for pneumothorax (B lines/lung sliding absent) |

**Positive FAST**: Free fluid (anechoic stripe) in any window
- Unstable patient + positive FAST → **emergency surgery** (not CT)
- Stable patient + positive FAST → CT for staging

### Abdominal USG Findings

| Condition | USG Finding |
|----------|------------|
| **Gallstones** | Echogenic foci + **posterior acoustic shadowing** + movement with gravity |
| **Cholecystitis** | Thickened GB wall >3mm + pericholecystic fluid + positive sonographic Murphy's sign |
| **Liver metastases** | Multiple hypoechoic (or hyperechoic) lesions |
| **HCC** | Heterogeneous mass; vascular invasion; Doppler flow |
| **Renal calculus** | Echogenic focus + shadowing; hydronephrosis if obstructing |
| **Hydronephrosis** | Dilated collecting system; anechoic pelvicalyceal dilation |
| **AAA** | Dilated aorta (>3 cm); mural thrombus |
| **DVT** | Incompressible vein; absent flow on Doppler |

### Thyroid Nodule - TI-RADS (PYQ HOTSPOT)

| Feature | Suspicious for Malignancy |
|---------|--------------------------|
| Microcalcifications | **High risk** |
| Irregular margins | High risk |
| Taller-than-wide | High risk (AP diameter > transverse) |
| Hypoechoic (vs thyroid) | Moderate risk |
| Solid | Moderate |
| Coarse calcification/eggshell | Lower risk |

**TI-RADS 1-2**: Benign (follow up or no action)
**TI-RADS 4-5**: FNA recommended
**FNAC result**: Bethesda system (I-VI) for thyroid nodules

---

## NUCLEAR MEDICINE

### PET Scan (PET-CT) (PYQ HOTSPOT)
- **Tracer**: **F-18 FDG (fluorodeoxyglucose)** - glucose analog; taken up by metabolically active cells
- **Principle**: Glucose uptake → β+ emission → annihilation → 2 gamma photons (511 keV) in opposite directions → coincidence detection
- **SUV (Standardized Uptake Value)**: Measure of FDG uptake; **SUV >2.5 = malignant** (general threshold)
- **Uses**: Cancer staging, recurrence detection, treatment response, solitary pulmonary nodule, unknown primary
- **False positives**: Inflammation, infection, brown fat, post-treatment changes
- **False negatives**: Small lesions, mucinous tumors, low-grade tumors (prostate, renal, hepatocellular in some)

### Bone Scan (PYQ HOTSPOT)
- **Tracer**: **Tc-99m MDP (methylene diphosphonate)** - most commonly used
- **Principle**: Localizes to areas of increased osteoblastic activity
- **Triple phase**: Angiographic (flow), blood pool, delayed (bone)
- **Indications**: Bony metastases (breast, prostate, lung), osteomyelitis, Paget's disease, stress fractures, AVN
- **Hot spots** (increased uptake): Osteoblastic mets, osteomyelitis, fractures, Paget's
- **Cold spots** (photopenia): **Multiple myeloma** (lytic, no osteoblastic activity - bone scan may miss!), early AVN, radiation therapy
- **Superscan**: Diffuse increased uptake throughout skeleton (metastatic prostate/breast cancer)

### Thyroid Scan (PYQ HOTSPOT)
- **Tracers**: Tc-99m pertechnetate (trapped but not organified) or I-123/I-131
- **Hot nodule**: Increased uptake (functioning/autonomous); **benign** (suppressed TSH)
- **Cold nodule**: Decreased uptake; **higher malignancy risk (~20%)** - needs FNA
- **Warm nodule**: Same as surrounding gland; intermediate risk
- **Thyroid cancer**: Usually cold; use PET-CT for recurrence

### Meckel's Scan (PYQ HOTSPOT)
- **Tracer**: **Tc-99m pertechnetate** - taken up by **gastric mucosa (parietal cells)**
- **Indication**: Suspected Meckel's diverticulum with ectopic gastric mucosa (painless rectal bleeding in children)
- **Enhancement**: Pentagastrin, cimetidine (blocks secretion without blocking uptake)
- **Sensitivity increased by**: Cimetidine pretreatment

### SPECT vs PET

| Feature | SPECT | PET |
|---------|-------|-----|
| Tracers | Tc-99m, Tl-201, I-123 | F-18, Ga-68, C-11 |
| Resolution | Lower (8-10 mm) | Better (4-6 mm) |
| Gamma cameras | Rotating | Coincidence detection |
| Quantification | Limited | Better (SUV) |
| Cost | Lower | Higher |

---

## INTERVENTIONAL RADIOLOGY

### Angiography
- **DSA (Digital Subtraction Angiography)**: **Gold standard for vascular imaging**; iodinated contrast; bone/soft tissue subtracted; only vessels visible
- **Common femoral artery**: Standard access (Seldinger technique); guide wire → sheath → catheter
- **Seldinger technique**: Needle → guide wire → dilator → sheath/catheter over wire

### ERCP (Endoscopic Retrograde Cholangiopancreatography)
- **Diagnostic and therapeutic**: Biliary and pancreatic duct
- **Indications**: Choledocholithiasis, biliary stricture, stenting, sphincterotomy
- **Complications**: Pancreatitis (most common, 3-5%), bleeding, perforation, cholangitis
- **MRCP**: Non-invasive alternative for diagnosis; no therapy possible

### Percutaneous Procedures
- **CT-guided biopsy**: Liver, lung, kidney, retroperitoneal; core needle preferred for histology
- **US-guided procedures**: Drainages (abscess, pleural effusion, ascites)
- **Nephrostomy**: Obstructed kidney; antegrade drainage; US-guided
- **Biliary drainage (PTC/PTBD)**: Percutaneous transhepatic cholangiography + drainage; failed ERCP

### TIPS (Transjugular Intrahepatic Portosystemic Shunt)
- **Creates shunt between portal and hepatic veins** through liver parenchyma
- **Indications**: Refractory variceal bleeding, refractory ascites, Budd-Chiari
- **Complications**: Hepatic encephalopathy (shunts ammonia away from liver), stent stenosis/occlusion

### TACE (Transarterial Chemoembolization)
- **Treatment for HCC** (hepatocellular carcinoma)
- Combines intra-arterial chemotherapy (doxorubicin/cisplatin) with embolization (particles/lipiodol)
- **Principle**: Hepatic artery supplies HCC; portal vein supplies normal liver; selective hepatic artery embolization kills tumor

---

## RADIOLOGICAL SIGNS - HIGH YIELD (PYQ HOTSPOT)

### Pulmonary Signs

| Sign | Condition | Description |
|------|---------|------------|
| **Bat wing / Butterfly** | Pulmonary edema | Bilateral perihilar air-space opacity with clear costophrenic angles |
| **Hampton's hump** | Pulmonary embolism | Wedge-shaped pleural-based opacity (hemorrhagic infarction) |
| **Westermark sign** | Pulmonary embolism | Focal oligemia (decreased vascular markings) distal to occluded vessel |
| **Fleischner sign** | Pulmonary embolism | Enlarged pulmonary artery due to clot in main/lobar PA |
| **Tree-in-bud** | Endobronchial TB, bronchiectasis | Centrilobular nodules + branching structures (mucus/pus in bronchioles) |
| **Signet ring sign** | **Bronchiectasis** | Dilated bronchus + adjacent pulmonary artery; ring + dot |
| **Honeycombing** | UIP/IPF | Clustered 3-10mm cysts; subpleural; worst prognosis in ILD |
| **Air crescent sign** | **Aspergilloma in cavity** | Air crescent around fungal ball (Aspergillus) |
| **Monospot sign / Egg-shell calcification** | Silicosis/Sarcoid | Calcification of peripheral lymph nodes |

### Abdominal Signs (PYQ HOTSPOT)

| Sign | Condition | Description |
|------|---------|------------|
| **String sign of Kantor** | **Crohn's disease** | String-like narrowing of terminal ileum on barium (fibrotic stricture) |
| **Apple core / Napkin ring** | **Colorectal carcinoma** | Annular narrowing of colon (encircling tumor) |
| **Double duct sign** | **Pancreatic head carcinoma** | Simultaneous dilation of CBD + pancreatic duct on CT/MRCP/ERCP |
| **Bird beak** | **Achalasia** (esophagus) | Smooth tapering at LES on barium swallow |
| **Rat tail** | CBD stone/achalasia | Gradual tapering narrowing |
| **Stack of coins / Coil spring** | **Intussusception** | Concentric mucosal folds on barium enema; coil spring = reduced intussusception |
| **Cobblestone pattern** | **Crohn's disease** | Thickened mucosa with ulcers (deep transverse + longitudinal ulcers) on barium |
| **Whirlpool sign** | **Midgut volvulus** | Swirling of mesenteric vessels around SMA on CT |
| **Coffee bean sign** | **Sigmoid volvulus** | Inverted U-shaped loop on plain AXR; apex points to LUQ |
| **Rigler sign** | **Pneumoperitoneum** | Both walls of bowel visible (air on both sides) |
| **Football sign** | **Massive pneumoperitoneum** | Large oval lucency in abdomen (neonate) |
| **Mercedes-Benz sign** | Gallstone (pneumobilia) | Air in bile ducts (Y-shape) on plain AXR |
| **Air under right hemidiaphragm** | Perforation | Free gas; erect CXR best |
| **Lead pipe appearance** | **Ulcerative colitis** | Loss of haustrations, featureless colon on barium |
| **Rose thorn / Collar stud ulcer** | UC/Crohn's | Deep ulceration; flask/collar stud shape |

### Skeletal Signs (PYQ HOTSPOT)

| Sign | Condition | Description |
|------|---------|------------|
| **Codman's triangle** | **Osteosarcoma** (and any aggressive bone lesion) | Elevated periosteum at tumor margins; triangle of bone |
| **Sunburst pattern** | **Osteosarcoma** | Perpendicular periosteal spicules radiating from bone |
| **Onion peel / Onion skin** | **Ewing's sarcoma** | Layers of periosteal reaction (lamellated) |
| **Soap bubble** | **GCT / Aneurysmal bone cyst** | Expansile, multiloculated lytic appearance |
| **Erlenmeyer flask** | **Gaucher's disease** (also Niemann-Pick) | Failure of bone remodeling; expanded distal femur metaphysis |
| **Looser's zones** | **Osteomalacia** | Linear lucent bands (pseudofractures); perpendicular to cortex; incomplete fractures |
| **Rugger jersey spine** | **Renal osteodystrophy** | Alternating bands of density in vertebral bodies |
| **Scottie dog sign** | **Spondylolysis** | On oblique lumbar X-ray; collar on Scottie dog = pars defect |
| **Trolley track sign** | **Ankylosing spondylitis** | Bamboo spine; calcified interspinous ligaments (3 parallel lines) |
| **Punched-out lesions** | **Multiple myeloma** | Lytic lesions without sclerotic rim; skull, pelvis |
| **Ground glass bone** | Fibrous dysplasia | Hazy/ground glass matrix within expanded bone |
| **Blade of grass** | **Paget's disease** (tibia) | V-shaped lytic front advancing through bone |
| **Cotton-wool skull** | **Paget's disease** | Mixed lytic/sclerotic skull changes |

### CNS Signs (PYQ HOTSPOT)

| Sign | Condition | Description |
|------|---------|------------|
| **Hyperdense MCA sign** | **Acute MCA territory ischemic stroke** | Dense clot in MCA on non-contrast CT; early sign |
| **Hyperdense cisterns / Star sign** | **Subarachnoid hemorrhage (SAH)** | Blood in CSF spaces; Fisher grade |
| **Crescent-shaped hyperdense** | **Acute subdural hematoma (SDH)** | Concave inner margin following brain contour; venous (bridging veins) |
| **Biconvex lenticular hyperdense** | **Acute extradural hematoma (EDH)** | Convex inner margin; does NOT cross sutures; **arterial (MMA)** |
| **Periventricular white matter lesions** | **Multiple sclerosis** | Ovoid lesions perpendicular to lateral ventricles (Dawson's fingers); FLAIR bright |
| **Ring-enhancing lesion** | Abscess/GBM/metastasis/toxoplasmosis | Post-contrast enhancing ring; DWI/MRS/clinical context differentiates |
| **Figure-of-eight/Butterfly glioma** | **Glioblastoma multiforme (GBM)** | Corpus callosum crossing mass |
| **Target sign** | **Cerebral toxoplasmosis** | Concentric rings on contrast CT/MRI |
| **Empty sella** | Empty sella syndrome | CSF herniates into sella; flattened pituitary |
| **Midline shift calculation** | Mass effect | Shift of midline structures (falx, septum pellucidum); >5mm = significant |

---

## CT vs MRI COMPARISON (PYQ HOTSPOT)

| Feature | CT | MRI |
|---------|-----|-----|
| **Radiation** | Ionizing radiation | **No radiation** (magnetic field + radiofrequency) |
| **Scan time** | Fast (seconds) | Slow (minutes) |
| **Patient cooperation** | Less required | More required (longer, noisier) |
| **Bone** | **Better** (high resolution) | Poor (black signal) |
| **Soft tissue** | Moderate | **Excellent** |
| **Brain hemorrhage (acute)** | **Better** (hyperdense) | Acute blood can be isointense T1/T2 |
| **Stroke (acute, <6h)** | Poor for ischemia | **DWI excellent** (minutes) |
| **Spinal cord/disc** | Poor | **Best modality** |
| **MSK (soft tissue)** | Adequate | **Best** |
| **Lung** | **Best** (HRCT) | Poor |
| **Liver characterization** | Good with contrast | **Better (multisequence)** |
| **Contrast agent** | Iodinated (nephrotoxic) | Gadolinium (NSF in CKD) |
| **Contraindications** | Contrast allergy, CKD (relative) | Pacemakers, ferromagnetic implants |
| **Emergency** | **Preferred** (fast) | Not ideal in emergency |
| **Cost** | Moderate | High |

---

## SPECIFIC RADIOLOGICAL INVESTIGATIONS BY CONDITION

| Condition | Investigation of Choice |
|---------|----------------------|
| **Acute PE** | **CTPA** (CT pulmonary angiography) |
| **Acute stroke** | Non-contrast CT (hemorrhage exclusion); MRI DWI (ischemia) |
| **SAH** | Non-contrast CT first; MRI FLAIR if negative + high suspicion |
| **Temporal bone fracture** | High-resolution CT |
| **Disc prolapse** | MRI lumbar spine |
| **Soft tissue sarcoma** | MRI (staging), CT chest (lung mets) |
| **Bone mets (most tumors)** | Bone scan (Tc-99m MDP) |
| **Myeloma bone lesions** | Skeletal survey (plain X-rays) or whole-body MRI/PET-CT (more sensitive) |
| **DVT** | **Duplex ultrasound** |
| **AAA screening** | Ultrasound abdomen |
| **Thyroid nodule** | Ultrasound thyroid ± FNA |
| **Jaundice (obstructive)** | Ultrasound first → MRCP |
| **Biliary duct visualization** | **MRCP** (non-invasive); ERCP (therapeutic) |
| **Pancreatic cancer staging** | CT abdomen/chest/pelvis (triphasic) |
| **HCC diagnosis** | Triphasic CT/MRI (arterial enhancement + washout) |
| **Renal artery stenosis** | MR angiography / CT angiography / Duplex |
| **Pheochromocytoma localization** | CT/MRI first; then **MIBG scan** if negative |
| **Neuroendocrine tumor** | **Octreotide scan (In-111 pentetreotide)** or **Ga-68 DOTATATE PET** |
| **Lymphoma staging** | **PET-CT** |
| **Meckel's diverticulum** | **Tc-99m pertechnetate scan (Meckel's scan)** |

---

## MAMMOGRAPHY AND BREAST IMAGING

### Mammography
- **Screening**: Women 40-74 years (USMLE/ACS guidelines); Every 2 years from 50 (UK); Annual from 40 (ACS)
- **Diagnostic features of malignancy**: Spiculated mass, clustered microcalcifications, architectural distortion, asymmetric density
- **Benign features**: Smooth round mass, coarse calcifications, lucent center calcifications, vascular calcifications
- **BIRADS** classification determines management (1-6)

### Breast Ultrasound
- **Adjunct to mammography** in dense breasts
- **Anechoic + posterior enhancement**: Simple cyst (benign)
- **Irregular hypoechoic mass**: Suspicious for malignancy
- **Guidance for biopsy**: US-guided core biopsy (most common)

---

## RADIATION DOSE - COMPARATIVE (PYQ HOTSPOT)

| Examination | Effective Dose |
|------------|--------------|
| CXR (PA) | 0.02 mSv |
| Skull X-ray | 0.07 mSv |
| Lumbar spine X-ray | 1.3 mSv |
| **Chest CT** | **7 mSv** |
| **Abdomen/pelvis CT** | **10 mSv** |
| PET-CT | 15-25 mSv |
| Annual background | 2.4 mSv |
| CTPA | 4-10 mSv |

---

## PYQ HOTSPOT QUICK REVISION

1. **HU values**: Air -1000; Water 0; Fat -100 to -80; Bone +1000
2. **Occupational dose limit**: 20 mSv/year
3. **ALARA principle**: As Low As Reasonably Achievable
4. **Inverse square law**: Double distance = quarter dose
5. **T1 bright**: FAT; **T2 bright**: FLUID (mnemonic: FAT T1, FLUID T2)
6. **Acute blood on CT**: Hyperdense; **Old infarct/edema**: Hypodense
7. **EDH**: Biconvex lenticular; arterial; does NOT cross sutures
8. **SDH**: Crescent-shaped; venous; CROSSES sutures
9. **SAH**: Hyperdense cisterns; Fisher scale
10. **Hyperdense MCA sign**: Acute MCA territory infarct
11. **DWI**: Acute ischemia within minutes (bright DWI, dark ADC)
12. **FLAIR**: CSF suppressed; MS plaques visible (Dawson's fingers)
13. **CTPA**: Gold standard for PE
14. **Hampton's hump**: Wedge-shaped opacity in PE (infarction)
15. **Westermark sign**: Oligemia in PE
16. **Codman's triangle**: Aggressive bone lesion/osteosarcoma
17. **Onion peel**: Ewing's sarcoma
18. **Soap bubble**: GCT/ABC
19. **Sunburst**: Osteosarcoma
20. **Blade of grass**: Paget's disease (tibia lytic front)
21. **Double duct sign**: Pancreatic head carcinoma
22. **String of Kantor**: Crohn's ileum
23. **Apple core**: Colorectal carcinoma
24. **Meckel's scan**: Tc-99m pertechnetate (gastric mucosa)
25. **Cold thyroid nodule**: Higher malignancy risk
26. **Bone scan cold**: Multiple myeloma (lytic; no osteoblastic activity)
27. **PET tracer**: F-18 FDG; SUV >2.5 suspicious for malignancy
28. **FAST exam**: 4 windows for trauma; unstable + positive = OR
29. **Acoustic shadowing**: Calculi on USG; **posterior enhancement**: Cyst
30. **BART Doppler**: Blue Away, Red Towards
