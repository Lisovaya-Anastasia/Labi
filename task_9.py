#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    if (wall_is_above() == False):
        fill_cell()
    while ((wall_is_above() == True or wall_is_beneath() == True) and wall_is_on_the_right() == False):
        move_right()
    if (wall_is_above() == False):
        fill_cell()


if __name__ == '__main__':
    run_tasks()
