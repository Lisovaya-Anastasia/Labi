from random import randrange as rnd, choice
import math
import time

colors2 = ['#b5dfe5', '#437f83', '#a0d2d8', '#5e9fa3', '#d2f1f6']
colors1 = ['#ae215b', '#c1317e']


class Ball():
    def __init__(self, canv, x=40, y=450):
        """ Конструктор класса Ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.canv = canv
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(colors2)
        self.id = self.canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color,
            width=0
        )
        self.live = 30

    def set_coords(self):
        self.canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def draw_ball(self):
        self.id = self.canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color,
            width=0
        )

    def delete(self):
        """
        Deletes ball.id
        """
        self.canv.delete(self.id)

    def move(self):
        """
        Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """

        a = 10
        self.delete()
        self.x += self.vx
        self.y += -(self.vy - a / 2)
        self.vy -= a
        self.draw_ball()
        if self.x - self.r < 0 and self.vx < 0:
            self.x += (self.r - self.x)
            self.vx = -self.vx
        elif self.x + self.r > 800 and self.vx > 0:
            self.x -= (self.x + self.r - 800)
            self.vx = -self.vx
        elif self.y - self.r < 0 and self.vy > 0:
            self.y += (self.r - self.y)
            self.vy = -self.vy
        elif self.y + self.r > 600 and self.vy < 0:
            self.y -= (self.y + self.r - 600)
            self.vy = -self.vy
            self.vy -= 10

    def hittest(self, obj):
        if ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5 < self.r + obj.r:
            return True
        else:
            return False

        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """


class Gun():
    def __init__(self, canv, balls=0, bullet=0):
        self.balls = balls
        self.bullet = bullet
        self.canv = canv
        self.an = 1
        self.f2_power = 10
        self.f2_on = 0
        self.id = self.canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        # balls, bullet - were global
        self.bullet += 1
        new_ball = Ball(self.canv)
        new_ball.r += 3
        if event.x - new_ball.x != 0:
            self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))  # division by zero wtf?
        else:
            if (event.y - new_ball.y) > 0:
                self.an = math.pi / 2
            else:
                self.an = 3 * math.pi / 2
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        self.balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """
        Прицеливание. Зависит от положения мыши.
        """
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            self.canv.itemconfig(self.id, fill='white')
        else:
            self.canv.itemconfig(self.id, fill='black')
        self.canv.coords(self.id, 20, 450,
                         20 + max(self.f2_power, 20) * math.cos(self.an),
                         450 + max(self.f2_power, 20) * math.sin(self.an)
                         )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 5
            self.canv.itemconfig(self.id, fill='white')
        else:
            self.canv.itemconfig(self.id, fill='black')


class Target(Ball):
    """
    Класс цели. Обладает всеми свойствами мяча.
    """

    def __init__(self, canv):
        """
        Конструктор класса. self.points - количество очков
        """
        self.canv = canv
        self.vx = 0
        self.vy = 0
        self.points = 0
        self.live = 1
        self.color = choice(colors1)
        self.id = None
        self.id_points = self.canv.create_text(30, 30, text=self.points, font='28')

    def new_target(self):
        """
        Инициализация новой цели.
        """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.draw_ball()
        self.canv.itemconfig(self.id, fill=self.color)

    def hit(self, points=1):
        """
        Попадание шарика в цель.
        """
        self.canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        self.canv.itemconfig(self.id_points, text=self.points)

#сама прога
from random import randrange as rnd, choice
import tkinter as tk
import math
import time
import datetime
from gun import *

root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canv = tk.Canvas(root, bg='#7ebfc3')
canv.pack(fill=tk.BOTH, expand=1)
colors2 = ['#b5dfe5', '#437f83', '#a0d2d8', '#5e9fa3', '#d2f1f6']
colors1 = ['#ae215b', '#c1317e']

t1 = Target(canv)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun(canv)


def new_game(event=''):
	global t1, screen1
	t1.new_target()
	g1.bullet = 0
	g1.balls = []
	canv.bind('<Button-1>', g1.fire2_start)
	canv.bind('<ButtonRelease-1>', g1.fire2_end)
	canv.bind('<Motion>', g1.targetting)

	canv.update()
	zzz = 0.03
	t1.live = 1

	while t1.live:
		t1.move()
		for b in g1.balls:
			if b.live:
				b.move()
			if b.hittest(t1) and t1.live:
				t1.live = 0

				t1.hit()
				canv.bind('<Button-1>', '')
				canv.bind('<ButtonRelease-1>', '')
				canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(g1.bullet) + ' выстрелов')
				b.delete()
				t1.delete()
				b.live = 0

		canv.update()
		time.sleep(zzz)
		g1.targetting()
		g1.power_up()
		for i in g1.balls:
			i.delete()
	time.sleep(1)
	canv.delete(screen1)
	screen1 = canv.create_text(400, 300, text='', font='28')

	t = datetime.datetime.now()
	dt = 1
	while (datetime.datetime.now() - t).seconds < dt:
		canv.update()
		time.sleep(zzz)
		g1.targetting()
		g1.power_up()
	canv.itemconfig(screen1, text='')
	# canv.delete(gun)

	root.after(1, new_game)


new_game()

tk.mainloop()

