# Problem: https://leetcode.com/problems/running-sum-of-1d-array/
# Difficulty: Easy | Topic: Arrays
# Key idea: keep a running total; each answer = previous total + current number.


class Solution(object):
    def runningSum(self, nums):
        next=0
        for i in range(len(nums)):
            next+=nums[i]
            nums[i]=next
        return nums


# Time:  O(n)  - why: one pass, one addition per element (re-adding from the start each time would be O(n^2))
# Space: O(1)  - why: overwrites nums in place; only one extra variable
# Note: `next` shadows Python's built-in next() - rename to `total`.
