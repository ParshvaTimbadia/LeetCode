# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        def helper(node):
            
            if node is None:
                return True
            
            if node.val != root.val:
                return False
            
            return helper(node.left) and helper(node.right)
        
        return helper(root)