class UndergroundSystem:

    def __init__(self):
        self.incoming = collections.defaultdict(list)
        self.total = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.incoming[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.incoming[id]
        endStation, endTime = stationName,t
        
        if (startStation, endStation) not in self.total:
            self.total[(startStation, endStation)] = [0, 0] #Time and count
        
        self.total[(startStation, endStation)][0] += endTime - startTime
        self.total[(startStation, endStation)][1] += 1
        
        del self.incoming[id]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.total[(startStation, endStation)][0] / self.total[(startStation, endStation)][1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)