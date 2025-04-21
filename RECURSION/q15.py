"""Write a recursive function that reverses the list of numbers that it receives."""

def reverses_list(l1):
    if len(l1)<=1:
        return l1
    else:
        return reverses_list(l1[1:])+[l1[0]]
    
l1=[1,2,3,4,5,6,7,8]
result=reverses_list(l1)
print(result)
    