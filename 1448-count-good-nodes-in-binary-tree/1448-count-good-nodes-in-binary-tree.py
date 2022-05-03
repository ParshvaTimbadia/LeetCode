# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        count = 0
        def helper(node, maxSeenSoFar):
            nonlocal count
            
            if node is None:
                return
            
            if node.val >= maxSeenSoFar:
                count += 1
            
            helper(node.left, max(maxSeenSoFar, node.val) )
            helper(node.right, max(maxSeenSoFar, node.val))
        
        helper(root, root.val)
        return count
                
            