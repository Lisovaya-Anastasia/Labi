from turtle import *

n = 12
length = 50
for i in range (n):
    forward(length)
    stamp()
    right(180)
    forward(length)
    right(180)
    right(360/n)

