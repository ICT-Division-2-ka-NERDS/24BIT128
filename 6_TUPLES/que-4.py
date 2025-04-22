l = [("Gulabjamun",15),("Kajukatri",50),("kalajam",30)]
l1 = []
l2 = []
for ele in l:
    l1.append(ele[1])
    
l1.sort(reverse = True)

for i in range(len(l1)):
    for j in range(len(l)):
        if (l[j][1] == l1[i]):
            l2.append(l[j])
            break
print(l2)