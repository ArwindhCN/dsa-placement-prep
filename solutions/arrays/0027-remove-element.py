# Problem: https://leetcode.com/problems/remove-element/
# Difficulty: Easy | Topic: Arrays
# Key idea: write pointer - i reads every element, k marks where the next kept element goes.


class Solution(object):
    def removeElement(self, nums, val):
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k


# Time:  O(n)  - why: one pass, each element read once and written at most once
# Space: O(1)  - why: overwrites nums in place; only k
