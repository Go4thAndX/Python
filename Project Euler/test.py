import time

original = 600851475143
option = original - 50
start = original - 10
end = start + 10

for i in range(5):
    for i in range(start, end):
        if i != end - 1:
            print(i, end=" ")
        else:
            print(i)
    if i == option:
        break
    time.sleep(2)
    start -= 10
    end -= 10
