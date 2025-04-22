with open("D:\Book1.csv","r+") as p:
    data = p.readlines()
    data1 = []
    d = {}
    for ele in data:
        data1.append(ele.split(","))
    
    for i in range(len(data1)):
        data1[i][len(data1[i]) - 1] = data1[i][len(data1[i]) - 1][:-1]
        
    for i in range(len(data1[0])):
        l = []
        for j in range(1,len(data1)):
            l.append(data1[j][i])
        d[data1[0][i]] = l
    print(d)