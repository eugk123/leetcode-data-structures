"""
https://leetcode.com/problems/utf-8-validation/
"""


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        """
        Case 1: One-byte Character (bit sequence - 0xxxxxxx)
        If first bit is 0, then return True. Otherwise return False

        Case 2: n-bytes character (bit sequence - 110xxxxx, 1110xxxx, 1110xxxx, 11110xxx)
        The problem specifically states "the first n-bits are all one's." meaning there should be no starting 0s. Therefore, don't worry about that edge case.

        The following octets should follow this sequence based on first octet.
        If it starts with 1s, then look for total number of consecutive 1s "n"
        the total number of addtional bytes is going to be n-1 bytes
        110 -> n = 2 -> n-1 = 1 extra bytes
        1110 -> n = 3 -> n-1 = 2 extra bytes
        11110 -> n = 4 -> n-1 = 3 extra bytes (This is the upper bound stated by problem)
        """
        # Number of extra bytes (max 3)
        count = 0
        for num in data:

            binary_rep = '{0:08b}'.format(num)  # Get 8 LSB in base 2 (binary)

            if count == 0:
                # Using the first octet, analyze the octet sequence
                for binary in binary_rep:
                    if binary == '0':
                        break
                    count += 1

                # We cannot have just 0 extra bytes or more than 3 extra bytes according to the problem!
                if count == 1 or count > 4:
                    return False

                # So no 1s in current binary representation
                if count == 0:
                    continue

            else:
                # For extra bytes, they must start with '10' or else return False
                if binary_rep[0:2] != '10':
                    return False

            count -= 1

        # If there are expected remaining extra bytes, return False
        if count > 0:
            return False
        return True