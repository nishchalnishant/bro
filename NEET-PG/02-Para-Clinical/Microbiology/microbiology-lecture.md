# Microbiology — Lecture Notes for NEET PG
### Written in the style of an infectious disease specialist talking to a sharp student

---

## The Central Question of Microbiology

Before we name a single organism or memorize a single virulence factor, ask yourself the only question that matters in this subject: what does a pathogen want? It wants to survive, replicate, and spread to the next host. That is it. Every virulence factor, every toxin, every immune evasion strategy is in service of that single biological imperative. And on the other side, your immune system has one job: stop that from happening. Microbiology, at its core, is a war story. When you understand the strategies and counter-strategies, you stop memorizing and start understanding — and that is what the exam rewards.

---

## Immunology: The Foundation

### Why the Immune System Exists

Your body is a warm, nutrient-rich environment that every microorganism on Earth would love to colonize permanently. The immune system exists because without it, the first bacterial encounter would be your last. But immunity is not a single thing — it is a layered defense system, built from two fundamentally different philosophies about how to fight infection.

The first philosophy is speed at the cost of precision. The second is precision at the cost of speed. These two philosophies gave rise to the innate immune system and the adaptive immune system, respectively — and understanding why each exists the way it does will make every downstream concept make intuitive sense.

### The Innate Immune System: The First Responders

The innate immune system is your body's standing army — always deployed, always ready, never needing to be trained. It operates on a principle called pattern recognition. Over millions of years of co-evolution with microbes, the innate immune system has learned to recognize molecular patterns that are common to broad classes of pathogens but absent from human cells. These are called Pathogen-Associated Molecular Patterns (PAMPs), and the sensors that detect them are Pattern Recognition Receptors (PRRs), the most famous of which are the Toll-Like Receptors (TLRs).

Think of TLRs as tripwires. TLR4 detects lipopolysaccharide (LPS), the outer membrane molecule of Gram-negative bacteria. The moment LPS touches TLR4 on a macrophage, the macrophage does not need to pause and think — it immediately begins secreting inflammatory cytokines (TNF-α, IL-1, IL-6), upregulating phagocytic activity, and sending out chemical distress signals. This happens within minutes of infection. The innate response does not care whether the bacterium is E. coli or Klebsiella — it just knows it is a Gram-negative organism and responds accordingly.

**Analogy:** The innate immune system is like a smoke alarm. It does not tell you exactly what is burning or where — it just detects "fire" and triggers the alarm. Effective, fast, but not precise.

Neutrophils are the foot soldiers of the innate response. They arrive first (within hours), engulf pathogens via phagocytosis, and kill them with a devastating chemical arsenal: reactive oxygen species (respiratory burst — mediated by NADPH oxidase), myeloperoxidase (which generates hypochlorous acid — essentially bleach inside a cell), and proteolytic enzymes stored in granules. The neutrophil is not designed for finesse; it is designed to destroy pathogens quickly, and it does not much care about the collateral damage to surrounding tissue — which is why acute inflammation (pus, swelling, redness) is largely a neutrophil production.

Macrophages are more sophisticated. They are the tissue-resident phagocytes — present in virtually every organ (Kupffer cells in liver, microglia in brain, alveolar macrophages in lung) — and they do two things: they kill pathogens directly (phagocytosis, oxidative burst), and they bridge the innate and adaptive systems by acting as antigen-presenting cells (APCs). When a macrophage phagocytoses a bacterium, it breaks the proteins down into peptide fragments, loads them onto MHC class II molecules, and presents them on its surface to CD4+ T helper cells. This handoff is the moment the adaptive immune system is activated.

Natural Killer (NK) cells deserve special mention because they solve an important problem: viruses often downregulate MHC class I expression on infected cells to hide from cytotoxic T cells (because CTLs need MHC-I to identify targets). NK cells have a brilliant counter-strategy: they are inhibited by MHC-I. Normal cells express MHC-I → NK cells leave them alone. Virally infected cells lose MHC-I → NK cells kill them without needing prior sensitization. It is a "missing self" recognition system, the mirror image of the adaptive system's "foreign recognition."

