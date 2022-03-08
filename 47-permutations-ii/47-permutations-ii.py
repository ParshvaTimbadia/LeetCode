class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        def helper(index, arr):
            if index == len(arr): 
                result.append(arr[:]) 
                return
            hmap = {}
            for i in range(index, len(arr)):
                arr[i],arr[index] = arr[index],arr[i]
                
                if (arr[index] not in hmap):
                    helper(index+1, arr)
                    hmap[arr[index]] = 1
                
                arr[i],arr[index] = arr[index],arr[i]
        helper(0, nums)
        return result