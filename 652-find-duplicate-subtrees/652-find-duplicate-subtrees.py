# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        
        hMap = {}
        result = []
        def helper(node):
            
            if not node:
                return "*"
            
            left = helper(node.left)
            right = helper(node.right)
            

            path = str(node.val) + "-" +left + "-" +right
            
            if path not in hMap:
                hMap[path] = 0

            hMap[path] += 1
            
            if hMap[path] == 2:
                result.append(node)

            return path
        
        helper(root)
        return result
        
                
            
            
        
        