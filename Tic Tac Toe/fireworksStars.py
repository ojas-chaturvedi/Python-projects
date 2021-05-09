def celebration():
    import turtle
    import random

    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.colormode(255)

    turtle = turtle.Turtle()
    turtle.speed(1000)
    turtle.hideturtle()

    turtle.color("white")
    for i in range(30):
      x = random.randint(-250, 250)
      y = random.randint(-250,250)
      turtle.penup()
      turtle.goto(x,y)
      turtle.pendown()

      size = random.randint(2, 8)
      for i in range(5):
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(72)


    for i in range(10):
      x = random.randint(-250, 250)
      y = random.randint(-250,250)
      turtle.penup()
      turtle.goto(x,y)
      turtle.pendown()

      turtle.pencolor(random.randint(0, 255),random.randint(0, 255),random.randint(0, 255))

      size = random.randint(30, 200)
      for i in range(36):
        turtle.forward(size)
        turtle.backward(size)
        turtle.left(10)
if __name__ == '__main__':
    celebration()