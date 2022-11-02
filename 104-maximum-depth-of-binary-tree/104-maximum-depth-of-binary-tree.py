# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        queue = deque()
        if root:
            queue.append((root, 1))
        max_depth = 0
        while queue:
            node, depth = queue.popleft()
            max_depth = max(depth, max_depth)
            if node.left:
                queue.append((node.left, max_depth + 1))
            
            if node.right:
                queue.append((node.right, max_depth + 1))
            
        return max_depth
                         
        
        