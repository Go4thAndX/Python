# Lists

a = 10
b = 23
c = 25

print(a)
print(b)
print(c)
# Output:
# 10
# 23
# 25

list_l =[10, 23, 25]
print(list_l)
# Output:
# [10, 23, 25]

print(list_l[0])
# Output:
# 10

print(list_l[-1])
# Output:
# 25

list_l_1 = [13, "appeltaart", 1.25, True]
print(list_l_1)
# Output:
# [13, 'appeltaart', 1.25, True]

list_l_1[1] = "bosche bol"
print(list_l_1)
# Output:
# [13, 'bosche bol', 1.25, True]

list_l_1.append("pindakaas")
print(list_l_1)
# Output:
# [13, 'bosche bol', 1.25, True, 'pindakaas']

list_l_1.pop(3)
print(list_l_1)
# Output:
# [13, 'bosche bol', 1.25, 'pindakaas']

list_l_1.insert(1, False)
print(list_l_1)
# Output:
# [13, False, 'bosche bol', 1.25, 'pindakaas']
