from turtle import Turtle

# Set up paddles class
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=6, outline=1)
        self.setheading(90)
        self.goto(position)

    def up(self):
        self.forward(40)

    def down(self):
        self.backward(40)
