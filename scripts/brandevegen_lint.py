#!/usr/bin/env python3
"""
Brandevegen Deterministic Copy, Spec & State Linter (v1.3a - Hardened)
Zero-dependency Python 3 utility for any LLM sandbox or local machine.

Subcommands (use "-" as file path to read from stdin):
  python scripts/brandevegen_lint.py email draft.txt
  python scripts/brandevegen_lint.py ai-summary draft.txt
  python scripts/brandevegen_lint.py linkedin post.txt
  python scripts/brandevegen_lint.py carousel slides.json
  python scripts/brandevegen_lint.py coherence post.txt memory/state.json
  python scripts/brandevegen_lint.py google-rsa ads.json
  python scripts/brandevegen_lint.py rubric scores.json
  python scripts/brandevegen_lint.py state memory/state.json
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
    "quietly", "truly", "simply", "genuinely", "really", "actually", "basically", "just"
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
    "check in",
    "gentle reminder",
    "haven't heard from you",
    "any thoughts?",
    "did you see my last email",
    "brand journey",
    "my journey",
    "on this journey"
]

# Synthetic AI sentence shapes (regex, human label)
SYNTHETIC_SHAPES = [
    (r"\bmost people do\b.+?\bthe few who win\b", "Synthetic shape: 'Most people do X. The few who win do Y.'"),
    (r"\bstop doing\b.+?[.!]\s*\bstart doing\b", "Synthetic shape: 'Stop doing X. Start doing Y.'"),
    (r"\bit(?:'s| is) not\b[^.!?\n]{1,60}[.]\s*\bit(?:'s| is)\b", "Synthetic shape: 'It's not X. It's Y.'"),
    (r"\bhere(?:'s| is) the truth\s*:", "Synthetic shape: 'Here's the truth: ...'"),
    (r"\bif you(?:'re| are) not\b.+?\balready behind\b", "Synthetic shape: 'If you're not doing X, you're already behind.'"),
    (r"\byou don(?:'t| not) need more\b.+?\byou need\b", "Synthetic shape: 'You don't need more X. You need Y.'"),
    (r"\bthis is the thing that decides everything\b", "Synthetic shape: 'This is the thing that decides everything.'"),
    (r"\b(chance for human error|can lead to missed opportunities|slipping through the cracks)\b", "Hedged cost statement (state what actually happens as a fact)."),
]

SIGN_OFF_MARKERS = (
    "best,", "best regards,", "kind regards,", "warm regards,",
    "thanks,", "thank you,", "cheers,", "regards,", "sincerely,", "warmly,", "--"
)

# Detect raw URLs, www domains, and bare links (excluding bracketed signature domains like [northgate.com])
BARE_URL_RE = re.compile(
    r"(?<!\[)\b(?:https?://\S+|www\.[a-z0-9-]+\.[a-z]{2,}\S*|(?:calendly\.com|cal\.com|bit\.ly|tinyurl\.com|loom\.com|linktr\.ee|notion\.site|docs\.google\.com)/\S+)\b",
    re.IGNORECASE,
)

# Basic emoji / pictograph range detector
EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001F9FF"
    "\U0001FA00-\U0001FAFF"
    "\u2600-\u27BF"
    "]",
    flags=re.UNICODE,
)


def read_input(path_arg: str) -> str:
    if path_arg == "-":
        return sys.stdin.read()
    return Path(path_arg).read_text(encoding="utf-8")


def find_banned_terms(text: str):
    lower = text.lower()
    word_hits = [w for w in BANNED_WORDS if re.search(r"\b" + re.escape(w) + r"\b", lower)]
    weak_hits = [w for w in WEAKENER_WORDS if re.search(r"\b" + re.escape(w) + r"\b", lower)]
    phrase_hits = [p for p in BANNED_PHRASES if re.search(r"\b" + re.escape(p) + r"(?:\b|(?=\?))", lower)]
    shape_hits = [label for pat, label in SYNTHETIC_SHAPES if re.search(pat, lower, re.DOTALL)]
    return word_hits, weak_hits, phrase_hits, shape_hits


def find_unbracketed_urls(text: str):
    # Remove properly bracketed plain-text signature domains like [northgate.com]
    cleaned = re.sub(r"\[[a-z0-9.-]+\.[a-z]{2,}\]", "", text, flags=re.IGNORECASE)
    return BARE_URL_RE.findall(cleaned)


def extract_email_parts(text: str):
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
        if re.match(r"^p(\.p)*\.?s\.?:?\s", low):
            ps_lines.append(line)
            in_sig = True
            continue
        if low in SIGN_OFF_MARKERS:
            in_sig = True
            continue
        if not in_sig:
            body_lines.append(line)

    body_text = "\n".join(body_lines).strip()
    non_empty = [l.strip() for l in body_lines if l.strip()]
    if non_empty and re.match(r"^(hey|hi|hello|dear)\b", non_empty[0].lower()):
        post_greeting = "\n".join(non_empty[1:]).strip()
    else:
        post_greeting = body_text
    return subject, body_text, post_greeting, ps_lines


def split_first_sentence(text: str) -> str:
    if not text:
        return ""
    # Split on sentence-ending punctuation followed by whitespace/EOL (avoid splitting decimals like 1.2%)
    m = re.search(r"(?<!\d)[.?!](?:\s+|$)", text)
    if m:
        return text[: m.end()].strip()
    return text.splitlines()[0].strip()


def lint_email(text: str):
    if not text or not text.strip():
        return {
            "mode": "cold_email",
            "status": "FAIL",
            "subject_chars": None,
            "body_word_count": 0,
            "first_sentence_words": 0,
            "first_150_chars_preview": "",
            "issues": ["Input email is empty."],
            "warnings": [],
        }

    subject, body_text, post_greeting, ps_lines = extract_email_parts(text)
    words = re.findall(r"\b[\w'-]+\b", body_text)
    word_count = len(words)

    issues = []
    warnings = []

    if word_count == 0:
        issues.append("Email body has 0 words.")

    if subject is not None:
        if len(subject) > 50:
            issues.append(f"Subject line is {len(subject)} chars (max 50).")
        if "quick question" in subject.lower():
            issues.append("Subject contains banned phrase 'quick question'.")
        if subject.isupper() and len(subject) > 3:
            issues.append("Subject is ALL CAPS.")
        if EMOJI_RE.search(subject):
            issues.append("Subject contains emoji (banned in cold email subject lines).")

    if word_count > 90:
        issues.append(f"Email body is {word_count} words (hard ceiling <90; target 74-80).")
    elif 0 < word_count < 74 or word_count > 80:
        warnings.append(f"Email body is {word_count} words (sweet spot is 74-80; ceiling <90).")

    first_sentence = split_first_sentence(post_greeting)
    first_sentence_words = len(re.findall(r"\b[\w'-]+\b", first_sentence))
    if first_sentence_words > 15:
        warnings.append(
            f"Opening sentence is {first_sentence_words} words (target <15 words for one-breath readability)."
        )

    word_hits, weak_hits, phrase_hits, shape_hits = find_banned_terms(text)
    if word_hits:
        issues.append(f"Banned AI words found: {', '.join(word_hits)}")
    if weak_hits:
        warnings.append(f"Weakener words found (consider cutting): {', '.join(weak_hits)}")
    if phrase_hits:
        issues.append(f"Banned phrases found: {', '.join(phrase_hits)}")
    for sh in shape_hits:
        issues.append(sh)

    if "\u2014" in text or "\u2013" in text:
        issues.append("Contains em-dash or en-dash (plain text only).")
    if "!" in body_text:
        issues.append("Contains exclamation mark in email body.")
    url_hits = find_unbracketed_urls(text)
    if url_hits:
        issues.append(f"Contains link/URL before reply ({', '.join(url_hits)}). Remove links; use [domain.com] in signature.")
    if re.search(r"\*\*.*?\*\*|^[\s]*[-*]\s", body_text, re.MULTILINE):
        issues.append("Contains markdown bold or bullet formatting (plain text only).")
    if ps_lines and re.search(r"\bstop\b", " ".join(ps_lines).lower()):
        issues.append("P.S. opt-out uses spam-trigger word 'stop' (use 'nope' instead).")
    if body_text.count("?") >= 2:
        warnings.append(f"Body contains {body_text.count('?')} question marks (avoid stacking 2+ questions).")

    return {
        "mode": "cold_email",
        "status": "PASS" if not issues else "FAIL",
        "subject_chars": len(subject) if subject is not None else None,
        "body_word_count": word_count,
        "first_sentence_words": first_sentence_words,
        "ps_line_count": len(ps_lines),
        "first_150_chars_preview": re.sub(r"\s+", " ", post_greeting)[:150],
        "issues": issues,
        "warnings": warnings,
    }


def lint_ai_summary(text: str):
    if not text or not text.strip():
        return {
            "mode": "ai_summary_check",
            "status": "FAIL",
            "subject": None,
            "first_150_chars": "",
            "issues": ["Input email is empty."],
            "warnings": [],
        }

    subject, body_text, post_greeting, _ = extract_email_parts(text)
    lead_150 = re.sub(r"\s+", " ", post_greeting)[:150].strip()
    issues = []
    warnings = []

    if len(lead_150) < 40:
        issues.append("Opening after greeting is too short to convey concrete pain and relevance.")

    fluff_starts = (
        "my name is", "i am reaching out", "i'm reaching out", "we are a", "we're a",
        "i wanted to", "i noticed your profile", "congrats on", "i hope you"
    )
    low_lead = lead_150.lower()
    for f in fluff_starts:
        if low_lead.startswith(f):
            issues.append(f"First 150 chars start with self-centered/fluff opener ('{f}'). Lead with recipient pain.")

    has_number = bool(re.search(r"\d", body_text))
    has_free_offer = any(k in body_text.lower() for k in ("for free", "free ", "no risk", "no cost", "happy to"))
    if not has_number and not has_free_offer:
        warnings.append("Body lacks both a concrete numeral and a zero-risk free slice offer (weak AI summary value).")

    word_hits, _, phrase_hits, shape_hits = find_banned_terms(lead_150)
    if word_hits or phrase_hits:
        issues.append(f"Banned terms inside first 150 chars: {', '.join(word_hits + phrase_hits)}")
    for sh in shape_hits:
        issues.append(f"First 150 chars trigger {sh}")

    return {
        "mode": "ai_summary_check",
        "status": "PASS" if not issues else "FAIL",
        "subject": subject,
        "first_150_chars": lead_150,
        "has_verifiable_numeral": has_number,
        "has_low_risk_offer_cue": has_free_offer,
        "manual_prompt": "Compress this email into 12 factual words; confirm pain + proof + free slice all survive.",
        "issues": issues,
        "warnings": warnings,
    }


def lint_linkedin(text: str):
    if not text or not text.strip():
        return {
            "mode": "linkedin_post",
            "status": "FAIL",
            "word_count": 0,
            "issues": ["Input LinkedIn post is empty."],
            "warnings": [],
        }

    issues = []
    warnings = []

    word_hits, weak_hits, phrase_hits, shape_hits = find_banned_terms(text)
    if word_hits:
        issues.append(f"Banned AI words found: {', '.join(word_hits)}")
    if weak_hits:
        warnings.append(f"Weakener words found (consider cutting): {', '.join(weak_hits)}")
    if phrase_hits:
        issues.append(f"Banned phrases found: {', '.join(phrase_hits)}")
    for sh in shape_hits:
        issues.append(sh)

    if "\u2014" in text or "\u2013" in text or " - " in text:
        issues.append("Contains dashes/hyphens as punctuation (banned in LinkedIn post body).")
    elif re.search(r"\w-\w", text):
        warnings.append("Contains hyphenated compound word(s); strict LinkedIn Playbook prefers removing all hyphens.")

    if re.search(r"\*\*.*?\*\*", text):
        issues.append("Contains bold formatting (banned in LinkedIn post body).")
    if re.search(r"^[\s]*[-*\u2022]\s", text, re.MULTILINE):
        issues.append("Contains bullet points (banned in LinkedIn post body).")
    url_hits = find_unbracketed_urls(text)
    if url_hits:
        issues.append(f"Contains external link in post body ({', '.join(url_hits)}). Move links to first comment at +20 mins.")

    words = re.findall(r"\b[\w'-]+\b", text)
    return {
        "mode": "linkedin_post",
        "status": "PASS" if not issues else "FAIL",
        "word_count": len(words),
        "issues": issues,
        "warnings": warnings,
    }


def lint_carousel(data: dict):
    slides = data.get("slides", [])
    issues = []
    warnings = []
    report = []

    if not isinstance(slides, list) or len(slides) == 0:
        return {
            "mode": "linkedin_carousel",
            "status": "FAIL",
            "slide_count": 0,
            "slides": [],
            "issues": ["'slides' must be a non-empty JSON list of 8 to 12 slide strings."],
            "warnings": [],
        }

    total = len(slides)
    if total < 8 or total > 12:
        issues.append(f"Carousel has {total} slides (required range: 8 to 12 slides).")

    for idx, slide_text in enumerate(slides, 1):
        if not isinstance(slide_text, str) or not slide_text.strip():
            issues.append(f"Slide {idx} is empty.")
            report.append({"slide": idx, "role": "invalid", "words": 0, "ok": False, "notes": ["empty slide"]})
            continue

        wc = len(re.findall(r"\b[\w'-]+\b", slide_text))
        if idx == 1:
            role, lo, hi = "cover", 15, 25
        elif idx == total:
            role, lo, hi = "closing", 20, 30
        else:
            role, lo, hi = "content", 40, 55

        ok = lo <= wc <= hi
        word_hits, _, phrase_hits, shape_hits = find_banned_terms(slide_text)
        url_hits = find_unbracketed_urls(slide_text)
        has_bold = bool(re.search(r"\*\*.*?\*\*", slide_text))
        has_dash = ("\u2014" in slide_text or "\u2013" in slide_text or " - " in slide_text)

        slide_issues = []
        if not ok:
            slide_issues.append(f"{wc} words (target {lo}-{hi})")
            issues.append(f"Slide {idx} ({role}) is {wc} words (required {lo}-{hi}).")
        if word_hits or phrase_hits:
            terms = ", ".join(word_hits + phrase_hits)
            slide_issues.append(f"banned terms: {terms}")
            issues.append(f"Slide {idx} contains banned terms: {terms}")
        for sh in shape_hits:
            slide_issues.append(sh)
            issues.append(f"Slide {idx}: {sh}")
        if url_hits:
            slide_issues.append(f"contains URL: {', '.join(url_hits)}")
            issues.append(f"Slide {idx} contains URL ({', '.join(url_hits)}).")
        if has_bold:
            slide_issues.append("contains raw markdown bold")
            issues.append(f"Slide {idx} contains raw markdown bold (**...**).")
        if has_dash:
            slide_issues.append("contains punctuation dash")
            issues.append(f"Slide {idx} contains em/en/spaced dash.")

        report.append({
            "slide": idx,
            "role": role,
            "words": wc,
            "target": f"{lo}-{hi}",
            "ok": not slide_issues,
            "notes": slide_issues,
        })

    return {
        "mode": "linkedin_carousel",
        "status": "PASS" if not issues else "FAIL",
        "slide_count": total,
        "slides": report,
        "issues": issues,
        "warnings": warnings,
    }


def keyword_present(keyword: str, text: str) -> bool:
    """Strict word-boundary match so 'AI' never false-matches 'email' or 'paid'."""
    pat = r"(?<!\w)" + re.escape(keyword.strip()) + r"(?!\w)"
    return bool(re.search(pat, text, re.IGNORECASE))


def lint_coherence(post_text: str, state_data: dict):
    keywords = [k for k in state_data.get("profile", {}).get("niche_keywords", []) if isinstance(k, str) and k.strip()]
    issues = []
    warnings = []

    if not post_text or not post_text.strip():
        issues.append("Input post is empty.")
    if not keywords:
        issues.append("No profile.niche_keywords configured in memory/state.json. Populate 3-5 core niche terms first.")
        return {
            "mode": "linkedin_360brew_coherence",
            "status": "FAIL",
            "matched_keywords": [],
            "missing_keywords": [],
            "plain_topic_in_opening": False,
            "issues": issues,
            "warnings": warnings,
        }

    opening_lines = " ".join([l.strip() for l in post_text.strip().splitlines() if l.strip()][:2])

    matched = [k for k in keywords if keyword_present(k, post_text)]
    missing = [k for k in keywords if not keyword_present(k, post_text)]
    plain_topic_opening = any(keyword_present(k, opening_lines) for k in keywords)

    if len(matched) == 0:
        issues.append("Zero profile niche_keywords appear in this post (high risk of 360Brew topic mismatch).")
    elif len(matched) == 1 and len(keywords) >= 3:
        warnings.append("Only 1 profile keyword matched; reinforce topic clarity if natural.")

    if not plain_topic_opening:
        issues.append("None of your core niche_keywords appear in lines 1-2 (fails Plain-Topic Hook Test).")

    return {
        "mode": "linkedin_360brew_coherence",
        "status": "PASS" if not issues else "FAIL",
        "matched_keywords": matched,
        "missing_keywords": missing,
        "plain_topic_in_opening": plain_topic_opening,
        "issues": issues,
        "warnings": warnings,
    }


def lint_google_rsa(data: dict):
    headlines = data.get("headlines", [])
    descriptions = data.get("descriptions", [])
    issues = []
    warnings = []

    if not headlines:
        issues.append("No headlines provided (supply 3 to 15 distinct headlines).")
    if not descriptions:
        issues.append("No descriptions provided (supply 2 to 4 distinct descriptions).")
    if len(headlines) > 15:
        issues.append(f"Too many headlines: {len(headlines)} (max 15).")
    if len(descriptions) > 4:
        issues.append(f"Too many descriptions: {len(descriptions)} (max 4).")

    seen_h = set()
    headline_report = []
    for idx, h in enumerate(headlines, 1):
        h_str = h.strip() if isinstance(h, str) else ""
        h_issues = []
        if not h_str:
            h_issues.append("empty headline")
            issues.append(f"Headline #{idx} is empty.")
        if len(h_str) > 30:
            h_issues.append(f"exceeds 30 chars ({len(h_str)}/30)")
            issues.append(f"Headline #{idx} exceeds 30 chars ({len(h_str)}/30): '{h_str}'")
        if re.search(r"\[[^\]]+\]", h_str):
            h_issues.append("unfilled placeholder bracket")
            issues.append(f"Headline #{idx} contains unfilled placeholder brackets: '{h_str}'")
        if h_str.lower() in seen_h and h_str:
            h_issues.append("duplicate headline")
            issues.append(f"Headline #{idx} duplicates an earlier headline: '{h_str}'")
        seen_h.add(h_str.lower())
        headline_report.append({"index": idx, "text": h_str, "chars": len(h_str), "limit": 30, "ok": not h_issues})

    seen_d = set()
    desc_report = []
    for idx, d in enumerate(descriptions, 1):
        d_str = d.strip() if isinstance(d, str) else ""
        d_issues = []
        if not d_str:
            d_issues.append("empty description")
            issues.append(f"Description #{idx} is empty.")
        if len(d_str) > 90:
            d_issues.append(f"exceeds 90 chars ({len(d_str)}/90)")
            issues.append(f"Description #{idx} exceeds 90 chars ({len(d_str)}/90): '{d_str}'")
        if re.search(r"\[[^\]]+\]", d_str):
            d_issues.append("unfilled placeholder bracket")
            issues.append(f"Description #{idx} contains unfilled placeholder brackets: '{d_str}'")
        if d_str.lower() in seen_d and d_str:
            d_issues.append("duplicate description")
            issues.append(f"Description #{idx} duplicates an earlier description.")
        seen_d.add(d_str.lower())
        desc_report.append({"index": idx, "text": d_str, "chars": len(d_str), "limit": 90, "ok": not d_issues})

    return {
        "mode": "google_rsa",
        "status": "PASS" if not issues else "FAIL",
        "headlines": headline_report,
        "descriptions": desc_report,
        "issues": issues,
        "warnings": warnings,
    }


def score_rubric(data: dict):
    platform = str(data.get("platform", "google")).lower()
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
        return {
            "mode": "rubric",
            "status": "FAIL",
            "launch_ready": False,
            "issues": ["Platform must be 'google' or 'meta'."],
        }

    issues = []
    total = 0.0
    breakdown = {}
    for crit, w in weights[platform].items():
        if crit not in ratings:
            issues.append(f"Missing required rubric criterion: '{crit}'.")
            breakdown[crit] = {"rating": None, "weight": w, "points": 0.0}
            continue
        r = ratings[crit]
        if isinstance(r, bool) or not isinstance(r, (int, float)) or r < 1 or r > 5:
            issues.append(f"Invalid rating for '{crit}': {r!r} (must be a number from 1 to 5).")
            breakdown[crit] = {"rating": r, "weight": w, "points": 0.0}
            continue
        pts = round(r * w / 5.0, 2)
        breakdown[crit] = {"rating": r, "weight": w, "points": pts}
        total += pts

    if issues:
        return {
            "mode": f"{platform}_rubric",
            "status": "FAIL",
            "total_score": None,
            "band": "Invalid Input",
            "launch_ready": False,
            "issues": issues,
            "breakdown": breakdown,
        }

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
        "status": "PASS",
        "total_score": total,
        "band": band,
        "launch_ready": total >= 75,
        "issues": [],
        "breakdown": breakdown,
    }


def lint_state(data: dict):
    """v1.3a state.json schema & 2027 operational readiness validator."""
    issues = []
    warnings = []

    required_top = [
        "schema_version", "profile", "progress", "deliverability",
        "positioning", "evidence_ledger", "verify_flags", "linkedin_2027",
        "warm_signal_pipeline", "module_5_closes", "metrics", "idea_bank"
    ]
    for key in required_top:
        if key not in data:
            issues.append(f"Missing top-level key in state.json: '{key}'.")

    deliv = data.get("deliverability", {})
    if isinstance(deliv, dict):
        if deliv.get("bounce_rate_pct", 0) >= 2.0:
            issues.append(f"Hard bounce rate is {deliv['bounce_rate_pct']}% (must stay <2.0%).")
        if deliv.get("spam_complaint_pct", 0) >= 0.3:
            issues.append(f"Spam complaint rate is {deliv['spam_complaint_pct']}% (hard ceiling <0.3%; safe target <0.1%).")
        elif deliv.get("spam_complaint_pct", 0) >= 0.1:
            warnings.append(f"Spam complaint rate is {deliv['spam_complaint_pct']}% (approaching 0.3% ceiling; safe target <0.1%).")
        if deliv.get("daily_cap_per_inbox", 0) > 40:
            warnings.append(f"Daily inbox cap is {deliv['daily_cap_per_inbox']} (recommended safe range: 20-40/inbox/day).")

    li = data.get("linkedin_2027", {})
    if isinstance(li, dict):
        recent_dms = li.get("recent_dm_contacts", [])
        if len(recent_dms) != len(set(x.lower() for x in recent_dms if isinstance(x, str))):
            warnings.append("Duplicate names inside recent_dm_contacts (enforce 3-post Anti-Pod DM cooldown).")
        if li.get("ai_slop_notices_count", 0) > 0:
            warnings.append(f"{li['ai_slop_notices_count']} AI-slop analytics notice(s) logged; audit POV Swap-Test before next post.")

    if data.get("verify_flags"):
        warnings.append(f"{len(data['verify_flags'])} open VERIFY flag(s) must be cleared before publishing.")

    return {
        "mode": "state_validation",
        "status": "PASS" if not issues else "FAIL",
        "schema_version": data.get("schema_version"),
        "issues": issues,
        "warnings": warnings,
    }


def main():
    if hasattr(sys.stdin, 'reconfigure'):
        sys.stdin.reconfigure(encoding='utf-8', errors='replace')
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    parser = argparse.ArgumentParser(description="Brandevegen v1.3a Hardened Deterministic Linter")
    parser.add_argument(
        "command",
        choices=["email", "ai-summary", "linkedin", "carousel", "coherence", "google-rsa", "rubric", "state"],
    )
    parser.add_argument("file", help="Path to text/JSON file to audit (or '-' for stdin)")
    parser.add_argument("state_file", nargs="?", help="Path to memory/state.json (required for 'coherence')")
    args = parser.parse_args()

    try:
        raw = read_input(args.file)
    except Exception as exc:
        print(json.dumps({"status": "FAIL", "issues": [f"Failed to read input: {exc}"]}, indent=2))
        sys.exit(2)

    try:
        if args.command == "email":
            result = lint_email(raw)
        elif args.command == "ai-summary":
            result = lint_ai_summary(raw)
        elif args.command == "linkedin":
            result = lint_linkedin(raw)
        elif args.command == "carousel":
            result = lint_carousel(json.loads(raw))
        elif args.command == "coherence":
            if not args.state_file:
                print(json.dumps({"status": "FAIL", "issues": ["'coherence' requires memory/state.json as 2nd argument."]}, indent=2))
                sys.exit(2)
            state_data = json.loads(Path(args.state_file).read_text(encoding="utf-8"))
            result = lint_coherence(raw, state_data)
        elif args.command == "google-rsa":
            result = lint_google_rsa(json.loads(raw))
        elif args.command == "rubric":
            result = score_rubric(json.loads(raw))
        else:
            result = lint_state(json.loads(raw))
    except json.JSONDecodeError as exc:
        print(json.dumps({"status": "FAIL", "issues": [f"Invalid JSON input: {exc}"]}, indent=2))
        sys.exit(2)

    print(json.dumps(result, indent=2))
    ok = result.get("status") == "PASS" and result.get("launch_ready", True)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
