num = int(input("Enter a number : "))
d = len(str(num))
div = num
tem = 0
while div > 0:
    tem = tem + (div % 10)**(d)
    div = int(div / 10)
if tem == num :
    print("Entered number is armstrong.")
else :
    print("Entered number is not armstrong.")