# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        flag = 0 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                flag = 1
                break
        if flag==0:
            return 
        
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
            
        return slow
        