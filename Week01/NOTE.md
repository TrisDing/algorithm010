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
a.append(x)
a.extend(iterable)
a.insert(i, x)
a.remove(x)
a.pop([i])
a.clear()
a.count(x)
a.reverse()
a.copy()
a.index(x[, start[, end]])
a.sort(key=None, reverse=False)
```

Common Sequence Operations
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

List Comprehensions
```python
vec = [-4, -2, 0, 2, 4]

[x*2 for x in vec] # [-8, -4, 0, 4, 8]

[x for x in vec if x >= 0] # [0, 2, 4]

[abs(x) for x in vec] # [4, 2, 0, 2, 4]

[(x, x**2) for x in range(6)] # create a list of 2-tuples (number, square)

vec = [[1,2,3], [4,5,6], [7,8,9]]

[num for elem in vec for num in elem] # flatten a list
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
