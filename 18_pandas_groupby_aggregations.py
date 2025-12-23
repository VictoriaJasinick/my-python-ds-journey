import pandas as pd
import numpy as np

# Sample dataset
data = {
    "name": ["Viki", "Mary", "Sara", "John", "Anna"],
    "city": ["Rome", "New York", "Rome", "Rome", "New York"],
    "salary": [10000, 4500, 3000, 7000, 8000],
    "age": [26, 34, 29, 41, 31]
}

df = pd.DataFrame(data)

# 1) Average salary by city
avg_salary_by_city = df.groupby("city")["salary"].mean()
print("Average salary by city:")
print(avg_salary_by_city)

# 2) Multiple aggregations by city
city_stats = df.groupby("city").agg(
    salary_mean=("salary", "mean"),
    salary_sum=("salary", "sum"),
    avg_age=("age", "mean"),
    user_count=("name", "count")
)

print("\nCity statistics:")
print(city_stats)

# Note:
# user_count is calculated using 'count' because we want the number of records (users),
# not a numerical sum.
# If NaN values appear in 'salary', pandas ignores them by default when calculating
# mean and sum.
