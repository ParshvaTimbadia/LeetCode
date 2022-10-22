import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        # Quik Sort Algorithm
        
#         def quickSort(start, end):
            
#             if start >= end:
#                 return 
            
#             pivotIndex = random.randint(start, end)
#             nums[start], nums[pivotIndex] = nums[pivotIndex], nums[start]
            
#             i = start
#             for j in range(i+1, end + 1):
#                 if nums[start] >= nums[j]:
#                     i += 1
#                     nums[i], nums[j] = nums[j], nums[i]
            
#             nums[start], nums[i] = nums[i], nums[start]
            
#             quickSort(start, i - 1)
#             quickSort(i+1, end)
        
#         quickSort(0, len(nums)-1)
#         return nums

        if len(set(nums)) == 1:
            return nums

        def quickSort(A, start, end):
            
            if start >= end:
                return
            
            pivotIndex = random.randint(start, end)
            nums[start], nums[pivotIndex] = nums[pivotIndex], nums[start]
            
            i = start + 1
            
            for j in range(i, end+1):
                if nums[j] <= nums[start]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            
            i -= 1
            nums[start], nums[i] = nums[i], nums[start]
            
            quickSort(A, start, i - 1)
            quickSort(A, i + 1, end)
        
        quickSort(nums, 0, len(nums)-1)
        return nums
            
            