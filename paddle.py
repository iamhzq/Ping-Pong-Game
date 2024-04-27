from turtle import Turtle

position = [(350, 0), (-350, 0)]


class Paddle():
    def __init__(self):
        self.paddle_no = []
        self.create_paddle()
        self.p_1=self.paddle_no[0]
        self.p_2 = self.paddle_no[1]


    def add_paddle(self,pos):
        t = Turtle("square")
        t.color("white")
        t.shapesize(stretch_wid=5, stretch_len=1, outline=1)
        t.speed("fast")
        t.up()
        t.goto(pos)
        self.paddle_no.append(t)

    def create_paddle(self):
        for pos in position:
            self.add_paddle(pos)

    def up(self):
        new_y=self.p_2.ycor() + 30
        self.p_2.goto(self.p_2.xcor(),new_y)
    def down(self):
        new_y = self.p_2.ycor() - 30
        self.p_2.goto(self.p_2.xcor(), new_y)

    def up_2(self):
        new_y = self.p_1.ycor() + 30
        self.p_1.goto(self.p_1.xcor(), new_y)

    def down_2(self):
        new_y = self.p_1.ycor() - 30
        self.p_1.goto(self.p_1.xcor(), new_y)






