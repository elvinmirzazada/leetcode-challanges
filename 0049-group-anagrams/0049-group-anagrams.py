class Solution:
    def groupAnagrams(self, words: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        
        for word in words:
            count = [0] * 26
            
            for c in word:
                count[ord(c) - ord('a')] += 1
                
            result[tuple(count)].append(word)
            
            
        return result.values()
            