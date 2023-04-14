from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("pink")
        self.shape("circle")
        self.penup()
        self.x_move=0.3
        self.y_move=0.3

    def move(self):
        new_x = self.xcor()+self.x_move
        new_y = self.ycor()+self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move*=-1
        # new_x= self.xcor()-0.2
        # new_y= self.ycor()-0.2
        # self.goto(new_x,new_y)
    def bounce_x(self):
        self.x_move*=-1

    def reset_ball(self):
        self.goto(0,0)
        self.bounce_x()