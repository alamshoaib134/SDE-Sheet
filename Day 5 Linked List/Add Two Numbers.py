# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        newhead = None
        temp = None
        carry = 0
        while l1 or l2:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1=l1.next
            if l2:
                sum_val+= l2.val
                l2 = l2.next
            node = ListNode(sum_val %10)
            carry = sum_val//10
            
            if temp is None:
                temp = newhead = node
            else:
                temp.next = node
                temp = temp.next
            
        if carry > 0:
            temp.next = ListNode(carry)
        return newhead
                