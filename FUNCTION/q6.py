'''Write a function to create and return a list
 containing tuples of the form (x,x2,x3) for all x between 1 and given ending value (both inclusive).'''

def create_list(s):
    req_list = []
    for ele in range(1,2):
        
        for i in range(1,s+1):
              
           new_tuple=(i,i**2,i**3)
           req_list.append(new_tuple)
        return req_list

ans = create_list(3)
print(ans)




