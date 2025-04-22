n = int(input("Enter n : "))
r = int(input("Enter r : "))
pn, pnr = 1, 1
if (n >= r):
    for i in range(1,n+1):
        pn *= i
    for i in range(1,(n-r)+1):
        pnr *= i
    print(n,"P",r,"=",int(pn / pnr))
else :
    print("Enter valid numbers.(n >= r)")