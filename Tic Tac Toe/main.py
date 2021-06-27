import turtle
import time

#screen
screen = turtle.Screen()
screen.screensize(700,700)
screen.colormode(255)
screen.setworldcoordinates(0,0,3,3)


#pointer
pointer = turtle.Turtle()
pointer.shapesize(5)
pointer.up()
pointer.speed(0)
pointer.hideturtle()

#writer
writer = turtle.Turtle()
writer.color("green")
writer.shapesize(5)
writer.up()
writer.speed(0)
writer.hideturtle()
writer.goto(1.5,1.5)

#board game data
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

#variables
gameContine = True
winner = None
currentPlayer = 1

#display game board
def draw_line(x1,y1,x2,y2):
    pointer.goto(x1,y1)
    pointer.down()
    pointer.goto(x2,y2)
    pointer.up()
def draw_board():
    draw_line(0,1,3,1)
    draw_line(0,2,3,2)
    draw_line(1,0,1,3)
    draw_line(2,0,2,3)

#click
def fillarray (a,b):
    global click
    pointer.goto(a+.5, b+.5)
    if board[a][b]==0:
        if currentPlayer == 1:
            pointer.shape("circle")
            board[a][b] = 1
        else:
            pointer.shape("turtle")
            board[a][b] = 2
        pointer.stamp()
        click = False
        return click

def clickFunc(x,y):
    clicking = True
    while clicking == True:
        fillarray(int(x), int(y))
        clicking = click
    detectWin()

#handle turn
def turn_handle(player):
    if player == 1:
        writer.write("Circle's turn", align = 'center', font = ('Courier', 24, "underline", "bold"))
    else:
        writer.write("Turtle's turn", align = 'center', font = ('Courier', 24, "underline", "bold"))
    time.sleep(1)
    writer.clear()
    
#wins
def detectWin():
    detectWinner()
    if winner == 1 or winner == 2:
        pointer.goto(1.5,1.5)
        pointer.color("red")
        if winner == 1:
            pointer.write('Player Circle Won!', align = 'center', font = ('Courier', 24, "underline", "bold"))
        else:
            pointer.write('Player Turtle Won!', align = 'center', font = ('Courier', 24, "underline", "bold"))
    flipPlayer()
    
#winner
def detectWinner():
    global winner
    rowWinner = detectRow()
    columnWinner = detectColumn()
    diagonalWinner = detectDiagonal()
    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        winner = None
    return winner
        
#rows
def detectRow():
    global gameContine
    rowBottom = board[0][0] == board[1][0] == board[2][0] != 0
    rowMiddle = board[0][1] == board[1][1] == board[2][1] != 0
    rowTop = board[0][2] == board[1][2] == board[2][2] != 0
    if rowBottom or rowMiddle or rowTop:
        gameContine = False
    if rowBottom:
        return board[0][0]
    elif rowMiddle:
        return board[0][1] 
    elif rowTop:
        return board[0][2]
    else:
        return None

#columns
def detectColumn():
    global gameContine
    columnBottom = board[0][0] == board[0][1] == board[0][2] != 0
    columnMiddle = board[1][0] == board[1][1] == board[1][2] != 0
    columnTop = board[2][0] == board[2][1] == board[2][2] != 0
    if columnBottom or columnMiddle or columnTop:
        gameContine = False
    if columnBottom:
        return board[0][0]
    elif columnMiddle:
        return board[1][0] 
    elif columnTop:
        return board[2][0]
    else:
        return None
    
#diagonals
def detectDiagonal():
    global gameContine
    diagonal_1 = board[0][0] == board[1][1] == board[2][2] != 0
    diagonal_2 = board[0][2] == board[1][1] == board[2][0] != 0
    if diagonal_1 or diagonal_2:
        gameContine = False
    if diagonal_1:
        return board[0][0]
    elif diagonal_2:
        return board[0][2]
    else:
        return None
    
#flip players
def flipPlayer():
    global currentPlayer
    if currentPlayer == 1:
        currentPlayer = 2
    elif currentPlayer == 2:
        currentPlayer = 1
    turn_handle(currentPlayer)

#play game
draw_board()
screen.onclick(clickFunc)
        
    
#key functions
print("If you have a saved game, please press 'o'. If you do not have a saved game, please ignore this message.")
print("Key functions: \ns = save\no = open saved game\nr = resart\ne = exit")
def save():
    global currentPlayer, board
    f = open(r"videoGames\tictactoe\saved_board.txt", "w")
    for i in range(3):
        for s in range(3):
            if board[i][s] == 1:
                f.write("1\n")
            elif board[i][s] == 2:
                f.write("2\n")
            else:
                f.write("0\n")
    f.write(str(currentPlayer))     
def openFile():
    global board, currentPlayer
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    board_save = open(r"videoGames\tictactoe\saved_board.txt", "r")
    for i in range(10):
        board_numbers = (board_save.readline()).strip()
        if i < 3:
            if board_numbers == "0":
                board[0][i] = 0
            elif board_numbers == "1":
                board[0][i] = 1
                pointer.goto(0.5, i+.5)
                pointer.shape("circle")
                pointer.stamp()
            elif board_numbers == "2":
                board[0][i] = 2
                pointer.goto(0.5, i+.5)
                pointer.shape("turtle")
                pointer.stamp()
        elif i>=3 and i< 6:
            if board_numbers == "0":
                board[1][i-3] = 0
            elif board_numbers == "1":
                board[1][i-3] = 1
                pointer.goto(1.5, i-3+.5)
                pointer.shape("circle")
                pointer.stamp()
            elif board_numbers == "2":
                board[1][i-3] = 2
                pointer.goto(1.5, i-3+.5)
                pointer.shape("turtle")
                pointer.stamp()
        elif i>=6 and i< 9:
            if board_numbers == "0":
                board[2][i-6] = 0
            elif board_numbers == "1":
                board[2][i-6] = 1
                pointer.goto(2.5, i-6+.5)
                pointer.shape("circle")
                pointer.stamp()
            elif board_numbers == "2":
                board[2][i-6] = 2
                pointer.goto(2.5, i-6+.5)
                pointer.shape("turtle")
                pointer.stamp()
        elif i == 9:
            currentPlayer = int(board_numbers)
def exit():
    quit()
def restart():
    global board
    save()
    pointer.color("black")
    pointer.clear()
    board = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    draw_board()
    pointer.hideturtle()


screen.onkey(save, "s")
screen.onkey(openFile, "o")
screen.onkey(restart, "r")
screen.onkey(exit, "e")


screen.listen()
screen.mainloop()
