#!/usr/bin/env python3

import turtle
import time as t

window = turtle.Screen()
window.screensize(400, 400)
window.setworldcoordinates(0, 0, 400, 400)

turtle = turtle.Turtle()
turtle.color("red")
turtle.up()
turtle.hideturtle()
turtle.speed(0)


def drawRectangle(x, y, width, height):
    turtle.up()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.down()
    turtle.goto(x + width, y)
    turtle.goto(x + width, y + height)
    turtle.goto(x, y + height)
    turtle.goto(x, y)
    turtle.up()
    turtle.end_fill()


def drawRectangleInverse(x, y, width, height):
    turtle.up()
    turtle.goto(x, y)
    turtle.begin_fill()
    turtle.down()
    turtle.goto(x + height+width, y)
    turtle.goto(x + width+height, y + height-width)
    turtle.goto(x, y+width+height)
    turtle.goto(x, y)
    turtle.up()
    turtle.end_fill()


def drawBrickWall(rows, cols, brickWidth, brickHeight, mortarWidth):
    y = 0
    for _ in range(rows):
        x = 0
        for _ in range(cols):
            drawRectangle(x, y, brickWidth, brickHeight)
            x += (brickWidth + mortarWidth)
        y += (brickHeight + mortarWidth)


def drawBrickWallOffset(rows, cols, brickWidth, brickHeight, mortarWidth):
    y = 0
    brickWidth_offset = brickWidth + \
        (mortarWidth/2)-(0.5*brickWidth) - mortarWidth
    for s in range(rows):
        if s % 2 == 0:
            x = 0
            for i in range(cols):
                drawRectangle(x, y, brickWidth, brickHeight)
                x += (brickWidth + mortarWidth)
        else:
            x = brickWidth+(mortarWidth/2)-(0.5*brickWidth)
            for i in range(cols):
                if i == cols-1:
                    drawRectangle(x, y, brickWidth_offset, brickHeight)
                else:
                    drawRectangle(x, y, brickWidth, brickHeight)
                    x += (brickWidth + mortarWidth)
            x = 0
            drawRectangle(x, y, brickWidth_offset, brickHeight)
        y += (brickHeight + mortarWidth)


def drawCoolWall(rows, cols, brickWidth, brickHeight, mortarWidth):
    y = brickHeight
    brickWidth_offset = brickWidth + \
        (mortarWidth/2)-(0.5*brickWidth) - mortarWidth
    for s in range(rows):
        if s % 2 == 0:
            x = 0
            for i in range(cols):
                drawRectangleInverse(x, y, brickWidth, brickHeight)
                x += (brickWidth + mortarWidth)
        else:
            x = brickWidth+(mortarWidth/2)-(0.5*brickWidth)
            for i in range(cols):
                if i == cols-1:
                    drawRectangleInverse(x, y, brickWidth_offset, brickHeight)
                else:
                    drawRectangleInverse(x, y, brickWidth, brickHeight)
                    x += (brickWidth + mortarWidth)
            x = 0
            drawRectangleInverse(x, y, brickWidth_offset, brickHeight)
        y += (brickHeight + mortarWidth) + brickHeight


def main():
    rows = int(input('Insert the amount of rows: '))
    cols = int(input('Insert the integer amount of columns: '))
    brickWidth = int(
        input('Insert the integer amount of the width of the bricks: '))
    brickHeight = int(
        input('Insert the integer amount of the height of the bricks: '))
    mortarWidth = int(input(
        'Insert the integer amount of how much space you want between the bricks: '))
    drawBrickWall(rows, cols, brickWidth, brickHeight, mortarWidth)
    t.sleep(5)
    window.clear()
    drawBrickWallOffset(rows, cols, brickWidth, brickHeight, mortarWidth)
    t.sleep(5)
    window.clear()
    drawCoolWall(rows, cols, brickWidth, brickHeight, mortarWidth)
    window.exitonclick()
    window.mainloop()


if __name__ == "__main__":
    main()
