from turtle import *

def koch(kame,length,n):
    if n == 0:
        kame.forward(length);
    else:
        koch(kame,length/2,n-1)
        kame.left(60)
        koch(kame,length/2,n-1)
        kame.left(120)
        koch(kame,length/2,n-1)
        kame.left(60)
        koch(kame,length/2,n-1)

mykame = Turtle()

mykame.speed(10)
mykame.penup()
mykame.goto(0,0)
mykame.pendown()
koch(mykame, 500,3)
exitonclick()
