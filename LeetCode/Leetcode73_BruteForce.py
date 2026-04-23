"""

73. Set Matrix Zeroes
Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

"""

def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    zero_rows = set()
    zero_cols = set()
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    
    for i in range(rows):
        for j in range(cols):
            if i in zero_rows or j in zero_cols:
                matrix[i][j] = 0
                
                
# Time Complexity: O(m*n) where m and n are the number of rows and columns in the input matrix (due to nested loops)
# Space Complexity: O(m+n) in the worst case if all elements are zero (due to sets storing row and column indices)

