import random

list = ["positive", "negative"]
weight = [0.9, 0.1]

print (random.choices(list, weights=weight, k=1))

# print(random.choices(numberList, weights=(10, 20, 30, 40, 50), k=5))