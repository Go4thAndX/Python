# Tip and Trick 8: Convert Byte to String

# To convert the byte to string we can decode the bytes object to produce a string. You can decode in the charset you want.

byteVar = b"pynative"
str = str(byteVar.decode("utf-8"))
print("Byte to string is" , str )

# Output:

# Byte to string is pynative