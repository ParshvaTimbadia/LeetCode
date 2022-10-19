class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        result = []
        def helper(node, slate):
            
            if node is None or node >= len(graph):
                return
            
            slate.append(node)
            
            if node == len(graph) - 1:
                result.append(slate[:])
            
            for neighbor in graph[node]:
                helper(neighbor, slate)
            
            slate.pop()
        
        helper(0, [])
        return result
        
        
            
        
        