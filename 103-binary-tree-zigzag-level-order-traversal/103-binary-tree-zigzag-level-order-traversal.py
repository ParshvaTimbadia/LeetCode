# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
    
        q = deque()
        q.append(root)
        rightToLeft = True
        result = []
        
        while q:
            
            temp = deque()
            
            for _ in range(len(q)):
                
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
                    
                if rightToLeft:
                    temp.append(node.val)
                else:
                    temp.appendleft(node.val)
            
            result.append(list(temp))
            rightToLeft = not rightToLeft
        
        return result
                    
                
                
                
                
                
                