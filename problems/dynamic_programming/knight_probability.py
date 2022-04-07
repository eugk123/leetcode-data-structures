"""
https://leetcode.com/problems/knight-probability-in-chessboard/
"""
class Solution:
    """
    Recursion Relationship - 8 mov
    
    k=1
    ans = (0+0+0+0+0+0+1move3+1move4)/8 = 2 * (1/8) = 1/4
    k-- 
    --3
    -4-

    k=2
    ans = (0+0+0+0+0+0+1move3+1move4)/8 = 4/8 * (1/8) = 1/16
    1move3=(2move1+0+0+0+0+0+0+2move8)/8 = 2/8
    1move4=(0+0+0+0+0+0+2move6+2move7+0)/8 = 2/8
    1move3=2/8  1move4=2/8
    8-1         7--
    ---         --k
    -k-         6--

    k=3
    ans = (0+0+0+0+0+0+1move3+1move4)/8 = 2/16 * (1/8) = 1/64
    1move3=(2move1+0+0+0+0+0+0+2move8)/8 = 2/8 * (1/8) = 1/16
    1move4=(0+0+0+0+0+0+2move6+2move7+0)/8 = 2/8 * (1/8) = 1/16
    2move1=2/8  2move8=2/8  2move6=2/8  2move7=2/8
    --k         k--         -x-         k--
    x--         --x         --x         --x
    -x-         -x-         k--         -x-
    """
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        # Probability is total moves allowed / total moves possible. Figure out the total moves allowed by DFS
        def dfs(i, j, moves):
            if (i, j, moves) in memo:
                return memo.get((i, j, moves))
            
            # if out of bounds, return 0
            if i < 0 or j < 0 or i >= n or j >= n:
                return float(0)
            
            if moves == k:
                return float(1)
            
            # for as long as moves < k, we traverse all 8 possible spots
            # continue to add total possible spots
            a = dfs(i + 1, j + 2, moves + 1)
            b = dfs(i + 1, j - 2, moves + 1)  
            c = dfs(i - 1, j + 2, moves + 1)
            d = dfs(i - 1, j - 2, moves + 1)
            e = dfs(i + 2, j - 1, moves + 1)
            f = dfs(i + 2, j + 1, moves + 1)
            g = dfs(i - 2, j - 1, moves + 1)
            h = dfs(i - 2, j + 1, moves + 1)
            
            # At each recursive depth, it will divise by 8
            # so 2nd move will consist of ans = (a-h)/8 and move2 a=(a-h)/8; therefore ans=((a-h)/8+(a-h)/8+...+(a-h)/8)/8
            memo[(i, j, moves)] = (a + b + c + d + e + f + g + h)/8
            return (a + b + c + d + e + f + g + h)/8
        
        # k = 2 n = 3 -> 0.0625
        memo = {}
        return dfs(row, column, 0)