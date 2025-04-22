m1 = int(input("Enter marks of first subject : "))
m2 = int(input("Enter marks of second subject : "))
m3 = int(input("Enter marks of third subject : "))
totle = m1 + m2 + m3
avg = totle / 3
if 0 <= avg <= 39:
    print("Grade : Fail")
elif 40 <= avg <= 44:
    print("Grade : P")
elif 45 <= avg <= 49:
    print("Grade : C")
elif 50 <= avg <= 54:
    print("Grade : B")
elif 55 <= avg <= 59:
    print("Grade : B+")
elif 60 <= avg <= 69:
    print("Grade : A")
elif 70 <= avg <= 79:
    print("Grade : A+")
elif 80 <= avg <= 100:
    print("Grade : O")
else:
    print("Invalid marks.")