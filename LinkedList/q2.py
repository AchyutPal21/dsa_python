"""143. Reorder List"""

"""
Approach:
    1 2 3 4 5 6
    1. Find the mid and make the mid.next to Null
    2. Reverse the list after the mid
    3. Will use two pointers for each half
        3.1 l_curr, l_prev, r_curr and r_prev
        3.2 The prev pointer will be assigned to the curr pointer and curr pointer will move to the next node
        3.3 The l_prev will point the r_curr
        3.4 The right pointers will also do the same as the step 3.1 and 3.2
        3.5 The r_prev will then point to the l_curr
        3.6 And this is one cycle of the loop until one of the _curr pointer is not becoming None
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Finding the mid node of the list
        slow_pointer: ListNode = head
        fast_pointer: ListNode = head
        while (fast_pointer.next != None and fast_pointer.next.next != None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        # Separating the list from half and reversing the right half
        fast_pointer = slow_pointer.next
        slow_pointer.next = None
        slow_pointer = None
        temp_pointer: ListNode = None
        while (fast_pointer != None):
            slow_pointer = fast_pointer
            fast_pointer = fast_pointer.next
            slow_pointer.next = temp_pointer
            temp_pointer = slow_pointer
        
        # Applying our approach        
        left_prev: ListNode = None
        left_curr: ListNode = head
        right_prev: ListNode = None
        # slow_pointer is the head of the second half
        right_curr: ListNode = slow_pointer

        while(left_curr != None and right_curr != None):
            # Assigning the left_prev to left_curr
            left_prev = left_curr
            # Moving the left_curr to the next node
            left_curr = left_curr.next
            # Pointing the left_prev node to the right_curr node
            left_prev.next = right_curr
            # Assigning the right_prev to the right_curr
            right_prev = right_curr
            # Moving the right_curr to the next node
            right_curr = right_curr.next
            # Pointing the right_prev to the left_curr node
            right_prev.next = left_curr




        