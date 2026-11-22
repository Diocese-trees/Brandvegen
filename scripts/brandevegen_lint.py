#!/usr/bin/env python3
"""
Brandevegen Deterministic Copy & Spec Linter (v1.2)
Zero-dependency Python 3 utility for any LLM sandbox or local machine.

Usage:
  python scripts/brandevegen_lint.py email draft.txt
  python scripts/brandevegen_lint.py linkedin post.txt
  python scripts/brandevegen_lint.py google-rsa ads.json
  python scripts/brandevegen_lint.py rubric scores.json
"""

import argparse
import json
import re
import sys
from pathlib import Path

BANNED_WORDS = [
    "delve", "realm", "harness", "tapestry", "paradigm", "cutting-edge",
    "revolutionize", "landscape", "potential", "findings", "intricate",
    "showcasing", "crucial", "pivotal", "surpass", "meticulously", "vibrant",
    "unparalleled", "underscore", "leverage", "synergy", "innovative",
    "game-changer", "game changer", "testament", "commendable", "meticulous",
    "highlight", "emphasize", "boast", "groundbreaking", "align", "foster",
    "showcase", "enhance", "holistic", "garner", "accentuate", "pioneering",
    "trailblazing", "unleash", "versatile", "transformative", "redefine",
    "seamless", "optimize", "scalable", "robust", "breakthrough", "empower",
    "streamline", "intelligent", "smart", "next-gen", "frictionless",
    "elevate", "adaptive", "effortless", "data-driven", "insightful",
    "proactive", "mission-critical", "visionary", "disruptive", "reimagine",
    "agile", "customizable", "unprecedented", "intuitive", "leading-edge",
    "synergize", "democratize", "accelerate", "state-of-the-art", "dynamic",
    "cloud-native", "immersive", "predictive", "proprietary", "plug-and-play",
    "turnkey", "future-proof", "ai-powered", "next-generation", "always-on",
    "results-driven", "unlock", "grab", "solution", "hustle", "crush it",
    "skyrocket", "passionate", "impactful"
]

WEAKENER_WORDS = [
    "quietly", "truly", "simply", "genuinely", "really", "actually", "basically"
]

BANNED_PHRASES = [
    "in today's world",
    "in today's fast-paced world",
    "quick question",
    "honest question",
    "quick one",
    "hope this email finds you well",
    "dear sir/madam",
    "last chance",
    "only today",
    "act now",
    "just bumping this",
    "circling back",
    "following up",
    "checking in",
    "gentle reminder",
    "haven't heard from you",
    "any thoughts?",
    "did you see my last email",
    "brand journey",
    "my journey",
    "on this journey"
]

SIGN_OFF_MARKERS = ("best,", "thanks,", "cheers,", "regards,", "sincerely,")


def find_banned_terms(text: str):
    lower = text.lower()
    word_hits = [w for w in BANNED_WORDS if re.search(r"\b" + re.escape(w) + r"\b", lower)]
    weak_hits = [w for w in WEAKENER_WORDS if re.search(r"\b" + re.escape(w) + r"\b", lower)]
    phrase_hits = [p for p in BANNED_PHRASES if p in lower]
    return word_hits, weak_hits, phrase_hits


def lint_email(text: str):
    lines = [l.rstrip() for l in text.strip().splitlines()]
    subject = None
    body_lines = []
    ps_lines = []
    in_sig = False

    for line in lines:
        low = line.strip().lower()
        if subject is None and low.startswith("subject:"):
            subject = line.split(":", 1)[1].strip()
            continue
        if low.startswith("p.s.") or low.startswith("ps.") or low.startswith("ps:"):
            ps_lines.append(line)
            in_sig = True
            continue
        if low in SIGN_OFF_MARKERS:
            in_sig = True
            continue
        if not in_sig:
            body_lines.append(line)

    body_text = "\n".join(body_lines).strip()
    words = re.findall(r"\b[\w'-]+\b", body_text)
    word_count = len(words)

    issues = []
    warnings = []

    if subject is not None:
        if len(subject) > 50:
            issues.append(f"Subject line is {len(subject)} chars (max 50).")
        if "quick question" in subject.lower():
            issues.append("Subject contains banned phrase 'quick question'.")
        if subject.isupper() and len(subject) > 3:
            issues.append("Subject is ALL CAPS.")

    if word_count > 90:
        issues.append(f"Email body is {word_count} words (hard ceiling <90; target 74-80).")
    elif word_count < 74 or word_count > 80:
        warnings.append(f"Email body is {word_count} words (sweet spot is 74-80; ceiling <90).")

    word_hits, weak_hits, phrase_hits = find_banned_terms(text)
    if word_hits:
        issues.append(f"Banned AI words found: {', '.join(word_hits)}")
    if weak_hits:
        warnings.append(f"Weakener words found (consider cutting): {', '.join(weak_hits)}")
    if phrase_hits:
        issues.append(f"Banned phrases found: {', '.join(phrase_hits)}")

    if "—" in text or "–" in text:
        issues.append("Contains em-dash or en-dash (plain text only).")
    if "!" in body_text:
        issues.append("Contains exclamation mark in email body.")
    if re.search(r"https?://", text):
        issues.append("Contains raw URL/link (forbidden before reply; use [domain.com] in signature).")
    if re.search(r"\*\*.*?\*\*|^[\s]*[-*]\s", body_text, re.MULTILINE):
        issues.append("Contains markdown bold or bullet formatting (plain text only).")
    if ps_lines and re.search(r"\bstop\b", " ".join(ps_lines).lower()):
        issues.append("P.S. opt-out uses spam-trigger word 'stop' (use 'nope' instead).")
    if body_text.count("?") >= 2:
        warnings.append(f"Body contains {body_text.count('?')} question marks (avoid stacking 2+ questions).")

    status = "PASS" if not issues else "FAIL"
    return {
        "mode": "cold_email",
        "status": status,
        "subject_chars": len(subject) if subject is not None else None,
        "body_word_count": word_count,
        "issues": issues,
        "warnings": warnings,
    }


