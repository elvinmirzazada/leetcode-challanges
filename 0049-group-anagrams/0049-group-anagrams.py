from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        def create_unique_key(word):
            alph = [0] * 26
            for ch in word:
                alph[ord(ch) - ord('a')] += 1
            
            return tuple(alph)
        
        for s in strs:
            key = create_unique_key(s)
            result[key].append(s)
            
        return result.values()