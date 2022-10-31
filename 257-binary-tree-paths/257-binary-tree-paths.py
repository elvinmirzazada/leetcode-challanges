# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        queue = deque()
        result = []
        if root:
            queue.append((root, ""))
        
        while queue:
            node, path = queue.popleft()
            path += str(node.val) if len(path) == 0 else f"->{node.val}"

            if (not node.left) and (not node.right):
                result.append(path)
            
            else:
                if node.left:
                    queue.append((node.left, path))
                if node.right:
                    queue.append((node.right, path))
            
        return result