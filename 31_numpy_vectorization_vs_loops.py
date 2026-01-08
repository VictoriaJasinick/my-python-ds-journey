import numpy as np

# ==============================
# 6.8 Vectorization vs Loops
# ==============================

# Task 1:
# Create an array from 0 to 1_000_000 and apply vectorized operations

a = np.arange(1_000_001)
b = a * 3 + 7


# Task 2:
# Select elements greater than the mean value

mean_value = b.mean()
above_mean = b[b > mean_value]

print("Mean value:", mean_value)
print("Elements above mean:", above_mean[:10], "...")  # preview only


# Task 3:
# Use np.where for conditional logic without loops

scores = np.where(b >= 60, "pass", "fail")
print("Scores example:", scores[:10])


# Task 4:
# Compute sum and mean without loops

total_sum = b.sum()
average = b.mean()

print("Total sum:", total_sum)
print("Average:", average)


# Task 5:
# Conclusion
"""
Vectorized operations in NumPy are usually preferred because they:
- execute faster (C-level implementation),
- reduce Python-level loops,
- improve code readability,
- scale better for large datasets.

However, loops may still be appropriate for complex state-dependent logic
or when vectorization is not possible.
"""
