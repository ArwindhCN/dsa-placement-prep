# Patterns

One line per problem: the key idea that unlocks it. Reread this before interviews.

Format: `Problem (#) -> key idea`

## Arrays

- Running Sum of 1d Array (1480) -> keep a running total; each answer = previous total + current number
- Concatenation of Array (1929) -> ans[i] = ans[i + n] = nums[i] (or nums + nums)
- Richest Customer Wealth (1672) -> sum each row, track the max seen so far
- Max Consecutive Ones (485) -> count the current streak, reset on 0, update max on every 1 (or once more after the loop)
- Find Numbers with Even Number of Digits (1295) -> count digits with `while n > 0: n //= 10`, then check count % 2
- Remove Element (27) -> write pointer k: copy every nums[i] != val to nums[k], k += 1; return k
- Remove Duplicates from Sorted Array (26) -> k = last unique index; if nums[i] > nums[k]: k += 1, nums[k] = nums[i]; return k + 1
- Move Zeroes (283) -> write pointer + swap: if nums[i] != 0, swap nums[i] and nums[k], k += 1
- Merge Sorted Array (88) -> fill nums1 from the back with 3 pointers; bigger of nums1[i] / nums2[j] goes to nums1[k]; loop while j >= 0
- Squares of a Sorted Array (977) -> biggest square is at an end; two pointers l, r, fill res from the back with the bigger square

## Strings

- Merge Strings Alternately (1768) -> loop to the longer length, append each char only if i < len; "".join() at the end
- Length of Last Word (58) -> len(s.split()[-1]); O(1) space: scan from the end, skip spaces, count letters
- Reverse String (344) -> two pointers l, r: swap and move inward while l < r
- Check if the Sentence Is Pangram (1832) -> every letter a-z must appear: len(set(sentence)) == 26

## Hashing

## Sliding Window

- Best Time to Buy and Sell Stock (121) -> track the cheapest price so far; profit if selling today = price - cheapest
