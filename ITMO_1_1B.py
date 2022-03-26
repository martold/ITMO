cost = [54,32,123,43,251,23,56,74,767,49,78]
price = cost
for i in range(len(cost)):
    cost[i] += cost[i] * 0.2
print(price)