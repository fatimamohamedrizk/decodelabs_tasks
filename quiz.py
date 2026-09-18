"""
Project 4 - The General Knowledge Quiz
DecodeLabs Industrial Training Kit | Batch 2026

Goal:
    Create a game that asks 3 questions. Keep a score counter: +1 point
    for every correct answer. Print the final score at the end.

Key Skill: If-Else logic & Variables (Control Flow).

Why this implementation follows the project brief ("Above the API" checklist):
    - Logic Consistency: every question has both a success (if) and a
      failure (else) path — no silent gaps.
    - Whitespace Audit: .strip() is applied to every raw input to remove
      accidental leading/trailing spaces before comparison.
    - Data Normalization: .lower() is applied uniformly so the check is
      case-insensitive ("Paris", "paris", "PARIS" all count as correct).
    - Type Integrity: score is initialized as an integer (score = 0) and
      only ever incremented with score += 1 — no floats, no resets on
      failure (state is intentionally maintained, not reset).
    - Output Clarity: the final result is built with an f-string.
"""


def ask_question(question: str, correct_answer: str) -> bool:
    """
    One repeatable question block (Ask & Capture -> Sanitize -> Evaluate -> Execute).
    Returns True if the answer was correct, False otherwise.
    """
    raw_answer = input(question + " ")

    # Sanitization pipeline: strip surrounding whitespace, then normalize case.
    user_answer = raw_answer.strip().lower()
    reference_answer = correct_answer.strip().lower()

    if user_answer == reference_answer:
        print("✅ Correct!\n")
        return True
    else:
        print(f"❌ Wrong. The correct answer was: {correct_answer}\n")
        return False


def main():
    print("=== DecodeLabs Project 4: The General Knowledge Quiz ===\n")

    score = 0  # State Initialization - integer accumulator

    questions = [
        ("What is the capital of France?", "Paris"),
        ("What is the largest planet in our solar system?", "Jupiter"),
        ("Which programming language is this project written in?", "Python"),
    ]

    for question_text, answer in questions:
        if ask_question(question_text, answer):
            score += 1  # Accumulator pattern - only touched on success

    total = len(questions)
    print("--- Final Report ---")
    print(f"Your final score: {score}/{total}")

    if score == total:
        print("🏆 Perfect score! Excellent work.")
    elif score >= total / 2:
        print("👍 Good job!")
    else:
        print("📚 Keep practicing!")


if __name__ == "__main__":
    main()
