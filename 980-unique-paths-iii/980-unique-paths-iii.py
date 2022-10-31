class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.directions = [
            (0, 1),
            (0, -1),
            (-1, 0),
            (1, 0)
        ]
        self.obstacle_count = 0
        self.paths = []
        st_i, st_j = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    st_i, st_j = i, j
                elif grid[i][j] == -1:
                    self.obstacle_count += 1
        self.rec_bfs(grid, st_i, st_j, {(st_i, st_j)})      
        
        return len(self.paths)
        
    def rec_bfs(self, arr, i, j, path):
        if arr[i][j] == 2:
            if len(path) == (len(arr)*len(arr[0]) - self.obstacle_count):
                self.paths.append(path)
        elif arr[i][j] == -1:
            pass
        else:
            for d in self.directions:
                new_i, new_j = i + d[0], j + d[1]
                if new_i < len(arr) and new_i >= 0 and new_j < len(arr[0]) and new_j >= 0 and arr[new_i][new_j] != -1  and (new_i, new_j) not in path:
                    path.add((new_i, new_j))
                    self.rec_bfs(arr, new_i, new_j, path)

                    path.remove((new_i, new_j))        
                    
                
        
        
        