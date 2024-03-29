# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def helper(node):
            
            if node is None:
                return None
            
            if node == p or node == q:
                return node
            
            left = helper(node.left)
            right = helper(node.right)
            
            if left and right:
                return node
            
            if left:
                return left
            
            if right:
                return right
        
        return helper(root)
                