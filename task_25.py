#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
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
    move_down(2)
    cross()
    move_right(3)
    move_down()
    cross()
    move_right(3)
    move_down()
    cross()
    move_right(3)
    move_down()
    cross()
    move_right(3)
    move_down()
    cross()
    move_left()
if __name__ == '__main__':
    run_tasks()
