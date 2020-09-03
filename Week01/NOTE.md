Learning Notes Week 01
======================

Array
-----

> Array is a contiguous block of memory. It is usually used to represent sequences.

- Arrays are lists, lists are **mutable** sequences, tuples are **immutable** sequences
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

# Useful functions
map(lambda x: x * x, [1, 2, 3, 4, 5]) # [1, 4, 9, 16, 25]
map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]) # [5, 7, 9]
filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6]) # [1, 3, 5]
any((False, False, True)) # True
all((False, True, True)) # False
sum([1, 2, 3, 4, 5]) # 15
functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) # calculates ((((1+2)+3)+4)+5) = 15
```

```py
# total combinations of two numbers (pairs) in an array (brute force)
nums = [1,2,3,4]
n = len(nums)
for i in range(n-1):
    for j in range(i+1, n):
        print((nums[i], nums[j])) # [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# traverse backwards
nums = [1,2,3,4,5]
n = len(nums)
for i in range(n-1, -1, -1):
    print(nums[i]) # [5,4,3,2,1]

# Two Pointers
nums = [1,2,3,4,5,6,7,8,9]
n = len(nums)
i, j = 0, n-1
while i <= j:
    print(nums[i], nums[j]) # [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5)]
    while i <= j and nums[i+1] == nums[i]: i += 1 # skip duplicates
    while i <= j and nums[j-1] == nums[j]: j -= 1 # skip duplicates
    i += 1
    j -= 1

# Get sliding windows of size k in an array of nums
nums, k = [1,2,3,4,5,6], 3
n = len(nums)
windows = [nums[i:i+k] for i in range(n-k+1)]
print(windows) # [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]]

# Rotate array by k times (right shift)
nums, k = [1,2,3,4,5,6,7], 3
n = len(nums)
for i in range(n):
    res[(i+k)%n] = nums[i]
print(res) # [5,6,7,1,2,3,4]
```

Leetcode Problems
- [1. Two Sum](https://leetcode.com/problems/two-sum/)
- [66. Plus One](https://leetcode.com/problems/plus-one/)
- [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)
- [26. Remove Duplicates from Sorted Array ](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
- [189. Rotate Array](https://leetcode.com/problems/rotate-array/)
- [344. Reverse String](https://leetcode.com/problems/reverse-string/)
- [15. 3Sum](https://leetcode.com/problems/3sum/)
- [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

Linked Lists
------------

> A list implements an ordered collection of values, which may include repetitions.

Singly linked list: `2 -> 3 -> 5 -> 4 -> x`
- 2 is linked list head
- 4 is linked list tail
- 2's next is 3, 3's next is 5 and 5's next is 4, and 4's next is None
- L sometimes is used as a "dummy" head

Doubly linked list: `x <- 2 <-> 3 <-> 5 <-> 4 -> x`
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
    if not head:
        return head
    # do something before (pre-order)
    node = traverse(head.next)
    # do something after (post-order)
    return node
```

Leetcode Problems
- [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [92. Reverse Linked List II](https://leetcode.com/problems/reverse-linked-list-ii/)
- [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
- [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)
- [19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
- [148. Sort List](https://leetcode.com/problems/sort-list/)
- [25. Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)

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

Mono stack
```py
n = len(nums)
stack = []

prevGreaterElement = [-1] * n
for i in range(n): # push into stack
    while stack and stack[-1] <= nums[i]: # compare with stack top
        stack.pop() # pop out numbers smaller than me
    # now the top is the first element larger than me
    prevGreaterElement[i] = stack[-1] if stack else -1
    # push myself in stack for the next round
    stack.append(nums[i])
print(prevGreaterElement)

# Variation 1: push to stack backwards to get the rightMax
nextGreaterElement = [-1] * n
for i in range(n-1, -1, -1):
    while stack and stack[-1] <= nums[i]:
        stack.pop()
    nextGreaterElement[i] = stack[-1] if stack else -1
    stack.append(nums[i])
print(nextGreaterElement)

# Variation 2: find min rather than max (change the compare part)
prevSmallerElement = [-1] * n
for i in range(n):
    while stack and stack[-1] > nums[i]:
        stack.pop()
    prevSmallerElement[i] = stack[-1] if stack else -1
    stack.append(nums[i])
print(prevSmallerElement)

# Variation 3: push index to stack instead of numbers
prevGreaterIndex = [-1] * n
for i in range(n):
    while stack and nums[stack[-1]] <= nums[i]:
        stack.pop()
    prevGreaterIndex[i] = stack[-1] if stack else -1
    stack.append(i)
print(prevGreaterIndex)

# Mono Increasing Stack
for i in range(n):
    while stack and nums[stack[-1]] > nums[i]:
        curr = stack.pop()
        if not stack:
            ...
        left, right = stack[-1], i
        print(left, curr, right)
    stack.append(i)

# Mono Decreasing Stack
for i in range(n):
    while stack and nums[stack[-1]] < nums[i]:
        curr = stack.pop()
        if not stack:
            ...
        left, right = stack[-1], i
        print(left, curr, right)
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
- [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)
- [155. Min Stack](https://leetcode.com/problems/min-stack/)
- [496. Next Greater Element I](https://leetcode.com/problems/next-greater-element-i/)
- [503. Next Greater Element II](https://leetcode.com/problems/next-greater-element-ii/)
- [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)
- [239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

Skip List
---------

> The skip list is a probabilisitc data structure that is built upon the general idea of a linked list. The skip list uses probability to build subsequent layers of linked lists upon an original linked list. Each additional layer of links contains fewer elements, but no new elements.

```
   1                               10
 o---> o---------------------------------------------------------> o    Top level
   1           3              2                    5
 o---> o---------------> o---------> o---------------------------> o    Level 3
   1        2        1        2              3              2
 o---> o---------> o---> o---------> o---------------> o---------> o    Level 2
   1     1     1     1     1     1     1     1     1     1     1
 o---> o---> o---> o---> o---> o---> o---> o---> o---> o---> o---> o    Bottom level
Head  1st   2nd   3rd   4th   5th   6th   7th   8th   9th   10th  NIL
      Node  Node  Node  Node  Node  Node  Node  Node  Node  Node
```

| Operation  | Time Complexity |
| ---------- | :-------------: |
| Access     | O(log n)        |
| Search     | O(log n)        |
| Insertion  | O(log n)        |
| Deletion   | O(log n)        |

```py
def search(key):
    p = topLeftNode()
    while p.below:            # Scan down
        p = p.below
        while key >= p.next:  # Scan forward
            p = p.next
    return p

def insert(key):
    p, q = search(key), None
    i = 1
    while CoinFlip() != 'Tails':
        i = i + 1                   # Height of tower for new element
        if i >= h:
            h = h + 1
            createNewLevel()        # Creates new linked list level
        while p.above is None:
            p = p.prev              # Scan backwards until you can go up
        p = p.above
        q = insertAfter(key, p)     # Insert our key after position p
    n = n + 1
    return q

def delete(key):
    # Search for all positions p_0, ..., p_i where key exists
    if none are found:
        return
    # Delete all positions p_0, ..., p_i
    # Remove all empty layers of skip list
```