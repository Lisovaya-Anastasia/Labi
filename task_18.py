#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    if True:
        while not wall_is_on_the_left():
            if wall_is_above() and wall_is_beneath():
                move_left()
            elif not wall_is_above():
                while not wall_is_above():
                    move_up()
                while not wall_is_on_the_left():
                    move_left()
            elif not wall_is_beneath():
                move_down()
                while not wall_is_on_the_left():
                    move_left()
                while not wall_is_above():
                    move_up()
    elif wall_is_on_the_left():
        if not wall_is_above():
            while not wall_is_above():
                move_up()
            while not wall_is_on_the_left():
                move_left()
        elif not wall_is_beneath():
            move_down()
            while not wall_is_on_the_left():
                move_left()
            while not wall_is_above():
                move_up()
        else:
            move_right()
    
    
    else: 
    while not wall_is_on_the_right():
        if wall_is_above() and wall_is_beneath():
            move_right()
        elif not wall_is_above():
            while not wall_is_above():
                move_up()
            while not wall_is_on_the_left():
                move_left()
        elif not wall_is_beneath():
            move_down()
            while not wall_is_on_the_left():
                move_left()
            while not wall_is_above():
                move_up()
    if wall_is_on_the_right() and not wall_is_above()
        while not wall_is_above():
                move_up()
            while not wall_is_on_the_left():
                move_left()
    if wall_is_on_the_right() and not wall_is_beneath()
        move_down()
            while not wall_is_on_the_left():
                move_left()
            while not wall_is_above():
                move_up()         
    
if __name__ == '__main__':
    run_tasks()
