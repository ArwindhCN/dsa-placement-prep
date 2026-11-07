# Problem: https://leetcode.com/problems/is-subsequence/
# Difficulty: Easy | Topic: Strings
# Key idea: two pointers on two strings - j always moves through t, i moves only on a match;
#           s is a subsequence if i reaches the end of s.


class Solution(object):

    def isSubsequence(self, s, t):
        i = 0  # tracks s
        j = 0  # tracks t


        while i < len(s) and j < len(t):

            if s[i] == t[j]:
                i += 1

            j += 1


        return i == len(s)


# Time:  O(len(t))  - why: j advances every loop pass
# Space: O(1)       - why: two indexes
