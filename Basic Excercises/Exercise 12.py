# Exercise 12: Calculate income tax for the given income by adhering to the below rules

# For example, suppose the taxable income is 45000

# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20

# Expected Output:

# The payable income tax is: 10000*0% + 10000*10%  + 25000*20% = $6000.

# My solution:

def pay_income_tax(income, income_tax):
    if income > 20000:
        income_remain = income - 20000
        income_tax = income_remain * 20 / 100 + 1000
        print(f"The payable income tax is : 10000*0% + 10000*10% + {income_remain}*20% = ${int(income_tax)}")
    elif income > 10000 and income <= 20000:
        income_next = income - 10000
        income_tax = income_next * 10 /100
        print(f"The payable income tax is : 10000*0% + {income_next}*10% = ${int(income_tax)}")
    else:
        income_first = income
        income_tax
        print(f"The payable income tax is : {income_first}*0% = ${int(income_tax)}")

income = int(input("What is the income in dollars: "))
pay_income_tax(income, 0)

# Given solution:

income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    # no tax on first 10,000
    x = income - 10000
    # 10% tax
    tax_payable = x * 10 / 100
else:
    # first 10,000
    tax_payable = 0

    # next 10,000 10% tax
    tax_payable = 10000 * 10 / 100

    # remaining 20%tax
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)

        
