from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")
file = open("data.txt")
h_score = file.read()


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        data = open("data.txt")
        self.high_score = int(data.read())
        file.close()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            filew = open("data.txt", mode="w")
            filew.write(str(self.high_score))
            filew.close()

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def score_add(self):
        self.score += 1
        self.update_scoreboard()
