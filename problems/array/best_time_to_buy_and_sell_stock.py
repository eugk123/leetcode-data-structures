
def bestTimeToBuyAndSellStock(prices):  # Single Pass
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    Example:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                 Not 7-1 = 6, as selling price needs to be larger than buying price.

    Time Complexity: O(n), Single pass
    Space Complexity: O(1), Only two variables are used

    :type prices: List[int]
    :rtype: profit: int
    """
    low = float('inf')  # Set low; float('inf') is used for setting a variable with an infinitely large value
    profit = 0  # Set profit
    for i in prices:
        profit = max(profit, i - low)  # Take the max between profit and (current price - low)
        low = min(low, i)  # Take the min between low and current price
    return profit

def bestTimeToBuyAndSellStock_Eugene(nums):  # Sliding Window
    left = profit = 0
    for right in range(len(nums)):

        # Move the left pointer whenever the difference is positive
        while nums[right] - nums[left] < 0:
            left += 1
        profit = max(profit, nums[right] - nums[left])
    return profit

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(bestTimeToBuyAndSellStock([9, 1, 3, 5, 1, 3, 7]))