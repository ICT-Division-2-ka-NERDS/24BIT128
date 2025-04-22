with open ("D:\Book1.csv","r+") as p:
    data = p.readlines()
with open("D:\\Book2.csv","w+") as f:
    data1 = []
    for ele in data:
        data1.append(ele.split(","))
    for i in range(len(data1)):
        data1[i][len(data1)] =  data1[i][len(data1)][:-1]
    data1[0].append("Total\n")
    for i in range(1,len(data1)):
        sum = 0
        for j in range(3,len(data1[i])):
            sum += int(data1[i][j])
        data1[i].append(str(sum) + "\n")
    for ele in data1:
        f.write(','.join(ele))