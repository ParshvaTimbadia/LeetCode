class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        
        currentColor = image[sr][sc]
        
        if currentColor == color:
            return image
        
        def dfs(row, col):
            nonlocal currentColor
            
            if not(0<= row < len(image) and 0<= col < len(image[0])) or image[row][col]!=currentColor:
                return 
            
            image[row][col] = color
            
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
        
        dfs(sr, sc)
        return image
        