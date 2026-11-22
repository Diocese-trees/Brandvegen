# Brandevegen Quick Commands & Action Buttons (v1.2)

Use slash commands or reply with a single number (`1`, `2`, `3`, `4`) from the **Next Actions** bar at the bottom of every response. Works on any LLM, mobile app, or terminal.

---

## Core Sprint Commands

| Command | Shortcut / Alias | What It Runs |
| :--- | :--- | :--- |
| `/start` | `/init` | Interactive Track (Job/Client) & Mode (Solo/Team) setup + Gate 0 Research Draft |
| `/status` | `/dash` | 1-screen sprint dashboard: Track, Day, Gate, open `VERIFY` items, KPIs, next step |
| `/gate` | `/audit-gate` | Formal PASS / BLOCKED audit for your current Gate (0, 1, 2, 3, or 4) |
| `/ledger` | `/proof` | View, add entries to, or clear `VERIFY` flags in your Evidence Ledger |
| `/position` | `/pos` | Draft Positioning Statement + 7-criteria evaluation + credibility blocker check |
| `/slice` | `/offer` | Design a zero-risk "free slice" offer to overcome zero-proof cold starts |

## Execution & Audit Commands

| Command | Shortcut / Alias | What It Runs |
| :--- | :--- | :--- |
| `/email` | `/outreach` | Draft Email 1 (74-80 words) + 3-4 step follow-up sequence + Anti-AI & 8Q audit |
| `/lint` | `/check` | Lint pasted copy (email, LinkedIn post, bio, CV bullets) for AI words, dashes, and length |
| `/post [topic]` | `/linkedin` | Run full 13-stage LinkedIn Authority pack (Idea Card -> 11-point review -> 60-min plan) |
| `/ads` | `/paid` | Build 10-field brief + Google RSA (30/90 chars) or Meta 5-angle ads + 100-pt rubric |
| `/split` | `/test` | Generate prioritized split-test variants (Offer, Opening, Subject, 50/50 Language) |

## Memory & Quality-of-Life Commands

| Command | Shortcut / Alias | What It Runs |
| :--- | :--- | :--- |
| `/save` | `/snapshot` | Output a compact Portable Memory Snapshot (Markdown + JSON) for cross-chat/LLM handoff |
| `/load` | `/resume` | Hydrate agent state from a pasted Memory Snapshot and skip onboarding |
| `/mode solo` / `/mode team` | - | Switch between Solo Mode (default) and Team Mode (intern/designer roles) |
| `/brief` / `/deep` | - | Toggle concise 4-8 line blocks (default) vs. detailed step-by-step walkthroughs |
| `/preset` | - | Configure your brand kit, timezone, posting days, and content boundaries (or load Reference Preset) |
| `/help` | `/?` | Display this quick command table |

---

## Universal Quick-Pick Button Bar

Every LLM handles UI differently. Brandevegen adapts automatically:

1. **Platforms with native chips/forms** (e.g., Gemini interactive questionnaires or custom UI apps): Render native tappable options when gathering inputs.
2. **All chat & CLI platforms** (ChatGPT, Claude, Cursor, Ollama, mobile web): Append a 3 to 4 item bracket menu at the bottom of each response:

```text
Next Actions (reply with a number or command):
[1] /gate - Check Gate 2 readiness      [2] /email - Draft Cold Email 1
[3] /post - Build LinkedIn proof post   [4] /save - Export Memory Snapshot
```

Replying with just `2` executes `/email` immediately with your loaded sprint context.
