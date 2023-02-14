# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        
        def merge(list1, list2):
            node = ListNode()
            tmp = node
            while list1 or list2:
                if not list1:
                    tmp.next = list2
                    list2 = list2.next
                elif not list2:
                    tmp.next = list1
                    list1 = list1.next
                elif list1.val <= list2.val:
                    tmp.next = list1
                    list1 = list1.next
                else:
                    tmp.next = list2
                    list2 = list2.next
                
                tmp = tmp.next
            
            return node.next
        
        
        if lists:
            curr = lists[0]
            for i in range(1, len(lists)):
                curr = merge(curr, lists[i])
            
            return curr
        else:
            return None