# Brandevegen (v1.2)

**Universal personal rebranding agent for any LLM.**  
**Goal:** Get a job or land a client in 30 days.  
**Rule:** 90% hard work, 10% luck.

Brandevegen works on **Claude, ChatGPT, Gemini, Cursor, Windsurf, Qoder, and local LLMs**. It helps you clarify what you offer, prove your thinking in public, and start real conversations with hiring managers or clients in 30 days.

## What is new in v1.2

- **Works on any LLM.** Removed single-model lock-in. Includes `AGENTS.md`, `SKILL.md`, and 1-step setup guides in `adapters/UNIVERSAL_SETUP.md`.
- **Quick slash commands.** Jump straight to any task with `/start`, `/status`, `/gate`, `/email`, `/lint`, `/post`, `/ads`, `/save`, and `/load`.
- **Quick-pick action buttons.** Every step ends with numbered choices (`[1]`, `[2]`, `[3]`) so you reply with one tap or keystroke on any chat app.
- **Portable memory.** Export your sprint state with `/save` and resume in a new chat or a different LLM with `/load`.
- **Offline linter script.** Run `scripts/brandevegen_lint.py` to check word counts, banned words, dashes, and Google ad character limits with exact math.

## Why this exists

Most job searches and freelance pitches stall for four reasons:

1. **Design before clarity.** People redo their resume or portfolio before explaining what problem they solve.
2. **Robotic outreach.** Long emails packed with stiff phrases get deleted in three seconds.
3. **Weak public proof.** When a manager or founder checks your LinkedIn after an email, they find an empty or generic profile.
4. **Empty claims.** Generic templates push people to invent numbers they cannot back up on a call.

Brandevegen fixes this with four weekly checkpoints, a fact log, plain-text outreach rules, a LinkedIn proof engine, and ad scorecards.

## Pick your track

| What changes | Track A: Get a job | Track B: Land a client |
| :--- | :--- | :--- |
| **Who you reach** | Hiring managers, founders, team leads, recruiters | Business owners, agency founders, department heads |
| **What you offer** | Job-ready skills backed by real work | A clear service plus a small free sample |
| **Primary weapon** | Direct cold email (starts the conversation) | Direct cold email (starts the conversation) |
| **Trust shield** | LinkedIn proof posts (converts profile checks) | LinkedIn proof posts + optional scored ads |
| **Next step** | Interview invite or referral to the right manager | Quick "yes" reply, free sample, then paid work |
| **What you track** | Replies, profile views, interviews booked | Positive replies, saves, DMs, calls, proposals |

## How the 4 modules fit together

Do not run every channel at once. Each module has one clear job:

1. **Module 1: 30-Day Brand Sprint (The Spine)**  
   Four weekly gates (Discover, Define, Develop, Deploy) turn vague skills into clear positioning and verified proof.
2. **Module 2: Cold Outreach Engine (The Sword)**  
   Short 74 to 80 word plain-text emails open doors fast. This drives most replies inside the 30-day window.
3. **Module 3: LinkedIn Authority Engine (The Shield)**  
   Two proof-backed posts per week (8 per month) turn profile checks into trust using a 13-stage workflow, four fixed pillars, and a 60-minute engagement routine.
4. **Module 4: Paid Copy Lab (Optional Accelerator, Track B Only)**  
   Google Search and Meta ad drafts scored out of 100 before spending money. Skip this if you are job hunting or running on zero ad budget.

## Quick commands

| Command | What it does |
| :--- | :--- |
| `/start` | Pick your track (Job or Client), mode (Solo or Team), and build Step 0 Research Draft |
| `/status` | Show your current Day, Gate, blockers, and next single action |
| `/gate` | Run the pass/fail check for your active Gate (0 to 4) |
| `/ledger` | View, add, or clear `VERIFY` flags in your Evidence Ledger |
| `/position` | Draft and score your Positioning Statement plus a zero-risk free sample offer |
| `/email` | Write a 74 to 80 word Email 1 + 3 to 4 step follow-up sequence with full audit |
| `/lint` | Check any cold email, LinkedIn post, bio, or resume bullet against banned words |
| `/post [topic]` | Build a complete 13-stage LinkedIn post pack (copy, design brief, 11-point review) |
| `/ads` | Build and score Google Search (30/90 chars) or Meta ads out of 100 |
| `/save` | Export a compact Memory Snapshot to move across chats or LLMs |
| `/load` | Paste a Memory Snapshot to resume right where you left off |
| `/help` | Show all commands and output modes (`/brief` or `/deep`) |

