import turtle as tl
from ball import Ball
from paddle import Paddle
from board import UI
from bricks import Brick
from bricks import Bricks
from scoreboard import Scoreboard
import time

screen = tl.Screen()
screen.setup(width=1200, height=700)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)

ui = UI()
ui.header()

score = Scoreboard(lives=5)
paddle = Paddle()
# brick = Brick()
bricks = Bricks()

ball = Ball()

game_paused = False
playing_game = True

def pause_game():
    global game_paused
    if game_paused:
        game_paused = False
    else:
        game_paused = True

screen.listen()


def key_press():
    screen.onkey(key="Left", fun=paddle.move_left)
    screen.onkey(key="Right", fun=paddle.move_right)
    screen.onkey(key="space", fun=pause_game)

key_press()

#Detect collission with the walls
def check_collision_with_walls():
    global ball, score, playing_game, ui
    if ball.xcor() < -580 or ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        # ball.bounce_x_position()
    
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
        # ball.bounce_y_position()
        
    if ball.ycor() < -280:
        ball.reset_game_position()
        score.decrease_lives()
        if score.lives == 0:
            score.reset()
            playing_game = False
            ui.game_over(win=False)
            return 
        ui.change_color()
        return
            

#Detect collission with the paddle
def check_collision_with_paddle():
    global ball, paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()
    
    if ball.distance(paddle) < 110 and ball.ycor() < -250:
        if paddle_x > 0:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                # ball.bounce_x_position()
                # ball.bounce_y_position()
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                # ball.bounce_y_position()
                return   
            
        elif paddle_x < 0:
            if ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                # ball.bounce_x_position()
                # ball.bounce_y_position()
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                # ball.bounce_y_position()
                return
        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=False)
                # ball.bounce_x_position()
                # ball.bounce_y_position()
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                # ball.bounce_x_position()
                # ball.bounce_y_position()
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                # ball.bounce_y_position()
                return


#function to check when the ball collid with the bricks
def check_collision_with_bricks():
    global ball, score, bricks
    for brick in bricks.bricks_list:
        #check if the ball hit the brick
        if ball.distance(brick) < 40:
            score.increase_score()
            #decrease the brick quantity
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(4000, 4000)
                bricks.bricks_list.remove(brick)
                
            if ball.xcor() < brick.left_border:
                ball.bounce(x_bounce=True, y_bounce=False)
                # ball.bounce_x_position()
            
            elif ball.xcor() > brick.right_border:
                ball.bounce(x_bounce=True, y_bounce=False)
                # ball.bounce_x_position()
            
            elif ball.ycor() < brick.bottom_border:
                ball.bounce(x_bounce=True, y_bounce=False)
                # ball.bounce_y_position()
                
            elif ball.ycor() > brick.upper_border:
                ball.bounce(x_bounce=True, y_bounce=False)
                # ball.bounce_y_position()
        

#Keep the game playing up until the user loses or the pause button is pressed.
def keep_playing():
    while playing_game:
        if not game_paused:
            screen.update()
            time.sleep(0.01)
            ball.move_ball()
            
            #Detect collision with walls
            check_collision_with_walls()
            
            #Detect collision with paddle
            check_collision_with_paddle()
            
            #Detect collision with bricks
            check_collision_with_bricks()
            
            #Detect winner
            if len(bricks.bricks_list) == 0:
                ui.game_over(win=True)
                break
        else:
            ui.paused_game()

keep_playing()        
                 
screen.mainloop() 