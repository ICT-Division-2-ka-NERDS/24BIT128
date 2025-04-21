"""A list contains some negative and some positive values. Write a recursive function that sanitizes the 
list by replacing all negative numbers with 0."""

def sanitize_list(l1):
    if l1 == [] :
        return []
    else:
        if l1[0]<0:
            mark = 0
        else :
            mark = l1[0]
        return [mark] +sanitize_list(l1[1:])
       
        
    
list1=[-1,-1,1,1]
result=sanitize_list(list1)
print(result)