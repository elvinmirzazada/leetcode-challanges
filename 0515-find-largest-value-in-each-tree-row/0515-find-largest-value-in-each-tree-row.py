# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        tree_q = deque()
        if root:
            tree_q.append(root)
        result = []
        
        while tree_q:
            max_el = -2 ** 32
            for _ in range(len(tree_q)):
                node = tree_q.popleft()
                if node.val > max_el:
                    max_el = node.val
                if node.left: tree_q.append(node.left)
                if node.right: tree_q.append(node.right)
            
            result.append(max_el)
            
        return result