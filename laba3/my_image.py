import math
from graph import *
def update():
    if xCoord(obj) >=450:
        return()
    moveObjectBy(obj, 2, 0)
    
#onTimer(update, 50)

def keyPressed(event):
    if event.keycode == VK_ESCAPE:
        close()
onKey(keyPressed)


canvasSize(512, 512)
penSize(3)
penColor("#B8860B")
brushColor("#B8860B")
rectangle(0, 0, 512, 215)

penColor("#DAA520")
brushColor("#DAA520")
rectangle(0, 215, 512, 512)

penColor("#B0E0E6")
brushColor("#B0E0E6")
rectangle(200, 20, 500, 200)

penColor("#87CEEB")
brushColor("#87CEEB")
rectangle(220, 40, 480, 180)

penColor("#AD522D")
brushColor("#CD853F")
polygon([(130, 290), (120, 270), (120, 300)])
polygon([(170, 290), (180, 270), (180, 300)])



penColor("#AD522D")
brushColor("#CD853F")
circle(150, 315, 35)

penColor("#000000")
brushColor("#00B000")
circle(135, 310, 5)
circle(165, 310, 5)

penColor("#AD522D")
brushColor("#CD853F") 
def oval():
    b=50
    a=80
    points=list()
    for x in range(160, 320):
        y=360+b/a*(a**2-(x-240)**2)**0.5
        points.append((x, y))
    for x in range(320, 160, -1):
        y=360-b/a*(a**2-(x-240)**2)**0.5
        points.append((x, y))
    polygon(points)
oval()

brushColor("#808080")
x=120
y=400
obj=circle(x, y, 20)
#onKey(keyPressed)
onTimer(update, 50)

run()
