class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        sources = 0
        destination = len(graph) - 1
        result = []
        def dfs(source, slate):
            if source is None:
                return
            
            slate.append(source)
            
            if source == destination:
                result.append(slate[:])
                return
        
            for neighbor in graph[source]:
                dfs(neighbor, slate)
                slate.pop()
        
        dfs(sources, [])
        return result
                
            
        
        
        