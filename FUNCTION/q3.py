'''Write a program that defines a function create_array()
 to create and return a 3D array whose dimensions are passed to the function. Also initialize 
each element of this aray to a value passed to the function. e.g. create_array(3,4,5,n) where 
first three arguments are 3D array dimensions and 4th value is for initialing each value of the 3D array.'''

def create_array(depth,row,columns,value):
    return [[[value for ele in range(columns)]for ele in range(row)]for ele in range(depth)]
arr = create_array(3,4,5,5)
print(arr)
#for better view
for depth in arr:
    for row in depth:
        print(row)

    print()



    