names = [("B1","B2","B3"),"G1","G2",("B4",),"G3"]
boys = 0
girls = 0
for ele in names:
    if isinstance(ele,tuple):
        boys += len(ele)
    else :
        girls += 1
print("Boys :",boys)
print("Girls :",girls)