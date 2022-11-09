

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        f_q, s_q = [], []
        for ch in s:
            if ch == '#':
                if f_q:
                    f_q.pop()
            else:
                f_q.append(ch)
                
        for ch in t:
            if ch == '#': 
                if s_q:
                    s_q.pop()
            else:
                s_q.append(ch)
        print(f_q, s_q)
        if len(f_q) != len(s_q):
            return False
        
        for i in range(len(s_q)):
            if f_q[i] != s_q[i]:
                return False
                
        return True