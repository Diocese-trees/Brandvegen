# Brandevegen Quick Commands & Action Buttons (v1.3a)

Use slash commands or reply with a single number (`1`, `2`, `3`, `4`) from the **Next Actions** bar at the bottom of every response. Works on any LLM, mobile app, or terminal.

---

## Sprint, Strategy & Readiness Commands

| Command | Alias | What It Runs |
| :--- | :--- | :--- |
| `/start` | `/init` | Interactive Track (Job/Client) & Mode (Solo/Team) setup + Gate 0 Research Draft |
| `/status` | `/dash` | 1-screen dashboard: Track, Day, Gate, warmup status, open `VERIFY` items, next step |
| `/gate` | `/audit-gate` | Formal PASS / BLOCKED audit for your active Gate (0, 1, 2, 3, or 4) |
| `/deliverability` | `/warmup` | Day-1 domain warmup & 2027 DNS/bounce/spam pre-flight checklist (SPF/DKIM/DMARC, M365 cap) |
| `/coherence` | `/360brew` | LinkedIn `360Brew` Profile Coherence Audit (Headline, About, Roles, Skills, Country vs. `niche_keywords`) |
| `/ledger` | `/proof` | View, append to, or clear `VERIFY` flags in your Evidence Ledger |
| `/position` | `/pos` | Draft Positioning Statement + 7-criteria check (weak credibility/fit = hard blocker) |
| `/slice` | `/offer` | Design a zero-risk "free slice" sample offer to overcome zero-proof cold starts |

## Outreach, Content, Closing & Ads Commands

| Command | Alias | What It Runs |
| :--- | :--- | :--- |
| `/warm` | `/bridge` | Build a 5-Day Warm-Signal Sequence (Day 1 LinkedIn comment -> Day 3 Email 1 -> Days 5-9 follow-ups) |
| `/email` | `/outreach` | Draft Email 1 (74-80w) + 3-4 step follow-up sequence + `<15w` opener, 12w AI-summary & 8Q audit |
| `/lint` | `/check` | Audit pasted email, LinkedIn post, carousel, bio, or CV bullets against banned words & limits |
| `/post [topic]` | `/linkedin` | Run full 13-stage LinkedIn Authority pack (Idea Card -> 12-point review -> Anti-Pod 60-min plan) |
| `/video [topic]` | `/reel` | Optional 45-60s `9:16` Vertical Video Teardown with First-5-Second Spoken Keyword Rule |
| `/close` | `/handoff` | Run Module 5: 24-48h Free-Slice delivery, 15-min call/interview script, objections, 1-page proposal |
| `/ads` | `/paid` | Build 10-field brief + Google RSA (30/90 chars) or Meta 5-angle ads + 100-pt rubric (Track B) |
| `/tla` | `/boost` | Optional Track B LinkedIn Thought Leader Ad check (gated to top-quartile organic Save winners) |
| `/split` | `/test` | Generate prioritized split-test variants (Offer, Opening, Subject, 50/50 Language) |

## Memory & Quality-of-Life Commands

| Command | Alias | What It Runs |
| :--- | :--- | :--- |
| `/save` | `/snapshot` | Output one unified Portable Memory Snapshot (<45 lines) for cross-chat or cross-LLM handoff |
| `/load` | `/resume` | Hydrate agent state from a pasted Memory Snapshot and skip redundant onboarding |
| `/mode solo` / `/mode team` | - | Switch between Solo Mode (default) and Team Mode (intern/designer roles) |
| `/brief` / `/deep` | - | Toggle concise 4-8 line blocks (default) vs. detailed step-by-step walkthroughs |
| `/preset` | - | Configure your brand kit, timezone, posting days, and content boundaries (or load Reference Preset) |
| `/help` | `/?` | Display this quick command reference |

---

## Universal Quick-Pick Button Bar

1. **Host apps with native buttons/chips:** Render native tappable controls when collecting structured input.
2. **All chat & terminal apps:** Append 3 to 4 stage-relevant options at the bottom of every response:

```text
Next Actions (reply with a number or command):
[1] /deliverability - Day-1 warmup     [2] /coherence - Audit LinkedIn
[3] /warm - Build 5-day warm bridge    [4] /save - Export Memory Snapshot
```

Replying with just `3` executes `/warm` immediately using your loaded sprint state.
