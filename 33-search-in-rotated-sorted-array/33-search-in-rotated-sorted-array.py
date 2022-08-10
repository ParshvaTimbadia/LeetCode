class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        start = 0
        end = len(nums)-1
        
        while start <= end:
            
            mid = start + (end - start)//2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[-1] and target > nums[-1]: #I am in the wrong zone, move left
                end = mid - 1
            elif nums[mid] > nums[-1] and target <= nums[-1]: #I am in the wrong zone, move right
                start = mid + 1
            else:
                if target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        
        return -1
                
                
                