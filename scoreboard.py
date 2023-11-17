from turtle import Turtle
import random

FONT = "Arial"
SIZE = 24

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-20, 260) 
        self.color("white")
        self.score1 = 0
        self.score2 = 0

        arg = f"{str(self.score1)} : {str(self.score2)}"
        self.write(arg, False, "left", (FONT, SIZE, "normal"))
    
    def add_point_a(self):
        self.score1 += 1
        arg = f"{str(self.score1)} : {str(self.score2)}"
        self.clear()
        self.write(arg, False, "left", (FONT, SIZE, "normal"))
        
    def add_point_b(self):
        self.score2 += 1
        arg = f"{str(self.score1)} : {str(self.score2)}"
        self.clear()
        self.write(arg, False, "left", (FONT, SIZE, "normal"))
        
    def game_over(self, winner):
        self.goto(0, 0)
        self.color("red")
        self.write(f"{winner} WINS!!!", False, "center", (FONT, SIZE, "normal"))