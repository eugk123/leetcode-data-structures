"""
https://leetcode.com/problems/n-queens
"""
from typing import List
class Solution:
    """
    Iterate through only first row from 0->3 and perform backtracking()
        For every iteration, start with an empty matrix of size n by n. "x" denotes empty.
    xxxx
    xxxx
    xxxx
    xxxx

    Backtracking equation will do the following:
    1) Given i, j, mark horizontal and vertical and diagonal with periods (create helper method for this)
        Then populate current[i][j] with "Q"
        Count that queen. count += 1
    Q...
    ..xx
    .x.x
    .xx.

    2) On the next row, recursively call using a copy.deepcopy(current) at any empty spot with "x"
    This occurs at j = 2 and j = 3. So you can create a loop for j in range(n): backtrack(i, j, copy.deepcopy(current), count)
    backtracking(i, 2, copy.deepcopy(current), count)
    backtracking(i, 3, copy.deepcopy(current), count)

    3) Figure out some break conditions
    a) if empty, populate queen:            if current[i][j] == "x":
    b) if blocked ".", or populated "Q":    elif current[i][j] == "." or current[i][j] == "Q":
    c) counted n queens, add to result:     if count == n:
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        def compressResult(current):
            result = []
            for i in range(n):
                result.append("".join(current[i]))
            return result
        def blockQueenSpaces(i, j, current):
            # horizontal and vertical blocks
            for index in range(n):          
                current[i][index] = "."
                current[index][j] = "."

            
            # diagonal blocks down-right    
            row, col = i, j
            for index in range(j, n):          
                current[row][index] = "."
                row += 1
                if row == n:
                    break

            # diagonal blocks down-left /
            row, col = i, j
            for index in reversed(range(0, j + 1)):          
                current[row][index] = "."
                row += 1
                if row == n:
                    break

            # diagonal blocks up-right /
            row, col = i, j
            for index in range(j, n):          
                current[row][index] = "."
                row -= 1
                if row == -1:
                    break
            # diagonal blocks down-left /
            row, col = i, j
            for index in reversed(range(0, j + 1)):          
                current[row][index] = "."
                row -= 1
                if row == -1:
                    break

        def backtracking(i, j, count, current):
            # if empty, populate queen
            if current[i][j] == "x":
                # block all empty spaces in horizontal, vertically, and diagonally
                # print(i, j, current)
                blockQueenSpaces(i, j, current)
                # populate queen
                current[i][j] = "Q"
                count += 1
                
            # if blocked ".", or populated "Q"
            elif current[i][j] == "." or current[i][j] == "Q":
                return

            # counted n queens
            if count == n:
                result = compressResult(current)
                if result not in results:
                    results.append(result)
                return
                        
            for j in range(n):
                backtracking(i + 1, j, count, copy.deepcopy(current))
            
        results = []
        
        for j in range(n):
            empty = [["x"]*n for i in range(n)]
            backtracking(0, j, 0, empty)

        return results