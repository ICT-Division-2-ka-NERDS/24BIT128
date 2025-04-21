"""A string is entered through the keyboard. Write a recursive function that counts the number of vowels
 in this string."""

def vowels_count(s):
    if s=="":
        return 0
    elif s[0] in "aeiouAEIOU":
        return 1+vowels_count(s[1:])
    else :
        return vowels_count(s[1:])
    
test_string="Hello World"
result=vowels_count(test_string)
print("no of vowels in string :",result)
    
    