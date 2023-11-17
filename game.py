from turtle import Screen, Turtle
from scoreboard import ScoreBoard
from paddle import Paddle
from ball import Ball
import time
import random

screen = Screen()
screen.setup(height=600, width=1000)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
game_on = True

screen.listen()

# initialize objects
p1 = Paddle()
p1.goto(-486, 0)

p2 = Paddle()
p2.goto(480, 0)

ball = Ball()

score = ScoreBoard()



# Controls
screen.onkey(p2.up, "Up")  
screen.onkey(p2.down, "Down")

screen.onkey(p1.up, "w")  
screen.onkey(p1.down, "s")



# Game Functions
while game_on:
    
    # Detect if somebody has won
    if score.score1 > 5:
        score.game_over("Player 1")
        game_on = False
        ball.hide()
    elif score.score2 > 5:
        score.game_over("Player 2")
        game_on = False
        ball.hide()

    # Detect collision with paddle
    if ball.distance(p1.pad) < 50:
        ball.hit_pad1()
        
    elif ball.distance(p2.pad) < 50:
        ball.hit_pad2()
        
    # Detect collision with wall for point
    if ball.xcor() < -490 or ball.xcor() > 490:
        if ball.xcor() < -490:
            score.add_point_b()
            p1.goto(-486, 0)
            p2.goto(480, 0)
            ball.reset()
            
        elif ball.xcor() > 490:
            score.add_point_a()
            p1.goto(-486, 0)
            p2.goto(480, 0)
            ball.reset()
            
    # Detect collision with wall for bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        if ball.ycor() < -280:
            if ball.direction == 0:
                ball.bounce(10, 30)
                
            elif ball.direction == 180:
                ball.bounce(150, 170)
      
        elif ball.ycor() > 280:
            if ball.direction == 0:
                ball.bounce(330, 350)

            elif ball.direction == 180:
                ball.bounce(190, 210)
                
    screen.update()
    time.sleep(0.05)
    ball.move()


                
                


            
        


screen.exitonclick()