```txt
# Note: There is a -1st row and column, and a 5th row and column.
# These rows and collumns function as 0 paddings so that the indices will not be out of bounds

set I = -1 .. 5;

set N = 1 .. 9;

set four_long_interval = 1 .. 4;
set R = -1 .. 1;

var X {I, I, N}, binary;

# paddings must be zeros
s.t. firstRow: sum {n in N}sum {i in I} X[-1, i, n] = 0;
s.t. lastRow: sum {n in N}sum {i in I} X[5, i, n] = 0;
s.t. firstCol: sum {n in N}sum {i in I} X[i, -1, n] = 0;
s.t. lastCol: sum {n in N}sum {i in I} X[i, 5, n] = 0;

# each row and column most have only one of each number at most
s.t. row_unique {i in I, n in N}: sum {j in I} X[i, j, n] <= 1;
s.t. col_unique {j in I, n in N}: sum {i in I} X[i, j, n] <= 1;

# actual conditions for the game
# (the first part of the statement reflects the row, the second part of the statement reflects the column)
s.t. two_one_down: sum {n in N} sum {i in four_long_interval} X[2+i, 1, n] = 5;
```