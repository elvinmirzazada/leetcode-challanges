class Solution(object):
    def addToArrayForm(self, A, K):
        for i in range(len(A) - 1, -1, -1):
            if not K: break
            K, A[i] = divmod(A[i] + K, 10)
        while K:
            K, a = divmod(K, 10)
            A = [a] + A
        return A

# class Solution:
#     def addToArrayForm(self, num: List[int], k: int) -> List[int]:
#         num_int = self.arr_to_int(num)
#         res = num_int + k

#         return list(str(res))
    
#     def arr_to_int(self, arr):
#         n = len(arr)
#         num = 0
#         for i in arr:
#             num += i * (10**(n-1))
#             n-=1
        
#         return num
        
#     def int_to_arr(self, num):
#         res = []
#         while num:
#             res.append(num % 10)
#             num = num // 10
            
#         return reversed(res)