"""
Tests for scripts/sync_engagements.py — Phase 1b sync (ADR-024).

Coverage:
- tokenize() strips diacritics, stoplist words, single chars
- score_pair() respects token overlap + date-bonus
- match_engagement_pairs() resolves the 4 known Sarah pairs correctly
  (ARCC / PMI Women / ConstruTech / IA na Construção)
- date drift warning >30 days
- end-to-end run() with stub + orphan reports
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from sync_engagements import (  # noqa: E402
    MdxEngagement,
    OrenuEngagement,
    compute_drift_warnings,
    match_engagement_pairs,
    score_pair,
    tokenize,
    run,
)


# ─── Helpers ────────────────────────────────────────────────


def make_orenu(name: str, date: str | None = None, role: str = "panelist") -> OrenuEngagement:
    return OrenuEngagement(
        engagement_id=f"oid-{hash(name) & 0xffff:04x}",
        event_name=name,
        event_date=date,
        event_location=None,
        role=role,
        international_scope=False,
    )


def make_mdx(event: str, date: str = "", title: str = "Talk") -> MdxEngagement:
    return MdxEngagement(
        path=Path(event.split()[0].lower() + ".mdx"),
        frontmatter={"event": event, "date": date, "title": title},
        body="",
    )


# ─── tokenize() ─────────────────────────────────────────────


def test_tokenize_strips_diacritics():
    """'Construção' → 'construcao' (NFKD strip)."""
    assert "construcao" in tokenize("IA na Construção")


def test_tokenize_strips_stopwords():
    """'24 Hours of Women in Construction' drops 'of'/'in' (function words)."""
    tokens = tokenize("24 Hours of Women in Construction")
    assert "of" not in tokens
    assert "in" not in tokens
    # Event-type and content nouns retained — they're often the only
    # token overlap with the MDX event field.
    assert "24" in tokens
    assert "women" in tokens
    assert "construction" in tokens
    assert "hours" in tokens


def test_tokenize_drops_single_chars():
    tokens = tokenize("A B C 24")
    assert tokens == {"24"}


# ─── score_pair() ───────────────────────────────────────────


def test_score_pair_token_overlap():
    orenu = make_orenu("ConstruTech Summit 2024")
    mdx = make_mdx("ConstruTech Summit — StartSe University")
    # Shared: {construtech} — 'summit' is in stoplist.
    assert score_pair(orenu, mdx) >= 1


def test_score_pair_date_bonus():
    """Exact date match adds +2 to overlap score."""
    orenu = make_orenu("ARCC 2025 panel — Healthcare Net-Zero", date="2025-03-11")
    mdx = make_mdx("ARCC 2025 International Conference", date="2025-03-11")
    score_with_date = score_pair(orenu, mdx)
    mdx_no_date = make_mdx("ARCC 2025 International Conference", date="2099-12-31")
    score_no_date = score_pair(orenu, mdx_no_date)
    assert score_with_date - score_no_date == 2


# ─── match_engagement_pairs() ───────────────────────────────


def test_match_sarah_speaking_4_pairs():
    """The 4 real Sarah pairs all match correctly."""
    orenu_rows = [
        make_orenu("ARCC 2025 panel — Healthcare Net-Zero", date="2025-03-11"),
        make_orenu("PMI Women in Construction — Follow-the-Sun Keynote", date="2026-03-12"),
        make_orenu("ConstruTech Summit 2024", date="2024-01-01"),
        make_orenu("IA na Construção — Autodesk Forma", date="2026-03-27"),
    ]
    mdx_files = [
        MdxEngagement(
            path=Path("arcc-2025-wellbeing-net-zero-healthcare.mdx"),
            frontmatter={
                "event": "ARCC 2025 International Conference — Architectural Research Centers Consortium",
                "date": "2025-04-02",
                "title": "Integrating Comprehensive Wellbeing and Net-Zero Energy in Healthcare Design",
            },
            body="",
        ),
        MdxEngagement(
            path=Path("pmi-women-construction-follow-the-sun-2026.mdx"),
            frontmatter={
                "event": "24 Hours of Women in Construction Leadership · PMI Gigaproject & Construction Conferences",
                "date": "2026-03-12",
                "title": "From Architecture to Data Centers",
            },
            body="",
        ),
        MdxEngagement(
            path=Path("startse-construtech-summit-2024.mdx"),
            frontmatter={
                "event": "ConstruTech Summit — StartSe University",
                "date": "2024-02-27",
                "title": "My Professional Journey from Brazilian Architect to Tesla",
            },
            body="",
        ),
        MdxEngagement(
            path=Path("ia-na-construcao-autodesk-forma-2026.mdx"),
            frontmatter={
                "event": "IA na Construção — Community Class / Live Session",
                "date": "2026-03-27",
                "title": "AI in Construction · Autodesk Forma",
            },
            body="",
        ),
    ]
    matched, unmatched_orenu, unmatched_mdx = match_engagement_pairs(orenu_rows, mdx_files)
    assert len(matched) == 4
    assert not unmatched_orenu
    assert not unmatched_mdx

    # Verify each pair (by event_name → MDX path).
    pairs_by_orenu = {pair[0].event_name: pair[1].path.name for pair in matched}
    assert pairs_by_orenu["ARCC 2025 panel — Healthcare Net-Zero"] == "arcc-2025-wellbeing-net-zero-healthcare.mdx"
    assert pairs_by_orenu["PMI Women in Construction — Follow-the-Sun Keynote"] == "pmi-women-construction-follow-the-sun-2026.mdx"
    assert pairs_by_orenu["ConstruTech Summit 2024"] == "startse-construtech-summit-2024.mdx"
    assert pairs_by_orenu["IA na Construção — Autodesk Forma"] == "ia-na-construcao-autodesk-forma-2026.mdx"


def test_match_stub_when_no_mdx():
    orenu_rows = [make_orenu("Brand New Conference 2030")]
    matched, unmatched_orenu, _ = match_engagement_pairs(orenu_rows, [])
    assert not matched
    assert len(unmatched_orenu) == 1


def test_match_orphan_when_no_orenu():
    mdx_files = [make_mdx("Stale Conference 1999")]
    matched, _, unmatched_mdx = match_engagement_pairs([], mdx_files)
    assert not matched
    assert len(unmatched_mdx) == 1


# ─── compute_drift_warnings() ───────────────────────────────


def test_drift_date_within_30_days_no_warning():
    """30-day gap is within tolerance (conference-week pattern)."""
    orenu = make_orenu("ARCC 2025", date="2025-03-11")
    mdx = MdxEngagement(
        path=Path("a"),
        frontmatter={"date": "2025-04-02"},  # 22 days off
        body="",
    )
    warnings = compute_drift_warnings(orenu, mdx)
    assert not warnings


def test_drift_date_more_than_30_days_warns():
    orenu = make_orenu("Foo", date="2024-01-01")
    mdx = MdxEngagement(
        path=Path("a"),
        frontmatter={"date": "2024-02-27"},  # 57 days
        body="",
    )
    warnings = compute_drift_warnings(orenu, mdx)
    assert any("date:" in w for w in warnings)


# ─── End-to-end run() ───────────────────────────────────────


def test_run_clean_state_exit_0(tmp_path, capsys):
    content_dir = tmp_path / "engagements"
    content_dir.mkdir()
    (content_dir / "pmi.mdx").write_text(
        "---\n"
        "title: From Architecture to Data Centers\n"
        "event: 24 Hours of Women in Construction Leadership · PMI Gigaproject\n"
        "date: '2026-03-12'\n"
        "kind: talk\n"
        "abstract: foo\n"
        "---\n",
        encoding="utf-8",
    )
    orenu_rows = [
        make_orenu("PMI Women in Construction — Follow-the-Sun Keynote", date="2026-03-12"),
    ]
    exit_code = run(content_dir, apply=False, orenu_override=orenu_rows)
    out = capsys.readouterr().out
    assert exit_code == 0, out
    assert "Matched pairs:     1" in out
    assert "Stubs needed:  0" in out
    assert "Orphan MDX:    0" in out


def test_run_stub_needed_exit_1(tmp_path, capsys):
    content_dir = tmp_path / "engagements"
    content_dir.mkdir()
    orenu_rows = [make_orenu("Some New Conference 2030", date="2030-01-01")]
    exit_code = run(content_dir, apply=False, orenu_override=orenu_rows)
    out = capsys.readouterr().out
    assert exit_code == 1
    assert "STUB NEEDED" in out
