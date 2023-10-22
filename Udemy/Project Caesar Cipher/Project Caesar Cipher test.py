# Project Caesar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
text_plain = "h ello"
len_text_plain = len(text_plain)
shift_amount = 5
encode = True
cipher_text = ""

for i in range(0, len_text_plain):

    if text_plain[i] in alphabet:
        print(text_plain[i])
        
        alphabet_index = 0

        while alphabet[alphabet_index] != text_plain[i]:
            alphabet_index += 1

            if encode:
                alphabet_index += shift_amount
        string_letter = alphabet[alphabet_index]
        cipher_text += string_letter
        i += 1
    else:
        print("not in alphabet")

print(f"The text is {cipher_text}")    
    
