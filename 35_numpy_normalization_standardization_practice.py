import numpy as np

# ==================================================
# Task 1
# Normalization and Standardization
# ==================================================

a = np.array([10, 20, 30, 40, 50])

# Normalization (min-max scaling to [0, 1])
a_normalized = (a - a.min()) / (a.max() - a.min())

# Standardization (z-score: mean = 0, std = 1)
a_standardized = (a - a.mean()) / a.std()

print("Task 1:")
print("Original:", a)
print("Normalized:", a_normalized)
print("Standardized:", a_standardized)


# ==================================================
# Task 2
# Statistics before and after standardization
# ==================================================

b = np.random.randint(1, 1_000_001, size=1_000)

mean_before = b.mean()
median_before = np.median(b)
std_before = b.std()

b_standardized = (b - b.mean()) / b.std()

mean_after = b_standardized.mean()
median_after = np.median(b_standardized)
std_after = b_standardized.std()

print("\nTask 2:")
print("Before standardization:")
print("Mean:", mean_before)
print("Median:", median_before)
print("Std:", std_before)

print("\nAfter standardization:")
print("Mean:", mean_after)
print("Median:", median_after)
print("Std:", std_after)


# ==================================================
# Task 3
# Effect of an outlier
# ==================================================

b_with_outlier = np.append(b, 10_000)

mean_outlier = b_with_outlier.mean()
median_outlier = np.median(b_with_outlier)

print("\nTask 3:")
print("Mean after outlier:", mean_outlier)
print("Median after outlier:", median_outlier)

# Conclusion:
# The mean changes more than the median because it depends on all values,
# while the median depends only on the position of values in the sorted array.
