#!/usr/bin/env python3

import turtle as t
wn = t.Screen()
wn.title('Pong game')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer()
board_maker = t.Turtle()
board_maker.speed(0)
board_maker.color("grey")
board_maker.shape("square")
board_maker.sety(300)
board_maker.goto(0, -300)
board_maker.setx(-400)
board_maker.sety(300)
for _ in range(2):
    board_maker.fd(800)
    board_maker.right(90)
    board_maker.fd(600)
    board_maker.right(90)
board_maker.hideturtle()


class Score:
    def __init__(self):
        self.writer = t.Turtle()
        self.writer.speed(0)
        self.writer.color("white")
        self.writer.hideturtle()
        self.writer.penup()
        self.writer.goto(0, 250)
        self.score_a = 0
        self.score_b = 0

    def printScore(self):
        self.writer.clear()
        self.writer.write('{}  {}'.format(self.score_a, self.score_b),
                          align='center', font=('Times New Roman', 48, "normal"))


class Paddle:
    def __init__(self, x, y):
        self.paddle = t.Turtle()
        self.paddle.speed(0)
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.x = x
        self.y = y
        self.gotoInitialPosition()

    def gotoInitialPosition(self):
        self.paddle.penup()
        self.paddle.goto(self.x, self.y)

    def paddleUp(self):
        self.y = self.paddle.ycor()
        self.y += 20
        self.paddle.sety(self.y)

    def paddleDown(self):
        self.y = self.paddle.ycor()
        self.y -= 20
        self.paddle.sety(self.y)


class Ball:
    def __init__(self, score_class):
        self.ball = t.Turtle()
        self.ball.speed(0)
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.penup()
        self.dx = 2.5
        self.dy = 2.5
        self.score_class = score_class

    def main(self, left_paddle, right_paddle):
        self.ball.setx(self.ball.xcor() + self.dx)
        self.ball.sety(self.ball.ycor() + self.dy)
        self.checkCeilingAndFloorBounce()
        self.checkGoal()
        self.checkPaddleBounce(left_paddle, right_paddle)

    def checkGoal(self):
        if self.ball.xcor() > 390 or self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.dx *= -1
            if self.ball.xcor() > 390:
                self.score_class.score_a += 1
            else:
                self.score_class.score_b += 1
            self.score_class.printScore()

    def checkCeilingAndFloorBounce(self):
        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.dy *= -1
        elif self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.dy *= -1

    def checkPaddleBounce(self, left_paddle, right_paddle):
        if (self.ball.xcor() > 340 and self.ball.xcor() < 350) and (self.ball.ycor() < right_paddle.paddle.ycor() + 50 and self.ball.ycor() > right_paddle.paddle.ycor() - 50):
            self.ball.setx(340)
            self.dx *= -1
        elif (self.ball.xcor() < -340 and self.ball.xcor() > -350) and (self.ball.ycor() < left_paddle.paddle.ycor() + 50 and self.ball.ycor() > left_paddle.paddle.ycor() - 50):
            self.ball.setx(-340)
            self.dx *= -1


def main():
    scorekeeper = Score()
    left_paddle = Paddle(-350, 0)
    right_paddle = Paddle(350, 0)
    ball = Ball(scorekeeper)
    scorekeeper.printScore()
    wn.listen()
    wn.onkeypress(left_paddle.paddleUp, 'w')
    wn.onkeypress(left_paddle.paddleDown, 's')
    wn.onkeypress(right_paddle.paddleUp, 'Up')
    wn.onkeypress(right_paddle.paddleDown, 'Down')
    while True:
        wn.update()
        ball.main(left_paddle, right_paddle)


if __name__ == '__main__':
    main()
