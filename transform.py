# transform.py

import pandas as pd

# Load raw file
df = pd.read_csv("data/sales.csv", encoding='latin1')

# Select relevant columns and rename
df = df[[
    "Order ID", "Product Name", "Order Date", "Sales", "Quantity", "Profit"
]].rename(columns={
    "Order ID": "order_id",
    "Product Name": "product_name",
    "Order Date": "order_date",
    "Sales": "sales",
    "Quantity": "quantity",
    "Profit": "profit"
})

# Drop rows with nulls in required fields
df.dropna(subset=["order_id", "product_name", "order_date", "sales", "quantity"], inplace=True)

# Convert types
df["order_date"] = pd.to_datetime(df["order_date"], errors='coerce')
df["sales"] = pd.to_numeric(df["sales"], errors='coerce')
df["quantity"] = pd.to_numeric(df["quantity"], errors='coerce')
df["profit"] = pd.to_numeric(df["profit"], errors='coerce')

# Drop rows with bad conversions
df.dropna(subset=["order_date", "sales", "quantity"], inplace=True)

# Drop duplicates based on order_id
df.drop_duplicates(subset=["order_id"], inplace=True)

# Save cleaned output
df.to_csv("data/sales_cleaned.csv", index=False)

print("✅ Cleaned data saved to: data/sales_cleaned.csv")
print(f"📊 Final shape: {df.shape}")
