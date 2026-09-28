# Problem: https://leetcode.com/problems/richest-customer-wealth/
# Difficulty: Easy | Topic: Arrays
# Key idea: sum each customer's row, keep the largest sum seen so far.


class Solution(object):
    def maximumWealth(self, accounts):
        maxx=0
        for i in accounts:
            if sum(i)>maxx:
                maxx=sum(i)
        return maxx


# Time:  O(m*n)  - why: sum() touches every amount in every row (m customers x n banks)
# Space: O(1)    - why: only maxx
# Notes: starting at 0 is safe because the constraints guarantee every amount >= 1.
#        sum(i) runs twice when a row wins - store it in a variable once.