### The Complement System: Chemical Warfare

The complement system is one of the most elegant weapons in the innate immune arsenal, and it is also one of the most tested topics in NEET PG. Think of it as a cascade of plasma proteins that, once triggered, operate like a chain of dominoes — each protein activating the next — ultimately converging on three distinct outcomes, each of which damages the pathogen in a different way.

Complement can be activated by three pathways: the classical pathway (triggered by antibody-antigen complexes — so technically a bridge to adaptive immunity), the lectin pathway (triggered by mannose-binding lectin recognizing mannose on bacterial surfaces), and the alternative pathway (triggered directly by pathogen surfaces — completely innate, requires no antibody). All three pathways converge on the cleavage of C3 into C3a and C3b.

C3b is the opsonin. It coats the bacterial surface like a flag, and phagocytes have receptors (CR1) that recognize C3b-coated targets and preferentially engulf them. **Analogy:** Opsonization is like spray-painting a target fluorescent orange so your soldiers can find it in the dark. Bacteria that have been opsonized are phagocytosed at dramatically higher rates than non-opsonized bacteria.

C5a is the chemotactic agent — it diffuses outward from the site of complement activation and acts as a chemical gradient that neutrophils and macrophages follow toward the infection. It also activates mast cells (causing local inflammation) and primes neutrophils for the oxidative burst. C5a is the "calling all units, come to this address" signal.

The terminal complement components (C5b through C9) assemble into the Membrane Attack Complex (MAC). The MAC inserts into the bacterial cell membrane like a drill bit, creating a pore that disrupts the osmotic barrier — water rushes in, the bacterium swells and lyses. This is the only way complement kills directly without needing phagocytes. It is particularly effective against Neisseria species (N. meningitidis, N. gonorrhoeae) — which is why patients with terminal complement deficiencies (C5-C9 deficiency) are specifically susceptible to recurrent Neisseria infections.

> **Exam key:** C3 deficiency → susceptibility to encapsulated organisms (complement-mediated opsonization fails). C5-C9 deficiency → susceptibility to Neisseria species (MAC-mediated lysis fails). Deficiency of C1-inhibitor → hereditary angioedema (uncontrolled activation of the classical pathway).

### The Adaptive Immune System: Precision Warfare

The adaptive immune system takes 7-14 days to mount its first response — an eternity in infection terms. So why does it exist? Because it does something the innate system cannot: it generates exquisitely specific responses against any pathogen it encounters, and it remembers. The memory cells generated after a primary response allow secondary responses that are faster, larger, and more specific — this is the biological basis of vaccination.

The adaptive system has two arms: humoral immunity (B cells → antibodies) and cellular immunity (T cells). But T cells are not a monolithic population — they are divided into subsets that are specialized for different types of threats, and understanding these subsets through the lens of "what problem is each one solving?" makes everything click.

### T Helper Cell Subsets: Immune System Generals

CD4+ T helper cells are the generals of the adaptive immune response. They do not kill pathogens directly — they coordinate and amplify the responses of other immune cells. Different subsets of Th cells have evolved to deal with different categories of threats.

**Th1 cells** exist because of intracellular pathogens — bacteria and parasites that hide inside macrophages (Mycobacterium, Leishmania, Salmonella). Antibodies cannot reach them (antibodies are in the extracellular space), and complement cannot opsonize what it cannot see. The solution is to supercharge the macrophage that is already harboring the pathogen. Th1 cells secrete IFN-γ, which activates macrophages and dramatically upregulates their killing capacity (increased NADPH oxidase, more reactive oxygen species, inducible nitric oxide synthase → nitric oxide → lethal to intracellular pathogens). So Th1 → activated macrophages → intracellular killing. The price: the same activated macrophages can cause tissue damage if the response is excessive or chronic (tuberculosis granuloma, delayed-type hypersensitivity).

