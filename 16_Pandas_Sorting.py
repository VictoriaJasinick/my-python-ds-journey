import pandas as pd

# Create sample DataFrame
data = {
    "name": ["Viki", "Mary", "Sara"],
    "age": [26, 34, 29],
    "salary": [10000, 4500, 3000]
}

df = pd.DataFrame(data)

# Sort by age (ascending by default)
print("Sorted by age (ascending):")
print(df.sort_values("age"))

# Sort by salary in descending order and save the result
df_sorted = df.sort_values("salary", ascending=False)
print("\nSorted by salary (descending):")
print(df_sorted)

# Sort by multiple columns:
# - age ascending
# - salary descending when age is the same
print("\nSorted by age and salary:")
print(df.sort_values(["age", "salary"], ascending=[True, False]))

# Explanation:
# In pandas, most operations return a new DataFrame instead of modifying the original one.
# This design protects the original dataset from accidental changes.
# If we want to keep the sorted result, we must explicitly assign it to a variable.
