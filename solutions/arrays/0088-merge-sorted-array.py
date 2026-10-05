# Problem: https://leetcode.com/problems/merge-sorted-array/
# Difficulty: Easy | Topic: Arrays
# Key idea: fill nums1 from the back - the empty slots are there, so nothing unread gets overwritten;
#           the bigger of nums1[i] / nums2[j] goes in slot k.


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = m - 1          # last real element of nums1
        j = n - 1          # last element of nums2
        k = m + n - 1      # next slot to fill, from the back

        while j >= 0:                          # until all of nums2 is placed
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1


# Time:  O(m + n)  - why: every element is written exactly once
# Space: O(1)      - why: merged inside nums1
