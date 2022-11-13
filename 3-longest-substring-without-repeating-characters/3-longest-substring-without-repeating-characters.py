class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub_set = set()
        start = 0
        
        for idx, ch in enumerate(list(s)):
            
            if ch not in sub_set:
                sub_set.add(ch)
                max_len = max(max_len, idx-start+1)
            else:
                while ch in sub_set:
                    sub_set.discard(s[start])
                    start += 1
                    
                sub_set.add(ch)
                # max_len = max(max_len, idx-start+1)
        return max_len