from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.color("Black")
        self.score = 0
        self.print_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.print_score()

    def print_score(self):
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)