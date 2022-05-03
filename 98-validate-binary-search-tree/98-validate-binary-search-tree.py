# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node, leftbound, rightbound):
            
            if node is None:
                return True
            
            if not leftbound < node.val < rightbound:
                return False
            
            return helper(node.left, leftbound, node.val) and helper(node.right, node.val, rightbound)
        
        return helper(root, -math.inf, math.inf)