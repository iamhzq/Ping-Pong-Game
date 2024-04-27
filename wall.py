from turtle import Turtle

class Wall(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1,stretch_len=40,outline=1)
        self.pu()
        self.goto(pos)