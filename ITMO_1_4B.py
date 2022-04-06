import pandas as pd

filename = r"/Users/admin/Desktop/orderdata_sample.csv"
df = pd.read_csv(filename)
df['Quantity'] = df['Quantity'].astype(float)
df['Price'] = df['Price'].astype(float)
df['Freight'] = df['Freight'].astype(float)
df = df.eval("Total = Quantity * Price + Freight")
print(df)
df.to_csv(r"/Users/admin/Desktop/result.csv", index=False)
