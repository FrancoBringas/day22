from turtle import Screen
from padle import Paddle
from ball import Ball
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
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
while game:
    screen.update()
    ball.move()
    time.sleep(0.1)
    if ball.ycor() > 280 or ball.ycor() < -280:
        screen.update()
        ball.bounce()
screen.exitonclick()
