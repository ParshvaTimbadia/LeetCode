import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def helper(start, end):

            pivot = random.randint(start, end)
            
            #Swap with the start
            nums[pivot], nums[start] = nums[start], nums[pivot]
            
            #Patitionting
            lower = start
            
            for i in range(start+1, end+1):
                if nums[i] <= nums[start]:
                    lower += 1
                    nums[lower], nums[i] = nums[i], nums[lower]
            
            #Place the pivot at the right location
            nums[start], nums[lower] = nums[lower], nums[start]
            
            if lower == len(nums) - k:
                return nums[lower]
            elif lower < len(nums) - k:
                return helper(lower + 1, end)
            else:
                return helper(start, lower - 1)
        
        return helper(0, len(nums) - 1)