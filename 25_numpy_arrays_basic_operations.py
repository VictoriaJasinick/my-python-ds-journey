import numpy as np

# Create a 1D NumPy array with values from 1 to 10
# (np.arange is the NumPy-native way to generate numeric ranges)
a = np.arange(1, 11)

# Basic array properties
a.ndim     # number of dimensions
a.shape    # array shape
a.dtype    # data type of elements

# Vectorized arithmetic operations
c = a * 3          # multiply each element by 3
d = a + 5          # add 5 to each element

# Adding values only to the first 5 elements
b = np.array([10, 20, 30, 40, 50])
a[:5] = a[:5] + b

# Boolean masking: values greater than the mean
mean_value = a.mean()
mask = a > mean_value
over_mean = a[mask]

# Number of elements greater than the mean
count_over_mean = over_mean.size

# Create a 2D NumPy array (matrix)
numbers = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Sum operations with axis parameter
column_sum = numbers.sum(axis=0)  # sum by columns
row_sum = numbers.sum(axis=1)     # sum by rows
