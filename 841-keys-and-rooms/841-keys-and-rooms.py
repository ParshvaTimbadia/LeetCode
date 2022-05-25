class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        
        def bfs(source):
            
            q = deque()
            q.append(source)
            visited = set()
            visited.add(source)
            
            while q:
                
                if len(visited) == len(rooms):
                    return True
                
                previousRoom = q.popleft()
                for keys in rooms[previousRoom]:
                    if keys not in visited:
                        visited.add(keys)
                        q.append(keys)
            
            return False
        
        return bfs(0)