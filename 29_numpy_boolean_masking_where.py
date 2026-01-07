import numpy as np

# ------------------------------
# Boolean masking examples
# ------------------------------

a = np.array([5, 12, 25, 40, 7, 18])

# Elements greater than 10
print("Elements > 10:", a[a > 10])

# Elements less than or equal to 20
print("Elements <= 20:", a[a <= 20])

# Elements between 10 and 30 (exclusive)
print("Elements between 10 and 30:", a[(a > 10) & (a < 30)])

# ------------------------------
# np.where() example
# ------------------------------

b = np.arange(1, 11)

# Replace even numbers with 0, odd numbers with 1
even_odd_mask = np.where(b % 2 == 0, 0, 1)
print("Even/Odd mask:", even_odd_mask)

# ------------------------------
# Classification example
# ------------------------------

scores = np.array([45, 72, 88, 60, 30])

# Classify scores as pass/fail
status = np.where(scores >= 60, "pass", "fail")
print("Scores status:", status)
