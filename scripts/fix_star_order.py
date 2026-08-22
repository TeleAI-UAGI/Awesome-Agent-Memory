#!/usr/bin/env python3
"""Re-sort the Open-Source products section of README.md by GitHub star count.

The companion fixer for check_star_order.py: where that script reports the
inversions, this one applies them. Entries are sorted within the main list and
within the collapsed "Emerging projects" block separately, then renumbered
continuously across both. Ties keep their current relative order, so a re-sort
only moves what the star counts actually require.

Section membership is never changed. An entry on the wrong side of the
100-star boundary is reported and left alone: graduating a project into the
main list is an editorial decision, and the grace band in check_star_order.py
exists so entries hovering around the threshold don't bounce every week.

Before writing, the rewritten README is checked line-for-line against the
original — same lines, same count, differing only in entry numbers — so a
parsing slip can't silently drop or duplicate an entry.

Usage: GITHUB_TOKEN=... python3 scripts/fix_star_order.py [README.md] [--write]

Without --write it reports the moves it would make and leaves the file alone.
"""

import io
import json
import os
import re
import sys
import urllib.request

BADGE_RE = re.compile(r"img\.shields\.io/github/stars/([\w.-]+/[\w.-]+)\.svg")
ENTRY_RE = re.compile(r"^(\d+)\.\s+(.*)$")
NAME_RE = re.compile(r"^\d+\.\s+\*{0,2}\[([^\]]+)\]")
SECTION_START = "### Open-Source"
SECTION_END = "### Closed-Source"
EMERGING_MARKER = "Emerging projects"
THRESHOLD = 100
GRACE = 10  # mirrors check_star_order.py


def split_blocks(lines, start, end):
    """Group the section into ("entry", lines) and ("raw", lines) blocks.

    An entry is a numbered line carrying a star badge (on the same line or the
    next one) plus the indented lines that follow it. Everything else — blank
    lines, the <details> wrapper, the italic section notes — stays raw and is
    left exactly where it is.
    """
    blocks = []
    current = None
    emerging_at = None
    for i in range(start, end):
        line = lines[i]
        nxt = lines[i + 1] if i + 1 < end else ""
        if "<summary>" in line and EMERGING_MARKER in line:
            emerging_at = len(blocks)
        if ENTRY_RE.match(line) and (BADGE_RE.search(line) or BADGE_RE.search(nxt)):
            current = [line]
            blocks.append(["entry", current])
            continue
        if current is not None and (line.startswith(" ") or not line.strip()):
            # A blank line continues the entry only if an indented line follows.
            if not line.strip() and not (nxt.startswith(" ") and not ENTRY_RE.match(nxt)):
                current = None
                blocks.append(["raw", [line]])
                continue
            current.append(line)
            continue
        current = None
        blocks.append(["raw", [line]])
    return blocks, emerging_at


def fetch_stars(repo, token):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{repo}",
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {token}",
            "User-Agent": "awesome-agent-memory-star-fix",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)["stargazers_count"]


def renumbered(lines):
    """The lines with entry numbers stripped, for the content-preservation check."""
    return sorted(ENTRY_RE.sub(r"\2", line) for line in lines)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv[1:]
    readme = args[0] if args else "README.md"

    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        sys.exit("GITHUB_TOKEN is required (rate limits)")

    original = io.open(readme, encoding="utf-8", newline="").read()
    if "\r" in original:
        sys.exit(f"{readme} has CRLF line endings; convert to LF first")
    lines = original.split("\n")

    try:
        start = next(i for i, l in enumerate(lines) if SECTION_START in l)
        end = next(i for i, l in enumerate(lines) if SECTION_END in l)
    except StopIteration:
        sys.exit("Could not locate the Open-Source section — README format may have changed")

    blocks, emerging_at = split_blocks(lines, start, end)
    slots = [i for i, (kind, _) in enumerate(blocks) if kind == "entry"]
    if not slots:
        sys.exit("No open-source entries parsed — README format may have changed")

    meta = {}
    for i in slots:
        body = "\n".join(blocks[i][1])
        repo = BADGE_RE.search(body).group(1)
        name_match = NAME_RE.match(blocks[i][1][0])
        stars = fetch_stars(repo, token)  # a failure here aborts: a missing
        meta[i] = {                       # count would sort the entry to the bottom
            "repo": repo,
            "name": name_match.group(1) if name_match else repo,
            "stars": stars,
            "position": int(ENTRY_RE.match(blocks[i][1][0]).group(1)),
            "emerging": emerging_at is not None and i > emerging_at,
        }

    main_slots = [i for i in slots if not meta[i]["emerging"]]
    emerging_slots = [i for i in slots if meta[i]["emerging"]]
    # Stable sort: entries on equal stars keep the order they already have.
    rewritten = list(blocks)
    for group in (main_slots, emerging_slots):
        for slot, source in zip(group, sorted(group, key=lambda i: -meta[i]["stars"])):
            rewritten[slot] = blocks[source]

    moves = []
    for number, slot in enumerate(main_slots + emerging_slots, start=1):
        body = list(rewritten[slot][1])
        entry = ENTRY_RE.match(body[0])
        was = int(entry.group(1))
        if was != number:
            name = NAME_RE.match(body[0])
            moves.append((name.group(1) if name else body[0], was, number))
        body[0] = f"{number}. {entry.group(2)}"
        rewritten[slot] = ["entry", body]

    crossings = [
        m for m in meta.values()
        if (not m["emerging"] and m["stars"] < THRESHOLD - GRACE)
        or (m["emerging"] and m["stars"] >= THRESHOLD + GRACE)
    ]

    print(f"{len(slots)} entries ({len(main_slots)} main, {len(emerging_slots)} emerging)")
    if moves:
        print(f"\n{len(moves)} entries move:")
        for name, was, now in sorted(moves, key=lambda m: m[2]):
            print(f"  {name:<40} #{was:>2} -> #{now}")
    else:
        print("\nAlready sorted — nothing to move.")
    if crossings:
        print(f"\nWrong side of the {THRESHOLD}-star boundary (±{GRACE} grace), left in place:")
        for m in crossings:
            side = "move down into Emerging projects" if not m["emerging"] else "graduate into the main list"
            print(f"  #{m['position']} {m['name']} ({m['stars']} stars) should {side}")

    out = lines[:start] + [l for _, body in rewritten for l in body] + lines[end:]
    if renumbered(out) != renumbered(lines) or len(out) != len(lines):
        sys.exit("ABORT: rewrite would change content, not just ordering — README not written")

    if not moves:
        return
    if not write:
        print("\n(dry run — pass --write to apply)")
        return
    io.open(readme, "w", encoding="utf-8", newline="").write("\n".join(out))
    print(f"\nWrote {readme}. Re-run scripts/check_star_order.py to confirm.")


if __name__ == "__main__":
    main()
