# Python DSA Toolkit

What each tool costs and why. Add to this whenever a problem teaches me something new.

## Why some lookups are O(1) and others O(n)

- **list `x in nums`** → O(n). Python checks elements one by one until it finds a match.
- **set / dict `x in seen`** → O(1) on average. Python hashes `x` into a number, which points almost directly at the slot where `x` would be. There's no scanning.
- Only **hashable** (immutable) values can go in a set or be dict keys: int, str, tuple. Lists and dicts can't. Convert first, e.g. `tuple(sorted(word))` or `tuple(count)`.

Rule of thumb: if I'm doing `in` on a list inside a loop, that's O(n²). Switch to a set.

## list

```python
nums = [3, 1, 2]
nums.append(4)        # O(1)   add to end
nums.pop()            # O(1)   remove from end
nums.pop(0)           # O(n)   remove from front: shifts every element left -> use deque
nums.insert(0, 9)     # O(n)   same shifting problem
nums[i]               # O(1)   index access
x in nums             # O(n)   linear scan
nums[::-1]            # O(n)   reversed copy
nums[a:b]             # O(b-a) slicing COPIES
len(nums)             # O(1)
[0] * n               # list of n zeros
[[0] * cols for _ in range(rows)]   # 2-D grid. NOT [[0]*cols]*rows (same row object repeated)
```

Loop patterns:
```python
for i, x in enumerate(nums):   # index + value
for a, b in zip(xs, ys):       # walk two lists together
for i in range(len(nums) - 1, -1, -1):   # backwards
```

## dict

```python
d = {}
d[key] = val            # O(1) insert/update
d.get(key, 0)           # O(1) read with default, no KeyError
key in d                # O(1)
d.pop(key)              # O(1)
for k, v in d.items():  # iterate pairs
```

Counting without Counter: `d[x] = d.get(x, 0) + 1`

## set

```python
s = set()
s.add(x)        # O(1)
s.remove(x)     # O(1), KeyError if missing
s.discard(x)    # O(1), no error if missing
x in s          # O(1)
a & b           # intersection
a | b           # union
a - b           # difference
len(set(nums)) != len(nums)   # quick "has duplicates" check, O(n)
```

## collections.Counter

```python
from collections import Counter
c = Counter("banana")     # {'a': 3, 'n': 2, 'b': 1}, built in O(n)
c['z']                    # 0: missing keys return 0, no KeyError
c.most_common(2)          # [('a', 3), ('n', 2)]
Counter(s) == Counter(t)  # anagram check in O(n)
```

## collections.defaultdict

```python
from collections import defaultdict
groups = defaultdict(list)
groups[key].append(x)     # missing key automatically starts as []
count = defaultdict(int)  # missing key starts as 0
```

Use this when grouping (e.g. Group Anagrams) so I don't need `if key not in d: d[key] = []`.

## collections.deque

```python
from collections import deque
q = deque([1, 2, 3])
q.append(x)       # O(1) right
q.appendleft(x)   # O(1) left
q.pop()           # O(1) right
q.popleft()       # O(1) left: this is why BFS uses deque, not list.pop(0)
```

A deque is a doubly-linked chain of blocks, so both ends are O(1). Indexing into the middle is O(n).

## heapq (min-heap)

```python
import heapq
h = []
heapq.heappush(h, x)      # O(log n)
heapq.heappop(h)          # O(log n): removes and returns the smallest
h[0]                      # O(1): peek at the smallest
heapq.heapify(nums)       # O(n): turns a list into a heap in place
heapq.nlargest(k, nums)   # top k
```

- Python only has a **min**-heap. For a max-heap, push `-x` and negate on the way out.
- Tuples compare element by element: `heappush(h, (priority, item))`.
- "Top k" / "kth largest" → keep a min-heap of size k. That's O(n log k).

## Sorting

```python
nums.sort()                           # in place, returns None (!)
new = sorted(nums)                    # returns a new list
sorted(nums, reverse=True)
sorted(words, key=len)                # sort by a computed value
sorted(pairs, key=lambda p: p[1])     # sort by second element
sorted(pairs, key=lambda p: (-p[1], p[0]))   # desc by [1], then asc by [0]
```

Cost: O(n log n) time. Python uses Timsort, which is stable: equal elements keep their original order. `x = nums.sort()` sets `x` to `None`, a classic bug.

## Strings

Strings are **immutable**. `s += c` in a loop builds a new string each time, which can make the loop O(n²). Collect parts in a list and `"".join(parts)` once at the end.

```python
s.lower(), s.upper()
s.isalnum(), s.isalpha(), s.isdigit()
s.strip()                 # trim whitespace both ends
s.split()                 # split on any whitespace
s.split(",")
" ".join(words)
s[::-1]                   # reversed
s.find(sub)               # index or -1
s.startswith(p), s.endswith(p)
ord('a'), chr(97)         # char <-> code; ord(c) - ord('a') gives 0..25
s.count(sub)
```

