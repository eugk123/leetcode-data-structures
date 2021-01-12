def setZeroes(matrix):  # Hash Table (Two-pass)
    """
    https://leetcode.com/problems/set-matrix-zeroes/

    Given an m x n matrix. If an element is 0, set its entire row and column to 0. Do it in-place.

    111    101      0120    0000
    101 -> 000      3452 -> 0450
    111    101      1315    0310

    Example 1:
    Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Output: [[1,0,1],[0,0,0],[1,0,1]]

    Example 2:
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    Intuition:
    If any cell of the matrix has a zero we can record its row and column number. All the cells of this recorded row
    and column can be marked zero in the next iteration.

    Algorithm:
    1. Iterate over the matrix and populate row index and col index when matrix[i][j] = 0
    2. Iterate over the matrix again then use a conditional for whenever row index or column index matches what's in the
    row or col set, then set matrix[i][j] = 0

    Complexity:
    Time: O(mn) - (rows * cols elements)
    Space: O(m+n) - 2 sets with different lengths (one for rows, one for cols)

    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    R = len(matrix)  # Length of rows
    C = len(matrix[0])  # Length of columns
    rows, cols = set(), set()  # Initialize empty sets which will identify which row or column needs to be full of zeroes

    # Essentially, we mark the rows and columns that are to be made zero
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)  # Additional Memory M from new Set
                cols.add(j)  # Additional Memory N from new Set

    # Iterate over the array once again and using the rows and cols sets, update the elements
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0
    print(matrix)

def setZeroes_ConstantSpace(matrix):  # Hash Table (Two-pass)
    """
    https://www.youtube.com/watch?v=1KnLIAvTxjQ

    Intuition:
    Rather than using additional variables to keep track of rows and columns to be reset, we use the matrix itself as
    the indicators.

    Complexity:
    Time: O(mn) - (rows * cols elements)
    Space: O(1)

    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    R = len(matrix)  # Number of rows
    C = len(matrix[0])  # Number of columns

    # This will be your switch to nullify first row and column.
    firstRowZero = False
    firstColZero = False
    for i in range(R):
        if matrix[i][0] == 0:  # If any item in first row is 0, set to True
            firstRowZero = True
    for j in range(C):
        if matrix[0][j] == 0:  # If any item in first col is 0, set to True
            firstColZero = True

    # Set zeroes in first row/col.
    for i in range(1, R):
        for j in range(1, C):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Then use first row/col zeros to nullify the rest of matrix
    for i in range(1, R):
        for j in range(1, C):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # If True, set entire first row/col to zeros
    if firstColZero:
        for i in range(C):
            matrix[i][0] = 0
    if firstRowZero:
        for j in range(R):
            matrix[0][j] = 0
    print(matrix)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix = [[1,1,0,1],
              [1,1,1,1],
              [1,1,0,1],
              [0,1,1,1]]
    setZeroes_ConstantSpace(matrix)
    # setZeroes(matrix)

    # [[0, 0, 1, 0],
    # [1, 1, 1, 1],
    # [0, 0, 1, 1],
    # [1, 1, 1, 1]]

    # [[0, 0, 0, 0],
    # [1, 0, 1, 0],
    # [0, 0, 0, 0],
    # [1, 0, 1, 0]]


