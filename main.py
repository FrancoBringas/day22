from turtle import Screen
from padle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
MOVE_DISTANCE = 20
X = 350
Y = 0
game = True
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong game")

screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
x = 0.10
while game:
    screen.listen()
    screen.update()
    ball.move()

    time.sleep(x)
    if ball.ycor() > 280 or ball.ycor() < -280:
        screen.update()

        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 324 or ball.distance(l_paddle) < 50 and ball.xcor() < -324:
        ball.bounce_x()
        if x > 0.01:
            x -= 0.01
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        x = 0.1

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        x = 0.1
screen.exitonclick()
