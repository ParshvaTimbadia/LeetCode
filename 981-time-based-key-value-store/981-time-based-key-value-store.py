class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.dict:
            return ""
        start = 0
        end = len(self.dict[key]) - 1
        
        while start <= end:
            
            mid = start + (end - start)//2
            
            if self.dict[key][mid][0] <= timestamp:
                start = mid + 1
            else:
                end = mid - 1
        
        return self.dict[key][end][1] if end >= 0 else ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)