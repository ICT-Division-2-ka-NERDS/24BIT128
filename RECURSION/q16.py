"""Calculate a ** b where a and b received through the keyword using recursion."""

def power(a,b):
    if b==0:
        return 1
    else:
        return a*power(a,b-1)
    
result = power(10,2)
print(result)