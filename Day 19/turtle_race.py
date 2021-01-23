import random
from turtle import Turtle, Screen

screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racing_turtles = []
y = -100
for turtle_index in range(6):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    # jimmy.shape()
    new_turtle.goto(-230, y)
    racing_turtles.append(new_turtle)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in racing_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet == winner:
                print(f"You've won! The {winner} turtle is the winner")
            else:
                print(f"You've lost! The {winner} turtle is the winner")

        random_number = random.randint(0, 10)
        turtle.forward(random_number)

screen.exitonclick()
