# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        def leftHeight(node):
            if node is None:
                return 0
            return 1 + leftHeight(node.left)
        
        def rightHeight(node):
            if node is None:
                return 0
            return 1 + rightHeight(node.right)
        
        l, r = leftHeight(root), rightHeight(root)
        
        if l > r:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
        else:
            return 2**l - 1