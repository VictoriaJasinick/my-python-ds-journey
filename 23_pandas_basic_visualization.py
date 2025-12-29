import pandas as pd
import numpy as np

# Create sample DataFrame
df = pd.DataFrame({
    "user": ["Mariana", "Jordan", "Chris", "Jordan", "Mariana"],
    "city": ["Rome", "Rome", "Bolzano", "Rome", "Bolzano"],
    "age": [30, 40, 18, 40, 30],
    "salary": [17000, 45000, np.nan, 45000, 17000]
})

# Histogram: salary distribution
# Shows how salary values are distributed across bins
df["salary"].plot(kind="hist", bins=5, title="Salary Distribution")

# Boxplot: salary spread and outliers
# Useful to detect outliers and understand median and quartiles
df["salary"].plot(kind="box", title="Salary Boxplot")

# Bar chart: number of users per city
# Value counts are used to aggregate categorical data
df["city"].value_counts().plot(kind="bar", title="Users per City")

# Bar chart: average salary per city
# NaN values are ignored by default in mean()
df.groupby("city")["salary"].mean().plot(kind="bar", title="Average Salary per City")

# Conclusion:
# The salary distribution is limited and fairly symmetric, with no visible outliers.
# Most users are located in Rome, which also shows a higher average salary
# compared to Bolzano in this small dataset.
