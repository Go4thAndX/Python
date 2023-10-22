def test_function():
    x = "Aap"
    y = "Noot"

    return x, y


print(test_function())
# Output: ('Aap', 'Noot')
print(test_function()[0])
# Output: Aap
print(test_function()[1])
# Output: Noot
