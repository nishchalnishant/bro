"""
DIRECT_URLS — maps every local image filename (from download_images.py SEARCHES)
to either:
  • A https://commons.wikimedia.org/wiki/Special:FilePath/<name> URL  (Commons)
  • A https://radiopaedia.org/articles/<slug> article URL             (Radiopaedia placeholder)
  • None  — no reliable free source known; search/license manually

Sources: IMAGE-SOURCES.md + download_images.py SEARCHES keys.
For entries whose IMAGE-SOURCES.md entry says only "Search:" (no direct File: or URL),
the value is None — do not guess.
"""

def _wp(filename):
    """Return the Special:FilePath redirect URL for a Wikimedia Commons File:."""
    return f"https://commons.wikimedia.org/wiki/Special:FilePath/{filename}"


DIRECT_URLS = {

    # ── RADIOLOGY ──────────────────────────────────────────────────────────────

    # These filenames are from download_images.py but map to the IMAGE-SOURCES.md
    # entries by subject.  Radiopaedia entries use the article URL.
    "radiology-air-bronchogram.jpg":
        "https://radiopaedia.org/articles/air-bronchogram",
    "radiology-silhouette-sign-cardiorespiratory.jpg":
        "https://radiopaedia.org/articles/silhouette-sign-cardiomediastinal",
    "radiology-bat-wing-sign-pulmonary-oedema.jpg":
        "https://radiopaedia.org/articles/bat-wing-sign-pulmonary-oedema",
    "radiology-hampton-hump.jpg":
        "https://radiopaedia.org/articles/hampton-hump-sign",
    "radiology-westermark-sign.jpg":
        "https://radiopaedia.org/articles/westermark-sign",
    "radiology-kerley-lines.jpg":
        "https://radiopaedia.org/articles/kerley-lines",
    "radiology-codman-triangle.jpg":
        "https://radiopaedia.org/articles/codmans-triangle",
    "radiology-sunburst-pattern-osteosarcoma.jpg":
        "https://radiopaedia.org/articles/sunburst-pattern-1",
    "radiology-ewing-sarcoma-of-bone.jpg":
        "https://radiopaedia.org/articles/ewings-sarcoma",
    "radiology-rigler-sign.jpg":
        "https://radiopaedia.org/articles/riglers-sign",
    "radiology-coffee-bean-sign-sigmoid-volvulus.jpg":
        "https://radiopaedia.org/articles/sigmoid-volvulus",
    "radiology-string-sign-of-kantor.jpg":
        "https://radiopaedia.org/articles/string-sign-of-kantor",
    "radiology-thumbprinting-sign-large-bowel.jpg":
        "https://radiopaedia.org/articles/thumbprinting-sign-colon",
    "radiology-crescent-sign-avascular-necrosis.jpg":
        "https://radiopaedia.org/articles/crescent-sign-avascular-necrosis",
    "radiology-double-line-sign-avascular-necrosis.jpg":
        "https://radiopaedia.org/articles/crescent-sign-avascular-necrosis",  # same article
    "radiology-lemon-sign.jpg":
        "https://radiopaedia.org/articles/lemon-sign",
    "radiology-banana-sign.jpg":
        "https://radiopaedia.org/articles/banana-sign",

    # ── GENERAL MEDICINE ───────────────────────────────────────────────────────

    "general-medicine-atrial-fibrillation.jpg":
        _wp("Afib_ecg.jpg"),
    "general-medicine-ventricular-tachycardia.jpg":
        _wp("VT_ECG.jpg"),
    "general-medicine-hyperkalaemia-ecg-changes.jpg":
        _wp("Hyperkalemia_changes_ECG.png"),
    "general-medicine-pulmonary-oedema.jpg":
        "https://radiopaedia.org/articles/pulmonary-oedema",
    "general-medicine-cardiomegaly.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "general-medicine-pulmonary-tuberculosis-1.jpg":
        "https://radiopaedia.org/articles/pulmonary-tuberculosis-1",
    "general-medicine-st-elevation.jpg":
        _wp("Inferior_STEMI.jpg"),
    "general-medicine-papilloedema.jpg":
        _wp("Papilledema.jpg"),
    "general-medicine-diabetic-retinopathy.jpg":
        _wp("Fundus_photograph_of_normal_left_eye.jpg"),  # background DR image from IMAGE-SOURCES.md
    "rheumatoid-hand-deformities.jpg":
        _wp("Rheumatoid_Arthritis.JPG"),
    "sle-malar-rash.jpg":
        _wp("Lupus_erythematosus_(LE)_cell.jpg"),
    "ecg-digoxin-reverse-tick.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "ecg-qt-prolongation-torsades.jpg":
        _wp("Torsades_de_pointes.png"),
    "hyperkalaemia-sine-wave-ecg.jpg":
        _wp("Hyperkalemia_changes_ECG.png"),
    "t-wave-inversion-ischaemia-ecg.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "anterior-mi-q-waves-ecg.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "jvp-waveform.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name; Search: only
    "frank-starling-curve.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name; Search: only
    "pressure-volume-loop.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name; Search: only
    "wiggers-diagram.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name; Search: only

    # ── GENERAL SURGERY ────────────────────────────────────────────────────────

    "general-surgery-acute-appendicitis.jpg":
        "https://radiopaedia.org/articles/appendicitis",
    "general-surgery-tension-pneumothorax.jpg":
        "https://radiopaedia.org/articles/tension-pneumothorax",
    "general-surgery-keloid.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "general-surgery-breast-carcinoma.jpg":
        "https://radiopaedia.org/articles/breast-carcinoma",
    "general-surgery-gallstones.jpg":
        "https://radiopaedia.org/articles/cholelithiasis",
    "general-surgery-pneumoperitoneum.jpg":
        "https://radiopaedia.org/articles/riglers-sign",
    "general-surgery-inguinal-hernia.jpg":
        None,   # no specific direct URL in IMAGE-SOURCES.md
    "general-surgery-direct-inguinal-hernia.jpg":
        _wp("Hesselbach%27s_triangle.png"),
    "general-surgery-papillary-thyroid-carcinoma.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "hesselbachs-triangle-laparoscopy-direct-hernia.jpg":
        _wp("Hesselbach%27s_triangle.png"),
    "calots-triangle-laparoscopic-cholecystectomy.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "caput-medusae-portal-hypertension.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "mcburneys-point-surface-marking.jpg":
        _wp("McBurneys_point.jpg"),

    # ── ORTHOPEDICS ────────────────────────────────────────────────────────────

    "orthopedics-bamboo-spine.jpg":
        "https://radiopaedia.org/articles/bamboo-spine",
    "orthopedics-developmental-dysplasia-of-the-hip.jpg":
        "https://radiopaedia.org/articles/shentons-line",
    "orthopedics-legg-calve-perthes-disease.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "orthopedics-slipped-upper-femoral-epiphysis.jpg":
        "https://radiopaedia.org/articles/slipped-capital-femoral-epiphysis",
    "orthopedics-colles-fracture.jpg":
        "https://radiopaedia.org/articles/colles-fracture",
    "orthopedics-smith-fracture.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "orthopedics-scaphoid-fracture.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "orthopedics-scoliosis.jpg":
        _wp("Cobb_angle_scoliosis.jpg"),
    "orthopedics-scotty-dog-sign.jpg":
        "https://radiopaedia.org/articles/scottie-dog-sign",
    "orthopedics-brodie-abscess.jpg":
        "https://radiopaedia.org/articles/brodies-abscess",
    "orthopedics-acute-osteomyelitis.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "orthopedics-codman-triangle.jpg":
        "https://radiopaedia.org/articles/codmans-triangle",
    "orthopedics-ewing-sarcoma-of-bone.jpg":
        "https://radiopaedia.org/articles/ewings-sarcoma",
    "orthopedics-giant-cell-tumour-of-bone.jpg":
        "https://radiopaedia.org/articles/giant-cell-tumour-of-bone",
    "orthopedics-fibrous-dysplasia.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "orthopedics-lumbar-disc-herniation.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "orthopedics-multiple-myeloma-skeletal-manifestations.jpg":
        "https://radiopaedia.org/articles/multiple-myeloma",
    "orthopedics-garden-classification-of-femoral-neck-fractures.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "rickets-xray-cupping-fraying-metaphyses.jpg":
        "https://radiopaedia.org/articles/rickets",
    "xray-rickets-wrist.jpg":
        "https://radiopaedia.org/articles/rickets",
    "pathological-fracture-lytic-metastasis-xray.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "scaphoid-fracture-MRI-STIR.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known

    # ── OPHTHALMOLOGY ──────────────────────────────────────────────────────────

    "ophthalmology-central-retinal-artery-occlusion.jpg":
        _wp("Central_retinal_artery_occlusion.jpg"),
    "ophthalmology-central-retinal-vein-occlusion.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "ophthalmology-glaucomatous-cupping.jpg":
        _wp("Cupped_disc.jpg"),
    "ophthalmology-herpes-simplex-keratitis.jpg":
        _wp("Dendritic_corneal_ulcer.jpg"),
    "ophthalmology-hypopyon.jpg":
        _wp("Hypopyon.jpg"),
    "ophthalmology-kayser-fleischer-ring.jpg":
        _wp("Kayser-Fleischer_ring.jpg"),
    "ophthalmology-rhegmatogenous-retinal-detachment.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "ophthalmology-relative-afferent-pupillary-defect.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "ophthalmology-papilloedema.jpg":
        _wp("Papilledema.jpg"),
    "ophthalmology-diabetic-retinopathy.jpg":
        _wp("Diabetic_retinopathy_photocoagulation_scarring.jpg"),
    "fundoscopy-diabetic-retinopathy-pdr-nvd.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only (proliferative DR / NVD)
    "proliferative-diabetic-retinopathy-fundus.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "hypertensive-retinopathy-fundus.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "visual-field-bitemporal-hemianopia-pituitary.jpg":
        _wp("Bitemporal_hemianopia.svg"),
    "visual-field-homonymous-hemianopia-mca-stroke.jpg":
        _wp("Homonymous_hemianopia.svg"),
    "visual-field-arcuate-scotoma-glaucoma.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "visual-field-pie-in-sky-temporal-lobe.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "hirschberg-test-esotropia.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "colposcopy-acetowhite.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "colposcopy-mosaic.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "colposcopy-punctation.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "colposcopy-schiller-test.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "slit-lamp-keratic-precipitates-mutton-fat.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known

    # ── ENT ────────────────────────────────────────────────────────────────────

    "ent-audiogram.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "ent-cholesteatoma.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "ent-chronic-suppurative-otitis-media.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "ent-laryngeal-squamous-cell-carcinoma.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "ent-maxillary-sinusitis.jpg":
        "https://radiopaedia.org/articles/maxillary-sinusitis",
    "ent-sinonasal-polyposis.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "ent-steeple-sign.jpg":
        "https://radiopaedia.org/articles/croup",
    "ent-thumbprint-sign-epiglottitis.jpg":
        "https://radiopaedia.org/articles/epiglottitis",
    "ent-tympanic-membrane.jpg":
        _wp("Ear_drum.jpg"),
    "ent-vocal-cord-paralysis.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only

    # ── ANATOMY ────────────────────────────────────────────────────────────────

    "brachial-plexus-roots-trunks-divisions-cords-branches.jpg":
        _wp("Brachial_plexus.svg"),
    "axilla-cross-section-brachial-plexus-cords.jpg":
        _wp("Brachial_plexus_in_axilla.png"),
    "erb-palsy-waiters-tip.jpg":
        _wp("Brachial_plexus_in_axilla.png"),
    "klumpke-palsy-total-claw-hand.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "saturday-night-palsy-wrist-drop-radial-nerve.jpg":
        _wp("Wrist_drop.jpg"),
    "winged-scapula-long-thoracic-nerve.jpg":
        _wp("Winged_scapula.jpg"),
    "popes-blessing-hand-high-median-nerve.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "ape-hand-median-nerve-palsy.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "carpal-tunnel-thenar-wasting-median-nerve.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "claw-hand-ulnar-nerve.jpg":
        _wp("Claw_hand.jpg"),
    "froments-sign-ulnar-nerve.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "ain-palsy-ok-sign-pinch-test.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "pin-palsy-finger-drop-radial-nerve.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "foot-drop-common-peroneal-nerve.jpg":
        _wp("Foot_drop.jpg"),
    "trendelenburg-sign-superior-gluteal-nerve.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "anatomical-snuffbox-surface-marking.jpg":
        _wp("Anatomical_snuff_box.jpg"),
    "femoral-triangle-navy-cross-section.jpg":
        _wp("Femoral_triangle.png"),
    "posterior-triangle-neck-brachial-plexus.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "cubital-fossa-contents-diagram.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "lumbosacral-plexus-diagram.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "dermatome-map-trunk-spinal-levels.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "upper-limb-dermatome-map-spinal-levels.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "cavernous-sinus-coronal-mri.jpg":
        "https://radiopaedia.org/articles/cavernous-sinus",
    "lesser-sac-foramen-of-winslow-axial-ct.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "collagen-triple-helix-structure.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known

    # ── PHYSIOLOGY ─────────────────────────────────────────────────────────────

    "o2-hb-dissociation-curve.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "action-potential-trace.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "spirometry-trace-obstructive-restrictive.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "flow-volume-loop.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "renal-glucose-clearance-curve.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "eeg-wave-patterns.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "coagulation-cascade-diagram.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "coagulation-cascade-heparin-warfarin.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "complement-cascade-three-pathways.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "dopamine-pathways-schizophrenia.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "autonomic-receptor-diagram.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name

    # ── BIOCHEMISTRY ───────────────────────────────────────────────────────────

    "glycolysis-pathway-pfk1.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "tca-cycle-diagram.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "electron-transport-chain-oxidative-phosphorylation.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "fatty-acid-synthesis-vs-beta-oxidation-compartments.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "lipoprotein-structure-size-comparison.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "urea-cycle-diagram.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "pku-metabolic-pathway.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "dna-replication-fork-diagram.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known

    # ── PHARMACOLOGY ───────────────────────────────────────────────────────────

    "pharmacokinetic-elimination-curves.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "dose-response-curves-agonist-antagonist.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "therapeutic-index-ed50-ld50.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "beta-lactam-ring-structures.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "antidepressant-synapse-mechanisms.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "mac-values-inhalational-agents.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "train-of-four-tof-monitoring.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "spinal-anesthesia-baricity-meninges.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "malignant-hyperthermia-ryr1-cascade.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "succinylcholine-hyperkalemia-ecg.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known

    # ── PATHOLOGY ──────────────────────────────────────────────────────────────

    "hydropic-change-cellular-edema.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "coagulative-necrosis-myocardial-infarct.jpg":
        _wp("Coagulative_necrosis_of_myocardium.jpg"),
    "langhans-vs-foreign-body-giant-cell.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "caseous-necrosis-tuberculous-lung-gross.jpg":
        _wp("Caseous_necrosis.jpg"),
    "caseating-granuloma-tuberculosis-langhans.jpg":
        _wp("Granuloma_with_Langhans_type_giant_cells.jpg"),
    "foam-cells-fatty-streak-atherosclerosis.jpg":
        _wp("Foam_cells.jpg"),
    "fatty-streak-aorta-gross.jpg":
        _wp("Fatty_streaks_aorta.jpg"),
    "wavy-fibers-coagulative-necrosis-mi-early.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "tb-granuloma-caseous-necrosis-histology.jpg":
        _wp("Granuloma_with_Langhans_type_giant_cells.jpg"),
    "type-i-hypersensitivity-ige-mast-cell-degranulation.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "type-ii-hypersensitivity-antibody-cell-surface-cytotoxicity.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "type-iii-hypersensitivity-immune-complex-deposition.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "type-iv-delayed-hypersensitivity-th1-macrophage-activation.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "histology-cin1.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "histology-cin3.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known

    # ── MICROBIOLOGY ───────────────────────────────────────────────────────────

    "ziehl-neelsen-acid-fast-bacilli-mtb-red-rods-blue-background.jpg":
        _wp("Ziehl_Neelson_stain.jpg"),
    "gram-stain-s-aureus-gram-positive-cocci-clusters.jpg":
        _wp("Staphylococcus_aureus_gram_stain.jpg"),
    "koh-mount-candida-pseudohyphae-blastoconidia.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "germ-tube-test-candida-albicans-true-hyphae.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "aspergillus-septate-hyphae-acute-angle-branching.jpg":
        _wp("Aspergillus_fumigatus.jpg"),
    "halo-sign-invasive-aspergillosis-ct-chest-ground-glass-halo.jpg":
        "https://radiopaedia.org/articles/halo-sign-pulmonary",
    "aspergilloma-crescent-sign-chest-xray-fungal-ball-cavity.jpg":
        "https://radiopaedia.org/articles/aspergilloma",
    "india-ink-cryptococcus-capsule-halo-csf.jpg":
        _wp("Cryptococcus_neoformans_using_a_light_India_ink_staining_preparation.jpg"),
    "malaria-thin-film-falciparum-ring-trophozoites-crescent-gametocyte.jpg":
        _wp("Plasmodium_falciparum_01.png"),
    "malaria-thin-film-vivax-schuffner-dots-enlarged-rbc.jpg":
        _wp("Plasmodium_vivax_thin_film.jpg"),
    "ghon-complex-primary-tb-chest-xray-calcified-focus-hilar-nodes.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "hbv-serology-timeline-window-period-markers.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "hiv-western-blot-gp120-gp41-p24-bands.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only
    "koplik-spots-measles.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known

    # ── FORENSIC MEDICINE ──────────────────────────────────────────────────────
    # All forensic entries in IMAGE-SOURCES.md are "Search:" only or
    # "Forensic pathology atlas" (not freely hotlinkable). All None.

    "rigor-mortis-distribution-pattern-progression.jpg":  None,
    "livor-mortis-fixed-vs-unfixed-blanching-test.jpg":    None,
    "livor-mortis-color-comparison-normal-cherry-red-co-poisoning.jpg": None,
    "putrefaction-marbling-green-discoloration-right-iliac-fossa.jpg":  None,
    "adipocere-vs-mummification-comparison-preservation-types.jpg":     None,
    "incised-wound-clean-margins-no-tissue-bridges.jpg":   None,
    "lacerated-wound-tissue-bridges-abraded-margins.jpg":  None,
    "stab-wound-entry-shape-single-double-edged-blade.jpg": None,
    "co-poisoning-cherry-red-skin-globus-pallidus-necrosis.jpg":        None,
    "critoe-elbow-ossification-centers-xray-age-sequence.jpg":
        "https://radiopaedia.org/articles/critoe",
    "gustafson-tooth-age-estimation-six-criteria-cross-section.jpg":    None,
    "contact-range-gunshot-stellate-tear-muzzle-imprint-co-muscle.jpg": None,
    "close-range-gunshot-blackening-soot-singeing.jpg":    None,
    "intermediate-range-gunshot-tattooing-stippling-powder-grains.jpg": None,
    "distant-range-gunshot-entry-contusion-ring-grease-ring-only.jpg":  None,
    "entry-vs-exit-wound-comparison-contusion-ring-everted-margins.jpg": None,

    # ── COMMUNITY MEDICINE / EPIDEMIOLOGY ──────────────────────────────────────

    "2x2-contingency-table-sensitivity-specificity.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "roc-curve-auc-interpretation.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "normal-distribution-bell-curve-sd-zones.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "forest-plot-meta-analysis.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "funnel-plot-publication-bias.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "growth-monitoring-road-to-health-card.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "epidemic-curve-shapes-point-propagated-continuous.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "vaccine-cold-chain-temperature-zones.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "silicosis-chest-xray-eggshell-calcification.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "asbestosis-chest-xray-pleural-plaques.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known

    # ── PEDIATRICS ─────────────────────────────────────────────────────────────

    "developmental-milestone-chart.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "neonatal-jaundice-kramer-zones.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "cxr-neonatal-rds.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "cxr-tga-egg-on-side.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "cxr-tof-boot-shaped-heart.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "measles-maculopapular-rash.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "marasmus-clinical-appearance.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "kwashiorkor-edema-flag-sign.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "malnutrition-kwashiorkor.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "malnutrition-marasmus.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "bitots-spots-xerophthalmia-vitamin-a.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "pellagra-casals-necklace-niacin-deficiency.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "pellagra-rash-casals-necklace.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name (same subject, two local names)
    "angular-cheilitis-b2-deficiency.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "angular-stomatitis-riboflavin-b2-deficiency.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "goitre-iodine-deficiency.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name
    "scurvy-gum-hemorrhage-perifollicular.jpg":
        None,   # IMAGE-SOURCES.md lists "Wikimedia Commons" but no File: name

    # ── OBG ────────────────────────────────────────────────────────────────────

    "ctg-early-decelerations.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "ctg-late-decelerations.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "ctg-variable-decelerations.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "ctg-sinusoidal-pattern.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "usg-ectopic-adnexal-ring-sign.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "usg-pcos-necklace-sign.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "usg-placenta-accreta.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "usg-placenta-previa-complete.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "hysteroscopy-endometrial-polyp.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "hysteroscopy-submucous-fibroid.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "hysteroscopy-uterine-septum.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known

    # ── DERMATOLOGY ────────────────────────────────────────────────────────────

    "dermatology-psoriasis.jpg":
        None,   # IMAGE-SOURCES.md: "Search:" only (Auspitz/Koebner entries)

    # ── PSYCHIATRY ─────────────────────────────────────────────────────────────

    "cage-questionnaire-table.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "alcohol-withdrawal-timeline.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known

    # ── CT/MRI BRAIN ───────────────────────────────────────────────────────────

    "ct-brain-cmv-periventricular-calcifications.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
    "ct-brain-toxoplasma-diffuse-calcifications.jpg":
        None,   # not in IMAGE-SOURCES.md; no direct URL known
}
