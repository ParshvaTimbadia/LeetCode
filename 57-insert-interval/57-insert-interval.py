class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        i = 0 

        result = []        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        #Time to merge the new Interval.
        start = newInterval[0]
        end = newInterval[1]
        
        while i < len(intervals) and end >= intervals[i][0]:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        
        result.append([start, end])
        
        while i < len(intervals):
            result.append(intervals[i])
            i += 1
        
        return result
            
        