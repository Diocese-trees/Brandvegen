# Brandevegen

**Goal:** Get a job or land a client in 30 days.

**Rule:** 90% hard work, 10% luck.

Brandevegen is a 30-day rebranding and outreach guide. It helps you show real proof, write short plain-text emails, post useful LinkedIn updates, and run a local check before you send anything.

## Pick your track

| Area | Track A: Get a job | Track B: Land a client |
| --- | --- | --- |
| **Target** | Hiring managers, founders, team leads, recruiters | Business owners, agency founders, department heads |
| **Offer** | Clear skills backed by real work | Clear service plus a small free sample |
| **Proof** | Projects, repos, case notes, real work | Past work or a small free sample with clear limits |
| **Next step** | Interview invite or referral | Reply, free sample, then paid scope |

## How the 30 days work

Start at **Day 1** by logging real facts and starting domain warmup early so your sending setup is ready before outreach starts.

1. **Days 1 to 7: Discover**
   List your real skills, finished work, and gaps. Start domain warmup and list checks early.
2. **Days 8 to 14: Define**
   Pick one target group, write your positioning, and tie every claim to real proof. Align your LinkedIn profile with what you will talk about.
3. **Days 15 to 21: Develop**
   Update your resume, portfolio, or service page so every piece matches.
4. **Days 22 to 30: Deploy**
   Send plain-text outreach, post clear LinkedIn breakdowns, follow up cleanly, and close real conversations.

Move forward when the work for each stage is checked, not just because a date passes.

## How to install

Pick the tool you use.

### Gemini

1. Open this repository and copy `SKILL.md` and the files inside `references/`, `docs/`, and `templates/`.
2. Create a new Gem or skill in Gemini and paste `SKILL.md` as its main instructions.
3. Upload the reference PDFs and markdown guides into the Gem or skill knowledge files.
4. Start a chat and type `/start` or `/gate`.

### ChatGPT

1. Open ChatGPT and create a new Project or Custom GPT.
2. Paste the contents of `SKILL.md` (and `COMMANDS.md`) into the instructions box.
3. Upload `docs/PLAYBOOK_SYNTHESIS.md`, `references/dont-sound-like-ai.md`, `templates/working-templates.md`, and the reference PDFs as knowledge files.
4. Start a chat and type `/start`.

### Local LLM or other LLM

1. Clone or download this repository to your computer.
2. Open a chat with your local model (such as Ollama or LM Studio) or another AI assistant.
3. Paste `AGENTS.md` or `SKILL.md` at the start of the chat, along with `memory/MEMORY_TEMPLATE.md` when you want to save or load progress.
4. Use the offline Python scripts in `scripts/` (`scripts/brandevegen_lint.py` and `scripts/test_brandevegen.py`) in your terminal to check drafts and run tests.

## Core rules

- **Real facts only.** Never invent numbers, client wins, quotes, or fake urgency.
- **Short cold emails.** Keep the first email around 74 to 80 words (under 90 max). Use plain text with no links or attachments until they reply.
- **Simple follow-ups.** Send 3 to 4 follow-ups every other working day in the same thread, ending with a short referral line.
- **Plain language.** Cut stiff buzzwords, hype, and robotic phrasing. Check drafts with `references/dont-sound-like-ai.md` and `scripts/brandevegen_lint.py`.

## Repo layout

```
brandevegen/
├── README.md
├── SKILL.md
├── AGENTS.md
├── COMMANDS.md
├── adapters/
├── docs/
├── memory/
├── references/
├── scripts/
└── templates/
```

## Honest note

A 30-day plan gives you structure, real proof, and steady outreach. It cannot guarantee a job offer or a paying client. Your effort and proof do the heavy lifting; timing and budgets still play a role.
