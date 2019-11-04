import turtle as t

t.shape('classic')

width = 2

t.width(width)

side = 100
for i in range(10):
    t.penup()
    t.goto(-side/2, -side/2)
    t.pendown()

    for j in range(4):
        t.forward(side)
        t.left(90)

    t.penup()
    t.goto(-side//2, -side//2)
    t.pendown()

    side += 30