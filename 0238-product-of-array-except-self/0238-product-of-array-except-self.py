class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        left_product = []
        product = 1
        
        for num in nums:
            left_product.append(product)
            product = product*num
        
        product = 1
        for i in range(len(nums)-1, -1, -1):
            left_product[i] = product*left_product[i]
            product = product*nums[i]
        
        return left_product
            
            