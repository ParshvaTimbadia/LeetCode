


# Solution 1

class Solution:
    def square(self, n):
        return n*n
    
    def sortedSquares(self, A: List[int]) -> List[int]:
        
        
        
        result=[0 for i in range(len(A))]
        left=0
        right=len(A)-1
        if left ==right:
            result[left]=A[left]*A[left]
            return result
        i=len(A)-1
        while i>=0:
            if(self.square(A[left])  >= self.square(A[right])):
                result[i]=A[left]*A[left]
                left+=1
                i-=1
            elif(self.square(A[left])  < self.square(A[right])):
                result[i]=A[right]*A[right]
                right-=1
                i-=1
                
        return result        
  
 #Solution 2
 
 class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        a=[i*i for i in A]
        a.sort()
        return a
