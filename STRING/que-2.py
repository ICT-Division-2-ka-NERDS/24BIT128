st = input("Enter a string : ")
a = int(input("What you want to do? (for lower:1,upper:2,toggle:3) : "))
s = [""] * len(st)
if (a == 1):
    for i in range(0,len(st)):
        if (65 <= ord(st[i]) <= 90):
            s[i] = s[i] + chr(ord(st[i]) + 32)
        elif (97 <= ord(st[i]) <= 122):
            s[i] = s[i] + st[i]
        else:
            s[i] = s[i] + st[i]
elif (a == 2):
    for i in range(0,len(st)):
        if (65 <= ord(st[i]) <= 90):
            s[i] = s[i] + st[i]
        elif (97 <= ord(st[i]) <= 122):
            s[i] = s[i] + chr(ord(st[i]) - 32)
        else:
            s[i] = s[i] + st[i]
elif (a == 3):
    for i in range(0,len(st)):
        if (65 <= ord(st[i]) <= 90):
            s[i] = s[i] + chr(ord(st[i]) + 32)
        elif (97 <= ord(st[i]) <= 122):
            s[i] = s[i] + chr(ord(st[i]) - 32)
        else:
            s[i] = s[i] + st[i]
else:
    print("Valide input.")
print(s)