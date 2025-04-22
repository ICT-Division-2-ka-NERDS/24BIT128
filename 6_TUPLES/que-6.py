t1 = ("Hello","PDPU","ICT")
print(t1)
a = int(input("Enter index of element which you want to change? : "))
b = input("Enter new value : ")
for i in range(a):
    t2 = (t1[i],)
t3 = (*t2,b)
for i in range(a+1,len(t1)):
    t4 = (*t3,t1[i])
print(t4)