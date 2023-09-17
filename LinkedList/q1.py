"""206. Reverse Linked List"""

"""
Approach:
    Using the pointer
        p1 is moving one by one node
        p2 is changing the node's pointer to the previous p3 pointer
        p3 pointer is then pointing to the p2 pointer
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (head == None or head.next == None):
            return head
        
        p1: ListNode = head
        p2: ListNode = None
        p3: ListNode = None

        while (p1 != None):
            p2 = p1
            p1 = p1.next
            p2.next = p3
            p3 = p2

        return p2  