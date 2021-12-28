"""
https://leetcode.com/problems/multiply-strings/
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Understanding Problem Constraints:
        Understand that integer limits at 2^31 = 2,147,483,647. If we go beyond this value, it will overflow into a negative value.
        With the given max constrant of num.length is 200, we cannot simply convert the entire string into a integer since integer max length is 10.
        
        The algorithm is broken into two techniques:
        1) Multiplication of digits with string concatenation -> O(n^2)
        2) Summation of multiple numbers by using a matrix -> O(n*m)
        
        where n = len(num1) and m = len(num2)
        Time Complexity: O(n^2 + n*m)
        Combining the two techniques.
        
        Space Complexity: O(n*m)
        Matrix of size n*m
        """ 