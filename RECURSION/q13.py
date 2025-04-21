"""A positive integer is entered through the keyboard. Write a function to find its binary equivalent of 
this number.
"""
def binary_number(n):
    if n==0:
        return ""
    else :
        return binary_number(n//2)+str(n%2)
    
result=binary_number(5)
print(result)