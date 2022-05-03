# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        index = 1
        ansNode = None
        def helper(node):
            nonlocal ansNode, index
            
            if node is None:
                return
            
            helper(node.left)
            
            
            if index == k:
                ansNode = node.val
            
            index += 1
            helper(node.right)
        
        helper(root)
        return ansNode
    