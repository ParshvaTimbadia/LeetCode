class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        
        parent = {}
        
        def find(x):
            if parent[x] == x:
                return x
            
            root = find(parent[x])
            parent[x] = root
            
            return parent[x]
        
        def union(u, v):
            if u not in parent:
                parent[u] = u
            
            if v not in parent:
                parent[v] = v
            
            findU = find(u)
            findV = find(v)
            
            if findU != findV:
                parent[findU] = findV
        
        
        for i, j in stones:
            union(i, j + 100001)
        
        connectComponents = 0
        
        for key, value in parent.items():
            if key == value:
                connectComponents += 1
        
        return len(stones) - connectComponents
        
        