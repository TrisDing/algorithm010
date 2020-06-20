"""
My Implementation of Heap
"""
class BinaryHeap:
    def __init__(self, capacity = 10):
        self.heapsize = 0
        self.heap = [-1] * (capacity + 1)

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
        self.heap[self.heapsize] = elem # 1. append new element to the end of heap.
        self.heapsize += 1              # 2. heap size + 1.
        endpos = self.heapsize - 1
        self._siftup(endpos)            # 3. bubble up the larger child until hitting root.

    def _siftup(self, i):
        """
        Maintains the heap property while inserting an element at position i
        """
        newitem = self.heap[i]
        while i > 0:
            parentpos = (i - 1) >> 1 # parent position
            parent = self.heap[parentpos]
            if newitem > parent:
                self.heap[i] = parent # Move the larger child up.
                i = parentpos
                continue
            break
        self.heap[i] = newitem

    def delete(self, i):
        """
        Remove an element at position i
        """
        if self.is_empty():
            raise Exception("Heap is empty, No element to delete")
        delitem = self.heap[i]
        endpos = self.heapsize - 1
        self.heap[i] = self.heap[endpos] # 1. replace the element at position i with the last element.
        self.heapsize -= 1               # 2. heap size - 1
        self._siftdown(i)                # 3. move down the new element until the end of heap.
        return delitem

    def _siftdown(self, i):
        """
        Maintains the heap property while deleting an element.
        """
        target = self.heap[i]
        endpos = self.heapsize
        childpos = 2 * i + 1 # leftmost child position
        while childpos < endpos:
            rightpos = childpos + 1
            if rightpos < endpos and self.heap[rightpos] > self.heap[childpos]:
                childpos = rightpos
            if target >= self.heap[childpos]:
                break
            self.heap[i] = self.heap[childpos] # Move the smaller child down.
            i = childpos
            childpos = 2 * i + 1
        self.heap[i] = target

    def find_max(self):
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
print(max_heap.find_max())
max_heap.delete(0)
max_heap.printheap()
print(max_heap.find_max())