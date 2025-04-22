s = {"Arnav","Bhavik","Dhruv","Ary"}
s1 = {ele for ele in s if (ele[0] == "A" or ele[0] == "a")}
s2 = {ele for ele in s if (ele[0] == "B" or ele[0] == "b")}
print(s1)
print(s2)