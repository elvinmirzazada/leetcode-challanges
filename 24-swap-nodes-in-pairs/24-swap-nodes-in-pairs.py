# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        first_node = head
        sec_node = head.next
        
        first_node.next = self.swapPairs(sec_node.next)
        sec_node.next = first_node
        
        return sec_node