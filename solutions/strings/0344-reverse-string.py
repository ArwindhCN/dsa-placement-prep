# Problem: https://leetcode.com/problems/reverse-string/
# Difficulty: Easy | Topic: Strings
# Key idea: two pointers from both ends - swap s[l] and s[r], move both inward until they meet.


class Solution(object):
    def reverseString(self, s):
        l = 0
        r = len(s) - 1
        while (l<r):

            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1

        return s


# Time:  O(n)  - why: n/2 swaps
# Space: O(1)  - why: swaps inside s
# Notes: `return s` isn't needed (problem returns nothing).
#        s[::-1] fails here: it builds a new list and leaves the original s unchanged.
#        Forgetting l += 1 / r -= 1 gave TLE (infinite loop).
