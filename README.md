# Brandevegen (v1.3a)

**Universal personal rebranding agent for any LLM.**  
**Goal:** Get a job or land a client in 30 days.  
**Rule:** 90% hard work, 10% luck.

Brandevegen works on **Claude, ChatGPT, Gemini, Cursor, Windsurf, Qoder, and local LLMs**. It helps you clarify what you offer, warm your sending setup on Day 1, prove your thinking in public, start direct conversations, and close replies into offers in 30 days.

## What is new in v1.3a (Hardened & Unified)

Version 1.3a stress-tests and unifies every rule from v1.0 through v1.3 into one clean system with zero contradictions:

- **Unified 5-module flow.** Merged all scattered v1.2/v1.3 add-ons into one unified playbook, one memory snapshot block, and one 12-point LinkedIn review checklist.
- **Hardened offline linter (`scripts/brandevegen_lint.py`).** Fixed 8 edge-case bugs found in stress testing: catches bare links (`calendly.com/...`, `www...`), subject emojis, synthetic AI sentence shapes, empty drafts, out-of-range rubric scores, duplicate/bracketed Google ads, carousel URLs/bold text, and false-positive keyword matches. Added stdin (`-`) piping and `state` JSON validation.
- **Automated QA suite (`scripts/test_brandevegen.py`).** Run one command to verify all linter rules, repo links, schema validity, and anti-AI checks.
- **Full 2027 readiness built in.** Includes Day-1 domain warmup, LinkedIn `360Brew` profile checks, plain-topic hooks, anti-pod DM rotation, AI-slop POV defense, AI inbox 12-word summary checks, a 5-day warm bridge, and Module 5 closing scripts.

## Why this exists

Most job searches and freelance pitches stall for five reasons:

1. **Design before clarity.** People redo their resume or portfolio before explaining what problem they solve.
2. **Cold domains and late setup.** Waiting until Week 4 to warm an inbox sends emails straight to bounce or spam.
3. **Robotic outreach.** Long emails packed with stiff phrases get crushed by AI inbox summaries and deleted in three seconds.
4. **Weak public proof.** When a manager or founder checks your LinkedIn after an email, they find an empty or off-topic profile.
5. **No plan after "yes".** People get a reply and either give away free consulting or fumble the 15-minute call.

Brandevegen fixes all five with four weekly gates, a fact log, plain-text outreach rules, a LinkedIn proof engine, closing scripts, and an offline Python linter.

## Pick your track

| What changes | Track A: Get a job | Track B: Land a client |
| :--- | :--- | :--- |
| **Who you reach** | Hiring managers, founders, team leads, recruiters | Business owners, agency founders, department heads |
| **What you offer** | Job-ready skills backed by real work | A clear service plus a small free sample |
| **Primary weapon** | Direct cold email + 5-day warm LinkedIn bridge | Direct cold email + 5-day warm LinkedIn bridge |
| **Trust shield** | LinkedIn proof posts (converts profile checks) | LinkedIn proof posts + optional scored ads |
| **Post-reply close** | Free sample delivery + 15-min portfolio call | Free sample delivery + 15-min discovery call + 1-page proposal |
| **What you track** | Replies, profile views, interviews booked | Positive replies, saves, DMs, calls, proposals |

## How the 5 modules work together

Do not run every channel on Day 1. Follow this exact order of force:

1. **Module 1: 30-Day Brand Sprint (The Spine)**  
   Four weekly gates (Discover, Define, Develop, Deploy) plus Day-1 domain warmup turn vague skills into clear positioning and verified proof.
2. **Module 2: Cold Outreach Engine (The Sword)**  
   Short 74 to 80 word plain-text emails (and a 5-day LinkedIn-comment warm bridge) open doors fast inside 30 days.
3. **Module 3: LinkedIn Authority Engine (The Shield)**  
   Two proof-backed posts per week starting in Week 3 convert profile checks into trust using a 13-stage workflow, `360Brew` profile checks, anti-pod rotation, and a 12-point review.
4. **Module 4: Paid Copy Lab (Optional Accelerator, Track B Only)**  
   Google Search, Meta, and LinkedIn Thought Leader ads scored out of 100 before spending money. Skip if job hunting or running on zero ad budget.
5. **Module 5: The Close & Free-Slice Handoff (The Closer)**  
   Turns a `"yes"` reply into an interview or paid project with a 24 to 48 hour free-sample handoff, a 15-minute call script, honest objection replies, and a 1-page scope proposal.

## How the 30 days work

