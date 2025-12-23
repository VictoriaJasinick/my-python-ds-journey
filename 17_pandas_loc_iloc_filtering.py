import pandas as pd

data = {
    "name": ["Viki", "Mary", "Sara", "John"],
    "age": [26, 34, 29, 41],
    "city": ["Rome", "New York", "Bolzano", "Rome"],
    "salary": [10000, 4500, 3000, 7000],
}

df = pd.DataFrame(data)

# 1) Users older than 30
print("1) Users older than 30:")
print(df.loc[df["age"] > 30])

# 2) Name and city for users from Rome
print("\n2) Users from Rome (name, city):")
print(df.loc[df["city"] == "Rome", ["name", "city"]])

# 3) Salary between 3000 and 8000 AND age > 30
print("\n3) Salary (3000, 8000) and age > 30:")
print(df.loc[(df["salary"] > 3000) & (df["salary"] < 8000) & (df["age"] > 30)])

# 4) First 2 rows and last 2 columns (using iloc)
print("\n4) First 2 rows and last 2 columns:")
print(df.iloc[:2, -2:])

# 5) Name and salary for users younger than 35
print("\n5) Users younger than 35 (name, salary):")
print(df.loc[df["age"] < 35, ["name", "salary"]])

# Note: Initially I placed the age filter in the columns section, which felt intuitive.
This helped me realize that in pandas conditions filter rows, while columns define what information to display.
