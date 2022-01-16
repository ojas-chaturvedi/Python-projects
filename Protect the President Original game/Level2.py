import turtle, time, winsound, math, os
level = 2

turtle.register_shape("shooter.gif")
turtle.register_shape("alien.gif")
turtle.register_shape("shelter.gif")
turtle.register_shape("president.gif")
turtle.register_shape("kidnap president.gif")

screen = turtle.Screen()
screen.setup(800, 350)
screen.bgpic("background.gif")
screen.title("Protect the President Level " + str(level) + " by Ojas Chaturvedi")

president = turtle.Turtle()
president.shape("president.gif")
president.hideturtle()

score = 0
scorePen = turtle.Turtle()
scorePen.speed(0)
scorePen.color("pink")
scorePen.penup()
scorePen.goto(-375, 150)
scoreString = "Score: %s" % score
scorePen.write(scoreString, False, align="left", font=('Arial', 14, 'normal'))
scorePen.hideturtle()

shooter = turtle.Turtle()
shooter.penup()
shooter.shape("shooter.gif")
shooter.speed(0)
shooter.goto(-300, -100)
shooterspeed = 25
gravity = 1

numberAliens = 8
aliens = []
for i in range(numberAliens):
    aliens.append(turtle.Turtle())

s = -80

for alien in aliens:
    alien.shape("alien.gif")
    alien.penup()
    alien.speed(0)
    alien.goto(450, s)
    s += 25.625
alienspeed = 2.5

bullet = turtle.Turtle()
bullet.hideturtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.shapesize(0.5, 0.5)
bullet.penup()
bullet.speed(0)
bulletspeed = 20
bulletstate = "ready"

def fire():
    global bulletstate
    if bulletstate == 'ready':
        winsound.PlaySound("Gun+Luger.wav", winsound.SND_ASYNC)
        bulletstate = "fire"
        bullet.goto(shooter.xcor() + 40, shooter.ycor() + 25)
        bullet.showturtle()

def left():
    shooter.setx(shooter.xcor() - shooterspeed)
    if shooter.xcor() <= -325:
        shooter.setx(-325)

def right():
    shooter.setx(shooter.xcor() + shooterspeed)
    if shooter.xcor() >= 325:
        shooter.setx(325)

def jump():
    shooter.sety(shooter.ycor() + 100)
    if shooter.ycor() >= 125:
        shooter.sety(125)

def descend():
    shooter.sety(shooter.ycor() - 10 )

def Collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance <= 15:
        return True
    else:
        return False

shelter = turtle.Turtle()
shelter.hideturtle()
shelter.speed(0)
shelter.shape("shelter.gif")
shelter.penup()
smashwall = 0
showshelter=False

def wall():
    global showshelter
    if shooter.xcor() + 200 <= alien.xcor():
        shelter.goto(shooter.xcor() + 200, shelter.ycor())
    else:
        shelter.goto(alien.xcor()-100, alien.ycor())
    shelter.showturtle()
    showshelter=True

def failScreen():
    screen.setup(370, 370)
    screen.bgpic("alien kidnapping.gif")
    president.shape("kidnap president.gif")
    president.goto(0, -20)
    president.showturtle()
    time.sleep(3)
    screen.bye()
    os.system("python main.py")

screen.onkey(fire, "space")
screen.onkey(left, "a")
screen.onkey(right, "d")
screen.onkey(jump, "w")
screen.onkey(descend, "s")
screen.onkey(wall, "q")
screen.listen()

while True:
    shooter.sety(shooter.ycor() - gravity)
    if shooter.ycor() <= -100:
        shooter.sety(-100)
        pass
    for alien in aliens:
        alien.setx(alien.xcor() - alienspeed)
        if alien.xcor() == -325:
            winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
            shooter.hideturtle()
            shelter.hideturtle()
            scorePen.penup()
            scorePen.goto(0, 0)
            scorePen.color("red")
            scorePen.write("You failed your job", False, align="center", font=('Arial', 24, 'normal'))
            failScreen()
        if bulletstate == "fire":
            if Collision(bullet, alien):
                bullet.hideturtle()
                winsound.PlaySound("explosion.wav", winsound.SND_ASYNC)
                alien.goto(1000, 1000)
                bulletstate = "ready"
                score += 10
                scoreString = "Score: %s" % score
                scorePen.clear()
                scorePen.write(scoreString, False, align="left", font=('Arial', 14, 'normal'))
                if score == 80:
                    shooter.hideturtle()
                    shelter.hideturtle()
                    scorePen.clear()
                    screen.setup(1200, 800)
                    screen.bgpic("flag.gif")
                    president.showturtle()
                    scorePen.penup()
                    scorePen.goto(0, 0)
                    scorePen.color("red")
                    scorePen.write("You saved the president", False, align="center", font=('Arial', 24, 'normal'))
                    time.sleep(3)
                    screen.bye()
                    os.system("python Level3.py")
        if showshelter==True:
            if shelter.xcor() + 100 == alien.xcor():
                alienspeed =0
                smashwall += 1
                if smashwall == 50:
                    shelter.hideturtle()
                    alienspeed = 2.5
                    showshelter=False
    bullet.setx(bullet.xcor() + bulletspeed)
    if bullet.xcor() >= 450:
        bullet.hideturtle()
        bulletstate = "ready"
