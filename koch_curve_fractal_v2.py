import turtle as tl
step = 1000000000

def signature():
	tl.up()
	tl.home()
	tl.backward(40)
	tl.left(90)
	tl.forward(250)

	tl.down()
	tl.write("Koch Curve Fractal", font=("Arial", 16, "normal"))
	tl.up()
	tl.backward(20)
	tl.down()
	tl.write("~Tanvir Ahmed", font=("Arial", 9, "normal"))
	tl.up()

#fd id for taking minimum and same length step every time
def fd(stp):
	global step
	if stp < step:
		step = stp

	tl.forward(step)


def fractal(n):
	l = n/2
	if n < 6:
		return
	fractal(l)
	fd(l)

	tl.left(60)
	fractal(l)
	fd(l)


	tl.right(120)
	fractal(l)
	fd(l)

	tl.left(60)
	fractal(l)

#tl.shape("turtle")
signature()
tl.home()
tl.speed(0)
tl.left(90)
tl.backward(348)
tl.setheading(0.0)
tl.backward(680)
tl.down()

#tl.forward(200)
fractal(200)

tl.exitonclick()


