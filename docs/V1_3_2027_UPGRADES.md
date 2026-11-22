# Brandevegen v1.3a - 2027 Readiness & LinkedIn Gap Integration Manual

Additive release manual integrating all 10 verified 2027 readiness gaps without changing or removing any v1.0, v1.1, or v1.2 rules.

---

## 1. Gap 1: LinkedIn 360Brew & Profile Coherence Audit (Gate 2 / Gate 3)

LinkedIn's `360Brew` feed and profile relevance AI builds an expertise summary from your **Headline, About, Work History, Role Descriptions, Skills, and Country** and compares every post against that summary before expanding reach beyond 1st-degree connections.

### Mandatory Profile Coherence Checklist (Pass Before Post #1)
- [ ] **Headline:** States target role or buyer problem + core niche keywords plainly (no vague slogans).
- [ ] **About section:** Mirrors the exact 3 to 5 niche terms used across your 4 content pillars.
- [ ] **Work history & role descriptions:** Zero empty role descriptions; every recent role includes concrete deliverables and niche keywords.
- [ ] **Skills section:** Top pinned skills match your positioning pillars (remove unrelated legacy skills).
- [ ] **Location / Country:** Matches your target market context cleanly.
- [ ] **Deterministic check:** Store `profile.niche_keywords` in `memory/state.json` and run `python scripts/brandevegen_lint.py coherence post.txt memory/state.json` before publishing.

---

## 2. Gap 2: 0.5-Second + Plain-Topic Hook Test

Purely cryptic curiosity hooks ("Do you know this 6'5 giant?") can confuse Stage 1 semantic topic classification. Keep the curiosity, but anchor the concrete niche or topic noun plainly in both the visual cover and lines 1 to 2 of the post.

- **Rule:** A stranger AND a feed classifier reading only the cover + first 2 lines must immediately know (a) what exact niche/topic the post covers, and (b) why it matters now.

---

## 3. Gap 3: Anti-Pod Rotation & Out-of-Network Rule (60-Minute Window)

LinkedIn penalizes engagement pods, recurring bursts from the same commenters, and generic one-line replies. Unconnected distribution requires at least one genuine interaction from outside your existing connections.

### Upgraded 60-Minute Engagement Rules
1. **Strict DM rotation:** Never message the same 3 contacts on consecutive posts. Track `recent_dm_contacts` in `memory/state.json` and enforce a minimum 3-post cooldown before messaging the same person again.
2. **Niche micro-creator targeting:** Build a rotating list of 100 to 200 niche micro-creators (posts averaging 10 to 30 comments) and leave substantive, multi-sentence comments on 10 relevant posts per publishing window.
3. **Out-of-network spark:** At least 3 of your 10 comments must be on 2nd-degree or non-connected niche peers so your profile earns out-of-network visits and replies.
4. **Zero bot policy:** Automated or AI-generated comment bots are strictly prohibited.

---

## 4. Gap 4: "Seems Like AI Slop" Flag Defense & POV Swap-Test Gate

LinkedIn allows readers to flag posts as "Seems like AI slop" (reducing reach and surfacing in creator analytics) and suppresses generic posts lacking human perspective.

### 12th LinkedIn Pre-Publish Review Check (Added to the 11-Point Scorecard)
- **Check 12 - POV & Swap-Test Gate:**
  - **The Swap Test:** Replace your name with a random peer's name on your core claim. If the post still reads identically, rewrite it with your own stance.
  - **Firsthand Detail Rule:** Every post must include at least one concrete firsthand observation, teardown screenshot finding, real conversation detail, or verified trade-off you personally examined.
  - **48-Hour Slop Watch:** Log any "AI slop" or low-relevance analytics warning in your 48-hour Idea Bank review and audit the hook/POV before the next post.

---

## 5. Gap 5 (Optional Toggle): 45-60s Vertical Video Teardown (`9:16`)

Optional format override for Module 3 alongside Single Image (`1080x1080`), Carousel (`1080x1350`), and rare Text. LinkedIn parses spoken audio transcripts for Profile Relevance matching.

- **Dimensions & length:** `1080x1920` (`9:16`), 45 to 60 seconds max, burned-in readable captions (safe from UI overlays).
- **First-5-Second Spoken Keyword Rule:** Speak your primary niche keyword and concrete teardown subject out loud within the first 5 seconds so transcript indexing aligns with your profile expertise.
- **Structure:** 0-5s Spoken Keyword Hook -> 5-35s Screen/Visual Teardown of 1 concrete detail -> 35-50s Named Saveable Rule -> 50-60s Real closing question (no hard CTA).

---

## 6. Gap 6 (Optional Toggle): Track B LinkedIn Thought Leader Ads (Module 4)

Optional Track B accelerator allowing solo consultants to sponsor proven personal profile posts directly to target B2B job titles.

- **Organic Proof Gate (Non-Negotiable):** Never sponsor an untested post. Only boost a personal post that already ranked in your top 25% for **Saves** and **Profile Views** organically over 48+ hours.
- **Targeting:** Exact decision-maker job titles, company size, and target geography matching Gate 2 audience prioritization.
- **Compliance & Hygiene:** Respect LinkedIn Thought Leader Ad formatting limits (no fabricated claims, no misleading urgency, clear alignment between the post's insight and your profile's Featured/About conversion path).

---

## 7. Gap 7: Day-1 Domain Warmup & 2027 Deliverability Ignition

