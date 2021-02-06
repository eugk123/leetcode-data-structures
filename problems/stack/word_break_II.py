from typing import List
class Solution:
    def wordBreak(self, s, wordDict):
        """
        DFS w/ Memoization

        https://www.youtube.com/watch?v=uR3RElKnrkU&feature=emb_title

        Memoization stores unique string (key) with the list of possible sentences (value)
        """
        def helper(current):
            # We use a cache to store key-unique string values and value-result
            if current in memo:
                return memo.get(current)

            # Reset result for current string
            res = []

            if len(current) == 0:
                res.append("")
                return res

            # Traverse through each word in word dictionary
            for word in wordDict:

                # If the word doesn't start with the current string, then skip
                if current.startswith(word):
                    resultOfTheRest = helper(current[len(word):])
                    for item in resultOfTheRest:
                        # if end is reached, item is empty, therefore no space is required.
                        if item:
                            optionalSpace = " "
                        else:
                            optionalSpace = ""

                        # Take current word and add result (
                        res.append(word + optionalSpace + item)

            memo[current] = res
            return res

        memo = {}
        res = helper(s)
        print(res)
        return res

    def wordBreakDfs(self, s, wordDict):
        """
        Same as optimal except without the memoization.

        https://www.youtube.com/watch?v=uR3RElKnrkU&feature=emb_title
        """
        def helper(current):
            # We use a cache to store key-unique string values and value-result
            res = []

            if len(current) == 0:
                res.append("")
                return res

            # Traverse through each word in word dictionary
            for word in wordDict:

                # If the word doesn't start with the current string, then skip
                if current.startswith(word):
                    resultOfTheRest = helper(current[len(word):])
                    for item in resultOfTheRest:
                        if item:
                            optionalSpace = " "
                        else:
                            optionalSpace = ""
                        item = word + optionalSpace + item
                        res.append(item)

            return res

        res = helper(s)
        print(res)
        return res

    def wordBreakDfsLong(self, s: str, wordDict: List[str]) -> List[str]:
        """
        DFS TLE - This solution does not work as you are iterating through every character of the word dictionary.
        Takes way too long
        """
        def dfs(index, current, length):
            """
            :param index: current index of input string "s"
            :param current: current string
            :param length: total length of current string
            :return:
            """
            print(current, index)
            # If length is equal to length of s, then you found a solution
            if index == len(s):
                if length == len(s):
                    result.add(current)
                return

            # Find possible neighbors based on wordDict
            for word in wordDict:

                # For each word, compare letter by letter with input string s
                for i in range(len(word)):

                    # Make sure s[index + i] does not go out of bounds
                    if index + i == len(s):
                        # You want to break here to try another word.
                        break

                    # You want to use current index on the input string s. That way you can continue to traverse s.
                    elif word[i] == s[index + i]:

                        # If i reaches length of the word, then you found yourself a candidate.
                        if i == len(word) - 1:

                            # Execute dfs here
                            if current == "":
                                dfs(index + i + 1, current + word, length + len(word))
                            else:
                                dfs(index + i + 1, current + " " + word, length + len(word))

                        continue
                    else:
                        # You want to break here to try another word.
                        break
            return

        # Can have length updated as you traverse through current string

        result = set()

        dfs(0, "", 0)

        return list(result)




if __name__ == '__main__':
    Solution().wordBreak(s = "catsanddogcat", wordDict = ["cat", "cats", "c", "at", "and", "sand", "dog"])
    Solution().wordBreakDfs(s = "catsanddogcat", wordDict = ["cat", "cats", "c", "at", "and", "sand", "dog"])


