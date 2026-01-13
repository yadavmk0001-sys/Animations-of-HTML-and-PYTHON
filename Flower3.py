import turtle as t
import colorsys
t.bgcolor("black")
t.tracer(127)
def design():
    h = 70
    n = 298
    for i in range(2000):
        c = colorsys.hsv_to_rgb(h,1,0.9)
        h += 2/n
        t.pensize(7)
        t.color("black")
        t.up()
        t.goto(0,0)
        t.down()
        t.fillcolor(c)
        t.begin_fill()
        t.circle(94,60,steps=5)
        t.fd(i)
        t.rt(79)
        t.lt(90)
        t.bk(70)
        t.end_fill()
design()
t.seth(80)
