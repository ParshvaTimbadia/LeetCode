class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        start = 0
        end = len(nums) - 1
        
        while start < end and nums[start] <= nums[start + 1]:
            start += 1
        
        while start < end and nums[end - 1] <= nums[end]:
            end -= 1
        
        if start == end: 
            return 0
        

        mini = math.inf
        maxi = -math.inf
        
        for index in range(start, end + 1):
            mini = min(mini, nums[index])
            maxi = max(maxi, nums[index])
        

        while start - 1 >= 0 and nums[start-1] > mini:
            start -= 1
        
        while end + 1 < len(nums) and nums[end+1] < maxi:
            end += 1
        
        return end - start + 1
        