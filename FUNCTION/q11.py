"""Write a function create_list() that creates and returns a list which is an intersection of two
 lists passed to it."""

def create_list(l1,l2):
    return list(set(l1)&set(l2))

list1=[1,2,3,4,5]
list2=[3,4,5]

result=create_list(list1,list2)
print(result)