# Tip and Trick 13: Format a decimal to always show 2 decimal places

# Let say you want to display any float number with 2 decimal places. For example 73.4 as 73.40 and 288.5400 as 88.54.

number= 88.2345
print('{0:.2f}'.format(number))

# Output:

# 88.23