#main file
import pygame
from sudokuGenerator import generateSudoku
from sudokuSolver import solve,isSafe
import time
displayWidth = 750
displayHeight = 750
pygame.init()
screen = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('SUDOKU')
black = (0,0,0)
white = (255,255,255)
running = True
temp = True
start = time.time()
key = None
temp1 = False
sudoku = generateSudoku()
sudoku1 = list()
for i in sudoku:
    line = i[:]
    sudoku1.append(line)
select = False

def textObjects(text,font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def messageDisplay(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = textObjects(text, largeText)
    TextRect.center = ((displayWidth/2),(displayHeight/2))
    screen.blit(TextSurf, TextRect)
    pygame.display.update()
    #time.sleep(2)

def dis(text):
    messageDisplay(text)

def sudokuDraw(i, j, screen , sudoku,gap):
    fnt = pygame.font.SysFont("comicsans", 60)
    x = i * gap
    y = j * gap
    if(sudoku[i][j]!=0):
        text = fnt.render(str(sudoku[i][j]), 1, black)
        screen.blit(text, (x+55,y+17))

def Draw(screen,sudoku):
    # Draw Grid Lines
    gap = displayWidth / 9.7
    for i in range(9):
        if i % 3 == 0:
            thick = 4
        else:
            thick = 1
        pygame.draw.line(screen, (0, 0, 0), (30, (i * gap)), (displayWidth-30, i * gap), thick)
        pygame.draw.line(screen, (0, 0, 0), ((i * gap)+30, 0), ((i * gap)+30, displayHeight-50), thick)
    pygame.draw.line(screen,black,(30,displayHeight-50),(displayWidth-30,displayHeight-50),4)
    pygame.draw.line(screen, (0, 0, 0), (displayWidth-30, 0), (displayWidth-30, displayHeight - 50), 4)

    for i in range(9):
        for j in range(9):
            sudokuDraw(i,j,screen,sudoku,gap)
    pygame.display.update()



def format_time(secs):
    sec = secs%60
    minute = secs//60
    hour = minute//60

    mat = " " + str(minute) + ":" + str(sec)
    return mat

def redrawWindow(screen, sudoku, playTime ):
    screen.fill(white)
    fnt = pygame.font.SysFont('comicsans', 40)
    text = fnt.render("Time: "+format_time(playTime), 1, black)
    screen.blit(text, (30, 720))
    Draw(screen,sudoku)

def clicked(pos):
    if(pos[0]<displayWidth-30 and pos[0]>20 and pos[1]<displayHeight-50 and pos[1]>0):
        gap=displayWidth/9.7
        x=pos[0]//gap
        y=pos[1]//gap
        return (int(x),int(y))
    return None

def same(sudoku1,sudoku):
    for i in range(9):
        for j in range(9):
            if(sudoku[i][j]!=sudoku1[i][j]):
                return False
    return True


while(running):
    screen.fill(white)
    playTime = round(time.time() - start)
    while(temp1):
        for event in pygame.event.get():
            if (event.type == pygame.KEYDOWN):
                temp1 = False
                running = False
            if (event.type == pygame.QUIT):
                temp1 = False
                running = False
        redrawWindow(screen, sudoku, playTime)


    while(temp):
        for event in pygame.event.get():
            if(event.type == pygame.KEYDOWN):
                temp = False
            if(event.type == pygame.QUIT):
                temp = False
                running = False
        dis('SUDOKU')
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                key = 1
            if event.key == pygame.K_2:
                key = 2
            if event.key == pygame.K_3:
                key = 3
            if event.key == pygame.K_4:
                key = 4
            if event.key == pygame.K_5:
                key = 5
            if event.key == pygame.K_6:
                key = 6
            if event.key == pygame.K_7:
                key = 7
            if event.key == pygame.K_8:
                key = 8
            if event.key == pygame.K_9:
                key = 9
            if event.key == pygame.K_SPACE:
                print(sudoku1)
                solve(sudoku1,0,0)
                print(sudoku1)
                if(same(sudoku1,sudoku)):
                    running = False
                    while (temp1):
                        for event in pygame.event.get():
                            if (event.type == pygame.KEYDOWN):
                                temp1 = False
                                running = False
                            if (event.type == pygame.QUIT):
                                temp1 = False
                                running = False
                        dis('YOU WIN')
                else:
                    temp1 = True
                    sudoku = sudoku1
                    dis("YOU LOSE")
                    time.sleep(3)
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if(clicked(pos)!=None):
                x,y= clicked(pos)
                if(x<9 and y<9 and x>=0 and y>=0):
                    if(sudoku[x][y]==0):
                        select = True
        #print(key)
    if(select and key!=None):
        if(x<9 and y<9 and isSafe(sudoku,key,x,y)):
            sudoku[x][y]=key
            select=False
            key=None

    #screen.fill(white)
    #Draw(screen)
    redrawWindow(screen, sudoku, playTime)
    pygame.display.update()





