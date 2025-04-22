import random
L = []
for i in range(50):
    L.append(random.randint(1,30))
print("L :",L)
for i in L:
    if L.count(i) > 1:
        L.remove(i)
print("New L :",L)