# Monthly Budget Tracker
# Intro to Python Project - Matches classmate's simplicity level

print("=== Monthly Budget Tracker ===")
print("This program helps you track your monthly spending.\n")

# MVP 1 & 2: Greeting + set budget
budget = float(input("Enter your monthly budget: $"))

expenses = []
total_spent = 0.0

print("\nEnter expenses one by one. Press Enter (no name) when done.\n")

# MVP 3: Add expenses loop + show remaining after each
while True:
    name = input("Expense name: ").strip()
    if name == "":
        break
    try:
        amount = float(input(f"Amount for '{name}': $"))
        if amount <= 0:
            print("Amount must be positive. Try again.")
            continue
        expenses.append((name, amount))
        total_spent += amount
        remaining = budget - total_spent
        print(f"Remaining budget: ${remaining}\n")
    except ValueError:
        print("Please enter a valid number for the amount.\n")

# MVP 4: Final summary
print("\n=== MONTHLY SUMMARY ===")
print(f"Monthly Budget:     ${budget}")
print(f"Total Spent:        ${total_spent}")
print(f"Money Remaining:    ${budget - total_spent}")

print("\nExpenses:")
if not expenses:
    print("   (No expenses entered)")
else:
    for i, (name, amount) in enumerate(expenses, 1):
        print(f"   {i}. {name} — ${amount}")

print("===========================")