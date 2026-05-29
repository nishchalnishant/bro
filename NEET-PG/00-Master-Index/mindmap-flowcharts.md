# Repository Mind Map & Flowcharts

> **Navigation:** [Master Index](README.md) · [Study Schedule](study-schedule.md) · [Daily Revision](DAILY-REVISION.md) · [Progress Tracker](PROGRESS.md)

---

## 1. Repository Mind Map

Full structure of every folder and file in the repo.

```mermaid
mindmap
  root((NEET PG))
    00-Master-Index
      README
      Study Schedule
      SRS Schedule
      Daily Revision
      Progress Tracker
      Mind Map & Flowcharts
    01-Pre-Clinical
      Anatomy
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Physiology
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Biochemistry
        Lecture Notes
        Notes
        MCQs
        Weak Topics
    02-Para-Clinical
      Pathology
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Pharmacology
        Lecture Notes
        Notes
        MCQs
        Weak Topics
        Pharmacokinetics
        Autonomic
        CNS
        CVS
        Antimicrobials
        Anticancer
        Endocrine
        Side Effects
      Microbiology
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Forensic Medicine
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Community Medicine SPM
        Lecture Notes
        Notes
        MCQs
        Weak Topics
    03-Clinical
      General Medicine
        Lecture Notes
        Notes
        MCQs
        Weak Topics
        Cardiology
        Neurology
        Pulmonology
        Endocrinology
        Gastroenterology
        Rheumatology
      General Surgery
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      OBG
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Pediatrics
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Orthopedics
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      ENT
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Ophthalmology
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Psychiatry
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Dermatology
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Anesthesia
        Lecture Notes
        Notes
        MCQs
        Weak Topics
      Radiology
        Lecture Notes
        Notes
        MCQs
        Image-Based MCQs
        Weak Topics
    04-PYQ-Analysis
      Overview
      Subject-Wise PYQ
      Year-Wise PYQ
      High-Yield Topics
    05-Quick-Revision
      Last-Day Notes
      Master Mnemonics
      Master One-Liners
      Comparison Tables
      Normal Values
    06-Books-and-Resources
      Recommended Books
    07-Grand-Tests
      Mock Test Guide
      Grand Test 1
      Grand Test 2
      Grand Test 3
      Error Notebook
      Performance Tracker
```

---

## 2. Subject Question Weight Map

Size of each subject's contribution to the NEET PG paper (~200 Qs total).

```mermaid
pie title NEET PG Question Distribution (Approximate)
  "General Medicine" : 23
  "General Surgery" : 15
  "OBG" : 15
  "Pathology" : 18
  "Pharmacology" : 16
  "SPM / Community Med" : 16
  "Anatomy" : 14
  "Physiology" : 13
  "Microbiology" : 13
  "Biochemistry" : 11
  "Pediatrics" : 12
  "Orthopedics" : 7
  "Dermatology" : 7
  "Forensic Medicine" : 8
  "ENT" : 8
  "Ophthalmology" : 8
  "Psychiatry" : 6
  "Anesthesia" : 5
  "Radiology" : 5
```

---

## 3. Study Phase Flowchart

How to progress through the repo from Day 1 to exam day.

```mermaid
flowchart TD
    START([Start Preparation]) --> SCHEDULE[Set up Study Schedule\n00-Master-Index/study-schedule.md]
    SCHEDULE --> SRS[Configure SRS Schedule\n00-Master-Index/SRS-SCHEDULE.md]
    SRS --> PHASE1

    subgraph PHASE1[Phase 1 — Foundation: Pre-Clinical]
        A1[Anatomy\nLecture → Notes → MCQs] --> A2[Physiology\nLecture → Notes → MCQs]
        A2 --> A3[Biochemistry\nLecture → Notes → MCQs]
    end

    PHASE1 --> PHASE2

    subgraph PHASE2[Phase 2 — Para-Clinical]
        B1[Pathology] --> B2[Pharmacology]
        B2 --> B3[Microbiology]
        B3 --> B4[Forensic Medicine]
        B4 --> B5[Community Medicine / SPM]
    end

    PHASE2 --> PHASE3

    subgraph PHASE3[Phase 3 — Clinical]
        C1[General Medicine] --> C2[General Surgery]
        C2 --> C3[OBG]
        C3 --> C4[Pediatrics]
        C4 --> C5[Orthopedics + ENT\n+ Ophthalmology]
        C5 --> C6[Psychiatry + Dermatology\n+ Anesthesia + Radiology]
    end

    PHASE3 --> PYQ

    subgraph PYQ[Phase 4 — PYQ Analysis]
        D1[Read PYQ Overview\npyq-analysis-overview.md] --> D2[Subject-Wise Analysis\nsubject-wise-pyq.md]
        D2 --> D3[Year-Wise Trends\nyear-wise-pyq.md]
        D3 --> D4[High-Yield Topics\nhigh-yield-topics.md]
    end

    PYQ --> GRANDTEST

    subgraph GRANDTEST[Phase 5 — Grand Tests]
        E1[Grand Test 1] --> E2[Error Notebook]
        E2 --> E3[Grand Test 2]
        E3 --> E4[Error Notebook]
        E4 --> E5[Grand Test 3]
        E5 --> E6[Performance Tracker Review]
    end

    GRANDTEST --> FINALWEEK

    subgraph FINALWEEK[Final Week]
        F1[One-Liners daily\nmaster-one-liners.md] --> F2[Comparison Tables\ncomparison-tables.md]
        F2 --> F3[Mnemonics sprint\nmaster-mnemonics.md]
        F3 --> F4[Normal Values\nnormal-values.md]
    end

    FINALWEEK --> LASTDAY[Last Day Notes\nlast-day-notes.md]
    LASTDAY --> EXAM([NEET PG Exam\n200 Qs · 3.5 hrs · +4/−1])
```

