# Brandevegen

> **Personal Rebranding Agent**
> **Promise:** Get a job or land your client in 30 days.
> **Operating Ethos:** 90% hardwork, 10% luck.

Brandevegen is a deterministic, evidence-first personal rebranding and 30-day pipeline agent skill. Built as the next-generation successor to Emplowise, it fuses structured 30-day brand strategy, anti-AI cold outreach engineering, and scored paid acquisition copywriting into a single modular execution system.

---

## Why Brandevegen Exists

Most career tools and personal branding templates fail for three predictable reasons:

1. **Aesthetics before strategy:** People redesign resumes, logos, or LinkedIn banners before proving what problem they solve or why anyone should pick them.
2. **AI-slop outreach:** Candidates and freelancers send 200-word pitches stuffed with phrases like "I hope this email finds you well" and "cutting-edge solutions" that get deleted in three seconds.
3. **Unverified claims:** Generic templates encourage exaggerating metrics, faking urgency, or promising outcomes nobody can defend in an interview or discovery call.

Brandevegen replaces guesswork with **four sequential quality gates**, an **Evidence Ledger**, a **strict anti-AI linter**, and **100-point copy rubrics**.

---

## Dual-Track Execution Model

Brandevegen runs two 30-day sprint tracks built on one shared strategic core:

| Dimension | Track A: Land a Job (30 Days) | Track B: Land a Client (30 Days) |
| :--- | :--- | :--- |
| **Target Buyer** | Hiring managers, founders, technical leads, recruiters | Agency owners, B2B founders, department heads |
| **Core Offer** | Role-specific capability + verified work proof | Scoped service + zero-risk free "slice" deliverable |
| **Primary Touchpoints** | LinkedIn profile, portfolio/GitHub, proof-backed resume, direct outreach | Landing page, case-study proof ladder, cold email sequence, optional paid ads |
| **Primary Conversion Action** | Interview invite or referral to the hiring decision-maker | Low-friction "yes" reply -> free audit/slice -> paid scope |
| **30-Day Measurement** | Qualified replies, interviews booked, feedback signals | Positive reply rate, audits delivered, discovery calls, proposals sent |

---

## Repository Structure

```text
brandevegen/
├── SKILL.md                                           # Core agent instructions and trigger rules
├── README.md                                          # GitHub repository overview, architecture, quickstart
├── docs/
│   ├── RESEARCH_DRAFT.md                              # Pre-execution research draft & evidence ledger
│   └── PLAYBOOK_SYNTHESIS.md                          # 30-day sprint, outreach rules, paid rubrics & SOPs
├── templates/
│   └── working-templates.md                           # Ready-to-use personal rebranding templates
└── references/
    ├── dont-sound-like-ai.md                          # Anti-AI word/phrase/shape linter + 8Q audit
    ├── Advegen-30-Day-Brand-Building-Method.pdf       # Source Playbook 1: 4-Gate 30-Day Method
    ├── The-Cold-Email-Copy-Playbook.pdf               # Source Playbook 2: Cold Email Copy Rules
    └── Advegen-Copywriting-Playbook.pdf               # Source Playbook 3: Google & Meta Ad Playbook
```

---

## System Architecture & 4-Gate State Machine

```text
[Gate 0: Pre-Execution Research Draft & Evidence Ledger]
   Condition: Track selected, real skills/proof logged, gaps disclosed.
                         │
                         ▼
       ┌─────────────────────────────────┐
       │   MODULE 1: 30-DAY BRAND SPRINT │
       │  Days 1-7   Discover  (Gate 1)  │
       │  Days 8-14  Define    (Gate 2)  │
       │  Days 15-21 Develop   (Gate 3)  │
       │  Days 22-30 Deploy    (Gate 4)  │
       └───────────────┬─────────────────┘
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
┌──────────────────────┐  ┌──────────────────────────┐
│ MODULE 2: COLD ENGINE│  │ MODULE 3: PAID COPY LAB  │
│ - 74-80w Email 1     │  │ - 7-Step Brief           │
│ - 3-4 Step Sequence  │  │ - Google RSA (30/90 chr) │
│ - Anti-AI Linter     │  │ - Meta 5-Angle Testing   │
│ - 8-Question Audit   │  │ - 100-Pt Scoring Rubrics │
└──────────────────────┘  └──────────────────────────┘
```

