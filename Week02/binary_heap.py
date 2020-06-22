"""
My Implementation of Max Heap
"""
class BinaryHeap:
    def __init__(self, capacity = 10):
        self.heapsize = 0
        self.heap = [-1] * capacity

    def is_empty(self):
        return self.heapsize == 0

    def is_full(self):
        return self.heapsize == len(self.heap)

    def insert(self, elem):
        """
        Inserts new element in to heap
        Time Complexity: O(log N)
        """
        if self.is_full():
            raise Exception("Heap is full, No space to insert new element")
        # 1. append new element to the end of heap.
        self.heap[self.heapsize] = elem
        # 2. increase the heapsize by 1.
        self.heapsize += 1
        # 3. bubble up the larger child until hitting root.
        endpos = self.heapsize - 1
        self._siftup(endpos)

    def _siftup(self, i):
        """
        Maintains the heap property while inserting an element at position i
        """
        while i > 0:
            newitem = self.heap[i]
            parentpos = (i - 1) >> 1
            parent = self.heap[parentpos]
            if newitem > parent:
                # newitem is bigger, move it up.
                newitem, parent = parent, newitem
                # process the next element (parentpos).
                i = parentpos
                continue
            # parent is bigger, we are done.
            break

    def delete(self, i):
        """
        Remove an element at position i from the heap
        Time Complexity: O(log N)
        """
        if self.is_empty():
            raise Exception("Heap is empty, No element to delete")
        delitem = self.heap[i]
        endpos = self.heapsize - 1
        # 1. replace the element at position i with the last element.
        self.heap[i] = self.heap[endpos]
        # 2. decrease heapsize by 1 (so the last item is removed).
        self.heapsize -= 1
         # 3. move down the new element until the end of heap.
        self._siftdown(i)
        return delitem

    def _siftdown(self, i):
        """
        Maintains the heap property while deleting an element.
        """
        leftpos = 2 * i + 1
        while leftpos < self.heapsize:
            delitem = self.heap[i]
            # select the bigger one from leftchild and rightchild.
            childpos = leftpos
            rightpos = leftpos + 1
            if rightpos < self.heapsize and self.heap[rightpos] > self.heap[leftpos]:
                childpos = rightpos
            # delitem is bigger than child, we are done.
            if delitem >= self.heap[childpos]:
                break
            # delitem is smaller, move it down.
            self.heap[i], self.heap[childpos] = self.heap[childpos], self.heap[i]
            # process the next element (childpos).
            i = childpos
            leftpos = 2 * i + 1

    def find_max(self):
        """
        Return the Max Element (Heap Top)
        Time Complexity: O(1)
        """
        if self.is_empty():
            raise Exception("Heap is empty.")
        return self.heap[0]

    def printheap(self):
        n = self.heapsize
        depth = n // 2
        line = ''
        for i in range(depth + 1):
            j = 0
            while j < 2**i and (j + 2**i - 1) < n:
                padding = ' ' * (2**(depth - i) - 1)
                line += padding + str(self.heap[j + 2**i - 1]) + padding + ' '
                j += 1
            line = line[:-1] + '\n'
        print(line)

max_heap = BinaryHeap(10)
max_heap.insert(10)
max_heap.insert(4)
max_heap.insert(9)
max_heap.insert(1)
max_heap.insert(7)
max_heap.insert(5)
max_heap.insert(3)

max_heap.printheap()
max_heap.delete(5)
max_heap.printheap()
max_heap.delete(0)
max_heap.printheap()
print("heapmax = ", max_heap.find_max())