#!/usr/bin/env python3
"""
Download real medical images using Wikimedia REST API to find correct URLs.
Uses the /w/api.php endpoint to get actual image URLs.
"""

import os
import sys
import time
import json
import urllib.request
import urllib.parse
import urllib.error

DEST = "/Users/nishchalnishant/Documents/GitHub/bro/NEET-PG/images"

# Map: local filename -> Wikimedia Commons exact filename (case-sensitive)
# These are the EXACT filenames as stored on Wikimedia Commons
WIKI_FILES = {
    # ── RADIOLOGY ──
    "radiology-air-bronchogram.jpg": "Air_bronchograms_on_chest_x-ray_RML_pneumonia.jpg",
    "radiology-silhouette-sign-cardiorespiratory.jpg": "Chest_Xray_PA_3-8-2010.png",
    "radiology-bat-wing-sign-pulmonary-oedema.jpg": "Pulmonary_edema_x-ray.jpg",
    "radiology-hampton-hump.jpg": "Pulmonary_embolism_with_hamptom_hump.jpg",
    "radiology-westermark-sign.jpg": "Pulmonary_embolism_with_hamptom_hump.jpg",
    "radiology-kerley-lines.jpg": "Kerley_B_Lines.jpg",
    "radiology-codman-triangle.jpg": "Osteosarcoma_-_Codman_triangle.jpg",
    "radiology-sunburst-pattern-osteosarcoma.jpg": "Osteosarcoma_-_Sunburst_appearance.jpg",
    "radiology-ewing-sarcoma-of-bone.jpg": "Ewing_sarcoma_-_xray_-_Radiopaedia.jpg",
    "radiology-rigler-sign.jpg": "Rigler_sign.jpg",
    "radiology-coffee-bean-sign-sigmoid-volvulus.jpg": "Volvulusxray.jpg",
    "radiology-string-sign-of-kantor.jpg": "Crohn_s_disease_-_string_sign.jpg",
    "radiology-thumbprinting-sign-large-bowel.jpg": "Ischaemic_colitis.jpg",
    "radiology-crescent-sign-avascular-necrosis.jpg": "Avascular_necrosis_of_the_femoral_head.jpg",
    "radiology-double-line-sign-avascular-necrosis.jpg": "Avascular_necrosis_MRI.jpg",
    "radiology-lemon-sign.jpg": "Lemon_sign_ultrasound.jpg",
    "radiology-banana-sign.jpg": "Banana_sign_Chiari_II.jpg",

    # ── GENERAL MEDICINE ──
    "general-medicine-atrial-fibrillation.jpg": "Afib_ecg.jpg",
    "general-medicine-ventricular-tachycardia.jpg": "VT_ECG.jpg",
    "general-medicine-hyperkalaemia-ecg-changes.jpg": "Hyperkalemia_ECG_changes.jpg",
    "general-medicine-pulmonary-oedema.jpg": "Pulmonary_edema_x-ray.jpg",
    "general-medicine-cardiomegaly.jpg": "Cardiomegaly.jpg",
    "general-medicine-pulmonary-tuberculosis-1.jpg": "TB_CXR.jpg",
    "general-medicine-st-elevation.jpg": "Inferior_STEMI.jpg",
    "general-medicine-papilloedema.jpg": "Papilledema.jpg",
    "general-medicine-diabetic-retinopathy.jpg": "Fundus_diabetic_retinopathy.jpg",
    "rheumatoid-hand-deformities.jpg": "Rheumatoid_Arthritis.JPG",
    "sle-malar-rash.jpg": "Malar_rash_of_lupus.jpg",
    "ecg-digoxin-reverse-tick.jpg": "Digoxin_effect.jpg",
    "ecg-qt-prolongation-torsades.jpg": "Torsades_de_pointes.png",
    "hyperkalaemia-sine-wave-ecg.jpg": "Hyperkalemia_ECG_changes.jpg",
    "t-wave-inversion-ischaemia-ecg.jpg": "T_wave_inversion_ECG.jpg",
    "anterior-mi-q-waves-ecg.jpg": "Inferior_STEMI.jpg",
    "jvp-waveform.jpg": "Jugular_venous_pressure_waveform.jpg",
    "frank-starling-curve.jpg": "Frank-Starling_mechanism.jpg",
    "pressure-volume-loop.jpg": "Pressure_volume_relationship.jpg",
    "wiggers-diagram.jpg": "Wiggers_Diagram.svg",

    # ── GENERAL SURGERY ──
    "general-surgery-acute-appendicitis.jpg": "Acute_appendicitis_CT.jpg",
    "general-surgery-tension-pneumothorax.jpg": "Tension_pneumothorax_on_CXR.jpg",
    "general-surgery-keloid.jpg": "Keloid.jpg",
    "general-surgery-breast-carcinoma.jpg": "Mammo_breast_cancer_wArrows.jpg",
    "general-surgery-gallstones.jpg": "Gallstones_ultrasound.jpg",
    "general-surgery-pneumoperitoneum.jpg": "Pneumoperitoneum.jpg",
    "general-surgery-inguinal-hernia.jpg": "Inguinal_hernia_repair.jpg",
    "general-surgery-direct-inguinal-hernia.jpg": "Inguinalhernia.gif",
    "general-surgery-papillary-thyroid-carcinoma.jpg": "Papillary_thyroid_carcinoma_2.jpg",
    "hesselbachs-triangle-laparoscopy-direct-hernia.jpg": "Hesselbach%27s_triangle.jpg",
    "calots-triangle-laparoscopic-cholecystectomy.jpg": "Gallbladder_laparoscopy.jpg",
    "caput-medusae-portal-hypertension.jpg": "Caput_medusae.jpg",
    "mcburneys-point-surface-marking.jpg": "McBurneys_point.jpg",

    # ── ORTHOPEDICS ──
    "orthopedics-bamboo-spine.jpg": "Bamboo_spine_x-ray.jpg",
    "orthopedics-developmental-dysplasia-of-the-hip.jpg": "DDH.jpg",
    "orthopedics-legg-calve-perthes-disease.jpg": "Perthes_disease.jpg",
    "orthopedics-slipped-upper-femoral-epiphysis.jpg": "Slipped_capital_femoral_epiphysis.jpg",
    "orthopedics-colles-fracture.jpg": "Colles_fracture.jpg",
    "orthopedics-smith-fracture.jpg": "Smith_fracture.jpg",
    "orthopedics-scaphoid-fracture.jpg": "Scaphoid_fracture.jpg",
    "orthopedics-scoliosis.jpg": "Scoliosis_xray.jpg",
    "orthopedics-scotty-dog-sign.jpg": "Scottie_dog_sign.jpg",
    "orthopedics-brodie-abscess.jpg": "Brodie_abscess.jpg",
    "orthopedics-acute-osteomyelitis.jpg": "Osteomyelitis_xray.jpg",
    "orthopedics-codman-triangle.jpg": "Osteosarcoma_-_Codman_triangle.jpg",
    "orthopedics-ewing-sarcoma-of-bone.jpg": "Ewing_sarcoma_-_xray_-_Radiopaedia.jpg",
    "orthopedics-giant-cell-tumour-of-bone.jpg": "Giant_cell_tumor_of_bone.jpg",
    "orthopedics-fibrous-dysplasia.jpg": "Fibrous_dysplasia.jpg",
    "orthopedics-lumbar-disc-herniation.jpg": "Lumbar_disc_herniation_MRI.jpg",
    "orthopedics-multiple-myeloma-skeletal-manifestations.jpg": "Multiple_myeloma_skull.jpg",
    "orthopedics-garden-classification-of-femoral-neck-fractures.jpg": "Hip_fracture_xray.jpg",
    "rickets-xray-cupping-fraying-metaphyses.jpg": "Rickets_UOTW_52_-_UOTW.jpg",
    "xray-rickets-wrist.jpg": "Rickets_UOTW_52_-_UOTW.jpg",
    "pathological-fracture-lytic-metastasis-xray.jpg": "Pathological_fracture.jpg",
    "scaphoid-fracture-MRI-STIR.jpg": "Scaphoid_fracture_MRI.jpg",

    # ── OPHTHALMOLOGY ──
    "ophthalmology-central-retinal-artery-occlusion.jpg": "Central_retinal_artery_occlusion.jpg",
    "ophthalmology-central-retinal-vein-occlusion.jpg": "Central_retinal_vein_occlusion.jpg",
    "ophthalmology-glaucomatous-cupping.jpg": "Optic_disc_glaucoma.jpg",
    "ophthalmology-herpes-simplex-keratitis.jpg": "Dendritic_corneal_ulcer.jpg",
    "ophthalmology-hypopyon.jpg": "Hypopyon.jpg",
    "ophthalmology-kayser-fleischer-ring.jpg": "Kayser-Fleischer_ring.jpg",
    "ophthalmology-rhegmatogenous-retinal-detachment.jpg": "Rhegmatogenous_retinal_detachment.jpg",
    "ophthalmology-relative-afferent-pupillary-defect.jpg": "RAPD.jpg",
    "ophthalmology-papilloedema.jpg": "Papilledema.jpg",
    "ophthalmology-diabetic-retinopathy.jpg": "Fundus_diabetic_retinopathy.jpg",
    "fundoscopy-diabetic-retinopathy-pdr-nvd.jpg": "Fundus_diabetic_retinopathy.jpg",
    "proliferative-diabetic-retinopathy-fundus.jpg": "Proliferative_diabetic_retinopathy.jpg",
    "hypertensive-retinopathy-fundus.jpg": "Hypertensive_retinopathy.jpg",
    "visual-field-bitemporal-hemianopia-pituitary.jpg": "Bitemporal_hemianopia.svg",
    "visual-field-homonymous-hemianopia-mca-stroke.jpg": "Homonymous_hemianopsia.svg",
    "visual-field-arcuate-scotoma-glaucoma.jpg": "Arcuate_scotoma_glaucoma.jpg",
    "visual-field-pie-in-sky-temporal-lobe.jpg": "Pie_in_the_sky_visual_field.jpg",
    "hirschberg-test-esotropia.jpg": "Esotropia_in_child.jpg",
    "colposcopy-acetowhite.jpg": "Acetowhite_area.jpg",
    "colposcopy-mosaic.jpg": "Colposcopy_mosaic_pattern.jpg",
    "colposcopy-punctation.jpg": "Colposcopy_punctation.jpg",
    "colposcopy-schiller-test.jpg": "Schiller_iodine_test.jpg",
    "slit-lamp-keratic-precipitates-mutton-fat.jpg": "Keratic_precipitates.jpg",

    # ── ENT ──
    "ent-audiogram.jpg": "Audiogram_example.jpg",
    "ent-cholesteatoma.jpg": "Cholesteatoma.jpg",
    "ent-chronic-suppurative-otitis-media.jpg": "Tympanic_membrane_perforation.jpg",
    "ent-laryngeal-squamous-cell-carcinoma.jpg": "Laryngeal_carcinoma.jpg",
    "ent-maxillary-sinusitis.jpg": "Maxillary_sinusitis_xray.jpg",
    "ent-sinonasal-polyposis.jpg": "Nasal_polyp.jpg",
    "ent-steeple-sign.jpg": "Croup_steeple_sign.jpg",
    "ent-thumbprint-sign-epiglottitis.jpg": "Epiglottitis_lateral_neck_xray.jpg",
    "ent-tympanic-membrane.jpg": "Ear_drum.jpg",
    "ent-vocal-cord-paralysis.jpg": "Vocal_cord_paralysis.jpg",

    # ── ANATOMY ──
    "brachial-plexus-roots-trunks-divisions-cords-branches.jpg": "Brachial_plexus.svg",
    "axilla-cross-section-brachial-plexus-cords.jpg": "Brachial_plexus_in_axilla.png",
    "erb-palsy-waiters-tip.jpg": "Erbs_palsy.jpg",
    "klumpke-palsy-total-claw-hand.jpg": "Claw_hand.jpg",
    "saturday-night-palsy-wrist-drop-radial-nerve.jpg": "Wrist_drop.jpg",
    "winged-scapula-long-thoracic-nerve.jpg": "Winged_scapula.jpg",
    "popes-blessing-hand-high-median-nerve.jpg": "High_median_nerve_palsy.jpg",
    "ape-hand-median-nerve-palsy.jpg": "Ape_hand_deformity.jpg",
    "carpal-tunnel-thenar-wasting-median-nerve.jpg": "Carpal_tunnel_syndrome_thenar_wasting.jpg",
    "claw-hand-ulnar-nerve.jpg": "Claw_hand.jpg",
    "froments-sign-ulnar-nerve.jpg": "Froment_sign.jpg",
    "ain-palsy-ok-sign-pinch-test.jpg": "AIN_palsy_OK_sign.jpg",
    "pin-palsy-finger-drop-radial-nerve.jpg": "Finger_drop_PIN_palsy.jpg",
    "foot-drop-common-peroneal-nerve.jpg": "Foot_drop.jpg",
    "trendelenburg-sign-superior-gluteal-nerve.jpg": "Trendelenburg_sign.jpg",
    "anatomical-snuffbox-surface-marking.jpg": "Anatomical_snuff_box.jpg",
    "femoral-triangle-navy-cross-section.jpg": "Gray545.png",
    "posterior-triangle-neck-brachial-plexus.jpg": "Gray1210.png",
    "cubital-fossa-contents-diagram.jpg": "Gray413.png",
    "lumbosacral-plexus-diagram.jpg": "Gray822.png",
    "dermatome-map-trunk-spinal-levels.jpg": "Dermatoms.png",
    "upper-limb-dermatome-map-spinal-levels.jpg": "Upper_limb_dermatomes.png",
    "cavernous-sinus-coronal-mri.jpg": "Cavernous_sinus.jpg",
    "lesser-sac-foramen-of-winslow-axial-ct.jpg": "Gray1037.png",
    "collagen-triple-helix-structure.jpg": "Collagen_fibril.png",

    # ── PHYSIOLOGY ──
    "o2-hb-dissociation-curve.jpg": "2511_Oxygen-hemoglobin_Dissociation_Curve.jpg",
    "action-potential-trace.jpg": "Action_potential.svg",
    "spirometry-trace-obstructive-restrictive.jpg": "Spirometry_NIH.jpg",
    "flow-volume-loop.jpg": "Flow_volume_loop.jpg",
    "renal-glucose-clearance-curve.jpg": "Renal_glucose_transport.jpg",
    "eeg-wave-patterns.jpg": "EEG_brain_waves.svg",
    "coagulation-cascade-diagram.jpg": "Coagulation_cascade.svg",
    "coagulation-cascade-heparin-warfarin.jpg": "Coagulation_cascade.svg",
    "complement-cascade-three-pathways.jpg": "Complement_pathway.svg",
    "dopamine-pathways-schizophrenia.jpg": "Dopamine_pathways.svg",
    "autonomic-receptor-diagram.jpg": "Autonomic_nervous_system.svg",

    # ── BIOCHEMISTRY ──
    "glycolysis-pathway-pfk1.jpg": "Glycolysis_metabolic_pathway_3_annotated.svg",
    "tca-cycle-diagram.jpg": "TCA_cycle_Deutsch.PNG",
    "electron-transport-chain-oxidative-phosphorylation.jpg": "Electron_transport_chain.svg",
    "fatty-acid-synthesis-vs-beta-oxidation-compartments.jpg": "FattyAcidSynthesisMitochondria.svg",
    "lipoprotein-structure-size-comparison.jpg": "Density_of_various_lipoproteins.jpg",
    "urea-cycle-diagram.jpg": "Urea_cycle.svg",
    "pku-metabolic-pathway.jpg": "Phenylalanine-metabolism.svg",
    "dna-replication-fork-diagram.jpg": "DNA_replication_en.svg",

    # ── PHARMACOLOGY ──
    "pharmacokinetic-elimination-curves.jpg": "Linear_PK.jpg",
    "dose-response-curves-agonist-antagonist.jpg": "Dose_response_curve.jpg",
    "therapeutic-index-ed50-ld50.jpg": "Therapeutic_index.png",
    "beta-lactam-ring-structures.jpg": "Beta-lactam_antibiotics_general_structure.png",
    "antidepressant-synapse-mechanisms.jpg": "SynapseSchematic_lines.svg",
    "mac-values-inhalational-agents.jpg": "Inhaled_anesthetics_MAC_values.jpg",
    "train-of-four-tof-monitoring.jpg": "Train_of_four.jpg",
    "spinal-anesthesia-baricity-meninges.jpg": "Spinal_anaesthesia.jpg",
    "malignant-hyperthermia-ryr1-cascade.jpg": "Malignant_hyperthermia.jpg",
    "succinylcholine-hyperkalemia-ecg.jpg": "Hyperkalemia_ECG_changes.jpg",

    # ── PATHOLOGY ──
    "hydropic-change-cellular-edema.jpg": "Hydropic_degeneration_of_tubular_cells.jpg",
    "coagulative-necrosis-myocardial-infarct.jpg": "Coagulative_necrosis_of_myocardium.jpg",
    "langhans-vs-foreign-body-giant-cell.jpg": "Granuloma_with_Langhans_type_giant_cells.jpg",
    "caseous-necrosis-tuberculous-lung-gross.jpg": "Caseous_necrosis.jpg",
    "caseating-granuloma-tuberculosis-langhans.jpg": "Granuloma_with_Langhans_type_giant_cells.jpg",
    "foam-cells-fatty-streak-atherosclerosis.jpg": "Foam_cells.jpg",
    "fatty-streak-aorta-gross.jpg": "Fatty_streaks_aorta.jpg",
    "wavy-fibers-coagulative-necrosis-mi-early.jpg": "Coagulative_necrosis_of_myocardium.jpg",
    "tb-granuloma-caseous-necrosis-histology.jpg": "Granuloma_with_Langhans_type_giant_cells.jpg",
    "type-i-hypersensitivity-ige-mast-cell-degranulation.jpg": "IgE_receptor_mast_cell.svg",
    "type-ii-hypersensitivity-antibody-cell-surface-cytotoxicity.jpg": "Type_II_hypersensitivity.svg",
    "type-iii-hypersensitivity-immune-complex-deposition.jpg": "Type_III_hypersensitivity.jpg",
    "type-iv-delayed-hypersensitivity-th1-macrophage-activation.jpg": "Delayed_hypersensitivity.jpg",
    "histology-cin1.jpg": "CIN1.jpg",
    "histology-cin3.jpg": "CIN3.jpg",

    # ── MICROBIOLOGY ──
    "ziehl-neelsen-acid-fast-bacilli-mtb-red-rods-blue-background.jpg": "Ziehl_Neelson_stain.jpg",
    "gram-stain-s-aureus-gram-positive-cocci-clusters.jpg": "Staphylococcus_aureus_gram_stain.jpg",
    "koh-mount-candida-pseudohyphae-blastoconidia.jpg": "Candida_albicans_in_sputum.jpg",
    "germ-tube-test-candida-albicans-true-hyphae.jpg": "Candida_albicans_germ_tube.jpg",
    "aspergillus-septate-hyphae-acute-angle-branching.jpg": "Aspergillus_fumigatus.jpg",
    "halo-sign-invasive-aspergillosis-ct-chest-ground-glass-halo.jpg": "Invasive_aspergillosis_CT.jpg",
    "aspergilloma-crescent-sign-chest-xray-fungal-ball-cavity.jpg": "Aspergilloma_xray.jpg",
    "india-ink-cryptococcus-capsule-halo-csf.jpg": "Cryptococcus_neoformans_using_a_light_India_ink_staining_preparation.jpg",
    "malaria-thin-film-falciparum-ring-trophozoites-crescent-gametocyte.jpg": "Plasmodium_falciparum_01.png",
    "malaria-thin-film-vivax-schuffner-dots-enlarged-rbc.jpg": "Plasmodium_vivax_01.png",
    "ghon-complex-primary-tb-chest-xray-calcified-focus-hilar-nodes.jpg": "TB_CXR.jpg",
    "hbv-serology-timeline-window-period-markers.jpg": "HBV_serology.svg",
    "hiv-western-blot-gp120-gp41-p24-bands.jpg": "HIV_western_blot.jpg",
    "koplik-spots-measles.jpg": "Koplik_spots_in_measles.jpg",

    # ── FORENSIC MEDICINE ──
    "rigor-mortis-distribution-pattern-progression.jpg": "Rigor_mortis.jpg",
    "livor-mortis-fixed-vs-unfixed-blanching-test.jpg": "Livor_mortis.jpg",
    "livor-mortis-color-comparison-normal-cherry-red-co-poisoning.jpg": "Livor_mortis.jpg",
    "putrefaction-marbling-green-discoloration-right-iliac-fossa.jpg": "Decomposition.jpg",
    "adipocere-vs-mummification-comparison-preservation-types.jpg": "Adipocere.jpg",
    "incised-wound-clean-margins-no-tissue-bridges.jpg": "Incised_wound.jpg",
    "lacerated-wound-tissue-bridges-abraded-margins.jpg": "Laceration.jpg",
    "stab-wound-entry-shape-single-double-edged-blade.jpg": "Stab_wound.jpg",
    "co-poisoning-cherry-red-skin-globus-pallidus-necrosis.jpg": "Carbon_monoxide_poisoning_CT.jpg",
    "critoe-elbow-ossification-centers-xray-age-sequence.jpg": "Elbow_ossification_centers.jpg",
    "gustafson-tooth-age-estimation-six-criteria-cross-section.jpg": "Tooth_cross_section_diagram.jpg",
    "contact-range-gunshot-stellate-tear-muzzle-imprint-co-muscle.jpg": "Gunshot_wound_contact_range.jpg",
    "close-range-gunshot-blackening-soot-singeing.jpg": "Gunshot_wound_close_range.jpg",
    "intermediate-range-gunshot-tattooing-stippling-powder-grains.jpg": "Gunshot_wound_intermediate_range.jpg",
    "distant-range-gunshot-entry-contusion-ring-grease-ring-only.jpg": "Gunshot_wound_distant_range.jpg",
    "entry-vs-exit-wound-comparison-contusion-ring-everted-margins.jpg": "Gunshot_entry_exit_wound.jpg",

    # ── COMMUNITY MEDICINE ──
    "2x2-contingency-table-sensitivity-specificity.jpg": "Sensitivity_and_specificity.svg",
    "roc-curve-auc-interpretation.jpg": "Roc_curve.svg",
    "normal-distribution-bell-curve-sd-zones.jpg": "Standard_deviation_diagram.svg",
    "forest-plot-meta-analysis.jpg": "Forest_plot_example.jpg",
    "funnel-plot-publication-bias.jpg": "Funnel_plot.jpg",
    "growth-monitoring-road-to-health-card.jpg": "WHO_Growth_Chart.svg",
    "epidemic-curve-shapes-point-propagated-continuous.jpg": "Epidemic_curve.jpg",
    "vaccine-cold-chain-temperature-zones.jpg": "Cold_chain.jpg",
    "silicosis-chest-xray-eggshell-calcification.jpg": "Silicosis_CXR.jpg",
    "asbestosis-chest-xray-pleural-plaques.jpg": "Asbestosis.jpg",

    # ── PEDIATRICS ──
    "developmental-milestone-chart.jpg": "Child_development_stages.svg",
    "neonatal-jaundice-kramer-zones.jpg": "Neonatal_jaundice.jpg",
    "cxr-neonatal-rds.jpg": "Infant_respiratory_distress_syndrome.jpg",
    "cxr-tga-egg-on-side.jpg": "TGA_egg_on_side.jpg",
    "cxr-tof-boot-shaped-heart.jpg": "Tetralogy_of_fallot_CXR.jpg",
    "measles-maculopapular-rash.jpg": "Morbillivirus_measles_infection.jpg",
    "marasmus-clinical-appearance.jpg": "Starved_child.jpg",
    "kwashiorkor-edema-flag-sign.jpg": "Kwashiorkor_6183.jpg",
    "malnutrition-kwashiorkor.jpg": "Kwashiorkor_6183.jpg",
    "malnutrition-marasmus.jpg": "Starved_child.jpg",
    "bitots-spots-xerophthalmia-vitamin-a.jpg": "Bitot_spot.jpg",
    "pellagra-casals-necklace-niacin-deficiency.jpg": "Pellagra.jpg",
    "pellagra-rash-casals-necklace.jpg": "Pellagra.jpg",
    "angular-cheilitis-b2-deficiency.jpg": "Angular_cheilitis.jpg",
    "angular-stomatitis-riboflavin-b2-deficiency.jpg": "Angular_cheilitis.jpg",
    "goitre-iodine-deficiency.jpg": "Goitre.jpg",
    "scurvy-gum-hemorrhage-perifollicular.jpg": "Scurvy_vitamin_c.jpg",

    # ── OBG ──
    "ctg-early-decelerations.jpg": "CTG_early_decelerations.jpg",
    "ctg-late-decelerations.jpg": "CTG_late_decelerations.jpg",
    "ctg-variable-decelerations.jpg": "CTG_variable_decelerations.jpg",
    "ctg-sinusoidal-pattern.jpg": "CTG_sinusoidal.jpg",
    "usg-ectopic-adnexal-ring-sign.jpg": "Ectopic_pregnancy_ultrasound.jpg",
    "usg-pcos-necklace-sign.jpg": "Polycystic_ovary_ultrasound.jpg",
    "usg-placenta-accreta.jpg": "Placenta_accreta.jpg",
    "usg-placenta-previa-complete.jpg": "Placenta_previa.jpg",
    "hysteroscopy-endometrial-polyp.jpg": "Endometrial_polyp_hysteroscopy.jpg",
    "hysteroscopy-submucous-fibroid.jpg": "Submucous_fibroid_hysteroscopy.jpg",
    "hysteroscopy-uterine-septum.jpg": "Uterine_septum.jpg",

    # ── DERMATOLOGY ──
    "dermatology-psoriasis.jpg": "Psoriasis_on_back.jpg",

    # ── PSYCHIATRY ──
    "cage-questionnaire-table.jpg": "CAGE_questionnaire.svg",
    "alcohol-withdrawal-timeline.jpg": "Alcohol_withdrawal_syndrome.jpg",

    # ── CT / MRI ──
    "ct-brain-cmv-periventricular-calcifications.jpg": "CMV_calcifications_CT.jpg",
    "ct-brain-toxoplasma-diffuse-calcifications.jpg": "Toxoplasmosis_CT.jpg",
}


