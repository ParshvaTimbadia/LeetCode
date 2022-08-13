class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        employeeMap = defaultdict(list)
        
        for e, m in enumerate(manager):
            employeeMap[m].append(e)
            
        
        def helper(id):
            
            if informTime[id] == 0:
                return 0
            
            timeFromSubordinates = 0
            
            for child in employeeMap[id]:
                timeFromSubordinates = max(timeFromSubordinates, helper(child))
            
            return informTime[id] + timeFromSubordinates
        
        
        return helper(headID)