def lint_linkedin(text: str):
    issues = []
    warnings = []

    word_hits, weak_hits, phrase_hits = find_banned_terms(text)
    if word_hits:
        issues.append(f"Banned AI words found: {', '.join(word_hits)}")
    if weak_hits:
        warnings.append(f"Weakener words found: {', '.join(weak_hits)}")
    if phrase_hits:
        issues.append(f"Banned phrases found: {', '.join(phrase_hits)}")

    if "—" in text or "–" in text or " - " in text:
        issues.append("Contains dashes/hyphens as punctuation (banned in LinkedIn post body).")
    if re.search(r"\*\*.*?\*\*", text):
        issues.append("Contains bold formatting (banned in LinkedIn post body).")
    if re.search(r"^[\s]*[-*•]\s", text, re.MULTILINE):
        issues.append("Contains bullet points (banned in LinkedIn post body).")
    if re.search(r"https?://", text):
        issues.append("Contains external URL in post body (move links to first comment at +20 mins).")

    words = re.findall(r"\b[\w'-]+\b", text)
    status = "PASS" if not issues else "FAIL"
    return {
        "mode": "linkedin_post",
        "status": status,
        "word_count": len(words),
        "issues": issues,
        "warnings": warnings,
    }


def lint_google_rsa(data: dict):
    headlines = data.get("headlines", [])
    descriptions = data.get("descriptions", [])
    issues = []

    if len(headlines) > 15:
        issues.append(f"Too many headlines: {len(headlines)} (max 15).")
    if len(descriptions) > 4:
        issues.append(f"Too many descriptions: {len(descriptions)} (max 4).")

    headline_report = []
    for idx, h in enumerate(headlines, 1):
        ok = len(h) <= 30
        headline_report.append({"index": idx, "text": h, "chars": len(h), "limit": 30, "ok": ok})
        if not ok:
            issues.append(f"Headline #{idx} exceeds 30 chars ({len(h)}/30): '{h}'")

    desc_report = []
    for idx, d in enumerate(descriptions, 1):
        ok = len(d) <= 90
        desc_report.append({"index": idx, "text": d, "chars": len(d), "limit": 90, "ok": ok})
        if not ok:
            issues.append(f"Description #{idx} exceeds 90 chars ({len(d)}/90): '{d}'")

    return {
        "mode": "google_rsa",
        "status": "PASS" if not issues else "FAIL",
        "headlines": headline_report,
        "descriptions": desc_report,
        "issues": issues,
    }


def score_rubric(data: dict):
    platform = data.get("platform", "google").lower()
    ratings = data.get("ratings", {})

    weights = {
        "google": {
            "search_intent_alignment": 20,
            "keyword_and_ad_relevance": 15,
            "value_proposition": 15,
            "headline_variety_and_quality": 10,
            "description_clarity": 10,
            "landing_page_alignment": 10,
            "cta_specificity": 5,
            "trust_and_claim_accuracy": 5,
            "technical_and_policy_compliance": 5,
            "offer_clarity": 5,
        },
        "meta": {
            "hook_and_attention": 15,
            "audience_relevance": 15,
            "value_proposition": 15,
            "offer_clarity": 10,
            "creative_and_copy_alignment": 10,
            "message_clarity_and_readability": 10,
            "cta_relevance": 10,
            "credibility_and_evidence": 5,
            "landing_page_alignment": 5,
            "platform_policy_and_technical_compliance": 5,
        },
    }

    if platform not in weights:
        raise ValueError("Platform must be 'google' or 'meta'.")

    total = 0.0
    breakdown = {}
    for crit, w in weights[platform].items():
        r = ratings.get(crit, 0)
        pts = round(r * w / 5.0, 2)
        breakdown[crit] = {"rating": r, "weight": w, "points": pts}
        total += pts

    total = round(total, 2)
    if total >= 90:
        band = "Excellent (90-100)"
    elif total >= 75:
        band = "Strong (75-89)"
    elif total >= 60:
        band = "Needs improvement (60-74) - Revise before launch"
    else:
        band = "Rewrite (<60) - Do not launch"

    return {
        "mode": f"{platform}_rubric",
        "total_score": total,
        "band": band,
        "launch_ready": total >= 75,
        "breakdown": breakdown,
    }


def main():
    parser = argparse.ArgumentParser(description="Brandevegen v1.2 Deterministic Linter")
    parser.add_argument("command", choices=["email", "linkedin", "google-rsa", "rubric"])
    parser.add_argument("file", help="Path to text or JSON file to audit")
    args = parser.parse_args()

    raw = Path(args.file).read_text(encoding="utf-8")
    if args.command == "email":
        result = lint_email(raw)
    elif args.command == "linkedin":
        result = lint_linkedin(raw)
    elif args.command == "google-rsa":
        result = lint_google_rsa(json.loads(raw))
    else:
        result = score_rubric(json.loads(raw))

    print(json.dumps(result, indent=2))
    sys.exit(0 if result.get("status", "PASS") == "PASS" and result.get("launch_ready", True) else 1)


if __name__ == "__main__":
    main()
