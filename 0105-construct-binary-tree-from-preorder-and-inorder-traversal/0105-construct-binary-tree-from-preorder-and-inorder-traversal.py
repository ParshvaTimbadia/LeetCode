# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None
        
        inOrderDict = {value:index for index, value in enumerate(inorder)}
        preIndex = 0
        
        
        def helper(start, end):
            nonlocal preIndex
            
            if start > end:
                return 
            
            if start == end:
                node = TreeNode(preorder[preIndex])
                preIndex += 1
                return node
            
            node = TreeNode(preorder[preIndex])
            rootIndex = inOrderDict[preorder[preIndex]]
            preIndex += 1
            
            node.left = helper(start,rootIndex -1)
            node.right = helper(rootIndex+1, end)
            
            return node
        
        return helper(0, len(preorder)-1)