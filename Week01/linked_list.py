"""
Singly Linked List Data Structure
"""

class ListNode:
    """
    Linked List Node
    """
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insert_node(node, new_node):
    new_node.next = node.next
    node.next = new_node

def remove_node(node):
    node.next = node.next.next

def create_list(iterable = ()):
    dummy = ListNode()
    for elem in reversed(iterable):
        insert_node(dummy, ListNode(elem))
    return dummy.next

def print_list(head):
    result, p = [], head
    while p:
        result.append(p.val)
        p = p.next
    print(result)
