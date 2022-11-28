
from collections import defaultdict

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = [""]
        
        
        
        for idx, ch in enumerate(s):
            tmp = []
            if ch .isalpha():
                for res in result:
                    tmp.append(res+ch.lower())
                    tmp.append(res+ch.upper())
            else:
                for res in result:
                    tmp.append(res+ch)
                    
            result = tmp
            
        return result