def fun(a,b):
    print("a+b :",a + b)
def disp(a,b):
    print("a*b :",a * b)
def msg(a,b):
    print("Message")
l = [fun, disp, msg]

for f in l:
    f(1,2)