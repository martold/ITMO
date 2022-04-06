# import csv
# with open('/Users/admin/Desktop/orderdata_sample.csv') as csvfile:
#     inputcsv = csv.reader(csvfile, delimiter=',')
#     for i in inputcsv:
#         print(i)

import pandas as pd

filename = r"/Users/admin/Desktop/orderdata_sample.csv"
df = pd.read_csv(filename)
df['Quantity'] = df['Quantity'].astype(float)
df['Price'] = df['Price'].astype(float)
df['Freight'] = df['Freight'].astype(float)
print(df)
df = df.eval("Total = Quantity * Price + Freight")
print(df)
df.to_csv(r"/Users/admin/Desktop/result.csv", index=False)
