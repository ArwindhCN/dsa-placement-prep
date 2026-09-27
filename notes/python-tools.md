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
