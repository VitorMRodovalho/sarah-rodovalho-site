#!/usr/bin/env python3
"""
sync_engagements.py — Phase 1b Orenu → sarahrodovalho.com /speaking sync.

Per ADR-024 Phase 1b. Mirrors the architecture of sync_publications.py
(Phase 1a) with two table-specific differences:

  - Source table: public.fact_speaker_engagement (12 rows currently;
    4 public as of mig 0092).
  - Matching: Orenu event_name doesn't always substring-match the MDX
    `event` field (Orenu often has a short canonical name; MDX has the
    full hosting-org name). Sync uses a token-overlap heuristic with a
    small Portuguese/English stoplist + a year/date tiebreaker.
  - Authority scope: Phase 1b is PRESENCE-AWARE only. No fields are
    overwritten — Orenu's engagement schema (event_name, event_date,
    role enum, audience_size_estimate) doesn't capture the talk-level
    fields that matter on /speaking (title, abstract, audience copy).
    Field authority migrates as Orenu deepens.

Run modes:
  python scripts/sync_engagements.py                # dry-run
  python scripts/sync_engagements.py --apply        # no-op in Phase 1b
                                                    # (no field writes)
                                                    # — flag retained for
                                                    # symmetry + future use

Environment:
  ORENU_DATABASE_URL — read-only Postgres URL (CI secret).

Exit codes:
  0 — perfect match (every public Orenu row paired to an MDX, no orphans)
  1 — warnings: unmatched Orenu (stub needed) or orphan MDX (review)
  2 — fatal error

Shared helpers (parse_frontmatter, write_mdx, _normalize) are imported
from sync_publications to avoid duplication; if either script gets a
breaking change, the other's tests will catch the regression.
"""

from __future__ import annotations

import argparse
import os
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import psycopg2

from sync_publications import (  # type: ignore[import]
    HOUSEHOLD_ID,
    parse_frontmatter,
)

DEFAULT_CONTENT_DIR = Path("src/content/engagements")

# Function-word stoplist only — articles, prepositions, conjunctions.
# Event-type words like "summit"/"conference"/"panel" are NOT stripped
# because they're often the only token-overlap between a short Orenu
# name (e.g., "ConstruTech Summit 2024") and a longer MDX event field
# (e.g., "ConstruTech Summit — StartSe University").
_STOPWORDS: set[str] = {
    # English function words
    "the", "of", "in", "on", "at", "to", "for", "with", "and", "a", "an",
    "&", "from", "by", "is",
    # Portuguese function words
    "de", "da", "do", "das", "dos", "em", "na", "no", "nas", "nos",
    "para", "com", "por", "e",
}

# Heuristic threshold: >=2 shared significant tokens = match candidate.
_MIN_TOKEN_OVERLAP = 2


@dataclass
class OrenuEngagement:
    engagement_id: str
    event_name: str
    event_date: str | None
    event_location: str | None
    role: str
    international_scope: bool


@dataclass
class MdxEngagement:
    path: Path
    frontmatter: dict[str, Any]
    body: str


def _strip_diacritics(s: str) -> str:
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def tokenize(s: str) -> set[str]:
    """Tokenize for match-overlap. Diacritics stripped, lowercase, alphanumeric only."""
    if not s:
        return set()
    cleaned = _strip_diacritics(s).lower()
    tokens = {
        tok
        for tok in (
            "".join(c if c.isalnum() else " " for c in cleaned).split()
        )
        if tok and tok not in _STOPWORDS and len(tok) > 1
    }
    return tokens


def fetch_public_engagements(conn) -> list[OrenuEngagement]:
    sql = """
        SELECT
          engagement_id::text,
          event_name,
          event_date::text,
          event_location,
          role::text,
          international_scope
        FROM public.fact_speaker_engagement
        WHERE household_id = %s
          AND public_visibility = true
        ORDER BY event_date DESC NULLS LAST
    """
    with conn.cursor() as cur:
        cur.execute(sql, (HOUSEHOLD_ID,))
        rows = cur.fetchall()
    return [
        OrenuEngagement(
            engagement_id=r[0],
            event_name=r[1],
            event_date=r[2],
            event_location=r[3],
            role=r[4],
            international_scope=bool(r[5]),
        )
        for r in rows
    ]


def read_mdx_files(content_dir: Path) -> list[MdxEngagement]:
    out: list[MdxEngagement] = []
    for path in sorted(content_dir.glob("*.mdx")):
        text = path.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        out.append(MdxEngagement(path=path, frontmatter=fm, body=body))
    return out


def score_pair(orenu: OrenuEngagement, mdx: MdxEngagement) -> int:
    """Return a match score; ≥_MIN_TOKEN_OVERLAP qualifies as a match."""
    orenu_tokens = tokenize(orenu.event_name)
    fm = mdx.frontmatter
    mdx_tokens = tokenize(
        " ".join(
            [
                str(fm.get("event", "")),
                str(fm.get("title", "")),
                str(fm.get("venue", "")),
            ]
        )
    )
    overlap = len(orenu_tokens & mdx_tokens)

    # Bonus for exact-date alignment (strong disambiguator).
    if orenu.event_date and fm.get("date") == orenu.event_date:
        overlap += 2

    return overlap


