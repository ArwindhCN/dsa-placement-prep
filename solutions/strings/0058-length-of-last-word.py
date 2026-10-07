# Problem: https://leetcode.com/problems/length-of-last-word/
# Difficulty: Easy | Topic: Strings
# Key idea: s.split() (no argument) splits on runs of whitespace and drops leading/trailing spaces,
#           so the last item is the last word.


class Solution(object):
    def lengthOfLastWord(self, s):
        words = s.split()

        return len(words[-1])


# Time:  O(n)  - why: split scans the whole string once
# Space: O(n)  - why: split builds a list of all words
# Notes: s.split(" ") would break on trailing/double spaces (gives empty strings).
#        O(1)-space version: from the end, skip spaces, then count letters until the next space.
