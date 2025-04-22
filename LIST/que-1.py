L1 = [11,5,9,15,21]
L2 = [8,10,2,22]
L1[2] = L2
print("new L1 :",L1)
L3 = L1[0:2] + L2[:] + L1[3:]
print("Flatterned L3 :",L3)
L3.sort()
print("Sorted L3 :",L3)