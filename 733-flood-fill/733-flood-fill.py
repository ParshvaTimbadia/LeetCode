class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        [0,0,0],
        [0,1,1]
        """
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        def dfs(row, col):
            
            if not(0<=row< len(image) and 0 <= col < len(image[0])) or image[row][col] != oldColor:
                return
            
            image[row][col] = newColor
            
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
        
        dfs(sr, sc)
        return image
        