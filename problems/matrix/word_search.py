"""
https://leetcode.com/problems/word-search/
https://www.youtube.com/watch?v=vYYNp0Jrdv0

Given an m x n board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or
vertically neighboring. The same letter cell may not be used more than once.

 [A] [B] [C]  E
  S   F  [C]  S
  A  [D] [E]  E

Example:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Complexity:
Time: O(N^2)
Space: O(

Speed: 292 ms 91.2%

:type board: List[List[str]]
:type word: str
:rtype: word: str
"""
class Solution:
    def dfs(self, board, i, j, count, word):
        if count == len(word):  # Checks to see if we found the word. This occurs when the count value is equal to the length of the word
            return True

        # Index out of bounds on left, right, above, below, and
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]):
            return False

        # If the cell we're on is not equal to the character we're looking for
        if board[i][j] != word[count]:
            return False

        # Need to pull out current element. This is because when we start traversing, it may traverse back to the previous
        # element due to having the same previous letter.
        # To preserve matrix, store it:
        temp = board[i][j]
        board[i][j] = ' '

        # Traverse to cell below, above, right, left
        found = self.dfs(board, i + 1, j, count + 1, word) \
                or self.dfs(board, i - 1, j, count + 1, word) \
                or self.dfs(board, i, j + 1, count + 1, word) \
                or self.dfs(board, i, j - 1, count + 1, word)

        # Restore temp value
        board[i][j] = temp

        return found

    def exist(self, board, word):
        # Base cases
        if not word:  # No word? return True
            return True
        if not board:  # No board? return False
            return False

        # Iterate through matrix
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.dfs(board, i, j, 0, word):  # Recursive DFS Solution
                    return True
        return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    board = [["A","B","C","E"],
             ["S","F","C","S"],
             ["A","D","E","E"]]

    word = "ABCA"  # This case would have resulted in True if we didn't pull out the element in current index.
    print(Solution().exist(board, word))