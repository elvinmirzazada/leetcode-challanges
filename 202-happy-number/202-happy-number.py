class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n > 1:
            num_str = str(n)
            new_n = 0
            for c in num_str:
                new_n += int(c)**2
            if new_n in visited:
                break
            visited.add(new_n)
            n = new_n
        
        return n == 1