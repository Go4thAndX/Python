#  Strings

print("Hallo")
# Output:
# Hallo

tekst = "Pindakaas"
print(tekst)
# Output:
# Pindakaas

print(tekst + "is lekker")
# Output:
# Pindakaasis lekker

print(tekst + " is lekker")
# Output:
# Pindakaas is lekker

print(tekst[0])
# Output:
# P

print(tekst[5])
# Output:
# k

# print(tekst[12])
# Output:
# File "g:\Mijn Drive\GoogleMap Python\Python Algemeen\Strings.py", line 15, in <module>
#     print(tekst[12])
# IndexError: string index out of range

print(tekst[-1])
# Output:
# s

print(tekst[-3])
# Output:
# k
print(tekst[0:5])
# Output:
# a

print(tekst[-3:-1])
# Output:
# aa

x = len(tekst)
print(x)
# Output:
# 9

y = tekst.upper()
print(y, tekst)
# Output:
# PINDAKAAS Pindakaas

z = tekst.lower()
print(z, tekst)
# Output:
# pindakaas Pindakaas
