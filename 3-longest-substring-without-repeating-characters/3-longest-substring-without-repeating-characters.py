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
                while start < idx:
                    sub_set.discard(s[start])
                    if s[start] == s[idx]:
                        start += 1
                        break
                    else:
                        start += 1
                sub_set.add(ch)
                max_len = max(max_len, idx-start+1)
        return max_len