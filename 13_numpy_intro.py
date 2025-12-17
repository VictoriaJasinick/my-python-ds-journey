import numpy as np

# --- Level 1: Basic array creation and attributes ---

# Create an array with numbers from 10 to 50
a = np.array(range(10, 51))

# Check basic properties
print("Dimensions:", a.ndim)
print("Shape:", a.shape)
print("Data type:", a.dtype)


# --- Level 2: Arithmetic and filtering ---

# Create an array of 5 random numbers from 0 to 1
b = np.random.rand(5)
print("Random values (0–1):", b)

# Multiply a by 2 and add b (broadcasting will apply b only to the first 5 elements)
c = a[:5] * 2 + b
print("Modified first 5 elements of a:", c)

# Print values greater than 70
print("Values > 70:", np.sort(c[c > 70]))


# --- Level 3: Matrices ---

# Create a 3x3 matrix of ones
matrix_ones = np.ones((3, 3))
print("3×3 matrix of ones:\n", matrix_ones)

# Create array from -5 to 4 (10 elements)
d = np.array(range(-5, 5))

# Print only positive numbers (excluding zero)
print("Positive numbers from d:", d[d > 0])

# Reshape to 2x5
d_reshaped = d.reshape((2, 5))
print("Reshaped array (2×5):\n", d_reshaped)


# --- Level 4: Boolean mask experiment ---

a = np.array([1, 2, 3, 4, 5])
mask = a > 3

print("Boolean mask (a > 3):", mask)
print("Filtered values:", a[mask])


# --- Final reflection ---

"""
Summary about NumPy:
NumPy is a high-performance library that makes working with arrays much easier. 
It offers pre-built functions for mathematical operations, filtering, and reshaping data — 
allowing us to write clean, fast code without manual loops.

All of this can technically be done with native Python, but NumPy is significantly faster and more readable.
Great for both data science and real-world applications involving numerical logic.
"""
