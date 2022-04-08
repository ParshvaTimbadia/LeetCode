# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        
        inOrderList = []
        def fillInorder(node:TreeNode):
            
            if node is None:
                return 
            
            fillInorder(node.left)
            inOrderList.append(node.val)
            fillInorder(node.right)
        
        fillInorder(root)
        
        def generateBalancedBST(inOrderList:List[int]) -> TreeNode:
            
            
            if len(inOrderList) == 0:
                return None
            
            elementIndex = len(inOrderList) // 2
            node = TreeNode(inOrderList[elementIndex])
            node.left = generateBalancedBST(inOrderList[:elementIndex])
            node.right = generateBalancedBST(inOrderList[elementIndex+1:])
        
            return node
        
        return generateBalancedBST(inOrderList)
            
            
        