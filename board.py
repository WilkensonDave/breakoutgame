from turtle import Turtle 
import time
import random

FONT= ("Courier", 52, "normal")
FONT2 = ("Courier", 32, "normal")
ALIGNMENT = 'center'
COLOR_LIST = [
    'light blue', 'royal blue', 'light steel blue', 'steel blue',  'light sky blue',
    'salmon', 'tomato', 'sandy brown', 'purple', 'deep pink', 'medium sea green', 'light green'
]

#class to create the board where the game will be played
class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(random.choice(COLOR_LIST))
        self.header()
    
    #display a message to give a hint to the player so they can know if the press the mentioned key the game will be paused
    def header(self):
        self.clear()
        self.goto(x=0, y=-150)
        self.write("Breakout", align=ALIGNMENT, font=FONT)
        self.goto(x=0, y=-180)
        self.write("Press Space to Pause or Resume the Game", align=ALIGNMENT, font=("Calibri", 14, 'normal'))
    
    #this function is responsible to change the color of some of the text while playing the game.
    def change_color(self):
        self.clear()
        self.color(random.choice(COLOR_LIST))
        self.header()
    
    #the game will stop when this function is executed
    def paused_game(self):
        self.clear()
        self.change_color()
        time.sleep(0.5)
    
    
    #if the lives is equal to zero the game will be over and the message will be displayed.
    def game_over(self, win):
        self.clear()
        if win == True:
            self.write("You've win the game", align='center', font=FONT)
        else:
            try:
                score = int(open("HighestScore.txt", "r").read())
            except FileNotFoundError as e:
                self.write(f"{e}", align="center", font=FONT)
            self.write("OUUPPS Game over!!\n", align="center", font=FONT)  
            self.write(f"Your highest score is: {score}", align='center', font=FONT)