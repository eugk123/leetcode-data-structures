"""
https://leetcode.com/problems/product-of-array-except-self/
"""
class Solution:
    def productOfArrayExceptSelfEugene(self, nums):  # Two Pass - constant space
        """
        Two Pass (Constant Space)

        First pass, get total without zeroes and count number of zeroes.

        Second pass, we have three type of answers:
        1 - zero_count > 1 -> all zeroes
        2 - zero_count = 1 -> all zeroes except index that has the zero element. Replace that index with the total.
        3 - zero_count = 0 -> total/nums[i] at every iteration!
        
        Time O(n)
        Space O(1)
        """
        count = 0
        total = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
                continue           
            total = total * nums[i]
        
        
        if count > 1:
            # zeroes count > 1, zero array
            for i in range(len(nums)):
                nums[i] = 0
        elif count == 1:
            # zeroes count = 1, element with zero is replaced with total
            for i in range(len(nums)):
                if nums[i] == 0:
                    nums[i] = total
                else:
                    nums[i] = 0
        else:
            # zeroes count = 0, do the usual - product / nums[i]
            for i in range(len(nums)):
                nums[i] = int(total/nums[i])
        
        return nums

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