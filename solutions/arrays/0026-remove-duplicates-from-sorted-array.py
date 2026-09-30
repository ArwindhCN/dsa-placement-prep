# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Difficulty: Easy | Topic: Arrays
# Key idea: sorted, so duplicates sit together; k = index of last unique value,
#           and a bigger nums[i] is a new unique -> k += 1, then write it there.


class Solution(object):
    def removeDuplicates(self, nums):
        k=0
        for i in range(1,len(nums)):
            if nums[i]>nums[k]:
                k+=1
                nums[k]=nums[i]
        return k+1


# Time:  O(n)  - why: one pass over nums
# Space: O(1)  - why: in place; only k
