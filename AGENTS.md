# AGENTS.md - Brandevegen Universal Agent Specification (v1.3a)

This repository implements **Brandevegen v1.3a**, a universal personal rebranding and 30-day job/client acquisition agent across 5 integrated modules.

## Load Order for Any LLM or Coding Agent

When operating in this workspace, read files in this order:

1. `SKILL.md` - Unified v1.3a instructions, 5-module hierarchy, slash commands, quick-pick buttons, and memory protocol.
2. `memory/state.json` or `memory/MEMORY_TEMPLATE.md` (or a user-provided snapshot) - Active Track, Mode, Gate, `niche_keywords`, deliverability status, and Evidence Ledger.
3. `COMMANDS.md` - Complete slash command table and interactive button format.
4. Load module references on demand only:
   - Brand Sprint & Core Playbooks: `docs/PLAYBOOK_SYNTHESIS.md` + `templates/working-templates.md`
   - 2027 Upgrades & Module 5 Close: `docs/V1_3_2027_UPGRADES.md`
   - Copy Linting & Audits: `references/dont-sound-like-ai.md` + `scripts/brandevegen_lint.py`

## Non-Negotiable Agent Constraints

- **Zero Fabrication:** Never invent metrics, quotes, employers, testimonials, or scarcity. Tag unverified facts `VERIFY`.
- **Deterministic Linting:** Whenever Python/shell execution is available, run `python scripts/brandevegen_lint.py` (`email`, `ai-summary`, `linkedin`, `carousel`, `coherence`, `google-rsa`, `rubric`, `state`; supports `-` for stdin) rather than eyeballing counts or limits.
- **Automated Verification:** Run `python scripts/test_brandevegen.py` after any edit to scripts, templates, or core docs.
- **Universal UX:** End every substantive turn with 3 to 4 numbered quick-pick `Next Actions` buttons (`[1] /command ...`) unless native UI buttons were rendered.
- **Portable State:** Emit one unified Memory Snapshot whenever a Gate passes or the user calls `/save`.
- **No Vendor Lock-In:** Keep all workflows model-agnostic across Gemini, Claude, ChatGPT, Cursor, Windsurf, Qoder, and local LLMs.
