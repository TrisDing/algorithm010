"""
21. Merge Two Sorted Lists <Easy>
https://leetcode-cn.com/problems/merge-two-sorted-lists/
"""
from linked_list import ListNode, create_list, print_list

class Solution:
    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Solution #1: iteratively
        Time: O(n)
        Space: O(1)
        """
        dummy = ListNode()
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next, l1 = l1, l1.next
            else:
                p.next, l2 = l2, l2.next
            p = p.next
        p.next = l1 or l2
        return dummy.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Solution #2: recursively
        Time: O(n)
        Space: O(1)
        """
        if not l1: return l2
        if not l2: return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2

solution = Solution()

l1 = create_list([1,2,3])
l2 = create_list([1,2,4])
ans1 = solution.mergeTwoLists1(l1, l2)
print_list(ans1) # [1,1,2,2,3,4]

l1 = create_list([1,2,3])
l2 = create_list([3,4,5,6,7])
ans2 = solution.mergeTwoLists2(l1, l2)
print_list(ans2) # [1, 2, 3, 3, 4, 5, 6, 7]