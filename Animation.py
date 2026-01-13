import turtle as t
t.bgcolor("Black")
t.pensize(5)
t.speed(1)
t.color("red")
t.begin_fill()
t.fillcolor("red")
t.left(150)
t.forward(180)
t.circle(-90, 180)
t.setheading(60)
t.circle(-90, 180)
t.forward(180)
t.end_fill()
t.hideturtle()
msg=" My name is Pragya."
t.write(msg,move=True,align="left", font="Arial")

t.done()