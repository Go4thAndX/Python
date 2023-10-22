# Tip and Trick 1: How to measure the time elapsed to execute your code in Python

# Let’s say you want to calculate the time taken to complete the execution of your code. Using a time module, You can calculate the time taken to execute your code.

import time

startTime = time.time()

# write your code or functions calls

endTime = time.time()
totalTime = endTime - startTime

print("Total time required to execute code is= ", totalTime)