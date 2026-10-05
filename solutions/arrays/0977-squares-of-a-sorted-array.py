# Problem: https://leetcode.com/problems/squares-of-a-sorted-array/
# Difficulty: Easy | Topic: Arrays
# Key idea: the biggest square is always at one of the two ends - two pointers l, r,
#           put the bigger square at the back of res and move that pointer inward.


class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        res = [0] * n
        l, r = 0, n - 1
        k = n - 1                      # fill res from the back

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res[k] = nums[l] * nums[l]
                l += 1
            else:
                res[k] = nums[r] * nums[r]
                r -= 1
            k -= 1

        return res


# Time:  O(n)  - why: each element is placed once
# Space: O(n)  - why: res (O(1) extra if the output isn't counted)
# Notes: first attempt was square + bubble sort, O(n^2) -> Time Limit Exceeded at n = 10^4.
#        Can't write into nums from the back here: unlike 88 there are no empty slots, so unread values get overwritten.
