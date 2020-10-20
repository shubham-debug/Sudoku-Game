# Sudoku solver
# need to add gui to it using pygame and then put it in my repository in github

def isSafe(sudoku,k,i,j):
    #check if the number if present in the given row or not
    for i1 in range(9):
        if(i1==i):
            continue
        if(sudoku[i1][j]==k and sudoku[i1][j]!=None):
            return False
    #check if the number is present in the given column or not
    for j1 in range(9):
        if(j1==j):
            continue
        if(sudoku[i][j1]==k and sudoku[i][j1]!=None):
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
                
    

def solve(sudoku,i,j):
    if(i>8):
        return True
    # visit the if part if we need to fill the number in the sudoku
    # if the number is already present in the position then we simply continue
    # else part shows that 
    if(sudoku[i][j]==0):
        for k in range(1,10):
            if(isSafe(sudoku,k,i,j)):
                sudoku[i][j]=k
                if(j+1<=8):
                    if(solve(sudoku,i,j+1)):
                        return True
                else:
                    if(solve(sudoku,i+1,0)):
                        return True
                sudoku[i][j]=0
               
    else:
        if(j+1<=8):
            if(solve(sudoku,i,j+1)):
                return True
        else:
            if(solve(sudoku,i+1,0)):
                return True
    return False

                    
                
            


if __name__=="__main__":
    pass
    '''sudoku=[[9, 0, 0, 0, 0, 0, 0, 7, 0], 
            [6, 1, 7, 0, 8, 0, 0, 2, 0], 
            [0, 5, 0, 0, 3, 9, 0, 0, 8], 
            [0, 4, 0, 8, 0, 0, 5, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 2, 6, 0, 0, 0, 0], 
            [7, 0, 5, 0, 0, 8, 0, 0, 0], 
            [0, 6, 0, 9, 0, 5, 3, 0, 7], 
            [2, 0, 8, 0, 0, 0, 0, 0, 0]]
    # if solve return true then sudoku can be solved other wise no solution is
    # possible
    if(solve(sudoku,0,0)):
        for i in sudoku:
            print(*i)
    else:
        print('No answer is  possible')'''
