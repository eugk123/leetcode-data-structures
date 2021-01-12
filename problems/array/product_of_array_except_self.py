class Solution:
    def productOfArrayExceptSelf(self, nums):  # Three Pass - HashMap
        """
        https://leetcode.com/problems/product-of-array-except-self/

        Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product
        of all the elements of nums except nums[i].

        Example:
        Input:  [1,2,3,4]
        Output: [24,12,8,6]

        Complexity:
        Time Complexity: We traverse the list containing n elements exactly three times. Since the hash table reduces the look up time
        to O(1), the time complexity is O(n).
        Space: O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly
        n elements

        :type nums: List[int]
        :rtype: output: List[int]
        """
        product = 1
        zeroes_count = 0
        output = []
        for num in nums:  # First pass - Get product total
            if num == 0:
                zeroes_count += 1  # Figure out how many zeroes
                num = 1  # Total product cannot be multiplied by a zero. So use 1.
            product = num * product  # Populate the total product

        # Scenario 1: 2 or more zeroes -> append(0)
        if zeroes_count >= 2:
            return [0] * len(nums)

        # Scenario 2: len(nums) == 2 and 1 zero, then flip
        if len(nums) == 2 and zeroes_count == 1:
            return [nums[1], nums[0]]

        # Scenario 3: 1 zero
        if zeroes_count == 1:
            for num in nums:  # Final pass - O(1) lookup to get item from Map.
                if num == 0:
                    output.append(int(product))  # Index is a zero, take product
                else:
                    output.append(0)  # Index isn't a zero, product = 0
            return output

        # Scenario 4: 0 zero
        for num in nums:
            output.append(int(product/num))  # No zeroes, take product/nums[i]
        return output


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(Solution().productOfArrayExceptSelf([9,0,-2]))