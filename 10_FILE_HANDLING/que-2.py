with open("que-2_Input.csv","r+") as p:                    # Create dictionary before adding Totle
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
    print(d,"\n")

with open("que-2_Output.csv","w+") as f:                       # Adding Totle
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
        
with open("que-2_Output.csv","r+") as q:                  # Create dictionary after adding Totle
    data2 = q.readlines()
    data3 = []
    d = {}
    for ele in data2:
        data3.append(ele.split(","))
    for i in range(len(data3)):
        data3[i][len(data3[i]) - 1] = data3[i][len(data3[i]) - 1][:-1]
    for i in range(len(data3[0])):
        l = []
        for j in range(1,len(data3)):
            l.append(data3[j][i])
        d[data3[0][i]] = l
    print(d)