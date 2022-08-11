class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        
        l, r = 0,0
        steps = 1
        
        for i in range(len(nums)):
            maxJump = 0
            for j in range(l, r+1):
                maxJump = max(maxJump, nums[j] + j)
            
            l = r + 1
            r = maxJump
            if r >= len(nums) - 1:
                return steps
            
            steps += 1
    
            
            