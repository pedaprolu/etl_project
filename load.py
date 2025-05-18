# load.py

import pandas as pd
import psycopg2

# Load cleaned data
df = pd.read_csv("data/sales_cleaned.csv")

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="etl_project_db",
        user="postgres",
        password="admin123",   # replace if different
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    print("✅ Connected to PostgreSQL")

    # Insert rows into sales_data table
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO sales_data (order_id, product_name, order_date, sales, quantity, profit)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row["order_id"],
            row["product_name"],
            row["order_date"],
            row["sales"],
            int(row["quantity"]),
            row["profit"]
        ))

    conn.commit()
    print("✅ All data inserted into sales_data")

except Exception as e:
    print(f"❌ Error: {e}")
finally:
    cursor.close()
    conn.close()