Start with **Step 0 (Research Draft)** and run `/deliverability` on Day 1 if using a sending domain.

1. **Days 1 to 7: Discover (Gate 1)**  
   Start domain warmup, audit your skills, study your market, and separate facts from guesses.
2. **Days 8 to 14: Define (Gate 2)**  
   Pick one target group, lock positioning, tie every claim to proof, and run `/coherence` to match your LinkedIn profile to your niche keywords.
3. **Days 15 to 21: Develop (Gate 3)**  
   Update LinkedIn, portfolio, resume, or service page. Publish your first 2 LinkedIn proof posts so your profile backs up your outreach.
4. **Days 22 to 30: Deploy (Gate 4)**  
   Run daily outreach and warm bridges, complete 60-minute LinkedIn engagement windows, handle replies with Module 5 (`/close`), and review metrics weekly for 90 days.

Do not move to the next week because the calendar says so. Move when the work for the current gate is done and verified.

## Quick commands

Every response also ends with 3 to 4 numbered quick-pick actions (`[1]`, `[2]`, `[3]`, `[4]`) so you can reply with one keystroke on any chat app.

| Command | What it does |
| :--- | :--- |
| `/start` | Pick Track (Job/Client), Mode (Solo/Team), and build Step 0 Research Draft |
| `/status` | Show current Day, Gate, blockers, open `VERIFY` items, and next single action |
| `/gate` | Run the PASS / BLOCKED audit for your active Gate (0 to 4) |
| `/deliverability` | Run the Day-1 domain warmup and 2027 DNS, bounce, and spam checklist |
| `/coherence` | Audit LinkedIn profile fields against your `niche_keywords` (`360Brew`) |
| `/ledger` | View, add to, or clear `VERIFY` flags in your Evidence Ledger |
| `/position` | Draft and 7-criteria-score your Positioning Statement |
| `/slice` | Design a low-cost, zero-risk free sample offer when client numbers are missing |
| `/warm` | Build a 5-day LinkedIn-comment-to-cold-email warm sequence |
| `/email` | Write Email 1 (74-80 words) + 3-4 step follow-up sequence with AI-summary & anti-AI checks |
| `/lint` | Check any email, LinkedIn post, carousel, bio, or CV bullet against banned words & limits |
| `/post [topic]` | Build a complete 13-stage LinkedIn post pack (copy, design brief, 12-point review, 60-min plan) |
| `/video [topic]` | Optional 45-60s vertical video teardown script (spoken niche keyword in first 5s) |
| `/close` | Run Module 5: Free-Slice delivery, 15-min call script, objections, and 1-page proposal |
| `/ads` | Build and score Google Search (30/90 chars) or Meta 5-angle ads out of 100 (Track B) |
| `/tla` | Optional Track B LinkedIn Thought Leader Ad check for proven organic Save winners |
| `/split` | Build prioritized split tests (Offer, Opening, Subject, 50/50 Language) |
| `/save` / `/load` | Export or paste a single Portable Memory Snapshot across chats or LLMs |
| `/mode solo` / `/mode team` | Switch between Solo Mode (default) and Team Mode |
| `/brief` / `/deep` | Toggle short 4-8 line blocks (default) vs. detailed walkthroughs |
| `/preset` / `/help` | Configure brand kit/timezone/boundaries or print all commands |

See `COMMANDS.md` for shortcuts and aliases.

## Quick setup on any LLM

- **Claude / Gemini Skills:** Upload the repo folder or `brandevegen-v1.3a.zip` as a Skill (reads `SKILL.md`).
- **ChatGPT Custom GPT or Project:** Paste `SKILL.md` into Instructions, enable Code Interpreter, and upload `COMMANDS.md`, `docs/`, `templates/`, `memory/`, `scripts/`, and `references/`.
- **Cursor / Windsurf / Qoder / Codex:** Drop the folder into your workspace (`AGENTS.md` loads automatically).
- **Local LLMs (Ollama / LM Studio):** Copy the single bootstrap prompt from `adapters/UNIVERSAL_SETUP.md`.

## Offline linter & QA test suite

Run deterministic checks locally with Python 3 (zero external dependencies):

```bash
python scripts/brandevegen_lint.py email my_draft.txt
python scripts/brandevegen_lint.py ai-summary my_draft.txt
python scripts/brandevegen_lint.py linkedin my_post.txt
python scripts/brandevegen_lint.py carousel my_slides.json
python scripts/brandevegen_lint.py coherence my_post.txt memory/state.json
python scripts/brandevegen_lint.py google-rsa my_ads.json
python scripts/brandevegen_lint.py rubric my_scores.json
python scripts/brandevegen_lint.py state memory/state.json

# Pipe directly from stdin using "-"
cat my_draft.txt | python scripts/brandevegen_lint.py email -

# Run the full automated repo & linter QA suite
python scripts/test_brandevegen.py
```

