# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        queue.append((root, 0, 0))
        hashMap = defaultdict(list)
        minimum = math.inf
        maximum = -math.inf
        
        while queue:
            
            node, vlevel, hlevel = queue.popleft()
            
            hashMap[vlevel].append((hlevel, node.val))
            minimum = min(minimum, vlevel)
            maximum = max(maximum, vlevel)
                
            if node.left:
                queue.append((node.left, vlevel-1, hlevel+1))
            
            if node.right:
                queue.append((node.right, vlevel+1, hlevel+1))
            
        result = []
        for i in range(minimum, maximum+1):
            temp = []
            for j in sorted(hashMap[i], key = lambda x:(x[0],x[1])):
                temp.append(j[1])
            result.append(temp)
        
        return result
            
            
            
            
            
            