"""Tutorial for Turtle"""

from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(45, 60)
leo.pendown()
colormode(255)
leo.pencolor("pink")
leo.fillcolor(32, 67, 93)
leo.color("green", "yellow")


i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
done()