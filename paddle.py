from turtle import Turtle

STARTER_LOCATIONS = [(-370, 0), (370, 0)]

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(4, 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def go_up(self):
        if self.ycor() < 250:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -250:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)
