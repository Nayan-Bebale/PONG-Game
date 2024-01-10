from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
# TODO 1. Create the Screen

screen.setup(width=800, height=600)
screen.title("PONG")
screen.bgcolor("black")

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()


screen.exitonclick()
