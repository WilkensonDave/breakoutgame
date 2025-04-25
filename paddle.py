from turtle import Turtle

#the distance the paddle will be move from
MOVE_DIST = 70


#class to define the paddle and create it as well
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=15, stretch_wid=1)
        self.goto(x=0, y=-280)
    
    #define how the paddle will be moved from left to right
    def move_left(self):
        self.backward(MOVE_DIST)
        
    #define how the paddle will be moved from rigt to left
    def move_right(self):
        self.forward(MOVE_DIST)