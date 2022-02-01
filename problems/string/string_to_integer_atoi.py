"""

"""
class Solution:
    """
    One Pass w/ Two Pointer - Constant Space
    
    "    -6412aasfa"
          l  r
    return int(s[l:r+1])
    
    Approach: Try to figure out exactly what conditions are needed to get a valid result given the questions conditions.
    Here were a few things I thought were most important that I set as conditions in my linear pass.
    - Remove all leading spaces
    - Positive or Negative based on leading operator (must be next to integer)
    - Takes first number
    - If first letter is not a number, then return 0
    - Return max integer if number exceeds max integer

    With these conditions, I used booleans to determine whether leading spaces were removed
    and whether the result is positive or negative.

    I used two pointers to determine the start and end of the number.

    I first focused on removing all leading spaces. Then I focused on the operator. Then I focused on returning the max integer.

    Here are some Edge cases:
    1. s = " "
    2. s = "+"  

    Time O(N)
    Space O(1)
    """
    def myAtoiEugene(self, s: str) -> int:
        def isLetterANumber(letter):
            if 48 <= ord(letter) <= 57:
                return True
            return False
        
        def getMaximumInteger(number):
            if number < -2147483648:
                return -2147483648
            elif number > 2147483647:
                return 2147483647
            return number
            
        is_leading_spaces_gone = False
        is_positive = False
        
        if not s:
            return 0
        
        left = None
        right = None
        
        # Skip leading spaces
        for i in range(len(s)):
            letter = s[i]
            
            # Get rid of leading spaces
            if letter == " " and not is_leading_spaces_gone:
                continue
            if letter != " " and not is_leading_spaces_gone:
                
                is_leading_spaces_gone = True
                
                # Check if it is an operator
                if letter == "+":
                    is_positive = True
                    left = i + 1
                    
                    # It's possible next number is not an integer or reached end of length, so check
                    if left == len(s):
                        return 0
                    if not isLetterANumber(s[left]):
                        return 0
                    
                elif letter == "-":
                    is_positive = False
                    left = i + 1
                    
                    # It's possible next number is not an integer or reached end of length, so check
                    if left == len(s):
                        return 0
                    if not isLetterANumber(s[left]):
                        return 0

                elif isLetterANumber(letter):
                    is_positive = True
                    left = i
                    
                else:
                    # This means, we have a non-number.
                    return 0
                
            
            # At this point, we've reached the first integer. We will keep going until letter is not a number. Then we set the right pointer
            # Use an elif to ensure we don't run this block until leading spaces are gone
            elif not isLetterANumber(letter):
                right = i - 1
                break
            
        
            # print(i, left, right)

        # If end was reached and last letter was a number, then we set right pointer at the end
        if isLetterANumber(letter):
            right = i
        
        # Edge case: " "  only spaces, then left = None
        if left == None:
            return 0
        

        # Finally, convert answer to integer
        if is_positive:
            number = int(s[left:right+1])
        else:
            number = int("-" + s[left:right+1])
        
        return getMaximumInteger(number)