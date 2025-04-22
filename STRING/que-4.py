str1 = input("Enter a string : ")
str2 = input("Enter a string which you want to delet : ")
a = str1.find(str2)
b = len(str2)
if (a >= 0):
    str3 = str1[:a] + str1[(a+b):]
    print("New string :",str3)
else :
    print("Entered string is not found in previous string.")