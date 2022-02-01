"""
https://leetcode.com/problems/next-greater-element-ii/
"""
class Solution:
    """
    Pretty much, only one position (the max) will have a -1 result. Everything else will have a next greater number. The tricky part is figuring out the value of the next greater number.

    nums = 2 1 3 4 6 5
    res = 3 3 4 5 - 6

    The best solution is using a stack of tuples (num, index) and have an initial results array of -1s.

    2 1 3 4 6 5
    i           stack empty, stack = [(2,0)]
    i         1 < peek, add to stack, stack = [(2,0) (1,1)]
        i       [while] 3 >= peek, pop, add to result using index, stack = [2], result = [-1 3 -1 -1 -1 -1 -1]
        i       [while] 3 >= peek, pop, add to result, stack = [], result = [3 3]
        i         At the end of while loop, add to stack, stack = [(3,2)],
        i     [while] 4 >= peek, pop, add to result via appendleft, stack = [], result = [3 3 4 -1 -1 -1 -1]
        i       At the end of while loop, add to stack, stack = [(4,3)]
        
    Return res[:len(nums)] = [3 3 4 5 -1 6]

    2 1 7 4 3 5 4 stack                 res
        i         [(2,0) (1,0)]         [- - - - - - -] pop2, pop1, append7
              i   [(7,3) (4,4) (3,5)]   [7 7 - - - - -] pop3, pop4, append6
                  [(7,3) (5,6)]         [7 7 - 5 5 - -] pop6, pop7, append8
                i [(7,3) (5,6) (4,7)]   [7 7 - 5 5 - -] end is reached, but this doesn't give us all the results.
                
    We can try to use the existing contents of the stack to figure out the rest of the result, but the problem is we need the order of the nums to accurately get the "next" number.
    
    So a strategy that works, is we can double the contents of the initial array, perform the above algo, then return the result of the size of the initial array.
    double_nums = nums + nums
    
    Where we left off...
    nums 2 1 7 4 3 5 4 2 1 7 4 3 5 4
    res  7 7 - 5 5 - -

    nums 2 1 7 4 3 5 4 2 1 7 4 3 5 4
    res  7 7 - 5 5 7 7 7 7 - 5 5 - -
    
    Eventually, with a double sized nums, we will have gotten a full answer for the nums-length result.
    return res[:len(nums)] = [7 7 -1 5 5 7 7]
    """
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []

        double_nums = nums + nums
        result = [-1] * len(double_nums)

        for i in range(len(double_nums)):
            num = double_nums[i]
            if stack:
                while num > stack[len(stack) - 1][0]:
                    
                    # Populating the index of the stack peek (previous) number with the current number (next)
                    index = stack.pop()[1]
                    result[index] = num
                    
                    # Break condition if stack becomes empty
                    if not stack:
                        break
            
            
            stack.append((double_nums[i], i))   # append (value, index)
        
        # The final stack pop is the first element in the remaining stack which is the greater number. This should be -1. 
        return result[:len(nums)]