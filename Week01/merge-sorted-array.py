"""
88. Merge Sorted Array <Easy>
https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List

class Solution:
    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Solution #1: Two pointers, forwards
        Time: O(m+n)
        Space O(m): need a copy for nums1
        """
        nums1_copy = nums1[:m]
        nums1[:] = []

        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # reminder
        if p1 < m: nums1[p1+p2:] = nums1_copy[p1:]
        if p2 < n: nums1[p1+p2:] = nums2[p2:]

    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Solution #2: Three pointers, backwards
        Time: O(m+n)
        Space O(1)
        """
        p1, p2, p = m-1, n-1, len(nums1) - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        nums1[:p2+1] = nums2[:p2+1]

solution = Solution()

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
solution.merge1(nums1, 3, nums2, 3)
print(nums1) # [1, 2, 2, 3, 5, 6]

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
solution.merge2(nums1, 3, nums2, 3)
print(nums1) # [1, 2, 2, 3, 5, 6]