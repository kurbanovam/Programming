#!/usr/bin/python3
import turtle

turtle.shape('turtle')
side=20
for i in range(10):
    for j in range(4):
        turtle.forward(side)
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)
    turtle.pendown()
    side = side + 20
turtle.done()
