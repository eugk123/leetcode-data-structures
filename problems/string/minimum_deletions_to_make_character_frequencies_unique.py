"""
://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
"""
class Solution:
    def minDeletions(self, s: str) -> int:
        # First pass, add to hashmap (key-letter, val-number)
        res = 0

        letter_to_frequency = {}
        for letter in s:
            if not letter_to_frequency.get(letter):
                letter_to_frequency[letter] = 1
            else:
                letter_to_frequency[letter] += 1

        # Second pass, move from previous hashmap -> new hashmap (key-val, val-letter)
        frequency_to_letter = {}

        # Grab each item from the previous hashmap
        for text, frequency in letter_to_frequency.items():

            if frequency not in frequency_to_letter:
                frequency_to_letter[frequency] = text

            # Otherwise we know the current frequency exists, so we need to subtract by 1 and count that.
            else:

                while frequency in frequency_to_letter:
                    frequency -= 1
                    res += 1

                    # If there is none left, we can skip
                    if frequency == 0:
                        break

                frequency_to_letter[frequency] = text

            print(frequency_to_letter)

        return res
