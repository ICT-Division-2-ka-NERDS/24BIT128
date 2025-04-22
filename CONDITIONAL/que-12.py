x = int(input("Enter x-cordinate of center of circle : "))
y = int(input("Enter y-cordinate of center of circle : "))
r = int(input("Enter radius of a circle : "))
x1 = int(input("Enter x-cordinate of a point : "))
y1 = int(input("Enter y-cordinate of a point : "))

import math
d = math.sqrt(pow((x-x1),2) + pow((y-y1),2))

if r > d:
    print("Enter point is in the given circle.")
elif r < d:
    print("Enter point is outside the given circle.")
else:
    print("point is on the circle.")