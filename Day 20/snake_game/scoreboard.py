from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        self.update_highscore()


    def update_scoreboard(self):
        self.goto(-80, 270)
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def update_highscore(self):
        with open("data.txt", "r") as f:
            self.high_score = f.read()
        self.goto(80, 270)
        self.write(arg=f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            with open("data.txt", "w") as f:
                f.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()
        self.update_highscore()

    def increase_score(self):
        self.score += 1
        # self.clear()
        self.update_scoreboard()
        self.update_highscore()
