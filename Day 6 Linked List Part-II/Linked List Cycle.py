# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        fast = head
        slow = head
        
        if head is None or head.next is None or (head.next).next is None:
            return False
        
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
            if slow == fast:
                return True
        return False
            
        