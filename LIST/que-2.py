import random
L = []
for i in range(20):
    L.append(random.randint(1,100))
print(L)
num = int(input("Enter a number between 1 to 100 : "))
if (L.count(num) == 0):
    print("There isnot present",num,"in the list.")
else :
    print("The number is present at position/s :",L.index(num) + 1)