## Core rules

- **Facts only.** Never invent numbers, quotes, client results, testimonials, or fake deadlines. Flag anything unverified as `VERIFY`.
- **Warm early.** Start domain warmup on Day 1 (SPF <10 lookups, 2048-bit DKIM, DMARC, <2% bounce, <0.3% spam, zero open tracking).
- **Short cold emails.** Keep Email 1 to 74-80 words (<90 max, first sentence <15 words). First 150 characters must survive a 12-word AI inbox summary. Plain text only, zero links or attachments until they reply, `"nope"` opt-out (never `"stop"`).
- **Save-worthy LinkedIn posts.** Pass `360Brew` profile coherence, plain-topic hooks, anti-pod DM rotation (3-post cooldown), zero body links/dashes/bold/bullets, and all 12 review checks (including the POV Swap Test).
- **Score ads first (Track B).** Rate Google and Meta drafts out of 100 before spending money; rewrite anything under 75. Sponsor LinkedIn Thought Leader Ads only on top-quartile organic Save winners.

## What is in this repo

```text
brandevegen/
├── .gitignore
├── README.md                                          # Project guide (v1.3a)
├── SKILL.md                                           # Unified universal agent spec (v1.3a)
├── AGENTS.md                                          # Coding/workspace agent entry point
├── COMMANDS.md                                        # Full slash commands & quick-pick buttons
├── adapters/
│   └── UNIVERSAL_SETUP.md                             # Setup for Claude, ChatGPT, Gemini, Cursor, local LLMs
├── memory/
│   ├── MEMORY_TEMPLATE.md                             # Single unified cross-LLM memory snapshot
│   └── state.json                                     # Clean v1.3a machine-readable sprint state
├── scripts/
│   ├── brandevegen_lint.py                            # Hardened 8-command offline Python linter
│   └── test_brandevegen.py                            # Automated stress-test & repo QA suite
├── docs/
│   ├── RESEARCH_DRAFT.md                              # Gate 0 evidence ledger, audit, and 2027 gaps
│   ├── PLAYBOOK_SYNTHESIS.md                          # Unified 5-module operational reference
│   └── V1_3_2027_UPGRADES.md                          # Deep 2027 LinkedIn, inbox, and closing manual
├── templates/
│   └── working-templates.md                           # 14 fill-in templates across all 5 modules
└── references/
    ├── dont-sound-like-ai.md                          # Shared + channel-specific anti-AI linter
    ├── Advegen-30-Day-Brand-Building-Method.pdf       # Playbook 1: 30-day brand method
    ├── The-Cold-Email-Copy-Playbook.pdf               # Playbook 2: Cold email copy rules
    ├── Advegen-Copywriting-Playbook.pdf               # Playbook 3: Google & Meta ads playbook
    └── LinkedIn-Content-Execution-Playbook-v2.4.pdf   # Playbook 4: LinkedIn content execution
```

## Honest note on results

Thirty days gives you a strict work plan, warmed outreach infrastructure, verified proof assets, public authority posts, and a clean closing process. It cannot guarantee a job offer or signed client. You control the 90% hard work: research, proof, clear writing, and daily outreach. Hiring timing and client budgets make up the 10% luck.

## Version

- **v1.3a** - Harsh stress-test optimization release: unified all split v1.2/v1.3 docs into one zero-contradiction spec, hardened `brandevegen_lint.py` against 8 edge-case bypasses, added `state` validation and stdin piping, cleaned `state.json` schema, and added automated `scripts/test_brandevegen.py` QA suite.
- **v1.3.0** - Added 10 verified 2027 readiness upgrades (Day-1 warmup, `360Brew` coherence, plain-topic hooks, anti-pod rotation, 12th AI-slop POV check, AI inbox summary check, 5-day warm bridge, Module 5 Close Kit, optional vertical video and Thought Leader Ads).
- **v1.2.0** - Made fully LLM-universal with slash commands, quick-pick buttons, portable memory, and offline linter.
- **v1.1.0** - Added LinkedIn Authority Engine v2.4, Machiavellian systems audit, and Solo/Team modes.
- **v1.0.0** - Initial release with 30-day brand plan, cold email rules, ad scorecards, and templates.
