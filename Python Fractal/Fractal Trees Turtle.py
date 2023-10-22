from turtle import *
from random import *

tree1 = Turtle()
tree2 = Turtle()
tree3 = Turtle()
tree4 = Turtle()
tree5 = Turtle()

x = -200
turtles = [tree1, tree2, tree3, tree4, tree5]

for t in turtles:
    t.speed(0)
    t.left(90)
    t_color = choice(['saddlebrown','sienna', 'chocolate', 'maroon'])
    t.color(t_color)
    t.pu()
    x += randint(80, 160)
    t.goto(x, randint(-100, 100))
    t.pd()

def branch(turt, branch_len):
    angle = randint(20, 30)
    shrink_factor = uniform(0.6, 0.9)
    size = int(branch_len / 10)
    turt.pensize(size)
    
    if branch_len < 20:
        leaf_color = choice(['green', 'dark green', 'forest green', 'green yellow', 'lime green', 'lime', 'olive drab'])
        turt.color(leaf_color)
        turt.stamp()
        branch_color = choice(['chocolate', 'brown', 'saddle brown', 'sienna', 'peru', 'burlywood', 'tan'])
        turt.color(branch_color)        
        
    if branch_len > 10:
        turt.forward(branch_len)
        turt.left(angle)
        branch(turt, branch_len * shrink_factor)
        turt.right(angle * 2)
        branch(turt, branch_len * shrink_factor)
        turt.left(angle)
        turt.backward(branch_len)        

for t in turtles:
    branch(t, 100)
