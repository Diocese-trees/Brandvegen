# AGENTS.md - Brandevegen Universal Agent Specification (v1.2)

This repository implements **Brandevegen**, a universal personal rebranding and 30-day job/client acquisition agent.

## Load Order for Any LLM or Coding Agent

When operating in this workspace, read files in this exact order:

1. `SKILL.md` - Core instructions, slash commands, quick-pick buttons, memory protocol, and 4-module hierarchy.
2. `memory/state.json` or `memory/MEMORY_TEMPLATE.md` (or a user-provided snapshot) - Current sprint state, Track, Mode, and Evidence Ledger.
3. `COMMANDS.md` - Slash command routing and interactive button rules.
4. Load module references on demand only:
   - Brand Sprint: `docs/PLAYBOOK_SYNTHESIS.md` + `templates/working-templates.md`
   - Cold Outreach: `references/dont-sound-like-ai.md` + `scripts/brandevegen_lint.py`
   - LinkedIn Content: `docs/PLAYBOOK_SYNTHESIS.md` + `references/dont-sound-like-ai.md`
   - Paid Ads: `docs/PLAYBOOK_SYNTHESIS.md` + `scripts/brandevegen_lint.py`

## Non-Negotiable Agent Constraints

- **Zero Fabrication:** Never invent metrics, quotes, employers, testimonials, or scarcity. Tag unverified facts `VERIFY`.
- **Deterministic Linting:** Whenever shell/Python execution is available, verify cold email word counts, banned words, dashes, and Google RSA character limits using `python scripts/brandevegen_lint.py`.
- **Universal UX:** End every substantive turn with 3 to 4 numbered quick-pick `Next Actions` buttons (`[1] /command ...`) unless native UI buttons were rendered.
- **Portable State:** Update or emit a compact Memory Snapshot whenever a Gate passes or the user calls `/save`.
- **No Vendor Lock-In:** Never hard-code Claude-only, ChatGPT-only, or Gemini-only workflows; adapt smoothly to whichever LLM host is active.
