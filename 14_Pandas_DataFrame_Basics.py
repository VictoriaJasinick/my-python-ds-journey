import pandas as pd

# Create initial dataset using a dictionary
data = {
    "name": ["Viki", "Mary", "Sara"],
    "age": [26, 34, 29],
    "city": ["Rome", "New York", "Bolzano"]
}

# Create DataFrame from dictionary
df = pd.DataFrame(data)

# -----------------------------
# Basic DataFrame inspection
# -----------------------------

# Show the first rows of the DataFrame
print("DataFrame preview (head):")
print(df.head())

# Display DataFrame structure and data types
# Note: df.info() prints directly to console and returns None
print("\nDataFrame info:")
df.info()

# Show descriptive statistics for numeric columns only
print("\nDescriptive statistics (numeric columns only):")
print(df.describe())

# -----------------------------
# Working with columns
# -----------------------------

# Variant 1: Print column using separate print calls (recommended for readability)
print("\nColumn 'age' (as Series):")
print(df["age"])

# Variant 2: Print column by converting Series to string
# This avoids extra spaces added by print when passing multiple arguments
print("\nColumn 'age' (string representation):")
print(df["age"].to_string())

# Selecting multiple columns returns a DataFrame
print("\nColumns 'name' and 'city' (as DataFrame):")
print(df[["name", "city"]])
