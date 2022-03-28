import numpy
import random, pandas as pd, csv

products = ["lime", "apple", "orange", "bred", "eggs", "butter", "oil", "gum", "icecream", "watermelon"]
code = list(numpy.random.random_integers(1, 100, 10))
price = list(numpy.random.random_integers(100, 999, 10))

listzip = list(zip(products, code, price))

df = pd.DataFrame(listzip)

df.to_csv('input_m.csv',index=False,header=["Product","Price","Worker Code"])

print(df)
