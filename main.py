import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from wall import Wall
from score import Score

sc=Screen()
sc.title("Pong Game")
sc.setup(800, 600)
sc.bgcolor("black")
sc.tracer(0)
p = Paddle()
b = Ball()
w1 = Wall((0, 290))
w2 = Wall((0, -290))
scoreboard=Score()

speed=0.0001

sc.listen()
sc.onkeypress(p.up, "w")
sc.onkeypress(p.down, "s")
sc.onkeypress(p.up_2, "Up")
sc.onkeypress(p.down_2, "Down")


is_game_on=True
while is_game_on:
    sc.update()
    b.move()
    time.sleep(0.04-speed)
    #collision with wall
    if b.ycor() > 280 or b.ycor() < -280:
       b.bounce_y()

    #collision with paddle
    if b.distance(p.p_1) < 50 and b.xcor() > 330 or b.distance(p.p_2) < 50 and b.xcor() < -330:
        b.bounce_x()
        speed *= 0.9

    #ball misses the right paddle
    if b.xcor() > 380 :
       b.reset_postion()
       speed=0
       scoreboard.l_point()
    # ball misses the left paddle
    if b.xcor() < -380 :
        b.reset_postion()
        speed=0
        scoreboard.r_point()







sc.exitonclick()