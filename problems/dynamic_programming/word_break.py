class Solution:
    """
    Try all possible combination of words. Check s[i : i + len(word)] == word, if so, dfs(i + len(word))

    s = "catsandog" wordDict = ["cats","cat","and","dog","sand"]
    catsandog
    cat -> sandog
           sand -> og; no matching word found -> False
    cats -> andog
            and -> og; False

    s = "leetcode" wordDict = ["leet", "code"]
    leetcode
    leet -> code; i = 0 + 4 + 4 = 8 = len(leetcode) -> True

    Time O(n^3) we are traversing the wordDict N number of words, N times
    Space O(n) size of cache or depth of recursion stack
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def dfs(i):
            if i in memo:
                return memo.get(i)
            
            # end is reached, then we know it works
            if i == len(s):
                return True
            
            # try each word
            ans = False
            for word in wordDict:
                
                # index must be within bound
                if i + len(word) <= len(s):
                    
                    # check if substring is in worddict.
                    if s[i:i+len(word)] == word:
                        
                        # if so, go deeper, until end is reached
                        ans = dfs(i + len(word))
                        if ans:
                            return True
            
            memo[i] = ans                    
            return ans
        
        memo = {}
        return dfs(0)