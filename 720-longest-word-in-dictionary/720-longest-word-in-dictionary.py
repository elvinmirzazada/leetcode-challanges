class Solution:
    def longestWord(self, words: List[str]) -> str:
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c))
        print(words)
        ans = ''
        
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                if len(ans) < len(word):
                    ans = word
                    
        return ans