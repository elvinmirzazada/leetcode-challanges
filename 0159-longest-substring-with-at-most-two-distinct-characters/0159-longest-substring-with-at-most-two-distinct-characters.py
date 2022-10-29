class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        chars = set()
        c_sub = 0
        for i in range(len(s)):
            len_sub = 0
            for j in range(i, len(s)):
                if s[j] in chars:
                    len_sub += 1
                    
                        
                else:
                    if len(chars) >= 2:
                        c_sub = max(c_sub, len_sub)
                        chars = set()
                        break
                    
                    chars.add(s[j])
                    len_sub += 1
                    
                if j == len(s)-1:
                    c_sub = max(c_sub, len_sub)
                    
        return (c_sub)           