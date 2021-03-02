"""
https://leetcode.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters/
"""
class Solution:
    def modifyString(self, s: str) -> str:
        """
        We know if we use 3 different characters, we can answer any test case with infinite number of ?s.

        '????' -> 'abca'
        """
        res = []
        for i in range(len(s)):
            if s[i] == '?':

                # Option of 3 letters to replace the question mark
                for replacement_letter in ['a', 'b', 'c']:

                    # If any of these are repeating on the right or left, continue
                    # Make sure to use result string when checking backwards.
                    if i > 0 and res[i - 1] == replacement_letter:
                        continue

                    if i < len(s) - 1 and s[i + 1] == replacement_letter:
                        continue

                    # If not, append then break out of this for loop
                    res.append(replacement_letter)
                    break
            else:
                res.append(s[i])
        return "".join(res)

if __name__ == '__main__':
    print(Solution().modifyString(s='abc?abc?abc'))