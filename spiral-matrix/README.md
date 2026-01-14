SPIRAL MATRIX - DIFFICULTY: MEDIUM

Given an m x n matrix, return all elements of the matrix in spiral order.

key here is to simulate the problem:
- first row, move top +1
- last column, move right -1
- last row backwards, move bottom -1
- first column, move left +1
repeat until we have all the numbers in the output list