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
ball_lifetime = list()
ball_x = list()
ball_y = list()
ball_r = list()
ball_color = list()
ball_v_x = list()
ball_v_y = list()
count=0
name = input("Enter name:")
def new_ball():
    global count
    global x, y, r
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    v_x = rnd(-5,5)
    v_y = rnd(-5,5)
    color = choice(colors)
    
    
    if count % 9 == 0:
        x = rnd(100,700)
        y = rnd(100,500)
        r = rnd(20, 30)
        v_x = rnd(-5,5)
        v_y = rnd(-5,5)
        color = "black"    
        
    
    
    i = 0
    flag = True
    while i < count:
        if (ball_x[i] - x) ** 2 + (ball_y[i] - y) ** 2 <= (ball_r[i]+r) ** 2:
            flag = False
            break
        else:
            i += 1
    if flag:
        ball_color.append(color)
        obj_ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = color, width=0)
        ball.append(obj_ball)
        if count % 9 == 0:
            ball_lifetime.append(97)
        else:
            ball_lifetime.append(-1)
        count += 1
        ball_x.append(x)
        ball_y.append(y)
        ball_r.append(r)
        ball_v_x.append(v_x)
        ball_v_y.append(v_y)
    
    root.after(1000, new_ball)
    

def move():
    global count
    canv.delete(ALL)
    for i in range (0,count):    
        canv.create_oval(ball_x[i]-ball_r[i]+ball_v_x[i],ball_y[i]-ball_r[i]+ball_v_y[i],ball_x[i]+ball_r[i]+ball_v_x[i],ball_y[i]+ball_r[i]+ball_v_y[i], fill = ball_color[i], width=0)
        ball_x[i] = ball_x[i] + ball_v_x[i]
        ball_y[i] = ball_y[i] + ball_v_y[i]
    
    for i in range (0, count):
        if (ball_x[i] <= ball_r[i]) or (ball_x[i] >= 800 - ball_r[i]) or (ball_y[i] <= ball_r[i]) or (ball_y[i] >= 600 - ball_r[i]):
            ball_v_x[i] = -ball_v_x[i]
            ball_v_y[i] = -ball_v_y[i]
                 
    
    for i in range (0,count):
        for j in range (i, count):
            if (ball_x[i] - ball_x[j]) ** 2 + (ball_y[i] - ball_y[j]) ** 2 <= (ball_r[i]+ball_r[j]) ** 2:
                ball_v_x[i] = -ball_v_x[i]
                ball_v_y[i] = -ball_v_y[i]
                ball_v_x[j] = -ball_v_x[j]
                ball_v_y[j] = -ball_v_y[j]
    i = 0
    while i < len(ball_lifetime):
        ball_lifetime[i] = ball_lifetime[i] - 1
        if ball_lifetime[i] == 0:
            del ball_x[i] 
            del ball_y[i] 
            del ball_r [i]
            del ball_color[i]
            del ball_v_x[i] 
            del ball_v_y[i]  
            del ball_lifetime[i]
            i -= 1
            count -= 1
        i += 1
    
    root.after(10, move)

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
            
            if ball_lifetime[i] < 0:
                k+=1
            else:
                k += 5
            del ball_lifetime[i]
            print(k)
            count -= 1
            break
    
def key(event):
	if event.char != 'q':
		return
	with open('Winners' ,'a') as f:
		f.write(str(k) + ' ' + str(name) + '\n')
	print('EXIT!!!!')
	exit(0)

new_ball()
move()
canv.bind('<Button-1>', click)
canv.bind('<Key>', key)
canv.focus_set()
mainloop()
