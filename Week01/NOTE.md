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
a.sort(key=None, reverse=False)
```

String Operations
```py
string.digits        # the string '0123456789'
string.hexdigits     # the string '0123456789abcdefABCDEF'
string.octdigits     # the string '01234567'
ord(c)               # the unicode code representation of the char
ord(c) - ord('a')    # the position of the char in 26 letters
chr(i)               # string representation of the char unicode code
s.strip([chars])     # return a copy of the string with the leading and trailing characters removed.
s.startswith(prefix) # return True if string starts with the prefix, False otherwise.
s.endswith(prefix)   # return True if string starts with the prefix, False otherwise.
s.slipt(delimiter)   # return a list of the words of the string s.
s.lower()            # return a copy of the string with all the lowercase characters
s.upper()            # return a copy of the string with all the uppercase characters
'Hello {name}'.format(name='World')
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
functools.reduce(func, iter, [initial_value])
itertools.groupby(iterable[, key])
```

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

LinkedList Node
```py
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
```

Coding Techniques
```py
# Linked List iteration framework (Double Pointers)
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

def reverseList(self, head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        cnext = curr.next
        if prev is None:
            curr.next = None
        else:
            curr.next = prev
        prev = curr
        curr = cnext
    return prev

# Linked List recursion framework (Think Backwards)
def reverseList(self, head: ListNode) -> ListNode:
    if not head or not head.next:   # end condition
        return head
    p = self.reverseList(head.next) # rest of the nodes are already reversed
    head.next.next = head           # start to reverse the first two nodes
    head.next = None
    return p                        # return head
```

Stacks and Queues
-----------------

> Stacks support first-in, last-out (FILO) for inserts and deletes, whereas queues are first-in first-out (FIFO)

| Operation  | Time Complexity |
| ---------- | :-------------: |
| Access     | O(n)            |
| Search     | O(n)            |
| Insertion  | O(1)            |
| Deletion   | O(1)            |

Stack Operations (List data types represent the implementation of stacks)
```py
stack.append(x)  # push
stack.pop()      # pop
stack[-1]        # peek
```

Queue Operations (collection.deque - class represent the implementation of double ended queues)
```py
q.append(x)      # add x to the right side of the deque
q.appendleft(x)  # add x to the left side of the deque
q.pop()          # remove and return an element from the right side of the deque
q.popleft()      # remove and return an element from the left side of the deque
q[0]             # peek left side of the deque
q[-1]            # peek right side of the deque
```

Skip List
---------

[TODO]