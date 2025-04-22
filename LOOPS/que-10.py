t = int(input("Enter number of terms which are you want to print : "))
a, b, c = 0, 1, 0
for i in range(0, t):
    a = b
    b = c
    c = a + b
    print(c,end=' ')