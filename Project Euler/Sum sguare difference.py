# Problem 6: Sum square difference

# Deze zinnen beschrijven een wiskundige berekening.
# De eerste zin zegt dat je de kwadraten van de eerste tien natuurlijke getallen moet optellen.
# De tweede zin zegt dat je de eerste tien natuurlijke getallen moet optellen en het resultaat moet kwadrateren.
# De derde zin zegt dat je het verschil tussen de som van de kwadraten van de eerste tien natuurlijke getallen en het kwadraat van de som moet vinden.
# De vierde zin vraagt om hetzelfde te doen voor de eerste honderd natuurlijke getallen.

natural_numbers_1_10_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum_squares_1_10 = 0
for i in range(1, 11):
    square_i = i**2
    sum_squares_1_10 += square_i
print(sum_squares_1_10)

sum_i = 0
square_sum_1_10 = 0
for i in range(1, 11):
    sum_i += i
square_sum_1_10 = sum_i**2
print(square_sum_1_10)
difference1 = square_sum_1_10 - sum_squares_1_10
print(difference1)

sum_squares_1_100 = 0
for i in range(1, 101):
    square_i = i**2
    sum_squares_1_100 += square_i
print(sum_squares_1_100)

sum_i = 0
square_sum_1_100 = 0
for i in range(1, 101):
    sum_i += i
square_sum_1_100 = sum_i**2
print(square_sum_1_100)
difference2 = square_sum_1_100 - sum_squares_1_100
print(difference2)