---

## 4. Per-Subject Study Flowchart

The standard workflow to follow for every subject.

```mermaid
flowchart LR
    ENTER([Start Subject]) --> LECTURE[Read Lecture Notes\nsubject-lecture.md]
    LECTURE --> NOTES[Study Notes\nsubject-notes.md]
    NOTES --> MCQ1[Attempt MCQs\nsubject-mcqs.md]
    MCQ1 --> WEAK{Weak areas\nidentified?}
    WEAK -- Yes --> WEAKTOPIC[Log in Weak Topics\nWEAK-TOPICS.md]
    WEAKTOPIC --> REVISIT[Revisit notes\nfor weak section]
    REVISIT --> MCQ1
    WEAK -- No --> PYQ[Do Subject PYQ section\nsubject-wise-pyq.md]
    PYQ --> HIGHYIELD[Check High-Yield list\nhigh-yield-topics.md]
    HIGHYIELD --> ONELINER[Add to One-Liners\nmaster-one-liners.md]
    ONELINER --> MNEMONIC[Add mnemonics\nmaster-mnemonics.md]
    MNEMONIC --> DONE([Subject Complete ✓])
```

---

## 5. Daily Revision Flowchart

What to do every single study day.

```mermaid
flowchart TD
    WAKEUP([Morning]) --> ONELINER[10 min: One-Liners\nmaster-one-liners.md]
    ONELINER --> SUBJECT[Main subject block\nLecture / Notes / MCQs]
    SUBJECT --> BREAK([Break])
    BREAK --> WEAKCHECK[Review yesterday's\nWeak Topics]
    WEAKCHECK --> PYQBLOCK[20 min: PYQ block\n5–10 Qs from subject bank]
    PYQBLOCK --> EVENING([Evening])
    EVENING --> COMPARE[15 min: Comparison Tables\n1–2 tables from comparison-tables.md]
    COMPARE --> MNEMONIC[10 min: Mnemonics\n1 subject from master-mnemonics.md]
    MNEMONIC --> LOG[Update Progress Tracker\nPROGRESS.md]
    LOG --> BED([End of Day])
```

---

## 6. MCQ Strategy Flowchart

Decision logic for answering a NEET PG MCQ under exam conditions.

```mermaid
flowchart TD
    Q([Read Question Stem]) --> KEYWORD[Identify keywords:\nage · gender · key finding · drug · organism]
    KEYWORD --> KNOW{Confident\nabout answer?}
    KNOW -- Yes --> MARK[Mark answer directly\nDo not second-guess]
    KNOW -- No --> ELIMINATE[Eliminate clearly wrong options\nusing basic science logic]
    ELIMINATE --> TWO{Down to\n2 options?}
    TWO -- Yes --> HIGHYIELD[Pick the high-yield / classic answer\nNot the rare exception]
    TWO -- No --> GUESS[Guess from remaining\nDo NOT leave blank\n+4 vs −1: guessing is +EV at >25%]
    MARK --> NEXT([Next Question])
    HIGHYIELD --> NEXT
    GUESS --> NEXT
    NEXT --> REVIEW{Time left\nfor review?}
    REVIEW -- Yes --> FLAGGED[Revisit flagged questions only\nDo not re-read unmarked ones]
    REVIEW -- No --> SUBMIT([Submit])
    FLAGGED --> SUBMIT
```

---

## 7. Error Analysis Flowchart

What to do with every wrong answer in a mock test or PYQ session.

```mermaid
flowchart TD
    WRONG([Wrong Answer]) --> WHY{Why was it wrong?}
    WHY -- Did not know the fact --> NOTES[Find fact in subject notes\nAnnotate: NEET PYQ year]
    WHY -- Knew it but misread stem --> STEM[Slow down on reading\nUnderline key words next time]
    WHY -- Eliminated correct answer --> LOGIC[Review elimination logic\nRevisit comparison table for that topic]
    WHY -- Guessed wrong --> MNEMONIC[Create or find a mnemonic\nmaster-mnemonics.md]
    NOTES --> ERRORBOOK[Log in Error Notebook\nerror-notebook-template.md]
    STEM --> ERRORBOOK
    LOGIC --> ERRORBOOK
    MNEMONIC --> ERRORBOOK
    ERRORBOOK --> WEAKLOG[Add topic to Weak Topics\nWEAK-TOPICS.md for that subject]
    WEAKLOG --> SRS[Schedule for SRS review\nSRS-SCHEDULE.md]
    SRS --> DONE([Closed loop ✓])
```
