class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        hMap = {}
        def dfs(node):
            
            if node in hMap:
                return hMap[node]
        
            hMap[node] = False
            
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
    
            hMap[node] = True
            
            return True
        
        result = []
        for node in range(len(graph)):
            if dfs(node):
                result.append(node)
        
        return result
        
        
            
            
            
            