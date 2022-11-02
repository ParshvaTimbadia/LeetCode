class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        
        timeLine = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            timeLine[name].append(self.getTime(time))
        
        result = []
        
        for name in sorted(timeLine.keys()):
            timeLine[name].sort()
            for i in range(2,len(timeLine[name])):
                if timeLine[name][i] - timeLine[name][i-2]  <= 60:
                    result.append(name)
        
        return sorted(list(set(result)))
    
    def getTime(self, time):
        hours, minutes = time.split(":")
        totalTime = int(hours)*60 + int(minutes) 
        return totalTime