class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # Solve by placing the number in the correct position
        
        i = 0
        while i < len(nums):
            if nums[i] == i + 1:
                i += 1
            else:
                swapIndex = nums[i] - 1
                if nums[swapIndex] == nums[i]:
                    return nums[i]
    
                nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
                