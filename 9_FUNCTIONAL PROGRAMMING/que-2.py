l1 = [1,2,3,4,5,6]
l2 = [6,5,4,3,2,1]
l = []
m = list(map((lambda i,j: i + j),l1,l2))
print(m)