from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_l = 0
        self.score_r = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.missing()

    def missing(self):

        self.goto(100, 260)
        self.write(f"R_Score: {self.score_r}", align='center', font=("Courier", 16, "normal"))
        self.goto(-100, 260)
        self.write(f"L_Score: {self.score_l}", align='center', font=("Courier", 16, "normal"))

    def l_point(self):
        self.clear()
        self.score_l += 1
        self.missing()

    def r_point(self):
        self.clear()
        self.score_r += 1
        self.missing()
