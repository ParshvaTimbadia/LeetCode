class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #Algorithm 
        # - add all the elements in the set
        # - iterate through all the elements in the list
        # - Check if the number has a smallest number. 
        # - If it has you can ignore that number since you want to track the bigger number.
        
        numbers = set(nums)
        maxCount = 0
        for index, num in enumerate(nums):
            if num - 1 in numbers:
                continue
            count = 0
            current_num = num
            while current_num in numbers:
                count += 1
                if current_num + 1 not in numbers:
                    break
                current_num = current_num + 1
            
            maxCount = max(count, maxCount)
        
        return maxCount