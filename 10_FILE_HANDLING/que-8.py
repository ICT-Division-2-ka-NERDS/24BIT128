with open("que-8_Input.txt","r+") as f:
    data = f.readlines()
with open("que-8_Output.txt","w+") as p:
    data1 = []
    articles = [" a ", " an ", " the "]
    for ele in data:
        for article in articles:
            ele = ele.replace(article," ")
        p.write(ele)