import turtle
import math
#Group: Igor Kuznetcov, Maria Yadreeva
def crcl(x, y, rds,
         p_clr, clr):
    t.color(clr, p_clr)
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.pendown()
    t.circle(rds)
    t.end_fill()
t = turtle.Turtle()


def trngl(x, y, hypotenuse,
          h, p_clr, clr, direction):
    crtn_ngl = h/hypotenuse
    crnr = math.asin(crtn_ngl) * 180/math.pi
    crnr1 = 180 - crnr
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
    rectangular_triangle(-400, -400, 90, 1, 600, 628.02, "#FF4C5B", "#FF4C5B")
    rectangle(-400, 200, 90, 200, 400, "#C6C3B5", "#C6C3B5")
    parallelogram(-277, -199, 180, 417, 310, 107, "#B2FF59", "#C5E1A5")
    isosceles_trapezium(55, -400, 180, 2, 210, 392, 272, "#FF0000", "#FF0000")
    rectangle(115, -400, 90, 800, 285, "#7FC7FF", "#7FC7FF")
    rectangular_triangle(115, -400, 90, 2, 201, 209.7, "#7FC7FF", "#7FC7FF")
    parallelogram(-50, -199, 134, 623.14, 182, 120, "#FF8800", "#FF8800")
    rectangular_triangle(0, 400, 270, 2, 420, 437.293377, "#FF00FF", "#FF00FF")
    isosceles_trapezium(10, 200, 180, 1, 285, 212, 133, "#00FFFF", "#00FFFF")
    trngl(-200, -400, 238, 237.8, "#000000", "#000000", 0)
    trngl(-400, -250, 250, 249, "#ADD8E6", "#87CEFA", 270)
    rectangle(-400, 0, 90, 150, 110, "#4B0082", "#8A2BE2")
    isosceles_trapezium(-152, -240, 90, 2, 86, 117, 82, "#CD853F", "#CD853F")
    isosceles_trapezium(-237, 200, 0, 1, 205, 15, 105, "#DC143C", "#B22222")
    trngl(-400, 300, 280, 279, "#FFA07A", "#FF7F50", -90)
    crcl(-260, 320, 30, "#FFC0CB", "#FF1493", 0)
    crcl(-260, 210, 20, "#FFC0CB", "#FF1493", 0)
    crcl(-210, 210, 10, "#FFC0CB", "#FF1493", 0)
    crcl(-260, 180, 10, "#FFC0CB", "#FF1493", 0)
    crcl(50, -256, 35, "#696969", "#A9A9A9", 0)
    rectangular_triangle(400, 400, -90, 1, 289.83, 401.7784, "#00FF00", "#32CD32")
    rectangle(30, 272, 90, 148, 36, "#F0FFFF", "#F0F8FF")
    parallelogram(185, -400, 180, 224.41, 66.27, 107.18, "#FFE4E1", "#FFF0F5")
    isosceles_trapezium(200, -100, 0, 1, 95, 128, 158, "#BC8F8F", "#BC8F8F")
    pass


t.pensize(4)
t.speed(10)
draw_art()
t = turtle.Turtle()
turtle.exitonclick()