import pandas as pd

# -------------------------
# CONCAT EXAMPLE
# -------------------------

users = pd.DataFrame({
    "name": ["Viki", "Marcel", "Mary"],
    "age": [30, 40, 25]
})

cities = pd.DataFrame({
    "city": ["Bolzano", "Copenhagen", "Rome"]
})

# Horizontal concatenation (by columns)
# Note: concat does NOT check logical relationships between data,
# it simply aligns rows by index.
concat_result = pd.concat([users, cities], axis=1)
print("Concat result (axis=1):")
print(concat_result)

# -------------------------
# MERGE EXAMPLE
# -------------------------

users2 = pd.DataFrame({
    "user_id": [1, 3, 5],
    "name": ["Alex", "Viki", "Dan"]
})

orders = pd.DataFrame({
    "user_id": [1, 2, 5],
    "total": [245, 392, 487]
})

# Inner join by user_id
merge_result = pd.merge(users2, orders, on="user_id", how="inner")
print("\nMerge result (inner join):")
print(merge_result)

# Notes:
# NaN values appear when there is no matching data between the tables.
# concat should not be used when data must be matched logically.
# merge is the correct tool when tables share a common key.
