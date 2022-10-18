class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        j = len(nums)
        i = 0
        while i < j:
            
            while j > 0 and nums[i] == val and i!=j:
                j -= 1
                nums[j], nums[i] = nums[i], nums[j]
        
            i += 1
        
        return j 
            