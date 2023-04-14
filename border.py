from turtle import  Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-385, 290)
        self.color("blue")
        self.pendown()

    def draw_border(self):
        for i in range(2):
            self.forward(770)
            self.right(90)
            self.forward(580)
            self.right(90)