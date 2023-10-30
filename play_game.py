import time
from divider import Divider
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG")
screen.tracer(0)

player_1_paddle = Paddle((-370, 0))    
player_2_paddle = Paddle((370, 0))
pong_ball = Ball()                     
scoreboard = Scoreboard()              
divider = Divider()

screen.listen()
screen.onkeypress(player_1_paddle.go_up, "w")       
screen.onkeypress(player_1_paddle.go_down, "s")

screen.onkeypress(player_2_paddle.go_up, "Up")      
screen.onkeypress(player_2_paddle.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(pong_ball.move_speed)        
    screen.update()
    pong_ball.move()                        

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce()

    if (pong_ball.distance(player_1_paddle) < 50 and pong_ball.xcor() < -340 or
            pong_ball.distance(player_2_paddle) < 50 and pong_ball.xcor() > 340):
        pong_ball.rebound()

    if pong_ball.xcor() > 380:
        pong_ball.reset_position()
        scoreboard.p1_point()

    if pong_ball.xcor() < -380:
        pong_ball.reset_position()
        scoreboard.p2_point()

    if scoreboard.p1_score == 5 or scoreboard.p2_score == 5:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
