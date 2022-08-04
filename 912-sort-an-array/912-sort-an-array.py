import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def quickSort(A, start, end):
            
            if start >= end:
                return
            
            pivotIndex = random.randint(start, end)
            
            A[start], A[pivotIndex] = A[pivotIndex], A[start]
            
            i = start
            
            for j in range(i+1, end + 1):
                if A[j] <= A[start]:
                    i += 1
                    A[i], A[j] = A[j], A[i]
            
            A[start], A[i] = A[i], A[start]
            
            quickSort(A, start, i - 1)
            quickSort(A, i + 1, end)
        
        quickSort(nums, 0, len(nums)-1)
        return nums
                    
            
            