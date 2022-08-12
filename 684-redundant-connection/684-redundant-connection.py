class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        
        def find(x):
            
            if x == parent[x]:
                return x
            
            root = find(parent[x])
            parent[x] = root
            
            return parent[x]
        
        n = set()
        for edge in edges:
            u = edge[0]
            v = edge[1]
            
            n.add(u)
            n.add(v)
        
        parent = [i for i in range(len(n)+1)]
        size = [1 for i in range(len(n)+1)]

        
        for edge in edges:
            rootU = find(edge[0])
            rootV = find(edge[1])
            
            if rootU == rootV:
                result = [edge[0], edge[1]]
            else:
                if size[rootU] < size[rootV]:
                    size[rootV] += size[rootU]
                    parent[rootU] = rootV
                else:
                    size[rootU] += size[rootV]
                    parent[rootV] = rootU
        
        return result
        