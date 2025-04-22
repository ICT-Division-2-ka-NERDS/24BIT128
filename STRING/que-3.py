str = input("Enter a string : ")
a = input("Enter a string which you want to compare : ")
if (str.find(a) > 0):
    print("Entered string is present in above string.")
else :
    print("Entered string is not present in above string.")
print(str.find(a))