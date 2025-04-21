"""Write a recursive function to obtain length of a given string."""


def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])

string1="sahilprajapati"
result=string_length(string1)
print(result)
