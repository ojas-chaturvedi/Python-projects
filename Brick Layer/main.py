import turtle
screen = turtle.Screen()
screen.screensize(400, 400)
screen.setworldcoordinates(0, 0, 400, 400)
pointer = turtle.Turtle()
pointer.color("red")
pointer.up()
pointer.hideturtle()
pointer.speed(0)
def drawRect(x, y, length, height):
    pointer.up()
    pointer.goto(x,y)
    pointer.begin_fill()
    pointer.down()
    pointer.goto(x + length, y)
    pointer.goto(x + length, y + height)
    pointer.goto(x, y + height)
    pointer.goto(x, y)
    pointer.up()
    pointer.end_fill()
def drawRectinverse(x, y, length, height):
    pointer.up()
    pointer.goto(x,y)
    pointer.begin_fill()
    pointer.down()
    pointer.goto(x + height+length, y)
    pointer.goto(x + length+height, y + height-length)
    pointer.goto(x, y+length+height)
    pointer.goto(x, y)
    pointer.up()
    pointer.end_fill()
def drawCoolWall(rows, cols, brickwidth, brickHeight, mortarWidth):
    #no real pattern, was just having fun with the rectangle shaped and liked it, so i used it as my fancy brick wall pattern
    y = brickHeight
    brickWidth_offset = brickWidth+(mortarWidth/2)-(0.5*brickWidth) - mortarWidth
    for s in range(rows):
        if s%2==0:
            x = 0
            for i in range(cols):
                drawRectinverse(x, y, brickWidth, brickHeight)
                x += (brickWidth + mortarWidth)
        else:
            x = brickWidth+(mortarWidth/2)-(0.5*brickWidth)
            for i in range(cols):
                if i==cols-1:
                    drawRectinverse(x, y, brickWidth_offset, brickHeight)
                else:
                    drawRectinverse(x, y, brickWidth, brickHeight)
                    x += (brickWidth + mortarWidth)
            x=0
            drawRectinverse(x, y, brickWidth_offset, brickHeight)
        y += (brickHeight + mortarWidth) + brickHeight
    pass
def drawBrickWallOffset(rows, cols, brickWidth, brickHeight, mortarWidth):
    y = 0
    brickWidth_offset = brickWidth+(mortarWidth/2)-(0.5*brickWidth) - mortarWidth
    for s in range(rows):
        if s%2==0:
            x = 0
            for i in range(cols):
                drawRect(x, y, brickWidth, brickHeight)
                x += (brickWidth + mortarWidth)
        else:
            x = brickWidth+(mortarWidth/2)-(0.5*brickWidth)
            for i in range(cols):
                if i==cols-1:
                    drawRect(x, y, brickWidth_offset, brickHeight)     
                else:
                    drawRect(x, y, brickWidth, brickHeight)
                    x += (brickWidth + mortarWidth)
            x=0
            drawRect(x, y, brickWidth_offset, brickHeight)
        y += (brickHeight + mortarWidth)
    pass
def drawBrickWall(rows, cols, brickWidth, brickHeight, mortarWidth):
    y = 0
    for s in range(rows):
        x = 0
        for i in range(cols):
            drawRect(x, y, brickWidth, brickHeight)
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
