d1 = {"names":("Jigar","Dhruv","Bhavik"),"fruits":("Banana","mango","apple")}
d2 = {"sweets":("Gulabjamun","Kalajam")}
d3 = {"numbers":(1,5,8,6,7),"alphabets":("a","b")}
d = {**d1,**d3,**d2}
print(d)
print(len(d1))