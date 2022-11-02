class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(1, numRows):
            new_row = [1]
            for j in range(1, i):
                new_row.append(res[i-1][j] + res[i-1][j-1])
            new_row.append(1)
            res.append(new_row)
        
        return res
            