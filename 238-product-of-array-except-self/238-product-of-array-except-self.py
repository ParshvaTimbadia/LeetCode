class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        #LeftArray = [1, 1, 2, 6]
        #RightArray = [24 ,12, 4,, 1]
        
        #Result = [24, 12, 8, 6]
        
        leftProduct = 1
        leftArray = []
        for index in range(len(nums)):
            leftArray.append(leftProduct)
            leftProduct = leftProduct*nums[index]
            
        
        rightProduct = 1
        for index in range(len(nums)-1, -1, -1):
            leftArray[index] = leftArray[index]*rightProduct
            rightProduct = rightProduct*nums[index]
        
        return leftArray
            
            