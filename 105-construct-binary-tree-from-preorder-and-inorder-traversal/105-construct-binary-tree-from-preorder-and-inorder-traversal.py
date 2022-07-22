# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        
        # Put the entire inOrder traversal into the hashMap
        hMap = {value:index for index, value in enumerate(inorder)}
        
        def helper(preorder, inorder, preStart, preEnd, inStart, inEnd):
            if preStart > preEnd or inStart > inEnd:
                return None
            
            node = TreeNode(preorder[preStart])
            
            inRoot = hMap[preorder[preStart]]
            numLeft = inRoot - inStart
            
            
            node.left = helper(preorder, inorder, preStart + 1, preStart + numLeft, inStart, inRoot - 1)
            node.right = helper(preorder, inorder, preStart + numLeft+ 1, preEnd , inRoot + 1, inEnd)
            
            return node
        
        
        root = helper(preorder, inorder, 0, len(preorder)-1, 0, len(inorder)-1)
        
        return root