def match_engagement_pairs(
    orenu_engs: list[OrenuEngagement],
    mdx_engs: list[MdxEngagement],
) -> tuple[
    list[tuple[OrenuEngagement, MdxEngagement]],
    list[OrenuEngagement],
    list[MdxEngagement],
]:
    """Greedy max-overlap match: for each Orenu row pick the highest-scoring MDX."""
    matched: list[tuple[OrenuEngagement, MdxEngagement]] = []
    used_paths: set[Path] = set()

    # Sort Orenu rows by date descending so the most recent gets first crack;
    # avoids a 2024 event accidentally claiming a 2026 MDX file.
    ordered = sorted(orenu_engs, key=lambda e: e.event_date or "", reverse=True)

    for orenu in ordered:
        best: tuple[int, MdxEngagement] | None = None
        for mdx in mdx_engs:
            if mdx.path in used_paths:
                continue
            score = score_pair(orenu, mdx)
            if score < _MIN_TOKEN_OVERLAP:
                continue
            if best is None or score > best[0]:
                best = (score, mdx)
        if best is not None:
            matched.append((orenu, best[1]))
            used_paths.add(best[1].path)

    matched_ids = {pair[0].engagement_id for pair in matched}
    unmatched_orenu = [op for op in orenu_engs if op.engagement_id not in matched_ids]
    unmatched_mdx = [m for m in mdx_engs if m.path not in used_paths]
    return matched, unmatched_orenu, unmatched_mdx


def compute_drift_warnings(orenu: OrenuEngagement, mdx: MdxEngagement) -> list[str]:
    """Phase 1b: warn on date misalignment (>30 days) only. No field overwrite."""
    warnings: list[str] = []
    fm = mdx.frontmatter

    orenu_date = orenu.event_date or ""
    mdx_date = str(fm.get("date") or "")
    if orenu_date and mdx_date and orenu_date != mdx_date:
        try:
            from datetime import date

            od = date.fromisoformat(orenu_date)
            md = date.fromisoformat(mdx_date)
            gap_days = abs((md - od).days)
            if gap_days > 30:
                warnings.append(
                    f"    date:   Orenu={orenu_date}\n"
                    f"            MDX  ={mdx_date}  (gap {gap_days} days)"
                )
        except ValueError:
            pass

    return warnings


def run(
    content_dir: Path,
    apply: bool,
    conn=None,
    *,
    orenu_override: list[OrenuEngagement] | None = None,
) -> int:
    mode_label = "APPLY" if apply else "DRY-RUN"
    print(f"sync_engagements.py [{mode_label}]")
    print(f"  content_dir = {content_dir}")

    if orenu_override is not None:
        orenu_engs = orenu_override
    else:
        assert conn is not None
        orenu_engs = fetch_public_engagements(conn)

    mdx_engs = read_mdx_files(content_dir)

    print(f"  Orenu public rows: {len(orenu_engs)}")
    print(f"  MDX files:         {len(mdx_engs)}")

    matched, unmatched_orenu, unmatched_mdx = match_engagement_pairs(orenu_engs, mdx_engs)
    print(f"  Matched pairs:     {len(matched)}")
    print(f"  Unmatched Orenu:   {len(unmatched_orenu)}")
    print(f"  Unmatched MDX:     {len(unmatched_mdx)}")

    exit_code = 0
    drift_warnings_total = 0

    for orenu, mdx in matched:
        drifts = compute_drift_warnings(orenu, mdx)
        if drifts:
            drift_warnings_total += len(drifts)
            print(f"\n  DRIFT [{mdx.path.name}]:")
            for d in drifts:
                print(d)

    for op in unmatched_orenu:
        print(f"\n  STUB NEEDED — Orenu engagement_id={op.engagement_id}")
        print(f"    event_name = {op.event_name!r}")
        print(f"    event_date = {op.event_date}")
        print(f"    No matching MDX file in {content_dir}.")
        print(f"    Action: create an MDX file with the canonical Orenu event_name + frontmatter.")
        exit_code = 1

    for mp in unmatched_mdx:
        print(f"\n  ORPHAN MDX — {mp.path.name}")
        print(f"    title = {mp.frontmatter.get('title')!r}")
        print(f"    event = {mp.frontmatter.get('event')!r}")
        print(f"    No matching public Orenu row.")
        print(f"    Action: flip the Orenu row's public_visibility = true, or move this MDX to _archive/.")
        exit_code = 1

    print(f"\nSummary:")
    print(f"  Drift warnings (date misalignment > 30 days): {drift_warnings_total}")
    print(f"  Stubs needed:  {len(unmatched_orenu)}")
    print(f"  Orphan MDX:    {len(unmatched_mdx)}")
    print(f"  Note: Phase 1b is presence-aware ONLY — no fields auto-overwritten.")

    if drift_warnings_total > 0:
        exit_code = 1

    return exit_code


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 1b Orenu → site engagement sync")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="No-op in Phase 1b (retained for symmetry; nothing is written)",
    )
    parser.add_argument(
        "--content-dir",
        default=str(DEFAULT_CONTENT_DIR),
        help="Path to the engagements content collection",
    )
    args = parser.parse_args()

    content_dir = Path(args.content_dir)
    if not content_dir.is_dir():
        print(f"ERROR: content dir not found: {content_dir}", file=sys.stderr)
        sys.exit(2)

    db_url = os.environ.get("ORENU_DATABASE_URL")
    if not db_url:
        print("ERROR: ORENU_DATABASE_URL environment variable not set", file=sys.stderr)
        sys.exit(2)

    try:
        conn = psycopg2.connect(db_url, application_name="sync-engagements")
    except Exception as e:
        print(f"ERROR: cannot connect to Orenu Postgres: {e}", file=sys.stderr)
        sys.exit(2)

    try:
        exit_code = run(content_dir, args.apply, conn=conn)
    finally:
        conn.close()

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
