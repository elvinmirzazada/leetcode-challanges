class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = ''
        longest = 0    
        for ch in s:
            ind = 0
            i = 0
            while i < len(sub):
                if sub[i] == ch:
                    ind = i + 1
                    break
                
                i += 1
            
            sub = sub[ind:]+ch
            longest = max(longest, len(sub))
        
        return longest
    