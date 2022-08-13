class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        #Create a graph
        graph = defaultdict(list)
        inDegree = {}
        supplies = set(supplies)
        for recipesIndex in range(len(ingredients)):
            for item in ingredients[recipesIndex]:                
                graph[item].append(recipes[recipesIndex])
                if item not in inDegree:
                    inDegree[item] = 0
                if recipes[recipesIndex] not in inDegree:
                    inDegree[recipes[recipesIndex]] = 0
                inDegree[recipes[recipesIndex]] += 1
        
        queue = deque(supplies)
        
        result = []
        while queue:
            
            node = queue.popleft()
            
            if node not in supplies:
                result.append(node)
            
            for neighbor in graph[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result
        
        
        