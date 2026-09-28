# Problem: https://leetcode.com/problems/concatenation-of-array/
# Difficulty: Easy | Topic: Arrays
# Key idea: ans[i] = ans[i + n] = nums[i] - or just nums + nums.


class Solution(object):
    def getConcatenation(self, nums):
        return nums + nums


# Time:  O(n)  - why: `+` builds a new list of length 2n, copying every element
# Space: O(n)  - why: the new list (O(1) extra if the output isn't counted)
