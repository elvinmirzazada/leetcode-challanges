from collections import defaultdict

class Solution:
    def countAndSay(self, n: int) -> str:
        return self.rec_say(n)
        
    def rec_say(self, n: int):
        if n == 1:
            return "1"
        
        latest = list(self.rec_say(n-1))
        result = ''
        count = 0
        curr_elm = latest[0]
        for i in range(len(latest)):
            if latest[i] != curr_elm:
                result += f'{count}{curr_elm}'
                count = 1
                curr_elm = latest[i] 
            else:
                count += 1
                
            if i == len(latest) - 1:
                result += f'{count}{curr_elm}'
        
        return result