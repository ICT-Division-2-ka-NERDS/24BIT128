t1 = ("Hello","PDPU","ICT")
a = int(input("Enter index element which you want to delet : "))
for i in range(a):
    t2 = (t1[i],)
for i in range(a+1,len(t1)):
    t3 = (*t2,t1[i])
print(t3)