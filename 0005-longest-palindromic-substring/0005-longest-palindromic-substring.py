class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 1
        result = s[0]
        while i < len(s):
            pal = s[i]
            j = i - 1
            k = i + 1
            
            while j >= 0 and k < len(s):
                if s[j] == s[k]:
                    pal = f"{s[j]}{pal}{s[k]}"
                    j -= 1
                    k += 1
                else:
                    break
            if len(pal) > len(result):
                result = pal
            i += 1
            
        i=1
        while i < len(s):
            if s[i-1] == s[i]:
                pal = s[i-1: i+1]
                j = i - 2
                k = i + 1

                while j >= 0 and k < len(s):
                    if s[j] == s[k]:
                        pal = f"{s[j]}{pal}{s[k]}"
                        j -= 1
                        k += 1
                    else:
                        break
                if len(pal) > len(result):
                    result = pal
            i += 1
            
        return result
    
    
    def check_pal(self, s):
        i, j = 0, len(s)-1
        
        while i < j:
            if s[i]!=s[j]:
                return False
            i += 1
            j -= 1
            
        return True