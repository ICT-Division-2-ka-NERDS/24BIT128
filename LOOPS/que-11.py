d = int(input("Enter a angle (in degree) : "))
r = d * (3.14159 / 180)
sin = 0
for i in range(0,50):
    fact = 1
    for j in range(1,(2*i + 2)):
        fact *= j
    sin = sin + ((-1)**(i))*((r**(2*i + 1)) / fact)
print("sin(",d,")","=",sin)