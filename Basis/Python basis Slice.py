# Slice function

# Voorbeelden van de slice-functie in Python:

# 1. Lijst elementen knippen:

lijst = [1, 2, 3, 4, 5, 6] 
nieuwe_lijst = lijst[2:5] 
print(nieuwe_lijst) 

# Output:
# [3, 4, 5]

# 2. Tekenreeks knippen:

tekst = "Hallo, ik ben een tekenreeks" 
nieuwe_tekst = tekst[7:13] 
print(nieuwe_tekst)

# Output:
# "ik ben"

# slice = [start:stop:step]

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
y = ["hi", "Hello", "goodbye", "cee ya", "Sure",]
s = "Hello World!"

sliced = x[0: 5: 2]
print(sliced)

# Output:
# [0, 2, 4]

sliced = y[3: 0: -2]
print(sliced)

# Output:
# ['cee ya', 'Hello']

# Wat een handige toepassing is van de slice functie is het omkeren van een lijst

sliced = x[::-1]
print(sliced)

# Output:
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Maar het werkt ook met een string
sliced = s[::-1]
print(sliced)

# Output:
# !dlroW olleH

sliced = s[::2]
print(sliced)

# Output:
# HloWrd