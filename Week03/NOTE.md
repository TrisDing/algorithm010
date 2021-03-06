Learning Notes Week 03
======================

Recursion Template
------------------

```py
def recursion(level, param1, param2, ...):
    # recursion terminator
    if level > MAX_LEVEL:
        process_result
        return

    # process logic in current level
    process(level, data, ...)

    # drill down
    recursion(level + 1, p1, ...)

    # reverse the current level status if needed
```

Divide & Conquer Template
-------------------------

```py
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        process_result
        return

    # prepare data (key is to how to split the problem)
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)

    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    ...

    # process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)

    # revert the current level states
```

- Sometimes we need to return multiple results (tuple)
- Sometimes we need global variables to easily update the final result

Leetcode Problems
- [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)
- [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)
- [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [169. Majority Element](https://leetcode.com/problems/majority-element/)

Backtrack Template
------------------

```py
result = []
def backtrack(path = [], choices):
    if end condition:
        result.add(path[:]) # param pass by reference
        return

    for choice in choices:
        # get rid of the illegal choices
        if exclusive condition:
            continue

        path.append(choice) # Make the choice
        backtrack(path, choices) # enter the next decision tree
        path.pop() # Remove the choice (since it's already made)
```

- Time complexity for backtrack algorithm is at least O(N!)
- Backtrack is a decision tree, updating the result is actually a preorder and/or postorder recursion (DFS)
- Sometimes we don't need to explicitly maintain the choice list, we derive it using other parameters (e.g. index)
- Sometimes path can be a string instead of an array, and we use `path += 'choice'` and `path = path[:-1]` to make and remove choice

Leetcode Problems
- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [78. Subsets](https://leetcode.com/problems/subsets/)
- [46. Permutations](https://leetcode.com/problems/permutations/)
- [47. Permutations II](https://leetcode.com/problems/permutations-ii/)
- [77. Combinations](https://leetcode.com/problems/combinations/)
- [17. Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)
- [51. N-Queens](https://leetcode.com/problems/n-queens/)
- [37. Sudoku Solver](https://leetcode.com/problems/sudoku-solver/)