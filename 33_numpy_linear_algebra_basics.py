import numpy as np

# Define a 2x2 matrix
A = np.array([
    [1, 2],
    [3, 4]
])

# Transpose of the matrix (swap rows and columns)
A_transposed = A.T

# Determinant of the matrix
det_A = np.linalg.det(A)

# Matrix multiplication (linear algebra, not element-wise)
A_squared = A @ A

# Define a system of linear equations:
# 3x + y = 7
# x + 2y = 5
B = np.array([
    [3, 1],
    [1, 2]
])

c = np.array([7, 5])

# Solve the linear system B · x = c
solution = np.linalg.solve(B, c)

# Output results
print("Matrix A:\n", A)
print("\nTranspose of A:\n", A_transposed)
print("\nDeterminant of A:", det_A)
print("\nA @ A:\n", A_squared)
print("\nSolution of the linear system:", solution)
