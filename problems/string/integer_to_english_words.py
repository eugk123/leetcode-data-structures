"""
https://leetcode.com/problems/integer-to-english-words
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        """
        This is my solution.

        However, I'm not done yet. I thought this was sufficient enough at this point.

        It is failing at the following edge cases:
        1000000 -> One Million (printing One Million Thousand).

        Need to fix this.

        O(N) Time and O(N) Space due to added queue
        """
        # Base Case - 0
        if num == 0:
            return "Zero"

        # current, digit
        map = {
            (1, 1): "One",
            (2, 1): "Two",
            (3, 1): "Three",
            (4, 1): "Four",
            (5, 1): "Five",
            (6, 1): "Six",
            (7, 1): "Seven",
            (8, 1): "Eight",
            (9, 1): "Nine",

            (2, 2): "Twenty",
            (3, 2): "Thirty",
            (4, 2): "Forty",
            (5, 2): "Fifty",
            (6, 2): "Sixty",
            (7, 2): "Seventy",
            (8, 2): "Eighty",
            (9, 2): "Ninety",

            (10, 0): "Ten",
            (11, 0): "Eleven",
            (12, 0): "Twelve",
            (13, 0): "Thirteen",
            (14, 0): "Fourteen",
            (15, 0): "Fifteen",
            (16, 0): "Sixteen",
            (17, 0): "Seventeen",
            (18, 0): "Eighteen",
            (19, 0): "Nineteen",

            (0, 3): "Hundred",
            (0, 4): "Thousand",
            (0, 7): "Million",
            (0, 10): "Billion"
        }

        queue = collections.deque()
        digit = 0
        for num in list(str(num)):
            queue.appendleft(int(num))
            digit += 1

        res = ""
        while queue:
            current = queue.pop()

            # current = 1 -> One
            # digit = 10 -> Billion
            # Zeroes, skip at digit = 1, 2,3, 5,6, 8,9, ..
            if current == 0 and digit % 3 != 1:
                digit -= 1
                continue

            # Hundreds are at digit = 3,6,9,12 ...
            if digit % 3 == 0:

                # ex: " Three Hundred"
                res = res + " " + map.get((current, 1)) + " " + map.get((0, 3))

            # Tens are at digit = 2,5,8,11 ...
            elif digit % 3 == 2 and current != 1:
                res = res + " " + map.get((current, 2))

            # Edge Case: (10 ~ 19), this occurs at digit = 2,5,8,11 ...
            elif (digit % 3) == 2 and current == 1:
                current = current * 10 + queue.pop()
                res = res + " " + map.get((current, 0))

                digit -= 1  # Need to subtract another digit
                # This zero will be used for another edge case:
                # 12000 -> Twelve Thousand --- this would capture the thousand
                current = 0
                if digit > 3 and digit % 3 == 1:
                    # Thousands - digit = 4
                    # Millions - digit = 7
                    # Billions - digit = 10
                    res = res + " " + map.get((0, digit))

                digit -= 1  # Need to subtract another digit
                continue

            # Singles are at digit = 1,4,7,10 ..
            elif digit % 3 == 1:
                # Ones - digit = 1
                # Thousands - digit = 4
                # Millions - digit = 7
                # Billions - digit = 10
                if current == 0 and digit == 1:
                    continue
                    digit -= 1

                elif current == 0:
                    res = res + " " + map.get((0, digit))

                elif digit == 1:
                    res = res + " " + map.get((current, 1))

                else:
                    res = res + " " + map.get((current, 1)) + " " + map.get((0, digit))

            digit -= 1

        return res[1:]