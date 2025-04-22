num = int(input("Enter number : "))
breaker = True
count = 2
if num == 0 or num == 1:
    breaker = False
elif num > 1:
    while breaker == True and count <= num**(1/2):
        if num % count == 0:
            breaker = False
        count = count + 1
else :
    print("Enter positive number.")
if breaker == False:
    print("Number is not prime.")
else:
    print("Number is prime.")