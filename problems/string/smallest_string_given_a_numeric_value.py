"""
https://leetcode.com/problems/smallest-string-with-a-given-numeric-value
"""
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # Going to find the total number of 26 chunks
        n_z = int(k/26)
        remainder = k % 26        
        
        # number of 'a's is intended to fill the rest except the last number
        n_a = n - n_z - 1
        

        # last number is going to be the remainder subtracted by the total number of 'a's
        last_number = remainder - n_a
        print(n_z, n_a, remainder, last_number)
        # if last number is negative, it means we need to decrease the number of z's until last number is positive.
        while last_number <= 0:
            n_z -= 1

            # remainder and last_number is updated with the trimmed "z"
            remainder += 26
            n_a = n - n_z - 1
            last_number = remainder - n_a
            print(n_z, n_a, last_number)

        
        result = []
        if n_a == -1:
            for i in range(n):
                result.append("z")
            return "".join(result)
        
        # What if n_z == 0?
        # Then we just need to add as many 'a's with the last_number.

        # If n_z + remainder >= n, we can proceed with the usual
        # fill the rest with 1s until we have one spot left
        # that final spot will be filled with the remainder
        for i in range(n_a):
            result.append("a")
        result.append(chr(ord('a') + last_number - 1))
        for i in range(n_z):
            result.append("z")

        return "".join(result)