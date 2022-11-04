class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dirs = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0),
            (1, 1),
            (1, -1),
            (-1, 1),
            (-1, -1)
        ]
        
        self.changes = {
            1: True,  # 1 -> 0
            0: False  # 0 -> 1
        }
        
        
        for k in range(len(board)):
            
            for m in range(len(board[k])):
                
                self.check_live_condition(board, k, m)
        
        for k in range(len(board)):
            
            for m in range(len(board[k])):
                if type(board[k][m]) == bool and board[k][m]:
                    board[k][m] = 0
                elif type(board[k][m]) == bool and not board[k][m]:
                    board[k][m] = 1
                    
        
        
        
    def check_live_condition(self, board, i, j):
        
        live_count = 0
        for d in self.dirs:
            new_i, new_j = d[0] + i, d[1] + j
            if new_i >=0 and new_i < len(board) and new_j >= 0 and new_j < len(board[i]):
                
                live_count += board[new_i][new_j]
                
        if live_count == 3 and board[i][j] == 0:
            board[i][j] = self.changes[0]
        
        elif board[i][j] == 1:
            if live_count < 2:
                board[i][j] = self.changes[1]
            elif live_count > 3:
                board[i][j] = self.changes[1]
                
        
        
        
            