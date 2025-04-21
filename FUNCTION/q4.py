'''Write a program that defines a function sum_avg() to accept
 marks of five subjects and calculates total and average. It should return directly both values.'''

def sum_avg(s1,s2,s3,s4,s5):
    total = s1+s2+s3+s4+s5
    average= (total)/5
    return total,average

#assume marks of subject and give argument

total_average = sum_avg(30,40,26,44,44)
print(total_average)