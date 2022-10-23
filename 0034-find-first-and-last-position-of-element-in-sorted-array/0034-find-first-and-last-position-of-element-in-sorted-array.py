class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return [-1,-1]
        
        def getPos(first):
            start = 0
            end = len(nums)-1


            while start <= end:

                mid = start + (end - start)//2

                if first:
                    if nums[mid] >= target:
                        end = mid - 1
                    else:
                        start = mid + 1
                else:
                    if nums[mid] <= target:
                        start = mid + 1
                    else:
                        end = mid - 1

            return start, end
        
        startFirst, endFirst = getPos(True)
        if not(0 <= startFirst < len(nums)) or nums[startFirst]!=target:
            return [-1,-1]
        
        startEnd, endEnd = getPos(False)
        
        return [startFirst, endEnd]
        
            
            