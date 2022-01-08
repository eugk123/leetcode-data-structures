"""
https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Constraints:
1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        Understanding Problem Constraints:
        Understand that integer limits at 2^31 = 2,147,483,647. If we go beyond this value, it will overflow into a negative value.
        With the given max constrant of num.length is 200, we cannot simply convert the entire string into a integer since integer max length is 10.
        
        The algorithm is broken into two techniques:
        1) Multiplication of digits and population of matrix -> O(n*m)
        2) Summation of multiple numbers by using a matrix -> O(n*m)
        
        where n = len(num1) and m = len(num2)
        Time Complexity: O(n*m)
        Each technique consists of a double for loop through each input string.
        
        Space Complexity: O(n*m)
        Matrix of size n*m.
        """
        # Edge Case, num1 = 0
        if len(num1) == 1:
            if int(num1) == 0:
                return "0"
        
        # Edge Case, num2 = 0
        if len(num2) == 1:
            if int(num2) == 0:
                return "0"
            
        # Matrix will be of length(num1 + num2) by length(num2). +1 comes from the possibility of the final leftmost product being 2 digits
        matrix_columns = len(num1)+len(num2)
        matrix = [['0']*(matrix_columns) for i in range(len(num2))]
        
        # Get all products and populate matrix
        for i in range(0, len(num2)):
            carry = 0
            bottom_index = len(num2) - 1 - i   # Backwards len(num2) = 3 -> index 2, 1, 0
            bottom_digit = num2[bottom_index]
            
            for j in range(0, len(num1)):
                top_index = len(num1) - 1 - j   # Backwards len(num1) = 2 -> index 1, 0
                top_digit = num1[top_index]
                
                product = int(bottom_digit) * int(top_digit) + carry

                # Carry over 1st digit if product has 2 digits
                if product >= 10:
                    carry = product // 10
                elif product < 10:
                    carry = 0
                
                # Each product, we're only taking rightmost digit.
                # However, final leftmost product we take both digits.
                if top_index > 0 and product >= 10:
                    current = str(product - carry * 10)
                elif top_index > 0 and product < 10:
                    current = str(product)
                elif top_index == 0:
                    current = str(product)
                    
                # matrix population for capturing all product digits
                # We add len(num2) to shift as far right on the matrix as possible
                # We subtract by i to shift to left base 10 every iteration
                matrix[i][top_index + len(num2) - i] = current

                # If final leftmost product is only one digit, we only populate the 2nd index of the sum matrix
                # Otherwise, populate both 1st and 2nd index
                if len(current) == 2:
                    matrix[i][top_index + len(num2) - 1 - i] = current[0]
                    matrix[i][top_index + len(num2) - i] = current[1]
                
        print(matrix)
        
        result = ""
        carry = 0
        # Finally add all rows together. Remember as you move down each row, you must multiply by 10^bottom_index
        # We are taking sums starting from the far right index - hence, we use reversed
        """
        [['0', '0', '8', '9', '9', '1'], 
         ['0', '8', '9', '9', '1', '0'], 
         ['8', '9', '9', '1', '0', '0']]
        1221
        998001
        """
        for i in reversed(range(len(matrix[0]))):  # len(matrix[0]) -> first row
            sum_column = 0
                        
            for j in range(len(matrix)):  # len(matrix) -> first column
                
                # Need to add from right-side to allow for carry
                sum_column = sum_column + int(matrix[j][i])
                
            sum_column = sum_column + carry

            # Carry over 1st digit if sum has 2 digits
            if sum_column >= 10:
                carry = sum_column // 10
                sum_column = sum_column - carry*10
            else:
                carry = 0
            
            if i > 0:
                result = str(sum_column) + result
            elif i == 0 and sum_column > 0:
                result = str(sum_column) + result
            elif i == 0 and sum_column == 0:
                result = result
        return result