"""Write a program that defines a function count_alpha_digits() that accepts a string and calculates the
 number of alphabets and digits in it. It should return these values as a dictionary.
"""

def count_alpha_digits(s):
    result={"digit":0,"Alphabate":0}
    for ele in s:
        if ele.isdigit():
            result["digit"]+=1
        elif ele.isalpha():
            result["Alphabate"]+=1
        else :
            continue
    return result

line="My password is SunShine123 and my room number is B7"
result=count_alpha_digits(line)
print(result)


