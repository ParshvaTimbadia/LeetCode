# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        hMap = {value:index for index, value in enumerate(inorder)}
        
        def preToIn(preStart, preEnd, inorderStart, inorderEnd):
            
            if inorderStart > inorderEnd or preStart > preEnd:
                return 
            
            node = TreeNode(preorder[preStart])
            inRoot = hMap[preorder[preStart]]
            numLeft = inRoot - inorderStart
            
            node.left = preToIn(preStart + 1, preEnd + numLeft, inorderStart, inRoot - 1)
            node.right = preToIn(preStart + numLeft + 1, preEnd, inRoot + 1, inorderEnd)
            
            return node
        
        return preToIn(0, len(preorder) - 1, 0, len(preorder) - 1)
            
            
            
            