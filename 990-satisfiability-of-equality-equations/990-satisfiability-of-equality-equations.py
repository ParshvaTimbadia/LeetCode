class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        
        def find(x):
            if parent[x] == x:
                return x
            
            root = find(parent[x])
            
            parent[x] = root
            
            return parent[x]
        
        def union(u, v):
            
            findU = find(u)
            findV = find(v)
            
            if findU != findV:
                if size[findU] < size[findV]:
                    size[findV] += size[findU]
                    parent[findU] = findV
                else:
                    size[findU] += size[findV]
                    parent[findV] = findU
        
        parent = [i for i in range(26)]
        size = [1]*26
        
        def char(c):
            return ord(c) - ord('a')
        
        for equalities in equations:
            if equalities[1] == "=" and equalities[2] == "=":
                union(char(equalities[0]), char(equalities[-1]))
        
        for inequalities in equations:
            if inequalities[1] == "!" and inequalities[2] == "=":
                u = find(char(inequalities[0]))
                v = find(char(inequalities[-1]))
        
                if u == v:
                    return False       
        return True
            