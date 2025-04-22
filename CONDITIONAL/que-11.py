x1 = int(input("Enter x-cordinate of first point : "))
y1 = int(input("Enter y-cordinate of first point : "))
x2 = int(input("Enter x-cordinate of second point : "))
y2 = int(input("Enter y-cordinate of second point : "))
x3 = int(input("Enter x-cordinate of three point : "))
y3 = int(input("Enter y-cordinate of three point : "))

if (y2-y1)*(x3-x1) == (x2-x1)*(y3-y1):
    print("Entered points are colinear.")
else:
    print("Entered points are not in colinear.")