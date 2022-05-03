# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        """
                1
               /
              1
        
        """
        
        
        
        def sameTree(p, q):
            
            if p is None and q is None:
                return True
            
            if p is None or q is None or p.val != q.val:
                return False
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        def helper(node):
            
            if node is None:
                return False
            
            if node.val == subRoot.val:
                if sameTree(node, subRoot): 
                    return True
                
            return helper(node.left) or helper(node.right)
        
        return helper(root)
                
            