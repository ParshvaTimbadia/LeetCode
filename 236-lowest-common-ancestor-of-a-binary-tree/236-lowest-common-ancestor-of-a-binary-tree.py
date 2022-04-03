# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def helper(root):
            
            if root is None:
                return None
            
            if root == p or root == q:
                return root
            
            found_from_left = helper(root.left)
            found_from_right = helper(root.right)
            
            if found_from_left and found_from_right:
                return root
            
            if found_from_left:
                return found_from_left
            
            if found_from_right:
                return found_from_right
        
        return helper(root)
            
            
            
            