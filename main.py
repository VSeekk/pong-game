from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen= Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle= Paddle(-350,0, "red")
r_paddle= Paddle(350,0, "blue")
ball =Ball()
scoreboard= ScoreBoard()


# def up():
#     new_y = paddle.ycor() + 20
#     paddle.goto(paddle.xcor(), new_y)
#
#
# def down():
#     new_y = paddle.ycor() - 20
#     paddle.goto(paddle.xcor(), new_y)


# paddle = Turtle()
# paddle.shape("square")
# paddle.color("red")
# paddle.shapesize(stretch_wid=5,  stretch_len=1)
# paddle.penup()
# paddle.goto(350, 0)
# screen.update()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

is_game_on= True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    #  to bounce the ball from the walls
    if ball.ycor() >290 or ball.ycor()< -300:
        ball.bounce_y()

    # to bounce the ball when it collides with the paddle
    if ball.distance(r_paddle)<50 and ball.xcor()> 320 or ball.distance(l_paddle)<50 and ball.xcor()< -320:
        ball.bounce_x()

    # detect when the ball goes outside the boundary
    if ball.xcor()> 400 :
        ball.reset_ball()
        scoreboard.l_score_increase()
    if  ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_score_increase()


screen.exitonclick()