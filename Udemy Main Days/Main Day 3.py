'''
# Section 3: Day 3

# 29. Control Flow with if / else and Conditional Operators

# Hier gaan we gebruik maken van de zogenaamde "Als(if) Anders(else)" constructie waarbij het heel belangrijk is om te letten op het "inspringen" (indentation) want alle code binnen de inspringing wordt gezien als een blok code, is de inspringing niet in orde dan veroorzaken we een zogenaamde IndentationError:

# Deze drie code regels worden gebruikt in alle hierna volgende voorbeelden van het gebruik van if elif else statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

# Hier testen we een zogenaamde vergelijkende operator ( Comparison Operator ) if y > z: ( Als(if) y groter is als z dan: Anders(else):)
# if height > 120:
#   print("You can ride the rollercoaster !")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# Hier testen we if y >= z: ( Als(if) y groter of gelijk is als z dan: Anders(else): )
# if height >= 120:
#   print("You can ride the rollercoaster !")
# else:
#   print("Sorry, you have to grow taller before you can ride.")

# Hier testen we if y == z: ( Als(if) y gelijkwaardig(equal) is aan z dan: Anders(else): )
if height == 120:
  print("You can ride the rollercoaster !")
else:
  print("Sorry, you are not the right height to ride.")

# We gebruiken voornamelijk de volgende vergelijkende operatoren
# if y > z: ( Als(if) y groter is als z dan: )
# if y < z: ( Als(if) y kleiner is als z dan: )
# if y >= z: ( Als(if) y groter of gelijk is als z dan: )
# if y <= z: ( Als(if) y kleiner of gelijk is als z dan: )
# if y == z: ( Als (if) y is z (gelijkwaardig aan) dan: )
# if y != z: ( Als (if) y niet z is ("niet" gelijkwaardig aan) dan: )
# Dit is een toekenning(assignment) y = z
# Dit is een gelijkwaardigheids test(equality check) y == z

# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division. For example:
# 6 ÷ 2 = 3 with no remainder.
# therefore: 6 % 2 = 0
# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.
# therefore: 5 % 2 = 1
# 14 ÷ 4 = 3 x 4 + 2, remainder is 2.
# therefore: 14 % 4 = 2

# 31. Nested if statements and elif statements
# 
# Hier gaan we gebruik maken van een "geneste(nested)" "Als(if) Anders(else)" en we gaan deze uitbreiden met de mogelijkheid om binnen de "if else" extra condities te evalueren met de zogenaamde "AndersAls(elif)" constructie.
# waarbij het weer heel belangrijk is om te letten op het "inspringen" (indentation).
if height >= 120:
  print("You can ride the rollercoaster !")
  age=int(input("What is your age ? "))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  elif age <= 60:
    print("Please pay $12.")
  else:
    print("Please pay $10.")
else:
  print("Sorry, you have to grow taller before you can ride.")


# 34. Multiple If Statements in Succession

if height >= 120:
  print("You can ride the rollercoaster !")
  age=int(input("What is your age ? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age <= 60:
    bill = 12
    print("Adult tickets are $12.")
  else:
    bill = 10
    print("Senior tickets are $10.")

  wants_photo = input("Do you want to purchase the photo taken for an additional $3 ? Y(es) or N(o) ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")  
   
else:
  print("Sorry, you have to grow taller before you can ride.")
'''

# 36. Logical Operators

'''
In de volgende code gaan we voorwaardelijke condities (logical operators) gebruiken in dezelfde code regel, de drie belangrijkste voorwaardelijke condities zijn: "and(en)", "or(of)"" en "not(niet").

condition_first en(and) condition_second:
Als beide voorwaarden waar(True) zijn dan is aan de conditie voldaan en is de conditie waar(True)
Als een van de voorwaarden onwaar(False) is dan is niet aan de conditie voldaan en is de conditie onwaar(False)
Als beide voorwaarden onwaar(False) zijn dan is niet aan de conditie voldaan en is de conditie onwaar(False)

condition_first of(or) condition_second:
Als een van de voorwaarden waar(True) is dan is aan de gehele conditie voldaan en is de conditie waar(True)
Als beide voorwaarden waar(True) zijn dan is aan de conditie voldaan en is de conditie waar(True)
Als beide voorwaarden onwaar(False) zijn dan is niet aan de conditie voldaan en is de conditie onwaar(False)

not condition:
Als de voorwaarde waar(True) is dan wordt de voorwaarde onwaar(False)
Als de voorwaarde onwaar(False) is dan wordt de voorwaarde waar(True)

if height >= 120:
  print("You can ride the rollercoaster !")
  age=int(input("What is your age ? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 50:
    bill = 0
    print("Such a hard age, tickets are for free.")
  elif age <= 60:
    bill = 12
    print("Adult tickets are $12.")
  else:
    bill = 10
    print("Senior tickets are $10.")
    
  if age >= 45 and age <= 50:
    bill += 0
    print("And the picture taken is also free.")
  else:
    wants_photo = input("Do you want to purchase the photo taken for an additional $3 ? Y(es) or N(o) ")
    if wants_photo == "Y":
      bill += 3
  
  print(f"Your final bill is ${bill}")  
   
else:
  print("Sorry, you have to grow taller before you can ride.")
'''