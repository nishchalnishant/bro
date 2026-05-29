# Repository Audit Report
**Date:** 2026-05-28  
**Repo:** NEET-PG Exam Preparation  
**Health Score:** 92/100

---

## Repository Stats
- **Total files:** 346 (72 markdown + 274 images)
- **Subjects:** 19 across 3 phases
- **File system:** Two-file system per subject (`*-notes.md` + `*-lecture.md`)

---

## File Size Analysis (Top Files)

| File | Lines |
|------|-------|
| `medicine-notes.md` | 1,304 |
| `pharmacology-notes.md` | 1,261 |
| `microbiology-notes.md` | 1,172 |
| `subject-wise-pyq.md` | 1,029 |

---

## Critical Gaps

### 1. ~~Missing Lecture Files — Tier 1 Subjects~~ — RESOLVED
- `pathology-lecture.md` — exists (319 lines, has content) ✓
- `pharmacology-lecture.md` — exists (364 lines, has content) ✓

### 2. Missing Lecture Files — Clinical Subjects
The following have notes only (no lecture file):
- `03-Clinical/OBG/` — Tier 1
- `03-Clinical/Pediatrics/` — Tier 1
- `03-Clinical/Dermatology/` — Tier 2
- `03-Clinical/Anesthesia/` — Tier 4 (lower priority)

### 3. Oversized Files (Hard to Navigate)
- `medicine-notes.md` (1,304 lines) — needs splitting by organ system
- `pharmacology-notes.md` (1,261 lines) — needs splitting by drug class
- `subject-wise-pyq.md` (1,029 lines) — needs anchor links at minimum

### 4. No Active Practice Infrastructure
The entire repo is **passive reading material**. Missing:
- MCQ banks with answers and explanations
- Flashcard-style Q&A sections
- Self-test checklists

### 5. PYQ Analysis is Siloed
`04-PYQ-Analysis/` has good data but zero cross-linking to lecture/notes files. High-frequency topics aren't flagged inside the study material.

### 6. No Progress Tracking
`study-schedule.md` exists but no way to mark topics done / weak / needs-review. Can't efficiently decide what to revisit.

### 7. Navigation Infrastructure Missing
- No root-level `README.md`
- No folder-level READMEs for `04-PYQ-Analysis/`, `05-Quick-Revision/`, `07-Grand-Tests/`
- 19 subject READMEs are 17-line stub templates

---

## Improvement Roadmap

| # | Action | Impact | Status |
|---|--------|--------|--------|
| 1 | ~~Add `pathology-lecture.md`~~ | High — Tier 1 subject gap | ☑ Already exists |
| 2 | ~~Add `pharmacology-lecture.md`~~ | High — Tier 1 subject gap | ☑ Already exists |
| 3 | Add MCQ files for top 5 subjects (Medicine, Surgery, OBG, Pathology, Pharmacology) | High — active recall | ☑ Done 2026-05-28 |
| 4 | Add `WEAK-TOPICS.md` tracker to all 19 subjects | High — revision targeting | ☑ Done 2026-05-28 |
| 5 | Split `medicine-notes.md` by organ system | Medium — navigation speed | ☑ Done 2026-05-28 (6 files) |
| 6 | Split `pharmacology-notes.md` by drug class | Medium — navigation speed | ☑ Done 2026-05-28 (8 files) |
| 7 | Add PYQ snapshot headers to each notes file | Medium — focus targeting | ☑ Done 2026-05-28 (all 19) |
| 8 | Add lecture files for OBG + Pediatrics | Medium — Tier 1 subjects | ☑ Already existed (8 + 9 sections respectively) |
| 9 | Add `DAILY-REVISION.md` in `00-Master-Index/` | Medium — daily use | ☑ Done 2026-05-28 (5-day rotation, 19 subjects, DoC + signs tables) |
| 10 | Add lecture file for Dermatology | Low — Tier 2 | ☑ Done 2026-05-28 (529 lines, 9 sections, PYQ snapshot, ASCII diagram) |
| 11 | Enrich 19 subject READMEs | Low — navigation | ☑ Done 2026-05-28 (all 19 rewritten with files table, high-yield areas, nav links, PYQ weight) |
| 12 | Add folder READMEs for 04/05/07 | Low — navigation | ☑ Done 2026-05-28 (04-PYQ-Analysis, 05-Quick-Revision, 07-Grand-Tests) |

---

---

## Audit 2026-05-29

**Health Score:** 96/100 (up from 92/100 on 2026-05-28)

### Repository Stats (2026-05-29)
- **Total files:** 383 (136 markdown + 247 images)
- **Subjects:** 19 across 3 phases
- **File system:** Two-file system per subject plus split files, MCQ banks, SRS schedule, normal values, image-based Qs

### Improvements Made 2026-05-29

| # | Action | Status |
|---|--------|--------|
| 1 | Expanded MCQ banks (Medicine, Surgery, OBG, Pathology, Pharmacology) to 60 Qs each | ☑ Done |
| 2 | Added anchor TOC to `subject-wise-pyq.md` and `year-wise-pyq.md` | ☑ Done |
| 3 | Fixed cross-links for medicine and pharmacology split files | ☑ Done |
| 4 | Added 30+ PYQ HOTSPOT tags to ENT, Pediatrics, Ophthalmology notes | ☑ Done |
| 5 | Added image refs to Psychiatry and Pharmacology lecture files | ☑ Done |
| 6 | Created `normal-values.md` in `05-Quick-Revision/` | ☑ Done |
| 7 | Added mermaid rendering note + ASCII fallback to all 19 lecture files | ☑ Done |
| 8 | Created 6 medicine system-specific MCQ files | ☑ Done |
| 9 | Created `SRS-SCHEDULE.md` in `00-Master-Index/` | ☑ Done |
| 10 | Validated and fixed broken image paths | ☑ Done |
| 11 | Updated General-Medicine and Pharmacology READMEs for split files | ☑ Done |
| 12 | Created `radiology-ibq-mcqs.md` with image-based questions | ☑ Done |
| 13 | Created 4 pharma drug-class MCQ files | ☑ Done |
| 14 | Updated AUDIT-REPORT and memory | ☑ Done |

### Remaining Gaps
No critical gaps remain. Optional future work: expand grand tests to 5, add Psychiatry image-based questions, add per-subject PYQ files to `04-PYQ-Analysis/Subject-Wise/`.

---

## What Was Done Before This Audit

All completed in prior sessions:

- [x] ASCII overview diagrams added to all 19 `*-lecture.md` files
- [x] IBQ placeholders added to all 19 subjects (sign name + image markdown + differentiation tip)
- [x] Broken local image paths replaced with Radiopaedia/Wikimedia article URLs
- [x] ASCII inline diagrams added for schematics (O2-Hb curve, Frank-Starling, coagulation cascade, dose-response, Lineweaver-Burk, urea cycle)
- [x] `/NEET-PG/images/IMAGE-SOURCES.md` created (119 entries with free URLs and search terms)
