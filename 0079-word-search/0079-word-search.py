class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.dirs = [
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        ]
        if not board:
            return False
        for i in range(len(board)):
            
            for j in range(len(board[i])):
                
                if self.rec_bfs(board, i, j, word):
                    return True
        
        return False
                        
        
    def rec_bfs(self, board, i, j, word):
        if len(word) == 0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
        # check whether can find "word" along one direction
        res = self.rec_bfs(board, i+1, j, word[1:]) or self.rec_bfs(board, i-1, j, word[1:]) \
        or self.rec_bfs(board, i, j+1, word[1:]) or self.rec_bfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res
