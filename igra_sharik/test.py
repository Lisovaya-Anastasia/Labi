from tkinter import *
from random import randrange as rnd, choice
import time
import math
root = Tk()
root.geometry('800x600')
k=0
canv = Canvas(root,bg = 'white')
canv.pack(fill = BOTH,expand = 1)

colors = ['red','orange','yellow','green','blue']
ball = list()
ball_x = list()
ball_y = list()
ball_r = list()
ball_color = list()
ball_v_x = list()
ball_v_y = list()
count=0
def new_ball():
    global count
    global x, y, r
    canv.delete(ALL)
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    v_x = rnd(-5,5)
    v_y = rnd(-5,5)
    color = choice(colors)
    ball_color.append(color)
    obj_ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = color, width=0)
    count += 1
    ball.append(obj_ball)
    ball_x.append(x)
    ball_y.append(y)
    ball_r.append(r)
    ball_v_x.append(v_x)
    ball_v_y.append(v_y)
    root.after(1000,new_ball)

def move():
    global count
    canv.delete(ALL)
    for i in range (0,count):	
        canv.create_oval(ball_x[i]-ball_r[i]+ball_v_x[i],ball_y[i]-ball_r[i]+ball_v_y[i],ball_x[i]+ball_r[i]+ball_v_x[i],ball_y[i]+ball_r[i]+ball_v_y[i], fill = ball_color[i], width=0)
        ball_x[i] = ball_x[i] + ball_v_x[i]
        ball_y[i] = ball_y[i] + ball_v_y[i]
    root.after(10,move)

def click(event):
    global k, x, y, r, count
    for i in range (0, count):
        if math.sqrt((ball_x[i]-event.x)**2+(ball_y[i]-event.y)**2) <= ball_r[i]:
            del ball_x[i] 
            del ball_y[i] 
            del ball_r [i]
            del ball_color[i]
            del ball_v_x[i] 
            del ball_v_y[i]
            k=k+1
            print(k)
            count -= 1
            break
    
new_ball()
move()
canv.bind('<Button-1>', click)
mainloop()
