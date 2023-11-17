from turtle import Screen, Turtle
import time

UP = 90
DOWN = 270
SPEED = 40

class Paddle():

    def __init__(self):
        self.pad = Turtle("square")
        self.pad.shapesize(stretch_wid=6, stretch_len=1)
        self.pad.penup()
        self.pad.color("white")
        

    def goto(self, x, y):
        self.pad.goto(x,y)


    def up(self):   
            y = self.pad.ycor()
            y += SPEED
            self.pad.sety(y)
            
    def down(self):
            y = self.pad.ycor()
            y -= SPEED
            self.pad.sety(y)

