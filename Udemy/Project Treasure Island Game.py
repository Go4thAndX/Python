'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

input_direction = input("\nTo find the treasure you first have to choose the right direction left or right. So choose wise !!!\n Answer with the letter (l) for Left or the letter (r) for Right ? ")
if input_direction != "l":
  print("\nSorry the wrong choice, you felt into a deep hole and died.\n Game over !!! Please try again and have more luck this time ???")
else:  
  input_choice = input("\nGood choise. you chose the right direction, to find the treasure you now have to make a second choice, you have to decide to go for a swim in the sea or wait a little longer on the island. Again choose wise !!!\n Answer with the letter (s) for Swim or the letter (w) for Wait ? ")
  if input_choice != "w":
    print("\nSorry the wrong choice, the sea is invested with men-eating sharks and they loved you.\n Game over !!! Please try again and have more luck this time ???")
  else:
    input_color = input("\nGood choise. After waiting for a little while you have the view of the sea in front of you and now have to walk to the right and follow the beach until you reach a place with three doors with different colors, red, blue and green. The treasure is behind one of these coloured doors. So choose a wise color !!!\n Answer with the letter (r) for Red, (b) for Bleu or (g) for Green ? ")    
    if input_color == "r":  
      print("\nYou were so close but you chose the wrong color door, this room is intoxicated with HydroSulfide gas and the door is closed behind you, you will get poisend and die.\n Game over !!! Please try again and have more luck this time ???")
    elif input_color == "b":
      print("\nYou were so close but you chose the wrong color door, the room temperature is far below zero degree Celsius and the door is closed behind you, you will freeze and die.\n Game over !!! Please try again and have more luck this time ???")
    elif input_color == "g":  
    # If you want to use multiple sets of quotes inside a single string, you might have to "escape" some of them using the backslash `\`. You can see this in my first sentence: 'You\'re at a crossroad...'.
      print("\nYou found the treasure, it\'s inside the box. The door is closed behind you but use the key inside the box to open the door and you are back on this beautiful island and still alive !!!\n Congratulations You win !!!")
    else:
      print("\nYou didn\'t follow the instructions and therefore you didn\'t find the treasure.\n Game Over !!! Please try again and have more luck this time ???")

