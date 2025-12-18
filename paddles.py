from turtle import Turtle

# Set up paddles class
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=6, outline=1)
        self.setheading(90)

    def set_player_loc(self):
        self.setposition(x=-580, y=0)

    def set_comp_loc(self):
        self.setposition(x=570, y=0)

    def up(self):
        self.forward(30)

    def down(self):
        self.backward(30)