# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        """
        Traversal: PostOrder
        
        Cases:  
        
                1. None
                
                2.      3
                      /   \
                      9   20
                            \
                             7

        """
        
        def helper(node):
            
            if node is None:
                return 0 #Number of nodes, maxNumberOfNodes
            
            leftnodes  = helper(node.left)
            rightnodes = helper(node.right)
            
            #Processing
            return max(leftnodes, rightnodes) + 1
        
        return helper(root)
        