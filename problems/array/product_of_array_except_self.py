"""
https://leetcode.com/problems/product-of-array-except-self/
"""
class Solution:
    def productOfArrayExceptSelf(self, nums):  # Three Pass - HashMap
        """
        Problem is asking for O(n) solution without using division.
        
        Input:   1  2  3  4
        Output: 24 12  8  6

        The trick is to create a list of left and right products
        Input             1  2  3  4
        Left product  =   1  1  2  6
        ---->

        Input             1  2  3  4
        Right product =  24 12  4  1
        <----
        """

        # Initialize left and right product lists
        L = [0] * len(nums)
        R = [0] * len(nums)
        res = [0] * len(nums)

        # L[0] = 1
        L[0] = left_product = 1
        for i in range(1, len(nums)):
            left_product = left_product * nums[i - 1]
            L[i] = left_product

        # R[-1] = 1
        R[-1] = right_product = 1
        for i in reversed(range(0, len(nums) - 1)):
            right_product = right_product * nums[i + 1]
            R[i] = right_product

        for i in range(len(nums)):
            res[i] = L[i] * R[i]

        return res

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Solution().productOfArrayExceptSelf([9,0,-2]))