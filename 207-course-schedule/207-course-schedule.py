class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        
        # BFS Approach:
        
        
        graph = {i:[] for i in range(n)}
        inDegree = {i:0 for i in range(n)}
        
        # Create the graph
        for u, v in prerequisites:
            graph[v].append(u)
            inDegree[u] += 1

        # Calculate in the Indegree
        # Start with indegree as zero
        
        queue = deque()
        for key, value in inDegree.items():
            if value == 0:
                queue.append(key)
        
        
        # Level by level traversal.
        result = []
        while queue:
            
            node = queue.popleft()
            
            result.append(node)
            
            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(result) == n
                
        