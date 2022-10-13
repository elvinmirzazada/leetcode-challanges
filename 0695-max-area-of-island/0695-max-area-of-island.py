class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        for i in range(len(grid)):
            
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.rec_island_check(grid, i, j))
                
                
        return max_area
                
    def rec_island_check(self, grid, m, n):

        area = 0
        if grid[m][n] == 1:
            grid[m][n] = 0
            area += 1
            if m+1 < len(grid) and grid[m+1][n] == 1:
                area += self.rec_island_check(grid, m+1, n)
            if m-1 >= 0 and grid[m-1][n] == 1:
                area += self.rec_island_check(grid, m-1, n)
            if n+1 < len(grid[0]) and grid[m][n+1] == 1:
                area += self.rec_island_check(grid, m, n+1)
            if n-1 >= 0 and grid[m][n-1] == 1:
                area += self.rec_island_check(grid, m, n-1)
        
        
            
        return area
                
                
                