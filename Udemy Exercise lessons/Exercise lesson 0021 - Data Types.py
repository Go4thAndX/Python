
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
# Eigenlijk zou je nog moeten testen of er werkelijk een getal bestaande uit 2 cijfers als input gegeven wordt

str_fst_two_digit_number = two_digit_number[0]
str_snd_two_digit_number = two_digit_number[1]

int_fst_two_digit_number = int(str_fst_two_digit_number)
int_snd_two_digit_number = int(str_snd_two_digit_number)

sum_two_digit_number = int_fst_two_digit_number + int_snd_two_digit_number

str_sum_two_digit_number = str(sum_two_digit_number)

# print(str_fst_two_digit_number + " + " + str_snd_two_digit_number + " = " + str_sum_two_digit_number)
print(sum_two_digit_number)