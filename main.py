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


def isosceles_trapezium(x, y, direction, form, side, top_base,
                        bottom_base, color, p_color):
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.pd()
    t.color(p_color, color)
    t.setheading(direction)
    c = (bottom_base - top_base) / 2
    if form == 1:
        fi = math.degrees((math.acos(c / side)))
    else:
        fi = -math.degrees((math.acos(c / side)))
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
              base, color, p_color):
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
           color, p_color):
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


def rectangular_triangle(x, y, direction, form, height,
                         hypotenuse, color, p_color):
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.pd()
    t.color(p_color, color)
    t.setheading(direction)
    ksi = math.degrees(math.acos(height/hypotenuse))
    if form == 1:
        psi = 180 - ksi
    else:
        psi = -(180 - ksi)
    base = (hypotenuse ** 2-height ** 2) ** 0.5
    t.fd(height)
    t.rt(psi)
    t.fd(hypotenuse)
    t.rt((psi / abs(psi))*(90 + ksi))
    t.fd(base)
    t.end_fill()


def parallelogram(x, y, direction, side,
                  base, angle, color, p_color):
    t.up()
    t.goto(x, y)
    t.begin_fill()
    t.pd()
    t.color(p_color, color)
    t.setheading(direction)
    angle2 = 180 - angle
    for i in range(4):
        if i % 2 == 0:
            t.rt(angle2)
            t.fd(side)
        else:
            t.rt(angle)
            t.fd(base)
    t.end_fill()


def draw_art():
    rectangular_triangle(-400, -400, 90, 1, 600, 627, "#FF4C5B", "#FF4C5B")
    rectangle(-400, 200, 90, 200, 400, "#C6C3B5", "#E7E6E0")
    parallelogram(-277, -199, 180, 417, 310, 107, "#B2FF59", "#C5E1A5")
    isosceles_trapezium(55, -400, 180, 2, 210, 392, 272, "red", "#000000")
    rectangle(115, -400, 90, 800, 285, "#7FC7FF", "#000000")
    rectangular_triangle(115, -400, 90, 2, 201, 209.7, "#7FC7FF", "#000000")
    parallelogram(-50, -199, 134, 623.14, 183, 120, "#FF8800", "#FFA343")
    rectangular_triangle(0, 400, 270, 2, 410, 427, "#FF00FF", "#FF00FF")
    pass


t.pensize(4)
t.speed(10)
draw_art()
t = turtle.Turtle()
turtle.exitonclick()