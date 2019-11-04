import turtle

n = 100
turtle.left(90)
turtle.penup()
turtle.forward(300)
turtle.pendown()
turtle.right(90)
for i in range(n):
    turtle.forward(3)
    turtle.right(360/n)
turtle.done()

