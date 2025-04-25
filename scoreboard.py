from turtle import Turtle

try:
    score = int(open("high_score.txt", "r").read())
except FileNotFoundError:
    score = int(open("high_score.txt", "w").write(str(0)))
except ValueError:
    score = 0
FONT = ('arial', 18, 'normal')


#class to create the scoreboard and put it at the stop of the screen
class Scoreboard(Turtle):
    def __init__(self, lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.highScore = score
        self.goto(x=-580, y=250)
        self.lives = lives
        self.score = 0
        self.update_score()
    
    #this method will be responsible to update the score on the page when the user loses the game
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} | Highest Score:\
            {self.highScore} | Lives: {self.lives}", align='left', font=FONT)
    
    #each time the ball hits a brick the score will be increased by 1   
    def increase_score(self):
        self.score += 1
        if self.score > self.highScore:
            self.highScore += 1
    
    #when the hit the bottom of the screen below the specified y and x positions 
    # the number of lives will be decreased by 1      
    def decrease_lives(self):
        self.lives -= 1
        self.update_score()
    
    #when the number of lives is zero the game is stop 
    # and the highest score will be saved inside the HighestScore.txt file     
    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()
        open("HighestScore.txt", 'w').write(str(self.highScore))
        