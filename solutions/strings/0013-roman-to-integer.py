# Problem: https://leetcode.com/problems/roman-to-integer/
# Difficulty: Easy | Topic: Strings
# Key idea: dict of symbol values; going left to right, subtract a symbol if it's smaller
#           than the next one (IV, IX, XL...), otherwise add it.


class Solution(object):
    def romanToInt(self, s):
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        n = len(s)

        for i in range(n):
            # If the current value is smaller than the next value, subtract it
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]

        return total


# Time:  O(n)  - why: one pass, O(1) dict lookup per symbol
# Space: O(1)  - why: the dict always has 7 entries
