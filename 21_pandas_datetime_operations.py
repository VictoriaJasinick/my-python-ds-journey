import pandas as pd
import numpy as np

# Create DataFrame with user activity dates
df = pd.DataFrame({
    "user": ["Mariana", "Jordan", "Chris"],
    "signup_date": ["2025-01-13", "2024-12-01", "2025-01-11"],
    "last_login": ["2025-03-13", "2024-12-01", "2025-02-11"]
})

# Convert date columns to datetime
df["signup_date"] = pd.to_datetime(df["signup_date"])
df["last_login"] = pd.to_datetime(df["last_login"])

# Extract registration date components
df["signup_year"] = df["signup_date"].dt.year
df["signup_month"] = df["signup_date"].dt.month
df["signup_weekday"] = df["signup_date"].dt.weekday

# Calculate how long each user has been active
df["active_days"] = df["last_login"] - df["signup_date"]

# Filter users registered after 2024-01-01
recent_users = df[df["signup_date"] >= "2024-01-01"]

# Sort users by signup date
df_sorted = df.sort_values("signup_date")

print(df_sorted)
