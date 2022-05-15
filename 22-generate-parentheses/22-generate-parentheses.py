class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
    
        result = []
        def helper(left, right, slate):

            if right > left or left > n or right > n:
                return 

            if left == n and right == n:
                result.append("".join(slate[:]))
                return

            slate.append('(')
            helper(left+1, right, slate)
            slate.pop()

            slate.append(')')
            helper(left, right+1, slate)
            slate.pop()

        helper(0,0,[])
        return result
        