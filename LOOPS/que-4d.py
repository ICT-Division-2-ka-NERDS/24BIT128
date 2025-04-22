num = int(input("Enter a number : "))
sq = num**2
d = len(str(num))
if ((sq-num) % (10**d) == 0):
    print("Entered number is automorphic.")
else :
    print("Entered number is not automorphic.")