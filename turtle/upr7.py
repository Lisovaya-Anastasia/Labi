import turtle as t


t.shape ("turtle")
a=5
for x in range(1, 360, 1):
	t.forward(0.01*a)
	t.left(5)
	a=a+5
