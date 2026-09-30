# Problem: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
# Difficulty: Easy | Topic: Arrays
# Key idea: count digits by repeatedly removing the last one (n // 10) until the number is 0.


class Solution(object):
    def findNumbers(self, nums):
        ans=0
        for i in nums:
            count = 0

            remain=1
            while(i>0):
                if (i//10 !=0):
                    count+=1
                    i = i//10
                else:
                    count+=1
                    i = i//10
                    if(count%2==0):
                        ans+=1

        return ans


# Time:  O(n * d)  - why: each number loses one digit per loop pass; d <= 6 here, so effectively O(n)
# Space: O(1)      - why: a few counters
# Notes: both branches do count += 1 and i //= 10, so the if/else isn't needed -
#        loop `while i > 0`, then check count % 2 once after the loop. `remain` is unused.
