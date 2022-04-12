# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first,second, third, previous = None, None, None, None
        def helper(current):
            nonlocal first,second, third, previous
            
            if current is None:
                return
            
            helper(current.left)
            
            if previous is not None and previous.val > current.val:
                
                if not first:
                    first = previous
                    second = current
                else:
                    third = current
            
            previous = current
            helper(current.right)
        
        helper(root)
        
        if not third:
            first.val ,second.val = second.val, first.val
        else:
            first.val, third.val = third.val, first.val