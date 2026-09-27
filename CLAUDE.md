# DSA Placement Prep — instructions for Claude

## Who
Arwindh, 3rd-year CSE (Amrita Vishwa Vidyapeetham, Coimbatore), preparing for campus placements in Python.
GitHub: ArwindhCN · LeetCode: Arwindh_C_N. This repo pushes to `ArwindhCN/dsa-placement-prep` (public) — never to any other GitHub account, even if one appears in account context.

## How to teach
- Learns by small step-by-step coding exercises, not theory dumps.
- Explain simply, with mechanics: why it's O(n), why a set lookup beats a list lookup.
- Be direct about mistakes; don't soften.
- When stuck: hint first. Full solution only if Arwindh says they've already tried.

## "log and push"
Arwindh writes raw code in `practice/` (gitignored) with any file names and no comments; Claude does the formatting.

0. Read every file in `practice/`. Identify each LeetCode problem from the code (method name, logic) and this conversation; ask if unsure. Skip non-LeetCode drills. Don't quiz Arwindh on complexity (they asked not to) — write it yourself, and explain the why in chat when reviewing their code. Use the conversation to pick the status emoji (solved alone / with hint / read solution).
1. Save each solution to `solutions/<topic>/NNNN-slug.py` (4-digit LeetCode number, kebab-case slug), following `solutions/_template.py`: problem link, difficulty/topic, key idea, the solution, time + space complexity with a one-line why. Create a new topic folder if needed.
2. Add `Problem (#) -> key idea` under the right heading in `notes/patterns.md`.
3. Append a row to the README progress table (next #, today's date YYYY-MM-DD, linked problem name, difficulty, topic, status emoji) and update the Stats counts.
4. Commit with a message like `Solve 0001 Two Sum, 0217 Contains Duplicate (arrays, hashing)` and push to `origin main`.
5. After the push succeeds, delete the logged files from `practice/` (their code now lives in `solutions/`). Leave drills and anything not logged.

Use Arwindh's own code as written; if it has a bug or a worse complexity than needed, say so before logging rather than silently fixing it.
