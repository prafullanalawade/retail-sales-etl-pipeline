import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2001",
    database="etl_project"
)

cursor = conn.cursor()

# Extract
df = pd.read_csv("sales.csv")

# Fix column names (VERY IMPORTANT)
df.columns = df.columns.str.replace(" ", "_")

# Transform
df = df.dropna()
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# -------------------------------
# Load Customers
# -------------------------------
customers = df[['Customer_ID', 'Customer_Name']].drop_duplicates()

for _, row in customers.iterrows():
    cursor.execute(
        "INSERT INTO dim_customers VALUES (%s,%s)",
        (row['Customer_ID'], row['Customer_Name'])
    )

# -------------------------------
# Load Products
# -------------------------------
products = df[['Product_ID', 'Category']].drop_duplicates()

for _, row in products.iterrows():
    cursor.execute(
        "INSERT INTO dim_products VALUES (%s,%s)",
        (row['Product_ID'], row['Category'])
    )

# -------------------------------
# Load Fact Table
# -------------------------------
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO fact_sales VALUES (%s,%s,%s,%s,%s)",
        (
            row['Order_ID'],
            row['Customer_ID'],
            row['Product_ID'],
            row['Order_Date'],
            row['Sales']
        )
    )

conn.commit()

print("ETL Process Completed ✅")