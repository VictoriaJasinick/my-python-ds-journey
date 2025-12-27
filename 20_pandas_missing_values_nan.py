import pandas as pd
import numpy as np

# Create DataFrame with missing values
df = pd.DataFrame({
    "name": ["Max", "Kate", "Sara"],
    "age": [45, np.nan, 18],
    "salary": [17000, 45000, np.nan]
})

# Check where values are missing
print(df.isna())

# Count missing values per column
print(df.isna().sum())

# Rows where age is missing
print(df[df["age"].isna()])

# Rows where salary is known
print(df[df["salary"].notna()])

# Fill missing age with the mean age
df["age"] = df["age"].fillna(df["age"].mean())

# Fill missing salary with 0
df["salary"] = df["salary"].fillna(0)

# Notes:
# NaN values should not be filled if it does not make sense for the data.
# dropna() can be dangerous because it may remove too many records unintentionally.
