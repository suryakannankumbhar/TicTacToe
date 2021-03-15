import pygame, sys, time
import numpy as np

pygame.init()

width = 800
height = width
lineWidth = 15
boardRows = 3
boardCols = 3
squareSize = width // boardCols
red = (255,0,0)
bgColor = (28, 170, 156)
lineColor = (23, 145, 135)
white = (255,255,255)
black = (0,0,0)
circleRadius = squareSize//3
circleWidht = 15
crossWidht = 25
crossSpace = squareSize//4
crossColor = (66, 66, 66)
circleColor = (239, 231, 200)
font = pygame.font.Font('freesansbold.ttf', 35)
text = font.render('Thank You for playing TIC-TAC-TOE!!', True, black)
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)
font1 = pygame.font.SysFont('arial', 20)
text1 = font1.render('@made by SURYA in association with google.com', True, black)
textRect1 = text1.get_rect()
textRect1.center = (width // 1.65, height // 1.2)
fontx = pygame.font.SysFont('Arial',24)
message = fontx.render("Press 'r' to Restart the game!!", True,black)



player = 1
gameOver = False

screen = pygame.display.set_mode( (width,height) )
pygame.display.set_caption( "Tic-Tac-Toe" )
screen.fill(bgColor)

board = np.zeros((boardRows,boardCols))



def drawLines():
    #partitions
    pygame.draw.line(screen,lineColor,(0,squareSize),(width,squareSize),lineWidth)
    pygame.draw.line(screen,lineColor,(0,2*squareSize),(width,2*squareSize),lineWidth)
    pygame.draw.line(screen,lineColor,(squareSize,0),(squareSize,height),lineWidth)
    pygame.draw.line(screen,lineColor,(2*squareSize,0),(2*squareSize,height),lineWidth)
    
    

drawLines()

def drawFigures():
    for row in range(boardRows):
        for col in range(boardCols):
            if board[row][col] == 1:
                pygame.draw.line(screen, crossColor, (col * squareSize + crossSpace, row * squareSize + squareSize - crossSpace),(col * squareSize + squareSize- crossSpace, row * squareSize + crossSpace),crossWidht)
                pygame.draw.line(screen, crossColor, (col * squareSize + crossSpace, row * squareSize + crossSpace),(col * squareSize + squareSize- crossSpace, row * squareSize + squareSize -  crossSpace),crossWidht)

            elif board[row][col] == 2:
                pygame.draw.circle(screen, circleColor,( int( col * squareSize + squareSize//2 ), int(row * squareSize + squareSize//2 )), circleRadius, circleWidht)


def markSquares(row,col,player):
    board[row][col] = player

def availableSquare(row,col):
    return board[row][col] == 0

def isBoardFull():
    for row in range(boardRows):
        for col in range(boardCols):
            if board[row][col] == 0:
                return False
    return True

def checkWinner(player):
    for col in range(boardCols):
       if board[0][col] == player and board[1][col] == player and board[2][col] == player:
           drawVerticalLine(col,player)
           return True
    
    for row in range(boardRows):
       if board[row][0] == player and board[row][1] == player and board[row][2] == player:
           drawHorizontalLine(row,player)
           return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        drawASCDaigonal(player)
        return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        drawDESCDaigonal(player)
        return True
    
    return False

def drawVerticalLine(col, player):
    posX = col * squareSize + squareSize//2
    if player == 1:
	    color = crossColor
    elif player == 2:
        color = circleColor
    pygame.draw.line(screen, color,(posX, 15),(posX, height - 15), 15)

def drawHorizontalLine(row, player):
    posY = row * squareSize + squareSize//2
    if player == 1:
	    color = crossColor
    elif player == 2:
	    color = circleColor
    pygame.draw.line(screen, color,(15, posY),(width - 15, posY), 15)

def drawASCDaigonal(player):
    if player == 1:
	    color = crossColor
    elif player == 2:
	    color = circleColor
    pygame.draw.line(screen,color,(15,height-15),(width-15,15),15)

def drawDESCDaigonal(player):
    if player == 1:
	    color = crossColor
    elif player == 2:
	    color = circleColor
    pygame.draw.line(screen,color,(15,15),(width-15,height-15),15)

def restart():
    screen.fill(bgColor)
    drawLines()
    player = 1
    for row in range(boardRows):
        for col in range(boardCols):
            board[row][col] = 0



while True:
    for event in pygame.event.get():
        screen.blit(message, [271.5,2])
        if event.type == pygame.QUIT:
            screen.fill(bgColor)
            screen.blit(message, [271.5,2])
            screen.blit(text, textRect)
            screen.blit(text1, [215,775])
            pygame.display.update()
            
            time.sleep(5)
            
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
        
            clickedRow = int(mouseY // squareSize)
            clickedCol = int(mouseX // squareSize)

            if availableSquare(clickedRow,clickedCol):
                markSquares(clickedRow, clickedCol, player)
                if checkWinner(player):
                    gameOver = True
                player = player % 2 + 1

                drawFigures()
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_r:
               restart()
               player = 1
               gameOver = False
           
    pygame.display.update()
