class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        result = []

        while l < r and t < b:
            i = l
            while i < r:
                result.append(matrix[t][i])
                i += 1
            t += 1
            
            j = t
            while j < b:
                # print(l,r, t, b)
            
                result.append(matrix[j][r-1])
                j += 1
            r -= 1
            
            if not (l < r and t < b):
                break
            
            i=r-1
            while i >= l:
                result.append(matrix[b-1][i])
                i -= 1
            b -= 1
            
            j=b-1
            while j >= t:
                result.append(matrix[j][l])
                j -= 1
            l += 1
            
            
        return result
            
            