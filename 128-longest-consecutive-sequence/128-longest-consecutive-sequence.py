class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        
        #[1, 2]
        
        store = set(nums)
        seen = set()
        max_count = 0
        for num in nums:
            if num in seen:
                continue
            curr = num
            while curr + 1 in store:
                seen.add(curr)
                curr = curr + 1
            max_count = max(max_count, curr - num + 1)
        return max_count
                
                
            
        