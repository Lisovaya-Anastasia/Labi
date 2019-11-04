from turtle import *
side = 8
step = 10
number_of_rotations = 42
for i in range (number_of_rotations*4):
    forward(side)
    left(90)
    side += step