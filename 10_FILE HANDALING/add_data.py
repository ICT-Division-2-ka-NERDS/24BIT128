with open ("D:\Book1.csv","r+") as p:
    data = p.readlines()
with open("D:\\Book2.csv","w+") as f:
    data1 = []
    for ele in data:
        data1.append(ele.split(","))
    data1[0][5] = data1[0][5][:-1]
    n = int(input("How many students are you want to add? :"))
    for i in range(n):
        l = []
        for j in range(6):
            l.append(input(str("Enter " + data1[0][j] + " :")))
            if (j == 5):
                l[j] += "\n"
        data1.append(l)
    data1[0][5] += "\n"
    for ele in data1:
        f.write(','.join(ele))