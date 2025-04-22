l = int(input("Enyter length of a rectangle : "))
b = int(input("Enter breadth of a rectangle : "))
ar = l * b
pr = 2 * (l + b)

if ar > pr:
    print("Area of a given rectangle is greater than it's perimeter.")
elif pr > ar:
    print("Area of a given rectangle is less than it's perimeter.")
else:
    print("Area and perimeter if a given rectangle both are same.")