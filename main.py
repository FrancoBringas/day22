from turtle import Screen,Turtle
from paddle import Paddle
MOVE_DISTANCE = 20
X=350
Y=0
game = True
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong game")
# screen.tracer(0)


screen.listen()

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(X, new_y)
def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(X, new_y)
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

while game:
    screen.update()
screen.exitonclick()
