# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
      
#         self.arr = []
#         self.rec_dfs(root)
#         return self.arr[k-1]
        
        
#     def rec_dfs(self, node):
        
#         if node.left:
#             self.rec_dfs(node.left)
#         self.arr.append(node.val)
#         if node.right:
#             self.rec_dfs(node.right)
            
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            
            if k == 1:
                return root.val
            k -= 1
            root = root.right