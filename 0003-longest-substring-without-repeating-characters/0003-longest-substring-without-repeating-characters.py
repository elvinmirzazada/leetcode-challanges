class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len, dup_set = 0, []
        i=0
        while i < len(s):
            # print(dup_set)
            if s[i] not in set(dup_set):
                dup_set.append(s[i])
            else:
                max_len = max(max_len, len(dup_set))
                while s[i] in set(dup_set):
                    dup_set = dup_set[1:]
                dup_set.append(s[i])
                
            i+=1
 
        max_len = max(max_len, len(dup_set))    
            
        return max_len