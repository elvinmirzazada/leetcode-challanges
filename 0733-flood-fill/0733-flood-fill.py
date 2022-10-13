class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        check_num = image[sr][sc]
        if check_num != color:
            self.dfs(image, sr, sc, color, check_num)
        return image
        
        
    def dfs(self, image, sr, sc, color, check_num):
        
        if image[sr][sc] == check_num:
            image[sr][sc] = color
            
            if sr+1 < len(image):
                self.dfs(image, sr+1, sc, color, check_num)
            if sr-1 >= 0:
                self.dfs(image, sr-1, sc, color, check_num)
            if sc+1 < len(image[0]):
                self.dfs(image, sr, sc+1, color, check_num)
            if sc-1 >=0:
                self.dfs(image, sr, sc-1, color, check_num)
                
        
        