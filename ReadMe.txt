
My breakout game and how it works!
What was easy?
What was difficult?
What lesson a learn that will help me for my next projects?
how can i improve my code for the next time?
if i will start the game again what will ne my new approach?


*********************************************************************************************************
My breakout game and how it works!

For the game to work, i firstly created multiple files so i can create each part of the game and create a 
main file so i can combine all the order files together. (OOP)
This is just Python OOP concepts.

Inside the ball file, i create the logic for the ball to move and how it will bounce back when
it hits the paddle or when it hits the walls.
for example when it hits the left or right side of the screen, it will be bounced back. 
It is the same for the top of the screen, which is considered the Y axis, while the left
and the right side is considered as the X axis.

When the ball hits the bottom of the screen, it will decrease the lives, and let's say you have 5 lives.
that means if the ball hits the bottom 5 times, you will lose the game.
And when the ball hits the paddle, it will bounce back. 
Each time the ball breaks a brick that will increase the score.

Inside the board file, i created the logic to manage how users will interact with the code.
For instance, when the user loses the game, it will  display a message below on the bricks. 
to let the user know they have lost the game or win it and the game will stop right there.
The color of the text will be changed, and that will be chosen randomly.
The user will see a message in case they don't want to keep playing that 
tells them they can pause the game.


For the bricks, we created a bricks file so we can implement the logic
to create the bricks.

The color of each brick will be chosen randomly inside the color list.
And we have the weights, which means how many times the brick will need
to hit the ball in order to remove it from the screen.

For instance, if the weight is 2, then the brick will need to be hit
two times by the ball before it can be removed from the screen 
and so one for the others.

We also created a border for each brick that will be created. 
So if the ball hits any of the borders, it will still count
as a hit so the ball can disappear from the screen.

Inside of this file you will find two methods, one that has been created 
and inherit from the Turtle class, 
and another that has not. 
When this class is initialized, it will create the bricks with the properties that are defined for each of them; 
for example, border, quantity, color, etc.

The second class will be responsible for placing the bricks on the screen.
Define the number of bricks needed and how they will be displayed.
it also saves each brick that has been created inside a list.
Which will be used later to remove the one that has been hit by the ball on the screen.

Inside the second class, we define two methods; the first one will be responsible for the
number of bricks to be displayed on each line, and also the second one will be responsible for
the number of lines to be created.

The paddle file is responsible for creating the paddle. 
we have two methods there, one to move the paddle to the left
another one to move it to the right.

The scoreboard file is responsible for displaying the score on the screen.
and how they will be displayed, for example, the highest score text, the number of lives,
and the current score will be displayed on the top left of the screen.
And then each time the ball hits a brick, the score increases.
and when the lives are gone, the score saves inside the HighestScore text file.
If the new score is higher than the previous one, the file will be updated to the new score.


The main file is responsible for putting together all the logic.
and it will be responsible for connecting all the other files together
so the program can run.

The first function will be responsible for pausing the game when the user 
click on the space button. 

The keypress function is responsible for moving the paddle to the left
or to the right and also to pause the game.
********Read the main file to find some other details.******


Read the main file to find what was easy.
It was easy to create the screen using Turtle and also the paddle
It was not difficult to create these files and also this logic
But the next time I will have to build something using Turtle
these will be easier.



What was difficult?
It was a little bit difficult to make the logic work for the ball
and also to create the bricks
Even when i have done it, but due to a mistake in my logic, it was 
moving diagonally only, like only back and forth
I spent, like, two days on that
But with the help of google and Youtube  i found how to make that work

What lesson did I learn that will help me for my next projects?
This project teaches me how to use OOP concepts in an effective way
I also learned it is okay to not know everything as soon as you try
to solve it, you will understand better, and you will know how things work
you will learn how to connect multiple logics so you can have a functional program


how can i improve my code for the next time?
The next time i will try to design the program and try to 
break it dowm, i will try to solve it piece by piece so i can make it work.
And also i will be more confident to know i can ask for help or take a break
with code when the solution is difficult to find or the logic is difficult to implement

If i will start the game again, what will be my new approach?
I will try to break the game down and try to think about solving 
one solution at a time and look for help when it is required. other details.