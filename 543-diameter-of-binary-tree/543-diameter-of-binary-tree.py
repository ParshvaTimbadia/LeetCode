# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def helper(node):
            
            if node is None:
                return 0, 0 #Diameter and left/right length
            
            left_diameter, left_height = helper(node.left)
            right_diameter, right_height = helper(node.right)
            
            return (max(left_diameter, right_diameter, left_height + right_height + 1), max(left_height, right_height) + 1)
        
        return helper(root)[0] - 1
    