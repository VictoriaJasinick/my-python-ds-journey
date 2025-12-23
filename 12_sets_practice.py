# This script demonstrates the use of Python sets:
# - how they remove duplicates
# - basic set operations (add, discard, union, intersection, difference)
# - converting between list and set

# Create a set with repeated numbers
numbers = {0, 1, 1, 2, 3, 5, 5}
print("Set with duplicates removed:", numbers)  # Output: {0, 1, 2, 3, 5}

# Check if a number is in the set
print("Is 3 in numbers?", 3 in numbers)  # Output: True

# Add a number to the set
numbers.add(5)  # No effect because 5 is already in the set

# Remove a number safely (no error if not found)
numbers.discard(2)  # Removes 2

# Sample sets for operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Intersection (common elements)
print("Intersection of a and b:", a.intersection(b))  # Output: {3, 4}

# Difference (elements in a but not in b)
print("Difference a - b:", a.difference(b))  # Output: {1, 2}
print("Difference b - a:", b.difference(a))  # Output: {5, 6}

# Union (all unique elements from both)
print("Union of a and b:", a.union(b))  # Output: {1, 2, 3, 4, 5, 6}

# Remove duplicates from a list using set, then convert back to list
items = [1, 2, 2, 3, 4, 4, 5]
unique_items = list(set(items))
print("Unique items from list:", unique_items)

# Clear a set (remove all elements)
numbers.clear()
print("Cleared set:", numbers)  # Output: set()
