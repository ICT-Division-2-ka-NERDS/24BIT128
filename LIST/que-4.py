import random
L = []
for i in range(30):
    L.append(random.randint(-50,50))
print(L)
L1 = []
L2 = []
for ele in L:
    if (ele < 0):
        L1.append(ele)
    else :
        L2.append(ele)
print("Negative :",L1)
print("Positive :",L2)