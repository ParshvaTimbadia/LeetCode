# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        
        if root is None:
            return []
        
        result = []
        def helper(node, slate):
            
            if node is None:
                return None
            
            slate.append(str(node.val))
            
            if node.left is None and node.right is None:
                result.append("->".join(slate))
            
            helper(node.left, slate)
            helper(node.right, slate)
            
            slate.pop()
        
        helper(root, [])
        return result