import pandas as pd

# STEP 1: Load data
df = pd.read_csv("data/sales_data.csv")

# STEP 2: Remove duplicates
df = df.drop_duplicates()

# STEP 3: Fix City (case mismatch)
df["City"] = df["City"].str.lower()

# STEP 4: Fill missing City
df["City"] = df["City"].fillna("unknown")

# STEP 5: Clean Price (remove 'rs')
df["Price"] = df["Price"].astype(str).str.replace("rs", "")
df["Price"] = df["Price"].astype(float)

# STEP 6: Fill missing Rating with average
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

# STEP 7: Remove rows where Quantity = 0
df = df[df["Quantity"] != 0]

# STEP 8: Create Total Sales column
df["Total_Sales"] = df["Price"] * df["Quantity"]

# STEP 9: Save cleaned data
df.to_csv("data/cleaned_data.csv", index=False)

print("Data cleaning done")