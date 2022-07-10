class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        i = 0 
        result = []
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        startIntervals = newInterval[0]
        endIntervals = newInterval[1]
        while i < len(intervals) and endIntervals >= intervals[i][0]:
            startIntervals = min(startIntervals, intervals[i][0])
            endIntervals = max(endIntervals, intervals[i][1])
            i += 1
        
        result.append([startIntervals, endIntervals])
        
        while i < len(intervals):
            result.append(intervals[i])
            i+=1
        
        return result