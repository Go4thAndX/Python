# Tip and Trick 14: Return multiple values from a function

def multiplication_Division(num1, num2):
  return num1 * num2, num2 / num1

product, division = multiplication_Division(10, 20)
print("Product", product, "Division", division)

# Output:

# Product 200 Division 2.0