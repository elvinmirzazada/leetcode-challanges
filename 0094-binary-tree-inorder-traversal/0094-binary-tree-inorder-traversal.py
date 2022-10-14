# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.rec_traverse(root, result)
        return result
        
        
        
    def rec_traverse(self, root, res):
        
        if root:
            self.rec_traverse(root.left, res)
            res.append(root.val)
            self.rec_traverse(root.right, res)