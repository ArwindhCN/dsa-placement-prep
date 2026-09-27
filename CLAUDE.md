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
1. Save each solution to `solutions/<topic>/NNNN-slug.py` (4-digit LeetCode number, kebab-case slug), following `solutions/_template.py`: problem link, difficulty/topic, key idea, the solution, time + space complexity with a one-line why. Create a new topic folder if needed.
2. Add `Problem (#) -> key idea` under the right heading in `notes/patterns.md`.
3. Append a row to the README progress table (next #, today's date YYYY-MM-DD, linked problem name, difficulty, topic, status emoji) and update the Stats counts.
4. Commit with a message like `Solve 0001 Two Sum, 0217 Contains Duplicate (arrays, hashing)` and push to `origin main`.

Use Arwindh's own code as written; if it has a bug or a worse complexity than needed, say so before logging rather than silently fixing it.
