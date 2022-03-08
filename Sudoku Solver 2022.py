 #What is NumPy? NumPy is a Python library used for working with arrays.
import numpy as np
    

    #gameboard for Sudoku, it's a list of lists that represents a row of sudoku. 
grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

def possible(row, column, number):
    global grid
    #Is the number appearing in the given row?
    for i in range(0,9):
        if grid[row][i] == number:
            #are any of of these numbers a solution in this row?
            return False 

    #Is the number appearing in the given column?
    for i in range(0,9):
        if grid[i][column] == number:
            #are any of of these numbers a solution in this column?
            return False 
        
    #Is the number appearing in the given square? x3 sections - regardless outcome will be 0,3,6
    x0 = (column // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if grid[y0+i][x0+j] == number:
                return False
# if the answer to all 3 questions is no, thats a possible solution. Continues to loop through board to find solution
    return True  

def solve():
    global grid
    for row in range(0,9):
         #checks to see if any fields or rows are empty
        for column in range(0,9): 
            #fields marked as zero are considered empty
            if grid[row][column] == 0: 
                for number in range(1,10):
                    if possible(row, column, number):
                        grid[row][column] = number
                        solve()
                        grid[row][column] = 0

                return
      
    print(np.matrix(grid))
    #possibilities for multiple solutions
    input('More possible solutions') 

solve()


