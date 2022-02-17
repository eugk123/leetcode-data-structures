"""
https://leetcode.com/problems/4sum/
"""
from typing import List
class Solution:
    """
    This problem solution is pretty much the same as 3sum. 
    
    The only difference is the summation equation: nums[i] + nums[j] + nums[k] = target, which results in three_sum = -nums[i] - nums[j] - nums[k] + target
    
    Time O(n^3)
    Space O(n)    
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # sort, we've decided that best possible answer is n^2

        # populate a value to index map for constant lookup time
        value_to_index = {}        
        for i in range(len(nums)):
            value_to_index[nums[i]] = i

            result = []
        for i in range(len(nums)):
            
            # We can skip i when the previous number is the same to remove duplicate answers
            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue
            for j in range(i + 1, len(nums)):
                
                
                for k in range(j + 1, len(nums)):
                    # nums[i] + nums[j] + two_sum = 0
                    # two_sum = -nums[i] - nums[j]
                    three_sum = -nums[i] - nums[j] - nums[k] + target

                    # check if map contains two_sum
                    if three_sum in value_to_index:
                        # if map contains two_sum, make sure of the following
                        # 1) it is an unused index (not equal to i or j)
                        # 2) new index is of greater value than j
                        if value_to_index[three_sum] != i and value_to_index[three_sum] != j and value_to_index[three_sum] != k and value_to_index[three_sum] > k:

                            # Keep only unique results
                            if [nums[i], nums[j], nums[k], three_sum] not in result:
                                result.append([nums[i], nums[j], nums[k], three_sum])
        
        return result
if __name__ == '__main__':
    print(Solution().threeSum(nums=[-1,0,1,2,-1,-4]))
