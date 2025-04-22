yr = int(input("Enter a year : "))

if yr%400 == 0:
    print("Entered year is leap year.")
elif yr%4 == 0 and yr%100 != 0:
    print("Entered year is leap year.")
else:
    print("Entered year is not leap year.")