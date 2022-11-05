# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = []
        is_left_to_right = True
        result = []
        if root:
            stack.append(root)
            
        while stack:
            tmp = []
            tmp_stack = []
            while stack:
                node = stack.pop()
                tmp.append(node.val)
                if is_left_to_right:
                    if node.left:
                        tmp_stack.append(node.left)
                    if node.right:
                        tmp_stack.append(node.right)
                    
                else:
                    if node.right:
                        tmp_stack.append(node.right)
                    if node.left:
                        tmp_stack.append(node.left)
            is_left_to_right = not is_left_to_right
            
            stack = tmp_stack
            result.append(tmp)
        return result
        