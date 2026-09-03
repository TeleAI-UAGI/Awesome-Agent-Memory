# Contributing to Awesome Agent Memory

Thanks for helping keep this list useful! Contributions of new products, papers, benchmarks, tutorials, and articles are all welcome — as are link fixes and better categorization.

## What belongs here

- **Products**: systems whose primary purpose is memory for LLM/MLLM agents (memory layers, knowledge bases for agents, memory MCP servers, etc.).
- **Papers / Benchmarks / Surveys**: peer-reviewed or arXiv work on agent memory, long-term context, retrieval-augmented memory, parametric memory, continual learning, or memory evaluation.
- **Tutorials / Articles / Workshops**: substantial educational or editorial content about agent memory (not product announcements).

General-purpose vector databases, RAG frameworks, or agent frameworks where memory is a minor feature are out of scope.

## Entry format

### Open-Source products

Ordered by GitHub star count (descending). Use a numbered entry with a star badge:

```markdown
N. **[Name](https://homepage)**
     ![Star](https://img.shields.io/github/stars/owner/repo.svg?style=social&label=Star)
     [[code](https://github.com/owner/repo)]
     [[paper](https://arxiv.org/abs/XXXX.XXXXX)]
     _One-line factual description (≤ 25 words)._
```

Place the new entry at the position matching its current star count. Products with fewer than 100 stars go inside the collapsed **Emerging projects** `<details>` block at the end of the section (numbering continues there); they graduate into the main list once they cross 100 stars. CI checks both the ordering and this boundary weekly, with a ±10-star grace band so projects hovering around 100 don't bounce between sections.

### Closed-Source products

Unnumbered bullet, no star badge, appended to the end of the section:

```markdown
-  [Name](https://homepage)
   [[blog](https://...)]
   _One-line factual description (≤ 25 words)._
```

### Link labels

Keep the label vocabulary small and say what the link *is*: `code`, `paper`, `docs`, `blog`, `spec`, `data`, `model`, `eval`.

- **`eval`** — the project's own published evaluation results (self-reported, however reproducible the harness). Use it instead of `benchmark`/`benchmarks`, which reads as a neutral third-party suite. Independent placements belong in the description with a sourced attribution, not in a link label.
- **No package-registry links.** PyPI, npm, crates, and similar are distribution channels, not primary sources; the `code` link already leads to install instructions.

### Papers, benchmarks, surveys

Grouped by year (newest first). **Bold** the title if reproducible code is publicly available, and add the `[[code](...)]` link:

```markdown
- **[Paper Title](https://arxiv.org/abs/XXXX.XXXXX)**
    [[code](https://github.com/owner/repo)]
```

## Editorial policy

- **Same rules for everyone.** Projects affiliated with the maintainers follow the same ranking, format, and style rules as every other entry, and are marked with † in the README.
- **Drop-in replacements nest under their target.** A project whose purpose is to be an API-compatible replacement for a listed open-source product is written as an indented, unranked sub-item (`    - **[Name](...)**`) directly under that product rather than given its own star-ranked position. This applies regardless of who maintains it. `scripts/check_star_order.py` lists sub-items under their parent but excludes them from the star-order and 100-star-boundary checks.
- **Stars are a signal, not a verdict.** Star ordering is an objective, CI-checked popularity signal — it is not a quality ranking or an endorsement.
- **Claims name their source.** When an entry carries performance or benchmark claims, say where they come from: self-reported, paper-reported, or independently verified. Leaderboard placements use the compact form `#N, <Leaderboard> (<track>, YYYY-MM)` — e.g. `#6, Agent Memory Leaderboard (academic textual, 2026-08)` — so the attribution stays short enough to fit the 25-word description limit.
- **Neutral statuses.** Projects that go inactive or whose claims are credibly disputed move to the Archival section with a neutral status label (Disputed / Inactive / Archived), links to the evidence, and the date the status was last checked — we document, we don't editorialize.

## Style rules

- Descriptions are factual, not promotional — no superlatives, pricing, or marketing copy.
- Link to primary sources (official homepage, arXiv abstract page, GitHub repo).
- Use LF line endings (enforced by `.gitattributes`); please don't let your editor convert the file to CRLF.
- One resource per PR is easiest to review, but related batches are fine.

## Before submitting

1. Check the resource isn't already listed (search the README — projects sometimes appear under a different name).
2. Verify all links resolve.
3. Confirm placement: correct section, correct year group, correct star-rank position.
