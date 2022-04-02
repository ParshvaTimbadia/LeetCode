# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        
        def helper(node, sumSoFar):
            
            if node is None:
                return False
            
            sumSoFar += node.val
            
            if node.left is None and node.right is None and targetSum == sumSoFar:
                return True
            
            return helper(node.left, sumSoFar) or helper(node.right, sumSoFar)
        
        return helper(root, 0)
    
                
            