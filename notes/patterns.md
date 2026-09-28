# Patterns

One line per problem: the key idea that unlocks it. Reread this before interviews.

Format: `Problem (#) -> key idea`

## Arrays

- Running Sum of 1d Array (1480) -> keep a running total; each answer = previous total + current number
- Concatenation of Array (1929) -> ans[i] = ans[i + n] = nums[i] (or nums + nums)
- Richest Customer Wealth (1672) -> sum each row, track the max seen so far
- Max Consecutive Ones (485) -> count the current streak, reset on 0, update max on every 1 (or once more after the loop)

## Strings

## Hashing

## Sliding Window

- Best Time to Buy and Sell Stock (121) -> track the cheapest price so far; profit if selling today = price - cheapest
