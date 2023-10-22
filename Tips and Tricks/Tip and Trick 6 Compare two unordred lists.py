# Tip and Trick 6: How to efficiently compare two unordered lists

# Let say you have two lists that contain the same elements but the elements order is different in both the list. For example,

one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]

# The above two lists contains the same elements only their order is different. Let see how we can find if the two lists are identical.

# We can use the [collections.Counter] method if our object is hashable.
# We can use [sorted()] if objects are orderable.

from collections import Counter

one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]

print("These two list are equal is:  ", Counter(one) == Counter(two))

# Output:

# 'These two list are equal is: ', True