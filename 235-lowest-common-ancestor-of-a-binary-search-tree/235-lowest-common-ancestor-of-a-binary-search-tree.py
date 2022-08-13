# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        def LCA(node):
            
            if node is None:
                return None
            
            if node is p or node is q:
                return node
            
            left = LCA(node.left)
            right = LCA(node.right)
            
            if left and right:
                return node
            
            if left:
                return left
            
            if right:
                return right
        
        return LCA(root)
            