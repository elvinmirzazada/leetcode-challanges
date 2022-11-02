# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_B = set()
        
        while headB:
            nodes_B.add(headB)
            headB = headB.next
            
        while headA:
            if headA in nodes_B:
                return headA
            headA = headA.next
        
        return None