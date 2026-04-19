"""
Retail Sales Analysis Project

This script performs:
- Data loading
- Data cleaning
- Exploratory analysis
- Multi-table joins
- Basic visualizations
"""

import pandas as pd
import matplotlib.pyplot as plt


# Load Data

sales = pd.read_csv("data/sales_data.csv")
customers = pd.read_csv("data/customers.csv")
products = pd.read_csv("data/products.csv")


# Data Cleaning


# Remove duplicate rows
sales = sales.drop_duplicates()

# Standardize city names
sales["City"] = sales["City"].str.lower().str.strip()

# Replace missing/empty city values
sales["City"] = sales["City"].replace("", "unknown")
sales["City"] = sales["City"].fillna("unknown")

# Convert price to numeric
sales["Price"] = pd.to_numeric(sales["Price"], errors="coerce")

# Remove rows with invalid quantity
sales = sales[sales["Quantity"] > 0]

# Create Total_Sales column
sales["Total_Sales"] = sales["Price"] * sales["Quantity"]


# Basic Analysis


total_sales = sales["Total_Sales"].sum()
print("Total Sales:", total_sales)

city_sales = sales.groupby("City")["Total_Sales"].sum()
print("\nCity-wise Sales:\n", city_sales)

top_products = (
    sales.groupby("Product")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)
print("\nTop Products:\n", top_products)


# Advanced Analysis


category_sales = sales.groupby("Category")["Total_Sales"].sum()
print("\nCategory-wise Sales:\n", category_sales)

payment_distribution = sales["Payment_Method"].value_counts()
print("\nPayment Method Distribution:\n", payment_distribution)

rating_analysis = sales.groupby("Rating")["Total_Sales"].mean()
print("\nAverage Sales by Rating:\n", rating_analysis)

discount_analysis = sales.groupby("Discount")["Total_Sales"].mean()
print("\nDiscount Impact:\n", discount_analysis)


# Multi-table Join


merged = sales.merge(customers, on="Customer_ID", how="left")
merged = merged.merge(products, on="Product_ID", how="left")

print("\nJoined Data Sample:\n")
print(merged[["Customer_Name_x", "Product_Name", "Quantity"]].head())


# Visualizations


# Category-wise sales
category_sales.plot(kind="bar")
plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

plt.figure()

# Payment method distribution

payment_distribution.plot(kind="pie", autopct="%1.1f%%")
plt.title("Payment Method Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

plt.figure()

# Rating vs sales

rating_analysis.plot(kind="line", marker="o")
plt.title("Rating vs Average Sales")
plt.xlabel("Rating")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.show()

plt.figure()

# Discount impact

discount_analysis.plot(kind="bar")
plt.title("Discount vs Average Sales")
plt.xlabel("Discount")
plt.ylabel("Average Sales")
plt.tight_layout()
plt.show()
