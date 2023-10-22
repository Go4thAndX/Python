# Project Caesar Cipher

'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text_plain, shift_amount):

# TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
        #e.g. 
        #text_plain = "hello"
        #shift_amount = 5
        #cipher_text = "mjqqt"
        #print output: "The encoded text is mjqqt"
    len_text_plain = len(text_plain)
    # num_shift = 5
    cipher_text = ""

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

    for i in range(0, len_text_plain):
        # Neem de eerste letter van de variabele [plain_text] en vergelijk deze met de eerste letter in de lijst [alphabet] als deze niet gelijk zijn vergelijk dan de eerste letter van de variabele [plain_text] met de volgende letter in de lijst [alphabet] en herhaal dit totdat ze wel gelijk zijn.
        alphabet_index = 0
        while alphabet[alphabet_index] != text_plain[i]:
            alphabet_index += 1
            # Neem nu de index van deze letter van de lijst [alphabet] en tel hier de waarde van de variabele [num_shift] bij op
        alphabet_index += shift_amount
        # Omdat het alfabet maar 26 letters kent zou bij een verschuiving waarbij alphabet_index groter dan 26 de code een probleem krijgen en omdat te ondervangen zorgen we dat de index na 26 weer bij 1 begint
        if alphabet_index > 25 :
            alphabet_index -= 25
        # Definieer de variabele [string_letter] en maak de variabele gelijk aan de letter van het alfabet met de verkregen index [alphabet[alphabet_index]  
        string_letter = alphabet[alphabet_index]
        # Voeg de waarde van de varibele [string_letter] toe aan de variabele [cipher_text]
        cipher_text += string_letter

    print(f"The encoded text is {cipher_text}")

text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
encrypt(text_plain = text, shift_amount = shift)

def encrypt(text_plain, shift_amount):
    len_text_plain = len(text_plain)
    cipher_text = ""
    for i in range(0, len_text_plain):
        alphabet_index = 0
        while alphabet[alphabet_index] != text_plain[i]:
            alphabet_index += 1          
        alphabet_index += shift_amount
        if alphabet_index > 25 :
            alphabet_index -= 25
        string_letter = alphabet[alphabet_index]
        cipher_text += string_letter
    print(f"The encoded text is {cipher_text}")

#TODO-4: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

#TODO-5: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
#e.g. 
#cipher_text = "mjqqt"
#shift = 5
#plain_text = "hello"
#print output: "The decoded text is hello"

#TODO-6: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.

def decrypt(text_plain, shift_amount):
    len_text_plain = len(text_plain)
    cipher_text = ""
    for i in range(0, len_text_plain):
        alphabet_index = 0
        while alphabet[alphabet_index] != text_plain[i]:
            alphabet_index += 1          
        alphabet_index -= shift_amount
        if alphabet_index < 0 :
            alphabet_index += 25
        string_letter = alphabet[alphabet_index]
        cipher_text += string_letter
    print(f"The decoded text is {cipher_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode":
    encrypt(text_plain = text, shift_amount = shift)
else:
    decrypt(text_plain = text, shift_amount = shift)
'''

#TODO-7: Combine the encrypt() and decrypt() functions into a single function called caesar_cypher().

def caesar_cypher(encode_decode, text_plain, shift_amount):
    len_text_plain = len(text_plain)
    cipher_text = ""

    for i in range(0, len_text_plain):
        alphabet_index = 0

        while alphabet[alphabet_index] != text_plain[i]:
            alphabet_index += 1
        
        if encode_decode == "encode":
            alphabet_index += shift_amount

            if alphabet_index > 25:
                alphabet_index -= 25
        else:
            alphabet_index -= shift_amount

            if alphabet_index < 0 :
                alphabet_index += 25

        string_letter = alphabet[alphabet_index]
        cipher_text += string_letter
    print(f"The {direction}d text is {cipher_text}")

#TODO-8: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

#TODO-9: Import and print the logo from art.py when the program starts.

#TODO-10: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

#TODO-11: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

# How to specificly locate if an item is "not" part of a list?
# You can use the "count" method to look for an item that is not part of a list, if the "count" method returns 0 the item is not part of the list
# For example:

# my_list = ["a", "b", "c"]
# number = my_list.count(" ")
# print(number)
# 
# Output:
# 0

def start():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if shift >= 25:
        shift = shift % 25 + 1

    caesar_cypher(encode_decode = direction, text_plain = text, shift_amount = shift)

#TODO-12: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

start()

answer = "yes"
while answer == "yes":
    answer = input("\nType 'Yes' if you want to go again. Otherwise type 'No'.\n")
    lowercase_answer = answer.lower()
    if answer == "yes":
        start()
    else:    
        print("The program has ended !!!")
        
# Kopieer de Udemy solution code naar de Caesar Cipher Udemy Solution.py 