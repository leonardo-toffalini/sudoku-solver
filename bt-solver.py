import sys
import os

def solve(board):
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True # No more empty spaces
    
    for i in range(1, 10): # try out all the numbers in the empty square
        if valid(board, (row, col), i): # if the number is valid in the empty square
            board[row][col] = i
            
            if solve(board): # if the board is solveable after the number is placed
                return True
            
            board[row][col] = 0 # backtrack
    return False # board is not solveable

def valid(board, pos, num):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
        
    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
        
    return True

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) # row, col
    return None


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")
            
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
                
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


def main():
    board_path = sys.argv[1]
    print(board_path)
    with open(board_path, 'r') as f:
        board = [[int(num) for num in line.split(',')] for line in f]
    
    print("Sudoku Board:")
    print_board(board)
    solve(board)
    print("\nSolved Sudoku Board:")
    print_board(board)

if __name__ == "__main__":
    main()
