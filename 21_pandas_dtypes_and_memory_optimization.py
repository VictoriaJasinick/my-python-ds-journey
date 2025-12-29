import pandas as pd
import numpy as np

# Create sample DataFrame
df = pd.DataFrame({
    "user": ["Mariana", "Jordan", "Chris", "Jordan", "Mariana"],
    "city": ["Rome", "Rome", "Bolzano", "Rome", "Bolzano"],
    "age": [30, 40, 18, 40, 30],
    "salary": [17000, 45000, np.nan, 45000, 17000],
    "is_premium": ["yes", "no", "no", "no", "yes"]
})

# Check data types of all columns
print("Data types before optimization:")
print(df.dtypes)

# Measure memory usage before optimization
memory_before = df.memory_usage(deep=True).sum()

# Optimize data types
df["city"] = df["city"].astype("category")
df["salary"] = df["salary"].astype("Int64")  # nullable integer
df["is_premium"] = df["is_premium"].map({"yes": True, "no": False})

# Check data types after optimization
print("\nData types after optimization:")
print(df.dtypes)

# Measure memory usage after optimization
memory_after = df.memory_usage(deep=True).sum()

# Compare memory usage
print(f"\nMemory usage before optimization: {memory_before} bytes")
print(f"Memory usage after optimization:  {memory_after} bytes")

# Conclusion:
# Using appropriate data types improves memory efficiency and performance.
# It also makes the dataset more semantically correct and easier to work with.
