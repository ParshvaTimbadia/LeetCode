class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        # A valid triangle is called when 
        # A + B > C
        # A + C > B
        # B + C > A
        
        nums.sort()
        count = 0
        for c in range(len(nums)-1, -1, -1):
            
            b = c - 1
            a = 0
            
            while a < b:
            
                if nums[a] + nums[b] > nums[c]: #Equation statisfied:
                    count += b - a
                    b -= 1
                else:
                    a += 1
        
        return count
                