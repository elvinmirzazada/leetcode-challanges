# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.rec_convert(nums, 0, len(nums)-1)
        
        
    def rec_convert(self, nums, i, j):
        
        if i > j:
            return None
        
        mid = (i + j) // 2
        node = TreeNode(nums[mid])
        node.left = self.rec_convert(nums, i, mid-1)
        node.right = self.rec_convert(nums, mid+1, j)
        
        return node