#!/usr/bin/env python3
"""
Brandevegen v1.3a Automated Stress-Test & Repo QA Suite
Run from repo root: python scripts/test_brandevegen.py
"""

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINT = ROOT / "scripts" / "brandevegen_lint.py"


def run_cli(args, stdin_text=None):
    res = subprocess.run(
        [sys.executable, str(LINT)] + args,
        input=stdin_text,
        capture_output=True,
        text=True,
    )
    data = json.loads(res.stdout) if res.stdout.strip().startswith("{") else {}
    return res.returncode, data, res.stderr


def main():
    passed = 0
    failed = 0

    def check(name, cond, detail=""):
        nonlocal passed, failed
        if cond:
            passed += 1
            print(f"[PASS] {name}")
        else:
            failed += 1
            print(f"[FAIL] {name} -> {detail}")

    # 1. Repo files & PDFs exist
    required_files = [
        "README.md", "SKILL.md", "AGENTS.md", "COMMANDS.md", ".gitignore",
        "adapters/UNIVERSAL_SETUP.md", "memory/MEMORY_TEMPLATE.md", "memory/state.json",
        "scripts/brandevegen_lint.py", "scripts/test_brandevegen.py",
        "docs/RESEARCH_DRAFT.md", "docs/PLAYBOOK_SYNTHESIS.md", "docs/V1_3_2027_UPGRADES.md",
        "templates/working-templates.md", "references/dont-sound-like-ai.md",
        "references/Advegen-30-Day-Brand-Building-Method.pdf",
        "references/The-Cold-Email-Copy-Playbook.pdf",
        "references/Advegen-Copywriting-Playbook.pdf",
        "references/LinkedIn-Content-Execution-Playbook-v2.4.pdf",
    ]
    missing = [f for f in required_files if not (ROOT / f).exists()]
    check("All 19 required repo files exist", not missing, f"Missing: {missing}")

    # 2. Zero em/en dashes across all Markdown docs & zero legacy brand leaks
    md_files = list(ROOT.rglob("*.md"))
    dash_leaks = [str(p.relative_to(ROOT)) for p in md_files if ("\u2014" in p.read_text(encoding="utf-8") or "\u2013" in p.read_text(encoding="utf-8"))]
    check("Zero em/en dashes across all Markdown files", not dash_leaks, f"Found in: {dash_leaks}")

    legacy_leaks = [str(p.relative_to(ROOT)) for p in md_files if "emplowise" in p.read_text(encoding="utf-8").lower()]
    check("Zero legacy brand mentions across all Markdown files", not legacy_leaks, f"Found in: {legacy_leaks}")

    # 3. SKILL.md under 500 lines & valid frontmatter
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    check("SKILL.md under 500 lines", len(skill_text.splitlines()) < 500, f"{len(skill_text.splitlines())} lines")
    check("SKILL.md starts with valid YAML frontmatter", skill_text.startswith("---\nname: brandevegen\ndescription:"))

    # 4. README.md zero banned AI words
    readme_text = (ROOT / "README.md").read_text(encoding="utf-8")
    sys.path.insert(0, str(ROOT / "scripts"))
    import brandevegen_lint as bl
    w_hits, _, p_hits, s_hits = bl.find_banned_terms(readme_text)
    check("README.md has zero banned AI words/phrases/shapes", not (w_hits or p_hits or s_hits), f"w={w_hits}, p={p_hits}, s={s_hits}")

    # 5. Clean state.json passes validator
    rc, out, _ = run_cli(["state", str(ROOT / "memory" / "state.json")])
    check("memory/state.json passes state schema validator", rc == 0 and out.get("schema_version") == "1.3a", out)

    # 6. Clean cold email passes via stdin ("-") with decimal 1.2% and 2 P.S. lines
    good_email = """Subject: reply rates at northgate

Hey Sarah,

Is your 1.2% reply rate still stuck after 2,000 sends a month? That burns domain reputation and wastes 12 hours a week on dead lists.

I rewrote the outbound sequence for a 10-person studio and replies jumped from 1.2% to 4.8% in three weeks.

Happy to rewrite your first email and send the new version over, for free.

Reply with "yes" and I'll send it over.

Best,
Alex
Copywriter [alexcopy.com]

P.S. If this isn't relevant, reply with "nope" and I won't send you more free stuff.
P.P.S. Liked your breakdown on agency pricing last Tuesday.
"""
    rc, out, _ = run_cli(["email", "-"], stdin_text=good_email)
    check("Clean cold email passes via stdin (decimal + 2 P.S. lines)", rc == 0 and out.get("ps_line_count") == 2 and out.get("first_sentence_words") == 14, out)

    # 7. Adversarial email: bare calendly/www URL, subject emoji, synthetic shapes, 'Kind regards'
    bad_email = """Subject: quick wins \U0001F680

Hey Sarah,

It's not your product. It's your copy. Stop doing cold email. Start doing warm funnels. Book at calendly.com/alex or www.site.com! I just wanted to check in.

Kind regards,
Alex
"""
    rc, out, _ = run_cli(["email", "-"], stdin_text=bad_email)
    issues_joined = " | ".join(out.get("issues", []))
    check(
        "Adversarial email catches bare URL, emoji, synthetic shapes, check in",
        rc == 1 and "emoji" in issues_joined.lower() and "calendly.com/alex" in issues_joined and "Stop doing" in issues_joined and "It's not X" in issues_joined,
        issues_joined,
    )

    # 8. Empty email MUST FAIL
    rc, out, _ = run_cli(["email", "-"], stdin_text="   \n ")
    check("Empty email fails hard", rc == 1 and out.get("status") == "FAIL", out)

    # 9. AI-summary check PASS & FAIL
    rc, out, _ = run_cli(["ai-summary", "-"], stdin_text=good_email)
    check("ai-summary passes on pain-led email", rc == 0 and out.get("status") == "PASS", out)
    rc, out, _ = run_cli(["ai-summary", "-"], stdin_text="Hey Sarah,\n\nMy name is Alex and I am reaching out to introduce our agency.")
    check("ai-summary fails on fluff opener", rc == 1 and out.get("status") == "FAIL", out)

    # 10. Coherence word-boundary check (no 'AI' inside 'email'/'paid'/'daily')
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as sf:
        json.dump({"profile": {"niche_keywords": ["AI", "brand positioning"]}}, sf)
        sf_path = sf.name
    rc, out, _ = run_cli(["coherence", "-", sf_path], stdin_text="I sent an email daily about paid recipes.\nNothing technical here.")
    check("coherence blocks substring false positive ('AI' in 'email'/'paid')", rc == 1 and out.get("matched_keywords") == [], out)
    rc, out, _ = run_cli(["coherence", "-", sf_path], stdin_text="I audited 10 AI tools on their brand positioning this week.\nHere is what broke on page one.")
    check("coherence passes genuine niche_keywords in lines 1-2", rc == 0 and len(out.get("matched_keywords", [])) == 2, out)
    Path(sf_path).unlink(missing_ok=True)

    # 11. Rubric rejects out-of-range (99, -5) and missing criteria
    rc, out, _ = run_cli(["rubric", "-"], stdin_text=json.dumps({"platform": "google", "ratings": {"search_intent_alignment": 99, "offer_clarity": -5}}))
    check("rubric rejects out-of-range & missing criteria", rc == 1 and out.get("launch_ready") is False and out.get("total_score") is None, out)

    # 12. Valid Google rubric computes exact 87.0 Strong
    valid_rubric = {
        "platform": "google",
        "ratings": {
            "search_intent_alignment": 5, "keyword_and_ad_relevance": 4, "value_proposition": 4,
            "headline_variety_and_quality": 4, "description_clarity": 4, "landing_page_alignment": 4,
            "cta_specificity": 5, "trust_and_claim_accuracy": 5, "technical_and_policy_compliance": 5,
            "offer_clarity": 4
        }
    }
    rc, out, _ = run_cli(["rubric", "-"], stdin_text=json.dumps(valid_rubric))
    check("rubric computes exact weighted score 87.0", rc == 0 and out.get("total_score") == 87.0 and out.get("launch_ready") is True, out)

    # 13. Google RSA rejects duplicates, placeholders, empty strings
    bad_rsa = {"headlines": ["Brand Audit", "Brand Audit", "[Service] in [City]", ""], "descriptions": ["Get [service] today."]}
    rc, out, _ = run_cli(["google-rsa", "-"], stdin_text=json.dumps(bad_rsa))
    check("google-rsa rejects duplicates, placeholders, empty headline", rc == 1 and len(out.get("issues", [])) >= 4, out)

    # 14. Carousel rejects bold & URLs inside cover slide
    bad_car = {"slides": ["**Check https://spam.com** " + " ".join(["word"] * 18)] + [" ".join(["word"] * 45)] * 6 + [" ".join(["word"] * 22)]}
    rc, out, _ = run_cli(["carousel", "-"], stdin_text=json.dumps(bad_car))
    check("carousel rejects markdown bold & URLs", rc == 1 and any("URL" in i for i in out.get("issues", [])), out)

    # 15. State validator catches unsafe bounce/spam rates
    bad_state = json.loads((ROOT / "memory" / "state.json").read_text(encoding="utf-8"))
    bad_state["deliverability"]["bounce_rate_pct"] = 3.5
    bad_state["deliverability"]["spam_complaint_pct"] = 0.4
    rc, out, _ = run_cli(["state", "-"], stdin_text=json.dumps(bad_state))
    check("state validator catches >=2% bounce & >=0.3% spam", rc == 1 and len(out.get("issues", [])) == 2, out)

    print(f"\nSUMMARY: {passed} passed, {failed} failed.")
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
