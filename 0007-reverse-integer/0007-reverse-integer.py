class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        
        is_negative = x[0] == '-'
        number_str = ''
        
        i = len(x)-1
        end = 1 if is_negative else 0
        while i >= end:
            number_str += x[i]
            i -= 1  
            
        final_number = int(number_str)
        
        if final_number >= 2**31:
            return 0
        
        return final_number*-1 if is_negative else final_number
        