l = input("Enter names :").split(" ")
s = {ele for ele in l}
print(s)
a = input("Which element would you like to delet? :")
s.remove(a)
s.update([input("Enter new element :")])
print(s)