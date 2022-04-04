# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        
        result = []
        def helper(node, slate, sumSoFar):
            
            if node is None:
                return 
            
            slate.append(node.val)
            sumSoFar += node.val
            
            
            if node.left is None and node.right is None and sumSoFar == targetSum:
                result.append(slate[:]) 
            
            helper(node.left, slate, sumSoFar)
            helper(node.right, slate, sumSoFar)
            
            slate.pop()
            
        
        helper(root, [], 0)
        return result
            
            