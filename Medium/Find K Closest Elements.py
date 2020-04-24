***
Find K Closest Elements


Given a sorted array, two integers k and x, find the k closest elements to x in the array. The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]
Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]
Note:
The value k is positive and will always be smaller than the length of the sorted array.
Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

***

class Solution:
    def findClosestElements(self, arr: List[int], K: int, X: int) -> List[int]:
        
        
        index = binary_search(arr, X)
        low, high = index - K, index + K

        low = max(low, 0)  # 'low' should not be less than zero
  # 'high' should not be greater the size of the array
        high = min(high, len(arr) - 1)

        minHeap = []
  # add all candidate elements to the min heap, sorted by their absolute difference from 'X'
        for i in range(low, high+1):
            heappush(minHeap, (abs(arr[i] - X), arr[i]))

  # we need the top 'K' elements having smallest difference from 'X'
        result = []
        for _ in range(K):
            result.append(heappop(minHeap)[1])

        result.sort()
        return result


def binary_search(arr,  target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    if low > 0:
        return low - 1
    return low
