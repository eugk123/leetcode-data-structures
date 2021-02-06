"""
https://leetcode.com/problems/design-tic-tac-toe
"""
class TicTacToe:
    def __init__(self, n):
        """

        :param n: size of rows and cols
        """
        self.n = n
        self.rows = [0]*n
        self.cols = [0]*n
        self.diagonal = 0
        self.anti_diagonal = 0


    def move(self, row, col, player):
        """

        :param row: The row of the board
        :param col: The column of the board
        :param player: The player, can be either 1 or 2
        :return: The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """

        # You add to each row and col element based on whether it's player 1 or 2
        # Player 1 -> +1
        # Player 2 -> -1
        if player == 1:
            counter = 1
        else:
            counter = -1

        # When there is 3 in a row horizontally, we know that one of the row elements will either be 3 or -3.
        # Same concept works for columns
        self.rows[row] += counter
        self.cols[col] += counter

        # For diagonals, we have two:
        # Diagonal (/): We can add/subtract 1 when row == col.
        # Antidiagonal (\): We can add/subtract 1 when row + col = n - 1 -> row = n - 1 - col
        if row == col:
            self.diagonal += counter
        if row == self.n - col - 1:
            self.anti_diagonal += counter

        # We can take the absolute value of the row elements and column elements at the player's move to determine
        # if that player won
        if abs(self.rows[row]) == self.n or \
                abs(self.cols[col]) == self.n or \
                abs(self.diagonal) == self.n or \
                abs(self.anti_diagonal) == self.n:
            return player
        return 0

if __name__ == '__main__':
    game = TicTacToe(n=3)
    print(game.move(0, 0, 1))
