import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# 1. Create a synthetic dataset
np.random.seed(42)
n = 100
df = pd.DataFrame({
    "Date": pd.date_range(start="2023-01-01", periods=n, freq="D"),
    "Sales": np.random.randint(1000, 5000, size=n),
    "Marketing_Spend": np.random.randint(500, 3000, size=n),
    "Region": np.random.choice(["North", "South", "East", "West"], size=n)
})
df["Profit"] = df["Sales"] - df["Marketing_Spend"]

# 2. Basic Info
print("\n--- Dataset Info ---")
print(df.info())
print("\n--- Descriptive Stats ---")
print(df.describe())

# 3. Group by Region
region_summary = df.groupby("Region")[["Sales", "Marketing_Spend", "Profit"]].mean()
print("\n--- Average by Region ---")
print(region_summary)

# 4. Matplotlib: Sales and Marketing Spend Over Time
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Sales"], label="Sales", color="blue")
plt.plot(df["Date"], df["Marketing_Spend"], label="Marketing Spend", color="orange")
plt.title("Sales vs Marketing Spend Over Time")
plt.xlabel("Date")
plt.ylabel("Amount ($)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. Plotly: Interactive Line Chart
fig = px.line(df, x="Date", y=["Sales", "Marketing_Spend"], title="Interactive Sales vs Marketing Spend")
fig.show()

# 6. Histogram of Profit
plt.figure(figsize=(8, 5))
plt.hist(df["Profit"], bins=20, color="green", edgecolor="black")
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# 7. Plotly: Average Sales by Region
fig_bar = px.bar(region_summary.reset_index(), x="Region", y="Sales", title="Average Sales by Region")
fig_bar.show()
