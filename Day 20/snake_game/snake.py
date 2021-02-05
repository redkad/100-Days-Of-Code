from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        x = 0
        for snake in range(3):
            new_snake = Turtle("square")
            new_snake.penup()
            new_snake.color("white")
            new_snake.goto(x, 0)
            x -= 20
            self.snake_body.append(new_snake)


    def move(self):
        for num in range(len(self.snake_body) - 1, -0, -1):
            new_x = self.snake_body[num - 1].xcor()
            new_y = self.snake_body[num - 1].ycor()
            self.snake_body[num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



