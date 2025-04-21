""""A palindrome is a word or phrase that reads the same in both directions. Write a program that
 defines a function ispalindrome() which checks whether a given string is a palindrome or not.
   Ignore spaces and case mismatch while checking for palindrome
"""




def ispalindrome(s):
    s1=s.upper()
    s2=s1.replace(" ","")
    res2=s2[::-1]
    if s2== res2 :
        print("given string is palindrome")
    else:
        print("not palindrome")

name="Was it a car or a cat I saw"
ispalindrome(name)

name2="A man a plan a canal Panama"
ispalindrome(name2)

        



   
