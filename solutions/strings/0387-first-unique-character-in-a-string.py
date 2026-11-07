# Problem: https://leetcode.com/problems/first-unique-character-in-a-string/
# Difficulty: Easy | Topic: Strings
# Key idea: two passes - count every char in a dict, then return the first index whose count is 1.


class Solution(object):

    def firstUniqChar(self, s):

        char_counts = {}
        for char in s:
            if char in char_counts:
                char_counts[char] = char_counts[char] + 1
            else:
                char_counts[char] = 1


        for i in range(len(s)):
            char = s[i]

            if char_counts[char] == 1:
                return i


        return -1


# Time:  O(n)  - why: two passes over s, O(1) dict operations
# Space: O(1)  - why: at most 26 lowercase letters in the dict
# Notes: counting shortcut: char_counts[char] = char_counts.get(char, 0) + 1, or Counter(s).
#        Two passes are needed: while reading s you can't know if a char repeats later.