**Th2 cells** exist because of helminths — large, multicellular parasites that cannot be phagocytosed. The solution to a large parasite is a different kind of immune response: IgE-mediated mast cell degranulation (immediate hypersensitivity), eosinophil recruitment (ADCC — antibody-dependent cellular cytotoxicity, where eosinophils attach to IgE-coated worms and release toxic granule contents), and increased mucus secretion (to expel gut parasites). Th2 cells drive this via IL-4 (promotes IgE class switching), IL-5 (eosinophil production and activation), and IL-13 (mucus production). This is also the pathway that goes wrong in allergy and asthma — chronic Th2 activation against harmless antigens (pollen, dust mites).

**Th17 cells** exist because of extracellular bacteria and fungi — pathogens that live outside cells in tissues but evade simple phagocytosis. The solution is massive neutrophil recruitment to the site of infection. Th17 cells secrete IL-17, which acts on epithelial cells and fibroblasts to produce G-CSF and CXC chemokines → neutrophil recruitment and mobilization from bone marrow. Th17 cells also drive production of antimicrobial peptides at mucosal surfaces. Loss of Th17 function (as in Job syndrome / Hyper-IgE syndrome) → recurrent bacterial and fungal infections (cold abscesses, recurrent skin and pulmonary infections).

### The Four Types of Hypersensitivity: When Immunity Causes Disease

Hypersensitivity reactions are not infections — they are the immune system causing collateral damage, either because it is reacting to a harmless antigen or because the immune response itself is injuring the host. Gell and Coombs classified these into four types, and understanding each through the lens of mechanism (not just memorization) is critical.

**Type I — IgE-mediated (Immediate Hypersensitivity):** This is the pathway that exists legitimately to fight helminths but goes wrong in allergy. On first exposure to an allergen (pollen, bee venom, penicillin), B cells class-switch to produce IgE under Th2 instruction. IgE binds to high-affinity receptors (FcεRI) on mast cells and basophils, effectively "loading" these cells. On re-exposure, the allergen cross-links two adjacent IgE molecules on the mast cell surface → immediate degranulation (within seconds to minutes) → release of preformed mediators (histamine, tryptase, heparin) and newly synthesized mediators (prostaglandins, leukotrienes, PAF) → vasodilation, bronchospasm, increased vascular permeability. In severe cases (anaphylaxis), systemic vasodilation → distributive shock. Treatment: epinephrine (counteracts vasodilation and bronchospasm by activating α and β adrenergic receptors).

**Type II — Antibody-Mediated Cytotoxicity:** Here, antibodies target antigens on cell surfaces, leading to cell destruction. The antibody (IgG or IgM) binds its target → activates complement (MAC lysis) or recruits NK cells (ADCC) or facilitates phagocytosis. Classic examples: autoimmune hemolytic anemia (antibodies against RBC surface antigens → complement-mediated lysis or splenic phagocytosis), Goodpasture's syndrome (antibodies against type IV collagen in glomerular basement membrane), myasthenia gravis (antibodies against acetylcholine receptors at the neuromuscular junction → receptor internalization and blockade → muscle weakness). Note: some Type II reactions involve stimulatory antibodies rather than destructive ones — Graves' disease (TSH receptor-stimulating antibodies → hyperthyroidism).

