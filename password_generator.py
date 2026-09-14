"""
Project 3 - Random Password Generator
DecodeLabs Industrial Training Kit | Batch 2026

Goal:
    Ask the user for a desired password length and generate a random,
    complex password made of letters and numbers.

Why this implementation follows the project brief:
    - Uses the `secrets` module (not `random`) because `random` relies on
      the Mersenne Twister, a *deterministic* generator that is not safe
      for anything security-related (passwords, tokens, etc.).
    - Uses the `string` module (string.ascii_letters, string.digits,
      string.punctuation) instead of manually typing out character sets.
    - Builds the password with a list + ''.join() instead of the
      `password += char` pattern, because strings are immutable in
      Python: every += creates a brand-new string in memory, which is
      slow (O(n^2)) for long passwords. join() allocates memory once and
      is O(n).
    - Validates user input so the program never crashes on bad input
      and never silently creates a weak/empty password.
"""

import string
import secrets


# NIST SP 800-63-4 (2024) guidance used as reference for this project:
MIN_LENGTH = 8            # absolute floor, program will not go below this
RECOMMENDED_LENGTH = 15    # NIST's minimum for high-security contexts
MAX_LENGTH = 64            # NIST's recommended upper bound


def get_password_length() -> int:
    """
    Phase 1 - Input.
    Repeatedly asks the user for a password length until a valid
    integer within an acceptable range is provided.
    """
    while True:
        raw_value = input(
            f"Enter the desired password length "
            f"({MIN_LENGTH}-{MAX_LENGTH}, {RECOMMENDED_LENGTH}+ recommended): "
        ).strip()

        try:
            length = int(raw_value)
        except ValueError:
            print("Please enter a whole number (e.g., 12).")
            continue

        if length < MIN_LENGTH:
            print(f"Length must be at least {MIN_LENGTH} characters for basic safety.")
            continue

        if length > MAX_LENGTH:
            print(f"Length must not exceed {MAX_LENGTH} characters.")
            continue

        if length < RECOMMENDED_LENGTH:
            print(
                f"Note: NIST 2024 guidelines recommend {RECOMMENDED_LENGTH}+ "
                f"characters for high-security passwords."
            )

        return length


def build_character_pool(include_symbols: bool = False) -> str:
    """
    Phase 2 (part 1) - defines the pool of characters the password can be
    built from. Uses the string module instead of manually typed arrays.
    """
    pool = string.ascii_letters + string.digits
    if include_symbols:
        pool += string.punctuation
    return pool


def generate_password(length: int, include_symbols: bool = False) -> str:
    """
    Phase 2 (part 2) - the transformation engine.
    Uses secrets.choice() (cryptographically secure) instead of
    random.choice(), and a list comprehension + ''.join() instead of
    repeated string concatenation.
    """
    pool = build_character_pool(include_symbols)
    password_chars = [secrets.choice(pool) for _ in range(length)]
    return "".join(password_chars)


def calculate_entropy(length: int, pool_size: int) -> float:
    """
    Phase 3 - mathematically proves the strength of the generated
    password using the information-entropy formula:
        E = L * log2(R)
    where L = length, R = size of the character pool.
    """
    import math
    return length * math.log2(pool_size)


def main():
    print("=== DecodeLabs Project 3: Random Password Generator ===\n")

    length = get_password_length()

    choice = input("Include special symbols too? (y/N): ").strip().lower()
    include_symbols = choice == "y"

    password = generate_password(length, include_symbols)
    pool_size = len(build_character_pool(include_symbols))
    entropy_bits = calculate_entropy(length, pool_size)

    print("\nYour generated password:")
    print(password)
    print(f"\nEstimated entropy: {entropy_bits:.1f} bits")

    if entropy_bits < 60:
        print("This is relatively weak. Consider a longer length.")
    elif entropy_bits < 90:
        print("This is a reasonably strong password.")
    else:
        print("This is a very strong password.")


if __name__ == "__main__":
    main()
