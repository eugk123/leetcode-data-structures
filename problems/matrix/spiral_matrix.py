"""
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

1 -> 2 -> 3     1 -> 2 -> 3 -> 4
          |                    |
4 -> 5    6     5 -> 6 -> 7    8
|         |     |              |
7 <- 8 <- 9     9 <- 10<- 11<- 12

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Complexity:
Time: O(n) - traversed through all elements once
Space: O(n) - creating a list of length n

Speed: 16ms 99.84% DAMN
"""
class Solution:
    def spiralOrder(self, matrix):
        """
        https://www.youtube.com/watch?v=BJnMZNwUk1M
        """
        res = []

        # Base Case - single row
        if len(matrix) == 1:
            print(matrix)
            return matrix[0]

        # Base Case - single column
        if len(matrix[0]) == 1:
            for i in range(len(matrix)):
                res.append(matrix[i][0])
            return res

        # if len(matrix) == 1:
        #     return matrix[0]

        top = 0
        bot = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bot and left <= right:
            # top side: i = left,right
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            # right side: i = top,bot
            for i in range(top, bot + 1):
                res.append(matrix[i][right])
            right -= 1

            # bot side: i = right,left
            if top <= bot:
                for i in reversed(range(left, right + 1)):
                    res.append(matrix[bot][i])
                    print(i, res)

                bot -= 1

            # left side: i = bot,top
            if left <= right:
                for i in reversed(range(top, bot + 1)):
                    res.append(matrix[i][left])

                left += 1
        return res

    def spiralOrderEugene(self, matrix):  # Hash Table (Two-pass)

        if not matrix:
            return
        elements = []
        last_col = len(matrix[0])
        last_row = len(matrix)
        first_col = first_row = 0

        # Taking 3x3 matrix for example. And using 00,01,02,10,11,12,20,21,22 indices as an example
        while(first_col < last_col and first_row < last_row):
            # Traverse entire first row using indexes (first_col to last_col) ex: 00 01 02
            for j in range(first_col, last_col):
                elements.append(matrix[first_row][j])

            if (first_row + 1 < last_row):  # This check is to prevent the last loop from going any further.
                # Traverse last column using indexes (first_row + 1 to last_row) ex: 12 22
                for i in range(first_row + 1, last_row):
                    elements.append(matrix[i][last_col-1])

                if (first_col + 1 < last_col):  # This check is to prevent the last loop from going any further.
                    # Traverse last row, (last_col - 1 to first_col): ex 21 20
                    for j in reversed(range(first_col, last_col - 1)):
                        elements.append(matrix[last_row-1][j])

                    # Traverse first row, (last_row - 1 to first_row - 1): ex 10
                    for i in reversed(range(first_row + 1, last_row - 1)):
                        elements.append(matrix[i][first_col])

            first_col+=1
            last_col-=1
            first_row+=1
            last_row-=1
        return elements


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    matrix1 = [[ 1, 2, 3, 4],
              [ 5, 6, 7, 8],
              [ 9,10,11,12],
              [13,14,15,16]]
    matrix2 = [[ 1, 2, 3, 4, 1],
              [ 5, 6, 7, 8, 1],
              [ 5, 6, 7, 8, 1]]
    matrix3 = [[7],
              [9],
              [6]]
    matrix4 = []
    print("Case 1: 4x4: {}".format(Solution().spiralOrder(matrix1)))
    print("Case 2: 3x5: {}".format(Solution().spiralOrder(matrix2)))
    print("Case 3: 3x1: {}".format(Solution().spiralOrder(matrix3)))
    print("Case 4: 0x0: {}".format(Solution().spiralOrder(matrix4)))