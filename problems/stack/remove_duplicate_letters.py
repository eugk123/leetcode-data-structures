"""
https://leetcode.com/problems/remove-duplicate-letters/submissions/
"""
class Solution:
    """
    Stack and Hashmap
    https://www.youtube.com/watch?v=2ayws5Y-WM4

    What makes this problem difficult is getting all unique letters in lexo order. 

    A naive approach would be n^2 time and constant space getting the minimum lexo order at every iteration
    afacf
    af c
    a  cf
    result = acf < afc

    We could try a queue or a sliding window, but the issue here is that we'll never catch duplicates that are within the window, but only duplicates in the front.
    afacf
    l r   -> af, don't traverse left pointer because "a" < "f" lexographically
    l  r  -> afc
    l   r -> afc

    Therefore, we need a data structure(s) that can continuously pop as well as tell us the popped letter exists later down the string.
    We capture the last index of each letter using a hashmap
    We use a stack to allow for continuous pops.
    We also need to handle duplicates, so we use a set for this for optimizing time. We could use the same stack to check for duplicates, but that would result in O(L) time per operation where L = len of stack.

    Let's run it again now
    last_index = {a:2, c:3, f:4}

    afacf   stack
    i       []      stack is empty, do nothing. add to stack -> [a]
     i      [a]     "f" > "a" so don't pop peek. add to stack -> [a,f]
      i     [a,f]   "a" is in duplicate -> skip
       i    [a,f]   "c" < "f" and "f" appears again later, pop peek -> [a]. Add to stack -> [a,c]
        i   [a,c]   "f" > "c" so don't pop peek, add to stack -> [a,c,f]
    result = "acf"
    
    Tiem and Space O(n)
    """
    def removeDuplicateLetters(self, s: str) -> str:
        # get final indices and store in hashmap - this tells you there are more repeats for each letter later.
        letter_to_final_index = {}
        for i in range(len(s)):
            letter_to_final_index[s[i]] = i
        
        # keep track of current letters in stack - this allows you to replace with a letter with a lesser lexo value
        stack = []
        
        # keep track of current letters in set - this allows you to check for duplicates
        check_duplicates = set()
        
        for i in range(len(s)):
            # print(stack)
            letter = s[i]
            
            # if duplicate, skip
            if letter in check_duplicates:
                continue
                
            # continuously check if current letter is lexographically lesser than previous letter (stack.peek())
            # also check if the previous letter will appear again in the future using the hashmap
            # if both are true, then pop from stack
            # also need to make sure stack is not empty. If empty, just continue
            if stack:
                peek = stack[len(stack) - 1]
                while letter < peek and i < letter_to_final_index[peek]:
                    stack.pop()
                    check_duplicates.remove(peek)
                    
                    if not stack:
                        break
                    peek = stack[len(stack) - 1]  # update peek
                    
            # add to data structures
            stack.append(letter)
            check_duplicates.add(letter)
            
        return "".join(stack)