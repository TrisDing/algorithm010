"""
Sorting Algorithms
"""
class Sort:
    def BubbleSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(n-1-i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

    def SelectionSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            min_j = i
            for j in range(i+1, n):
                if arr[j] < arr[min_j]:
                    min_j = j
            arr[i], arr[min_j] = arr[min_j], arr[i]
        return arr

    def InsertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):
            j = i
            while j > 0 and arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1
        return arr

    def MergeSort(self, arr):
        n = len(arr)
        if n < 2: return arr
        mid = n // 2
        leftSorted = self.MergeSort(arr[:mid])
        rightSorted = self.MergeSort(arr[mid:])
        return self.merge(leftSorted, rightSorted)

    def merge(self, left, right):
        res = []
        while left and right:
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        while left: res.append(left.pop(0))
        while right: res.append(right.pop(0))
        return res

    def QuickSort(self, arr):
        def quickSort(arr, left, right):
            if left < right:
                p = self.partition(arr, left, right)
                quickSort(arr, left, p - 1)
                quickSort(arr, p + 1, right)

        quickSort(arr, 0, len(arr) - 1)
        return arr

    def partition(self, arr, left, right):
        pivot = arr[left]
        i, j = left + 1, right
        while i <= j:
            while i <= j and arr[i] <= pivot: i += 1
            while i <= j and arr[j] >= pivot: j -= 1
            if i <= j:
                arr[i], arr[j] = arr[j], arr[i]
        arr[left], arr[j] = arr[j], arr[left]
        return j

    def HeapSort(self, arr):
        n = len(arr)

        # Build max heap. All nodes after n//2 - 1 are leaf-nodes and they
        # don't need to be heapified.
        for i in range(n//2 - 1, -1, -1):
            self.heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)

        return arr

    def heapify(self, arr, n, i):
        # Find largest among root, left child and right child
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        # Swap and continue if root is not largest
        if largest != i:
            arr[largest], arr[i] = arr[i], arr[largest]
            self.heapify(arr, n, largest)

    def CountingSort(self, arr):
        n = len(arr)
        res = [0] * n
        # Store the count of each elements in count array
        max_elem = max(arr)
        count = [0] * (max_elem + 1)
        for i in range(n):
            count[arr[i]] += 1
        # Store the cumulative count
        for i in range(1, max_elem + 1):
            count[i] += count[i-1]
        # Find the index of each element of the original array in count array
        # place the elements in output array
        i = n - 1
        while i >= 0:
            res[count[arr[i]] - 1] = arr[i]
            count[arr[i]] -= 1
            i -= 1
        # Copy the sorted elements into original array
        arr[:] = res[:]
        return arr

    def RadixSort(self, arr):
        # Get maximum element
        max_elem = max(arr)
        # Apply counting sort to sort elements based on place value.
        place = 1
        while max_elem // place > 0:
            self.couting(arr, place)
            place *= 10
        return arr

    def couting(self, arr, place):
        n = len(arr)
        res = [0] * n
        max_elem = max(arr)
        count = [0] * (max_elem + 1)
        # Calculate count of elements
        for i in range(n):
            index = arr[i] // place
            count[index % 10] += 1
        # Calculate cumulative count
        for i in range(1, max_elem + 1):
            count[i] += count[i-1]
        # Place the elements in sorted order
        i = n - 1
        while i >= 0:
            index = arr[i] // place
            res[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        arr[:] = res[:]

    def BucketSort(self, arr):
        n = len(arr)
        # Create empty buckets
        bucket = [[] for i in range(n)]
        # Insert elements into their respective buckets
        for x in arr:
            index = int(10 * x)
            bucket[index].append(x)
        # Sort the elements of each bucket
        for i in range(n):
            bucket[i] = sorted(bucket[i])
        # Get the sorted elements
        k = 0
        for i in range(n):
            for j in range(len(bucket[i])):
                arr[k] = bucket[i][j]
                k += 1
        return arr

arr = [3, 48, 15, 42, 26, 50, 27, 4, 34, 19, 2, 13, 36, 5, 47, 17]
sort = Sort()
print('Bubble Sort   ', sort.BubbleSort(arr[:]))
print('Selection Sort', sort.SelectionSort(arr[:]))
print('Insertion Sort', sort.InsertionSort(arr[:]))
print('Merge Sort    ', sort.MergeSort(arr[:]))
print('Quick Sort    ', sort.QuickSort(arr[:]))
print('Heap Sort     ', sort.HeapSort(arr[:]))
print('Counting Sort ', sort.CountingSort(arr[:]))
print('Radix Sort    ', sort.RadixSort(arr[:]))
print('Bucket Sort   ', [int(x*100) for x in sort.BucketSort([x/100 for x in arr])])