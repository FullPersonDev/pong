from turtle import Screen
from paddles import Paddle
from court import Net, Scoreboard
from ball import Ball

# Set up screen
screen = Screen()
screen.setup(1200, 600)
screen.bgcolor("black")
screen.title("Welcome to Pong")

# Set up player paddles and locations
player1_paddle = Paddle()
player1_paddle.set_player_loc()
player2_paddle = Paddle()
player2_paddle.set_comp_loc()

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



screen.exitonclick()
