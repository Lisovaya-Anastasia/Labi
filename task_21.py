#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    for i in range(0, 14):
        move_down()
    for n in range(0, i):
        move_right()
    fill_cell()
    while (wall_is_on_the_left() == False):
        move_left()
    move_down()
    move_right()
        

if __name__ == '__main__':
    run_tasks()