API_URL = "https://en.wikipedia.org/w/api.php"
COMMONS_API = "https://commons.wikimedia.org/w/api.php"


def get_image_url_from_commons(filename):
    """Use Wikimedia Commons API to get the real URL for a file."""
    params = {
        'action': 'query',
        'titles': f'File:{filename}',
        'prop': 'imageinfo',
        'iiprop': 'url',
        'format': 'json',
    }
    url = COMMONS_API + '?' + urllib.parse.urlencode(params)
    headers = {'User-Agent': 'NEET-PG-StudyBot/1.0 (educational; noreply@example.com)'}
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        pages = data.get('query', {}).get('pages', {})
        for page in pages.values():
            info = page.get('imageinfo', [])
            if info:
                return info[0].get('url')
        return None
    except Exception as e:
        return None


def download_url(url, dest_path):
    """Download a file from a URL."""
    headers = {
        'User-Agent': 'NEET-PG-StudyBot/1.0 (educational; noreply@example.com)',
        'Accept': '*/*',
        'Referer': 'https://commons.wikimedia.org/',
    }
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
        if len(data) < 3000:
            return False, f"too small ({len(data)} bytes)"
        with open(dest_path, 'wb') as f:
            f.write(data)
        return True, f"{len(data)//1024}KB"
    except Exception as e:
        return False, str(e)[:80]


