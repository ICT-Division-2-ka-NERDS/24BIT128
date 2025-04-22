import random
l = [random.randint(-15,15) for i in range(10)]
print(l)
print(list(map(lambda i: i**2,l)))