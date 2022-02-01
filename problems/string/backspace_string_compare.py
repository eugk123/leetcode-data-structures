"""
https://leetcode.com/problems/backspace-string-compare/
"""
class Solution:
    """
    ab#c    ad#c
    s       t    s == t, -1 on both indices
    s       t     while s == #, move s left 
    s              if s[i-1] == #, move s left
    s
            t      while t == #, move t left
            t       if t[i-1] == #, move t left                
                    s == t, -1 on both indices, end loop since both s and t are < 0

    We want to traverse index until a valid letter is found that doesn't need to be backspaced. We do this for both t and s. 
    Then we compare the letters. If letters are the same, traverse both indices. If not the same, return False.

    Backspace conditions
    bta#aa###
        iii     backspace, count and traverse, count = 3
        ii        count > 0, -count and traverse, count = 1
    i          backspace, count and traverse, count = 2
    ii           count > 0, -count and traverse, count = 0
    i             count = 0. finally ready to check on other input

    Time O(n+m)
    Space O(1)
    """
    def backspaceCompare(self, s: str, t: str) -> bool:
        # Iterate backwards and count number of backspaces when letter == "#"
        idx_s = len(s) - 1
        idx_t = len(t) - 1

        while idx_s >= 0 or idx_t >= 0:
            # If current index is a backspace, keep traversing until backspace count == 0
            while s[idx_s] == "#":
                backspace_s = 1  # count
                idx_s -= 1  # traverse
                while backspace_s > 0:
                    if s[idx_s] == "#":
                        backspace_s += 1
                        idx_s -= 1
                    else:
                        backspace_s -= 1
                        idx_s -= 1
                    if idx_s < 0:
                        break
                if idx_s < 0:
                    break
            
            # Do the same for t
            while t[idx_t] == "#":
                backspace_t = 1  # count
                idx_t -= 1  # traverse
                while backspace_t > 0:
                    if t[idx_t] == "#":
                        backspace_t += 1
                        idx_t -= 1
                    else:
                        backspace_t -= 1
                        idx_t -= 1
                    if idx_t < 0:
                        break
                if idx_t < 0:
                    break
                        
            # At this point, we may have a negative index.
            if idx_t < 0 and idx_s >= 0:
                return False
            elif idx_s < 0 and idx_t >= 0:
                return False
            elif idx_t < 0 and idx_t < 0:
                return True
            elif s[idx_s] == t[idx_t]:
                idx_s -= 1
                idx_t -= 1
            else:
                return False
            
        return True