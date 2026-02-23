import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# -----------------------------
# STEP 1: Create Funnel Dataset
# -----------------------------

data = {
    "Channel": ["Google Ads", "Facebook", "Instagram", "Email", "LinkedIn"],
    "Visitors": [10000, 8500, 9000, 5000, 4000],
    "Leads": [2500, 2000, 1800, 2200, 1500],
    "Qualified_Leads": [1500, 1100, 1000, 1600, 900],
    "Customers": [800, 600, 550, 900, 400],
    "Marketing_Cost": [200000, 150000, 130000, 80000, 90000]
}

df = pd.DataFrame(data)

print(df)

# -----------------------------
# STEP 2: Conversion Rates
# -----------------------------

df["Visitor_to_Lead"] = df["Leads"] / df["Visitors"]
df["Lead_to_Qualified"] = df["Qualified_Leads"] / df["Leads"]
df["Qualified_to_Customer"] = df["Customers"] / df["Qualified_Leads"]
df["Overall_Conversion"] = df["Customers"] / df["Visitors"]

print("\nConversion Rates:")
print(df[["Channel", "Overall_Conversion"]])

# -----------------------------
# STEP 3: Drop-off Analysis
# -----------------------------

dropoff = {
    "Visitors_to_Leads": df["Visitors"].sum() - df["Leads"].sum(),
    "Leads_to_Qualified": df["Leads"].sum() - df["Qualified_Leads"].sum(),
    "Qualified_to_Customers": df["Qualified_Leads"].sum() - df["Customers"].sum()
}

plt.figure()
plt.bar(dropoff.keys(), dropoff.values())
plt.title("Funnel Drop-Off Analysis")
plt.ylabel("Number of Users Dropped")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# STEP 4: Channel Performance
# -----------------------------

df["Cost_Per_Customer"] = df["Marketing_Cost"] / df["Customers"]

plt.figure()
plt.bar(df["Channel"], df["Cost_Per_Customer"])
plt.title("Cost Per Customer by Channel")
plt.ylabel("Cost")
plt.xticks(rotation=45)
plt.show()

# -----------------------------
# STEP 5: ROI Analysis
# -----------------------------

# Assume average revenue per customer = 5000
df["Revenue"] = df["Customers"] * 5000
df["ROI"] = (df["Revenue"] - df["Marketing_Cost"]) / df["Marketing_Cost"]

plt.figure()
plt.bar(df["Channel"], df["ROI"])
plt.title("Return on Investment (ROI)")
plt.ylabel("ROI")
plt.xticks(rotation=45)
plt.show()