**Type III — Immune Complex-Mediated:** When antigen-antibody complexes form in excess (antigen excess or small complexes that don't precipitate well), they circulate and deposit in vessel walls, glomeruli, and synovium. There they activate complement → C5a attracts neutrophils → neutrophils attempt to phagocytose the complexes but are frustrated (the complexes are embedded in vessel wall) → release of lysosomal enzymes into the extracellular space → tissue damage. This is why Type III reactions characteristically cause vasculitis, nephritis, and arthritis. Classic examples: serum sickness (after foreign protein injection — immune complexes develop 7-10 days later), SLE (autoantibodies against nuclear antigens → immune complex deposition in kidneys, skin, joints), post-streptococcal glomerulonephritis (streptococcal antigen-antibody complexes deposit in glomeruli).

**Type IV — T Cell-Mediated (Delayed-Type Hypersensitivity):** This is the only type that does not involve antibodies. Instead, sensitized CD4+ T cells (Th1 subtype) recognize antigen presented by APCs and release IFN-γ → macrophage activation → tissue damage. The "delayed" refers to the timeline: 48-72 hours after antigen exposure (versus minutes for Type I). The tuberculin (Mantoux) test is the classic example: inject purified protein derivative (PPD) intradermally → in a sensitized individual, local Th1 cells recognize the antigen → macrophage accumulation → induration (not redness, but induration — the firmness from cellular infiltration) after 48-72 hours. Contact dermatitis (nickel, poison ivy) is also Type IV — haptens penetrate skin, bind to skin proteins, forming a complete antigen that sensitizes local T cells.

> **Exam key:** Type IV is the ONLY antibody-independent hypersensitivity. The tuberculin test measures induration (cellular infiltration), not redness (which is vascular). Caseous necrosis in TB granulomas is a manifestation of Type IV hypersensitivity — macrophage activation gone to destructive extremes.

---

## Key Bacterial Pathogens

### Staphylococcus aureus: The Master of Immune Evasion

If bacteria were poker players, S. aureus would be the one who has memorized every tell at the table and written a cheat sheet for every situation. It is not the most deadly organism, but it is arguably the most strategically sophisticated — and studying its virulence factors teaches you more about the immune system than any textbook chapter on immunology alone.

S. aureus's first strategy is to prevent opsonization. Protein A, anchored in the cell wall, binds the Fc region of IgG — but in reverse orientation. Normally, antibodies bind antigen via their Fab region and leave their Fc region free to bind phagocyte Fc receptors (the Fc region is the "handle" that phagocytes grab). Protein A binds the Fc region directly → the antibody is oriented backwards → the Fab regions point inward → the phagocyte has nothing to grab → opsonization is neutralized. It is a spectacularly simple trick: bind the weapon by its handle so it cannot be used.

The second strategy is the fibrin coat. Coagulase is an enzyme secreted by S. aureus that converts fibrinogen to fibrin — but unlike normal coagulation (which requires the clotting cascade), coagulase does this directly. The result is a fibrin shell around the bacterium. **Analogy:** Coagulase builds a personal bunker around S. aureus — a wall of clotted protein that phagocytes cannot penetrate. This is also why S. aureus infections tend to form abscesses (loculated collections of pus with a fibrin wall) rather than spreading diffusely.

The third strategy — and the most devastating — is Panton-Valentine Leukocidin (PVL). PVL is a pore-forming toxin that targets leukocytes (primarily neutrophils). It inserts into the neutrophil cell membrane, creates a pore, and kills the cell. Consider what this means: the bacterium is killing the very cells that are trying to kill it. PVL-positive S. aureus strains (commonly community-acquired MRSA) cause particularly severe skin and soft tissue infections and necrotizing pneumonia, because they systematically eliminate the primary cellular defense at the site of infection.

Beyond these evasion strategies, S. aureus produces a range of toxins that cause disease through specific mechanisms. Alpha-toxin pore-forms in red blood cells and platelets. Exfoliative toxins (ETs A and B) cleave desmoglein-1 in the superficial epidermis → splitting at the stratum granulosum → scalded skin syndrome (Ritter's disease in neonates, staphylococcal scalded skin syndrome in children). The toxin cleaves desmoglein-1 — the same molecule targeted by autoantibodies in pemphigus foliaceus — which is why both diseases look identical histologically.

**Superantigens: Why TSST-1 Causes Toxic Shock.** Normal T cell activation is extraordinarily specific. A T cell receptor (TCR) recognizes a specific peptide (8-12 amino acids) bound in the groove of an MHC molecule. This interaction is like a lock-and-key fit — only the right key (specific peptide-MHC combination) opens the lock. The result is that at any given moment, perhaps 1 in 10,000 to 1 in 100,000 T cells are activated by any given antigen. The immune response is precise and proportionate.

Superantigens throw this elegant specificity out the window. TSST-1 (Toxic Shock Syndrome Toxin-1) does not enter the groove of the MHC molecule and does not need to be processed by APCs. Instead, it bridges the outside of the MHC class II molecule to the Vβ region of the TCR — a region that is shared by large families of T cells regardless of their antigen specificity. One superantigen can activate 5-30% of all T cells simultaneously. The result is a catastrophic cytokine storm: massive simultaneous release of IL-2, IFN-γ, TNF-α, and IL-1 from thousands of T cells and macrophages → fever, hypotension, multiorgan failure → toxic shock syndrome. The name "superantigen" reflects this: it acts like an antigen, but with super-physiological, non-specific power.

**Clinical connection:** The management of TSST-mediated toxic shock is not just antibiotics — it includes clindamycin (which inhibits ribosomal protein synthesis, reducing toxin production at the existing bacterial load, even if the bacteria are not killed) and IVIg (which contains antibodies that neutralize the superantigen). Understanding the mechanism tells you exactly why each treatment component works.

> **Exam key:** TSST-1 is associated with tampon use and surgical wound infections. S. aureus food poisoning is caused by preformed enterotoxins (heat-stable — boiling the food kills the bacteria but NOT the toxin), which act as superantigens in the gut → rapid-onset vomiting within 1-6 hours (no fever, short duration). This distinguishes it from Salmonella/Campylobacter (which require live bacteria and cause fever and diarrhea 12-48 hours later).

### Mycobacterium tuberculosis: Biology as Strategy

Mycobacterium tuberculosis is an organism that has co-evolved with the human immune system for tens of thousands of years, and it shows. Its entire biology is an adaptation to surviving inside the most hostile environment that eukaryotic evolution has created — the activated macrophage. To understand TB, you must understand that this organism is not trying to avoid the immune system; it is trying to live inside it.

The mycolic acid coat is the foundational adaptation. Mycolic acids are long-chain fatty acids (60-90 carbons long) that form a waxy, hydrophobic layer around the cell wall, outside the peptidoglycan layer. This coat does three things simultaneously: it makes the organism acid-fast (the lipid coat retains carbol fuchsin even after treatment with acid-alcohol — the basis of the Ziehl-Neelsen stain); it makes the organism extraordinarily resistant to desiccation (TB can survive in aerosolized droplet nuclei for hours in still air); and it makes the organism resistant to the oxidative killing mechanisms of macrophages (the waxy coat is partially resistant to hydrogen peroxide and hypochlorite).

But the most important adaptation is the mechanism of phagosomal escape. When a macrophage phagocytoses a normal bacterium, the phagosome (the membrane bubble containing the bacterium) fuses with lysosomes (bags of hydrolytic enzymes) to form a phagolysosome — the bacterium is bathed in acid and enzymes and dies. MTB inhibits this phagosome-lysosome fusion by secreting proteins (including lipoarabinomannan, or LAM, and the ESX-1 secretion system effectors) that interfere with the vesicle trafficking machinery of the macrophage. The bacterium sits inside a phagosome that never acidifies and never acquires lysosomal enzymes — essentially living in a protected vacuole within the macrophage. The macrophage that was supposed to kill the pathogen has been turned into its host.

**The Immunology of Granuloma Formation.** When the innate immune system fails to eliminate MTB (because lysosomal killing is blocked), the adaptive immune system mounts a Th1-dominated response. CD4+ Th1 cells recognize MTB antigens presented on MHC class II by infected macrophages → secrete IFN-γ → macrophages are activated to a more powerful killing state → some bacteria are killed. But the immune system cannot fully eliminate the infection, so it does the next best thing: it walls it off. Macrophages begin to fuse and transform into epithelioid cells and Langhans giant cells, surrounding the infected macrophages with layer after layer of activated macrophages, forming a granuloma. The center of the granuloma undergoes caseous necrosis — a dry, cheese-like material (caseum) resulting from the cytotoxic effects of the Th1-driven immune response on the infected cells. The granuloma is essentially a prison: the bacteria are alive inside it (this is latent TB), but they are contained and cannot spread.

**Primary TB versus Reactivation TB.** In a child with no prior immunity encountering MTB for the first time, the organism reaches the alveoli (usually lower or middle lobes, where ventilation is greatest) and begins multiplying. The initial focus of infection is called the Ghon focus — a small area of pneumonitis in the lung parenchyma. The organism spreads via lymphatics to the hilar lymph nodes, forming the Ghon complex (Ghon focus + enlarged hilar nodes). The Ranke complex refers to the calcified remnant of the Ghon complex visible on chest X-ray years later. In an immunocompetent host, this primary infection is usually self-limited — the adaptive immune response walls off the infection in granulomas, and the patient never becomes sick (primary TB is subclinical in most cases). The organism enters a state of metabolic dormancy (or very slow replication) inside the granuloma — this is latent TB.

Reactivation TB occurs when the immunological containment fails — most commonly due to declining immunity from HIV infection, malnutrition, diabetes mellitus, corticosteroid use, or simply the immunosenescence of old age. The granuloma breaks down (the Th1 response weakens, the prison walls crumble). The bacteria begin replicating actively again. But now the infection is different: this is a host who has previously been sensitized to MTB antigens, so the immune response is intense — paradoxically, this intense immune response is what causes the tissue destruction of reactivation TB. Cytokines drive liquefactive necrosis (the caseum liquefies — creating the perfect culture medium for extracellular MTB replication). The liquefied caseum drains into a bronchus → cavity formation (cavities are characteristically in the upper lobes because the upper lobe has high oxygen tension, which MTB prefers as an obligate aerobe). The patient becomes infectious (cavitary lesions → organisms in the airways → expelled in cough).

> **Exam key:** The difference between primary and reactivation TB is an immunological story, not just anatomical. Lower/middle lobe + hilar lymphadenopathy + calcified Ghon complex = primary TB (in an immunologically naive host). Upper lobe cavitation + hemoptysis + weight loss = reactivation TB (in a previously sensitized host with waning immunity). MTB is the most common cause of granulomatous disease worldwide.

---

## Virology

### Hepatitis B: The Immune System as the Weapon

Hepatitis B virus is a masterclass in the concept that in viral disease, the virus is often not directly killing cells — the immune response is. This distinction has profound clinical implications for understanding disease outcomes and designing treatments.

HBV is a DNA virus (Hepadnaviridae family) with a compact, partially double-stranded circular genome. It infects hepatocytes via the NTCP (sodium-taurocholate co-transporting polypeptide) receptor. Inside the hepatocyte, the viral DNA is converted to covalently closed circular DNA (cccDNA), which acts as a stable episomal template for viral transcription. This is critically important: cccDNA is not integrated into the host genome, but it is extremely stable, resides in the nucleus, and is very difficult to eliminate — which is why HBV infection can persist for decades and why current antivirals (which block the polymerase) suppress viral replication but do not eliminate the cccDNA reservoir.

The hepatocyte infected with HBV does not immediately die. HBV is not intrinsically cytopathic at normal viral loads. The hepatocyte manufactures viral proteins (HBsAg, HBeAg) and assembles viral particles, but it continues to function. What brings it down is the cytotoxic T lymphocyte (CTL) response: CD8+ T cells recognize viral peptides presented on MHC class I on the infected hepatocyte surface → kill the hepatocyte. This is the host trying to eliminate infected cells to stop viral spread — but the collateral damage is hepatocyte death → elevation of ALT/AST → hepatitis.

**The neonatal story.** If the immune system causes hepatitis by killing infected hepatocytes, then a weak immune response should cause less hepatitis — but also less viral clearance. This is exactly what happens in neonates. The neonatal immune system is immature (lower CTL activity, poor T cell responses to new antigens, regulatory T cells predominate to prevent autoimmunity). When a neonate is infected with HBV (most commonly during delivery, from an HBeAg-positive mother), the CTL response is inadequate — not enough hepatocytes are being killed, so there is minimal acute hepatitis (neonates rarely develop symptomatic acute hepatitis B). But because the virus is not being cleared, it establishes persistent infection. Over 90% of neonates infected with HBV become chronically infected. In contrast, healthy adults who acquire HBV have fully competent immune responses — they develop acute hepatitis (elevated ALT, jaundice, symptoms) but clear the infection in over 95% of cases.

**Clinical connection:** This is why universal HBV vaccination of all neonates (within 24 hours of birth, ideally in the delivery room) is so critical. A neonate who escapes vaccination and acquires HBV from its HBeAg-positive mother has a >90% chance of becoming a chronic carrier — and 25% of those chronic carriers will eventually die of cirrhosis or hepatocellular carcinoma. Vaccination completely prevents this chain of events.

**HBV Serological Markers as a Timeline.** The serological course of HBV infection is one of the most frequently tested topics in NEET PG, and it is much easier to understand as a narrative than as a list.

HBsAg (surface antigen) is the first marker to appear — it shows up 1-6 weeks after infection, even before symptoms, and indicates that virus is present. HBeAg (envelope antigen) appears shortly after and indicates active viral replication (it is a secreted form of the core protein, acting as a marker of high replicative activity). ALT rises as the CTL response begins killing infected hepatocytes — this is when the patient becomes symptomatic. In a patient who will clear the infection, HBeAg disappears first (replication slows), followed by appearance of anti-HBe antibodies. Then HBsAg disappears (window period — neither HBsAg nor anti-HBs detectable). Finally, anti-HBs appears — this is the marker of protective immunity (either from infection clearance or from vaccination). Anti-HBc (core antibody, IgM then IgG) persists for life as a marker of past or present infection.

> **Exam key — the window period:** A patient in the window period has neither HBsAg nor anti-HBs — the only marker present is IgM anti-HBc. This patient had acute HBV infection, is in the process of clearing it, and is not yet immune. In this period, standard surface antigen testing is falsely negative — only anti-HBc IgM identifies recent infection. Anti-HBs alone (without anti-HBc) = vaccine-induced immunity.

### HIV: The Systematic Dismantling of Adaptive Immunity

HIV is not just a virus — it is a 10-year project to dismantle the adaptive immune system from the inside. The tragedy of HIV is that the cell it preferentially infects is the very cell that coordinates the entire adaptive immune response: the CD4+ T helper cell.

HIV enters CD4+ cells via a two-receptor system: CD4 is the primary receptor (which is why CD4+ T cells, macrophages, and dendritic cells — all of which express CD4 — are targets), but HIV also requires a co-receptor for entry. CCR5 is the co-receptor used by R5-tropic (macrophage-tropic) strains, which dominate early infection. CXCR4 is the co-receptor for X4-tropic (T cell-tropic) strains, which emerge later in disease. Individuals who are homozygous for the CCR5Δ32 mutation (a deletion that results in a non-functional CCR5 receptor) are almost completely resistant to HIV-1 infection — a genetic accident that has inspired the development of CCR5 antagonists (maraviroc) as antiretrovirals.

Once inside, HIV undergoes reverse transcription (RNA → DNA via reverse transcriptase — an error-prone enzyme that introduces mutations with every replication cycle, generating the extraordinary genetic diversity that makes vaccine development so challenging) and integration (the viral DNA integrates into the host chromosome via integrase, becoming a provirus that persists as long as the host cell lives).

**The CD4 count as a measure of immune competence.** A normal CD4 count is 500-1500 cells/μL. As HIV progressively depletes CD4+ T helper cells (both by direct viral cytopathic effect and by immune-mediated killing of infected cells), the immune system loses its coordination capacity. But different arms of the immune system require different levels of CD4 support to function, and different pathogens require different levels of immune defense to be contained. This is why opportunistic infections appear in a predictable sequence as the CD4 count falls.

At CD4 >500, the immune system is largely intact — the patient has AIDS-related complex (ARC) or may be asymptomatic. Between 200-500, cellular immunity begins to wane — susceptibility to some fungi (Candida, especially mucosal), reactivation of VZV (shingles), and bacterial infections increases. Below 200 cells/μL, the CDC definition of AIDS is met, and Pneumocystis jirovecii pneumonia (PCP) becomes the major threat. PCP is caused by an organism that is present (as spores) in the lungs of most normal adults without causing disease — it only becomes pathogenic when T cell-mediated immunity falls below a critical threshold. Below 100, Toxoplasma gondii reactivates — latent Toxoplasma cysts in the brain break down (when Th1 CD4+ cell-mediated immunity collapses) → reactivation toxoplasmosis → multiple ring-enhancing lesions in the brain (particularly in basal ganglia and at the grey-white junction). Below 50, CMV disseminates — CMV is kept in check by CD8+ CTLs (which require CD4+ T cell help for maintenance) and NK cells — as both decline, CMV can infect the retina (CMV retinitis — "pizza pie" appearance on fundoscopy), colon, and adrenal glands.

> **Exam key — CD4 thresholds and prophylaxis:** PCP prophylaxis (TMP-SMX) is initiated at CD4 <200. Toxoplasma prophylaxis (also TMP-SMX) at CD4 <100 (and positive Toxoplasma serology). MAC (Mycobacterium avium complex) prophylaxis (azithromycin) at CD4 <50. CMV prophylaxis is generally not given routinely (relies on ART-mediated immune reconstitution). These thresholds reflect the CD4 levels at which each pathogen's containment fails.

**Clinical connection:** The viral load determines how quickly CD4 cells are destroyed (rate of disease progression). The CD4 count determines current immune status and what infections to prevent. ART targets multiple steps in the viral replication cycle simultaneously (NRTI + NNRTI or PI + integrase inhibitor) to prevent resistance emergence — any single drug is defeated by mutational escape within weeks; three drugs with different targets make the probability of simultaneous resistance to all three vanishingly small.

---

## Summary Tables

### Complement Pathways

| Pathway | Trigger | Key Proteins | Outcome |
|---|---|---|---|
| Classical | Ab-Ag complex (IgG, IgM) | C1q, C1r, C1s, C4, C2 | C3 cleavage → C3b, C3a |
| Lectin | Mannose on pathogens | MBL, MASP1/2 | C3 cleavage |
| Alternative | Pathogen surfaces (spontaneous) | Factor B, D, Properdin | C3 cleavage |
| All converge | C3 cleavage | C3b (opsonin), C3a/C5a (anaphylatoxins), MAC (C5b-9) | Opsonization, chemotaxis, lysis |

### Hypersensitivity Quick Reference

| Type | Mediator | Timing | Prototype Disease |
|---|---|---|---|
| I | IgE + mast cells | Minutes | Anaphylaxis, asthma, urticaria |
| II | IgG/IgM vs cell surface | Hours | AIHA, Goodpasture, Graves |
| III | Immune complexes | 6-12 hours | SLE, serum sickness, PSGN |
| IV | T cells (Th1/CTL) | 48-72 hours | TB tuberculin, contact dermatitis, transplant rejection |

### HBV Serological Markers

| Marker | Significance | Present in |
|---|---|---|
| HBsAg | Virus present | Acute + chronic infection |
| Anti-HBs | Immunity | Recovery OR vaccination |
| HBeAg | Active replication | High infectivity |
| Anti-HBe | Replication declining | Late acute / chronic low-replication |
| IgM anti-HBc | Recent acute infection | Acute + window period |
| IgG anti-HBc | Past infection | Resolved infection + chronic |

### HIV CD4 Count and Opportunistic Infections

| CD4 Count | Opportunistic Infection |
|---|---|
| <500 | Candida (mucosal), VZV reactivation |
| <200 | PCP (Pneumocystis jirovecii pneumonia) |
| <100 | Toxoplasma encephalitis, Cryptosporidium |
| <50 | CMV retinitis, MAC (M. avium complex) |
