"""
https://leetcode.com/problems/perfect-squares/
"""
import collections
class Solution:
    def numSquares(self, n: int) -> int:
        # You can find possible neighbors from the input number (Ex: 12)
        # You first need to solve the highest possible square. (Ex: 12 -> 3^2 = 9)
        # Possible neighbors can start from squared of 1 up to the highest possible square. (3 -> 3, 2, 1)
        possible_squares = []
        i = 1
        while i ** 2 <= n:
            possible_squares.append(i)
            i += 1
        # print(possible_squares)

        # Element in queue will be in form of tuple consisting of sum and count.
        # We first start at sum == 0 and count == 0.
        queue = collections.deque([(0, 0)])

        while queue:
            # (0, 0)
            curr = queue.popleft()
            # print(curr)

            for nei in possible_squares:
                # Process: Compute sum and update count
                total = curr[0] + nei ** 2
                count = curr[1] + 1

                # Constraints: total > n
                if total > n:
                    continue

                # Constraints: total == n
                if total == n:
                    return count

                # Traverse neighbor
                queue.append((total, count))
