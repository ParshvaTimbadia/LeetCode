class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1]*size
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def Union(self, u, v):
        findU = self.find(u)
        findV = self.find(v)
        
        if findU != findV:
            if self.size[findU] < self.size[findV]:
                self.size[findV] += self.size[findU]
                self.parent[findU] = findV
            else:
                self.size[findU] += self.size[findV]
                self.parent[findV] = findU
            

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU(len(accounts))
        
        emailGroup = {}
        
        for acid, account in enumerate(accounts):
            for j in range(1, len(account)):
                
                if account[j] not in emailGroup:
                    emailGroup[account[j]] = acid
                else:
                    dsu.Union(emailGroup[account[j]], acid)
        
        
        # Group all the email now.
        component = defaultdict(list)
        for email in emailGroup.keys():
            componentid = dsu.find(emailGroup[email])
            component[componentid].append(email)
        
        
        result = []
        # Map name and id:
        for acid in range(len(accounts)):
            if acid not in component:
                continue
            subres = []
            name = accounts[acid][0]
            subres.append(name)
            subres.extend(sorted(component[acid]))
            result.append(subres)
        
        return result
            
            
            
            
            