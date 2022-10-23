class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        R, C = len(matrix), len(matrix[0])
        ans = [[None] * R for _ in range(C)]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                ans[c][r] = matrix[r][c]
        
        return ans