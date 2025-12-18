from turtle import Screen
from paddles import Paddle
from court import Net, Scoreboard
from ball import Ball

# Set up screen
screen = Screen()
screen.setup(1200, 600)
screen.bgcolor("black")
screen.title("Welcome to Pong")
screen.tracer(0)

# Set up player paddles and locations
player1_paddle = Paddle((-580, 0))
player2_paddle = Paddle((570, 0))

# Set up court (net and scoreboard)
new_net = Net()
scoreboard = Scoreboard()

# Set up ball
ball = Ball()
ball.refresh_ball()

# Set up listening events
screen.listen()
screen.onkey(player1_paddle.up, "w")
screen.onkey(player1_paddle.down, "s")
screen.onkey(player2_paddle.up, "o")
screen.onkey(player2_paddle.down, "l")

# Keep game on until game over
game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()
