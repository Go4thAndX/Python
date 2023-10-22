# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lowercase = name1.lower()
name2_lowercase = name2.lower()
occur_t_true = name1_lowercase.count("t") + name2_lowercase.count("t")
occur_r_true = name1_lowercase.count("r") + name2_lowercase.count("r")
occur_u_true = name1_lowercase.count("u") + name2_lowercase.count("u")
occur_e_true = name1_lowercase.count("e") + name2_lowercase.count("e")
sum_occur_true = occur_t_true + occur_r_true + occur_u_true + occur_e_true
# print(sum_occur_true)

if sum_occur_true >= 9:
    sum_occur_true = 9

occur_l_love = name1_lowercase.count("l") + name2_lowercase.count("l")
occur_o_love = name1_lowercase.count("o") + name2_lowercase.count("o")
occur_v_love = name1_lowercase.count("v") + name2_lowercase.count("v")
occur_e_love = name1_lowercase.count("e") + name2_lowercase.count("e")
sum_occur_love = occur_l_love + occur_o_love + occur_v_love + occur_e_love
# print(sum_occur_love)

if sum_occur_love >= 9:
    sum_occur_love = 9

true_love_score = sum_occur_true * 10 + sum_occur_love
# print(true_love_score)

if true_love_score < 10 or true_love_score > 90:
    print(f"Your score is {true_love_score}, you go together like coke and mentos.")
elif true_love_score > 40 and true_love_score < 50:
    print(f"Your score is {true_love_score}, you are alright together.")
else:
    print(f"Your score is {true_love_score}.")

