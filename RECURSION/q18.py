"""Write a recursive function to obtain average of all numbers present in a given list."""

def average_recursive(lst, index=0, total=0):
    if index == len(lst):
        return total / len(lst) if len(lst) > 0 else 0
    return average_recursive(lst, index + 1, total + lst[index])

list1=[1,2,3,4,5,6]
result=average_recursive(list1)
print(result)