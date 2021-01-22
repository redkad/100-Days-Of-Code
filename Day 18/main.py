from turtle import Turtle, Screen
import random

jimmy = Turtle()

jimmy.shape("turtle")
jimmy.color("blue")

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         jimmy.forward(100)
#         jimmy.right(angle)
#     # jimmy.color(R, G, B)
#
#
# for i in range(3, 11):
#     R = random.random()
#     G = random.random()
#     B = random.random()
#     jimmy.color(R, G, B)
#     draw_shape(i)

walk = [0, 90, 180, 270]

jimmy.speed('fastest')


def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    color = (r, g, b)
    return color


size = 100
jimmy.speed("fastest")


def draw(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        jimmy.color(random_color())
        jimmy.circle(size)
        current_heading = jimmy.heading()
        jimmy.setheading(current_heading + size_of_gap)

draw(5)
    # size+=5

# jimmy.forward(100)

# Screen().exitonclick()
