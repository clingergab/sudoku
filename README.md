# Sudoku
Sudoku solver using backtracking algorithm  

## Goal:
The objective of Sudoku is to fill a 9x9 grid with the numbers 1-9 so that each column, row, and 3x3 sub-grid (or
box) contains one of each digit. Sudoku has 81 variables, i.e. 81 tiles. The variables are named by row and column, and are valued from 1 to 9 subject to the constraints that no two cells in the same row, column, or box may be the same.  

### Implementation:
Implemented with backtracking search algorithm using the minimum remaining value heuristic, and forward checking to reduce variables domains.

### To execute:
**run** python3 sudoku.py <input_string>  
e.g. ```$ python3 sudoku.py 003020600900305001001806400008102900700000008006708200002609500800203009005010300```
