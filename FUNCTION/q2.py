'''
Write a program that defines a function compute() that calculates the value of n + nn + nnn + nnnn, 
where n is digit received by the function. test the function for digits 4 to 7.'''

def compute(n):
    a= str(n)
    n1 = n
    n2 = int(a*2)
    n3 = int(a*3)
    n4 = int(a*4)
    return n1+n2+n3+n4
   
    
for ele in range(4,8):
 
    print(f"compute({ele})=",compute(ele))