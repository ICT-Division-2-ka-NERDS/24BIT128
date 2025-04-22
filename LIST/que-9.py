import random
L1 = []
L2 = []
for i in range(10):
    L1.append(random.randint(1,10))
for i in range(15):
    L2.append(random.randint(1,20))
print(L1)
print(L2)
L = []
for ele in L1:
    if (ele not in L2 and ele not in L):
        L.append(ele)
print(L)