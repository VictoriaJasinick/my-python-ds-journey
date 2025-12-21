import pandas as pd
import numpy as np

# Create sample DataFrame
data = {
    "name": ["Viki", "Mary", "Sara"],
    "age": [26, 34, 29],
    "city": ["Rome", "New York", "Bolzano"],
    "salary": [10000, 4500, 3000]
}

df = pd.DataFrame(data)

# Filter people older than 30
print("People older than 30:")
print(df[df["age"] > 30])

# Filter people from Bolzano
print("\nPeople from Bolzano:")
print(df[df["city"] == "Bolzano"])

# Filter salary between 3000 and 5000
print("\nSalary between 3000 and 5000:")
print(df[(df["salary"] > 3000) & (df["salary"] < 5000)])

# Filter people from Rome or Bolzano
print("\nPeople from Rome or Bolzano:")
print(df[df["city"].isin(["Rome", "Bolzano"])])

# Exclude people from Bolzano
print("\nPeople NOT from Bolzano:")
print(df[~(df["city"] == "Bolzano")])

# Add NaN value to salary
df.loc[1, "salary"] = np.nan

# Rows with NaN salary
print("\nRows with NaN salary:")
print(df[df["salary"].isna()])

# Rows without NaN salary
print("\nRows without NaN salary:")
print(df[df["salary"].notna()])
