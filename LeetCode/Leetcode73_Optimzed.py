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
    
    first_row_zero = any(matrix[0][j] == 0 for j in range(cols))
    first_col_zero = any(matrix[i][0] == 0 for i in range(rows))
    
    # mark
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    
    # fill
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    
    # first row
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0
    
    # first col
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0
                
                
# Time Complexity: O(m*n) where m and n are the number of rows and columns in the input matrix (due to nested loops)
# Space Complexity: O(m+n) in the worst case if all elements are zero (due to sets storing row and column indices)


"""

⏱ Complexity
Time: O(m*n)
Space: O(1) ✅
🎯 Pattern

👉 Matrix Marking / In-place trick

⚠️ Common Mistakes
Directly modifying matrix without markers ❌
Forgetting first row/col special handling ❌
Overwriting markers too early ❌
🔥 Interview Tip

If you say:
👉 “I’ll use first row/column as a hash map”

→ interviewer knows you understand space optimization

"""