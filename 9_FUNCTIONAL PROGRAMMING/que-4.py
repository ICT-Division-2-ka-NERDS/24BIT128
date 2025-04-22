lst = ['madam','Python',"malayalam","12321"]
def palindrome(l):
    for i in range(len(l) // 2):
        if (l[i] != l[len(l) - i -1]):
            return False
    return True
print(list(filter(palindrome,lst)))