# For loop

for i in range(10):
    print(i)
    
# Output:
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
    
# range is een function die een verzameling nummers genereert gebaseerd op de input die we het geven en bestaat uit de "start", "stop" en "step" waardes.
# Als we maar 1 argument gebruiken dan is dat automatisch de "stop" waarde, die altijd begint bij 0 en stopt bij waarde die we ingeven, exclusief die waarde.
# Als we 2 argumenten gebruiken dan zijn dat de "start" en "stop" waardes, die altijd begint bij de "start" waarde, inclusief die waarde en stopt bij de "stop" waarde, exclusief deze waarde.
# Als we 3 argumenten gebruiken dan geeft de laatste waarde de "step" grootte aan met hoeveel we de waarde per stap verhogen, dit kan ook een negatieve waarde zijn.

for i in range(10, -1, -1):
    print(i)
    
# Output
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
# 0
    
for i in [3, 4, 42, 8, 1, 12,]:
    print(i)
    
# Output:
# 3
# 4
# 42
# 8
# 1
# 12

x = [3, 4, 42, 8, 1, 12,]

for i in range(len(x)):
    print(i)
    
# Output:
# 0
# 1
# 2
# 3
# 4
# 5    

for i in range(len(x)):
    print(x[i])
    
# Output:
# 3
# 4
# 42
# 8
# 1
# 12
    
for i in range(len(x)):
    print(f"item {i} has value: {x[i]}")
    
# Output:
# item 0 has value: 3
# item 1 has value: 4
# item 2 has value: 42
# item 3 has value: 8
# item 4 has value: 1
# item 5 has value: 12

for i, element in enumerate(x):
    print(f"item {i} has value: {element}")
    
# Output:
# item 0 has value: 3
# item 1 has value: 4
# item 2 has value: 42
# item 3 has value: 8
# item 4 has value: 1
# item 5 has value: 12
