a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

if a > b > c:
    print("Largest =",a)
    print("Smallest =",c)
elif a > c > b:
    print("Largest =",a)
    print("Smallest =",b)
elif b > a > c:
    print("Largest =",b)
    print("Smallest =",c)
elif b > c > a:
    print("Largest =",b)
    print("Smallest =",a)
elif c > a > b:
    print("Largest =",c)
    print("Smallest =",b)
elif c > b > a:
    print("Largest =",c)
    print("Smallest =",a)
elif a == b and a > c:
    print("Largest =",a,"(a = b)")
    print("Smallest =",c)
elif a == b and a < c:
    print("Largest =",c)
    print("Smallest =",a,"(a = b)")
elif a == c and a > b:
    print("Largest =",a,"(a = c)")
    print("Smallest =",b)
elif a == c and a < b:
    print("Largest =",b)
    print("Smallest =",a,"(a = c)")
elif b == c and a > b:
    print("Largest =",a)
    print("Smallest =",b,"(b = c)")
elif b == c and a < b:
    print("Largest =",b,"(b = c)")
    print("Smallest =",a)
else :
    print("All values are same.(a = b = c)")