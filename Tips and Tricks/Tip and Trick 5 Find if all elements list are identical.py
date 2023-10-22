# Tip and Trick 5: Find if all elements in a list are identical

# Count the occurrence of a first element. If it is the same as the length of a list then it is clear that all elements are the same.

listOne = [20, 20, 20, 20]
print("All element are duplicate in listOne", listOne.count(listOne[0]) == len(listOne))

listTwo = [20, 20, 20, 50]
print("All element are duplicate in listTwo", listTwo.count(listTwo[0]) == len(listTwo))

# Output:

# 'All element are duplicate in listOne', True
# 'All element are duplicate in listTwo', False