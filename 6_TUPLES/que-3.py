t1 = (15,5,2025)
t2 = (28,3,2023)
leap = [31,29,31,30,31,30,31,31,30,31,30,31]
nonleap = [31,28,31,30,31,30,31,31,30,31,30,31]
days = 0

def leap_year(yr):
    if (yr % 400 == 0):
        return leap
    elif (yr % 4 == 0 and yr % 100 != 0):
        return leap
    else :
        return nonleap
    
days += leap_year(t2[1])[t2[1] - 1] - t2[0]
days += t1[0] - 1

for i in range(t2[1],12):
    days += leap_year(t2[2])[i]
for i in range(t1[1] - 1):
    days += leap_year(t1[2])[i]

for i in range(t2[2] + 1, t1[2]):
    days += 365 if leap_year(i) == "nonleap" else 366

print("Days between two dates is :",days)