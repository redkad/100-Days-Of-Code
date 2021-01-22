from turtle import Turtle, Screen

jimmy = Turtle()
screen = Screen()


def forward():
    jimmy.forward(10)


def backward():
    jimmy.backward(10)


def counter_clock_wise():
    jimmy.left(15)


def clockwise():
    jimmy.right(15)


def clear():
    jimmy.clear()
    jimmy.penup()
    jimmy.home()
    jimmy.pendown()


screen.listen()

screen.onkey(forward, "W".lower())
screen.onkey(backward, "S".lower(), )
screen.onkey(counter_clock_wise, "A".lower())
screen.onkey(clockwise, "D".lower())
screen.onkey(clear, "C".lower())

screen.exitonclick()