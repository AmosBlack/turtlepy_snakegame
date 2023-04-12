from tkinter import CENTER
from tkinter.font import BOLD
import turtle
import random
import time
from xxlimited import new

#setup
screen = turtle.Screen()
screen.title("SnakeGame")
screen.setup(width=600,height=630)
screen.tracer(0)
turtle.bgcolor('green')

#border
turtle.speed(5)
turtle.pensize(5)
turtle.penup()
turtle.goto(290,-290)
turtle.pendown()
turtle.left(90)
turtle.forward(585)
turtle.left(90)
turtle.forward(585)
turtle.left(90)
turtle.forward(585)
turtle.left(90)
turtle.forward(585)
turtle.penup()
turtle.hideturtle()

#SNAKE
snake = turtle.Turtle()
snake.shape('circle')
snake.speed(0)
snake.color("blue")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#FRUIT
fruit = turtle.Turtle()
fruit.shape('circle')
fruit.speed(0)
fruit.color('red')
fruit.penup()
fruit.goto(50,50)

#SCORING
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color('white')
scoring.penup()
scoring.goto(0,280)
scoring.write('Score:0', align="center",font=("Courier",24,"bold"))

#FRUIT
score = 0
old_fruit = []

#FUNCTIONS-MOVEMENT
def snake_up():
    if snake.direction != "down":
        snake.direction = "up"
def snake_down():
    if snake.direction != 'up':
        snake.direction = "down"
def snake_left():
    if snake.direction != "right":
        snake.direction = "left"
def snake_right():
    if snake.direction != "left":
        snake.direction = "right"

def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y+20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y-20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x-20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x+20)

screen.listen()
screen.onkeypress(snake_up,"Up")
screen.onkeypress(snake_down,"Down")
screen.onkeypress(snake_left,"Left")
screen.onkeypress(snake_right,"Right")

delay = 0.1

def game_over():
    time.sleep(1)
    screen.clear()
    screen.bgcolor('turquoise')
    scoring.goto(0,0)
    scoring.write("   GAME OVER \n Your Score is {}".format(score),align='center',font=("Courier",30,"bold"))

#run
while True:   
    if snake.distance(fruit)<20:
        x = random.randint(-290,270)
        y = random.randint(-240,240)
        fruit.goto(x,y)
        scoring.clear()
        score+=1
        scoring.write(f"Score:{score}",align="center",font=("Courier",24,"bold"))
        delay -= 0.001

        #creating new fruit
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape('square')
        new_fruit.color('blue')
        new_fruit.penup()
        old_fruit.append(new_fruit)

    for index in range(len(old_fruit)-1,0,-1):
        a = old_fruit[index-1].xcor()
        b = old_fruit[index-1].ycor()
        old_fruit[index].goto(a,b)
    if len(old_fruit)>0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a,b)
       
    snake_move()

    #snake/border collisions
    if snake.xcor()>280 or snake.xcor() < -290 or snake.ycor()>290 or snake.ycor() < -290:
        game_over()

    for food in old_fruit:
        if food.distance(snake) < 20:
            game_over()




    screen.update()
    time.sleep(delay)   

turtle.Terminator() 