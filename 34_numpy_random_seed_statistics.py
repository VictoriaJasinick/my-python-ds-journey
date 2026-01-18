import numpy as np

# Fix the random seed for reproducibility
np.random.seed(42)

# Generate an array of random integers from 1 to 1,000,000
a = np.random.randint(1, 1_000_001, size=1_000)

# Basic statistics
mean_a = a.mean() # Calculates the average (mean) of all elements in array a
median_a = np.median(a)  # Calculates the median (middle value) of the elements in array a
std_a = a.std() # Calculates the standard deviation (spread) of elements in array a

# Add an extreme outlier
b = np.append(a, 10_000_000)

# Statistics after adding the outlier
mean_b = b.mean()
median_b = np.median(b)
std_b = b.std()

# Count how many values are above the mean
above_mean_count = (b > mean_b).sum()

# Output results
print("Original array statistics:")
print(f"Mean: {mean_a}")
print(f"Median: {median_a}")
print(f"Std: {std_a}")

print("\nAfter adding an outlier:")
print(f"Mean: {mean_b}")
print(f"Median: {median_b}")
print(f"Std: {std_b}")

print(f"\nNumber of values above the mean: {above_mean_count}")
