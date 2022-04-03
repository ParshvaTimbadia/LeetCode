# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        
        def helper(node):
            
            if node is None:
                return 0, True
            
            left_height, left_balanced = helper(node.left)
            right_height, right_balanced = helper(node.right)
            
            
            if not left_balanced or not right_balanced or  abs(left_height - right_height) > 1:
                return 0, False
            
            return max(left_height, right_height) + 1, True
        
        return helper(root)[1]
    
            