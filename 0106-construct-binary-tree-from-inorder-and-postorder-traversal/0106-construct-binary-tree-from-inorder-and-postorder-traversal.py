# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeV1(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        
        root = TreeNode(val = postorder.pop())
        ind = inorder.index(root.val)
        
        root.left = self.buildTree(inorder[:ind], postorder[:ind]) 
        root.right = self.buildTree(inorder[ind+1:], postorder[ind:])
        return root
        
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def rec_builder(low, high):
            if low > high:
                return None
            
            root = TreeNode(val=postorder.pop())
            mid = inorder_map[root.val]
            root.right = rec_builder(mid+1, high)
            root.left = rec_builder(low, mid-1)
            
            return root
            
            
            
        return rec_builder(0, len(inorder)-1)