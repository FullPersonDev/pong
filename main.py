from turtle import Screen
from paddles import Paddle
from court import Net, Scoreboard
from ball import Ball
import time

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
ball.ball_refresh()

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
    time.sleep(0.03)
    ball.ball_move()

    # Detect collision with top and bottom walls
    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(player2_paddle) < 50 and ball.xcor() >= 540:
        ball.bounce_x()

    if ball.distance(player1_paddle) < 50 and ball.xcor() <= -550:
        ball.bounce_x()

    # Detect who scored, update scoreboard, and refresh ball
    if ball.xcor() >= 610:
        scoreboard.p1_score += 1
        scoreboard.print_scoreboard()
        ball.ball_refresh()

    elif ball.xcor() <= -610:
        scoreboard.p2_score += 1
        scoreboard.print_scoreboard()
        ball.ball_refresh()

screen.exitonclick()
