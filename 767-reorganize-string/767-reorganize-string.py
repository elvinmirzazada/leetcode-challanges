from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        freqs = defaultdict(int)
        
        for ch in s:
            freqs[ch] += 1
            
        result = [' '] * len(s)

        max_ch, max_freq = 0, 0
        for key, val in freqs.items():
            if val > max_freq:
                max_freq = val
                max_ch = key
                
        idx = 0
        while max_freq > 0:
            if idx >= len(s):
                return ""
            result[idx] = max_ch
            max_freq -= 1
            idx += 2
        
        del freqs[max_ch]
        if idx >= len(result):
            idx = 1
        for key, val in freqs.items():
            print(key, val, idx)
            while val > 0:
                result[idx] = key
                idx += 2
                val -= 1
                if idx >= len(s):
                    idx = 1
        return "".join(result)
        