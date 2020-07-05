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

Backtrack Template
------------------

```py
result = []
def backtrack(path = [], choices):
    if end condition:
        result.add(path[:]) # have to make a new copy
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
- Backtrack is a decision tree, updating the result is actually a preorder and/or postorder recursion
- Sometimes we don't need to explicitly maintain the choice list, we derive it using other parameters (e.g. index)
- Sometimes path can be a string instead of an array, and we use `path += 'choice'` and `path = path[:-1]` to make and remove choice