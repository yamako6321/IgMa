import turtle
import math
#Group: Igor Kuznetcov, Maria Yadreeva
def okrgnst(x, y, rds,
            color, p_color):
    h.speed(40)
    h.pensize(4)
    h.color(color, p_color)
    h.penup()
    h.goto(x, y)
    h.begin_fill()
    h.pendown()
    h.circle(rds)
    h.end_fill()
h = turtle.Turtle()
def triangle(x, y, gipotenuza,
             h, color, p_color):
    sin = h/gipotenuza
    ugol1 = math.asin(sin) * 180/math.pi
    ugol = 180-ugol1
    t.speed(10)
    t.pensize(5)
    t.color(color, p_color)
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.forward(((gipotenuza**2-h**2)**0.5)*2)
    t.left(ugol)
    t.forward(gipotenuza)
    t.left(2 * ugol1)
    t.forward(gipotenuza)
    t.end_fill()
    t.left(360 + 180 - ugol1)


def isosceles_trapezium(x, y, direction, side, top_base,
                        bottom_base, color, p_color, p_size):
    t.pensize(p_size)
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.pd()
    t.color(p_color, color)
    t.setheading(direction)
    c = (bottom_base - top_base) / 2
    fi = math.degrees((math.acos(c / side)))
    t.lt(fi)
    t.fd(side)
    t.rt(fi)
    t.fd(top_base)
    t.rt(fi)
    t.fd(side)
    t.rt(180 - fi)
    t.fd(bottom_base)
    t.end_fill()


def rectangle(x, y, direction, side,
              base, color, p_color, p_size):
    t.pensize(p_size)
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.pd()
    t.color(p_color, color)
    t.setheading(direction)
    for i in range(4):
        if i % 2 == 0:
            t.fd(side)
        else:
            t.fd(base)
        t.rt(90)
    t.end_fill()


def square(x, y, direction, side,
           color, p_color, p_size):
    t.pensize(p_size)
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.pd()
    t.color(p_color, color)
    t.setheading(direction)
    for i in range(4):
        t.fd(side)
        t.rt(90)
    t.end_fill()



t = turtle.Turtle()
turtle.exitonclick()