class Solution:
    def increasingTriplet(self, s: List[int]) -> bool:
        f_num = float('inf')
        s_num = float('inf')
        
        for n in s:
            if n <= f_num:
                f_num = n
            elif n <= s_num:
                s_num = n
            else:
                return True
        return False
                
                