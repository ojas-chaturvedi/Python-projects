import turtle
import time
import random

delay = .065

score = 0
high_score = 0

#screen
screen = turtle.Screen()
screen.title("Snake game by SaltiestOrange4")
screen.bgcolor("green")
screen.setup(width=600, height = 600)
screen.tracer(0)

#snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.penup()
head.goto(0,0)
head.direction = 'stop'

bodyParts = []

#food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

#score keeper
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

#Functions
def goUp():
    if head.direction != "down":
        head.direction = "up"
    
def goDown():
    if head.direction != "up":
        head.direction = "down"
    
def goLeft():
    if head.direction != "right":
        head.direction = "left"
    
def goRight():
    if head.direction != "left":
        head.direction = "right"
    
def move():
    if head.direction == 'up':
        head.sety(head.ycor() + 20)
    elif head.direction == 'down':
        head.sety(head.ycor() - 20)
    elif head.direction == 'left':
        head.setx(head.xcor() - 20)
    elif head.direction == 'right':
        head.setx(head.xcor() + 20)        
        
#Keybinds
screen.listen()
screen.onkey(goUp, "w")
screen.onkey(goDown, "s")
screen.onkey(goLeft, "a")
screen.onkey(goRight, "d")

#main game
while True:
    screen.update()
    
    #border collisions
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for bodyPart in bodyParts:
            bodyPart.goto(1000,1000)
            
        bodyParts.clear()
        
        score = 0
        
        delay = .075
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    if head.distance(food) < 20:
        food.goto(random.randint(-290, 290),random.randint(-290, 290))

        new_part = turtle.Turtle()
        new_part.speed(0)
        new_part.shape("square")
        new_part.color("grey")
        new_part.penup()
        bodyParts.append(new_part)
        
        delay -= .001
        
        score += 10
        
        if score >= high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
    for index in range(len(bodyParts)-1,0,-1):
        bodyParts[index].goto(bodyParts[index-1].xcor(), bodyParts[index-1].ycor())
    
    if len(bodyParts) > 0:
        bodyParts[0].goto(head.xcor(),head.ycor())
    
    move()
    
    for bodyPart in bodyParts:
        if bodyPart.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            for bodyPart in bodyParts:
                bodyPart.goto(1000, 1000)
        
            bodyParts.clear()

            score = 0

            delay = 0.1
        

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    time.sleep(delay)

screen.mainloop()
