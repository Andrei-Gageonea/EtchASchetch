import random
import turtle as turtle
from turtle import *
screen = Screen()
beast = Turtle()

def forward():
    beast.forward(10)

def back():
    beast.back(10)

def turn_left():
    beast.left(5)

def turn_right():
    beast.right(5)

def clear_screen():
    screen.resetscreen()

def moving():
    screen.listen()
    screen.onkeypress(fun = forward, key = "Up")
    screen.onkeypress(fun = back, key = "Down")
    screen.onkeypress(fun = turn_left, key = "Left")
    screen.onkeypress(fun = turn_right, key = "Right")
    screen.onkeypress(fun = clear_screen , key = "c")
    mainloop()
    moving()


moving()
screen.exitonclick()
