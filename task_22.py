#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    count=0
    if wall_is_beneath() and wall_is_above() and wall_is_on_the_right() and wall_is_on_the_left():
        fill_cell()
    else:
        fill_cell()
        while not wall_is_on_the_right():
            
            move_right()
            fill_cell()
            count+=1
        move_down()
        fill_cell()
        def paint():
            fill_cell()
            for i in range (count):
                move_right()
                fill_cell()
            if not wall_is_beneath():
                move_down()
                fill_cell()
                for i in range (count):
                    move_left()
                    fill_cell()
                if not wall_is_beneath():
                    move_down()
                    fill_cell()
            else:
                move_left(count)
        for i in range (count):
                move_left()
                fill_cell()
        if not wall_is_beneath():
            move_down()
            fill_cell()
        while not wall_is_beneath():
            paint()
        if wall_is_beneath():
            for i in range(count):
                move_right()
                fill_cell()
            move_left(count)
        
    
    

if __name__ == '__main__':
    run_tasks()
