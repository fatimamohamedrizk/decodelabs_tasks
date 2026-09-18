# Project 4 — The General Knowledge Quiz
**DecodeLabs Industrial Training Kit — Batch 2026 (Optional Mastery Project)**

## What it does
Asks the user 3 general knowledge questions, keeps a running score, and prints the final result at the end.

## How to run
```bash
python3 quiz.py
```

## Why it's built this way (per the "Above the API" checklist)
| Requirement | What was used | Why |
|---|---|---|
| Logic Consistency | `if / else` on every question | Every question has both a success and a failure path — no silent gaps. |
| Whitespace Audit | `.strip()` on every raw input | Removes accidental leading/trailing spaces before comparing. |
| Data Normalization | `.lower()` on both user input and reference answer | Makes the check case-insensitive (`"Paris"`, `"paris"`, `"PARIS"` all count). |
| Type Integrity | `score = 0` (integer), `score += 1` only on success | Reliable cumulative math; state is maintained (not reset) on a wrong answer. |
| Output Clarity | f-strings for the final report | Clean, readable console output. |

## Example output
```
=== DecodeLabs Project 4: The General Knowledge Quiz ===

What is the capital of France? paris
✅ Correct!

What is the largest planet in our solar system? Mars
❌ Wrong. The correct answer was: Jupiter

Which programming language is this project written in? Python
✅ Correct!

--- Final Report ---
Your final score: 2/3
👍 Good job!
```

## Files
- `quiz.py` — main script
