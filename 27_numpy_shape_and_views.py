import numpy as np

# --------------------------------------------------
# 1. Creating a 1D array and inspecting its shape
# --------------------------------------------------

a = np.arange(12)

print("Array a:", a)
print("a.ndim:", a.ndim)
print("a.shape:", a.shape)

# --------------------------------------------------
# 2. Reshape: changing shape without changing data
# --------------------------------------------------

b = a.reshape(3, 4)
print("\nReshaped array b:\n", b)

# reshape returns a view (when possible)
b[0, 0] = 1000
print("\nAfter modifying b[0, 0]:")
print("Array a:", a)  # a is also modified → view

# --------------------------------------------------
# 3. ravel(): flattening (view if possible)
# --------------------------------------------------

r = b.ravel()

b[0, 0] = 77
print("\nAfter modifying b again:")
print("Array a:", a)
print("Raveled array r:", r)

# --------------------------------------------------
# 4. flatten(): always returns a copy
# --------------------------------------------------

f = b.flatten()
f[1] = 17

print("\nAfter modifying flattened array f:")
print("Array b (unchanged):\n", b)

# --------------------------------------------------
# 5. Transpose (.T): swapping axes for 2D arrays
# --------------------------------------------------

m = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

t = m.T
print("\nTransposed array t shape:", t.shape)

t[0, 0] = 365
print("Original array m after modifying t:\n", m)
# .T returns a view → original array is affected

# --------------------------------------------------
# 6. swapaxes(): works only for arrays with ndim >= 2
# --------------------------------------------------

x = np.arange(24).reshape(4, 6)
swapped = np.swapaxes(x, 0, 1)

print("\nOriginal shape:", x.shape)
print("Swapped shape:", swapped.shape)
