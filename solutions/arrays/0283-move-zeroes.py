# Problem: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy | Topic: Arrays
# Key idea: write pointer k + swap - each non-zero is swapped into slot k, so zeros drift to the back
#           and the non-zeros keep their order.


class Solution(object):
    def moveZeroes(self, nums):
        k=0
        for i in range(len(nums)):
            if nums[i]==0:
                continue

            else:
                temp=nums[i]
                nums[i]=nums[k]
                nums[k]=temp

                k+=1
        return k


# Time:  O(n)  - why: one pass, O(1) swap per element
# Space: O(1)  - why: in place; only k and temp
# Notes: `return k` isn't needed (problem returns nothing). One-line swap: nums[i], nums[k] = nums[k], nums[i].
#        pop(i) inside the loop was the first attempt - it skips elements and costs O(n) per pop (O(n^2) total).
