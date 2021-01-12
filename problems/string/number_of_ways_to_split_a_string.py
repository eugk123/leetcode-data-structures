"""
https://leetcode.com/problems/number-of-ways-to-split-a-string/
"""
class Solution:
    """
    https://leetcode.com/problems/number-of-ways-to-split-a-string/discuss/830536/Python-or-One-pass-or-Explained-and-Visualised
    """
    def numWays(self, s: str) -> int:
        m = 10 ** 9 + 7  # Take the modulus of 10^9 + 7

        # Grab the indices and count for "1"
        ones_indices = []
        for i in range(len(s)):
            if s[i] == '1':
                ones_indices.append(i)
        ones_count = len(ones_indices)

        # Scenario 3) Zero 1s scenario, only 0s
        if ones_count == 0:
            n = len(s)
            return int((n - 1) * (n - 2) / 2 % m)

        # Scenario 2) Total number of 1s not divisible by 3
        remainder = ones_count % 3
        if remainder > 0:
            return 0

        # Scenario 3) Total number of 1s divisible by 3
        a = int(ones_count / 3 - 1)
        b = int(ones_count / 3)
        c = int(ones_count / 3 * 2 - 1)
        d = int(ones_count / 3 * 2)

        # Number of zeros between block 1 and block 2
        x = ones_indices[a] - ones_indices[b]
        # Number of zeros between block 2 and block 3
        y = ones_indices[c] - ones_indices[d]

        ans = x * y % m
        return (int)(ans)



if __name__ == '__main__':
    print(Solution().numWays('10101'))