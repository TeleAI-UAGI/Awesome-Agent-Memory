#!/usr/bin/env python3
"""Generate the self-hosted star-history chart embedded in README.md.

Fetches stargazer timestamps from the GitHub API (requires a token with read
access to the repo — since June 2026 GitHub restricts stargazer timestamps to a
repository's own admins and collaborators; the Actions GITHUB_TOKEN qualifies),
builds the cumulative star count over time, and renders two static SVGs:

    assets/star-history-light.svg
    assets/star-history-dark.svg

The README embeds them via a <picture> element so GitHub serves the right one
for the viewer's color scheme.

Usage: GITHUB_TOKEN=... python3 scripts/gen_star_history.py [owner/repo]
"""

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date, datetime, timezone

DEFAULT_REPO = "TeleAI-UAGI/Awesome-Agent-Memory"
OUT = {
    "light": "assets/star-history-light.svg",
    "dark": "assets/star-history-dark.svg",
}

# Chart chrome per color scheme, chosen for GitHub's README surfaces
# (light #ffffff, dark #0d1117); background stays transparent.
THEME = {
    "light": {
        "series": "#2a78d6",
        "ink": "#0b0b0b",
        "muted": "#898781",
        "grid": "#e1e0d9",
        "axis": "#c3c2b7",
    },
    "dark": {
        "series": "#3987e5",
        "ink": "#ffffff",
        "muted": "#898781",
        "grid": "#2c2c2a",
        "axis": "#383835",
    },
}

W, H = 720, 360
ML, MR, MT, MB = 52, 84, 28, 40  # margins: left, right, top, bottom


def fetch_star_dates(repo, token):
    """Return sorted list of starred_at dates (date objects)."""
    dates = []
    page = 1
    while True:
        req = urllib.request.Request(
            f"https://api.github.com/repos/{repo}/stargazers?per_page=100&page={page}",
            headers={
                "Accept": "application/vnd.github.star+json",
                "Authorization": f"Bearer {token}",
                "User-Agent": "awesome-agent-memory-star-history",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                batch = json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code in (401, 403, 404, 422):
                sys.exit(
                    f"GitHub API {e.code} for {repo} stargazers: the token must "
                    "belong to a repo admin/collaborator (GitHub restricted "
                    "stargazer timestamps in June 2026)."
                )
            raise
        if not batch:
            break
        for item in batch:
            dates.append(
                datetime.strptime(item["starred_at"], "%Y-%m-%dT%H:%M:%SZ").date()
            )
        if len(batch) < 100:
            break
        page += 1
    dates.sort()
    return dates


def cumulative_by_day(dates):
    """Collapse star dates to [(date, cumulative_count)], one point per day."""
    points = []
    for d in dates:
        if points and points[-1][0] == d:
            points[-1] = (d, points[-1][1] + 1)
        else:
            points.append((d, (points[-1][1] if points else 0) + 1))
    return points


def nice_ticks(vmax):
    """Y-axis ticks: 4-6 round steps from 0 covering vmax."""
    for step in (10, 20, 25, 50, 100, 150, 200, 250, 500, 1000, 2000, 2500, 5000):
        if vmax / step <= 5:
            break
    top = ((vmax + step - 1) // step) * step
    return list(range(0, top + 1, step))


def month_ticks(d0, d1):
    """X-axis ticks on month starts, thinned to at most ~6 labels."""
    months = []
    y, m = d0.year, d0.month
    if d0.day > 1:
        m += 1
        if m > 12:
            y, m = y + 1, 1
    while (y, m) <= (d1.year, d1.month):
        months.append(date(y, m, 1))
        m += 1
        if m > 12:
            y, m = y + 1, 1
    stride = max(1, (len(months) + 5) // 6)
    return months[::stride]


def render_svg(points, theme, as_of):
    c = THEME[theme]
    d0, d1 = points[0][0], points[-1][0]
    total = points[-1][1]
    yticks = nice_ticks(total)
    ymax = yticks[-1]
    span = max((d1 - d0).days, 1)
    pw, ph = W - ML - MR, H - MT - MB

    def x(d):
        return ML + pw * (d - d0).days / span

    def y(v):
        return MT + ph * (1 - v / ymax)

    path = " ".join(
        f"{'M' if i == 0 else 'L'}{x(d):.1f},{y(v):.1f}"
        for i, (d, v) in enumerate(points)
    )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'font-family="system-ui, -apple-system, \'Segoe UI\', sans-serif" font-size="12">',
        f'<title>Cumulative GitHub stars over time: {total} as of {as_of}</title>',
    ]
    for v in yticks[1:]:
        parts.append(
            f'<line x1="{ML}" y1="{y(v):.1f}" x2="{ML + pw}" y2="{y(v):.1f}" '
            f'stroke="{c["grid"]}" stroke-width="1"/>'
        )
        parts.append(
            f'<text x="{ML - 8}" y="{y(v) + 4:.1f}" text-anchor="end" '
            f'fill="{c["muted"]}" style="font-variant-numeric: tabular-nums">{v}</text>'
        )
    parts.append(
        f'<line x1="{ML}" y1="{y(0):.1f}" x2="{ML + pw}" y2="{y(0):.1f}" '
        f'stroke="{c["axis"]}" stroke-width="1"/>'
    )
    for m in month_ticks(d0, d1):
        label = m.strftime("%b %Y") if m.month == 1 or m == month_ticks(d0, d1)[0] else m.strftime("%b")
        parts.append(
            f'<text x="{x(m):.1f}" y="{H - MB + 20}" text-anchor="middle" '
            f'fill="{c["muted"]}">{label}</text>'
        )
    parts.append(
        f'<path d="{path}" fill="none" stroke="{c["series"]}" stroke-width="2" '
        'stroke-linejoin="round" stroke-linecap="round"/>'
    )
    ex, ey = x(d1), y(total)
    parts.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="4" fill="{c["series"]}"/>')
    parts.append(
        f'<text x="{ex + 10:.1f}" y="{ey + 4:.1f}" fill="{c["ink"]}" '
        f'font-weight="600" font-size="13">{total} ★</text>'
    )
    parts.append(
        f'<text x="{ML + pw}" y="{H - 6}" text-anchor="end" fill="{c["muted"]}" '
        f'font-size="11">as of {as_of}</text>'
    )
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main():
    repo = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPO)
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        sys.exit("GITHUB_TOKEN is required")

    points = cumulative_by_day(fetch_star_dates(repo, token))
    if not points:
        sys.exit(f"No stargazers found for {repo}")
    as_of = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    for theme, rel in OUT.items():
        out_path = os.path.join(root, rel)
        with open(out_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(render_svg(points, theme, as_of))
        print(f"wrote {rel} ({points[-1][1]} stars, {len(points)} points)")


if __name__ == "__main__":
    main()
