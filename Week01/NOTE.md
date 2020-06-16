Learning Notes Week 01
======================

Array
-----

Basic Concepts
- Arrays are lists, lists are mutable sequences, tuples are immutable sequences
- list is dynamically-resized, there is no upper bound
- Values can be deleted and inserted at arbitrary locations

Time Complexity of array operations
- Retrieving  O(1)
- Updating    O(1)
- Insertion   O(n)
- Deletion    O(n-i)

List Operations
```python
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

Common Sequence Operations (list, tuple, range, etc.)
```python
x in s          # True if an item of s is equal to x, else False
x not in s      # False if an item of s is equal to x, else True
s + t           # the concatenation of s and t
s * n or n * s  # equivalent to adding s to itself n times
s[i]            # ith item of s, origin 0
s[i:j]          # slice of s from i to j
s[i:j:k]        # slice of s from i to j with step k
len(s)          # length of s
min(s)          # smallest item of s
max(s)          # largest item of s
reversed(s)     # return a reverse iterator
sorted(s)       # return a new sorted list from the items in iterable
```

String Operations
```python
string.digits      # The string '0123456789'
string.hexdigits   # The string '0123456789abcdefABCDEF'
string.octdigits   # The string '01234567'

ord(c)             # Unicode code representation of the char
ord(c) - ord('a')  # Position of the char in 26 letters
chr(i)             # String representation of the char unicode code

s.strip([chars])
s.startswith(prefix)
s.endswith(prefix)
s.slipt(delimiter)
s.lower()
s.upper()
'Hello {name}'.format(name='World')
```

Coding Techniques
```python
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

# Rotate array by k times (right shift)
nums = [1,2,3,4,5,6,7]
for i in range(len(nums)):
    res[(i+k) % len(nums)] = nums[i]
res  # [5,6,7,1,2,3,4]

# Useful functions
functools.reduce(func, iter, [initial_value])
itertools.groupby(iterable[, key])
```

Linked Lists
------------

A list implements an ordered collection of values, which may include repetitions.

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

Coding Techniques
```python
# Linked list recursion (think backwards)
def reverseList(self, head: ListNode) -> ListNode:
    if not head or not head.next: return head # end condition
    p = self.reverseList(head.next) # rest of the nodes are already reversed
    head.next.next = head # start to reverse the first two nodes
    head.next = None
    return p # return head
```

Stacks and Queues
-----------------

- Stack: First In Last Out (FILO)
- Queue: First In First Out (FIFO)

Stack Libraries (Stack uses the build-in list-type)
```python
stack.append(e)  # push
stack[-1]        # peek
stack.pop()      # pop
len(stack)       # len
```

Queue Libraries (Queue uses the collection.deque class)
```python
queue.append(e)  # push
queue[0]         # peek front
queue[-1]        # peek back
queue.popleft()  # pop
```