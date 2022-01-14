"""
https://leetcode.com/problems/minimum-window-substring
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Order does not matter
        First reduce the string to only input t letters
        Store all indices of that string
        ADOBACBECA -> ABACBCA
                      0345689
        Keep traversing right pointer until all letters are found
        Keep traversing left pointer until next first letter is found
        Repeat
        ABABCBCA  | t=ABC
        l   r      keep traversing right pointer until all letters are found (current is empty) c={} | We will also add duplicate letters d={A1 B1}
           lr      keep traversing left pointer until one letter is missing (current has a letter) c={A} | We also need to remove duplicate letters as we go empty d={}
           l   r   keep traversing right pointer until all letters are found (current is empty)  c={}
              1r   keep traversing left pointer until one letter is missing   c={B}
                   r-l < len(t)-1 and r = len(t)-1 end.
                   
                   
        AC | t=AC
        l
          r
        * During this whole loop, check for min indices
        * Convert indices to original input indices using the intersected map
        current={A0 C1}
        duplicate={A1 B1 C0}

        Time Complexity: O(s + t) - worst case O(s*2 + t)
        """
        def addToMap(letter, input_map):
            if letter in input_map:
                input_map[letter] += 1
            else:
                input_map[letter] = 1

        def removeFromMap(letter, input_map):
            if letter in input_map:
                input_map[letter] -= 1
                if input_map[letter] == 0:
                    input_map.pop(letter)
        
        # Set up maps - lc: letters to count map
        input_set = set()  # input is used to track which letters to pull 
        current_letter_map = {}  # current is fully populated. we use this to determine which pointer to move. 
        duplicate_letter_map = {}  # duplicate is used to track duplicate input letters
        
        for letter in t:
            addToMap(letter, current_letter_map)
            input_set.add(letter)
        
        # edge cases
        if s == t:  # same strings, then return s
            return s
        if len(s) < len(t):  # length of input s is less than length of input t
            return ""
        if not s:  # input s is empty
            return ""
        if t in s:  # substring in string is O(n)
            return t

        l = 0   # initialize pointers
        final_left = final_right = None  # initialize final indices
        min_length = math.inf   # we need to take work towards minimum length
        
        for r in range(len(s)): 
        
            # This condition is satisfied when not all letters in input string t have been found.
            if current_letter_map:
                
                letter = s[r]
            
                # Remove from current if exists. Otherwise, track duplicates.
                if letter in input_set:
                    if letter in current_letter_map:
                        removeFromMap(letter, current_letter_map)
                    else:
                        addToMap(letter, duplicate_letter_map)

            # During this iteration, if we found a valid substring, we want to traverse left pointer until one letter of input t is missing.
            while not current_letter_map:
                
                letter = s[l]
                
                # We update the indices and minimum length at every interation of this condition
                if letter in input_set:
                    length = r - l
                    if length < min_length:
                        min_length = length
                        final_left, final_right = l, r  # there are your final string indices

                    # Add to current and traverse left
                    if letter in duplicate_letter_map:
                        removeFromMap(letter, duplicate_letter_map)
                    else:
                        addToMap(letter, current_letter_map)

                # Traverse left pointer
                l += 1

        if final_left == None:
            return ""

        # Confirm again if we reached the end, we need to run the same 
        # Return string with min_length indices left, right
        return s[final_left:final_right+1]
