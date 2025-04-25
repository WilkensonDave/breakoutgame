from turtle import Turtle
import random

MOVE_DISTANCE = 10
#class to create the ball
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.move_speed = 0.1
        self.reset_game_position()
    
    #this function will control how the ball moves while the game is on and when it hits the walls or the paddle   
    def move_ball(self):
        random_x = self.xcor() + self.x_move
        random_y = self.ycor() + self.y_move
        self.goto(random_x, random_y)
    
    
    #control how the game will bounce  when it hits the walls, or even the paddle
    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_move *=-1
        
        if y_bounce:
            self.y_move *=-1
            
    #Make the game move faster    
    def move_faster(self):
        self.move_speed *=0.1
        
    #Reset the game to make it goes to initial position
    def reset_game_position(self):
        self.goto(x=0, y=-240)
        self.y_move = 10
        
