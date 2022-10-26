# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()
        
        if root:
            queue.append(root)
            
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                if node.val != (node.left.val + node.right.val):
                    return False
                queue.append(node.left)
                queue.append(node.right)
                
        return True
        
        