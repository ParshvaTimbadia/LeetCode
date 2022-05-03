# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        
        """
        Traversal:  PostOrder
        
        Cases:     None -> 0
                    
                    1
                  /   \
                 2     3
        
        
        """
        diameter = 0
        def helper(node):
            nonlocal diameter
            
            if node is None:
                return 0
            
            leftNodes = helper(node.left)
            rightNodes = helper(node.right)
            
            
            maxHeightfromLeftAndRight = max(leftNodes, rightNodes) + 1
            diameter = max(diameter,leftNodes+rightNodes+1)
            
            return maxHeightfromLeftAndRight
        
        helper(root)
        return diameter - 1
         
        