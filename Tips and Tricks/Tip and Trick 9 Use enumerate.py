# Tip and Trick 9: Use enumerate

# Use enumerate() function when you want to access the list element and also want to keep track of the list items’ indices.

listOne = [123, 345, 456, 23]
print("Using enumerate")
for index, element in enumerate(listOne): 
    print("Index [", index,"]", "Value", element)
    
# Output:

# Using enumerate
# Index [ 0 ] Value 123
# Index [ 1 ] Value 345
# Index [ 2 ] Value 456
# Index [ 3 ] Value 23    