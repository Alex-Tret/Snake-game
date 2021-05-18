from turtle import Turtle
ALIGN = 'center'
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, Highscore {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt", mode="w") as data:
            data.write(f"{self.highscore}")


    def display_score(self):

        self.score += 1
        self.update_scoreboard()