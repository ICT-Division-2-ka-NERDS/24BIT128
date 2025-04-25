with open("que-5_Input.txt","r+") as f:
    data = f.readlines()
with open("que-5_Output.txt","w+") as p:
    data1 = []
    for ele in data:
        data1.append(ele[:-1].upper() + "\n")
    for ele in data1:
        p.write(ele)