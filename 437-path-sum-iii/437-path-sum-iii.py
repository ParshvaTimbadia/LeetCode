# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        hMap = {0:1}
        count = 0
        def helper(node, sumSoFar, hMap):
            nonlocal count
            
            if node is None:
                return 
            
            sumSoFar += node.val
            
            if sumSoFar - targetSum in hMap:
                count += hMap[sumSoFar - targetSum]
            
            if sumSoFar not in hMap:
                hMap[sumSoFar] = 0
            
            hMap[sumSoFar] += 1
            
            helper(node.left, sumSoFar, hMap)
            helper(node.right, sumSoFar, hMap)
            
            hMap[sumSoFar] -= 1
            
            if hMap[sumSoFar] == 0:
                del hMap[sumSoFar]
        
        helper(root, 0, hMap)
        return count
            
            
            
            
            