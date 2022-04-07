# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def helper(root, minNode, maxNode):
            
            if root is None:
                return True
            
            if not minNode < root.val < maxNode:
                return False
            
            return helper(root.left, minNode, root.val) and helper(root.right, root.val, maxNode)   
        
        return helper(root, -math.inf, math.inf)