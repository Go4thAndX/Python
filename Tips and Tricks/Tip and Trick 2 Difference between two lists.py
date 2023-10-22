# Tip and Trick 2: Get the difference between the two Lists

# Let’s say you have the following two lists.

list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
list2 = ['Scott', 'Eric', 'Kelly']

# If you want to create a third list from the first list which isn’t present in the second list. So you want output like this list3 = [ 'Emma', 'Smith]

# Let see the best way to do this without looping and checking. To get all the differences you have to use the set’s symmetric_difference operation.

list1 = ['Scott', 'Eric', 'Kelly', 'Emma', 'Smith']
list2 = ['Scott', 'Eric', 'Kelly']

set1 = set(list1)
set2 = set(list2)

list3 = list(set1.symmetric_difference(set2))
print(list3)