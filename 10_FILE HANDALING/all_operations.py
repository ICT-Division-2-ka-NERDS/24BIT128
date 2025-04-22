with open ("D:\Book1.csv","r+") as p:
    data = p.readlines()
with open("D:\\Book2.csv","w+") as f:
    data1 = []
    d = {}
    for ele in data:
        data1.append(ele.split(","))
    data1[0][len(data1[0]) - 1] = data1[0][len(data1[0]) - 1][:-1]
    
    n = int(input("How many students are you want to add? :"))           # add new data
    for i in range(n):
        l = []
        for j in range(len(data1[0])):
            l.append(input(str(data1[0][j] + " :")))
            if (j == len(data1[0])):
                l[j] += "\n"
        data1.append(l)
    
    for i in range(1,len(data1)):                                        # remove \n
        if (i < len(data1) - n):
            data1[i][len(data1[i]) - 1] =  data1[i][len(data1[i]) - 1][:-1]
    data1[0].append("Total\n")                                           # add total
    for i in range(1,len(data1)):
        sum = 0
        for j in range(3,len(data1[i])):
            sum += int(data1[i][j])
        data1[i].append(str(sum) + "\n")
    
    for ele in data1:                                                    # write in new file
        f.write(','.join(ele))
        
    for i in range(len(data1)):                                          # remove \n
        data1[i][len(data1[i]) - 1] = data1[i][len(data1[i]) - 1][:-1]
    for i in range(len(data1[0])):                                       # creat dictionary d
        l = []
        for j in range(1,len(data1)):
            l.append(data1[j][i])
        d[data1[0][i]] = l
    print(d)