# Tip and Trick 4: Removing duplicates items from a list

# Most of the time we wanted to remove or find the duplicate item from the list.  Let see how to delete duplicate from a list. The best approach is to convert a list into a set. Sets are unordered data-structure of unique values and don’t allow copies.

listNumbers = [20, 22, 24, 26, 28, 28, 20, 30, 24]
print("Original= ", listNumbers)

listNumbers = list(set(listNumbers))
print("After removing duplicate= ", listNumbers)

# Output:

# 'Original= ', [20, 22, 24, 26, 28, 28, 20, 30, 24]
# 'After removing duplicate= ', [20, 22, 24, 26, 28, 30]