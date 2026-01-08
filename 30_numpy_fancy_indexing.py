import numpy as np

# ==============================
# 6.7 Fancy Indexing in NumPy
# ==============================

# Task 1:
# Select elements by explicit indices from a 1D array

a = np.array([5, 10, 15, 20, 25, 30])

# Fancy indexing using a list of indices
selected_elements = a[[1, 3, 5]]
print("Selected elements by indices [1, 3, 5]:", selected_elements)

# The same result using np.take (explicit and safer in pipelines)
selected_with_take = np.take(a, [1, 3, 5])
print("Selected elements using np.take:", selected_with_take)


# Task 2:
# Select the last and pre-last elements using negative indices

last_elements = a[[-1, -2]]
print("Last and pre-last elements:", last_elements)


# Task 3:
# Fancy indexing in a 2D array (main diagonal)

m = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Select elements (0,0), (1,1), (2,2)
diagonal = m[[0, 1, 2], [0, 1, 2]]
print("Main diagonal elements:", diagonal)


# Task 4:
# The same diagonal selection using np.take is NOT straightforward
# because np.take works on flattened arrays by default.
# Fancy indexing is the correct and readable solution here.


# Task 5:
# Summary of indexing methods

"""
SLICING:
- Selects a continuous block
- Returns a view when possible
- Example: a[1:4]

BOOLEAN MASKING:
- Selects elements based on a condition
- Returns a copy
- Example: a[a > 10]

FANCY INDEXING:
- Selects elements by explicit indices
- Returns a copy
- Example: a[[1, 3, 5]]
"""

print("Indexing methods comparison completed.")
