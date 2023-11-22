# Sudoku solver

This project contains two seperate ways of solving a sudoku puzzle algorithmically:
-  with a backtracking algorithm
-  with a Linear Programming model

### To solve a sudoku puzzle using backtracking
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
python3 bt-solver.py board.txt
```

### To solve a sudoku puzzle using a Linear Programming model
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
python3 lp-solver.py board.txt
```
3. Copy the contents of the generated ```sudoku-lp.txt``` file into your LP solver of choice.

To install all the dependencies run the following command in your terminal:
```bash
pip install requrements.txt
```