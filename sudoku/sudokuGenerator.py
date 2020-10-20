#sudoku generator
import random


def emptyBoard():
    return [[0 for i in range(9)] for j in range(9)]

def isSafe(sudoku,k,i,j):
    #check if the number if present in the given row or not
    for i1 in range(9):
        if(i1==i):
            continue
        if(sudoku[i1][j]==k):
            return False
    #check if the number is present in the given column or not
    for j1 in range(9):
        if(j1==j):
            continue
        if(sudoku[i][j1]==k):
            return False
    #x and y finds the 3*3 grid
    x=i//3
    y=j//3
    # to find the start x and y of the grid we multiply it by 3
    x*=3
    y*=3
    #check if the number is present in the grid of not
    for i1 in range(x,x+3):
        for j1 in range(y,y+3):
            if(i1==i and j1==j):
                continue
            if(sudoku[i1][j1]==k):
                return False
    return True


def solve(sudoku,num):
    while(num>0):
        i=random.randrange(0,8,1)
        j=random.randrange(0,8,1)
        while(True):
            k=random.randrange(1,9,1)
            if(isSafe(sudoku,k,i,j)):
                sudoku[i][j]=k
                break
        num-=1

        
    

def generateSudoku():
    sudoku=emptyBoard()
    #num=random.choice([16,17,18,19])
    num =  25
    solve(sudoku,num)
    return sudoku
    


if __name__=="__main__":
    sudoku=generateSudoku()
    for i in sudoku:
        print(i)
    
     
