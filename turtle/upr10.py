import turtle as t


def circle(r):
	for i in range(1, 101, 1):
		t.forward(r)
		t.left(360/100)

t.shape ("turtle")
r=5
for i in range(1, 7, 1):
	circle(r)
	t.left(360/6)