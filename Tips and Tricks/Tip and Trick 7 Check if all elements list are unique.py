# Tip and Trick 7: How to check if all elements in a list are unique

# Let say you want to check if the list contains all unique elements or not.

def isUnique(item):
    tempSet = set()
    return not any(i in tempSet or tempSet.add(i) for i in item)

listOne = [123, 345, 456, 23, 567]
print("All List elements are unique is: ", isUnique(listOne))

listTwo = [123, 345, 567, 23, 567]
print("All List elements are unique is: ", isUnique(listTwo))

# Output:

# All List elements are unique is:  True
# All List elements are unique is: False