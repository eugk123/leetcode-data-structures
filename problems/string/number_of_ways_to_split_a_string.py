"""
https://leetcode.com/problems/number-of-ways-to-split-a-string/
"""
class Solution:
    """
    https://leetcode.com/problems/number-of-ways-to-split-a-string/discuss/830536/Python-or-One-pass-or-Explained-and-Visualised
    """
    def numWays(self, s: str) -> int:
        # Count the total number of 1s and 0s
        ones_count = 0
        zeroes_count = 0
        for char in s:
            if char == '1':
                ones_count += 1
            if char == '0':
                zeroes_count += 1

        # If count == 0, then we need to figure out what the equation is for
        # Number of Zeroes -> Total combinations
        # 3 zeroes -> 1
        # 4 zeroes -> 1 + 2
        # 5 zeroes -> 1 + 2 + 3 ...
        # total = (n-1)(n-2)/2
        if ones_count == 0:
            if zeroes_count < 3:
                return 0
            if zeroes_count >= 3:
                return int((zeroes_count - 1) * (zeroes_count - 2) / 2) % (10 ** 9 + 7)

        # If count is not divisible by 3, then return 0
        if ones_count % 3 != 0:
            return 0

        # Number of ones per section
        ones_count_per_section = int(ones_count / 3)

        # Count the zeroes between each section
        # The solution will be (# of zeroes + 1 of section a) * (# of zeroes + 1 of section b)
        ones_count = 0
        product_a = 0
        product_b = 0
        for char in s:
            # If number of ones per section is met, then start counting zeroes
            if ones_count == ones_count_per_section and char == '0':
                product_a += 1

            if ones_count == ones_count_per_section * 2 and char == '0':
                product_b += 1

            if char == '1':
                if ones_count == ones_count_per_section * 2:
                    break
                ones_count += 1

        return (product_a + 1) * (product_b + 1) % (10 ** 9 + 7)

if __name__ == '__main__':
    print(Solution().numWays('10101'))