# draw color filled circle in turtle

import turtle

# creating turtle pen
t = turtle.Turtle()

# taking input for the radius of the circle
r = int(input("Enter the radius of the circle: "))

# taking the input for the color
col = input("Enter the color name or hex value of color(# RRGGBB): ")

# set the fillcolor
t.fillcolor(col)

# start the filling color
t.begin_fill()

# drawing the circle of radius r
t.circle(r)

# ending the filling of the color
t.end_fill()

turtle.mainloop()
