import os
import sys

itos = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

def generate(board):
    output = ""
    output += 'set I = 0 .. 8;\n'
    output += 'set N = 1 .. 9;\n'
    output += 'var X {I, I, N} binary;\n'
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (val := board[i][j]) != 0:
                output += f"s.t. {itos[i]}-{itos[j]}: X[{i}][{j}][{val}] = 1;\n"

    output += "s.t. row_unique {i in I, n in N}: sum {j in I} X[i, j, n] = 1;\n"
    output += "s.t. col_unique {j in I, n in N}: sum {i in I} X[i, j, n] = 1;\n"
    return output


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
    output = generate(board)
    with open('sudoku-lp.txt', 'w') as f:
        for line in output.splitlines():
            f.write(line + '\n')


if __name__ == "__main__":
    main()