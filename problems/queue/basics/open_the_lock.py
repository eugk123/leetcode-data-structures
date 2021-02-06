"""
https://leetcode.com/problems/open-the-lock
"""
from typing import List
import collections
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        """
        Return minimum number of turns to get the target combination

        Time complexity - O(N 10^N + D)   Solution says O(N^2 10^N + D) not sure why it's N^2.
         1. while queue -> O(10^4)
         2. for index in combo -> O(4)
         3. instantiate dead sets -> O(D)

        Same complexity - O(10^4 + D)
         1. visited set = O(10^4)
         2. deadset = 4
        """
        # The trick is to treat '0000' to '9999' as a 10,000 node graph
        # '0000' has 8 neighbors: '0001', '0010', '0100', '1000', '0009', '0090', '0900', '9000'
        # For every neighbor you jump to, you count that. Therefore, your should use a tuple to keep
        # track of node value and # of turns

        # Base cases
        if target == "0000":
            return 0
        if "0000" in deadends:
            return -1

        combinations = [('0000', 0)]
        queue = collections.deque(combinations)

        # Visited will only contain combination.
        visited = set('0000')

        while queue:
            combo, count = queue.popleft()

            # Find the neighbors of curr
            # iterate through each index and +1 and -1 (if 0, go to 9)
            # Should find 8 neighbors for every iteration

            count = count + 1  # update count for neighbors

            combo_list = list(combo)  # Convert combination to char array

            neighbors = []  # Initialize empty neighbors
            # print(combo, count)

            for index in range(len(combo_list)):
                # +1 to each index and add to neighbors.
                combo_list[index] = str(int(combo_list[index]) + 1)
                if combo_list[index] == '10':
                    combo_list[index] = '0'
                neighbors.append((''.join(combo_list), count))

                # backtrack -1
                combo_list[index] = str(int(combo_list[index]) - 1)
                if combo_list[index] == '-1':
                    combo_list[index] = '9'

                # -1 to each index and add to neighbors.
                combo_list[index] = str(int(combo_list[index]) - 1)
                if combo_list[index] == '-1':
                    combo_list[index] = '9'
                neighbors.append((''.join(combo_list), count))

                # backtrack +1
                combo_list[index] = str(int(combo_list[index]) + 1)
                if combo_list[index] == '10':
                    combo_list[index] = '0'

            # Nei will contain both combination and count.
            for nei in neighbors:

                # Constraints: (1) visited, (2) deadend combination
                if nei[0] in visited or nei[0] in deadends:
                    continue

                # Constraints: (3) target is reached
                if nei[0] == target:
                    return nei[1]

                # Process: add to visited - remember only combination
                visited.add(nei[0])

                # Add to queue
                queue.append(nei)

        return -1

if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"

    print(Solution().openLock(deadends, target))