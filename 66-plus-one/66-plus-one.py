class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            currentSum = digits[i] + carry
            carry = currentSum//10
            remainder = currentSum%10
            digits[i] = remainder
        
        return digits if carry == 0 else [carry] + digits
        
            