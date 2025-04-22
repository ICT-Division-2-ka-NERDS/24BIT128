import random
s = {random.randint(15,45) for i in range(11)}
print(s)
count = sum(1 for ele in s if ele < 30)
print(count)
print({ele for ele in s if ele < 35})