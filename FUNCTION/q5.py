'''Pangram is a sentence that uses every letter of the alphabet. Write a program to check whether
 a given string is pangram or not, through a user-defined function ispangram(). Test the
 function with “The quick brown fox jumps over the lazy dog” or “Crazy Fredrick bought many very
 exquisite opal jewels”. Hint: use set() to convert the string into a set of characters present in 
the string and use <= to check whether alphaset is a subset of the given string.'''
import string


def ispangram(s):
    #set of alphabet 
    alphabet = set(string.ascii_letters)
    return alphabet<=set(s.lower())

sample=["The quick brown fox jumps over the lazy dog","Crazy Fredrick bought many very exquisite opal jewels"]

for ele in sample:
    result = ispangram(ele)
    print(result)
    