def main():
    ok, failed = 0, 0
    fail_list = []
    total = len(WIKI_FILES)

    for i, (local_name, wiki_name) in enumerate(WIKI_FILES.items(), 1):
        dest = os.path.join(DEST, local_name)
        print(f"[{i:3d}/{total}] {local_name[:52]:<52} ", end='', flush=True)

        # Get real URL from Commons API
        image_url = get_image_url_from_commons(wiki_name)
        if not image_url:
            print(f"✗ API: file not found on Commons")
            failed += 1
            fail_list.append((local_name, wiki_name, "not found on Commons"))
            time.sleep(0.2)
            continue

        # Download
        success, msg = download_url(image_url, dest)
        if success:
            print(f"✓ {msg}")
            ok += 1
        else:
            print(f"✗ DL: {msg}")
            failed += 1
            fail_list.append((local_name, wiki_name, f"download: {msg}"))

        time.sleep(0.4)  # polite rate limit

    print(f"\n{'='*70}")
    print(f"Done: {ok} ok, {failed} failed out of {total}")
    if fail_list:
        print(f"\nFailed ({len(fail_list)}):")
        for f, w, m in fail_list:
            print(f"  {f}")
            print(f"    Wiki: {w}")
            print(f"    Reason: {m}")


if __name__ == "__main__":
    main()
