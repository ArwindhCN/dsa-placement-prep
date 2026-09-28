# Problem: https://leetcode.com/problems/max-consecutive-ones/
# Difficulty: Easy | Topic: Arrays
# Key idea: count the current streak of 1s, reset it on 0, update the max on every 1
#           (updating only on 0 misses a streak that runs to the end of the array).


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max = 0
        temp_sum = 0
        for i in nums:
            if i == 0:
                temp_sum = 0
            else:
                temp_sum += 1
                if temp_sum>max:
                    max = temp_sum
        return max


# Time:  O(n)  - why: one pass, constant work per element
# Space: O(1)  - why: two variables regardless of input size
# Note: `max` shadows Python's built-in max() - rename to `best`.
