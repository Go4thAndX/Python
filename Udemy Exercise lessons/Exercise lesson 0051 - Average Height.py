# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

# We are not allowed to use the sum() and len() funtion

# total_height = sum(student_heights)
# print(total_height)
# average_height = total_height / len(student_heights)
# print(average_height)
sum_height = 0
sum_loop = 0
for student_height in student_heights:
    sum_height += student_height
    sum_loop += 1 
# print(sum_height)
# print(sum_loop)
average_height = round(sum_height / sum_loop)
print(average_height)





