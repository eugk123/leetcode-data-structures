class Solution:
    def numDecodings(self, s: str) -> int:

        # We know that s will never have two adjacent 0s.
        def dfs(index):
            if index in memo:
                return memo.get(index)
            
            # count when past last index
            if index >= len(s):
                return 1

            # If the string starts with a zero, it can't be decoded
            # Remember, two digit path will be able to continue
            if s[index] == '0':
                return 0

            # count at last index
            # this is an edge case because it has to be positioned after condition s[index] == 0
            # if the input ends with 0, this makes sure that isn't counted.
            if index == len(s) - 1:
                return 1
            
            # one digit path
            a = dfs(index + 1)

            # two digit path; valid only if two_digits <= 26
            b = 0 # initialize as 0
            two_digits = int(s[index:index+2])
            if 10 <= two_digits <= 26:
                b = dfs(index + 2)
            
            # MEMO Add
            memo[index] = a + b
            return a + b

        
        # edge case, leading 0 return 0
        if s[0] == "0":
            return 0
        
        # if len == 1, return 1
        if len(s) == 1:
            return 1
        
        # edge case, 00 or [3~9]0
        prev = "99"
        for letter in s:
            # if we have two adjacent 0s, return 0
            if prev == "0" and letter == "0":
                return 0
            
            # if we have leading number >= 3 with adjacent 0, return 0
            if int(prev) >= 3 and letter == "0":
                return 0
            
            prev = letter
        
        memo = {}
        return dfs(0)