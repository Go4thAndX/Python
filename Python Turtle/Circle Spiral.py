# Python program to demonstrate
# spiral circle drawing


import turtle

t = turtle.Turtle()

# taking radius of initial radius
r = 10

# Loop for printing spiral circle
for i in range(100):
    t.circle(r + i, 45)

turtle.mainloop()
