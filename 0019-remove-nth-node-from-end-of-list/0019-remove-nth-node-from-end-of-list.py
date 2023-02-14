# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = head
        size = 0
        while curr:
            size += 1
            curr = curr.next
        
        size -= n
        curr = dummy
        while size > 0:
            curr = curr.next
            size -= 1
            
        curr.next = curr.next.next
        
        return dummy.next