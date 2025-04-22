d1 = {"names":("Jigar","Dhruv","Bhavik"),"fruits":("Banana","mango","apple")}
d2 = {"sweets":("Gulabjamun","Kalajam")}
d3 = {}
d4 = {"numbers":(1,5,8,6,7),"alphabets":("a","b")}
d5 = {}
l = [d1,d2,d3,d4,d5]

for i in range(len(l)):
    if (len(l[i]) == 0):
        print("Dictionary d",i+1,"is empty.")