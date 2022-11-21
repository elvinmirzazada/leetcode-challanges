class Solution:
    def climbStairs(self, n: int) -> int:
        return self.dp_memo(n)
#         dp = [1] * n
#         if n > 1:
#             dp[1] = 2
        
#         for i in range(2, n):
#             dp[i] = dp[i-1] + dp[i-2]
        
#         return dp[-1]
    
    
    def dp_memo(self, n, memo={}):
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        if n in memo:
            return memo[n]
        
        memo[n] = self.dp_memo(n-1, memo) + self.dp_memo(n-2, memo)
        
        return memo[n]
    