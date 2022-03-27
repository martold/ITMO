cost = [54,32,123,43,251,23,56,74,767,49,78]
price = [54,32,123,43,251,23,56,74,767,49,78]
for i in range(len(price)):
    price[i] += price[i] * 0.2
print(price)