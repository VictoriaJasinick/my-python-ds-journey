import numpy as np

# --- 1. Create a 1D NumPy array ---
# Using arange to generate values from 1 to 99
a = np.arange(1, 100)

# Vectorized arithmetic operations
c = a + 100        # add 100 to each element
d = c * 0.5        # multiply each element by 0.5

# --- 2. Element-wise addition with equal shapes ---
b = np.array([17, 13, 25, 47, 7])

# Add array b to the first 5 elements of a
e = a[:5] + b

# --- 3. 2D array (matrix) and broadcasting ---
# Create a 2x3 matrix
f = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Create a 1D array with length equal to the number of columns
g = np.array([7, 8, 9])

# Broadcasting: g is added to each row of f
h = f + g

# --- 4. Example of incompatible shapes (broadcasting error) ---
x = np.array([1, 2, 3])
y = np.array([10, 20])

# This operation will raise a ValueError because shapes are incompatible
# x + y
