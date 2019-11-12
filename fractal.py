import turtle as tl

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


def fractal(n):
	l = n/2
	if l < 3:
		return
	fractal(l)
	tl.forward(l)

	tl.left(60)
	fractal(l)
	#tl.forward(l)

	tl.forward(l)

	tl.right(120)
	fractal(l)
	tl.forward(l)

	tl.left(60)
	fractal(l)

#tl.shape("turtle")
signature()
tl.home()
tl.left(90)
tl.backward(348)
tl.setheading(0.0)
tl.backward(680)
tl.down()

#tl.forward(200)
fractal(100)

tl.exitonclick()


