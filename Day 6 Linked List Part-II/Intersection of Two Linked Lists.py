# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        lenA = 0
        lenB = 0
        
        tempA = headA
        tempB = headB
        
        while tempA is not None:
            tempA = tempA.next
            lenA+=1
        while tempB is not None:
            tempB = tempB.next
            lenB+=1
        
        tempA = headA
        tempB = headB
        
        diff = 0
        if lenA >= lenB:
            diff = lenA-lenB
            for i in range(diff):
                tempA = tempA.next
        else:
            diff = lenB - lenA
            for i in range(diff):
                tempB = tempB.next
        # intersectVal = 0       
        while tempA is not None and tempB is not None:
            if tempA == tempB:
                return tempA
            else:
                tempA = tempA.next
                tempB = tempB.next
        
            
        
        
        
        