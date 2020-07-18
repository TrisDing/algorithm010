Learning Notes Week 01
======================

Array
-----

> Array is a contiguous block of memory. It is usually used to represent sequences.

- Arrays are lists, lists are mutable sequences, tuples are immutable sequences
- Lists are dynamically-resized, there is no upper bound
- Values can be deleted and inserted at arbitrary locations

| Operation  | Time Complexity |
| ---------- | :-------------: |
| Access     | O(1)            |
| Search     | O(1)            |
| Insertion  | O(n)            |
| Deletion   | O(n)            |

Common Sequence Operations (list, tuple, range, etc.)
```py
x in s             # True if an item of s is equal to x, else False
x not in s         # False if an item of s is equal to x, else True
s + t              # the concatenation of s and t
s * n or n * s     # equivalent to adding s to itself n times
s[i]               # ith item of s, origin 0
s[i:j]             # slice of s from i to j
s[i:j:k]           # slice of s from i to j with step k
len(s)             # length of s
min(s)             # smallest item of s
max(s)             # largest item of s
reversed(s)        # return a reverse iterator
sorted(s)          # return a new sorted list from the items in iterable
```

List Operations
```py
a.append(x)        # appends x to the end of the sequence (same as s[len(s):len(s)] = [x])
a.extend(iterable) # extends s with the contents of t (same as s += t)
a.insert(i, x)     # inserts x into s at the index given by i (same as s[i:i] = [x])
a.remove(x)        # remove the first item from s where s[i] is equal to x
a.pop([i])         # retrieves the item at i and also removes it from s
a.clear()          # removes all items from s (same as del s[:])
a.count(x)         # total number of occurrences of x in s
a.reverse()        # reverses the items of s in place
a.copy()           # creates a shallow copy of s (same as s[:])
a.index(x[, start[, end]]) # index of the first occurrence of x in s
a.sort(key=None, reverse=False) # Sort the items of the list in place
```

String Operations
```py
s.strip([chars])     # return a copy of the string with the leading and trailing characters removed.
s.startswith(prefix) # return True if string starts with the prefix, False otherwise.
s.endswith(prefix)   # return True if string starts with the prefix, False otherwise.
s.slipt(delimiter)   # return a list of the words of the string s.
s.lower()            # return a copy of the string with all the lowercase characters
s.upper()            # return a copy of the string with all the uppercase characters
ord(c)               # the unicode code representation of the char
ord(c) - ord('a')    # the position of the char in 26 letters
chr(i)               # string representation of the char unicode code
```

String Constants
```py
import string

string.digits          # the string '0123456789'
string.hexdigits       # the string '0123456789abcdefABCDEF'
string.octdigits       # the string '01234567'
string.ascii_lowercase # the uppercase letters 'abcdefghijklmnopqrstuvwxyz'
string.ascii_letters   # The lowercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string.letters         # The concatenation of the ascii_lowercase and ascii_uppercase
```

Coding Techniques
```py
# List comprehension
vec = [-4, -2, 0, 2, 4]
[x*2 for x in vec] # [-8, -4, 0, 4, 8]
[x for x in vec if x >= 0] # [0, 2, 4]
[abs(x) for x in vec] # [4, 2, 0, 2, 4]

# Create a list of 2-tuples (number, square)
[(x, x**2) for x in range(4)] # [(0, 0), (1, 1), (2, 4), (3, 9)]

# Flatten a 2-D list
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]

# String formatter
'Hello {name}'.format(name='World')

# Get sliding windows of size k in an array of nums
nums, k = [1,2,3,4,5,6], 3
n = len(nums)
windows = [nums[i:i+k] for i in range(n-k+1)]
print(windows) # [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]

# Rotate array by k times (right shift)
nums = [1,2,3,4,5,6,7]
n = len(nums)
for i in range(n):
    res[(i + k) % n] = nums[i]
print(res)  # [5,6,7,1,2,3,4]

# Useful functions
map(lambda x: x * x, [1, 2, 3, 4, 5]) # [1, 4, 9, 16, 25]
map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]) # [5, 7, 9]
filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6]) # [1, 3, 5]
any((False, False, True)) # True
all((False, True, True)) # False
sum([1, 2, 3, 4, 5]) # 15
functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) # calculates ((((1+2)+3)+4)+5) = 15
```

