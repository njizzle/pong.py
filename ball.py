from turtle import Turtle
import random

MPH = 20
INCREMENT = 0

LEFT = 180
RIGHT = 0

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed = MPH
        self.goto(0, 0)
        self.direction = 0
        
    def reset(self):
        self.goto(0,0)
        self.setheading(self.direction)
        
    def move(self):
        self.forward(self.speed)
    
    def bounce(self, x, y):
        angle = random.randint(x, y)
        self.setheading(angle)
        # self.forward(40)
        
    def hide(self):
        self.hideturtle()
        
    def hit_pad1(self):
        angle = random.randint(-45, 45)
        self.direction = RIGHT
        self.setheading(angle)
        self.speed += INCREMENT
        
    def hit_pad2(self):
        angle = random.randint(135, 225)
        self.direction = LEFT
        self.setheading(angle)
        self.speed += INCREMENT

        

        
    
