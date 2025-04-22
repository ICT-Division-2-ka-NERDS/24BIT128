n = int(input("Enter n : "))
r = int(input("Enter r : "))
fn, fr, fnr = 1, 1, 1
if (n >= r):
    for i in range(1,n+1):
        fn *= i
    for i in range(1,r+1):
        fr *= i
    for i in range(1,(n-r)+1):
        fnr *= i
    print(n,"C",r,"=",int(fn / (fnr * fr)))
else :
    print("Enter valid numbers.(n >= r)")