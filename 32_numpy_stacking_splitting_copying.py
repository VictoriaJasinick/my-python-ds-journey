import numpy as np

# -------------------------------
# Task 1–3: Stacking arrays
# -------------------------------

a = np.arange(6)
b = np.arange(6)

# Vertical stacking (adds rows)
v_stacked = np.vstack([a, b])
print("vstack result:\n", v_stacked)

# Horizontal stacking (extends array)
h_stacked = np.hstack([a, b])
print("hstack result:\n", h_stacked)

# Stack adds a NEW axis (default axis=0)
stacked = np.stack([a, b])
print("stack result:\n", stacked)
print("stack shape:", stacked.shape)

# -------------------------------
# Task 4: Splitting a matrix
# -------------------------------

c = np.arange(16).reshape(4, 4)
print("Original matrix:\n", c)

# Split into 2 parts by columns
hsplit_result = np.hsplit(c, 2)
print("hsplit result:\n", hsplit_result)

# Split into 4 parts by rows
vsplit_result = np.vsplit(c, 4)
print("vsplit result:\n", vsplit_result)

# -------------------------------
# Task 5: View behavior (DANGEROUS)
# -------------------------------

# Reshape returns a VIEW, not a copy
view_example = c.reshape(2, 8)
view_example[0, 0] = 999

print("After modifying view:")
print("view_example:\n", view_example)
print("original c (changed!):\n", c)

# -------------------------------
# Task 6: Safe copy
# -------------------------------

safe_copy = c.copy()
safe_copy[0, 1] = 777

print("After modifying copy:")
print("safe_copy:\n", safe_copy)
print("original c (unchanged):\n", c)
