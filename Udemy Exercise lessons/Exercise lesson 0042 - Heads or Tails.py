#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random
random_integer_0_1 = random.randint(0, 1)
# print(random_integer_0_1)
if random_integer_0_1 == 0:
    print("Tails")
else:
    print("Heads")