Waiting until Week 3 or 4 (Days 22-30) to buy and warm a secondary sending domain breaks a 30-day sprint because 2027 mailbox providers require 2 to 4 weeks of warmup and outright bounce unauthenticated mail.

### Day-1 Pre-Flight Checklist (Start in Gate 0 / Day 1)
- [ ] **Secondary domain purchased:** Separate from your primary personal/company domain (Track B bulk senders) and configured on Day 1.
- [ ] **DNS Authentication:** SPF (strictly under 10 DNS lookups), 2048-bit DKIM, and DMARC policy aligned and verified before sending email #1.
- [ ] **Warmup ramp:** 2 to 4 weeks gradual warmup, capped at 20 to 40 cold emails per inbox per day.
- [ ] **Microsoft 365 tenant awareness:** Account for new M365 tenant 60-day sending limits when choosing infrastructure.
- [ ] **List hygiene & thresholds:** Verify every email address before loading. Hard bounce ceiling `<2%`; spam complaint ceiling `<0.3%` (operating safety target `<0.1%`).
- [ ] **Provider matching & zero tracking:** Route Gmail-to-Gmail and Outlook-to-Outlook where supported; keep open tracking OFF (protects deliverability and EU consent compliance).

---

## 8. Gap 8: AI Inbox Gatekeeper Defense (12-Word Summary Compression Test)

Gmail Gemini and Outlook Copilot compress incoming emails into a 1-line summary before the human decides to open or read. Clever or delayed hooks disappear under AI summarization.

### Mandatory Compression Test (Run in `/email` and `/lint`)
1. Extract the **first 150 characters** of Email 1 (after the greeting).
2. Compress Email 1 into a **12-word factual summary** as an AI inbox assistant would render it.
3. **Pass criteria:** The 12-word summary still clearly preserves (a) the specific recipient pain, (b) concrete proof or relevance, and (c) the zero-risk free slice. If it collapses into generic fluff ("Someone offering marketing help"), rewrite the opening 150 characters immediately.

---

## 9. Gap 9: 5-Day Warm-Signal Bridge + Module 5 (The Close & Free-Slice Handoff)

### 9A. 5-Day Warm-Signal Sequence (Connecting Module 3 -> Module 2)
Instead of blasting ice-cold strangers, warm high-priority targets first:
- **Day 1:** Leave 1 substantive, non-sycophantic comment on the target's recent LinkedIn post (or a relevant thread they engaged with).
- **Day 3:** Send plain-text Cold Email 1 (74-80 words, zero links, `"yes"` CTA).
- **Day 5:** Standalone Follow-Up 2 (new proof or micro-observation, shorter than Email 1).
- **Day 7:** Standalone Follow-Up 3 (optional, different case study/angle, shorter again).
- **Day 9:** Final 1-line referral email (`Hey [FirstName], is there anyone better at [Company] to reach out to about this?`).

### 9B. Module 5: The Close & Free-Slice Handoff (`/close`)
Activates the moment a prospect or hiring manager replies `"yes"`.

1. **Free-Slice Delivery Protocol (No Free Consulting Trap):**
   - Deliver the promised narrow slice within 24 to 48 hours (1-page teardown, 3-minute Loom/screen recording, or mini prototype).
   - Structure the delivery in 3 parts: **What works today** (fairness) -> **Top 2-3 specific gaps found** (evidence) -> **What fixing the deeper system requires** (bridge to paid scope or role impact).
   - Hard boundary: Fix or diagnose the slice only; never execute the full paid project for free.
2. **15-Minute Discovery Call (Track B) / Portfolio Defense Script (Track A):**
   - Min 0-2: Confirm context and why they replied.
   - Min 2-8: Walk through 1 key finding from the Free Slice (or 1 verified project decision) and ask diagnostic questions to uncover cost of inaction.
   - Min 8-12: Present the scoped next step (paid sprint/retainer for Track B; role fit and 30-60-90 day impact for Track A).
   - Min 12-15: Handle objections calmly and confirm exact next date/decision-maker.
3. **Honest Objection Matrix:**
   - *"No budget / hiring freeze"* -> Clarify exact quarter or smaller paid pilot; never invent fake urgency or discounts.
   - *"Send me a proposal / portfolio"* -> Confirm decision criteria and review date before sending.
   - *"We handle this in-house"* -> Ask where the internal bottleneck sits; offer targeted support or bow out cleanly.
4. **1-Page Scope Proposal (Track B):**
   - Problem verified in Free Slice -> Exact Deliverables -> Timeline -> Fixed Price & Terms -> Exclusions -> Single Sign-Off Next Step.

---

## 10. Gap 10: Upgraded Deterministic Linter (`scripts/brandevegen_lint.py`)

Adds 3 new subcommands and 2 upgraded email checks while keeping all v1.2 subcommands 100% backward compatible:
- `email`: Preserves all v1.2 checks + adds `<15w` first-sentence check and first-150-char value-density preview.
- `carousel`: Audits slide count (8-12), cover (15-25w), interior slides (40-55w), closing slide (20-30w), plus banned AI words.
- `coherence`: Audits a LinkedIn post draft against `profile.niche_keywords` in `memory/state.json` for `360Brew` semantic alignment.
- `ai-summary`: Extracts the first 150 chars of an email and flags vague/delayed openings that fail Gmail Gemini / Outlook Copilot compression.
