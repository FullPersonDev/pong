from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.x = 0
        self.y = 0
        self.x_move = 10
        self.y_move = 10
        self.goto(self.x, self.y)

    def ball_refresh(self):
        self.x = random.randint(-300, 300)
        self.y = random.randint(-250, 250)
        self.goto(self.x, self.y)

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
