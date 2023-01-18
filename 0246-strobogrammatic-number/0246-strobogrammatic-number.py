class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        nums_dict = {
            "6": "9",
            "9": "6",
            "8": "8",
            "1": "1",
            "0": "0"
        }
        
        i, j = 0, len(num)-1
        
        while i <= j:
            if num[i] in nums_dict and nums_dict[num[i]] == num[j]:
                i += 1
                j -= 1
            else:
                return False
        
            
            
            
        return True