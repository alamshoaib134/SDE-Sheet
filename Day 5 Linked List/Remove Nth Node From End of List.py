# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        l = 0
        if not head.next:
            return None
        while temp:
            temp = temp.next
            l+=1
        index = l - n 
        if index==0:
            return head.next
        temp = head
        for i in range(index-1):
            temp = temp.next
        t = temp.next
        temp.next = t.next
       
        return head
      