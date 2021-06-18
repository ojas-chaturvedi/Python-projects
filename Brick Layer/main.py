import turtle
screen = turtle.Screen()
screen.screensize(400, 400)
screen.setworldcoordinates(0, 0, 400, 400)
drawer = turtle.Turtle()
drawer.color("red")
drawer.up()
drawer.hideturtle()
drawer.speed(0)
def drawRectangle(x, y, length, height):
    drawer.up()
    drawer.goto(x,y)
    drawer.begin_fill()
    drawer.down()
    drawer.goto(x + length, y)
    drawer.goto(x + length, y + height)
    drawer.goto(x, y + height)
    drawer.goto(x, y)
    drawer.up()
    drawer.end_fill()
def drawRectangleInverse(x, y, length, height):
    drawer.up()
    drawer.goto(x,y)
    drawer.begin_fill()
    drawer.down()
    drawer.goto(x + height+length, y)
    drawer.goto(x + length+height, y + height-length)
    drawer.goto(x, y+length+height)
    drawer.goto(x, y)
    drawer.up()
    drawer.end_fill()
def drawCoolWall(rows, cols, brickwidth, brickHeight, mortarWidth):
    y = brickHeight
    brickWidth_offset = brickWidth+(mortarWidth/2)-(0.5*brickWidth) - mortarWidth
    for s in range(rows):
        if s%2==0:
            x = 0
            for i in range(cols):
                drawRectangleInverse(x, y, brickWidth, brickHeight)
                x += (brickWidth + mortarWidth)
        else:
            x = brickWidth+(mortarWidth/2)-(0.5*brickWidth)
            for i in range(cols):
                if i==cols-1:
                    drawRectangleInverse(x, y, brickWidth_offset, brickHeight)
                else:
                    drawRectangleInverse(x, y, brickWidth, brickHeight)
                    x += (brickWidth + mortarWidth)
            x=0
            drawRectangleInverse(x, y, brickWidth_offset, brickHeight)
        y += (brickHeight + mortarWidth) + brickHeight
    pass
def drawBrickWallOffset(rows, cols, brickWidth, brickHeight, mortarWidth):
    y = 0
    brickWidth_offset = brickWidth+(mortarWidth/2)-(0.5*brickWidth) - mortarWidth
    for s in range(rows):
        if s%2==0:
            x = 0
            for i in range(cols):
                drawRectangle(x, y, brickWidth, brickHeight)
                x += (brickWidth + mortarWidth)
        else:
            x = brickWidth+(mortarWidth/2)-(0.5*brickWidth)
            for i in range(cols):
                if i==cols-1:
                    drawRectangle(x, y, brickWidth_offset, brickHeight)     
                else:
                    drawRectangle(x, y, brickWidth, brickHeight)
                    x += (brickWidth + mortarWidth)
            x=0
            drawRectangle(x, y, brickWidth_offset, brickHeight)
        y += (brickHeight + mortarWidth)
    pass
def drawBrickWall(rows, cols, brickWidth, brickHeight, mortarWidth):
    y = 0
    for s in range(rows):
        x = 0
        for i in range(cols):
            drawRectangle(x, y, brickWidth, brickHeight)
            x += (brickWidth + mortarWidth)
        y += (brickHeight + mortarWidth)
    pass
rows = int(input('Insert the integer amount of rows: '))
cols = int(input('Insert the integer amount of columns: '))
brickWidth = int(input('Insert the integer amount of the width of the bricks: '))
brickHeight = int(input('Insert the integer amount of the height of the bricks: '))
mortarWidth = int(input('Insert the integer amount of how much space you want between the bricks: '))
drawBrickWallOffset(rows,cols,brickWidth,brickHeight,mortarWidth)
screen.exitonclick()