See `COMMANDS.md` for full examples and shortcuts.

## Quick setup on any LLM

- **Claude / Gemini Skills:** Upload the repo folder or zip as a Skill (uses `SKILL.md`).
- **ChatGPT Custom GPT or Project:** Paste `SKILL.md` into instructions and upload `docs/`, `references/`, and `templates/` as knowledge files.
- **Cursor / Windsurf / Qoder / Codex:** Drop the folder into your workspace. `AGENTS.md` is read automatically.
- **Any other or local LLM:** Copy the single bootstrap prompt from `adapters/UNIVERSAL_SETUP.md`.

## Offline linter script

Test any email or ad copy locally with Python 3 (no extra packages needed):

```bash
python scripts/brandevegen_lint.py email my_draft.txt
python scripts/brandevegen_lint.py linkedin my_post.txt
python scripts/brandevegen_lint.py google-rsa my_ads.json
```

## Core rules

- **Facts only.** Never invent numbers, quotes, client results, testimonials, or fake deadlines. Flag anything unverified as `VERIFY`.
- **Short cold emails.** Keep Email 1 to 74 to 80 words (under 90 max). One problem, one proof point, one easy ask. Plain text only, with no links or attachments until they reply.
- **Clean follow-ups.** Send 3 to 4 emails total, every other working day, in the same thread. End with one referral line asking who the right contact is.
- **Save-worthy LinkedIn posts.** Every post needs a 0.5-second visual hook, a source log, one saveable takeaway, no body links, no hard sales pitch, and an 11-point review pass.
- **No AI buzzwords.** Check every draft against `references/dont-sound-like-ai.md` or `scripts/brandevegen_lint.py`.
- **Score ads first (Track B).** Rate Google and Meta ad drafts out of 100 before spending money. Rewrite anything under 75.

## What is in this repo

```text
brandevegen/
├── SKILL.md                                           # Universal agent instructions (v1.2)
├── AGENTS.md                                          # Cross-tool coding/agent entry point
├── COMMANDS.md                                        # Slash commands and quick-pick button guide
├── README.md                                          # Project guide
├── adapters/
│   └── UNIVERSAL_SETUP.md                             # Setup for Claude, ChatGPT, Gemini, Cursor, local LLMs
├── memory/
│   ├── MEMORY_TEMPLATE.md                             # Human-readable cross-LLM memory file
│   └── state.json                                     # Machine-readable sprint state
├── scripts/
│   └── brandevegen_lint.py                            # Offline Python linter for copy, word counts, and RSA limits
├── docs/
│   ├── RESEARCH_DRAFT.md                              # Pre-run facts, critical audit, and gaps
│   └── PLAYBOOK_SYNTHESIS.md                          # 30-day plan, email, LinkedIn, and ad rules
├── templates/
│   └── working-templates.md                           # Fill-in templates for all 4 modules
└── references/
    ├── dont-sound-like-ai.md                          # Shared + channel-specific anti-AI linter
    ├── Advegen-30-Day-Brand-Building-Method.pdf       # 30-day brand method playbook
    ├── The-Cold-Email-Copy-Playbook.pdf               # Cold email playbook
    ├── Advegen-Copywriting-Playbook.pdf               # Google and Meta ads playbook
    └── LinkedIn-Content-Execution-Playbook-v2.4.pdf   # LinkedIn content execution playbook
```

## Honest note on results

Thirty days gives you a strict work plan, verified proof assets, public authority posts, and live outreach. It cannot guarantee a job offer or signed client. You control the 90% hard work: research, proof, clear writing, and daily outreach. Hiring timing and client budgets make up the 10% luck.

## Version

- **v1.2.0** - Made fully LLM-universal (`AGENTS.md`, `adapters/UNIVERSAL_SETUP.md`), added quick slash commands (`COMMANDS.md`), universal quick-pick action buttons, portable cross-LLM memory (`/save`, `/load`, `memory/`), and offline deterministic linter (`scripts/brandevegen_lint.py`).
- **v1.1.0** - Added Module 3 (LinkedIn Authority Engine v2.4), resolved cross-playbook contradictions, added Solo vs. Team mode, and simplified docs.
- **v1.0.0** - Initial release with the 30-day plan, cold email rules, ad scorecards, templates, and reference playbooks.
