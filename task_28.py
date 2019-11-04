#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    n = 0
    while not n == 5:
        if cell_is_filled():
            n += 1
        if n != 5:
            move_right()


if __name__ == '__main__':
    run_tasks()
