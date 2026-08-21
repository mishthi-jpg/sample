import numpy as np
import pandas as pd 
df = pd.read_csv('orders.csv')

row_count = len(df)
print(f"Number of rows in the DataFrame: {row_count}")

for col_name in df.columns:
    print(col_name)

for dtype in df.dtypes:
    print(dtype)
"""
print(df.duplicated())
a=0
for i in range(row_count):
    if df.duplicated().iloc[i]:
        a=a+1
        print(f"Row {i} is a duplicate.")
print(f"Total duplicates found: {a}")
"""

cols_to_check = df.columns[1:]
duplicates = df.duplicated(subset=cols_to_check, keep=False)

print(duplicates)

a=0
for i in range(row_count):
    if duplicates.iloc[i]:
        a=a+1
        print(f"Row {i} is a duplicate.")
print(f"Total duplicates found: {a}")

df=df.drop_duplicates(subset=cols_to_check, keep='first')

df.to_csv('orders_cleaned.csv', index=False)

df_cleaned = pd.read_csv('orders_cleaned.csv')

"""
df_cleaned = df_cleaned.replace(['null', 'NULL', 'NaN', ''], np.nan)

df_cleaned['quantity'] = pd.to_numeric(df_cleaned['quantity'], errors='coerce')

print(df_cleaned[['customer_email', 'quantity']].isna().sum())


df_cleaned.to_csv('orders_cleaned2.csv', index=False)
"""

is_missing = df_cleaned.isna()

for idx, row in is_missing.iterrows():
    if row.any():
        missing_cols = row[row].index.tolist()
        print(f"Row {idx} has missing values in columns: {missing_cols}")
        df_cleaned.loc[idx, missing_cols] = 'N/A'





df_cleaned['order_date'] = pd.to_datetime(df_cleaned['order_date'], errors='coerce')
df_cleaned['order_date'] = df_cleaned['order_date'].dt.strftime('%Y-%m-%d')

revenue = 0.0
for row2 in df_cleaned.itertuples():
    if row2.quantity != 'N/A' and row2.unit_price != 'N/A':
        revenue = revenue + (row2.quantity * row2.unit_price)

print(f"Total revenue: {revenue}")

summary = df_cleaned.groupby('product_category').agg(
    total_orders=('quantity', 'count'),
    total_revenue=('unit_price', 'sum')
)


df_cleaned.to_csv('orders_cleaned.csv', index=False)

print("Summary by product category:")
print(summary)