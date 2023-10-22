# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# We are not allowed to use the max() or min() function

# Het eerste nummer in de lijst wordt het hoogste nummer
highest_number = student_scores[0]

# Loop door alle nummers van de lijst heen
for student_score in student_scores:
    # controleer of deze student_score hoger is dan de actuele higest_number
    if student_score > highest_number:
        # Als dat waar(True) dan wordt deze student_score de highest_number
        highest_number = student_score

# nadat de hele lijst is doorlopen, zal de hoogste student_score als waarde zijn opgeslagen als highest_number
print(f"The highest score in the class is: {highest_number}")