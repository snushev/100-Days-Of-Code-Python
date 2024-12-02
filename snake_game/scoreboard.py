from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.scoreboard()

    def scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points}. High Score: {self.high_score}", align=ALIGN, font=FONT)

    def update_score(self):

        self.scoreboard()
        self.points += 1

    def reset(self):
        if self.points > self.high_score:
            self.high_score = self.points
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.points = 0
        self.update_score()

    # def endgame(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER!", align=ALIGN, font=("Courier", 20, "normal"))