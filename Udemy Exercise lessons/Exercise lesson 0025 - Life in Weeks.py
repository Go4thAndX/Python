# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# input string: huidige leeftijd ?
# maak van de str een int
int_age = int(age)
# verwachte jaren nog te leven = 90 - huidige leeftijd
exp_years=90-int_age 
# verwachte maanden nog te leven = afgeronde(verwachte jaren nog te leven * 12)
exp_months=round(exp_years*12)
# verwachte weken nog te leven = afgeronde(verwachte jaren nog te leven * 52)
exp_weeks=round(exp_years*52)
# verwachte dagen nog te leven = afgeronde(verwachte jaren nog te leven * 365)
exp_days=round(exp_years*365)
# output f-string: You have  days,  weeks, and  months left.
print(f"You have {exp_days} days, {exp_weeks} weeks, and {exp_months} months left.")
