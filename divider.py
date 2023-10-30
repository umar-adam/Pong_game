from turtle import Turtle

class Divider(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.create_middle_line()

    def create_middle_line(self):
        self.goto(0, -300)
        self.setheading(90)
        while self.ycor() != 300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)
