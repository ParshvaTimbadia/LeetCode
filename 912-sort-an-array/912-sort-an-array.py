class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        def mergeSort(nums, start, end):
            
            if start == end:
                return
            
            mid = start + (end - start)//2
            
            mergeSort(nums, start, mid)
            mergeSort(nums, mid + 1, end)
            
            aux = []
            i = start 
            j = mid + 1
            
            while i <= mid and j <= end:
                
                if nums[i] < nums[j]:
                    aux.append(nums[i])
                    i += 1
                else:
                    aux.append(nums[j])
                    j += 1
            
            while i <= mid:
                aux.append(nums[i])
                i += 1
            
            while j <= end:
                aux.append(nums[j])
                j += 1
            
            nums[start:end+1] = aux
        
        mergeSort(nums, 0, len(nums)-1)
        return nums