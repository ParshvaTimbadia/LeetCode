# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        
        def helper(node):
            
            if node is None:
                return math.inf
            
            if node.left is None and node.right is None:
                return 1
            
            left_depth = 1+helper(node.left)
            right_depth = 1+helper(node.right)
            
            return min(left_depth, right_depth)
        
        return helper(root) 