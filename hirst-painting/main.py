from turtle import Turtle, Screen
from random import choice


def random_color():
    return choice(color_list)


def row():
    for i in range(10):
        jim.forward(50)
        jim.dot(20, random_color())


def move_up():
    jim.up()
    jim.hideturtle()
    jim.setpos(-275, -200)
    y = -200
    for i in range(10):
        row()
        y += 50
        jim.teleport(-275, y)


jim = Turtle()
screen = Screen()
screen.colormode(255)
color_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]

jim.speed(10)
jim.shape("turtle")

move_up()

screen.exitonclick()
