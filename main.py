import turtle
import math
#Group: Igor Kuznetcov, Maria Yadreeva
def crcl(x, y, rds,
            clr, p_clr, direction):
    t.speed(40)
    t.pensize(4)
    t.color(clr, p_clr)
    t.setheading(direction)
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.circle(rds)
    t.end_fill()
t = turtle.Turtle()


def trngl(x, y, hypotenuse,
             h, clr, p_clr, direction):
    crtn_ngl = h/hypotenuse
    crnr = math.asin(crtn_ngl) * 180/math.pi
    crnr1 = 180-crnr
    t.speed(10)
    t.pensize(5)
    t.color(clr, p_clr)
    t.setheading(direction)
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.forward(((hypotenuse**2-h**2)**0.5)*2)
    t.left(crnr1)
    t.forward(hypotenuse)
    t.left(2 * crnr)
    t.forward(hypotenuse)
    t.end_fill()
    t.left(360 + 180 - crnr)
t = turtle.Turtle()


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