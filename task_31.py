#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    flag = True

    while flag:
        while not wall_is_on_the_right() and wall_is_beneath():
            move_right()

        while not wall_is_on_the_left() and wall_is_beneath():
            move_left()

        if not wall_is_beneath():
            move_down()
        else:
            flag = False


if __name__ == '__main__':
    run_tasks()
