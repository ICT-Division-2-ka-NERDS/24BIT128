"""Write a program that defines a function called frequency() which computes the frequency of words present
 in a string passed to it. The frequencies should be returned in sorted order of words in the string.
"""
def frequency(s):
    frequency={}
    for char in s:
        if char.isalpha():
            char=char.lower()
            if char in frequency:
                frequency[char]+=1
            else:
                frequency[char]=1

    sorted_frequency=dict(sorted(frequency.items()))
    
    return sorted_frequency

#example

word = "Banana"
result=frequency(word)
print(result)    


