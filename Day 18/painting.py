import turtle
import random

# import colorgram
#
# colors = colorgram.extract('test.jpg', 60)
# rgb = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb.append(new_color)

jimmy = turtle.Turtle()
screen = turtle.Screen()


jimmy.penup()
jimmy.hideturtle()
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]
jimmy.setheading(225)
jimmy.forward(300)
jimmy.setheading(0)

turtle.colormode(255)


def draw_dots():
    for _ in range(10):
        jimmy.dot(20, random.choice(color_list))
        jimmy.forward(50)

    jimmy.left(90)
    jimmy.forward(50)
    jimmy.left(90)
    jimmy.forward(500)
    jimmy.left(180)


for _ in range(10):
    draw_dots()


screen.exitonclick()
