#!/usr/bin/env python3
"""Check that the Open-Source products section of README.md is ordered by GitHub stars.

Parses the numbered entries (each carries a shields.io star badge identifying its
owner/repo), fetches live star counts from the GitHub API, and reports any entry
that is out of descending order. Exits non-zero if a re-sort is needed, so the
scheduled workflow notifies maintainers.

Also checks the 100-star boundary of the collapsed "Emerging projects" details
block: entries in the main list should have >= 100 stars and emerging entries
< 100. A grace band (main >= 90 passes, emerging < 110 passes) stops projects
hovering around 100 from flip-flopping between sections every week.

Usage: GITHUB_TOKEN=... python3 scripts/check_star_order.py [README.md]

To apply the ordering this script suggests, run its companion fixer:
GITHUB_TOKEN=... python3 scripts/fix_star_order.py README.md --write
"""

import json
import os
import re
import sys
import urllib.request

BADGE_RE = re.compile(r"img\.shields\.io/github/stars/([\w.-]+/[\w.-]+)\.svg")
ENTRY_RE = re.compile(r"^(\d+)\.\s+\*\*\[([^\]]+)\]")
SECTION_START = "### Open-Source"
SECTION_END = "### Closed-Source"
EMERGING_MARKER = "Emerging projects"
THRESHOLD = 100
GRACE = 10  # main entries pass at >= THRESHOLD - GRACE, emerging at < THRESHOLD + GRACE


def parse_entries(readme_path):
    """Return [(position, name, owner/repo, emerging)] for numbered open-source entries."""
    with open(readme_path, encoding="utf-8") as f:
        lines = f.readlines()

    entries = []
    in_section = False
    emerging = False
    current = None  # (position, name) awaiting its badge
    for line in lines:
        if SECTION_START in line:
            in_section = True
            continue
        if SECTION_END in line:
            break
        if not in_section:
            continue
        if "<summary>" in line and EMERGING_MARKER in line:
            emerging = True
        m = ENTRY_RE.match(line)
        if m:
            current = (int(m.group(1)), m.group(2))
        b = BADGE_RE.search(line)
        if b and current:
            entries.append((current[0], current[1], b.group(1), emerging))
            current = None
    return entries


def fetch_stars(repo, token):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "awesome-agent-memory-star-check",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)["stargazers_count"]
    except Exception as e:  # 404 (renamed/deleted repo), rate limit, network
        print(f"WARN: could not fetch {repo}: {e}", file=sys.stderr)
        return None


def main():
    readme = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        sys.exit("GITHUB_TOKEN is required (rate limits)")

    entries = parse_entries(readme)
    if not entries:
        sys.exit("No open-source entries parsed — README format may have changed")

    starred = []
    for pos, name, repo, emerging in entries:
        stars = fetch_stars(repo, token)
        if stars is not None:
            starred.append((pos, name, repo, stars, emerging))

    print(f"{'#':>3}  {'stars':>7}  name")
    for pos, name, repo, stars, emerging in starred:
        tag = "  [emerging]" if emerging else ""
        print(f"{pos:>3}  {stars:>7}  {name} ({repo}){tag}")

    failed = False

    inversions = [
        (a, b)
        for a, b in zip(starred, starred[1:])
        if a[3] < b[3]
    ]
    if inversions:
        failed = True
        print("\nOut of order (lower-ranked entry has more stars):")
        for a, b in inversions:
            print(f"  #{b[0]} {b[1]} ({b[3]} stars) should rank above #{a[0]} {a[1]} ({a[3]} stars)")
        print("\nSuggested order:")
        for i, (_, name, repo, stars, _e) in enumerate(
            sorted(starred, key=lambda e: -e[3]), start=1
        ):
            print(f"{i:>3}. {name} ({repo}, {stars} stars)")

    crossings = [
        e for e in starred
        if (not e[4] and e[3] < THRESHOLD - GRACE)
        or (e[4] and e[3] >= THRESHOLD + GRACE)
    ]
    if crossings:
        failed = True
        print(f"\nWrong side of the {THRESHOLD}-star boundary (±{GRACE} grace):")
        for pos, name, repo, stars, emerging in crossings:
            direction = "move down into Emerging projects" if not emerging else "graduate into the main list"
            print(f"  #{pos} {name} ({stars} stars) should {direction}")

    if failed:
        sys.exit(1)

    print("\nOK: list is ordered by star count and the emerging boundary holds.")


if __name__ == "__main__":
    main()
