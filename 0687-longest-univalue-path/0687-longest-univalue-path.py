# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        # Using DFS
        # We want information from left and right both. 
        # So we need to do bottom up. 
        
        if root is None:
            return 0
        
        maxUnival = 0
        def helper(node):
            nonlocal maxUnival
            
            if node is None:
                return 0 #longestchain
            
            left_chain = helper(node.left)
            right_chain = helper(node.right)
            
            left, right = 0, 0
            if node.left and node.val == node.left.val:
                left = left_chain
            
            if node.right and node.val == node.right.val:
                right = right_chain
            
            maxUnival = max(max(left, right) + 1, maxUnival, 1 + left + right)
            
            return max(left, right) + 1
        
        helper(root)
        return maxUnival - 1
        