def twoSum(nums, target):  # Hash Table (Two-pass)
    """
    https://leetcode.com/problems/two-sum/
    https://www.youtube.com/watch?v=U8B984M1VcU

    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
    target.

    Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].

    Complexity:
    Time: O(n). We traverse the list containing n elements exactly twice. Since the hash table reduces the look up time
    to O(1), the time complexity is O(n).
    Space: O(n). The extra space required depends on the number of items stored in the hash table, which stores exactly
    n elements

    Initution:
    :type nums: List[int]
    :type target: int
    :rtype: indices: List[int]
    """
    map = dict()
    for i in range(0, len(nums)):  # Added O(n) space due to creating an equivalent map of the array
        map[nums[i]] = i  # We store each element as { Key=Number, Value=Index } because we can only grab the value of the map using it's key
    for i in range(0, len(nums)):  # While iterating through each element
        complement = target - nums[i]   # We take the complement and the value (nums[i]) then store it into an Array
        if complement in map and map.get(complement) != i:
            return [i, map[complement]]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nums = [2, 4, 3, 5]
    target = 5
    print(twoSum(nums, target))