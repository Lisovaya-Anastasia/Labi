#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def cross():
        for i in range(2):
            fill_cell()
            move_right()
        fill_cell()
        move_down()
        move_left()
        fill_cell()
        move_up(2)
        fill_cell()
        
    def go():
        move_right(3)
        move_down()
    move_down()
    
    def begin():
            move_down(5)
            move_left(37)
            
    for i in range(4):
        for i in range(9):
            cross()
            go()
        cross()
        begin()
    for i in range(9):
        cross()
        go()
    cross()
    move_left(37)    
if __name__ == '__main__':
    run_tasks()
