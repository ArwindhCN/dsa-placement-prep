# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Difficulty: Easy | Topic: Sliding Window (NeetCode 150)
# Key idea: track the cheapest price so far; selling today earns price - cheapest.


class Solution(object):
    def maxProfit(self, prices):
        cheapest = prices[0]   # lowest price seen so far
        best = 0               # best profit so far

        for price in prices:
            if price < cheapest:
                cheapest = price           # new buying opportunity
            else:
                best = max(best, price - cheapest)   # profit if we sell today

        return best


# Time:  O(n)  - why: one pass over prices, O(1) work per day
# Space: O(1)  - why: only two variables
