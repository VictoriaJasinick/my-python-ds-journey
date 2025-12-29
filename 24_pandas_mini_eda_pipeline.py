import pandas as pd
import numpy as np

# Create initial DataFrame
df = pd.DataFrame({
    "user": ["Mariana", "Jordan", "Chris", "Jordan", "Mariana", "Alex"],
    "city": ["Rome", "Rome", "Bolzano", "Rome", "Bolzano", "Rome"],
    "age": [30, 40, 18, 40, 30, 50],
    "salary": [17000, 45000, np.nan, 45000, 17000, 60000],
    "is_premium": [True, False, False, False, True, True]
})

# -------------------------
# 1. First look at the data
# -------------------------
df.head()
df.info()
df.dtypes

# -------------------------
# 2. Data quality checks
# -------------------------
df.isna().sum()
df.duplicated().sum()

# -------------------------
# 3. Basic statistics
# -------------------------
df.describe()
df["city"].value_counts()

# -------------------------
# 4. Grouped analysis
# -------------------------
df.groupby("city")["salary"].mean()
df.groupby("city")["user"].count()

# -------------------------
# 5. Visual exploration
# -------------------------
df["salary"].plot(kind="hist")
df["salary"].plot(kind="box")
df["city"].value_counts().plot(kind="bar")

# -------------------------
# Conclusions (EDA summary)
# -------------------------
# 1. Rome has the highest number of users and the highest average salary.
# 2. There is one missing salary value, which should be handled before any modeling.
# 3. Salary distribution is right-skewed, with a potential high-income outlier.
# 4. Bolzano has fewer users and lower average salary compared to Rome.
# 5. Further analysis could explore salary differences by premium status and age groups.
