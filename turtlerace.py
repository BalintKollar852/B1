from turtle import Turtle
from turtle import Screen
from Lib import random


class TurtleRace:

    def __init__(self):

        rnd = random.Random()

        screen = Screen()
        screen.setup(width=1280, height=720)

        turtle_goal = Turtle()
        turtle_goal._tracer(1, 10)
        turtle_goal.penup()
        turtle_goal.setposition(screen.window_width() / 5, -screen.window_height() / 2 + 20)
        turtle_goal.color("black", "black")
        turtle_goal.shape("turtle")
        turtle_goal.pendown()
        turtle_goal.pensize(5)
        turtle_goal.left(90)

        while turtle_goal.ycor() < (screen.window_height() / 2 - 20):
            turtle_goal.color("black", "black")
            turtle_goal.forward(10)
            turtle_goal.color("white", "black")
            turtle_goal.forward(10)

        turtle_goal.penup()
        turtle_goal.left(90)
        turtle_goal.forward(20)
        turtle_goal.left(90)

        turtle_joe = Turtle()
        turtle_joe.penup()
        turtle_joe.shape("turtle")
        turtle_joe.color("green", "yellow")
        turtle_joe.setx(-screen.window_width() / 2 + 100)
        turtle_joe.sety(20)

        turtle_jack = Turtle()
        turtle_jack.penup()
        turtle_jack.shape("turtle")
        turtle_jack.color("blue", "pink")
        turtle_jack.setx(-screen.window_width() / 2 + 100)
        turtle_jack.sety(-20)

        while turtle_jack.xcor() < turtle_goal.xcor() and turtle_joe.xcor() < turtle_goal.xcor():
            turtle_jack.forward(rnd.randint(0, 5))
            turtle_jack.left(rnd.randint(-2, 2))
            turtle_joe.forward(rnd.randint(0, 5))
            turtle_joe.left(rnd.randint(-2, 2))

        screen.delay(1)
        turtle_goal.color("black")
        if turtle_jack.xcor() < turtle_goal.xcor():
            turtle_goal.write("Joe win!")
        if turtle_joe.xcor() < turtle_goal.xcor():
            turtle_goal.write("Jack win!")
        screen.mainloop()


TurtleRace()
