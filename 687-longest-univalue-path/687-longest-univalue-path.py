# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    result = 0
    def helper(self, node): 
        
        if node is None:
            return 0
        
        left = self.helper(node.left)
        right = self.helper(node.right)
        
        if node.left and node.right and node.val == node.left.val and node.val == node.right.val:
            self.result = max(self.result, left + right + 2)
            return max(0, max(left, right) + 1)
        elif node.left and node.left.val == node.val:
            self.result = max(self.result, left + 1)
            return max(0, left + 1)
        elif node.right and node.right.val == node.val:
            self.result = max(self.result, right + 1)
            return max(0, right + 1)
        else:
            return 0
            
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.result
    