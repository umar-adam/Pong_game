from turtle import Turtle

FONT = ("Courier", 70, "normal")
ALIGNMENT = "center"
WINNING_SCORE = 5

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.ht()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.color("green")
        self.clear()
        self.goto(-100, 200)
        self.write(self.p1_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.p2_score, align=ALIGNMENT, font=FONT)

    def p1_point(self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2_point(self):
        self.p2_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        if self.p1_score == WINNING_SCORE:
            self.write("PLAYER 1 WINS", align=ALIGNMENT, font=FONT)
        else:
            self.write("PLAYER 2 WINS", align=ALIGNMENT, font=FONT)
