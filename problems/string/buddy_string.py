class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        letter_count = [0]*26
        
        count = 0
        index1 = None
        index2 = None
        
        for i in range(len(s)):
            letter_count[ord(s[i]) - ord('a')] += 1
            
            if s[i] != goal[i]:
                count += 1
                
                if index1 == None:
                    index1 = i
                else:
                    index2 = i
                
        if count == 0 and max(letter_count) >= 2:
            # aab aab
            # aaa aaa
            return True
        elif count == 0 and max(letter_count) <= 1:
            # ab ab
            # abc abc
            return False

        if count == 1 or count >= 3:
            # ab ap
            # abbb abbp
            # abc bcd
            return False
        
        # swap index1 and index2
        print(index1, index2)
        
        tmp1 = s[index1]
        tmp2 = s[index2]

        print(s[0:index1] + tmp2 + s[index1+1:index2] + tmp1 + s[index2+1:])
        if s[0:index1] + tmp2 + s[index1+1:index2] + tmp1 + s[index2+1:] == goal:
            return True
        return False