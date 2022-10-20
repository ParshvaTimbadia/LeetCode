class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        #Graph Traversal:
        
        def dfs(start, destination, product, visited):
            
            answer = float(-1)
            visited.add(start)
            
            if start in graph and destination in graph[start]:
                return product*graph[start][destination]

            #Seek for the neighbors 
            for neighbor in graph[start].keys():
                if neighbor in visited:
                    continue
                answer = dfs(neighbor, destination, product*graph[start][neighbor], visited)
                if answer != float(-1):
                    return answer
            
            return answer
        
        
        # Let's create a graph
        graph = collections.defaultdict(dict)
        
        for index, equation in enumerate(equations):
            
            num = equation[0]
            denom = equation[1]
        
            graph[num][denom] = values[index]
            graph[denom][num] = 1/values[index]
        
        
        # Outer Loop
        result = []
        for query in queries:
            start = query[0]
            end = query[1]
            
            if start not in graph or end not in graph:
                result.append(float(-1))
            elif start == end:
                result.append(float(1))
            else:  
            #Path exists and we will call the dfs
                result.append(dfs(start, end, 1, set()))
        
        
        return result
        