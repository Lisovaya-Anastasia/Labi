import turtle
import math

R = 80  #  radius of the face
n = 100  # the "accuracy"
r = 10  #  radius of the eye
l = 10  #  lenght of the nose
P = 20  #  radius of the acr of the smale
pi = 3.1415


def circle(R):
    l = 2 * R * math.cos(pi * (n - 2) / (2 * n))
    for i in range(n):
        turtle.forward(l)
        turtle.left(360 / n)


def arc(R):
    l = 2 * R * math.cos(pi * (n - 2) / (2 * n))
    for i in range(n // 2):
        turtle.forward(l)
        turtle.right(360 / n)


turtle.width(2)

turtle.penup()
turtle.goto(0, -R)
turtle.pendown()
turtle.begin_fill()
circle(R)
turtle.color("yellow")
turtle.end_fill()

turtle.penup()
turtle.goto(-4 * r, 2 * r)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
circle(r)
turtle.color("blue")
turtle.end_fill()

turtle.penup()
turtle.goto(4 * r, 2 * r)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
circle(r)
turtle.color("blue")
turtle.end_fill()

turtle.width(10)

turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.color("black")
turtle.right(90)
turtle.forward(r / 2)

turtle.penup()
turtle.goto(P, -R / 2)
turtle.pendown()
turtle.color("red")
arc(P)