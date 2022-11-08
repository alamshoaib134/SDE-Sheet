# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reversedll(ptr) -> ListNode:
    pre = None
    nex = None
    while ptr is not None:
        nex = ptr.next
        ptr.next = pre
        pre = ptr
        ptr = nex
    return pre

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if head is None and head.next is None:
            return True
        
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
            fast = (fast.next).next
            slow = slow.next
            
        slow.next = reversedll(slow.next)
        slow = slow.next
        dummy = head
                

        
        while slow is not None:
            if slow.val != dummy.val:
                return False
            slow = slow.next
            dummy = dummy.next
        return True
        