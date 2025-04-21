"""If a positive integer is entered through the keyword, write a recursive function to obtain the prime 
factors of the number.
"""

def prime_factor(n,i=2):
    if n==1:
        return []
    elif n%i==0:
        return [i]+prime_factor(n//i,i)
    else :
        return prime_factor(n,i+1)
    
result=prime_factor(21)
print(result)

