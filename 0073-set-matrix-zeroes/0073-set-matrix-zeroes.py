class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        founds = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                
                if matrix[i][j] == 0:
                    founds.append([i, j])

                    
        for n, m in founds:
            self.rec_set_0(matrix, n, m)
        # print(matrix)
        
        
    def rec_set_0(self, matrix, i, j):
        
        k = i - 1
        while k >= 0:
            if matrix[k][j] != 0:
                matrix[k][j] = 0
            # elif matrix[k][j] == 0:
            #     self.rec_set_0(matrix, k, j)
            k -= 1

        k = i + 1
        while k < len(matrix):
            print(k, j)
            if matrix[k][j] != 0:
                matrix[k][j] = 0
            # elif matrix[k][j] == 0:
            #     self.rec_set_0(matrix, k, j)
            k += 1

        k = j - 1
        while k >= 0:
            if matrix[i][k] != 0:
                matrix[i][k] = 0
            # elif matrix[i][k] == 0:
            #     self.rec_set_0(matrix, i, k)
            k -= 1

        k = j + 1
        while k < len(matrix[i]):
            if matrix[i][k] != 0:
                matrix[i][k] = 0
            # elif matrix[i][k] == 0:
            #     self.rec_set_0(matrix, i, k)
            k += 1   
            