# Ask the user to input two numbers
a = int(input("Insert the first number: "))
b = int(input("Insert the second number: "))

# Create a list of all numbers between a and b (inclusive)
all_numbers = [x for x in range(a, b + 1)]

# Calculate the sum of all numbers in the list
total = 0
for x in all_numbers:
    total += x

# Print the result
print(f"The sum of all numbers from {a} to {b} is {total}")

# ─────────────────────────────────────────────────────────────
# Developer notes:
#
# 1. For real-world use, it's safer to check that b > a to avoid
#    confusion or unintended behavior.
#
# 2. We don't actually need to store the list in memory.
#    Python’s built-in `sum(range(...))` would be shorter and more efficient:
#
#      total = sum(range(a, b + 1))
#      print(f"The sum of all numbers from {a} to {b} is {total}")
#
# 3. But for the scope of this exercise, I left the longer version
#    to explicitly show list creation and manual summation.
#
#    This helps practice loops and list comprehensions together.
