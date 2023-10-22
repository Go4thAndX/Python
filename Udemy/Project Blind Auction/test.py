# naam_1 = "Jan"
# bedrag_1 = 123

# dict = {naam_1: bedrag_1}
# print(dict)

# naam_2 = "George"
# bedrag_2 = 321

# dict[naam_2] = bedrag_2
# print(dict)

dict = {}
meer_invoer = True
while meer_invoer:
    input_name = input("Wat is je naam ?: ")
    input_bedrag = int(input("Wat is je bedrag ?: $"))
    dict[input_name] = input_bedrag
    input_meer = input(
        "Wil je nog meer namen en bedragen invoeren ? Type 'ja' of 'nee': \n"
    )

    if input_meer != "ja":
        meer_invoer = False
print(dict)
