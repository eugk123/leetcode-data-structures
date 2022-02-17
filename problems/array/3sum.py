"""
https://leetcode.com/problems/3sum
"""
from typing import List
class Solution:
    """
    Sort, Hash map, Double loop

    https://www.youtube.com/watch?v=jzZsG8n2R9A

    sum of 3 distinct elements == 0

    [-1,0,1,2,-1,-4]
    x x x
    x     x  x

    First, sort. then create a map containing value to index
        map = {-4: 0, -1: 2, 0: 3, 1: 4, 2: 5}
    check if map contains two_sum = -nums[i] - nums[j] and adhere to the following conditions:
        1) new index is an unused index (not equal to i or j)
        2) new index is greater than j
    check if result does not already exist prior to appending

    [-4,-1,-1,0,1,2]    i + j + k = 0 -> two_sum = -nums[i] - nums[j]
      i  j              nums[i] = -4, nums[j] = -1, check if map contains two_sum = -nums[i] - nums[j] -> two_sum = 5, not in map
      i     j           two_sum = 5, not in map
      i       j         two_sum = 4, not in map
      i         j       two_sum = 3, not in map
      i           j     two_sum = 2, in map, but index j is in use
         i  j     x     iterate i, two_sum = 2, in map, index not in use, add to answer
         i    j x       two_sum = 1, in map, index not in use, add to answer
         i      j

    Time O(n^2)
    Space O(n)
    """
    def threeSumEugene(self, nums: List[int]) -> List[List[int]]:
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
                
                # nums[i] + nums[j] + two_sum = 0
                # two_sum = -nums[i] - nums[j]
                two_sum = -nums[i] - nums[j]
                
                # check if map contains two_sum
                if two_sum in value_to_index:
                    
                    # if map contains two_sum, make sure of the following
                    # 1) it is an unused index (not equal to i or j)
                    # 2) new index is of greater value than j
                    if value_to_index[two_sum] != i and value_to_index[two_sum] != j and value_to_index[two_sum] > j:
                        
                        # Keep only unique results
                        if [nums[i], nums[j], two_sum] not in result:
                            result.append([nums[i], nums[j], two_sum])
        
        return result
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the array - O(nlogn) time
        nums.sort()

        res = []

        # Iterate current pointer as the target and Use L and R pointer (two pointer) for each iteration
        for curr in range(len(nums)):

            # Since curr is one step behind left, if they are equal, traverse both to the right 1 step
            if curr > 0 and nums[curr] == nums[curr - 1]:
                continue

            # Update pointers
            left = curr + 1
            right = len(nums) - 1

            # Search between left and right pointer for any 3sum combinations
            while left < right:
                three_sum = nums[left] + nums[right] + nums[curr]

                # Found combination when L + R = C
                if three_sum == 0:
                    res.append([nums[left], nums[right], nums[curr]])
                    left += 1
                    # left pointer duplicate traversal
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

                # If sum < 0 -> move left pointer
                if three_sum < 0:
                    left += 1

                # If sum > 0 -> move right pointer (this also takes care of right pointer duplicates)
                if three_sum > 0:
                    right -= 1

        return res

if __name__ == '__main__':
    print(Solution().threeSum(nums=[-1,0,1,2,-1,-4]))
