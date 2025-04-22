num = int(input("Enter a number : "))
i = num**(1/2)
if (num < 0):
    print("Invalid input. Enter positive number.")
elif ((i*10) == int(i)*10):
    print("Entered number is perfect square.")
else:
    print("Entered number is not perfect square.")