import sqlite3
import pandas as pd

# 1. Connect to the database provided in the repo
conn = sqlite3.connect('shipment_database.db')

# --- SPREADSHEET 0: Direct Insert ---
df0 = pd.read_csv('data/shipping_data_0.csv')
df0.to_sql('spreadsheet_0_table', conn, if_exists='append', index=False)

# --- SPREADSHEET 1 & 2: Merge & Insert ---
df1 = pd.read_csv('data/shipping_data_1.csv')
df2 = pd.read_csv('data/shipping_data_2.csv')

# The task says Spreadsheet 1 has products and 2 has origins/destinations.
# We merge them on the 'shipment_identifier' (the common link).
merged_df = pd.merge(df1, df2, on='shipment_identifier')

# Now insert the combined data into the database
merged_df.to_sql('shipment_items', conn, if_exists='append', index=False)

# Close connection
conn.close()
print("Success! Database populated.")