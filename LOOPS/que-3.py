st = input("Enter a string : ")
a, d, s = 0, 0, 0
for char in st:
    if (char.isalpha()):
        a = a + 1
    elif (char.isdigit()):
        d = d + 1
    else :
        s = s + 1
print("Digit/s :",d)
print("Alphabet/s :",a)
print("Special Character/s : ",s)