### Gate Advancement Governance

- **Gate 1 (Day 7 - Discovery):** Facts separated from assumptions; target opportunity is plausible. Fail action: run targeted research or narrow niche.
- **Gate 2 (Day 14 - Strategy):** Passes 7 Positioning Criteria; zero credibility or business-fit blockers. Fail action: revise promise or replace missing proof with a zero-risk "free slice" offer.
- **Gate 3 (Day 21 - Identity):** Passes 7 Creative Criteria; touchpoints express approved positioning. Fail action: revise prototypes or escalate strategic contradiction.
- **Gate 4 (Day 30 - Launch Readiness):** Assets owned, outreach linted, links/tracking verified, 90-day learning rhythm set. Fail action: hold launch on unresolved critical blockers.

---

## Core Operating Principles (The 90% Hardwork Rule)

1. **Evidence before certainty:** Every skill, metric, and market claim is tagged by source type and confidence (`High`, `Medium`, `Low`).
2. **Honest claims only:** Zero fabricated results, fake scarcity, invented case studies, or inflated percentages.
3. **Decisions over calendar dates:** Never advance past a gate merely because time elapsed. Move when the evidence is documented and approved.
4. **Ask for less, prove more:** Cold emails stay between 74 and 80 words, contain one pain point, one proof point, and one easy ask, with zero links or attachments in Email 1.
5. **Score before launch, judge after:** Pre-launch 100-point rubrics verify ad construction (target 75+/100). Post-launch metrics evaluate real-world market response.

---

## Workspace Folder Standard (For Users Running a Sprint)

- `00_Admin_and_Scope`
- `01_Discovery_and_Research`
- `02_Strategy_and_Positioning`
- `03_Verbal_Identity`
- `04_Visual_Identity`
- `05_Touchpoints_and_Applications`
- `06_Launch_and_Outreach`
- `07_Governance_and_Measurement`
- `08_Final_Handover`

**File Naming Convention:** `NAME_Workstream_Deliverable_v01_YYYY-MM-DD` tagged as `DRAFT`, `FOR_REVIEW`, `APPROVED`, or `SUPERSEDED`.

---

## Quickstart Prompts

### Track A: Land a Job in 30 Days
> "Start a Brandevegen 30-day sprint for Track A. I am a junior full-stack Laravel developer targeting remote product teams. Initiate Gate 0 Research Draft first."

### Track B: Land a Client in 30 Days
> "Run Brandevegen Track B to reposition me as a conversion-focused brand and web strategist and land my first 2 retainer clients in 30 days. Start with the Research Draft."

### Cold Outreach Drafting & Anti-AI Audit
> "Use Brandevegen to draft a 4-email cold outreach sequence to SaaS founders offering a free homepage teardown. Keep Email 1 between 74 and 80 words and run the full Anti-AI linter and 8-question audit."

### Paid Acquisition Copy & 100-Point Scoring
> "Use Brandevegen's Paid Copy Lab to build a Google RSA and 3 Meta ad angles for my freelance UI/UX audit service, then score every draft on the 100-point rubrics."

---

## Scope Boundary & Honesty Notice

"Get a job or land your client in 30 days" defines an intense, structured 30-day execution window built on **90% hardwork** (daily discovery, positioning rigor, proof building, disciplined outreach) and **10% luck** (market timing, hiring cycles, inbox visibility). Brandevegen guarantees a launch-ready personal brand blueprint, linted outreach assets, and measurable operating cadence; it does not guarantee hiring outcomes, client contracts, or revenue.

---

## Versioning

- **v1.0.0** - Initial Brandevegen release integrating the 30-Day Brand Building Method, The Cold Email Copy Playbook, and the Advertising Copywriting Playbook into a unified GitHub-ready personal rebranding skill.
