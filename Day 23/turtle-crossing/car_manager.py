from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.cars = []
        self.carspeed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            color = random.choice(COLORS)
            y_cor = random.randint(-250, 250)
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(color)
            new_car.shapesize(1,2)
            new_car.goto(300, y_cor)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.carspeed)

    def level_up(self):
        self.carspeed += MOVE_INCREMENT
