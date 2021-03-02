"""
https://leetcode.com/problems/android-unlock-patterns
"""
class Solution:
    """
    https://leetcode.com/problems/android-unlock-patterns/discuss/475868/Python-DFS-readable-code.

    The functions constraint that needs to be considered is the skip and checking if the element has been visited.
    """
    def numberOfPatterns(self, m: int, n: int) -> int:
        def backtracking(num, count):
            # Consider valid patterns only in length (m to n)
            if m <= count <= n:
                self.ans += 1

            # After reaching path count 'n', we do not need to go any further.
            if count == n:
                return

            # Visited.
            visited.add(num)

            # Try other numbers from 1 through 9
            for next_num in range(1, 10):
                # Rule out many options by requiring the next number to not be visited
                if next_num not in visited:
                    # if a next_num has an obstacle while starting from num, and is not visited previously, don't consider this path.
                    if (num, next_num) in skip and skip[(num, next_num)] not in visited:
                        continue
                    backtracking(next_num, count + 1)  # Increase count (path count, aka. combination length)

            # Unvisit to try other options
            visited.remove(num)

            return

        skip = {
            (1, 3): 2, (1, 9): 5, (1, 7): 4,
            (3, 1): 2, (3, 7): 5, (3, 9): 6,
            (7, 1): 4, (7, 3): 5, (7, 9): 8,
            (9, 3): 6, (9, 1): 5, (9, 7): 8,
            (2, 8): 5, (8, 2): 5,
            (4, 6): 5, (6, 4): 5
        }

        self.ans = 0  # This is how I am able to update the answer. Cannot update as an int variable unless initialized by object.

        for num in range(1, 10):
            visited = set()  # Reset the visited array every iteration
            backtracking(num, 1)

        return self.ans


if __name__ == '__main__':
    print(Solution().numberOfPatterns(1, 3))




# def numberOfPatterns(self, m: int, n: int) -> int:
    #     # Need this map to determine if combination skip is valid. Combination skip is valid when number in between
    #     # is in the combination.
    #     skip = {
    #         (1, 3): 2, (1, 9): 5, (1, 7): 4,
    #         (3, 1): 2, (3, 7): 5, (3, 9): 6,
    #         (7, 1): 4, (7, 3): 5, (7, 9): 8,
    #         (9, 3): 6, (9, 1): 5, (9, 7): 8,
    #         (2, 8): 5, (8, 2): 5,
    #         (4, 6): 5, (6, 4): 5
    #     }
    #     result = [0]
    #
    #     # Find combinations on each element on the
    #     # for i in range(1,10):
    #     #     visited = [[0,0,0],[0,0,0],[0,0,0]]
    #     #     self.dfs(m, n, i, j, 0, skip, visited, [], result)
    #
    #     visited = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    #     combination = []
    #     self.backtracking(m, n, 0, 0, 0, skip, visited, combination, result)
    #     return result[0]
    #
    # def backtracking(self, m, n, i, j, length, skip, visited, combination, result):
    #
    #     # Combination Length cannot exceed n AND you cannot land outside the grid
    #     if len(combination) > n or i < 0 or j < 0 or i >= 3 or j >= 3:
    #         print("OUT OF BOUNDS")
    #         return
    #
    #     # You cannot go to a visited element (1). We put this below because if indices are out of bounds, this would fail
    #     if visited[i][j] == 1:
    #         print("VISITED")
    #         return
    #
    #     # Valid combination within length constraints, add to result:
    #     print(len(combination), length)
    #     if len(combination) >= m and len(combination) <= n and len(combination) == length:
    #         print("RESULT, {}".format(combination))
    #         result[0] += 1
    #
    #     if len(combination) == n:
    #         print("STOP")
    #         return
    #
    #     # You cannot skip a number unless that number has been selected.
    #     # ADD CONSTRAINT
    #
    #     visited[i][j] = 1  # Visited 0 -> 1
    #     combination.append(numpad[i][j])
    #     print(combination)
    #
    #     # print("1, {}".format(combination))
    #     # You can go up, right, left, down
    #     self.backtracking(m, n, i, j + 1, length + 1, skip, numpad, visited, combination, result)
    #     # self.backtracking(m, n, i, j - 1, length + 1, skip, numpad, visited, combination, result)
    #     # self.backtracking(m, n, i - 1, j, length + 1, skip, numpad, visited, combination, result)
    #     combination.pop()
    #     j -= 1
    #     print("NEXT, {}".format(combination))
    #
    #     self.backtracking(m, n, i + 1, j, length + 1, skip, numpad, visited, combination, result)
    #
    #     # You can go diagonally
    #     # You can skip numbers (up, right, left, down)
    #     # You can skip numbers (diagonally)
    #     # You can perform L jumps

