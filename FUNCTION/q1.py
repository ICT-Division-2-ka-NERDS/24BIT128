'''Write a program that defines a function count_lower_upper() that accepts a string and
calculates the number of uppercase and lowercase alphabets in it. It should 
return these values as a dictionary. Call this function for some sample string.'''

def count_lower_upper(s):
    count_dict={"Lower":0,"Upper":0}
    for ele in s:
        if ele.islower():
            count_dict["Lower"]+=1
        elif ele.isupper():
            count_dict["Upper"]+=1

    return count_dict

name = "SAhil Prajapati"
number = count_lower_upper(name)
print("number of upper and lower case are as follows",number)

   
