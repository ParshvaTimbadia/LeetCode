class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        if len(nums) <= 1:
            return nums
        
        if len(nums) == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return nums
        
        found = False
        #Check for the value which is not sorted
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                found = True
                break
        
        if not found:
            start = 0
            end = len(nums) -1
            while start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            return nums
        
        toChangePrfixIndex = i
        toChangePrfixNumber = nums[i]
        
        # Find the number towards right which is just greater than the currentNumber
        for j in range(len(nums)-1, toChangePrfixIndex, -1):
            if nums[j] > toChangePrfixNumber:
                break
        
        nums[j], nums[toChangePrfixIndex] = nums[toChangePrfixIndex], nums[j]
        
        start = toChangePrfixIndex + 1
        end = len(nums) -1
        while start <= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
        return nums