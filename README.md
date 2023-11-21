# Sudoku solver

The following is a sudoku solver with the backtracking algorithm.
To solve a sudoku puzzle using the solver
1. Create a file named ```board.txt``` and put the matrix representation of the board into this file.
Example matrix representation:
```txt
7, 8, 0, 4, 0, 0, 1, 2, 0
6, 0, 0, 0, 7, 5, 0, 0, 9
0, 0, 0, 6, 0, 1, 0, 7, 8
0, 0, 7, 0, 4, 0, 2, 6, 0
0, 0, 1, 0, 5, 0, 9, 3, 0
9, 0, 4, 0, 6, 0, 0, 0, 5
0, 7, 0, 3, 0, 0, 0, 1, 2
1, 2, 0, 0, 0, 7, 4, 0, 0
0, 4, 9, 2, 0, 6, 0, 0, 7
```
2. Run the solver with the argument of the path to the board file:
```bash
python3 solver.py board.txt
```

To install all the dependencies run the following command in your terminal:
```bash
pip install requrements.txt
```