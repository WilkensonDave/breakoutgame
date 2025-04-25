from turtle import Turtle
import random

COLOR_LIST = [
    'light blue', 'royal blue', 'light steel blue', 'steel blue', 'light yellow', 'light sky blue',
    "violet", 'salmon', 'tomato', 'sandy brown', 'purple', 'deep pink', 'medium sea green', 'orange', 'light green'
]

weights = [1, 2, 1, 1, 3, 2, 1, 4, 1, 3, 1, 1, 1, 4, 1, 3, 2, 2, 1, 2, 1, 1, 2, 1, 2, 1]

#class to define the breaks
class Brick(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=3)
        self.color(random.choice(COLOR_LIST))
        self.goto(x=x_cor, y=y_cor)
        
        #each brick that is builded will have a weight and 
        # their weight will be how many times they will 
        # need to be hit by the ball before removing from 
        # the list and disappear from the screen
        self.quantity = random.choice(weights)
        
        #each brick that will be created will have a border 
        # and if the border is touching by the ball it will still remove based on the weight 
        self.left_border = self.xcor() - 30
        self.right_border = self.xcor() + 30
        self.upper_border = self.ycor() + 15
        self.bottom_border = self.ycor() - 15


#class to create the bricks and we use the class to define the  bricks andi it can be created. 
class Bricks:
    def __init__(self):
        self.y_start = 0
        self.y_end = 240
        self.bricks_list = []
        self.create_all_lanes()
        
    #this method is responsible to create the line of bricks
    def create_lane(self, y_cor):
        for i in range(-570, 570, 30):
            brick = Brick(i, y_cor)
            self.bricks_list.append(brick)

    #this method is responsible to create position for each line
    def create_all_lanes(self):
        for i in range(self.y_start, self.y_end, 32):
            self.create_lane(i)
    
        
        