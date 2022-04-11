# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    adjList = defaultdict(list)
    def createGraph(self, root:TreeNode) -> dict:
        
        q = deque()
        q.append(root)
        
        while q:
            
            for _ in range(len(q)):
                
                node = q.popleft()
                
                if node.left:
                    q.append(node.left)
                    self.adjList[node.left].append(node)
                    self.adjList[node].append(node.left)
                    
                if node.right:
                    q.append(node.right)
                    self.adjList[node.right].append(node)
                    self.adjList[node].append(node.right)
        
        

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        self.createGraph(root)
        result = []
        
        def helper(target, distance, visited):
            
            if distance == k and target not in visited:
                result.append(target.val)
            
            if distance > k or target is None:
                return
            
            if target in visited:
                return
            
            visited.add(target)
            
            for node in self.adjList[target]:
                helper(node, distance+1, visited)
            
            visited.remove(target)
        
        helper(target, 0, set())
        return result
            
            
        
        