'''
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Examples:
    Input:          Output:
1)  s = "()"        true
2)  s = "()[]{}"    true
3)  s = "(]"        false
4)  s = "([)]"      false
5)  s = "{[]}"      true

:type s: str
:rtype: bool
'''
def validParentheses(s: str) -> bool:  # HashMap and Stack
    """
    Intuition: Use a map storing <open paren, close paren>. Use a stack to populate all the opening characters.
    When looping through each character, if it's a close paren, then pop the open equivalent from stack. Once done
    looping, if stack is empty, then return True.

    Algorithm:
        1. Initialize a stack S.
        2. Process each bracket of the expression one at a time.
        3. If we encounter an opening bracket, we simply push it onto the stack. This means we will process it later,
        let us simply move onto the sub-expression ahead.
        4. If we encounter a closing bracket, then we check the element on top of the stack. If the element at the top
        of the stack is an opening bracket of the same type, then we pop it off the stack and continue processing.
        Else, this implies an invalid expression.
        5. In the end, if we are left with a stack still having elements, then this implies an invalid expression.

    Time: O(n) because we simply traverse the given string one character at a time and push and pop operations on a stack
    take O(1) time
    Space: O(n) as we push all opening brackets onto the stack and in the worst case, we will end up pushing all the
    brackets onto the stack. e.g. ((((((((((.
    """
    # The stack to keep track of opening brackets.
    stack = []

    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    mapping = {")": "(", "}": "{", "]": "["}

    # For every bracket in the expression.
    for char in s:

        # If the character is an closing bracket
        if char in mapping:

            # Pop the topmost element from the stack, if it is non empty
            # Otherwise assign a dummy value of '#' to the top_element variable
            if stack:
                top_element = stack.pop()
            else:
                '#'

            # The mapping for the opening bracket in our hash and the top
            # element of the stack don't match, return False
            if mapping[char] != top_element:
                return False
        else:
            # We have an opening bracket, simply push it onto the stack.
            stack.append(char)

    # In the end, if the stack is empty, then we have a valid expression.
    # The stack won't be empty for cases like ((()
    return not stack

if __name__ == '__main__':
    print(validParentheses("{}{}"))

