# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        return root if self.rec_dfs(root, limit) else None
        
        
        
    def rec_dfs(self, node, limit, curr_sum=0):
        curr_sum += node.val
       
        if not node.left and not node.right:
            return curr_sum >= limit 
        
        left = self.rec_dfs(node.left, limit, curr_sum) if node.left else False

        right = self.rec_dfs(node.right, limit, curr_sum) if node.right else False
        
        if not left:
            node.left = None
        if not right:
            node.right = None
        
        return left or right
            