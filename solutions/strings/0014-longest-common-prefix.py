# Problem: https://leetcode.com/problems/longest-common-prefix/
# Difficulty: Easy | Topic: Strings
# Key idea: after sorting, the first and last words are the most different - their common prefix
#           is shared by every word in between, so compare only those two.


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""


        strs.sort()
        first = strs[0]
        last = strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]


# Time:  O(n log n * m)  - why: sorting n strings, each comparison up to m chars (column-by-column is O(n * m))
# Space: O(1) extra      - why: sorts in place (note: strs.sort() changes the caller's list; sorted(strs) wouldn't)
