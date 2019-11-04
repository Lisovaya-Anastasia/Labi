#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    if (wall_is_on_the_left() == False):
        move_left(n=1)
    elif (wall_is_on_the_right() == False):
        move_right(n=1)
    elif (wall_is_above() == False):
    move_up(n=1)
    elif (wall_is_beneath() == False):
    move_down(n=1)


if __name__ == '__main__':
    run_tasks()
