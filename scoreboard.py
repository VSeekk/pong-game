from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):

        self.goto(-100, 260)
        self.write(f"Score: {self.l_score}", align="center", font=("Courier", 20, "normal"))
        self.goto(100, 260)
        self.write(f"Score: {self.r_score}", align="center", font=("Courier", 20, "normal"))

    def l_score_increase(self):
        self.l_score += 1
        self.clear()
        self.update_score()

    def r_score_increase(self):

        self.r_score +=1
        self.clear()
        self.update_score()