Fixed alphabet trick: `count = [0] * 26` then `count[ord(c) - ord('a')] += 1`. That's O(1) space, since the size is fixed at 26.

## Handy built-ins

```python
float('inf'), float('-inf')   # starting values for min/max tracking
max(a, b), min(nums)
sum(nums)
divmod(a, b)                  # (quotient, remainder)
a // b                        # floor division (rounds toward -inf for negatives!)
abs(x)
any(...), all(...)
```

## LeetCode gotchas I've hit

- **`return`, not `print`.** LeetCode calls my method and checks what it *returns*. A `print` shows up in stdout but the answer comes back as `None`.
- **`self`.** Methods live on the `Solution` class. LeetCode runs `Solution().twoSum(nums, target)`, and Python passes that object in as `self` automatically. To call my own helper method, use `self.helper(...)`.
- **Indentation.** `else` must line up exactly with its `if`. Everything inside a block is indented one level (4 spaces) further than the line that opens it.
- **Don't name variables after built-ins** (`max`, `min`, `sum`, `next`, `list`, `str`, `len`). It hides the function: a later `max(a, b)` crashes with `'int' object is not callable`. Use `best`, `total`, `largest`.
- **Local test prints nothing?** `sol.method(x)` returns the answer and throws it away. To see it: `print(sol.method(x))`.
- **Class-level variables aren't visible inside methods.** `total = 0` in the class body, then `total += x` in a method, gives `UnboundLocalError`. Anything that belongs to one call (totals, counters, results) goes *inside* the method.
- **Starting value for max tracking:** `nums[0]` or `float('-inf')`, never `0` (fails when all numbers are negative). `0` is fine only if the constraints guarantee positives. Always read the constraints.
- **Loop over what you need:** values → `for x in nums`; index → `range(len(nums))`; both → `enumerate(nums)`.
- **Don't slice just to skip an element.** `nums[1:]` copies the list (O(n) space). Use `range(1, len(nums))`.
- **"Best so far" must be checked where the streak can end, including at the end of the array.** In 485, updating the max only when a `0` appears missed a run of 1s at the very end. Fix: update on every step, or once more after the loop.
- **`%` vs `//` for digits:** `n % 10` *gives* the last digit; `n // 10` *removes* it. Count digits with `while n > 0: count += 1; n //= 10`. Stop when the **number** is 0, not when the last digit is 0 (that breaks on 10, 100).
- **Time Limit Exceeded on a tiny input = infinite loop.** Check that something inside the `while` changes the loop condition.
- **Short code isn't always fast.** `nums + nums`, `sum(row)`, and slicing all loop underneath, O(n) each. Don't call `sum()` twice on the same row; store it.
- **Never delete from a list while looping over its indexes.** `range(len(nums))` is computed once, so after a `pop`/`remove` the list is shorter and later `i` values run past the end → `IndexError`. Overwrite in place with a write pointer instead (27).
- **Write pointer: decide what `k` means and stick to it.** "Next empty slot" → write, then `k += 1`, return `k` (27). "Last kept element" → `k += 1`, then write, return `k + 1` (26). Mixing the two gives off-by-one bugs.
- **`()` calls, `[]` indexes.** `nums.append[0]` → `TypeError: 'builtin_function_or_method' object has no attribute '__getitem__'`. It's `nums.append(0)`.
- **`nums = new` vs `nums[:] = new`.** `nums = new` only moves my local name; the caller's list is unchanged. `nums[:] = new` copies values into the original list. But building `new` is still O(n) extra space, so it's not truly in place (283).
- **Negative indexes don't crash in Python.** `nums[-1]` silently reads the *last* element. If a pointer can go below 0, guard it: `if i >= 0 and nums[i] ...` (88).
- **`and` short-circuits.** In `i >= 0 and nums[i] > x`, if `i >= 0` is False Python never evaluates `nums[i]`. Put the safety check first.
- **In-place merge/insert: if the front is full, fill from the back** where the free space is, so nothing unread gets overwritten (88).
- **Read n in the constraints before choosing an approach.** n ≈ 10^4 or more → O(n²) is ~50M+ steps, too slow in Python (TLE). Need O(n log n) or O(n). (977: bubble sort timed out.)
- **"Fill from the back" in place only works if the back is free** (88). If every slot holds unread data, use a separate result array (977).
- **Two pointers from both ends: loop `while l <= r`** when the middle element still needs handling; `l < r` skips it.
- **Two sequences of different lengths:** loop `range(max(len1, len2))` and guard each access with `if i < len1:` (1768).
- **Build strings with a list + `"".join()`,** not `s += c` in a loop. Strings are immutable, so each `+=` copies the whole string (can be O(n²)).
- **`s.split()` vs `s.split(" ")`.** No argument splits on any run of whitespace and ignores leading/trailing spaces. `split(" ")` splits on every single space and leaves empty strings `''` for repeated/trailing spaces (58).
- **Swap in one line:** `a, b = b, a`. No temp variable needed.
- **LeetCode's "Beats X%" is noise** at small runtimes. Complexity is what matters.
