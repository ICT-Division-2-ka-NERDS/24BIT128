a = input("Enter a string : ")
v = 0
for i in range (0, len(a)):
    if (a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u" or 
        a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U"):
        v = v + 1
print("No. of vowels in entered string is",v,".")