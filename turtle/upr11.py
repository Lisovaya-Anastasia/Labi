import turtle
import math

R = 40  # the radius of the first circle
n = 100  # the "accuracy"
delta_R = 10  # the increment of the radius
x = 10  # number of the circles
pi = 3.1415


def circle(R):
    l = 2 * R * math.cos(pi * (n - 2) / (2 * n))
    for i in range(n):
        turtle.forward(l)
        turtle.left(360 / n)


turtle.left(90)

for j in range(x):
    circle(R)
    turtle.left(180)
    circle(R)

    R += delta_R