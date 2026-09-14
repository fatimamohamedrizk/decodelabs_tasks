def expense_tracker():
    total = 0.0          # State initialized BEFORE the loop
    count = 0            # Number of expenses recorded (optional but useful)

    print("=== Expense Tracker ===")
    print("Enter an expense amount and it will be added to your total.")
    print("Type 'done' when you want to stop and see the final total.\n")

    while True:
        user_input = input("Enter expense (or type 'done' to finish): ").strip()

        # Kill Switch / Sentinel Value
        if user_input.lower() == "done":
            break

        # Defensive Coding: make sure the input is a valid number
        try:
            expense = float(user_input)
        except ValueError:
            print("⚠️  Error: Please enter a valid number (or 'done' to exit).\n")
            continue

        # Prevent negative values (optional but makes sense for an expense app)
        if expense < 0:
            print("⚠️  Negative values are not allowed.\n")
            continue

        # Accumulator Pattern
        total += expense
        count += 1
        print(f"✅ Added. Current total: {total:.2f}\n")

    # Final Output
    print("\n--- Final Report ---")
    print(f"Number of expenses recorded: {count}")
    print(f"Total spent: {total:.2f}")


if __name__ == "__main__":
    expense_tracker()