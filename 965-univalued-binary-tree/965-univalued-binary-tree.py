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
            
            if node.left is None and node.right is None:
                return True
            
            left = helper(node.left)
            right = helper(node.right)
            
            if not left or not right:
                return False
            
            if node.left and node.right and node.val != node.left.val and node.val != node.right.val:
                return False
            
            if node.left and node.left.val != node.val or node.right and node.right.val != node.val:
                return False
            
            return True
        
        return helper(root)