import turtle
import math
#Group: Igor Kuznetcov, Maria Yadreeva
def okrgnst(x,y,rds,color,p_color):
    h.speed(40)
    h.pensize(4)
    h.color(color, p_color)
    h.penup()
    h.goto(x,y)
    h.begin_fill()
    h.pendown()
    h.circle(rds)
    h.end_fill()
h=turtle.Turtle()

def triangle(x,y,gipotenuza,h,color,p_color):
    sin=h/gipotenuza
    ugol1=math.asin(sin)*180/math.pi
    ugol=180-ugol1
    t.speed(10)
    t.pensize(5)
    t.color(color,p_color)
    t.penup()
    t.goto(x,y)
    t.begin_fill()
    t.pendown()
    t.forward(((gipotenuza**2-h**2)**0.5)*2)
    t.left(ugol)
    t.forward(gipotenuza)
    t.left(2*ugol1)
    t.forward(gipotenuza)
    t.end_fill()
    t.left(360+180-ugol1)
t=turtle.Turtle()
turtle.exitonclick()