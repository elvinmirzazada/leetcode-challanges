from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue = deque()
        self.dirs = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        n = len(board)
        m = len(board[0])
        for i in range(n):
            if board[i][0] == 'O':
                queue.append((i,0))
            if board[i][m-1] == 'O':
                queue.append((i, m-1))
        
        
        for j in range(m):
            if board[0][j] == 'O':
                queue.append((0,j))
            if board[n-1][j] == 'O':
                queue.append((n-1, j))
        
        def inBounds(i,j):   
            return (0 <= i < n) and (0 <= j < m)
        print(queue)
        while queue:
            i, j = queue.popleft()
            board[i][j] = "#"
            
            
            for d in self.dirs:
                ii, jj = i + d[0], j + d[1]
                
                if not inBounds(ii, jj):
                    continue
                if board[ii][jj] != 'O':
                    continue
                queue.append((ii,jj))
                board[ii][jj] = '#'
            
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
            
        