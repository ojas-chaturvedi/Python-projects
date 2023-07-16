import turtle
import winsound
import math
import random

score = 0
scorePen = turtle.Turtle()
scorePen.speed(0)
scorePen.color("white")
scorePen.penup()
scorePen.goto(-290,275)
scoreString = "Score: %s" %score
scorePen.write(scoreString, False, align = "left", font = ('Arial',14,'normal'))
scorePen.hideturtle()

screen = turtle.Screen()
screen.setup(700,700)
screen.bgcolor('black')
screen.bgpic("background.gif")
screen.title("Space Invaders")

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
    border.forward(600)
    border.left(90)
border.hideturtle()

player = turtle.Turtle()
player.speed(0)
player.color("red")
player.shape("player.gif")
player.penup()
player.goto(0,-250)
player.left(90)
playerspeed = 15

numberEnemy = 5
enemies = []
for i in range(numberEnemy):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.speed(0)
    enemy.color("green")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.goto(random.randint(-200,200),random.randint(100,250))
enemyspeed = 2


bullet = turtle.Turtle()
bullet.speed(0)
bullet.hideturtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.left(90)
bullet.shapesize(0.5,0.5)
bulletspeed = 20
bulletstate = "ready"

def fire():
    global bulletstate
    if bulletstate == 'ready':
        winsound.PlaySound("shoot.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        bullet.goto(player.xcor(), player.ycor() + 10)
        bullet.showturtle()

def left():
    player.setx(player.xcor() - playerspeed)
    if player.xcor() <= -280:
        player.setx(-280)

def right():
    player.setx(player.xcor() + playerspeed)
    if player.xcor() >= 280:
        player.setx(280)

def Collision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance <= 15:
        return True
    else:
        return False


screen.onkey(left,"Left")
screen.onkey(right, "Right")
screen.onkey(fire, "space")
screen.listen()


while True:
    for enemy in enemies:
        enemy.setx(enemy.xcor() + enemyspeed)
        if enemy.xcor() >= 280 or enemy.xcor() <= -280:
            enemyspeed *= -1
            for e in enemies:
                e.sety(e.ycor() - 50)
                if e.ycor() >= -260 and e.ycor() <= -240:
                    winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
                    player.hideturtle()
                    enemy.hideturtle()
                    scorePen.penup()
                    scorePen.goto(0, 0)
                    scorePen.write("Game Over", False, align="left", font=('Arial', 14, 'normal'))

        if Collision(bullet, enemy):
            bullet.hideturtle()
            winsound.PlaySound("invaderkilled.wav", winsound.SND_ASYNC)
            bulletstate = "ready"
            bullet.goto(0, -400)
            enemy.goto(random.randint(-200,200),random.randint(100,250))
            score += 10
            scoreString = "Score: %s" %score
            scorePen.clear()
            scorePen.write(scoreString, False, align="left", font=('Arial', 14, 'normal'))

    # if bulletstate = "fire":
    bullet.sety(bullet.ycor() + bulletspeed)
    if bullet.ycor() >= 275:
        bullet.hideturtle()
        bulletstate = "ready"
