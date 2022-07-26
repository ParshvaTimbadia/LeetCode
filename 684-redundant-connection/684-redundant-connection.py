class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
    
        def find(x):
            if parent[x] == x:
                return x
            
            rootx = find(parent[x])
            parent[x] = rootx
            
            return rootx
        
        
        
        parent = [i for i in range(0, len(edges)+1)]
        size = [1]*(len(edges)+1)
        result = []
        
        for u, v in edges:
            findu = find(u)
            findv = find(v)
            
            if findu == findv:
                result.append([u, v])
            else:
                if size[findu] < size[findv]:
                    parent[findu] = findv
                    size[findv] += size[findu]
                else:
                    parent[findv] = findu
                    size[findu] += size[findv]
        
        return result[-1]
                    