with open("que-6_Input(1).txt","r+") as f:
    data1 = f.readlines()
with open("que-6_Input(2).txt","r+") as p:
    data2 = p.readlines()
with open("que-6_Output.txt","w+") as q:
    data3 = []
    n = data1 if data1 >= data2 else data2
    m = data1 if data1 < data2 else data2
    for i in range(len(m)):
        data3.append(n[i][:-1] + " " + m[i])
        q.write(n[i][:-1] + " " + m[i])
    for i in range(len(m),len(n)):
        data3.append(n[i])
        q.write(n[i])