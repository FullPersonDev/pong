from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()

    def refresh_ball(self):
        ran_x = random.randint(-300, 300)
        ran_y = random.randint(-250, 250)
        self.setposition(ran_x, ran_y)