"""Write a program that defines a function convert() that receives a string containing a sequence of
 whitespace separated words and returns a string after removing all duplicate words and sorting them
   alphanumerically. Hint: use set(), list () , sorted(), join().

"""

def convert(s):
    words = s.split()
    unique_words=set(words)
    sorted_words=sorted(unique_words)
    ans=' '.join(sorted_words)
    return ans 

s1="banana apple orange banana kiwi apple"
Result=convert(s1)
print(Result)



