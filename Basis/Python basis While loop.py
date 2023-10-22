# While loop

i = 0
while i < 5:
    print(f"Loop fst: {i}")
    i += 1
print("\n")
    
i = 0
while True:
    print(f"Loop sec: {i}")
    i += 1
    
    if i == 5:
        break   