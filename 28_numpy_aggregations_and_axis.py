import numpy as np

# ---------------------------------------------
# NumPy aggregations and axis logic
# ---------------------------------------------

m = np.array([
    [10, 20, 30],
    [5,  15, 25],
    [2,  4,  6]
])

# axis=1 -> collapse columns, result per row
sum_by_rows = m.sum(axis=1)
mean_by_rows = m.mean(axis=1)

# axis=0 -> collapse rows, result per column
sum_by_columns = m.sum(axis=0)
mean_by_columns = m.mean(axis=0)

print("Sum by rows:", sum_by_rows)
print("Mean by rows:", mean_by_rows)
print("Sum by columns:", sum_by_columns)
print("Mean by columns:", mean_by_columns)

# ---------------------------------------------
# Axis explanation example
# ---------------------------------------------

a = np.arange(1, 13).reshape(3, 4)

# axis=0 collapses rows -> one value per column
# axis=1 collapses columns -> one value per row

print("\nArray a:\n", a)
print("Sum axis=0:", a.sum(axis=0))
print("Sum axis=1:", a.sum(axis=1))
