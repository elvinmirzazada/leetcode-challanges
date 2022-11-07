class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        
        p = 1
        curr_prod = x
        
        while n > 0:
            if n % 2:
                p = p * curr_prod
            curr_prod *= curr_prod
            n = n//2
        return p
        