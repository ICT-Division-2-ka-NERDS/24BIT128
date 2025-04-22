num = int(input("Eneter a number of elements : "))
L = []
print("Eneter temperature in fahrenheit : ")
for i in range(num):
    L.append(float(input()))
print(L)
L1 = []
for ele in L:
    L1.append((ele - 32) * 5 / 9)
print("Temperature in celsius :",L1)