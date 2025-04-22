d = {"E1":("A",101,25000),"E2":("B",102,30000),"E3":("A",103,25500),"E4":("C",104,28850),"E5":("A",105,24500)}
la, lb, lc = [], [], []
dept = []
i, j, k = 0, 0, 0
for k,v in d.items():
    if (v[0] == "A"):
        la.append(v[2])
    elif (v[0] == "B"):
        lb.append(v[2])
    else :
        lc.append(v[2])
print("Max.and Min. salary in department A is :",max(la),min(la))
print("Max. and Min. salary in department B is :",max(lb),min(lb))
print("Max. and Min. salary in department C is :",max(lc),min(lc))