Leetcode Problems
- [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [66. Plus One](https://leetcode.com/problems/plus-one/)
- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [26. Remove Duplicates from Sorted Array ](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
- [167. Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [15. 3Sum](https://leetcode.com/problems/3sum/)
- [344. Reverse String](https://leetcode.com/problems/reverse-string/)
- [189. Rotate Array](https://leetcode.com/problems/rotate-array/)
- [704. Binary Search](https://leetcode.com/problems/binary-search/)
- [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

Linked Lists
------------

> A list implements an ordered collection of values, which may include repetitions.

Singly linked list: `L -> 2 -> 3 -> 5 -> 4 -> EOL`
- 2 is linked list head
- 4 is linked list tail
- 2's next is 3, 3's next is 5 and 5's next is 4, and 4's next is None
- L sometimes is used as a "dummy" head

Doubly linked list: `L -> x <- 2 <-> 3 <-> 5 <-> 4 -> x`
- 2's prev is None, 2's next is 3
- 3's prev is 2   , 3's next is 5
- 4's prev is 3   , 5's next is 4
- 4's prev is 5   , 4's next is None

| Operation  | Time Complexity |
| ---------- | :-------------: |
| Access     | O(n)            |
| Search     | O(n)            |
| Insertion  | O(1)            |
| Deletion   | O(1)            |

```py
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
```

Two Pointers Template
```py
prev, curr = None, head
while curr:
    # do something with prev and curr
    if prev is None:
        # when curr is head
    else:
        # when curr is not head
    # move prev and curr
    prev = curr
    curr = curr.next

return prev
```

Dummy Head (Sentry) Template
```py
dummy = ListNode(None)
dummy.next = head

prev, curr = dummy, head
while curr:
    # prev will never be None
    prev.next = curr.next
    # move prev and curr
    prev = curr
    curr = curr.next

return dummy.next
```

Fast Slow Template
```py
fast = slow = head
while fast and fast.next:
    # fast move 2 steps
    fast = fast.next.next
    # slow move 1 step
    slow = slow.next

# when num of the list is odd, slow is the mid
# when num of the list is even, slow is the first node after mid
return slow
```

Linked List Recursion
```py
def traverse(head):
    # base case
    if head.next:
        return head
    # do something before (pre-order)
    node = traverse(head.next)
    # do something after (post-order)
    return node
```

Leetcode Problems
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
- [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
- [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
- [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
- [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
- [148. Sort List](https://leetcode.com/problems/sort-list/)
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)

Stacks and Queues
-----------------

> Stacks support first-in, last-out (FILO) for inserts and deletes, whereas queues are first-in first-out (FIFO)

| Operation  | Time Complexity |
| ---------- | :-------------: |
| Access     | O(n)            |
| Search     | O(n)            |
| Insertion  | O(1)            |
| Deletion   | O(1)            |

Stack Operations
```py
stack = []       # create a stack (nothing but a list)
stack.append(x)  # push
stack.pop()      # pop
stack[-1]        # peek (top of the stack)
```

Queue Operations
```py
from collections import deque

queue = deque()      # create a double ended queue
queue.append(x)      # add x to the right side of the deque
queue.appendleft(x)  # add x to the left side of the deque
queue.pop()          # remove and return an element from the right side of the deque
queue.popleft()      # remove and return an element from the left side of the deque
queue[0]             # peek left side of the deque
queue[-1]            # peek right side of the deque
```

Sliding Window Template
```py
from collections import Counter

def slidingWindow(s, t):
    window = Counter()
    target = Counter(t)

    len_s, len_t = len(s), len(t)
    left = right = 0
    valid = 0

    while right < len_s:
        # c is the element to be inserted into the window
        c = s[right]
        # expand the current window
        right += 1
        # If c is our target, we are 1 step closer to the answer
        if c in target:
            window[c] += 1
            if window[c] == target[c]:
                valid += 1

        while # when we found a valid window
            if valid == len(target):
                # check the answer or update the result

            # d is the element to be removed from the window
            d = s[left]
            # shrink the current window
            left += 1
            # if d is our target, shrinking might cause the window to be invalid
            if d in target:
                if window[d] == target[d]:
                    valid -= 1
                window[d] -= 1
```

Mono stack
```py
n = len(nums)
stack = []
leftMax = [-1] * n
for i in range(n): # push into stack
    while stack and stack[-1] <= nums[i]: # compare with stack top
        # pop out numbers smaller than me
        stack.pop()
        # now the top is the first element bigger than me
        leftMax[i] = stack[-1] if stack else -1
    # push myself in stack for the next round
    stack.append(nums[i])
return leftMax

# Variation 1: push to stack backwards to get the rightMax
rightMax = [-1] * n
for i in range(n-1, -1, -1):
    ...

# Variation 2: find min rather than max
leftMin = [-1] * n
for i in range(n):
    while stack and nums[i] <= stack[-1]:
        ...

# Variation 3: push index to stack instead of numbers
while stack and nums[stack[-1]] <= nums[i]:
    stack.pop()
...
stack.append(i)

# Variation 4: find leftMax and rightMax in one pass
for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        currIndex = stack.pop()
        if not stack:
            break
        leftMax = stack[-1]
        rightMax = i
        print(leftMax, currIndex, rightMax)
    stack.append(i)
```

Mono Queue
```py
class monoQueue:
    def __init__(self):
        self.queue = deque()

    def push(self, x):
        while self.queue and self.queue[-1] < x:
            self.queue.pop()
        self.queue.append(x)

    def pop(self, x):
        if self.queue and self.queue[0] == x:
            self.queue.popleft()

    def max(self):
        return self.queue[0]
```

Leetcode Problems
- [20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [155. Min Stack](https://leetcode.com/problems/min-stack/)
- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)
- [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)
- [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)
- [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [42. Trapping Rain Water](https://leetcode.com/problems/next-greater-element-ii/)
-

Skip List
---------

[TODO]