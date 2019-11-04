#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    x = 1
    while not wall_is_on_the_right():
        move_right()
        x = x + 1

    move_left(x - 1)

    for i in range(x):
        for j in range(x):
            if not (i == j or i + j == x - 1):
                if i:
                    move_down(i)
                if j:
                    move_right(j)

                fill_cell()

                if i:
                    move_up(i)
                if j:
                    move_left(j)

    move_down(x - 1)


if __name__ == '__main__':
    run_tasks()
